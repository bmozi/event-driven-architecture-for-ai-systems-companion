# Temporal Freeze Protocol and Record Templates

**Packet:** EVT-RV-PILOT-001 version 1.2.1
**Status:** Facilitator-only static validation note and blank run-record schema;
prepared and unrun

## Static protocol finding

Version 1.2.0 could ask a governed workbook or handoff to contain its own later
freeze timestamp, hash, or manifest reference. Those values cannot truthfully
exist until after the governed bytes are final. Version 1.2.1 removes that
temporal self-reference from the initial, revised, handoff, and all three Stage
B freezes.

The valid causal order is:

`COMPLETE ARTIFACT BYTES -> GOVERNING MANIFEST -> MANIFEST VERIFICATION ->`
`DETACHED VERIFICATION RECORD -> NEXT-PHASE SEALED INPUT MANIFEST`

Rules:

1. Every governed artifact contains its literal filename, ID/version,
   completion timestamp/timezone, and complete pre-hash state before hashing.
2. The governing manifest hashes only the completed governed artifacts. It
   never lists itself and cannot list the later record.
3. Verify the manifest from the sealed directory and observe the exact
   verification timestamp/timezone.
4. Only after that event, create the detached record. It describes the observed
   event and contains artifact identities/hashes plus manifest filename/hash.
   It is not governed by the manifest it describes and claims no self-hash.
5. Before the next phase opens, its sealed input manifest hashes the governed
   artifacts, governing manifest, and detached record, along with any newly
   released inputs.
6. A later correction never alters frozen bytes. Preserve the old three-part evidence set and
   issue new immutable artifact bytes, a new manifest, and a new detached
   verification record.

## Exact freeze inventory

| Freeze | Governed artifact(s) and required state | Governing manifest | Later detached verification record | Next-phase input manifest |
| --- | --- | --- | --- | --- |
| Stage A initial | `EVT-A-INITIAL-WORKBOOK-v1.md`; `EVT-A-INITIAL-MEANING-AUTHORITY-v1.md`; `EVT-A-INITIAL-MULTIPLIER-v1.md`; `EVT-A-INITIAL-LOOP-CHECK-v1.md`; `INITIAL COMPLETE` | `EVT-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` | `EVT-A-INITIAL-FREEZE-VERIFICATION-v1.md` | `EVT-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` |
| Stage A revised | `EVT-A-REVISED-WORKBOOK-v1.md`; `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`; `EVT-A-REVISED-MULTIPLIER-v1.md`; `EVT-A-REVISED-LOOP-CHECK-v1.md`; `REVISED COMPLETE` | `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` | `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` | `EVT-A-HANDOFF-PHASE-INPUT-SHA256SUMS-v1.txt` |
| Stage A handoff | `EVT-A-ONE-SCREEN-HANDOFF-v1.md`; `HANDOFF COMPLETE` | `EVT-A-HANDOFF-SHA256SUMS-v1.txt` | `EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 1 | `EVT-B-SECTION-1-SCAN-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTION-1-SHA256SUMS-v1.txt` | `EVT-B-SECTION-1-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 2 | `EVT-B-SECTION-2-DETAIL-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTION-2-SHA256SUMS-v1.txt` | `EVT-B-SECTION-2-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` |
| Stage B Sections 3-5 | `EVT-B-SECTIONS-3-5-DECISION-v1.md`; `SECTION COMPLETE` | `EVT-B-SECTIONS-3-5-SHA256SUMS-v1.txt` | `EVT-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` | `EVT-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` |

## Detached verification-record schema

Create one record for each inventory row under that row's exact record
filename. Do not place the later observed values back into a governed artifact.

- Attempt ID:
- Freeze-verification record ID/version:
- Observed manifest-verification timestamp and timezone:
- Verifier and relationship:
- Verification command or method:
- Verification result: pass / fail / deviation
- Governing manifest exact filename:
- Governing manifest SHA-256:
- Manifest excludes itself: yes / no
- Manifest excludes this later detached verification record: yes / no
- Record created only after manifest verification: yes / no

| Governed artifact exact literal filename | Artifact ID/version | Artifact completion timestamp/timezone | Pre-hash state | SHA-256 | Matches manifest |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Stop/deviation, if any:
- Record claims no self-hash: yes / no
- Freeze state for the listed verified hashes: `FROZEN` / not established
- Next-phase input manifest exact filename:
- Next-phase input manifest includes every governed artifact, the governing
  manifest, and this completed record: yes / no / not yet created

## Post-freeze correction schema

- Correction ID and reason:
- Exact correction timestamp/timezone:
- Prior artifacts, manifest, and detached record preserved: yes / no
- New immutable artifact filenames and IDs/versions:
- Replacement governing manifest filename/hash:
- Replacement manifest observed verification timestamp/timezone:
- Replacement detached verification-record filename:
- Affected route stopped until authorized review: yes / no

This static review proves only that the written protocol has a coherent causal
order. It is not evidence that a human session occurred, that the files fit on
one screen, or that the architecture, safety, usability, or business value is
valid.
