# Capacity, Shedding, and Recovery Decision Matrix

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Preserve business priority and make delay, rejection, degradation,
and recovery visible when capacity, dependencies, or retry budgets are
exhausted.

Use this with the
[Event Loop-Prevention Checklist](event-loop-prevention-checklist.md) and the
[Traffic, Cost, and Action Multiplier Calculator](traffic-cost-action-multiplier-calculator.md).

## 1. Decision control and observation unit

| Field | Decision |
| --- | --- |
| Matrix identifier and revision | |
| Flow, service, or dependency boundary | |
| Observation unit and time window | |
| Business priority owner | |
| Reliability and capacity owner | |
| Tenant or fairness boundary | |
| Normal and failure assumptions | |
| Validation state | proposed / unrun |

## 2. Work classification

| Work class | Business value and consequence | Acceptance point | Maximum useful delay | Queue or backlog limit | Normal priority | Failure priority | Allowed degradation | May shed? | Reconciliation obligation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |

**Work that must never be silently dropped:**

**Work whose loss is acceptable under named conditions:**

**How users, partners, and operators see delay, degradation, or rejection:**

## 3. Capacity and amplification assumptions

| Boundary | Unit | Normal assumption | Failure assumption | Hard limit | Evidence source | Unknown or correlation risk |
| --- | --- | ---: | ---: | ---: | --- | --- |
| Root stimuli | per window | | | | | |
| Publications | per stimulus or window | | | | | |
| Deliveries | per stimulus or window | | | | | |
| Execution attempts | per stimulus or window | | | | | |
| External calls | per stimulus or window | | | | | |
| Action attempts | per stimulus or window | | | | | |
| Distinct committed effects | per stimulus or window | | | | | |
| Backlog | records or age | | | | | |

## 4. Throttle, shed, and circuit decisions

| Trigger or signal | Scope | Decision | Work selected | Evidence emitted | Owner | False-positive consequence | False-negative consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rate or quota reached | | | | | | | |
| Retry budget exhausted | | | | | | | |
| Backlog age or depth reached | | | | | | | |
| Dependency latency or failure threshold reached | | | | | | | |
| Circuit opens | | | | | | | |
| Action or cost budget reached | | | | | | | |
| Evidence or reconciliation source unavailable | | | | | | | |

**Threshold authority and change control:**

**Whether acceptance happens before or after the control:**

**Dead-letter, quarantine, or explicit rejection destination:**

## 5. Retry and recovery

| Decision | Normal | Dependency failure | Recovery | Owner | Evidence |
| --- | --- | --- | --- | --- | --- |
| Per-operation retry continuation and maximum | | | | | |
| Aggregate retry budget | | | | | |
| Backoff and jitter | | | | | |
| Circuit open and half-open behavior | | | | | |
| Recovery probe limit | | | | | |
| Backlog drain rate and fairness | | | | | |
| Replay or redrive authorization | | | | | |
| Re-entry and loop guard | | | | | |

## 6. Adverse exercise plan

| Scenario | Business outcome to preserve | Stop or degradation expected | Reconciliation required | Result | Evidence | Unknown |
| --- | --- | --- | --- | --- | --- | --- |
| Sudden burst | | | | unrun | | |
| Sustained overload | | | | unrun | | |
| Correlated dependency failure | | | | unrun | | |
| Retry storm | | | | unrun | | |
| Circuit oscillation | | | | unrun | | |
| Backlog exceeds useful age | | | | unrun | | |
| Recovery plus live traffic | | | | unrun | | |
| Primary stop signal unavailable | | | | unrun | | |
| Partner or agent echo creates feedback | | | | unrun | | |

## 7. Recovery and business reconciliation

| Item | Expected | Observed | Gap | Required repair | Owner | Evidence state |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Accepted stimuli | | | | | | unrun |
| Explicitly rejected stimuli | | | | | | unrun |
| Deferred or quarantined stimuli | | | | | | unrun |
| Expired work | | | | | | unrun |
| Action attempts | | | | | | unrun |
| Distinct committed effects | | | | | | unrun |
| Unexplained outcomes | | | | | | unrun |

## 8. Close

**Evidence accepted:**

**Negative evidence:**

**Known unknowns:**

**Assumption most likely to reverse the design:**

**Reversal trigger:**

**Safe state and recovery authority:**

**Decision:** reject / revise / exercise / bounded release / release

This matrix documents a capacity policy. It does not prove the workload will
remain within capacity or that shedding preserves the business outcome until
the named adverse exercises and reconciliation are run.
