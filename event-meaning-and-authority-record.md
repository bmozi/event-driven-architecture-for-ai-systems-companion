# Event Ontology and Meaning-and-Authority Record

## Ten-minute first pass

Before filling the full record, complete these six lines in plain language:

1. **Something happened:**
2. **It happened to or for:**
3. **The party allowed to declare it is:**
4. **A consumer may now rely on:**
5. **A consumer must not assume:**
6. **We would detect a wrong declaration by:**

If two reasonable readers complete any sentence differently, the event is not
ready to multiply across consumers. Resolve the meaning before generating the
schema, producer, route, or handler.

### Miniature example

| First-pass line | Northbridge answer |
| --- | --- |
| Something happened | A named inventory allocation became a committed hold under the stated policy and contract revision. |
| It happened to or for | One order line, buyer, product, location, quantity, and commitment period. |
| Allowed declarer | The allocation authority; the event publisher may transmit the declaration but does not create the business authority. |
| Consumer may rely on | The stated units are committed under the recorded limits until they expire, are released, or are corrected under the contract. |
| Consumer must not assume | The order shipped, the buyer received the goods, or every reservation request succeeded. |
| Wrong-declaration evidence | The event cannot be reconciled to the authoritative allocation record, policy version, subject, quantity, or effective time. |

See the
[complete Northbridge event-system example](examples/northbridge-events-integrated-example.md)
for the full record in context and the limits of the constructed case.

## Plain-language vocabulary

- **Subject:** the order, allocation, shipment, account, or other thing the fact
  is about.
- **Predicate:** what became true about that subject.
- **Declarer:** the business authority accountable for saying the fact is true.
- **Publisher:** the technical participant that places the declaration on the
  delivery path; it may act for the declarer.
- **Effective time:** when the fact begins to matter to the business.
- **Invariant:** a truth that must survive duplication, delay, reordering,
  transformation, or replay.
- **Permitted inference:** what a consumer may safely conclude from the event.
- **Correlation:** evidence that records belong to the same investigation or
  flow; it does not by itself prove that one caused another.

**Status:** Working template; not yet practitioner validated
**Purpose:** Decide what a message declares before generating schemas,
producers, consumers, routes, or tests.

Use one record per semantic event type. A field left unknown is a design decision
to resolve or an explicit stop condition—not an invitation for a generator to
invent an answer.

## 1. Identity

| Field | Decision |
| --- | --- |
| Working event name | |
| Domain and bounded context | |
| Business subject and subject identifier | |
| Plain-language fact | |
| Why another party needs to know | |
| Contract owner | |
| Change authority | |

## 2. Semantic category

Select one primary category and explain borderline cases.

- [ ] Business fact: something authoritative occurred.
- [ ] Observation: a participant measured or detected a condition.
- [ ] Notification: a recipient's attention is requested; authority may live elsewhere.
- [ ] Command: a recipient is asked to attempt an action.
- [ ] Database change or CDC record: storage changed; business meaning may be separate.
- [ ] Delta: a value changed relative to a known base.
- [ ] Snapshot or event-carried state: state is transferred as of a stated time.
- [ ] Other, explicitly defined:

**Why this category is honest:**

**What the message does not declare:**

## 3. Occurrence and truth

| Question | Decision |
| --- | --- |
| What occurred? | |
| What conditions make the fact true? | |
| What invariant must already hold? | |
| What makes the fact final, provisional, corrected, or revocable? | |
| Which source is authoritative if records disagree? | |
| Which consumer inferences are permitted? | |
| Which tempting inferences are prohibited? | |

## 4. Authority and ownership

| Question | Decision |
| --- | --- |
| Business declarer | |
| Technical publisher, if different | |
| Actor whose action contributed | |
| Subject or party affected | |
| Tenant or authority boundary | |
| Delegated authority or policy reference | |
| Evidence that authority was valid at declaration time | |
| Who resolves disputes or corrections? | |

Do not treat topic write permission as proof of business authority.

## 5. Time and causality

| Field | Meaning and source |
| --- | --- |
| Occurred or effective time | |
| Recorded time | |
| Published time | |
| Expected clock uncertainty | |
| Causal parent or initiating intent | |
| Correlation or trace context | |
| Sequence or subject version | |
| Late-arrival rule | |

## 6. Contract and evolution

| Field | Decision |
| --- | --- |
| Semantic version or revision | |
| Schema and envelope reference | |
| Required versus optional fields | |
| Null, unknown, absent, redacted, and not-applicable meanings | |
| Syntactic compatibility promise | |
| Semantic and behavioral compatibility promise | |
| Authorization and temporal compatibility promise | |
| Correction and supersession mechanism | |
| Deprecation and consumer migration evidence | |

## 7. Allowed reaction and failure

| Question | Decision |
| --- | --- |
| Who may consume, for which purpose? | |
| Which reactions are allowed? | |
| Which reactions require separate authority? | |
| Duplicate behavior | |
| Reordering and stale-event behavior | |
| Unknown-outcome behavior | |
| Replay and backfill behavior | |
| Maximum useful delay or expiry | |
| Prohibited feedback path | |
| Stop, shed, quarantine, and escalation conditions | |

## 8. Data and governance

| Field | Decision |
| --- | --- |
| Classification by field | |
| Minimization decision | |
| Consumer entitlement and purpose | |
| Residency or contractual boundary | |
| Retention and deletion | |
| Legal hold or audit dependency | |
| Transformation and derived-data obligations | |

## 9. Evidence gate

| Claim | Evidence | What it does not prove | Owner | State |
| --- | --- | --- | --- | --- |
| Meaning is unambiguous to representative consumers | | | | planned |
| Declarer authority is valid and reviewable | | | | planned |
| Duplicate and reorder invariants survive | | | | planned |
| Compatibility survives representative change | | | | planned |
| Replay cannot repeat prohibited effects | | | | planned |
| Allowed reaction and feedback boundaries hold | | | | planned |
| Business outcome can be reconciled | | | | planned |

## 10. AI generation boundary

**AI may generate:**

**AI must not invent:**

**Unknowns that stop generation or release:**

**Required provenance for generated artifacts:**

**Required human reviewers and approval authority:**

## Design-review close

- What fact are we declaring?
- Who has authority to declare it?
- What may consumers safely infer and do?
- What evidence would convince us this record is wrong?

Give only the six first-pass lines to someone outside the producing team. Ask
them to restate the fact, name who may declare it, identify one permitted
reaction, and identify one conclusion the event does not support. If they need
the topic name, source code, or an old meeting to answer, the contract is not
yet clear enough to publish.
