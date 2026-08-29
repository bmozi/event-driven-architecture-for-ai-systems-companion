# Event Loop-Prevention Checklist

**Status:** Working checklist; not a safety guarantee
**Purpose:** Find and bound direct, indirect, retry, recovery, replay, and
autonomous feedback before consequential reactions multiply.

Run this review on the complete causal topology, not one service at a time.

## 1. Topology and ancestry

- [ ] The root business stimulus is named.
- [ ] Every producer, intermediary, consumer, external call, and consequential
      action is mapped.
- [ ] Direct causal parents are distinguishable from correlation and trace context.
- [ ] Transformations retain enough ancestry to detect re-entry.
- [ ] Cross-team, cross-tenant, vendor, and agent-controlled edges are included.
- [ ] Recovery, fallback, audit, notification, and reconciliation paths are mapped.

## 2. Feedback search

For every emitted event or action, ask whether it can:

- [ ] recreate its own input condition;
- [ ] republish an ancestor fact under a new type or schema;
- [ ] invoke a capability that produces an equivalent ancestor event;
- [ ] trigger a policy that issues the initiating command again;
- [ ] cause another tenant, partner, agent, or workflow to return the condition;
- [ ] re-enter through normalization, enrichment, or CDC;
- [ ] repeat through retry, timeout ambiguity, redelivery, or compensation;
- [ ] recur during replay, backfill, rebuild, or disaster recovery; or
- [ ] bypass ancestry checks because context was dropped.

Record each plausible feedback edge even if its probability appears low.

## 3. Legitimate recurrence versus runaway loop

| Question | Decision |
| --- | --- |
| When is recurrence a valid new business fact? | |
| What distinguishes new intent from repeated ancestry? | |
| Which subject and time window define a cycle? | |
| Which maximum iterations or actions are legitimate? | |
| Which budget applies per stimulus, subject, tenant, and time window? | |
| Which irreversible or high-consequence action requires separate authority? | |

## 4. Prevention and containment

- [ ] Idempotency protects the named business outcome, not only message handling.
- [ ] Ancestry or generation depth survives every required transformation.
- [ ] Re-entry and repeated-policy guards are defined.
- [ ] Retry budgets and backoff are bounded under correlated failure.
- [ ] Agent tool calls and event emissions consume an action budget.
- [ ] Rate, cost, and consequence budgets have hard stops where needed.
- [ ] Circuit and recovery events cannot silently recreate the initiating condition.
- [ ] Manual override has named authority and an audit trail.
- [ ] Stop behavior works when one dependency or evidence source is unavailable.
- [ ] Quarantine prevents continued external effect while preserving evidence.

## 5. Detection

| Signal | Threshold or rule | Scope | Evidence delay | False-positive risk | Owner |
| --- | --- | --- | --- | --- | --- |
| Repeated ancestry | | | | | |
| Generation depth | | | | | |
| Actions per stimulus | | | | | |
| Republish ratio | | | | | |
| Retry and recovery rate | | | | | |
| Cost or external-call budget | | | | | |
| Business reconciliation gap | | | | | |

Message-rate alerts alone may detect activity without identifying a loop or its
business consequence.

## 6. Adverse tests

- [ ] Duplicate the initiating event.
- [ ] Reorder ancestor and descendant events.
- [ ] Delay or remove causal context.
- [ ] Fail the downstream call after an unknown outcome.
- [ ] Open and close the circuit repeatedly.
- [ ] Replay the causal slice.
- [ ] Make an agent misclassify an inference as a fact or command.
- [ ] Let a partner or second tenant echo the condition.
- [ ] Remove the primary stop signal and exercise the backup stop.
- [ ] Verify containment prevents new effects and reconciliation finds prior effects.

## 7. Release gate

| Decision | Result |
| --- | --- |
| Known feedback edges | |
| Maximum credible action multiplier | |
| Prevention controls | |
| Detection evidence | |
| Stop authority and tested stop time | |
| Side effects requiring reconciliation | |
| Unresolved blind spots | |
| Reversal trigger | |
| Release owner and decision | |

If a plausible feedback path has no bounded stop or consequential effects cannot
be reconciled, the checklist does not pass merely because local tests are green.
