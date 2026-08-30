# Facilitator Execution and Access Log

**Packet:** EVT-RV-PILOT-001 version 1.2.4
**Status:** Blank facilitator-side control record; prepared and unrun

**Revision note:** Version 1.2.4 preserves the v1.2.3 replay controls and
requires the revision-phase inventory and verified manifest to bind exact
immutable `EVT-A-LIVE-UPDATE-v1.md` before its `FILE_OPENED` event.

Keep this log outside every sealed participant input. It is not a participant
instruction, artifact, answer key, or substitute for consent. Do not copy an
`ORCHESTRATION.md`, run note, hidden prompt, facilitator file, or any other
undeclared control file into a participant input. A participant input is valid
only when its item-by-item inventory matches the route's declared release and
its verified sealed-input manifest.

## Run identity and continuity

- Attempt ID:
- Stage and phase:
- Participant or reviewer code:
- Facilitator name/code:
- Execution owner:
- Timezone used for every timestamp:
- Previous phase's terminal event ID, filename, and SHA-256:
- Current sealed-input manifest filename and SHA-256:
- Current phase's first event ID:

Use one immutable attempt directory. Event IDs are monotonically increasing
within that attempt. Every row names its preceding event ID. Every phase-opening
row also binds the verified input manifest and the prior phase's terminal
record or manifest. A missing predecessor, unexplained gap, timestamp reversal,
or changed byte is a deviation, not a detail to reconstruct later.

## Declared participant-input inventory

Record one row for every expected file and every attempted extra surface before
the phase opens. `Present and manifested` must be `yes` for declared files and
`no` for undeclared files. Any undeclared orchestration or facilitator file
stops the phase.

For the Stage A revision phase, the declared inventory must include
`EVT-A-LIVE-UPDATE-v1.md`. Its first-open event must follow successful
verification of `EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`, which binds the
file with the completed initial artifacts, their governing manifest, and their
detached verification record.

| Stage/phase | Exact local filename or attempted surface | Declared by route/release | Expected SHA-256 | Present and manifested | Participant-accessible | First-open event ID | Disposition/deviation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | yes / no | | yes / no | yes / no | | |

## Item-by-item execution and access ledger

Use these exact event types in this order where applicable:

1. `SEALED_INPUT_MANIFEST_CREATED`
2. `SEALED_INPUT_MANIFEST_VERIFIED`
3. `PHASE_GATE_OPENED`
4. `FILE_OPENED` or `ACCESS_ATTEMPT_RECORDED`, once per item or attempt
5. `ARTIFACT_COMPLETED`, once per governed artifact
6. `GOVERNING_MANIFEST_CREATED`
7. `GOVERNING_MANIFEST_VERIFIED`
8. `DETACHED_RECORD_COMPLETED`
9. `NEXT_RELEASE_MANIFEST_CREATED`
10. `NEXT_RELEASE_MANIFEST_VERIFIED`
11. `NEXT_PHASE_GATE_OPENED`

Repeat events 4-11 for each release chain. A manifest gate or phase may open
only after the immediately required verification succeeded. Record the exact
command, complete observed output, exit code, verification timestamp/timezone,
and actor on every `*_MANIFEST_VERIFIED` row.

| Event ID | Prior event ID | Stage/phase | Event type | Exact filename/surface | Actor | Facilitator | Timestamp | Timezone | Verification command | Complete observed output | Exit code | Continuity binding: manifest or predecessor filename/SHA-256 | Outcome/deviation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| | | | | | | | | | | | | | | |

## Phase close

- Final event ID for this phase:
- Detached record filename, completion timestamp/timezone, and SHA-256:
- Next-release manifest filename, verification event ID, and SHA-256:
- Every participant-visible file declared and manifested: yes / no
- Any undeclared orchestration, hidden prompt, facilitator file, or extra
  surface exposed: no / deviation ID
- Gaps, reversals, failed commands, or access deviations:
- Facilitator signature/code and completion timestamp/timezone:

This log can show what the facilitator recorded for one attempt. It does not
prove participant understanding, architecture correctness, safety, or business
value.
