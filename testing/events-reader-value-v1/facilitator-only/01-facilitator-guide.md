# Facilitator Guide

**Packet:** EVT-RV-PILOT-001 version 1.2.5
**Status:** Facilitator-only; prepared and unrun

**Revision note:** Version 1.2.5 preserves v1.2.4's exact immutable live-update
binding and adds full-route closure; it has no human validation.

## Purpose

Test the materials, not the participants. Observe whether the reader-value
layer supports a practitioner event decision and an independent decision-owner
read-back.

## Recommended timing

### Stage A — 70 to 85 minutes

- consent and setup: 5 minutes;
- scenario and recognition questions: 10 minutes;
- meaning-and-authority record: 25 minutes;
- multiplier and loop review: 20 minutes;
- live update and revision: 10 minutes; and
- handoff and feedback: 10 minutes.

### Stage B — 35 to 50 minutes

- independent read-back: 15 minutes;
- executive brief and value ledger review: 10 minutes;
- bounded decision: 10 minutes; and
- debrief: 5 to 15 minutes.

Time is evidence, not a speed target.

## Required capture

For each participant, record setup start before the consent notice is first
opened. Obtain consent, then record the exact stage start immediately before
the route is opened. Record the exact file-open order, each pause or question,
and every intervention with time and level. Do not reconstruct these from
memory after the session.

Maintain the facilitator-only
[`execution and access log`](05-execution-and-access-log.md) item by item. Log
every manifest gate, file open or attempted access, artifact completion,
manifest creation, manifest verification, detached-record completion, and next
phase open with exact actor, facilitator, timestamp, timezone, filename, and
continuity binding.

## Select exactly one entry branch

Before run start, enforce
`ENTRY_BRANCH_SELECTED -> ENTRY_CONTEXT_RECORD_COMPLETED -> RUN_LOG_STARTED`.
Select `human` or `synthetic`.
Human runs use distinct Stage A/B consent records and exact human-context
manifests. Synthetic runs use
`EVT-SYNTHETIC-CONTEXT-<attempt-id>-v1.md` from the synthetic template with
`SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA`; never fill the human form or
claim human behavior/results. Missing selection or branch mixing stops the
attempt. Verify the selected context before run start and each stage checkpoint.

## Sealed flat delivery and manifest rule

Before each stage, copy only the approved exact files into a new sealed flat
input. Preserve every literal local filename named by the packet route. Create
and verify a run-specific delivery manifest before scored work and log each
later staged release. A manifest hashes other files; it never lists or hashes
itself. Do not rely on repository-relative paths.

Reject any participant input containing an undeclared `ORCHESTRATION.md`, run
note, hidden prompt, facilitator file, or other extra control file. Keep all
facilitation outside the sealed participant surface and prove the declared
inventory item by item in the external access log.

Every freeze uses four ordered operations: finish artifact bytes with
ID/version, completion timestamp/timezone, and complete pre-hash state; create
a manifest that hashes only those artifacts; verify it and observe the exact
verification timestamp/timezone; then create a detached record of that observed
event. The record is later than, and excluded from, the manifest it describes.
The next phase's sealed input manifest hashes the artifacts, governing manifest,
and detached record. Never require an artifact, manifest, or record to contain
its own hash or a future verification time.

Every detached record must contain attempt ID, stage/phase,
artifact-producing actor, facilitator, manifest verifier, exact verification
command, complete observed output, exit code, observed verification timestamp
and timezone, record-completing actor, and an explicit later record-completion
timestamp and timezone. Missing evidence prevents `FROZEN`.

The planned live update creates the first revised set. It is not a correction
of already frozen revised bytes. A later correction must preserve the old
artifact and create exact new immutable filename, ID/version, hash, reason,
correction timestamp/timezone, replacement detached verification record, and
replacement manifest. Never overwrite or reuse the old filename.

## No-coaching rule

During scored work, the facilitator may repeat written text or resolve file
access. Do not name the preferred facts, assign declarer authority, calculate
the multiplier, identify the loop, supply a budget, or confirm an answer.
Record every intervention.

## Stage A sequence

1. Confirm consent and freeze identity. Record Stage A start before opening the
   participant route.
2. Follow the route exactly. Supply the scenario and workbook only, then let the
   participant complete Section 1 before opening companion assets.
3. Supply only the four listed assets in the packet README, in order. The
   Northbridge miniature embedded in the supplied record and generic examples
   already visible in supplied files are allowed; do not allow linked
   comprehensive or completed examples.
4. Complete the initial workbook and detailed artifacts as
   `EVT-A-INITIAL-WORKBOOK-v1.md`,
   `EVT-A-INITIAL-MEANING-AUTHORITY-v1.md`,
   `EVT-A-INITIAL-MULTIPLIER-v1.md`, and
   `EVT-A-INITIAL-LOOP-CHECK-v1.md`, each with ID/version, completion
   timestamp/timezone, and `INITIAL COMPLETE` state. Hash only those completed
   artifacts in `EVT-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`, verify it, and
   then create `EVT-A-INITIAL-FREEZE-VERIFICATION-v1.md`. Before the update,
   verify `EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` over the artifacts,
   governing manifest, detached record, and exact immutable
   `EVT-A-LIVE-UPDATE-v1.md`.
5. Only after that manifest verifies, open `EVT-A-LIVE-UPDATE-v1.md` and read
   its update exactly. Do not deliver the update from memory or substitute a
   verbal, renamed, regenerated, summarized, omitted, or unmanifested copy.

<!-- EVT-A-LIVE-UPDATE-v1 CANONICAL START -->
> The same high-temperature reading was delivered three times. Two workers each
> produced `ShipmentAtRisk`, and every event triggered a carrier request, stock
> reservation, provisional credit, service case, and notification job. One
> carrier request was accepted but not decided. Its proposed `ShipmentRerouted`
> event caused the store to be told a replacement was coming. A late route
> update triggered the risk service again. Pine Hollow now has six risk events,
> six carrier requests, six reservations, and no verified reroute, replacement,
> or stop owner.
<!-- EVT-A-LIVE-UPDATE-v1 CANONICAL END -->

6. Ask only: “What can each party safely say or do now, and what changes in
   your artifacts?”
7. Let the participant revise the workbook, meaning/authority record,
   multiplier, and loop check. Require exactly
   `EVT-A-REVISED-WORKBOOK-v1.md`,
   `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`,
   `EVT-A-REVISED-MULTIPLIER-v1.md`, and
   `EVT-A-REVISED-LOOP-CHECK-v1.md`, each with artifact ID, version,
   completion timestamp/timezone, and pre-hash state `REVISED COMPLETE`.
8. Remove every `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank,
   or equivalent incomplete state, and reject a premature artifact
   self-declaration of `FROZEN`. Create
   `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`; it hashes the four details and
   does not hash itself.
9. Verify that governing manifest and observe the exact verification
   timestamp/timezone. Only then complete
   `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` with the observed event, literal
   filenames, IDs/versions, completion metadata, artifact hashes, and governing
   manifest filename/hash. Do not add this later record to the manifest it
   describes.
10. Verify a handoff-phase input manifest that hashes the four revised
    artifacts, governing manifest, and detached record. Only then supply
    `05-one-screen-handoff.md`. Ensure its inventory matches, complete it as
    `EVT-A-ONE-SCREEN-HANDOFF-v1.md` with ID/version, completion
    timestamp/timezone, and `HANDOFF COMPLETE`, hash only that completed handoff
    in `EVT-A-HANDOFF-SHA256SUMS-v1.txt`, verify the manifest, and then create
    `EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md`.
11. Preserve initial, revised, record, manifest, and handoff bytes without
    alteration.
12. Render the exact handoff as `EVT-A-ONE-SCREEN-HANDOFF-v1.pdf` and complete
    `EVT-A-HANDOFF-LAYOUT-PROOF-<attempt-id>-v1.md`. PASS requires one US
    Letter portrait page, margins >=0.5 inch, text >=9 points, <=450 reader-
    facing words excluding only labeled provenance, and no clipping, overlap,
    hidden overflow, or unreadable shrinking. It is not comprehension proof.
13. Complete material feedback and append
    `STAGE_A_MATERIAL_FEEDBACK_COMPLETED`, then `STAGE_A_ENDED`. Do not place
    or predict these future end facts in an earlier governed artifact.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact, obtain separate
   consent, verify the phase-1 input manifest over the handoff, its governing
   manifest, and detached verification record, and record exact Stage B start
   and timezone before opening the route.
2. Supply the route, `EVT-A-ONE-SCREEN-HANDOFF-v1.md` as first substantive
   content, and the decision-owner workbook. Complete
   `EVT-B-SECTION-1-SCAN-v1.md` with ID/version, completion timestamp/timezone,
   and `SECTION COMPLETE`; hash only that export, verify its governing manifest,
   and then create its detached verification record before any scenario or
   detail opens.
3. Verify the phase-2 input manifest over that Section 1 trilogy and every newly
   released file. Supply `02-scenario-and-task.md`, the detached verification record, its governing
   revised manifest, and all four exact handoff-linked revised details. Verify
   literal filenames, IDs/versions, completion timestamps/timezones, pre-hash
   `REVISED COMPLETE` states, hashes, and detached-record `FROZEN` conditions. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest stops detailed read-back.
4. Complete `EVT-B-SECTION-2-DETAIL-v1.md` with ID/version, completion
   timestamp/timezone, and `SECTION COMPLETE`; hash only that export, verify its
   governing manifest, and then create its detached verification record.
5. Verify the phase-3 input manifest over that Section 2 trilogy and the newly
   released `EXECUTIVE-DECISION-BRIEF.md` and
   `VALUE-AND-EVIDENCE-LEDGER.md`. Complete
   `EVT-B-SECTIONS-3-5-DECISION-v1.md` with completion metadata, hash only that
   export, verify its governing manifest, and then create its detached record.
   Keep Section 6 closed until a debrief-phase input manifest hashes the last
   export, governing manifest, and detached record and scoring ends.
6. Keep the Stage A participant unavailable until then. Append
   `STAGE_B_SCORING_ENDED` before allowing explanation or repair. Verify
   `EVT-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` over the final trilogy and
   blank `participant/07-stage-b-section-6-debrief.md`, complete
   `EVT-B-SECTION-6-DEBRIEF-v1.md`, then append
   `STAGE_B_SECTION_6_DEBRIEF_COMPLETED` and `STAGE_B_ENDED`. Debrief before
   scoring ends is forbidden and cannot alter frozen scores or artifacts.

## Results, close, and external binding

After `STAGE_B_ENDED`, complete immutable
`EVT-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`; append
`RUN_RESULTS_COMPLETED` and only then `RUN_LOG_CLOSED`. Results may bind the
final pre-results checkpoint, not a predicted final log hash or future closeout
time. After close, validate and copy the log byte-identically, verify
`EVT-RUN-EXECUTION-ACCESS-LOG-SHA256SUMS-<attempt-id>.txt`, and complete
`EVT-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md` with the actual results/log/copy/
manifest hashes. Six scored freeze chains alone are not full-route closure.

## Intervention levels

- **L0:** silence or think-aloud reminder;
- **L1:** repeat written text;
- **L2:** neutral probe such as “What fact can the store rely on?”;
- **L3:** define a term without applying it; and
- **L4:** recommend or supply the decision.

L3 is aided. L4 contaminates the affected gate. Preserve the result.

## Stop conditions

Stop and retain partial evidence on consent withdrawal, confidential-data
disclosure, material unblinding, changed frozen bytes, distress, material tool
failure, or coaching that makes the central result uninterpretable.
