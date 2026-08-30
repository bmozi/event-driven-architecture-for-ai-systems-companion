#!/usr/bin/env python3
"""Challenge the temporal protocol validator with disposable repository copies."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def protocol_path(repo: Path) -> Path:
    manifest = json.loads((repo / "companion.json").read_text(encoding="utf-8"))
    return repo / manifest["temporal_protocols"][0]


def load_protocol(repo: Path) -> dict:
    return json.loads(protocol_path(repo).read_text(encoding="utf-8"))


def write_protocol(repo: Path, protocol: dict) -> None:
    protocol_path(repo).write_text(
        json.dumps(protocol, indent=2) + "\n", encoding="utf-8"
    )
    refresh_packet_checksum(repo, protocol_path(repo))


def packet_manifest(repo: Path) -> Path:
    return protocol_path(repo).parent / "SHA256SUMS"


def refresh_packet_checksum(repo: Path, target: Path) -> None:
    manifest_path = packet_manifest(repo)
    relative = "./" + target.relative_to(manifest_path.parent).as_posix()
    replacement = f"{sha256(target)}  {relative}"
    lines = manifest_path.read_text(encoding="utf-8").splitlines()
    matched = False
    for index, line in enumerate(lines):
        if line.endswith(f"  {relative}"):
            lines[index] = replacement
            matched = True
            break
    if not matched:
        raise AssertionError(f"packet manifest has no entry for {relative}")
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_critical_document(repo: Path, relative: str, transform: Callable[[str], str]) -> None:
    protocol = load_protocol(repo)
    packet_dir = protocol_path(repo).parent
    target = packet_dir / relative
    original = target.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        raise AssertionError(f"mutation did not change {relative}")
    target.write_text(updated, encoding="utf-8")
    refresh_packet_checksum(repo, target)
    for item in protocol["critical_documents"]:
        if item["path"] == relative:
            item["sha256"] = sha256(target)
            break
    else:
        raise AssertionError(f"critical document not found: {relative}")
    write_protocol(repo, protocol)


def run_validator(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_repository.py"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def copied_repo(temp_root: Path, name: str) -> Path:
    target = temp_root / name
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    return target


def assert_rejected(
    name: str,
    mutation: Callable[[Path], None],
    expected: str,
) -> None:
    with tempfile.TemporaryDirectory(prefix=f"temporal-{name}-") as directory:
        repo = copied_repo(Path(directory), "repo")
        mutation(repo)
        result = run_validator(repo)
        output = result.stdout + result.stderr
        if result.returncode == 0:
            raise AssertionError(f"{name}: validator accepted forbidden mutation")
        if expected not in output:
            raise AssertionError(
                f"{name}: expected {expected!r} in validator output:\n{output}"
            )


def mutate_self_and_later_record(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["governing_manifest_members"] = [
        "governed_artifacts",
        "governing_manifest",
        "detached_verification_record",
    ]
    protocol["governing_manifest_excludes"] = []
    write_protocol(repo, protocol)


def mutate_reversed_order(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["causal_order"] = list(reversed(protocol["causal_order"]))
    write_protocol(repo, protocol)


def mutate_missing_next_release_triple(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["next_release_bindings"] = ["governed_artifacts"]
    write_protocol(repo, protocol)


def mutate_overwrite_permission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["correction_policy"]["allow_overwrite"] = True
    protocol["correction_policy"]["allow_same_filename"] = True
    protocol["correction_policy"]["required_new_identity"] = [
        "governing_manifest",
        "detached_verification_record",
    ]
    write_protocol(repo, protocol)


def mutate_stale_governed_field(repo: Path) -> None:
    protocol = load_protocol(repo)
    governed = protocol["governed_templates"][1]
    update_critical_document(
        repo,
        governed,
        lambda content: content + "\n- Freeze timestamp/timezone:\n",
    )


def mutate_incomplete_results_log(repo: Path) -> None:
    protocol = load_protocol(repo)
    relative = protocol["results_log"]
    label = protocol["release_chains"][4]["results_label"]
    update_critical_document(
        repo,
        relative,
        lambda content: "\n".join(
            line for line in content.splitlines() if not line.startswith(f"| {label} |")
        )
        + "\n",
    )


def mutate_version_mismatch(repo: Path) -> None:
    protocol = load_protocol(repo)
    relative = protocol["governed_templates"][0]
    expected = f"version {protocol['packet_version']}"
    update_critical_document(
        repo,
        relative,
        lambda content: content.replace(expected, "version 9.9.9", 1),
    )


def mutate_failed_verification_permission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["verification"]["must_succeed"] = False
    write_protocol(repo, protocol)


def mutate_missing_verification_output(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["verification"]["required_observation_fields"].remove("complete_output")
    write_protocol(repo, protocol)


def mutate_missing_attempt_identity(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["detached_record"]["required_fields"].remove("attempt_id")
    write_protocol(repo, protocol)


def mutate_record_chronology_permission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["detached_record"]["record_completion_must_follow_verification"] = False
    write_protocol(repo, protocol)


def mutate_undeclared_orchestration_permission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["participant_input_policy"]["undeclared_orchestration_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_missing_execution_event(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["execution_access_log"]["required_event_sequence"].remove(
        "GOVERNING_MANIFEST_VERIFIED"
    )
    write_protocol(repo, protocol)


def mutate_missing_execution_actor(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["execution_access_log"]["required_row_fields"].remove("actor")
    write_protocol(repo, protocol)


def mutate_record_template_omission(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/06-revised-artifact-freeze-record.md",
        lambda content: content.replace("- Complete observed command output:\n", "", 1),
    )


def mutate_unmanifested_byte(repo: Path) -> None:
    packet = protocol_path(repo).parent
    target = packet / "participant/02-scenario-and-task.md"
    target.write_text(
        target.read_text(encoding="utf-8") + "\nUNMANIFESTED CONTROL BYTE\n",
        encoding="utf-8",
    )


def main() -> int:
    baseline = run_validator(ROOT)
    if baseline.returncode != 0:
        sys.stderr.write(baseline.stdout + baseline.stderr)
        raise AssertionError("positive control: clean repository did not validate")

    cases = [
        (
            "self-and-later-record",
            mutate_self_and_later_record,
            "governing manifest must hash only governed artifacts",
        ),
        ("reversed-order", mutate_reversed_order, "invalid temporal causal order"),
        (
            "missing-next-release-triple",
            mutate_missing_next_release_triple,
            "next release must bind artifact, governing manifest, and detached record",
        ),
        (
            "overwrite-permission",
            mutate_overwrite_permission,
            "correction must forbid overwrite in place",
        ),
        (
            "stale-governed-field",
            mutate_stale_governed_field,
            "stale governed field",
        ),
        (
            "incomplete-results-log",
            mutate_incomplete_results_log,
            "results log missing release row",
        ),
        (
            "version-mismatch",
            mutate_version_mismatch,
            "packet ID/version mismatch",
        ),
        (
            "failed-verification-permission",
            mutate_failed_verification_permission,
            "manifest verification must succeed before release",
        ),
        (
            "missing-verification-output",
            mutate_missing_verification_output,
            "verification must capture exact command, complete output",
        ),
        (
            "missing-attempt-identity",
            mutate_missing_attempt_identity,
            "detached record must capture attempt, phase, actors",
        ),
        (
            "record-chronology-permission",
            mutate_record_chronology_permission,
            "record completion must follow manifest verification",
        ),
        (
            "undeclared-orchestration-permission",
            mutate_undeclared_orchestration_permission,
            "undeclared orchestration must be forbidden",
        ),
        (
            "missing-execution-event",
            mutate_missing_execution_event,
            "execution/access event sequence is incomplete or reordered",
        ),
        (
            "missing-execution-actor",
            mutate_missing_execution_actor,
            "execution/access log row fields are incomplete",
        ),
        (
            "record-template-omission",
            mutate_record_template_omission,
            "missing replay-control clause: - Complete observed command output:",
        ),
        (
            "checksum-control",
            mutate_unmanifested_byte,
            "checksum mismatch",
        ),
    ]
    for name, mutation, expected in cases:
        assert_rejected(name, mutation, expected)

    print(
        "temporal protocol mutation tests passed: "
        "1 clean positive control, 16 rejected mutations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
