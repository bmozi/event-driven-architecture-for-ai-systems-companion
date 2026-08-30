# One-Screen Stage A Handoff

**Packet:** EVT-RV-PILOT-001 version 1.2.6
**Status:** Blank; open only after the revised-detail governing manifest has
verified, its detached verification record exists, and the handoff-phase input
manifest verifies
**Revision note:** Version 1.2.6 preserves v1.2.5's full-route closure,
v1.2.4's exact immutable live-update binding, and the first-two-event rule:
branch selection, then run start; it remains unrun with people.

Keep this handoff to one declared US Letter portrait page. Link detail instead of repeating it. Use
`UNKNOWN` rather than guessing. An owner may be `UNASSIGNED`; do not invent an
assignment or date. Complete this as `EVT-A-ONE-SCREEN-HANDOFF-v1.md` only
after `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` exists and the sealed
handoff-phase input manifest verifies.

## Immutable provenance metadata — excluded from reader-facing word count

- Handoff ID/version:
- Handoff completion timestamp/timezone:
- Handoff pre-hash state: `HANDOFF COMPLETE` / invalid
- Linked scenario and input-template IDs/versions:
- Detached revised freeze-verification record exact local filename/hash:
  `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` /
- Governing revised-artifact manifest exact local filename/hash:
  `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` /

## Immutable revised-detail inventory — excluded from reader-facing word count

Stage B must receive all four files under these literal local filenames. Copy
the IDs, versions, states, and hashes from the verified detached record. A
rename, regenerated copy, summary, substitution, omission, mismatch, or
pre-hash state other than `REVISED COMPLETE` or missing detached `FROZEN`
verification stops detailed read-back.

| Exact local filename | Artifact ID/version | Completion timestamp/timezone | Pre-hash state | SHA-256 | Detached freeze status |
| --- | --- | --- | --- | --- | --- |
| `EVT-A-REVISED-WORKBOOK-v1.md` | | | `REVISED COMPLETE` | | `FROZEN` |
| `EVT-A-REVISED-MEANING-AUTHORITY-v1.md` | | | `REVISED COMPLETE` | | `FROZEN` |
| `EVT-A-REVISED-MULTIPLIER-v1.md` | | | `REVISED COMPLETE` | | `FROZEN` |
| `EVT-A-REVISED-LOOP-CHECK-v1.md` | | | `REVISED COMPLETE` | | `FROZEN` |

## Reader-facing decision transfer — maximum 450 words

- Current state:
- Evidence class (`REPORTED` / `INFERRED` / `PROPOSED` / `UNKNOWN`):
- Beneficiary and outcome:
- Decision needed now:
- Allowed now:
- Withheld:
- Accountable owner, or `UNASSIGNED`:
- If `UNASSIGNED`, authority or trigger needed to assign; use `UNKNOWN` if not
  known:
- Authority to act, or `UNKNOWN`:
- Known evidence:
- Unknowns:
- Unacceptable outcome:
- Immediate next action:
- Interim store/customer instruction:
- Authority and evidence for that instruction:
- Review date **or** evidence-based reconsideration trigger:

The word count covers all completed Markdown except only the two sections
explicitly labeled immutable provenance. After the handoff freezes, render the
exact Markdown as `EVT-A-ONE-SCREEN-HANDOFF-v1.pdf` and complete
`EVT-A-HANDOFF-LAYOUT-PROOF-<attempt-id>-v1.md`. A favorable one-page claim
requires exactly one US Letter portrait page, margins of at least 0.5 inch,
body and table text of at least 9 points, no more than 450 reader-facing words,
and no clipping, overlap, hidden overflow, or unreadable shrinking. Missing or
failed proof yields layout `HOLD`. Layout PASS is not comprehension evidence.

After every field is final, retain `HANDOFF COMPLETE`, hash this handoff alone
in `EVT-A-HANDOFF-SHA256SUMS-v1.txt`, verify that manifest, and only then create
`EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. Do not put this handoff's later
verification timestamp, its own SHA-256, the manifest hash, or the detached
record hash inside this governed handoff. The Stage B phase-1 input manifest
hashes the handoff, governing manifest, and detached record.
