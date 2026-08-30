# Stage A Practitioner Workbook

**Packet:** EVT-RV-PILOT-001 version 1.2.0
**Status:** Blank participant record

**Revision note:** Version 1.2.0 strengthens exact-file transfer and freeze
provenance after synthetic protocol audit; it has no human or practitioner
validation.

- Participant code:
- Broad role and experience band, optional:
- Stage start recorded before first file read, with timezone, and end time:
- Exact file-open order:
- Frozen supplied-file manifest:

## 1. Recognition before terminology

- Who needs what outcome?
- What is frustrating, slow, unsafe, or impossible today?
- What becomes possible if the facts and reactions are dependable?
- What can go wrong if an alert, assessment, request, and outcome are treated
  as the same fact?

## 2. Explain it to someone outside the team

In no more than five sentences, explain what happened, who may say so, what
remains uncertain, and how the store will know what actually occurred.

## 3. Event and reaction record

- Distinct facts and declarer for each:
- Facts or notifications rejected and why:
- Authority left unknown:
- Safe inference for each consumer:
- Prohibited inference:
- Shared causal identity:
- Initial delivery, reaction, cost, and autonomous-action estimate:
- Assumptions that make the estimate unreliable:
- Budget and breaker; authorized stop owner, or `UNASSIGNED` plus the
  authority/trigger needed to assign one:
- Final outcome evidence:

## 4. Monday-morning decision

- Smallest useful design or policy change:
- First duplicate, ordering, or loop failure to test:
- Owner of that test, or `UNASSIGNED` plus authority/trigger to assign one:
- Result that would block or reverse the design:

## 5. Live update

Record the update exactly as supplied.

This is the planned live-update revision that creates the first revised set.
It is not a correction of already frozen revised bytes.

- Initial answer now challenged:
- Facts that remain supportable:
- Unsafe reactions to stop or reconcile:
- Multiplication or loop path:
- Artifact fields revised:
- Evidence still missing:

### Compact incident sequence

Complete in order. Every entry must use exactly one evidence label:
`REPORTED`, `INFERRED`, `PROPOSED`, or `UNKNOWN`.

| Order | Required entry | Action or decision | Evidence label | Authorized owner or `UNASSIGNED` | Authority/evidence or `UNKNOWN` |
| ---: | --- | --- | --- | --- | --- |
| 1 | Immediate containment | | | | |
| 2 | Evidence preservation | | | | |
| 3 | Effect reconciliation | | | | |
| 4 | Authorized customer/store correction | | | | |
| 5 | Redesign or restart only after 1-4 | | | | |

## 6. Cross-role handoff

Before opening the handoff, save and freeze exactly:

- `EVT-A-REVISED-WORKBOOK-v1.md`;
- `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`;
- `EVT-A-REVISED-MULTIPLIER-v1.md`; and
- `EVT-A-REVISED-LOOP-CHECK-v1.md`.

Each file must record an artifact ID, version, completion timestamp/timezone,
and pre-hash state `REVISED COMPLETE`. Do not make the artifact self-declare
`FROZEN`. Create
`EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` without listing or hashing the
manifest itself. Complete and verify
`EVT-A-REVISED-FREEZE-RECORD-v1.md` from the detached record template before
opening the blank handoff.

| Exact revised filename | Artifact ID/version | Completion timestamp/timezone | Pre-hash state |
| --- | --- | --- | --- |
| `EVT-A-REVISED-WORKBOOK-v1.md` | | | `REVISED COMPLETE` |
| `EVT-A-REVISED-MEANING-AUTHORITY-v1.md` | | | `REVISED COMPLETE` |
| `EVT-A-REVISED-MULTIPLIER-v1.md` | | | `REVISED COMPLETE` |
| `EVT-A-REVISED-LOOP-CHECK-v1.md` | | | `REVISED COMPLETE` |

- Revised freeze timestamp and timezone:
- Governing manifest filename/hash:
- Detached freeze-record filename/hash:
- Detached record confirms all hashes and establishes `FROZEN`: yes / no
- No `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank, or
  equivalent incomplete state remains: yes / no

Only after those checks, complete [the One-Screen Stage A
Handoff](05-one-screen-handoff.md) as
`EVT-A-ONE-SCREEN-HANDOFF-v1.md`. Link the literal filenames, IDs, versions,
and hashes. If no accountable owner is authorized, record `UNASSIGNED` and
name the authority or trigger needed to assign one. Use either a justified
calendar date or an evidence-based reconsideration trigger; do not invent one.

- Handoff freeze timestamp/timezone, ID/version, hash, and manifest reference:

If any revised frozen byte later changes, preserve the old file and record the
exact old/new immutable filenames, IDs/versions, hashes, reason, correction
timestamp/timezone, replacement freeze record, and replacement manifest. Do
not describe that post-freeze correction as the planned live-update revision.

## 7. Material feedback

- Prompt that changed your thinking:
- Term or field that was unclear:
- Important decision the materials missed:
- Any prompt that pushed you toward an unsupported answer:
- What this exercise cannot establish:
