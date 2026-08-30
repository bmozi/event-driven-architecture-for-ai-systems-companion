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


def mutate_live_update_member_omission(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["required_members"].remove(
        "EVT-A-LIVE-UPDATE-v1.md"
    )
    write_protocol(repo, protocol)


def mutate_live_update_rename(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["immutable_participant_input"][
        "filename"
    ] = "EVT-A-LIVE-UPDATE-renamed-v1.md"
    write_protocol(repo, protocol)


def mutate_live_update_unbound(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["revision_phase_input"]["opens_release"] = "stage_a_handoff"
    write_protocol(repo, protocol)


def mutate_route_live_update_omission(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/00-packet-route.md",
        lambda content: content.replace(
            "`EVT-A-LIVE-UPDATE-v1.md`", "the live-update file"
        ),
    )


def mutate_live_update_wording_drift(repo: Path) -> None:
    protocol = load_protocol(repo)
    relative = protocol["revision_phase_input"]["immutable_participant_input"][
        "path"
    ]
    packet_dir = protocol_path(repo).parent
    target = packet_dir / relative
    original = target.read_text(encoding="utf-8")
    updated = original.replace(
        "six risk events,\nsix carrier requests, six reservations",
        "six risk events,\nsix carrier requests, five reservations",
    )
    if updated == original:
        raise AssertionError("live-update wording mutation did not change input")
    target.write_text(updated, encoding="utf-8")
    refresh_packet_checksum(repo, target)
    updated_hash = sha256(target)
    protocol["revision_phase_input"]["immutable_participant_input"][
        "sha256"
    ] = updated_hash
    for item in protocol["critical_documents"]:
        if item["path"] == relative:
            item["sha256"] = updated_hash
            break
    else:
        raise AssertionError("live-update critical document not found")
    write_protocol(repo, protocol)


def mutate_missing_entry_branch(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("entry_branch_contract")
    write_protocol(repo, protocol)


def mutate_mixed_entry_branches(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["entry_branch_contract"]["selection"] = "one_or_more"
    write_protocol(repo, protocol)


def mutate_synthetic_human_claim(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["entry_branch_contract"]["synthetic"][
        "human_result_claims_forbidden"
    ].remove("human comprehension passed")
    write_protocol(repo, protocol)


def mutate_missing_boundary(boundary: str):
    def mutation(repo: Path) -> None:
        protocol = load_protocol(repo)
        protocol["full_route_contract"]["required_boundary_order"].remove(boundary)
        write_protocol(repo, protocol)

    return mutation


def mutate_debrief_before_scoring(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["debrief_contract"]["after_event"] = "STAGE_B_STARTED"
    protocol["debrief_contract"]["debrief_before_scoring_forbidden"] = False
    write_protocol(repo, protocol)


def mutate_unbound_debrief_input(repo: Path) -> None:
    protocol = load_protocol(repo)
    final = next(
        item for item in protocol["release_chains"]
        if item["id"] == "stage_b_sections_3_5"
    )
    final.pop("next_release_additional_inputs")
    write_protocol(repo, protocol)


def mutate_premature_close(repo: Path) -> None:
    protocol = load_protocol(repo)
    order = protocol["full_route_contract"]["required_boundary_order"]
    order.remove("RUN_LOG_CLOSED")
    order.insert(order.index("RUN_RESULTS_COMPLETED"), "RUN_LOG_CLOSED")
    write_protocol(repo, protocol)


def mutate_predicted_future_hash(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["run_results_contract"]["forbidden_fields"].remove(
        "predicted_future_log_hash"
    )
    write_protocol(repo, protocol)


def mutate_missing_external_closeout(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol.pop("external_closeout_contract")
    write_protocol(repo, protocol)


def mutate_favorable_layout_without_proof(repo: Path) -> None:
    protocol = load_protocol(repo)
    protocol["layout_proof_contract"][
        "favorable_one_page_claim_requires_pass_proof"
    ] = False
    write_protocol(repo, protocol)


def mutate_future_end_field(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/03-practitioner-workbook.md",
        lambda content: content + "\n- Exact Stage A end timestamp/timezone:\n",
    )


def mutate_route_branch_after_run_start(repo: Path) -> None:
    update_critical_document(
        repo,
        "participant/00-packet-route.md",
        lambda content: content.replace(
            "ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
            "RUN_LOG_STARTED -> ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED",
            1,
        ),
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
        (
            "live-update-member-omission",
            mutate_live_update_member_omission,
            "revision phase input must bind exact prior release and immutable live-update members",
        ),
        (
            "live-update-rename",
            mutate_live_update_rename,
            "immutable live-update filename must be EVT-A-LIVE-UPDATE-v1.md",
        ),
        (
            "live-update-unbound",
            mutate_live_update_unbound,
            "revision phase input must open stage_a_revised",
        ),
        (
            "route-live-update-omission",
            mutate_route_live_update_omission,
            "missing replay-control clause: `EVT-A-LIVE-UPDATE-v1.md`",
        ),
        (
            "live-update-wording-drift",
            mutate_live_update_wording_drift,
            "immutable live-update participant input differs from canonical facilitator wording",
        ),
        (
            "missing-entry-branch",
            mutate_missing_entry_branch,
            "entry_branch_contract mismatch",
        ),
        (
            "mixed-entry-branches",
            mutate_mixed_entry_branches,
            "entry_branch_contract mismatch",
        ),
        (
            "synthetic-human-claim",
            mutate_synthetic_human_claim,
            "entry_branch_contract mismatch",
        ),
        *[
            (
                f"missing-boundary-{boundary.lower()}",
                mutate_missing_boundary(boundary),
                "full_route_contract mismatch",
            )
            for boundary in (
                "STAGE_A_STARTED",
                "STAGE_A_ENDED",
                "STAGE_B_STARTED",
                "STAGE_B_SCORING_ENDED",
                "STAGE_B_SECTION_6_DEBRIEF_COMPLETED",
                "STAGE_B_ENDED",
                "RUN_RESULTS_COMPLETED",
            )
        ],
        (
            "debrief-before-scoring",
            mutate_debrief_before_scoring,
            "debrief_contract mismatch",
        ),
        (
            "unbound-debrief-input",
            mutate_unbound_debrief_input,
            "final scored release must bind the exact Section 6 debrief input",
        ),
        (
            "premature-log-close",
            mutate_premature_close,
            "full_route_contract mismatch",
        ),
        (
            "predicted-future-log-hash",
            mutate_predicted_future_hash,
            "run_results_contract mismatch",
        ),
        (
            "missing-external-closeout",
            mutate_missing_external_closeout,
            "external_closeout_contract mismatch",
        ),
        (
            "favorable-layout-without-proof",
            mutate_favorable_layout_without_proof,
            "layout_proof_contract mismatch",
        ),
        (
            "future-end-field-in-governed-workbook",
            mutate_future_end_field,
            "future end field forbidden in governed template",
        ),
        (
            "route-branch-after-run-start",
            mutate_route_branch_after_run_start,
            "missing replay-control clause: ENTRY_BRANCH_SELECTED -> "
            "ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED",
        ),
    ]
    for name, mutation, expected in cases:
        assert_rejected(name, mutation, expected)

    print(
        "temporal protocol mutation tests passed: "
        f"1 clean positive control, {len(cases)} rejected mutations "
        "(21 preserved plus closure mutations)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
