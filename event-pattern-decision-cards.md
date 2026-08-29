# Event Pattern Decision Cards

**Status:** Working card set; not yet practitioner validated
**Purpose:** Select patterns by the invariant they protect, the assumptions they
make, and the failure surface they create.

Copy the blank card for a design review. The compact starter cards are prompts,
not complete pattern definitions or vendor instructions.

## Blank pattern card

**Pattern:**
**Business pressure:**
**Fact and subject:**
**Invariant protected:**
**Authority and owner:**
**Why this pattern fits:**
**Counterconditions—when not to use it:**
**New semantic or operational failure surface:**
**Traffic, cost, and action multiplication:**
**Duplicate, order, replay, and evolution behavior:**
**Privacy, retention, and provenance consequence:**
**What AI can generate:**
**What humans must define:**
**Positive evidence:**
**Negative or mutation evidence:**
**Operational evidence and reconciliation:**
**Remaining uncertainty:**
**Reversal trigger:**

## Routing and filtering

- **Protects:** delivery to eligible recipients under explicit business and
  policy conditions.
- **Use when:** recipients or paths legitimately differ by stable event context.
- **Watch for:** silent drops, leaked tenants, hidden business rules, duplicated
  filters, and lost provenance.
- **Disprove with:** unauthorized-recipient, missing-context, stale-policy, and
  visible-drop tests.

## Normalization

- **Protects:** a deliberate shared representation across source forms.
- **Use when:** semantic equivalence is owned and testable.
- **Watch for:** canonical ambiguity, loss of source nuance, new central
  authority, and `unknown` collapsed into a value.
- **Disprove with:** semantic counterexamples and source-to-canonical round-trip
  or difference tests.

## Enrichment

- **Protects:** consumer access to necessary context at a stated version and time.
- **Use when:** source authority, freshness, failure, privacy, and reprocessing
  semantics are explicit.
- **Watch for:** current context applied to historical facts, stale cache,
  unavailable source, and enlarged privacy surface.
- **Disprove with:** source-version, missing-source, stale-source,
  unauthorized-source, and replay tests.

## Claim check

- **Protects:** reference to data too large, sensitive, or independently managed
  to carry in the event.
- **Use when:** reference lifetime, access, version, availability, and deletion
  align with consumer use.
- **Watch for:** broken historical replay, reference expiry, authorization drift,
  and mutable content under stable identity.
- **Disprove with:** expired, deleted, mutated, unauthorized, and unavailable
  reference tests.

## Materialized state

- **Protects:** queryable derived state for a named use at an understood lag.
- **Use when:** projection ownership, correction, rebuild, and staleness behavior
  are explicit.
- **Watch for:** projection mistaken for source authority, silent gaps,
  irreproducible rebuilds, and order assumptions.
- **Disprove with:** duplicate, reorder, late, missing, correction, and rebuild tests.

## Splitter and fan-out

- **Protects:** independent treatment of explicit child subjects or reactions.
- **Use when:** causal ancestry, expected branches, ownership, and multiplication
  are bounded.
- **Watch for:** invisible traffic growth, lost parent identity, inconsistent
  partial success, and authorization expansion.
- **Disprove with:** missing-child, duplicate-child, unauthorized-branch, and
  multiplier tests.

## Aggregator

- **Protects:** a defined result over a known or discoverable group.
- **Use when:** membership, completeness, deadline, late arrival, and partial
  outcome are business-defined.
- **Watch for:** unbounded state, poisoned groups, false completeness, and hidden
  workflow responsibility.
- **Disprove with:** missing, duplicate, late, conflicting, expired, and unknown
  membership tests.

## Scatter-gather

- **Protects:** a bounded comparison or combined answer from multiple responders.
- **Use when:** responders, deadline, partial-answer semantics, and cancellation
  are explicit.
- **Watch for:** fan-out cost, slowest-responder coupling, duplicated action, and
  request-response disguised as facts.
- **Disprove with:** timeout, partial, conflicting, retry, and cancellation tests.

## Transactional outbox

- **Protects:** durable intent to publish alongside a local state change.
- **Use when:** local atomicity is required and relay duplication is handled.
- **Watch for:** claims of end-to-end exactly-once outcome, relay backlog,
  ordering assumptions, and unpublished poison records.
- **Disprove with:** failure before/after commit, relay duplicate, stalled relay,
  and consumer-side-effect tests.

## Saga or compensating reactions

- **Protects:** explicit response to distributed partial outcomes.
- **Use when:** each fact, action, compensation, terminal state, and owner is named.
- **Watch for:** compensation presented as rollback, ownership dispersed across
  reactions, and unbounded waiting.
- **Disprove with:** compensation failure, duplicate compensation, changed
  policy, human delay, and reconciliation tests.

## Backfill and replay

- **Protects:** authorized re-delivery or reconstruction for a stated purpose.
- **Use when:** range, version, effects, idempotency, dry run, abort, and
  reconciliation are explicit.
- **Watch for:** historical facts causing unauthorized present-day effects,
  current enrichment, expired authority, and privacy violations.
- **Disprove with:** effect enumeration, old/new consumer comparison, abort, and
  live-side-effect-disabled tests.

## Throttle, shed, and circuit break

- **Protects:** bounded capacity and recoverability under load or dependency failure.
- **Use when:** business priority, loss, delay, recovery, and reconciliation are defined.
- **Watch for:** silent business loss, retry storms, unfair tenants, and recovery loops.
- **Disprove with:** correlated failure, prolonged backlog, oscillating circuit,
  fallback, and end-to-end reconciliation tests.

## Card review close

1. What must remain true?
2. Who owns the new failure surface?
3. What can multiply?
4. What evidence would make us reject this pattern?
