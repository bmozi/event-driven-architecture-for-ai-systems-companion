# Observation and Scoring Rubric

**Packet:** EVT-RV-PILOT-001 version 1.2.0
**Status:** Predetermined, blank, and unrun

**Revision note:** Version 1.2.0 strengthens exact-file transfer, freeze
provenance, and staged decision evidence after synthetic protocol audit; it has
no human or practitioner validation.

Score retained behavior, not agreement with preferred vocabulary.

## Scale

- **2 — unaided and defensible:** explicit, coherent, and reached with L0–L1.
- **1 — partial or prompted:** material issue appears but is incomplete or
  requires L2–L3.
- **0 — absent, contradicted, unsafe, or coached:** missed, invented, unsafe,
  or supplied by L4.
- **NA — not interpretable:** missing or materially contaminated evidence.

Do not use the total as a validated psychometric score.

## Seven reader-value gates

| Gate | Observable evidence | Stage | Score | Evidence location |
| --- | --- | --- | ---: | --- |
| RV-1 Recognition | Names the human need and consequence before mechanisms | A | | |
| RV-2 Plain understanding | Explains alert, fact, request, pending state, and outcome without broker jargon | A and B | | |
| RV-3 First useful artifact | Produces a bounded event record with explicit unknowns | A | | |
| RV-4 Outside read-back | Stage B scans the one-screen handoff, then reconstructs meaning, authority, reactions, risk, and proof without repair | B | | |
| RV-5 Failure discovery | Detects duplication, false declaration, premature outcome, multiplication, and loop | A | | |
| RV-6 Team transfer | Scanable handoff yields decision, allowed/withheld scope, evidence, unknowns, next action, an assigned owner or `UNASSIGNED` with assignment authority/trigger, and a review date or evidence-based trigger | B | | |
| RV-7 Decision-owner legibility | Selects a bounded state without inventing ROI or approval | B | | |

## Critical Events gates

Mark `clear`, `unclear`, `unsafe`, or `contaminated`:

| Gate | Clear behavior | Result | Evidence |
| --- | --- | --- | --- |
| Meaning | Keeps sensor notice, risk assessment, route request, reroute, and replacement distinct | | |
| Authority | Names who may declare each fact and leaves missing authority unknown | | |
| Permitted inference | Consumers do not treat `accepted` or `at risk` as a final outcome | | |
| Causality and duplication | One business condition survives redelivery, workers, retries, and message IDs | | |
| Multiplication and loop | Reconstructs fan-out, detects feedback, names budgets and a breaker, and names an authorized stop owner or explicit `UNASSIGNED` state with assignment authority/trigger | | |
| Outcome evidence | Reroute, stock, credit, case, notification, and final store outcome can be reconciled | | |
| Revised-detail freeze integrity | Each revised detail reaches pre-hash `REVISED COMPLETE` with ID/version and completion timestamp/timezone; the manifest hashes those bytes without hashing itself; before handoff, the detached record matches filenames, IDs/versions, completion metadata, states, and hashes and establishes `FROZEN`; no artifact prematurely self-declares `FROZEN` | | |
| Stage B exact transfer | Stage B receives the detached record, governing manifest, and every handoff-linked revised detail under the same literal filename with matching ID/version, completion metadata, pre-hash state, hash, and detached freeze status; no rename, regeneration, summary, substitution, or omission occurs | | |
| Stage B sequencing | Sections 1, 2, and 3-5 are separately exported and checksum-frozen at the required gates; Section 6 remains closed until scoring ends | | |
| Revision/correction provenance | The planned live-update revision is distinct from a later correction of frozen revised bytes; every correction preserves old/new immutable filenames, IDs/versions, hashes, reason, timestamp/timezone, replacement freeze record, and replacement manifest | | |

Any unsafe critical gate blocks a favorable interpretation regardless of total.

Do not reward an invented owner, assignment authority, calendar date, or review
trigger. Record handoff scanability and whether Stage B had to search detailed
artifacts before it could identify the bounded decision.

## Findings to record

- exact prompt and participant words;
- initial and revised interpretation;
- intervention level;
- wording or route that caused friction;
- useful behavior to preserve;
- likely source: material, scenario, participant, facilitator, or unresolved;
- severity and proposed disposition; and
- regression condition for any change.

## Interpretation

Use only bounded language: complete, partial, materially unclear, unsafe, or
inconclusive for this participant, version, scenario, and stage. Do not claim
broad usability, correctness, safety, or benefit.
