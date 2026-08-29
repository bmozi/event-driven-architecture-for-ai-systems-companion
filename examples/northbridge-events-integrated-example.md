# Northbridge Events Integrated Companion Example

<!-- markdownlint-disable MD013 -->

**Status:** Completed fictional-composite tool application; not practitioner
validated and not production evidence

**Enterprise:** Northbridge Exchange

**Flow:** Shipment-exception observation, partner notification, pause request,
pause attempt, and bounded feedback review

## Disclosure and evidence rules

Northbridge Exchange, its people, architecture, policies, identifiers, and
decisions are authorized fictional-composite teaching material. They do not
represent a John Briggs customer, employer, incident, measurement, or outcome.

This example applies seven working tools:

1. [Event Flow and AI Implementation Brief](../event-flow-and-ai-implementation-brief.md)
2. [Transformation and Semantic-Difference Ledger](../transformation-and-semantic-difference-ledger.md)
3. [Fan-Out, Aggregation, and Responsibility Record](../fanout-aggregation-and-responsibility-record.md)
4. [Replay, Backfill, Authorization, and Effect Ledger](../replay-backfill-authorization-and-effect-ledger.md)
5. [Ordering, Duplication, and Idempotency Invariant Matrix](../ordering-duplication-and-idempotency-invariant-matrix.md)
6. [Capacity, Shedding, and Recovery Decision Matrix](../capacity-shedding-and-recovery-decision-matrix.md)
7. [Asynchronous Evidence and Business Reconciliation Map](../asynchronous-evidence-and-business-reconciliation-map.md)

Every mutation, behavioral test, replay, capacity exercise, and reconstruction
result below is explicitly **unrun** unless a row cites the retained synthetic
EVT-R012 experiment. That experiment is topology-specific and does not validate
Northbridge behavior, a broker, production capacity, ordering, privacy,
recovery, or one real business outcome.

| Evidence state | Meaning in this example |
| --- | --- |
| proposed composite decision | Constructed architecture for teaching; not tested or approved for a real system |
| scenario assumption | Frozen synthetic input, topology, probability, or budget; not measured history |
| observed — EVT-R012 bounded synthetic | Retained simulator output for the exact frozen topology and scenario |
| unrun | No result exists; the expected result is a design hypothesis |
| unknown | The tool exposed a decision that the composite has deliberately not resolved |

## Shared scenario spine

`shipment.exception.detected` is treated here as an **observation** that a
Northbridge detector found a condition associated with one shipment. It does
not declare a contractual breach, partner fault, shipment pause, or completed
remedy.

The frozen EVT-R012 synthetic topology contains five edges:

| Edge | Proposed composite interpretation | Evidence state |
| --- | --- | --- |
| E1 — operations projection | Update an internal view of observed shipment exceptions | scenario assumption |
| E2 — partner alert | Attempt a bounded notification to an entitled partner | scenario assumption |
| E3 — exception policy | Evaluate the observation and, when policy permits, publish `shipment.pause.requested` | scenario assumption |
| E4 — pause action | Attempt `pause-shipment` and publish `shipment.pause.attempted`; attempted is not completed | scenario assumption |
| E5 — partner-status echo | Translate a pause-attempt signal back into `shipment.exception.detected`, creating a feedback risk | scenario assumption |

The detector, policy evaluator, shipment controller, notifier, projection, and
partner echo are constructed components. Their real authority and contracts do
not exist outside this example.

## 1. Applied Event Flow and AI Implementation Brief

### Brief control and outcome

| Field | Applied value | State |
| --- | --- | --- |
| Brief identifier | `NBX-SHIP-EXC-BRIEF-v0` | proposed composite decision |
| Architecture owner | Maya Torres | proposed composite decision |
| Security and authority reviewer | Nia Okafor | proposed composite decision |
| Reliability owner | Eli Chen | proposed composite decision |
| Operations and reconciliation owner | Rosa Alvarez | proposed composite decision |
| Product and partner-policy owner | Samir Patel | proposed composite decision |
| Data and derivation reviewer | Lena Brooks | proposed composite decision |
| Root stimulus | One isolated `shipment.exception.detected` observation for one shipment subject | scenario assumption |
| Accepted | Broker or application acceptance is not yet defined | unknown; release stop |
| Completed | The entitled operations outcome is reconciled for the shipment; a send or pause attempt alone is insufficient | proposed composite decision |
| Invariant | One root intent must not create more than one distinct committed effect for the same action identity | proposed composite decision |

### Meaning, authority, and allowed inference

| Item | Category and meaning | Authority | Allowed inference | Prohibited inference | State |
| --- | --- | --- | --- | --- | --- |
| `shipment.exception.detected` | Observation: a detector observed a named condition | Detector is technical publisher; legitimate declarer remains to be approved | A condition was observed under the referenced detector revision | Partner fault, contractual breach, pause, or remediation | proposed; authority unknown |
| `shipment.pause.requested` | Command: an authorized policy asks the controller to attempt a pause | Exception policy under a current delegated operations policy | An attempt is requested | Pause accepted or completed | proposed; delegation unverified |
| `shipment.pause.attempted` | Observation: the controller attempted the pause capability | Shipment controller may report its own attempt | An attempt occurred | Shipment is paused | proposed; completion evidence unknown |
| `send-partner-alert` | Consequential action attempt | Partner-notification policy plus tenant entitlement | A notification attempt was made | Partner received, understood, or accepted it | proposed; delivery evidence unknown |
| `pause-shipment` | Consequential action attempt | Shipment operations policy | A pause was attempted | Pause committed or remained effective | proposed; effect evidence unknown |

Actor, subject, tenant, and delegated authority remain separate. Topic write
permission is not accepted as authority to classify an exception or pause a
shipment.

### Bounded flow and generation constraints

| Edge | Input | Operation | Output or effect | Owner | Bound or stop | State |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | exception observation | Project internal state | Operations view | Lena | Delivery and publication budgets | scenario assumption; behavior unrun |
| E2 | exception observation | Notify entitled partner | `send-partner-alert` attempt | Samir | Action and effect budgets; tenant check | scenario assumption; behavior unrun |
| E3 | exception observation | Evaluate pause policy | `shipment.pause.requested` | Nia and Rosa | Policy revision, delegation, publication budget | scenario assumption; behavior unrun |
| E4 | pause request | Attempt pause capability | `pause-shipment`; `shipment.pause.attempted` | Rosa | Action/effect budgets and idempotency | scenario assumption; behavior unrun |
| E5 | pause attempt | Echo condition | exception observation generation +1 | Eli | Maximum feedback generation 2 in EVT-R012 | bounded synthetic stop observed; production behavior unrun |

AI may scaffold schemas, handlers, policy adapters, tests, and telemetry only
from approved values. It must not invent the observation's authority, partner
entitlement, pause delegation, effect identity, retention, replay permission,
or completion evidence.

### Planned brief verification

| Mutation or review | Expected behavior | Result | Release consequence |
| --- | --- | --- | --- |
| Publisher has broker permission but no declaration authority | Reject or quarantine declaration | unrun | blocks release |
| Partner tenant differs from shipment tenant | Suppress alert and preserve denial evidence | unrun | blocks release |
| `pause.attempted` is treated as `pause.completed` | Contract or semantic test fails | unrun | blocks release |
| E5 drops causal ancestry | Backup generation/action stop contains recurrence | unrun | blocks release |
| AI omits an unknown field by choosing a default | Generation gate fails | unrun | blocks release |

**Known unknowns:** acceptance point, legitimate exception declarer, pause
delegation, partner entitlement source, effect ledger, and retention policy.

**Reversal trigger:** any generated or implemented consumer treats an
observation or attempt as an authoritative completed fact.

## 2. Applied Transformation and Semantic-Difference Ledger

### Transformation decisions

| Stage | Input to output | Intended relationship | Authority decision | Principal semantic risk | State |
| --- | --- | --- | --- | --- | --- |
| E1 projection | Exception observation to operations view | New representation of the same observation | Projection is not a new business declarer | View is mistaken for authoritative shipment state | proposed; unrun |
| E3 policy | Exception observation to pause request | New command derived from an observation | Requires separate delegated operations authority | Observation silently becomes authorized intent | proposed; authority unknown; unrun |
| E4 controller | Pause request to pause attempt | New observation of execution attempt | Controller may report attempt, not completion | Attempt is mislabeled as committed outcome | proposed; unrun |
| E5 echo | Pause attempt to exception observation | Potentially new observation, but semantically ambiguous | Partner echo is not automatically the original detector authority | Ancestor is recreated under the same type and loops | proposed; bounded loop simulated, semantic test unrun |

### Field-level difference focus

| Field or context | Required treatment | Planned mutation | Result |
| --- | --- | --- | --- |
| Root causal identity | Preserve through E1-E5 | Remove it at E5 | unrun |
| Feedback generation | Increment only on E5 | Reset to zero during normalization | unrun |
| Exception condition | Preserve detector-specific meaning | Map unknown condition to generic exception | unrun |
| Effective time | Preserve observation and attempt times separately | Replace both with processing time | unrun |
| Authority | Preserve detector, policy, controller, and echo identities separately | Copy technical publisher into business-declarer field | unrun |
| Tenant | Preserve shipment tenant and partner recipient independently | Substitute recipient tenant as subject tenant | unrun |
| Outcome category | Keep requested, attempted, and completed distinct | Relabel attempted as completed | unrun |

**Evidence:** EVT-R012 observed that a configured E5 feedback edge can recreate
the root event type until the generation cap binds. It did not test semantic
equivalence, authority, field mappings, or provenance.

**Unknown:** whether E5 represents a legitimate new observation at all.

**Reversal trigger:** a semantic-difference mutation passes while a consumer's
allowed action changes.

## 3. Applied Fan-Out, Aggregation, and Responsibility Record

### Fan-out inventory

| Branch | Selection and multiplicity | Consequential surface | Responsible owner | Completion evidence | State |
| --- | --- | --- | --- | --- | --- |
| E1 operations projection | One configured delivery plus possible duplicate per root publication | Internal derived state | Lena | Projection revision tied to root identity | scenario assumption; unrun |
| E2 partner alert | Route probability and duplicate probability are frozen synthetic inputs | Human-visible partner notification | Samir | Partner-notification effect ledger, not send success | scenario assumption; evidence unknown; unrun |
| E3 pause policy | Route probability is a frozen synthetic input | Can create pause request and downstream pause action | Nia and Rosa | Policy decision plus controller outcome | scenario assumption; evidence unknown; unrun |

The topology does not contain an aggregator. Northbridge must not infer that all
branches completed merely because the delivered branches returned technical
success.

### Responsibility decisions

| Condition | Responsible owner | Proposed response | Result |
| --- | --- | --- | --- |
| Projection late but action branches proceed | Lena | Mark view stale; do not block authoritative outcome without a separate decision | unrun |
| Partner alert fails after unknown send outcome | Samir | Reconcile by effect identity before another send | unrun |
| Pause policy publishes but controller never reconciles | Rosa | Retain durable owner and escalate stranded request | unrun |
| Branch membership changes after root publication | Maya | Version the flow contract; do not claim historical completeness from current membership | unrun |
| Feedback reaches generation stop | Eli | Quarantine further re-entry and reconcile prior effects | unrun in a real flow; bounded stop observed in EVT-R012 |

**Known unknown:** what group, if any, Northbridge wants to call “shipment
exception handling complete.”

**Reversal trigger:** a dashboard presents delivered-branch count as complete
business handling without an authoritative membership and outcome rule.

## 4. Applied Replay, Backfill, Authorization, and Effect Ledger

### Proposed authorization

| Field | Applied value | State |
| --- | --- | --- |
| Purpose | Rebuild the operations projection for an approved shipment slice | proposed composite decision |
| Input range | Exact tenants, subjects, time range, semantic revisions, and hash remain unspecified | unknown; execution stop |
| Environment | Isolated replay namespace with external effects disabled | proposed; unrun |
| Approval | Maya, Nia, Rosa, and the data-purpose owner | proposed; unrun |
| Abort authority | Rosa and Eli | proposed; stop behavior unrun |
| Present-day effect policy | E2 partner alert, E4 pause action, and E5 echo disabled by default | proposed; enforcement unrun |

### Consumer and effect ledger

| Consumer | Replay mode | Effect risk | Idempotency or evidence requirement | Result |
| --- | --- | --- | --- | --- |
| Operations projection | isolated commit after comparison | Derived state can differ under a new transformation revision | Root identity, semantic revision, before/after hash | unrun |
| Partner notifier | disabled | Duplicate present-day notification | Effect identity and partner receipt evidence | unrun |
| Exception policy | shadow only | Historical observation creates current pause request | Historical/current policy comparison | unrun |
| Shipment controller | disabled | Duplicate or newly unauthorized pause | Durable business-effect identity | unrun |
| Partner-status echo | disabled | Replay re-enters live exception flow | Root ancestry and generation stop | unrun |

### Replay mutations

| Mutation | Expected safe result | Result |
| --- | --- | --- |
| Partner notifier accidentally enabled | Preflight or hard action stop aborts before external effect | unrun |
| Current enrichment changes historical exception category | Semantic-difference comparison refuses commit | unrun |
| Idempotency evidence has expired | No live effect; quarantine and require a new decision | unrun |
| Restricted subject appears in slice | Exclude or stop under reviewed privacy rule | unrun |
| Abort signal is unavailable | Fail closed before live effect | unrun |
| Replay overlaps live event for the same shipment | Subject-version rule prevents ambiguous projection commit | unrun |

**Privacy countercondition:** broker retention or replay availability does not
establish that the purpose is still authorized or that restricted and deleted
data may be reconstructed.

**Known unknowns:** lawful/policy basis, historical transformation runtime,
consumer inventory completeness, effect-ledger retention, and deletion map.

**Reversal trigger:** any preflight shows an external branch cannot be disabled
or reconciled.

## 5. Applied Ordering, Duplication, and Idempotency Invariant Matrix

### Invariant decisions

| Handler or effect | Proposed invariant | Ordering scope | Duplicate identity | Committed-effect boundary | Evidence state |
| --- | --- | --- | --- | --- | --- |
| Operations projection | Older observations cannot overwrite a newer shipment subject version | One shipment subject; partition/key design unknown | Event identity plus semantic revision | Projection version commit | proposed; unrun |
| Partner alert | One root intent produces at most one distinct alert effect for the named recipient and alert purpose | Order is subordinate to current entitlement and effect identity | Root stimulus + action + recipient + purpose proposed | Durable partner-notification effect record | proposed; unrun |
| Pause request evaluation | A stale observation cannot authorize a new pause request | Shipment subject and policy revision | Root stimulus + policy decision proposed | Authorized pause request record | proposed; unrun |
| Pause action | One authorized pause intent produces at most one distinct committed pause effect | Shipment subject version | Root stimulus + `pause-shipment` in EVT-R012; real key unknown | Shipment control system commit | synthetic key observed; real boundary unrun |

### Retained bounded evidence

| Observation | Result | Exact boundary |
| --- | --- | --- |
| Deterministic feedback scenario with simulator idempotency enabled | Six action attempts produced two distinct committed effect instances and four suppressed duplicates | Observed — EVT-R012 bounded synthetic; two action names under root-stimulus-plus-action identity |
| Same deterministic scenario with idempotency disabled | Six action attempts produced six committed effect instances and no suppression | Observed — EVT-R012 bounded synthetic negative control |

These observations show only that attempts and effects differ in the retained
simulator. They do not prove the proposed Northbridge keys, concurrency rules,
partner delivery, pause commit, or production idempotency.

### Planned invariant mutations

| Mutation | Expected result | Actual result |
| --- | --- | --- |
| Same message identifier delivered twice | One permitted effect, duplicate attempt visible | unrun |
| Different identifiers express the same alert intent | One effect under business identity | unrun |
| Duplicate arrives after identity retention expires | Quarantine or reconcile before another effect | unrun |
| Newer shipment version arrives before older version | Older update rejected or recorded without overwriting | unrun |
| Pause effect commits but acknowledgment fails | Reconcile committed effect before retry | unrun |
| Two controllers race on the same pause intent | One committed effect or explicit conflict | unrun |

**Known unknowns:** real effect identities, retention windows, partition keys,
transaction boundaries, and concurrency behavior.

**Reversal trigger:** any duplicate, reorder, or race produces an unexplained or
repeated committed effect.

## 6. Applied Capacity, Shedding, and Recovery Decision Matrix

### Work-class decisions

| Work class | Proposed overload treatment | Business visibility | Reconciliation | State |
| --- | --- | --- | --- | --- |
| Operations projection | Delay within an explicit staleness window; do not claim freshness | Stale marker and backlog age | Compare eligible roots to applied subject versions | proposed; exercise unrun |
| Partner alert | Never silently discard after acceptance; reject, defer, or quarantine visibly | Partner and operator status | Effect identity and disposition | proposed; exercise unrun |
| Pause policy | Shed only before acceptance under an approved business rule | Explicit policy-evaluation status | Accepted observations versus policy dispositions | proposed; exercise unrun |
| Pause action | Fail closed when authority, evidence, or action budget is unavailable | Operations incident | Pause intent versus committed effect | proposed; exercise unrun |
| Feedback echo | Quarantine when ancestry or generation budget is exhausted | Loop-control evidence | Prior action attempts and effects | proposed; synthetic generation stop observed |

### Frozen synthetic budgets and evidence

| Boundary | EVT-R012 frozen value | Status and limitation |
| --- | ---: | --- |
| Maximum feedback generations | 2 | Scenario assumption; not a safe production threshold |
| Maximum delivery attempts per stimulus | 200 | Scenario assumption; not capacity advice |
| Maximum action attempts per stimulus | 50 | Scenario assumption; not authority or safety evidence |
| Maximum committed effects per stimulus | 8 | Scenario assumption; not an acceptable business-loss limit |
| Maximum event publications per stimulus | 200 | Scenario assumption; not a broker limit |
| Dependency-failure action-stop activations | 0.06768 per stimulus | Observed — EVT-R012 bounded synthetic |
| Dependency-failure delivery-stop activations | 0.01068 per stimulus | Observed — EVT-R012 bounded synthetic |

The stop activations are preserved evidence that the first-order model's
non-binding-budget assumption failed in the synthetic dependency scenario.
They do not establish a Northbridge capacity policy or recovery outcome.

### Planned adverse exercises

| Scenario | Expected evidence | Result |
| --- | --- | --- |
| Sustained exception burst | Explicit accepted, rejected, deferred, and expired counts | unrun |
| Correlated notifier and controller failure | Aggregate retry budget binds without hiding outcome gaps | unrun |
| Circuit repeatedly opens and half-opens | Probe limit prevents recovery flood and echo re-entry | unrun |
| Backlog becomes older than useful alert window | Expiry is visible and reconciled | unrun |
| Live traffic competes with recovery drain | Declared priority and tenant fairness remain visible | unrun |
| Primary generation-depth signal is missing | Action/publication budget provides backup containment | unrun |

**Known unknowns:** real arrival distribution, processing time, correlated
failures, useful-delay windows, fairness policy, backpressure, broker limits,
and business priority.

**Reversal trigger:** accepted work can be shed without a visible disposition
or recovery produces new feedback.

## 7. Applied Asynchronous Evidence and Business Reconciliation Map

### Evidence path

| Stage | Required evidence | What it could prove | What it cannot prove | State |
| --- | --- | --- | --- | --- |
| Declaration | Detector revision, condition, subject, tenant, authority reference, effective time | Which observation was asserted under which context | That the observation was true or authoritative for partner action | proposed; capture unrun |
| Publication | Event identity, semantic revision, causal root, publisher | Which record the publisher attempted to emit | Broker acceptance or consumer behavior | proposed; capture unrun |
| Delivery and processing | Broker identity, delivery attempt, handler revision, outcome | Which technical attempt occurred | One committed business effect | proposed; capture unrun |
| Action attempt | Root identity, action name, actor/delegation, request hash | Which consequential action was attempted | Whether the effect committed | proposed; capture unrun |
| Committed effect | Durable effect identity and authoritative state transition | Which effect the system of record accepted | Human understanding or downstream permanence | proposed; source unknown; unrun |
| Reconciliation | Eligible, accepted, rejected, pending, committed, corrected, and unexplained identities | Whether the named invariant balances within scope | Complete causation if evidence is sampled or missing | proposed; unrun |

Trace and correlation identifiers may help join evidence, but Northbridge must
not treat them as business-causation or authority proof. Evidence sampling,
retention, privacy restriction, and clock uncertainty remain unknown.

### Proposed reconciliation scope

For one root stimulus and action identity, Northbridge proposes to reconcile:

`accepted intents = completed outcomes + explicit rejections + pending items + unresolved gaps`

The identity rules and authoritative sources for every term are still unknown,
so this relationship is a review prompt, not a measured equation.

### Planned reconstruction exercises

| Exercise | Expected answer | Result |
| --- | --- | --- |
| One normal projection update | Root observation through committed subject version | unrun |
| Duplicate partner-alert attempts with one effect | Both attempts plus one effect identity and suppression decision | unrun |
| Pause commits but acknowledgment is lost | One committed pause found before another attempt | unrun |
| Partial fan-out | Each branch has an explicit disposition and owner | unrun |
| Feedback reaches generation stop | Further publication is contained and prior effects reconcile | unrun in an implemented flow; simulator stop observed only |
| Primary telemetry is unavailable | Authoritative ledgers still expose business gap without inventing trace completeness | unrun |
| Privacy retention removes detailed evidence | Permitted aggregate evidence and an explicit reconstruction limit remain | unrun |

**Known unknowns:** acceptance ledger, completion system of record, sampling,
evidence retention, privacy access, clock bounds, and correction process.

**Reversal trigger:** a consequential effect cannot be attributed to an
authorized root intent and tenant, or an accepted intent has no explainable
disposition.

## Integrated evidence and release close

| Question | Current answer | State |
| --- | --- | --- |
| Is the root message an authoritative business fact? | No; the example treats it as a detector observation | proposed composite decision |
| Can the generated implementation begin? | A scaffold may begin only where approved fields exist | proposed; unrun |
| Can the flow be released? | No; authority, acceptance, effect, privacy, replay, capacity, and reconciliation evidence is missing | proposed decision |
| What did EVT-R012 contribute? | Bounded synthetic evidence for count modeling, generation containment, binding budgets, and attempt/effect separation | observed — EVT-R012 bounded synthetic |
| What did EVT-R012 not contribute? | Production semantics, broker behavior, ordering, privacy, recovery, authority, or real business outcomes | explicit experiment boundary |
| What uncertainty most threatens the design? | E5 may recreate an ancestor condition without legitimate new meaning or authority | unknown |
| What reverses the design? | An unbounded or unreconstructable effect, lost tenant/authority context, or an attempted state treated as completed | proposed reversal trigger |

This completed example demonstrates how the tools fit together. It does not
validate the tools, the Northbridge design, or any implementation.
