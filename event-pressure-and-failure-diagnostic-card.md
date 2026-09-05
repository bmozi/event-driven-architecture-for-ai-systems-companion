# Event Pressure and Failure Diagnostic Card

**Status:** Working decision aid; `PLANNED/UNRUN` for practitioner validation.
**Purpose:** Diagnose skew, hot keys, poison messages, and dead-letter floods
without confusing a technically contained symptom with a resolved business
consequence.

This card is vendor-neutral. Map its terms to your platform only after naming
the fact, business priority, affected subject, invariant, owner, and evidence
source. Completing it does not prove capacity, resilience, correctness, or a
safe release.

## Start with the observable symptom

| Symptom | First distinction | Do not assume | Immediate containment question |
| --- | --- | --- | --- |
| One key, subject, or tenant dominates work | Skew versus legitimate priority | More partitions or workers will redistribute a logically single key | Which affected subjects may be delayed, split, or quarantined without changing the fact or violating fairness? |
| The same record repeatedly fails | Malformed/unauthorized/unsupported input versus transient dependency failure | Retry will repair a semantic or policy defect | Where can the original record, reason, identity, and permitted recovery path be retained safely? |
| Dead-letter volume grows faster than resolution | Quarantine evidence versus an operational trash pile | Moving a record elsewhere closes its business obligation | Who owns triage, capacity, expiry, correction, replay authorization, and final disposition? |
| Backlog rises after recovery | Catch-up work versus renewed current demand | Green consumer health means the business is caught up | Which window, priority, and business effect are still incomplete or stale? |
| A circuit opens and closes repeatedly | Protection versus oscillation | A technical circuit determines acceptable loss or recovery priority | Which owner decides when work is resumed, diverted, shed, or reconciled? |

## Diagnostic worksheet

| Field | Record |
| --- | --- |
| Observable symptom and start time | |
| Fact, subject, tenant, and business priority | |
| Affected population and evidence window | |
| Expected rate, observed rate, and measurement unit | |
| Dominant key, route, source, schema revision, or failure signature | |
| Contract/invariant at risk | |
| Current disposition: accepted, delayed, retried, quarantined, shed, or unknown | |
| Existing capacity, retry, DLQ, action, and effect limits | |
| Immediate containment and named authority | |
| What work remains owed, stale, unsafe, or unreconciled | |
| Evidence retained without re-exposing restricted data | |
| Re-entry, replay, correction, and closure authority | |
| Test or observation that can falsify the diagnosis | |

## Four challenge paths

### 1. Skew and hot keys

Ask whether the dominant key represents one legitimate high-volume subject,
bad partitioning, replay concentration, a retry loop, or a consumer that is
slower only for a particular contract revision. Do not split a key merely to
improve throughput if ordering or business identity would be lost.

Test a bounded high-volume fixture, record per-key lag and outcome age, then
compare the result with an unrelated normal key. Averages can hide the subject
that is waiting.

### 2. Poison messages

Classify the failure before retrying: invalid shape, impossible meaning,
unauthorized source, forbidden use, unavailable dependency, or unknown. Retain
the minimal safe evidence, not a duplicate sensitive payload. A poison record
must have a visible disposition: correct, reject, compensate, defer, replay
under authorization, or accept a named residual consequence.

### 3. Dead-letter floods

A dead-letter destination is an evidence path, not a terminal state. Set a
capacity threshold and escalation rule before a flood. Measure arrival rate,
age, reason distribution, storage/retention pressure, and closure rate. Stop
new unsafe replays when the queue cannot be triaged inside its stated recovery
window.

### 4. Cascades and loops

Trace whether a failure event, recovery event, alert, replay, or agent action
can recreate an ancestor condition. Bound generations, attempts, actions,
effects, cost, and time separately. A stop must remain effective when retry,
replay, or a differently named derived event enters the path.

## Evidence receipt

Link this card to the [Capacity, Shedding, and Recovery Decision
Matrix](capacity-shedding-and-recovery-decision-matrix.md), [Traffic, Cost, and
Action Multiplier Calculator](traffic-cost-action-multiplier-calculator.md),
and [Event Loop-Prevention Checklist](event-loop-prevention-checklist.md).
Record the symptom, containment, unresolved consequence, and re-entry decision
in the [Asynchronous Evidence and Business-Reconciliation
Map](asynchronous-evidence-and-business-reconciliation-map.md).

## What AI may and may not do

AI may group failure signatures, draft hypotheses, propose bounded fixtures,
and surface missing evidence. It must not decide that a key is expendable,
discard a record, authorize a replay, claim a poison message is harmless, or
close an unreconciled business obligation.
