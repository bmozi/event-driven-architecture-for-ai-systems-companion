# Event Flow and AI Implementation Brief

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Give an implementation team or AI coding system enough approved
meaning, authority, constraints, and evidence requirements to generate useful
machinery without inventing the architecture.

Complete the linked
[Event Meaning-and-Authority Record](event-meaning-and-authority-record.md)
before approving this brief. Use one brief for one bounded flow and one release
decision.

**Reader translation:** *Causal identity* is the evidence that lets a team link
an event, retry, or downstream action to the thing that caused it, rather than
merely showing that several records happened. A message ID alone may not be
enough. *Semantic difference* means a change in meaning, not just a renamed
field or changed format; if `unknown`, `zero`, or `approved` means something
different, the consumer contract has changed.

## Completion-state legend

| State | Meaning |
| --- | --- |
| proposed / unrun | Design or test exists only on paper |
| sourced | A cited specification or policy supports the stated scope |
| observed — bounded | Retained evidence exists for the named configuration only |
| contradicted | Evidence falsified the current decision |
| unknown | No approved answer; state whether this stops generation or release |

## 1. Brief control

| Field | Approved value or reference |
| --- | --- |
| Brief identifier and revision | |
| Flow name and bounded context | |
| Business sponsor | |
| Architecture owner | |
| Contract owner | |
| Security and privacy reviewer | |
| Operations owner | |
| Approval state and date | |
| Supersedes | |

## 2. Business stimulus and outcome

| Question | Decision |
| --- | --- |
| What starts this flow? | |
| Is the stimulus a fact, observation, notification, command, or state transfer? | |
| What business subject and tenant does it concern? | |
| What useful outcome is expected? | |
| What counts as accepted? | |
| What counts as completed? | |
| What does not count as success? | |
| Which invariant must remain true? | |

## 3. Meaning, authority, and allowed inference

| Event or action | Plain-language meaning | Legitimate declarer or authority | Technical publisher or executor | Allowed consumer inference | Prohibited inference |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

**Authority evidence required at execution or publication time:**

**Actor, subject, tenant, and delegated-authority distinctions:**

**Correction, supersession, or revocation rule:**

## 4. Bounded flow

Add one row per producer, route, transformation, consumer, external action, and
feedback edge. Do not hide generated infrastructure or managed-service steps.

| Step or edge | Input | Operation | Output or effect | Owner | Required context preserved | Maximum attempts or fan-out | Stop condition |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| | | | | | | | |

**Root causal identity rule:**

**Partitioning or ordering scope:**

**Idempotency identity and committed-effect boundary:**

**Feedback or re-entry rule:**

## 5. Contract and data constraints

| Constraint | Approved decision | Evidence reference | Unknown or countercondition |
| --- | --- | --- | --- |
| Envelope and schema revision | | | |
| Semantic revision | | | |
| Required, optional, null, absent, redacted, and not-applicable meanings | | | |
| Subject version and late-arrival rule | | | |
| Classification and minimization | | | |
| Consumer purpose and entitlement | | | |
| Retention, deletion, and legal hold | | | |
| Residency or contractual boundary | | | |
| Replay and backfill eligibility | | | |

## 6. Failure and recovery behavior

| Condition | Required behavior | Visible evidence | Reconciliation owner | Escalation or stop |
| --- | --- | --- | --- | --- |
| Duplicate delivery | | | | |
| Reordered or stale event | | | | |
| Dependency timeout with unknown outcome | | | | |
| Poisoned or repeatedly failing work | | | | |
| Capacity exhaustion or shedding | | | | |
| Partial fan-out or aggregation | | | | |
| Feedback or action-budget exhaustion | | | | |
| Replay interruption | | | | |

## 7. AI, agent, and MCP participation boundary

Complete this section when an AI application can consume an event, select a
tool, request an action, or publish a follow-on message. MCP exposure makes a
tool discoverable and invocable; it does not grant the model business authority
or turn a tool result into a declared fact.

| Participation decision | Approved value or evidence |
| --- | --- |
| AI host, agent role, represented actor, subject, tenant, and purpose | |
| MCP server, protocol revision, tool name, and exact operation | |
| Underlying API or capability owner and current authorization check | |
| Eligible input events and facts the participant may rely on | |
| Tool result classification: observation, data, recommendation, command result, or declared fact | |
| Events the participant may request, publish, or legitimately declare | |
| Durable-workflow handoff when responsibility remains open | |
| Tool-call, result, approval, action, event, and effect provenance | |
| Action, retry, cost, time, and feedback budgets enforced outside the model | |
| Refusal, escalation, quarantine, and stop path | |

### AI may generate

- [ ] Envelope and schema scaffolding from approved fields.
- [ ] Producer, consumer, routing, and transformation code from approved edges.
- [ ] Infrastructure configuration within named product and version constraints.
- [ ] Test fixtures for approved positive, negative, and boundary cases.
- [ ] Telemetry instrumentation for named evidence fields.
- [ ] Documentation that links generated artifacts to this brief revision.
- [ ] Other:

### AI must not invent

- [ ] Business meaning, declarer, or allowed inference.
- [ ] Actor, subject, tenant, or delegated authority.
- [ ] Completion, compensation, reconciliation, or committed-effect semantics.
- [ ] Idempotency identity, ordering key, retry budget, or feedback limit.
- [ ] Retention, replay authority, privacy purpose, or legal exception.
- [ ] A default answer for a field marked unknown.
- [ ] Other:

**Required model, tool, prompt, policy, and generated-artifact provenance:**

**Unknowns that stop generation:**

**Unknowns that permit a scaffold but stop release:**

## 8. Verification brief

| Claim to challenge | Positive case | Negative or mutation case | Required evidence | Result state | What passing would not prove |
| --- | --- | --- | --- | --- | --- |
| Meaning and contract | | | | proposed / unrun | |
| Authority and tenant isolation | | | | proposed / unrun | |
| Duplicate and ordering invariant | | | | proposed / unrun | |
| Failure and bounded retry | | | | proposed / unrun | |
| Feedback and action budget | | | | proposed / unrun | |
| Privacy, retention, and replay | | | | proposed / unrun | |
| Business reconciliation | | | | proposed / unrun | |

## 9. Release, unknowns, and reversal

| Field | Decision |
| --- | --- |
| Evidence accepted for this release | |
| Negative evidence retained | |
| Known unknowns | |
| Missing evidence that blocks release | |
| Residual risk accepted by whom | |
| Reversal trigger | |
| Safe disable, quarantine, or rollback action | |
| Reconsideration owner and deadline | |
| Final decision: reject / revise / bounded release / release | |

A completed brief makes decisions inspectable. It does not prove that generated
code implements them or that the resulting system is safe.
