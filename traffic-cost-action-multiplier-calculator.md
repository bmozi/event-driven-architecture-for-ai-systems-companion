# Traffic, Cost, and Action Multiplier Calculator

**Status:** Proposed first-order decision model; one topology-specific seeded
experiment completed, general equations and usability not validated
**Purpose:** Expose how one business stimulus can multiply into messages, calls,
bytes, cost, and automated actions.

This worksheet produces a transparent scenario model, not a universal capacity
formula. Cycles, correlation, batching, queue dynamics, backpressure, nonlinear
pricing, shared retries, and time-varying behavior may require simulation or a
more formal model.

**Bounded evidence:** The [EVT-R012 experiment](https://github.com/bmozi/architecting-with-events-in-the-age-of-ai/blob/main/research/2026-08-28-evt-r012-bounded-multiplier-experiment.md)
matched deterministic linear counts exactly and kept common normal-scenario
counts within 0.75% for one frozen seeded topology. When delivery and action
budgets bound in the failure scenario, the model overpredicted common observed
counts by roughly 1% to 2%. The negative control produced two committed effects
with idempotency and six without it from the same six action attempts. This
supports comparing the worksheet with observed evidence and keeping effects
separate from attempts. It does not validate the worksheet across systems or
provide cost or autonomous-agent evidence.

## 1. Define the unit

| Input | Scenario value | Evidence or source |
| --- | --- | --- |
| One business stimulus means | | |
| Time window | | |
| Expected stimuli in window | | |
| Peak stimuli in window | | |
| Worst credible stimulus burst | | |
| Topology and configuration version | | |
| Assumptions explicitly excluded | | |

Do not begin with “one message” if the business trigger can already publish
several root events.

## 2. Map every directed edge

Create one row for each publication, delivery, or call. Count action attempts
and committed effects separately in Section 3.

| Edge ID | From -> to | Conditional trigger probability `p` | Outputs per trigger `f` | Attempt model and cap | Bytes/metering rule | Direct-cost rule | Can feed an ancestor? |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| E1 | | | | | | | yes/no |

Use observed values where available. Label estimates and scenario assumptions.
For bounded retries, let `qi` be the conditional probability that processing
continues to attempt `i+1` after attempt `i`. Expected attempts through at most
`n` attempts are:

`E[A] = 1 + q1 + q1*q2 + ... + q1*q2*...*q(n-1)`

The geometric expression `1 + r + r^2 + ...` is only the special case where
all conditional continuation probabilities are the same. Do not assume that
case during a correlated outage. Record the policy cap, stop conditions, and a
worst credible attempt count separately.

## 3. First-order path calculation

For an acyclic path, a first-order expected-attempt estimate is:

`incoming triggers * p * f * E[A]`

This calculation is usable only when each value is conditional on the preceding
stage and the units match. Batching, duplicate suppression, shared retries,
conditional routing, correlated failure, and feedback can make edge-by-edge
multiplication or addition wrong.

Expected byte movement on that edge is:

`expected attempts * b`

When one documented price per attempt is a defensible dated approximation,
expected direct edge cost is:

`expected attempts * c`

Otherwise apply the actual metering rule for payload chunks, requests, batches,
tiers, transfer, storage, replay, or downstream services. Report direct provider
charges separately from operational cost and business consequence.

Do not infer business effects from attempt counts. Record separately:

- execution attempts;
- technically successful executions;
- action attempts produced by those executions;
- distinct externally committed business effects after idempotency and
  reconciliation;
- reversible and irreversible effects; and
- human-reviewed and autonomous effects.

A tool call, message, database write, proposed decision, approved decision, and
externally committed effect are different units. Define the consequential-action
unit before calculating or comparing it.

Maintain separate columns for:

- normal expected path;
- peak expected path;
- failure path;
- worst credible bounded path; and
- measured experiment result.

Do not add incomparable units. Report deliveries, calls, bytes, direct cost,
action attempts, and committed effects as separate totals before creating any
summary.

## 4. Branch and stage summary

| Stage | Incoming triggers | Publications | Delivery attempts | Downstream calls | Bytes | Direct cost | Technical successes | Action attempts | Distinct committed effects | Evidence quality |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Root | | | | | | | | | | |
| Fan-out | | | | | | | | | | |
| Transformation | | | | | | | | | | |
| Downstream reaction | | | | | | | | | | |
| Recovery and retry | | | | | | | | | | |
| Reconciliation | | | | | | | | | | |
| Total | | | | | | | | | | |

For every committed-effect total, record the business identity, deduplication
or reconciliation rule, reversibility, approval path, and evidence source.

## 5. Feedback and loop analysis

List any edge that can recreate an ancestor condition, republish a causal
ancestor, retrigger the same policy, or cause another participant to do so.

| Feedback edge | Causal route back | Re-entry condition | Amplification per cycle | Maximum cycles or action/effect budget | Detection | Stop authority | Reconciliation |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| | | | | | | | |

If any feedback path has no bounded stop, do not report a finite worst case.
Escalate to explicit loop modeling and containment design.

## 6. Sensitivity check

Vary the three inputs that most affect totals.

| Input | Low | Working | High | Effect on deliveries | Effect on direct cost | Effect on action attempts | Effect on committed outcomes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| | | | | | | | |

Ask whether one shared dependency failure changes multiple probabilities or
attempt counts together. Independent averages can hide correlated storms.

## 7. Budgets and decisions

| Boundary | Normal budget | Failure budget | Hard stop | Owner | Evidence |
| --- | ---: | ---: | ---: | --- | --- |
| Delivery attempts per stimulus | | | | | |
| Downstream calls per stimulus | | | | | |
| Cost per stimulus or window | | | | | |
| Automated action attempts | | | | | |
| Distinct externally committed effects | | | | | |
| Replay or backfill effects | | | | | |

**Throttling or shedding decision:**

**Loop-prevention decision:**

**Uncertainty that could reverse the design:**

## 8. Compare model with evidence

| Scenario | Metric and unit | Modeled | Observed | Difference | Explanation or unresolved gap | Model revision |
| --- | --- | ---: | ---: | ---: | --- | --- |
| Normal | | | | | | |
| Dependency failure | | | | | | |
| Replay | | | | | | |
| Feedback attempt | | | | | | |

A mismatch is useful evidence. Do not tune the record until it hides a failed
assumption.

If a hard stop activates, record it as part of the observation. An
expected-count model that assumes non-binding budgets and a contained system
are answering different questions; preserve that discrepancy before revising
either one.
