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
TEMPORAL_SCHEMA_VERSION = 3
CURRENT_PACKET_VERSION = "1.2.5"
LIVE_UPDATE_FILENAME = "EVT-A-LIVE-UPDATE-v1.md"
LIVE_UPDATE_PATH = f"participant/{LIVE_UPDATE_FILENAME}"
REVISION_PHASE_ID = "stage_a_revision"
REVISION_PRIOR_RELEASE = "stage_a_initial"
REVISION_OPENS_RELEASE = "stage_a_revised"
REVISION_MANIFEST = "EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt"
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
VERIFICATION_OBSERVATION_FIELDS = [
    "exact_command",
    "complete_output",
    "exit_code",
    "timestamp",
    "timezone",
]
DETACHED_RECORD_FIELDS = [
    "attempt_id",
    "phase",
    "artifact_actor",
    "facilitator",
    "manifest_verifier",
    "exact_verification_command",
    "complete_observed_output",
    "exit_code",
    "verification_timestamp",
    "verification_timezone",
    "record_completing_actor",
    "record_completion_timestamp",
    "record_completion_timezone",
]
EXECUTION_EVENT_SEQUENCE = [
    "SEALED_INPUT_MANIFEST_CREATED",
    "SEALED_INPUT_MANIFEST_VERIFIED",
    "PHASE_GATE_OPENED",
    "FILE_OPENED_OR_ACCESS_ATTEMPT_RECORDED",
    "ARTIFACT_COMPLETED",
    "GOVERNING_MANIFEST_CREATED",
    "GOVERNING_MANIFEST_VERIFIED",
    "DETACHED_RECORD_COMPLETED",
    "NEXT_RELEASE_MANIFEST_CREATED",
    "NEXT_RELEASE_MANIFEST_VERIFIED",
    "NEXT_PHASE_GATE_OPENED",
]
EXECUTION_LOG_FIELDS = [
    "event_id",
    "prior_event_id",
    "phase",
    "event_type",
    "filename_or_surface",
    "actor",
    "facilitator",
    "timestamp",
    "timezone",
    "verification_command",
    "complete_observed_output",
    "exit_code",
    "continuity_binding",
    "outcome_or_deviation",
]
FORBIDDEN_INPUT_EXAMPLES = [
    "ORCHESTRATION.md",
    "run note",
    "hidden prompt",
    "facilitator file",
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
ENTRY_BRANCH_CONTRACT = {
    "selection": "exactly_one",
    "selection_event": "ENTRY_BRANCH_SELECTED",
    "selection_before_scored_input": True,
    "branch_mixing_stops_attempt": True,
    "human": {
        "template": "participant/01-consent-and-privacy.md",
        "stage_a_record_pattern": "EVT-A-HUMAN-CONSENT-<attempt-id>-v1.md",
        "stage_b_record_pattern": "EVT-B-HUMAN-CONSENT-<attempt-id>-v1.md",
        "stage_a_manifest_pattern": "EVT-A-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "stage_b_manifest_pattern": "EVT-B-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "required_state": "HUMAN CONSENT COMPLETE",
        "synthetic_context_forbidden": True,
    },
    "synthetic": {
        "template": "facilitator-only/06-synthetic-context-record-template.md",
        "record_pattern": "EVT-SYNTHETIC-CONTEXT-<attempt-id>-v1.md",
        "manifest_pattern": "EVT-SYNTHETIC-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "required_identity_statement": "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
        "required_state": "SYNTHETIC CONTEXT COMPLETE",
        "human_consent_record_forbidden": True,
        "human_result_claims_forbidden": [
            "human consent obtained",
            "participant consented",
            "human comprehension passed",
            "human usability passed",
            "practitioner result observed",
        ],
    },
    "stage_context_gates": {
        "stage_a": "selected_branch_record_and_manifest_verified_before_STAGE_A_STARTED",
        "stage_b": "same_selected_branch_record_and_manifest_verified_before_STAGE_B_STARTED",
    },
}
FULL_ROUTE_CONTRACT = {
    "scored_freeze_chain_ids": RELEASE_IDS,
    "six_scored_freezes_are_full_route_closure": False,
    "required_boundary_order": [
        "ENTRY_BRANCH_SELECTED", "ENTRY_CONTEXT_RECORD_COMPLETED", "RUN_LOG_STARTED",
        "STAGE_A_STARTED", "stage_a_initial", "stage_a_revised", "stage_a_handoff",
        "HANDOFF_LAYOUT_PROOF_COMPLETED", "STAGE_A_MATERIAL_FEEDBACK_COMPLETED",
        "STAGE_A_ENDED", "STAGE_B_STARTED", "stage_b_section_1",
        "stage_b_section_2", "stage_b_sections_3_5", "STAGE_B_SCORING_ENDED",
        "STAGE_B_SECTION_6_DEBRIEF_COMPLETED", "STAGE_B_ENDED",
        "RUN_RESULTS_COMPLETED", "RUN_LOG_CLOSED",
    ],
    "premature_log_close_forbidden": True,
}
DEBRIEF_CONTRACT = {
    "template": "participant/07-stage-b-section-6-debrief.md",
    "input_manifest": "EVT-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
    "output_filename": "EVT-B-SECTION-6-DEBRIEF-v1.md",
    "required_state": "SECTION 6 DEBRIEF COMPLETE",
    "completion_event": "STAGE_B_SECTION_6_DEBRIEF_COMPLETED",
    "after_event": "STAGE_B_SCORING_ENDED",
    "debrief_before_scoring_forbidden": True,
    "retroactive_score_or_artifact_change_forbidden": True,
}
RUN_RESULTS_CONTRACT = {
    "template": "facilitator-only/03-results-and-deviation-log.md",
    "filename_pattern": "EVT-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md",
    "required_state": "RUN RESULTS COMPLETE",
    "completion_event": "RUN_RESULTS_COMPLETED",
    "after_event": "STAGE_B_ENDED",
    "before_event": "RUN_LOG_CLOSED",
    "immutable_before_log_close": True,
    "final_pre_results_checkpoint_required": True,
    "forbidden_fields": [
        "final_closed_log_sha256", "predicted_future_log_hash",
        "predicted_future_closeout_timestamp",
    ],
}
EXTERNAL_CLOSEOUT_CONTRACT = {
    "template": "facilitator-only/08-external-closeout-record-template.md",
    "filename_pattern": "EVT-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md",
    "required_state": "EXTERNAL CLOSEOUT COMPLETE",
    "after_event": "RUN_LOG_CLOSED",
    "binds_results_sha256": True,
    "binds_closed_log_sha256": True,
    "binds_external_manifest_sha256": True,
    "external_to_closed_log": True,
}
LAYOUT_PROOF_CONTRACT = {
    "handoff_markdown": "EVT-A-ONE-SCREEN-HANDOFF-v1.md",
    "handoff_pdf": "EVT-A-ONE-SCREEN-HANDOFF-v1.pdf",
    "proof_template": "facilitator-only/07-handoff-layout-proof-record-template.md",
    "proof_filename_pattern": "EVT-A-HANDOFF-LAYOUT-PROOF-<attempt-id>-v1.md",
    "completion_event": "HANDOFF_LAYOUT_PROOF_COMPLETED",
    "page_count": 1,
    "page_size": "US Letter portrait",
    "minimum_margin_inches": 0.5,
    "minimum_font_points": 9,
    "maximum_reader_facing_words_excluding_labeled_provenance": 450,
    "clipping_forbidden": True,
    "overlap_forbidden": True,
    "favorable_one_page_claim_requires_pass_proof": True,
    "human_comprehension_evidence": False,
}
FORBIDDEN_FUTURE_BOUNDARY_FIELDS = [
    "Exact Stage A end timestamp/timezone",
    "STAGE_A_ENDED event ID",
    "Exact Stage B scoring-end timestamp/timezone",
    "STAGE_B_SCORING_ENDED event ID",
    "Exact Stage B end timestamp/timezone",
    "STAGE_B_ENDED event ID",
]
EVIDENCE_STATE_CONTRACT = {
    "human_pilot": "PREPARED/UNRUN",
    "human_comprehension": "UNRUN",
    "real_world": "UNRUN",
    "synthetic_may_not_upgrade_human_or_real_world_state": True,
}


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


def canonical_blockquote(content: str, start: str, end: str) -> str | None:
    if content.count(start) != 1 or content.count(end) != 1:
        return None
    _, remainder = content.split(start, 1)
    block, _ = remainder.split(end, 1)
    lines = block.strip("\n").splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    extracted: list[str] = []
    for line in lines:
        if line == ">":
            extracted.append("")
        elif line.startswith("> "):
            extracted.append(line[2:])
        else:
            return None
    return "\n".join(extracted) + "\n"


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
        if protocol.get("schema_version") != TEMPORAL_SCHEMA_VERSION:
            errors.append(
                f"{prefix} schema_version must be {TEMPORAL_SCHEMA_VERSION}"
            )
        if not isinstance(packet_id, str) or not packet_id:
            errors.append(f"{prefix} packet_id must be a non-empty string")
        if not isinstance(packet_version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", packet_version):
            errors.append(f"{prefix} packet_version must use semantic versioning")
        elif packet_version != CURRENT_PACKET_VERSION:
            errors.append(f"{prefix} packet_version must be {CURRENT_PACKET_VERSION}")

        closure_contracts = {
            "entry_branch_contract": ENTRY_BRANCH_CONTRACT,
            "full_route_contract": FULL_ROUTE_CONTRACT,
            "debrief_contract": DEBRIEF_CONTRACT,
            "run_results_contract": RUN_RESULTS_CONTRACT,
            "external_closeout_contract": EXTERNAL_CLOSEOUT_CONTRACT,
            "layout_proof_contract": LAYOUT_PROOF_CONTRACT,
            "governed_future_boundary_fields_forbidden": FORBIDDEN_FUTURE_BOUNDARY_FIELDS,
            "evidence_state_contract": EVIDENCE_STATE_CONTRACT,
        }
        for contract_name, expected_contract in closure_contracts.items():
            if protocol.get(contract_name) != expected_contract:
                errors.append(f"{prefix} {contract_name} mismatch")

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
            if verification.get("required_observation_fields") != VERIFICATION_OBSERVATION_FIELDS:
                errors.append(
                    f"{prefix} verification must capture exact command, complete output, "
                    "exit code, timestamp, and timezone"
                )
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
            if detached.get("required_fields") != DETACHED_RECORD_FIELDS:
                errors.append(
                    f"{prefix} detached record must capture attempt, phase, actors, "
                    "facilitator, complete verification evidence, and record completion"
                )
            if detached.get("record_completion_must_follow_verification") is not True:
                errors.append(
                    f"{prefix} detached record completion must follow manifest verification"
                )

        input_policy = protocol.get("participant_input_policy")
        if not isinstance(input_policy, dict):
            errors.append(f"{prefix} participant_input_policy must be an object")
        else:
            if input_policy.get("declared_route_files_only") is not True:
                errors.append(f"{prefix} participant input must contain declared route files only")
            if input_policy.get("undeclared_orchestration_forbidden") is not True:
                errors.append(f"{prefix} undeclared orchestration must be forbidden")
            if input_policy.get("forbidden_examples") != FORBIDDEN_INPUT_EXAMPLES:
                errors.append(f"{prefix} participant input forbidden examples are incomplete")

        execution_log = protocol.get("execution_access_log")
        if not isinstance(execution_log, dict):
            errors.append(f"{prefix} execution_access_log must be an object")
        else:
            if execution_log.get("path") != "facilitator-only/05-execution-and-access-log.md":
                errors.append(f"{prefix} execution/access log path is invalid")
            if execution_log.get("facilitator_only") is not True:
                errors.append(f"{prefix} execution/access log must be facilitator-only")
            if execution_log.get("excluded_from_participant_input") is not True:
                errors.append(f"{prefix} execution/access log must be excluded from participant input")
            if execution_log.get("continuity_binding_required") is not True:
                errors.append(f"{prefix} execution/access continuity binding is required")
            if execution_log.get("required_event_sequence") != EXECUTION_EVENT_SEQUENCE:
                errors.append(f"{prefix} execution/access event sequence is incomplete or reordered")
            if execution_log.get("required_row_fields") != EXECUTION_LOG_FIELDS:
                errors.append(f"{prefix} execution/access log row fields are incomplete")
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

        revision_input = protocol.get("revision_phase_input")
        live_update_relative: str | None = None
        live_update_path: Path | None = None
        if not isinstance(revision_input, dict):
            errors.append(f"{prefix} revision_phase_input must be an object")
            revision_input = {}
        else:
            if revision_input.get("id") != REVISION_PHASE_ID:
                errors.append(f"{prefix} revision phase input has invalid identity")
            if revision_input.get("prior_release") != REVISION_PRIOR_RELEASE:
                errors.append(f"{prefix} revision phase input must bind stage_a_initial")
            if revision_input.get("opens_release") != REVISION_OPENS_RELEASE:
                errors.append(f"{prefix} revision phase input must open stage_a_revised")
            if revision_input.get("manifest") != REVISION_MANIFEST:
                errors.append(
                    f"{prefix} revision phase input manifest must be {REVISION_MANIFEST}"
                )
            if revision_input.get("manifest_verified_before_open") is not True:
                errors.append(
                    f"{prefix} revision phase manifest must verify before live-update open"
                )

            live_update = revision_input.get("immutable_participant_input")
            if not isinstance(live_update, dict):
                errors.append(
                    f"{prefix} immutable live-update participant input must be an object"
                )
            else:
                if live_update.get("filename") != LIVE_UPDATE_FILENAME:
                    errors.append(
                        f"{prefix} immutable live-update filename must be "
                        f"{LIVE_UPDATE_FILENAME}"
                    )
                if live_update.get("path") != LIVE_UPDATE_PATH:
                    errors.append(
                        f"{prefix} immutable live-update path must be {LIVE_UPDATE_PATH}"
                    )
                live_update_relative = live_update.get("path")
                live_update_path = temporal_target(
                    packet_dir,
                    live_update_relative,
                    "immutable live-update participant input",
                    errors,
                )
                live_hash = live_update.get("sha256")
                if not isinstance(live_hash, str) or not re.fullmatch(
                    r"[0-9a-f]{64}", live_hash
                ):
                    errors.append(f"{prefix} invalid immutable live-update SHA-256")
                elif (
                    live_update_path
                    and live_update_path.is_file()
                    and sha256(live_update_path) != live_hash
                ):
                    errors.append(
                        f"{prefix} immutable live-update participant input hash mismatch"
                    )
                if live_update_path and not live_update_path.is_file():
                    errors.append(
                        f"{prefix} missing immutable live-update participant input: "
                        f"{LIVE_UPDATE_PATH}"
                    )

                canonical_source = live_update.get("canonical_facilitator_source")
                if canonical_source != "facilitator-only/01-facilitator-guide.md":
                    errors.append(
                        f"{prefix} immutable live-update canonical source is invalid"
                    )
                canonical_path = temporal_target(
                    packet_dir,
                    canonical_source,
                    "live-update canonical facilitator source",
                    errors,
                )
                start_marker = live_update.get("canonical_start_marker")
                end_marker = live_update.get("canonical_end_marker")
                if not isinstance(start_marker, str) or not start_marker:
                    errors.append(f"{prefix} live-update canonical start marker is missing")
                if not isinstance(end_marker, str) or not end_marker:
                    errors.append(f"{prefix} live-update canonical end marker is missing")
                if (
                    canonical_path
                    and canonical_path.is_file()
                    and live_update_path
                    and live_update_path.is_file()
                    and isinstance(start_marker, str)
                    and isinstance(end_marker, str)
                ):
                    canonical = canonical_blockquote(
                        canonical_path.read_text(encoding="utf-8"),
                        start_marker,
                        end_marker,
                    )
                    if canonical is None:
                        errors.append(
                            f"{prefix} canonical facilitator live-update block is missing "
                            "or malformed"
                        )
                    elif live_update_path.read_text(encoding="utf-8") != canonical:
                        errors.append(
                            f"{prefix} immutable live-update participant input differs "
                            "from canonical facilitator wording"
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
            elif relative_to_packet == live_update_relative:
                found_id = packet_id
                found_version = packet_version
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
        if live_update_path is not None and live_update_path not in critical_paths:
            errors.append(f"{prefix} live-update input is not a critical document")

        required_document_clauses = {
            "README.md": [
                "auditable facilitator-side execution history",
                "exact manifest-verification command/output/exit/time/timezone",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "revision-phase input manifest must hash it",
                "`ORCHESTRATION.md`",
                "execution and access log",
                "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
                "six scored freeze chains",
                "US Letter",
                "RUN_RESULTS_COMPLETED",
                "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            ],
            "participant/00-packet-route.md": [
                "For every detached verification record named below",
                "exact verification command",
                "complete observed output",
                "later record-completion timestamp and timezone",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "After that revision-phase input manifest verifies",
                "`ORCHESTRATION.md`",
                "debrief before scoring ends is forbidden",
                "Do not put or predict those future end fields",
                "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            ],
            "participant/06-revised-artifact-freeze-record.md": [
                "- Attempt ID:",
                "- Stage and phase:",
                "- Artifact-producing actor code:",
                "- Facilitator name/code:",
                "- Exact manifest verification command:",
                "- Complete observed command output:",
                "- Observed command exit code:",
                "- Observed manifest verification timestamp:",
                "- Observed manifest verification timezone:",
                "- Record-completing actor name/code:",
                "- Record completion timestamp, explicitly later than manifest verification:",
                "- Record completion timezone:",
            ],
            "facilitator-only/01-facilitator-guide.md": [
                "execution and access log",
                "every manifest gate, file open or attempted access, artifact completion",
                "exact verification command, complete observed output, exit code",
                "explicit later record-completion timestamp and timezone",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "Only after that manifest verifies",
                "undeclared `ORCHESTRATION.md`",
                "STAGE_A_ENDED",
                "STAGE_B_SCORING_ENDED",
                "RUN_RESULTS_COMPLETED",
                "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            ],
            "facilitator-only/02-observation-and-scoring-rubric.md": [
                "Detached-record replay identity",
                "Execution/access continuity",
                "Revision-phase input integrity",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "participant input contains no undeclared orchestration or facilitator file",
                "Entry-branch integrity",
                "Literal one-page proof",
                "Full-route closure",
            ],
            "facilitator-only/03-results-and-deviation-log.md": [
                "Facilitator execution/access log exact filename and SHA-256",
                "Declared participant-input inventory matches item by item",
                "Detached-record required-field audit",
                "Complete observed output",
                "Later record-completion timestamp/timezone",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "RUN RESULTS COMPLETE",
                "Full-route boundary checkpoints",
                "Real-world evidence state: `UNRUN`",
                "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            ],
            "facilitator-only/04-temporal-freeze-protocol-and-record-templates.md": [
                "- Attempt ID:",
                "- Stage and phase:",
                "- Exact manifest-verification command:",
                "- Complete observed command output:",
                "- Observed command exit code:",
                "- Record completion timestamp, explicitly later than verification:",
                "- Record completion timezone:",
                "Revision-phase sealed-input inventory",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "Six freezes versus full-route closure",
                "governed/scored workbooks must not contain future",
                "Any blank required field prevents `FROZEN`",
            ],
            "facilitator-only/05-execution-and-access-log.md": [
                "Keep this log outside every sealed participant input",
                "SEALED_INPUT_MANIFEST_CREATED",
                "GOVERNING_MANIFEST_VERIFIED",
                "DETACHED_RECORD_COMPLETED",
                "NEXT_PHASE_GATE_OPENED",
                "Complete observed output",
                "Continuity binding",
                "`EVT-A-LIVE-UPDATE-v1.md`",
                "STAGE_B_SCORING_ENDED",
                "RUN_LOG_CLOSED",
                "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            ],
            "facilitator-only/06-synthetic-context-record-template.md": [
                "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
                "SYNTHETIC CONTEXT COMPLETE",
                "Human consent state",
            ],
            "facilitator-only/07-handoff-layout-proof-record-template.md": [
                "US Letter portrait",
                "0.5 inch",
                "9 points",
                "450",
                "Layout proof is not comprehension evidence.",
            ],
            "facilitator-only/08-external-closeout-record-template.md": [
                "EXTERNAL CLOSEOUT COMPLETE",
                "Run-results SHA-256",
                "Active closed-log SHA-256",
            ],
            "participant/07-stage-b-section-6-debrief.md": [
                "STAGE_B_SCORING_ENDED",
                "EVT-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
                "SECTION 6 DEBRIEF COMPLETE",
            ],
        }
        for document, clauses in required_document_clauses.items():
            document_path = packet_dir / document
            if not document_path.is_file():
                errors.append(f"{prefix} missing required protocol document: {document}")
                continue
            normalized_document = re.sub(
                r"\s+", " ", document_path.read_text(encoding="utf-8")
            ).casefold()
            for clause in clauses:
                normalized_clause = re.sub(r"\s+", " ", clause).casefold()
                if normalized_clause not in normalized_document:
                    errors.append(
                        f"{prefix} {document} missing replay-control clause: {clause}"
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
            for future_field in FORBIDDEN_FUTURE_BOUNDARY_FIELDS:
                if future_field in content:
                    errors.append(
                        f"{prefix} future end field forbidden in governed template "
                        f"{raw}: {future_field}"
                    )
            if re.search(r"-[A-Z]+-FREEZE-RECORD-v1\.md", content):
                errors.append(f"{prefix} stale freeze-record filename in {raw}")

        releases = protocol.get("release_chains")
        if not isinstance(releases, list):
            errors.append(f"{prefix} release_chains must be a list")
            releases = []
        release_ids = [item.get("id") for item in releases if isinstance(item, dict)]
        if release_ids != RELEASE_IDS:
            errors.append(f"{prefix} release_chains must contain all six releases in order")

        release_map = {
            item.get("id"): item for item in releases if isinstance(item, dict)
        }
        initial_release = release_map.get(REVISION_PRIOR_RELEASE)
        if isinstance(initial_release, dict):
            initial_artifacts = initial_release.get("artifacts")
            initial_names: list[str] = []
            if isinstance(initial_artifacts, list):
                initial_names = [
                    artifact.get("filename")
                    for artifact in initial_artifacts
                    if isinstance(artifact, dict)
                    and isinstance(artifact.get("filename"), str)
                ]
            expected_revision_members = [
                *initial_names,
                initial_release.get("governing_manifest"),
                initial_release.get("detached_record"),
                LIVE_UPDATE_FILENAME,
            ]
            if revision_input.get("manifest") != initial_release.get(
                "next_release_manifest"
            ):
                errors.append(
                    f"{prefix} revision phase manifest is not bound to "
                    "stage_a_initial next release"
                )
            if revision_input.get("required_members") != expected_revision_members:
                errors.append(
                    f"{prefix} revision phase input must bind exact prior release "
                    "and immutable live-update members"
                )
            if initial_release.get("next_release_additional_inputs") != [
                LIVE_UPDATE_FILENAME
            ]:
                errors.append(
                    f"{prefix} stage_a_initial next release must declare exact "
                    "immutable live-update input"
                )
        else:
            errors.append(f"{prefix} revision phase prior release is missing")

        final_release = release_map.get("stage_b_sections_3_5")
        if not isinstance(final_release, dict) or final_release.get(
            "next_release_additional_inputs"
        ) != ["07-stage-b-section-6-debrief.md"]:
            errors.append(
                f"{prefix} final scored release must bind the exact Section 6 debrief input"
            )

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
            additional_inputs = item.get("next_release_additional_inputs", [])
            if not isinstance(additional_inputs, list) or not all(
                isinstance(value, str) and value for value in additional_inputs
            ):
                errors.append(
                    f"{prefix} {release_id} next_release_additional_inputs must "
                    "be a list of filenames"
                )
                additional_inputs = []
            if (
                release_id != REVISION_PRIOR_RELEASE
                and LIVE_UPDATE_FILENAME in additional_inputs
            ):
                errors.append(
                    f"{prefix} immutable live update is bound to the wrong release: "
                    f"{release_id}"
                )
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
                *additional_inputs,
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
    if manifest.get("reader_value_packet_version") != CURRENT_PACKET_VERSION:
        errors.append(
            f"companion.json: reader_value_packet_version must be {CURRENT_PACKET_VERSION}"
        )
    if manifest.get("human_evidence_state") != "PREPARED/UNRUN":
        errors.append("companion.json: human evidence state must remain PREPARED/UNRUN")
    if manifest.get("real_world_evidence_state") != "UNRUN":
        errors.append("companion.json: real-world evidence state must remain UNRUN")

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
