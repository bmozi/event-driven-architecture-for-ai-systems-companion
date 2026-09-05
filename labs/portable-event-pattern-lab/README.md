# Portable Event Pattern Lab

**Status:** Runnable teaching fixture; it is not a broker benchmark, production
adapter, safety control, or evidence of platform behavior.

This optional lab makes the guide's event decisions executable without binding
the book to any event product. It deliberately uses only the Python standard
library and an in-memory runner. The reader supplies a real platform adapter
only after the event contract, authority, invariants, pressure limits, and
evidence requirements have been reviewed.

## Run it

```bash
python3 run_lab.py
```

The runner executes five constructed fixtures:

1. a normalizer keeps `unknown` distinct from `zero`;
2. a hot subject reaches a named pressure limit and is quarantined;
3. a poison event retains its root identity and reason;
4. a dead-letter flood reaches a hard capacity stop; and
5. a feedback event stops at its permitted generation.

All fixtures are deterministic and labeled teaching material. A passing result
proves only that this small in-memory model behaved as its assertions specify.
It does not prove broker ordering, partitions, throughput, delivery guarantees,
security, capacity, or a business outcome.

## The portable adapter boundary

Before replacing the in-memory runner, an implementation adapter must make
these decisions explicit:

| Adapter operation | Contract it must preserve |
| --- | --- |
| Receive | Event identity, root stimulus identity, subject, occurrence time, contract revision, and delivery evidence remain distinguishable. |
| Route | Recipient policy and default disposition are explicit; no hidden recipient becomes an authority decision. |
| Transform | A semantic-preservation decision exists, or a new derived claim receives its own identity, declarer, and provenance. |
| Quarantine | Minimal safe evidence, reason, owner, capacity, retention, correction, and re-entry path are retained. |
| Retry | Attempt identity, cap, backoff owner, idempotency boundary, and distinction between attempt and committed effect are explicit. |
| Stop | Pressure, generation, action, effect, and time limits fail closed with an owner for unfinished consequences. |
| Reconcile | Technical disposition reconnects to a named business outcome or records the remaining uncertainty. |

An adapter can use any product, managed service, library, or in-house runtime.
The field guide does not endorse one. Product configuration belongs in the
implementation repository, while the decision records remain portable.

## Use it with the book

1. Complete the [Event Pattern Decision Cards](../../event-pattern-decision-cards.md).
2. Use the [Capacity, Shedding, and Recovery Decision Matrix](../../capacity-shedding-and-recovery-decision-matrix.md)
   to define the relevant pressure and evidence boundary.
3. Fill the [Event Pressure and Failure Diagnostic Card](../../event-pressure-and-failure-diagnostic-card.md).
4. Change one fixture only after recording the expected invariant and failure
   result. Preserve failures rather than tuning the fixture until it passes.
5. Transfer the confirmed design decisions into the Event Flow and AI
   Implementation Brief; do not promote this lab's synthetic outcome into a
   production claim.
