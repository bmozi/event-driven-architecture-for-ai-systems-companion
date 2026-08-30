# One-Screen Stage A Handoff

**Packet:** EVT-RV-PILOT-001 version 1.2.3
**Status:** Blank; open only after the revised-detail governing manifest has
verified, its detached verification record exists, and the handoff-phase input
manifest verifies
**Revision note:** Version 1.2.3 adds replay identity, verification-command
evidence, completion chronology, and external access logging; it remains
unrun with people.

Keep this handoff to one page. Link detail instead of repeating it. Use
`UNKNOWN` rather than guessing. An owner may be `UNASSIGNED`; do not invent an
assignment or date. Complete this as `EVT-A-ONE-SCREEN-HANDOFF-v1.md` only
after `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` exists and the sealed
handoff-phase input manifest verifies.

- Handoff ID/version:
- Handoff completion timestamp/timezone:
- Handoff pre-hash state: `HANDOFF COMPLETE` / invalid
- Linked scenario and input-template IDs/versions:
- Detached revised freeze-verification record exact local filename/hash:
  `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` /
- Governing revised-artifact manifest exact local filename/hash:
  `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` /

## Exact revised-detail inventory

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

## Decision transfer

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

After every field is final, retain `HANDOFF COMPLETE`, hash this handoff alone
in `EVT-A-HANDOFF-SHA256SUMS-v1.txt`, verify that manifest, and only then create
`EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. Do not put this handoff's later
verification timestamp, its own SHA-256, the manifest hash, or the detached
record hash inside this governed handoff. The Stage B phase-1 input manifest
hashes the handoff, governing manifest, and detached record.
