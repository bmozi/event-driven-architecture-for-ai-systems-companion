# Fan-Out, Aggregation, and Responsibility Record

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Make multiplication, group completeness, partial outcomes, and
responsibility visible when one fact creates multiple reactions or many inputs
converge on one result.

Use this with the
[Traffic, Cost, and Action Multiplier Calculator](traffic-cost-action-multiplier-calculator.md)
when branches can multiply technical work or consequential actions.

## 1. Record control and root

| Field | Decision |
| --- | --- |
| Record identifier and revision | |
| Root event, command, or business stimulus | |
| Root causal identity | |
| Business subject and tenant | |
| Root declarer and technical publisher | |
| Contract and flow owners | |
| Observation unit | |
| Validation state | proposed / unrun |

## 2. Fan-out branch inventory

| Branch | Selection rule | Child subject or reaction | Owner | Authority required | Expected multiplicity | Maximum credible multiplicity | Consequential action | Completion evidence |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| | | | | | | | | |

**How expected branches are discovered:**

**How duplicate child creation is detected:**

**How authorization is prevented from expanding through fan-out:**

**Branch or tenant fairness rule:**

## 3. Aggregation group definition

Complete when branches converge, a response set is gathered, or a projection
claims completeness.

| Question | Decision |
| --- | --- |
| Aggregation or convergence identity | |
| Membership source and authority | |
| Is membership fixed, versioned, or discoverable? | |
| Expected count or closure signal | |
| Duplicate member rule | |
| Conflicting member rule | |
| Deadline and clock source | |
| Late-arrival rule | |
| Partial-result semantics | |
| Cancellation or abandonment semantics | |
| State retention and cleanup | |

## 4. Responsibility across outcomes

| Condition | Responsible owner | Required decision or action | Evidence | Escalation deadline |
| --- | --- | --- | --- | --- |
| All expected branches complete | | | | |
| One branch is late | | | | |
| One branch fails permanently | | | | |
| Membership is unknown | | | | |
| A duplicate branch commits an effect | | | | |
| Branches disagree | | | | |
| Compensation fails | | | | |
| Human judgment is required | | | | |
| Group remains stuck | | | | |

Events may announce branch facts; they do not by themselves assign durable
responsibility for completing the group.

## 5. Failure, compensation, and budgets

| Boundary | Normal rule | Failure rule | Hard stop | Owner | Reconciliation evidence |
| --- | --- | --- | --- | --- | --- |
| Publications per root | | | | | |
| Deliveries and retries | | | | | |
| Concurrent branches | | | | | |
| External calls | | | | | |
| Action attempts | | | | | |
| Distinct committed effects | | | | | |
| Aggregation wait | | | | | |
| Compensation attempts | | | | | |

## 6. Mutations and evidence

| Mutation | Invariant challenged | Expected handling | Result state | Evidence | Unresolved gap |
| --- | --- | --- | --- | --- | --- |
| Missing child | | | unrun | | |
| Duplicate child | | | unrun | | |
| Unauthorized branch | | | unrun | | |
| Late child after closure | | | unrun | | |
| Unknown membership | | | unrun | | |
| Conflicting child outcomes | | | unrun | | |
| Partial compensation | | | unrun | | |
| Branch multiplication reaches budget | | | unrun | | |

## 7. Close

**Evidence accepted:**

**Negative evidence retained:**

**Known unknowns:**

**Responsibility that remains unassigned:**

**Reversal trigger:**

**Safe containment or recovery action:**

**Decision:** reject / revise / bounded release / release

This record does not prove completeness merely because all delivered branches
were processed. Completeness depends on knowing which branches should exist.
