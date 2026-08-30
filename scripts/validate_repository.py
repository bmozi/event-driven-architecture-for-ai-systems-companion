#!/usr/bin/env python3
"""Validate the companion repository's reader routes and local links."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "companion.json"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{7,40}$")
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")
PACKET_ID_PATTERN = re.compile(r"^\*\*Packet ID:\*\*\s*(\S+)\s*$", re.MULTILINE)
PACKET_VERSION_PATTERN = re.compile(r"^\*\*Version:\*\*\s*(\S+)\s*$", re.MULTILINE)
PACKET_HEADER_PATTERN = re.compile(
    r"^\*\*Packet:\*\*\s*(\S+)\s+version\s+(\S+)\s*$", re.MULTILINE
)
TEMPORAL_ORDER = [
    "completed_artifacts",
    "artifact_only_manifest",
    "successful_manifest_verification",
    "detached_verification_record",
    "next_release_manifest",
]
RELEASE_IDS = [
    "stage_a_initial",
    "stage_a_revised",
    "stage_a_handoff",
    "stage_b_section_1",
    "stage_b_section_2",
    "stage_b_sections_3_5",
]
RELEASE_STATES = {
    "stage_a_initial": "INITIAL COMPLETE",
    "stage_a_revised": "REVISED COMPLETE",
    "stage_a_handoff": "HANDOFF COMPLETE",
    "stage_b_section_1": "SECTION COMPLETE",
    "stage_b_section_2": "SECTION COMPLETE",
    "stage_b_sections_3_5": "SECTION COMPLETE",
}
MANIFEST_MEMBERS = ["governed_artifacts"]
MANIFEST_EXCLUSIONS = ["governing_manifest", "detached_verification_record"]
NEXT_RELEASE_BINDINGS = [
    "governed_artifacts",
    "governing_manifest",
    "detached_verification_record",
]
NEW_CORRECTION_IDENTITY = [
    "filename",
    "artifact_id",
    "version",
    "sha256",
    "governing_manifest",
    "detached_verification_record",
]
STALE_GOVERNED_FIELDS = [
    "- Revised freeze timestamp and timezone:",
    "- Detached freeze-record filename/hash:",
    "- Detached record confirms",
    "- Handoff freeze timestamp/timezone",
    "- Separate handoff freeze timestamp/timezone",
    "- Freeze timestamp/timezone:",
    "- Artifact ID/version and SHA-256:",
    "- Manifest reference:",
    "- Governing manifest filename/hash:",
]


def markdown_links(path: Path):
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_PATTERN.finditer(line):
            yield number, match.group(1).strip()


def local_target(source: Path, raw: str) -> Path | None:
    target = raw
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(" ", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None
    if decoded.startswith("/"):
        raise ValueError("absolute local path")
    resolved = (source.parent / decoded).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("link escapes repository") from exc
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def temporal_target(packet_dir: Path, raw: object, field: str, errors: list[str]) -> Path | None:
    if not isinstance(raw, str) or not raw:
        errors.append(f"temporal protocol: {field} must be a non-empty relative path")
        return None
    target = (packet_dir / raw).resolve()
    try:
        target.relative_to(packet_dir.resolve())
    except ValueError:
        errors.append(f"temporal protocol: {field} escapes packet directory: {raw}")
        return None
    return target


def validate_temporal_protocols(manifest: dict, errors: list[str]) -> int:
    configured = manifest.get("temporal_protocols", [])
    if not isinstance(configured, list) or not configured:
        errors.append("companion.json: temporal_protocols must be a non-empty list")
        return 0

    checked = 0
    for relative in configured:
        if not isinstance(relative, str) or not relative:
            errors.append("companion.json: temporal protocol path must be a non-empty string")
            continue
        protocol_path = (ROOT / relative).resolve()
        try:
            protocol_path.relative_to(ROOT)
        except ValueError:
            errors.append(f"temporal protocol escapes repository: {relative}")
            continue
        if not protocol_path.is_file():
            errors.append(f"missing temporal protocol: {relative}")
            continue
        try:
            protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid temporal protocol {relative}: {exc}")
            continue
        if not isinstance(protocol, dict):
            errors.append(f"{relative}: temporal protocol must be a JSON object")
            continue

        checked += 1
        prefix = f"{relative}:"
        packet_dir = protocol_path.parent
        packet_id = protocol.get("packet_id")
        packet_version = protocol.get("packet_version")
        if protocol.get("schema_version") != 1:
            errors.append(f"{prefix} schema_version must be 1")
        if not isinstance(packet_id, str) or not packet_id:
            errors.append(f"{prefix} packet_id must be a non-empty string")
        if not isinstance(packet_version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", packet_version):
            errors.append(f"{prefix} packet_version must use semantic versioning")

        if protocol.get("causal_order") != TEMPORAL_ORDER:
            errors.append(f"{prefix} invalid temporal causal order")
        if protocol.get("governing_manifest_members") != MANIFEST_MEMBERS:
            errors.append(f"{prefix} governing manifest must hash only governed artifacts")
        if protocol.get("governing_manifest_excludes") != MANIFEST_EXCLUSIONS:
            errors.append(
                f"{prefix} governing manifest must exclude itself and the later detached record"
            )
        verification = protocol.get("verification")
        if not isinstance(verification, dict):
            errors.append(f"{prefix} verification must be an object")
        else:
            if verification.get("must_succeed") is not True:
                errors.append(f"{prefix} manifest verification must succeed before release")
            if verification.get("observed_timestamp_timezone_required") is not True:
                errors.append(f"{prefix} verification must record observed timestamp/timezone")
        detached = protocol.get("detached_record")
        if not isinstance(detached, dict):
            errors.append(f"{prefix} detached_record must be an object")
        else:
            if detached.get("created_after") != "successful_manifest_verification":
                errors.append(f"{prefix} detached record must follow successful verification")
            if detached.get("excluded_from_described_manifest") is not True:
                errors.append(f"{prefix} later detached record must be excluded from its manifest")
            if detached.get("claims_self_hash") is not False:
                errors.append(f"{prefix} detached record must not claim its own hash")
        if protocol.get("next_release_bindings") != NEXT_RELEASE_BINDINGS:
            errors.append(
                f"{prefix} next release must bind artifact, governing manifest, and detached record"
            )

        correction = protocol.get("correction_policy")
        if not isinstance(correction, dict):
            errors.append(f"{prefix} correction_policy must be an object")
        else:
            if correction.get("preserve_prior_release") is not True:
                errors.append(f"{prefix} correction must preserve the prior release")
            if correction.get("allow_overwrite") is not False:
                errors.append(f"{prefix} correction must forbid overwrite in place")
            if correction.get("allow_same_filename") is not False:
                errors.append(f"{prefix} correction must require a new immutable filename")
            if correction.get("required_new_identity") != NEW_CORRECTION_IDENTITY:
                errors.append(
                    f"{prefix} correction must require new filename, ID, version, hash, manifest, and record"
                )

        critical = protocol.get("critical_documents")
        critical_paths: set[Path] = set()
        if not isinstance(critical, list) or not critical:
            errors.append(f"{prefix} critical_documents must be a non-empty list")
            critical = []
        for index, item in enumerate(critical):
            if not isinstance(item, dict):
                errors.append(f"{prefix} critical_documents[{index}] must be an object")
                continue
            path = temporal_target(packet_dir, item.get("path"), "critical document", errors)
            if path is None:
                continue
            critical_paths.add(path)
            if not path.is_file():
                errors.append(f"{prefix} missing critical document: {item.get('path')}")
                continue
            expected = item.get("sha256")
            if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                errors.append(f"{prefix} invalid critical-document SHA-256: {item.get('path')}")
            elif sha256(path) != expected:
                errors.append(f"{prefix} critical document hash mismatch: {item.get('path')}")

            content = path.read_text(encoding="utf-8")
            relative_to_packet = path.relative_to(packet_dir).as_posix()
            if relative_to_packet == "README.md":
                id_match = PACKET_ID_PATTERN.search(content)
                version_match = PACKET_VERSION_PATTERN.search(content)
                found_id = id_match.group(1) if id_match else None
                found_version = version_match.group(1) if version_match else None
            else:
                header_match = PACKET_HEADER_PATTERN.search(content)
                found_id = header_match.group(1) if header_match else None
                found_version = header_match.group(2) if header_match else None
            if found_id != packet_id or found_version != packet_version:
                errors.append(
                    f"{prefix} packet ID/version mismatch in {relative_to_packet}: "
                    f"expected {packet_id} {packet_version}, found {found_id} {found_version}"
                )

        packet_markdown = {
            path.resolve() for path in packet_dir.rglob("*.md") if path.is_file()
        }
        if critical_paths != packet_markdown:
            for missing in sorted(packet_markdown - critical_paths):
                errors.append(
                    f"{prefix} Markdown missing from critical_documents: "
                    f"{missing.relative_to(packet_dir)}"
                )
            for extra in sorted(critical_paths - packet_markdown):
                errors.append(
                    f"{prefix} critical document is not packet Markdown: "
                    f"{extra.relative_to(packet_dir)}"
                )

        governed_templates = protocol.get("governed_templates")
        if not isinstance(governed_templates, list) or not governed_templates:
            errors.append(f"{prefix} governed_templates must be a non-empty list")
            governed_templates = []
        for raw in governed_templates:
            path = temporal_target(packet_dir, raw, "governed template", errors)
            if path is None or not path.is_file():
                if path is not None:
                    errors.append(f"{prefix} missing governed template: {raw}")
                continue
            if path not in critical_paths:
                errors.append(f"{prefix} governed template is not a critical document: {raw}")
            content = path.read_text(encoding="utf-8")
            for stale in STALE_GOVERNED_FIELDS:
                if stale in content:
                    errors.append(f"{prefix} stale governed field in {raw}: {stale}")
            if re.search(r"-[A-Z]+-FREEZE-RECORD-v1\.md", content):
                errors.append(f"{prefix} stale freeze-record filename in {raw}")

        releases = protocol.get("release_chains")
        if not isinstance(releases, list):
            errors.append(f"{prefix} release_chains must be a list")
            releases = []
        release_ids = [item.get("id") for item in releases if isinstance(item, dict)]
        if release_ids != RELEASE_IDS:
            errors.append(f"{prefix} release_chains must contain all six releases in order")

        results_path = temporal_target(packet_dir, protocol.get("results_log"), "results_log", errors)
        inventory_path = temporal_target(
            packet_dir, protocol.get("static_inventory"), "static_inventory", errors
        )
        results_text = results_path.read_text(encoding="utf-8") if results_path and results_path.is_file() else ""
        inventory_text = (
            inventory_path.read_text(encoding="utf-8")
            if inventory_path and inventory_path.is_file()
            else ""
        )
        if results_path and not results_path.is_file():
            errors.append(f"{prefix} missing results log: {protocol.get('results_log')}")
        if inventory_path and not inventory_path.is_file():
            errors.append(f"{prefix} missing static inventory: {protocol.get('static_inventory')}")

        seen_artifacts: set[str] = set()
        seen_release_files: set[str] = set()
        for item in releases:
            if not isinstance(item, dict):
                errors.append(f"{prefix} release chain must be an object")
                continue
            release_id = item.get("id")
            label = item.get("results_label")
            artifacts = item.get("artifacts")
            if release_id not in RELEASE_STATES:
                continue
            if not isinstance(label, str) or not label:
                errors.append(f"{prefix} {release_id} requires results_label")
                continue
            if not isinstance(artifacts, list) or not artifacts:
                errors.append(f"{prefix} {release_id} requires governed artifacts")
                artifacts = []
            names: list[str] = []
            for artifact in artifacts:
                if not isinstance(artifact, dict):
                    errors.append(f"{prefix} {release_id} artifact must be an object")
                    continue
                name = artifact.get("filename")
                state = artifact.get("state")
                if not isinstance(name, str) or not name:
                    errors.append(f"{prefix} {release_id} artifact requires filename")
                    continue
                names.append(name)
                if state != RELEASE_STATES[release_id]:
                    errors.append(f"{prefix} {release_id} artifact has wrong complete state")
                if name in seen_artifacts:
                    errors.append(f"{prefix} artifact filename reused across releases: {name}")
                seen_artifacts.add(name)
            manifest_name = item.get("governing_manifest")
            record_name = item.get("detached_record")
            next_name = item.get("next_release_manifest")
            for field, value in [
                ("governing_manifest", manifest_name),
                ("detached_record", record_name),
                ("next_release_manifest", next_name),
            ]:
                if not isinstance(value, str) or not value:
                    errors.append(f"{prefix} {release_id} requires {field}")
                    continue
                if value in seen_release_files:
                    errors.append(f"{prefix} release evidence filename reused: {value}")
                seen_release_files.add(value)
            release_filenames = [
                *names,
                *[value for value in [manifest_name, record_name, next_name] if isinstance(value, str)],
            ]
            for doc_name, text in [("results log", results_text), ("static inventory", inventory_text)]:
                row = next(
                    (line for line in text.splitlines() if line.startswith(f"| {label} |")),
                    None,
                )
                if row is None:
                    errors.append(f"{prefix} {doc_name} missing release row: {label}")
                    continue
                for name in release_filenames:
                    if f"`{name}`" not in row:
                        errors.append(
                            f"{prefix} {doc_name} {label} row missing release file: {name}"
                        )
                if f"`{RELEASE_STATES[release_id]}`" not in row:
                    errors.append(
                        f"{prefix} {doc_name} {label} row missing complete state: "
                        f"{RELEASE_STATES[release_id]}"
                    )

    return checked


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print("missing companion.json", file=sys.stderr)
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid companion.json: {exc}", file=sys.stderr)
        return 1

    if manifest.get("schema_version") != 1:
        errors.append("companion.json: schema_version must be 1")
    if not COMMIT_PATTERN.fullmatch(str(manifest.get("source_commit", ""))):
        errors.append("companion.json: source_commit must be a 7-40 character Git hash")

    required = manifest.get("required_files")
    if not isinstance(required, list) or not required:
        errors.append("companion.json: required_files must be a non-empty list")
        required = []
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    checksum_manifests = manifest.get("checksum_manifests", [])
    if not isinstance(checksum_manifests, list):
        errors.append("companion.json: checksum_manifests must be a list")
        checksum_manifests = []
    checked_checksums = 0
    for relative in checksum_manifests:
        checksum_path = ROOT / relative
        if not checksum_path.is_file():
            errors.append(f"missing checksum manifest: {relative}")
            continue
        listed_targets: set[Path] = set()
        for number, line in enumerate(
            checksum_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = CHECKSUM_PATTERN.fullmatch(line)
            if not match:
                errors.append(f"{relative}:{number}: invalid SHA256SUMS line")
                continue
            expected, raw_target = match.groups()
            target = (checksum_path.parent / raw_target).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}:{number}: checksum target escapes repository")
                continue
            if not target.is_file():
                errors.append(f"{relative}:{number}: missing checksum target: {raw_target}")
                continue
            listed_targets.add(target)
            checked_checksums += 1
            if sha256(target) != expected:
                errors.append(f"{relative}:{number}: checksum mismatch: {raw_target}")
        packet_files = {
            path.resolve()
            for path in checksum_path.parent.rglob("*")
            if path.is_file()
            and path != checksum_path
            and "__pycache__" not in path.parts
        }
        for unlisted in sorted(packet_files - listed_targets):
            errors.append(
                f"{relative}: packet file missing from checksum manifest: "
                f"{unlisted.relative_to(checksum_path.parent)}"
            )

    checked_temporal_protocols = validate_temporal_protocols(manifest, errors)

    gateways = manifest.get("gateway_assets")
    if not isinstance(gateways, list) or not gateways:
        errors.append("companion.json: gateway_assets must be a non-empty list")
        gateways = []
    for gateway in gateways:
        relative = gateway.get("path", "")
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing gateway asset: {relative}")
            continue
        content = path.read_text(encoding="utf-8").casefold()
        phrases = [gateway.get("first_pass", ""), *gateway.get("required_language", [])]
        for phrase in phrases:
            if not phrase or phrase.casefold() not in content:
                errors.append(f"{relative}: missing required gateway language: {phrase!r}")
        for example in gateway.get("examples", []):
            if not (ROOT / example).is_file():
                errors.append(f"{relative}: missing comprehensive example: {example}")

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    checked_links = 0
    for source in markdown_files:
        for line, raw in markdown_links(source):
            try:
                target = local_target(source, raw)
            except ValueError as exc:
                errors.append(f"{source.relative_to(ROOT)}:{line}: {exc}: {raw}")
                continue
            if target is None:
                continue
            checked_links += 1
            if not target.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}:{line}: missing local link target: {raw}"
                )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"companion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(
        f"companion validation passed: {len(markdown_files)} Markdown files, "
        f"{checked_links} local links, {len(gateways)} gateway asset(s), "
        f"{checked_checksums} checksum(s), "
        f"{checked_temporal_protocols} temporal protocol(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
