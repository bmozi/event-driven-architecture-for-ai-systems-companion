# Results and Deviation Log

**Packet:** EVT-RV-PILOT-001 version 1.2.6
**Status:** Blank controlled record; no result exists

**Revision note:** Version 1.2.6 preserves v1.2.5's full-route closure,
v1.2.4's exact immutable live-update binding, and the first-two-event rule:
branch selection, then run start; it has no human validation.

Export immutable run results as
`EVT-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`. Complete them after
`STAGE_B_ENDED` and before `RUN_RESULTS_COMPLETED` and `RUN_LOG_CLOSED`. They
may bind the final pre-results checkpoint but cannot predict the future closed-
log hash or external closeout timestamp.

## Run identity

- Attempt ID:
- Exact results filename and artifact ID/version:
- Packet ID/version: `EVT-RV-PILOT-001` / `1.2.6`
- Entry branch: human / synthetic
- Execution owner and authorization:
- Stage A participant code:
- Stage B reviewer code:
- Facilitator:
- Evaluator and independence disclosure:
- Date, mode, and time:
- Record completion timestamp/timezone:
- State: `RUN RESULTS COMPLETE` / invalid
- Facilitator execution/access log exact filename and SHA-256 of its final
  pre-results checkpoint bytes:
- Final pre-results event ID and exact line-byte SHA-256:

Do not place a final closed-log hash or future closeout timestamp here. The
later `EVT-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md` binds those actual bytes.

## Consent, privacy, and freeze

- Branch-selection event and human consent records or synthetic context:
- Branches mutually exclusive and context gates matched: yes / no / deviation
- Synthetic context contains no human consent/result claim: yes / no / N/A
- Storage/access/retention authority:
- Run-specific SHA-256 manifest:
- Sealed flat Stage A input location and manifest:
- Sealed flat Stage B input location and manifest:
- Prepared-source manifest match:
- Supplied and withheld materials correct: yes / no / deviation
- Declared participant-input inventory matches item by item: yes / no /
  deviation
- Undeclared orchestration, run note, hidden prompt, facilitator file, or other
  control file in participant input: none / deviation ID
- Confidentiality or privacy concern:
- Initial Stage A artifacts completed before manifest creation: yes / no /
  deviation; IDs/versions and completion timestamps/timezones:
- Initial governing manifest filename/hash and observed verification
  timestamp/timezone:
- Initial detached verification record filename:
  `EVT-A-INITIAL-FREEZE-VERIFICATION-v1.md`
- Revision-phase input manifest
  `EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` hashes initial artifacts,
  governing manifest, detached record, and exact immutable
  `EVT-A-LIVE-UPDATE-v1.md`: yes / no / deviation
- Live-update exact filename/hash, manifest verification event, and first-open
  event:

## Revised-detail and Stage B transfer verification

- Revised artifacts completed before governing manifest creation: yes / no /
  deviation
- Revised detached record created only after manifest verification: yes / no /
  deviation
- Detached record exact filename/hash:
  `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` /
- Revised governing manifest exact filename/hash:
  `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` /
- Manifest observed verification timestamp/timezone:
- Manifest verified and lists neither itself nor the later record: yes / no /
  deviation
- Detached record claims no self-hash or future event: yes / no / deviation
- Handoff-phase input manifest hashes revised artifacts, governing manifest,
  and detached record: yes / no / deviation
- Any incomplete state or premature artifact self-declaration of `FROZEN`:
  none / deviation

| Handoff-linked exact local filename | Artifact ID/version | Completion timestamp/timezone | Pre-hash state | SHA-256 | Matched later record/manifest | Supplied to Stage B under same filename |
| --- | --- | --- | --- | --- | --- | --- |
| `EVT-A-REVISED-WORKBOOK-v1.md` | | | `REVISED COMPLETE` | | | |
| `EVT-A-REVISED-MEANING-AUTHORITY-v1.md` | | | `REVISED COMPLETE` | | | |
| `EVT-A-REVISED-MULTIPLIER-v1.md` | | | `REVISED COMPLETE` | | | |
| `EVT-A-REVISED-LOOP-CHECK-v1.md` | | | `REVISED COMPLETE` | | | |

A rename, regenerated copy, summary, substitution, omission, missing record or
manifest, mismatch, wrong pre-hash state, or missing detached verification
stops detailed read-back.

## Artifact freezes

| Freeze | Governed artifact exact filename and pre-hash state | Governing manifest filename/hash | Observed manifest-verification timestamp/timezone | Later detached verification-record filename | Next-phase input manifest filename/hash and required new input | Preserved location |
| --- | --- | --- | --- | --- | --- | --- |
| Stage A initial | `EVT-A-INITIAL-WORKBOOK-v1.md`; `EVT-A-INITIAL-MEANING-AUTHORITY-v1.md`; `EVT-A-INITIAL-MULTIPLIER-v1.md`; `EVT-A-INITIAL-LOOP-CHECK-v1.md`; `INITIAL COMPLETE` | `EVT-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` / | | `EVT-A-INITIAL-FREEZE-VERIFICATION-v1.md` | `EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` /; `EVT-A-LIVE-UPDATE-v1.md` / | |
| Stage A revised | `EVT-A-REVISED-WORKBOOK-v1.md`; `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`; `EVT-A-REVISED-MULTIPLIER-v1.md`; `EVT-A-REVISED-LOOP-CHECK-v1.md`; `REVISED COMPLETE` | `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` / | | `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` | `EVT-A-HANDOFF-PHASE-INPUT-SHA256SUMS-v1.txt` / | |
| Stage A handoff | `EVT-A-ONE-SCREEN-HANDOFF-v1.md`; `HANDOFF COMPLETE` | `EVT-A-HANDOFF-SHA256SUMS-v1.txt` / | | `EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` / | |
| Stage B Section 1 | `EVT-B-SECTION-1-SCAN-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTION-1-SHA256SUMS-v1.txt` / | | `EVT-B-SECTION-1-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` / | |
| Stage B Section 2 | `EVT-B-SECTION-2-DETAIL-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTION-2-SHA256SUMS-v1.txt` / | | `EVT-B-SECTION-2-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` / | |
| Stage B Sections 3-5 | `EVT-B-SECTIONS-3-5-DECISION-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTIONS-3-5-SHA256SUMS-v1.txt` / | | `EVT-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` /; `07-stage-b-section-6-debrief.md` | |

## Detached-record required-field audit

Do not infer missing history. Each row must match the detached record and the
facilitator execution/access log. Any blank, failed verification, output
omission, or record completion that is not explicitly later blocks `FROZEN`.

| Scope | Attempt ID | Phase | Artifact actor | Facilitator | Manifest verifier | Exact command | Complete observed output | Exit code | Verification timestamp/timezone | Record-completing actor | Later record-completion timestamp/timezone | Chronology and log match |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| Stage A initial | | | | | | | | | | | | |
| Stage A revised | | | | | | | | | | | | |
| Stage A handoff | | | | | | | | | | | | |
| Stage B Section 1 | | | | | | | | | | | | |
| Stage B Section 2 | | | | | | | | | | | | |
| Stage B Sections 3-5 | | | | | | | | | | | | |

## Full-route boundary checkpoints

- Exact pre-run order
  `ENTRY_BRANCH_SELECTED -> RUN_LOG_STARTED -> ENTRY_CONTEXT_RECORD_COMPLETED`
  event IDs/hashes:
- Exact Stage A start and `STAGE_A_STARTED` event ID/hash:
- `STAGE_A_MATERIAL_FEEDBACK_COMPLETED` event ID/hash:
- Exact Stage A end and `STAGE_A_ENDED` event ID/hash:
- Exact Stage B start and `STAGE_B_STARTED` event ID/hash:
- Exact scoring end and `STAGE_B_SCORING_ENDED` event ID/hash:
- Debrief-input manifest verification event ID/hash:
- `STAGE_B_SECTION_6_DEBRIEF_COMPLETED` event ID/hash:
- Exact Stage B end and `STAGE_B_ENDED` event ID/hash:
- `RUN_RESULTS_COMPLETED` occurs before `RUN_LOG_CLOSED`: yes / no / deviation
- Six scored freeze chains complete: yes / no / stopped
- Pre-close route complete: yes / no / stopped
- External closeout state at this earlier result time:
  `PENDING — REQUIRED FOR FULL-ROUTE CLOSURE`

## Handoff layout proof

- Markdown/PDF exact filenames and hashes:
- Layout-proof record filename/hash:
- Rendering command and tool versions:
- US Letter portrait and exactly one page: yes / no
- All margins >=0.5 inch and body/table text >=9 points: yes / no
- Reader-facing words excluding only labeled immutable provenance:
- No clipping/overlap/hidden overflow/unreadable shrinking: yes / no
- Literal layout state: `PASS` / `FAIL` / `UNRUN`
- Human comprehension state: separately `UNRUN` unless a consented human route
  actually supplies evidence

## Timing and interventions

| Stage/activity | Start | End | Elapsed | Notes |
| --- | --- | --- | ---: | --- |
| A consent/setup before consent-file read | | | | |
| A start before first file read | | | | |
| A recognition | | | | |
| A artifact | | | | |
| A live update | | | | |
| A handoff | | | | |
| B consent/setup before consent-file read | | | | |
| B start before first file read | | | | |
| B one-screen read-back | | | | |
| B Section 1 freeze | | | | |
| B revised-detail verification | | | | |
| B Section 2 freeze | | | | |
| B Sections 3-5 freeze | | | | |
| B scoring end | | | | |
| B debrief-input manifest verification | | | | |
| B Section 6 debrief | | | | |
| B stage end | | | | |
| Run-results completion | | | | |

| Stage | Sequence | File opened | Open time | Close time | Notes |
| --- | ---: | --- | --- | --- | --- |
| | | | | | |

| Time | Stage | Pause, question, or observable route friction | Response or intervention | Level |
| --- | --- | --- | --- | --- |
| | | | | |

| Time | Exact intervention | Level | Gate affected | Interpretation effect |
| --- | --- | --- | --- | --- |
| | | | | |

## Gate results

| Gate | Score/state | Exact evidence | Negative or boundary finding |
| --- | --- | --- | --- |
| RV-1 | | | |
| RV-2 | | | |
| RV-3 | | | |
| RV-4 | | | |
| RV-5 | | | |
| RV-6 | | | |
| RV-7 | | | |

- One-screen handoff scanability evidence:
- Owner recorded as assigned or `UNASSIGNED`; assignment authority/trigger:
- Review date or evidence-based trigger; basis:

## Deviations and stops

The planned live-update revision is not a correction of frozen revised bytes.
For every later correction, retain both old and new immutable artifacts and
their governing records.

| ID | Condition/reason | Correction timestamp/timezone | Exact old filename, ID/version, SHA-256, manifest, verification record | Exact new filename, ID/version, SHA-256, manifest | Replacement detached verification record | Action/effect |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Record branch omission/mixing, synthetic human-result claims, missing stage
boundaries, debrief before scoring, missing or failed layout proof, premature
results/log close, predicted future hash/time, and missing external closeout.

## Findings and disposition

| ID | Finding | Source | Severity | Revise / retest / hold / remove | Owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Truthful state statement

- Six scored freeze-chain state: complete / incomplete / stopped
- Full selected-route state: pending external closeout / incomplete / stopped
- Protocol integrity state:
- Synthetic behavior state: passed / partial / failed / unrun / N/A
- Layout state: passed / failed / unrun; not comprehension evidence
- Human evidence state: passed / partial / failed / `PREPARED/UNRUN`
- Human comprehension state: `UNRUN` unless consented human evidence exists
- Real-world evidence state: `UNRUN`
- What this exact pair establishes:
- What it does not establish:
- Packet state after authorized review:
- Files changed only after raw evidence was preserved:
- Next attempt and version:

`RUN RESULTS COMPLETE` is allowed only when every required field is present,
the six freeze chains and full-route boundaries are reported separately, and
the record contains no predicted final log hash or future closeout time. Log
`RUN_RESULTS_COMPLETED`, then close the log. The external closeout later binds
the actual results, closed-log, copy, and external-manifest hashes.
