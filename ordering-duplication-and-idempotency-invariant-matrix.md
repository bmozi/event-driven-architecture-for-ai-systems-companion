# Ordering, Duplication, and Idempotency Invariant Matrix

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Define which business invariant must survive duplicated,
reordered, delayed, stale, retried, and concurrent event handling without
treating a transport guarantee as proof of one business outcome.

Use one row per consequential handler or projection. Pair attempt evidence with
committed-effect evidence; the two are not interchangeable.

## 1. Matrix control

| Field | Decision |
| --- | --- |
| Matrix identifier and revision | |
| Event type and semantic revision | |
| Business subject and tenant | |
| Consumer or handler | |
| Business invariant owner | |
| Transport product, mode, and version | |
| Transactional resources in scope | |
| External resources outside the transaction | |
| Validation state | proposed / unrun |

## 2. Guarantee-scope statement

| Claim | Exact scope | Configuration or identity | Expiry or countercondition | Evidence source | What it does not prove |
| --- | --- | --- | --- | --- | --- |
| Delivery | | | | | |
| Ordering | | | | | |
| Producer deduplication or idempotence | | | | | |
| Consumer idempotency | | | | | |
| Transactional processing | | | | | |
| Business reconciliation | | | | | |

Do not write *ordered*, *idempotent*, *transactional*, or *exactly once*
without completing every column in the applicable row.

## 3. Business invariant matrix

| Handler or effect | Named business invariant | Subject and version boundary | Order scope and key | Duplicate identity | Idempotency retention | Concurrency rule | Committed-effect boundary | Reconciliation source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

**Acceptance-versus-completion distinction:**

**Unknown-outcome behavior:**

**Correction, supersession, or stale-write rule:**

## 4. Mutation plan and results

Add concrete identifiers and schedules. “Duplicate test” is not sufficient.

| Mutation | Input schedule | Expected invariant-preserving behavior | Attempt evidence | Committed-effect evidence | Reconciliation result | State |
| --- | --- | --- | --- | --- | --- | --- |
| Same message identifier delivered twice | | | | | | unrun |
| Different message identifiers express the same intent | | | | | | unrun |
| Duplicate arrives after deduplication retention expires | | | | | | unrun |
| Newer subject version arrives before older version | | | | | | unrun |
| Related subjects arrive on different partitions | | | | | | unrun |
| Two consumers race to commit the same effect | | | | | | unrun |
| Effect commits but acknowledgment fails | | | | | | unrun |
| Local state commits but external effect is ambiguous | | | | | | unrun |
| Correction races with original event | | | | | | unrun |

## 5. Failure disposition

| Detected condition | Reject | Ignore as duplicate | Delay | Quarantine | Reconcile | Compensate | Escalate | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Duplicate within identity scope | | | | | | | | |
| Duplicate outside identity window | | | | | | | | |
| Stale subject version | | | | | | | | |
| Missing ordering or version context | | | | | | | | |
| Concurrency conflict | | | | | | | | |
| Unknown external outcome | | | | | | | | |
| Reconciliation discrepancy | | | | | | | | |

## 6. Evidence close

| Field | Value |
| --- | --- |
| Positive evidence | |
| Negative or boundary evidence | |
| Known unknowns | |
| Untested interleavings | |
| Missing evidence that blocks release | |
| Reversal trigger | |
| Safe disable or quarantine action | |
| Decision: reject / revise / bounded release / release | |

A passing broker or schema test cannot prove the invariant. The proof claim must
remain bounded to the identities, interleavings, resources, and evidence that
were actually exercised.
