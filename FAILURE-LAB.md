# Event Failure Lab: The Helpful Loop

**Status:** Prepared, constructed, and unrun
**Purpose:** Test whether the method exposes false declaration, semantic drift,
unbounded reaction, and feedback
**Does not prove:** event correctness, safe capacity, agent safety, business
benefit, or practitioner usability

## Scenario

Northbridge publishes `ShipmentExceptionDetected`. A normalizer republishes a
cleaner version. An agent consumes it, calls a recovery API, and publishes
`ShipmentRecoveryRequested`. A rule converts that message into another
`ShipmentExceptionDetected` until the shipment record shows normal. The recovery
API times out after accepting work.

All systems, values, and outcomes are constructed.

## Facilitator-only seeded defects

1. an observation is labeled as an authorized business fact;
2. normalization changes the claimed meaning without a new authority;
3. fan-out, retries, and recovery traffic are absent from the multiplier;
4. the agent's action budget counts tool calls but not accepted effects; and
5. the return edge has no ancestor detection, stop owner, or reconciliation.

## Participant task

Use the [Meaning-and-Authority Record](event-meaning-and-authority-record.md),
[Semantic-Difference Ledger](transformation-and-semantic-difference-ledger.md),
[Multiplier Calculator](traffic-cost-action-multiplier-calculator.md),
[Loop Checklist](event-loop-prevention-checklist.md), and
[Reconciliation Map](asynchronous-evidence-and-business-reconciliation-map.md).

Identify what each message may truthfully claim, calculate the first-order
path, mark the return edge, bound actions and effects, and state how the unknown
API outcome is reconciled.

## Detection record

| Seed | Detected? | Artifact location | Assistance | Revision |
| --- | --- | --- | --- | --- |
| Observation presented as fact | `UNRUN` | | | |
| Semantic change without authority | `UNRUN` | | | |
| Incomplete multiplier | `UNRUN` | | | |
| Effect outside action budget | `UNRUN` | | | |
| Uncontrolled return edge | `UNRUN` | | | |

Retain misses and confusion. Finding every seed in a constructed fixture does
not establish production safety or general multiplier validity.
