# Northbridge Data-Structures Architecture Bridge

**Status:** Constructed teaching example; `PLANNED/UNRUN`

**Disclosure:** Northbridge Exchange, its warehouse, records, quantities,
workload, and outcomes are fictional composite teaching material. They are not
production measurements or John Briggs project history.

## The structure does not define the event

Northbridge may use a hash index for current inventory, a deque for routine
picking, a heap for urgent orders, and a graph for routes. Those structures
help services work efficiently. They do not determine whether a message means
`ReserveInventory` (intent), `InventoryReserved` (declared fact), a notification,
or a materialized state view.

The durable event should carry business meaning and causal identity. A rebuilt
index may restore a projection; it must not silently invent a new inventory
change. A replay may rebuild analytical state; it must not create a second
shipment unless replay is explicitly authorized for that effect.

## Plain-language model: the journal and the whiteboard

The event history is the warehouse journal. A materialized view is the
whiteboard used to answer today's questions quickly. If the whiteboard is
erased, the journal can rebuild it. Rewriting the whiteboard must not make the
loading dock ship the same order again.

```text
receiving/shipping effect -> durable event with identity and causality
                          -> idempotent consumer -> current-state projection

replay -> historical events -> projection-only path
                            X-> live effect without fresh authority
```

| Structure | Failure question for the event design |
| --- | --- |
| Hash index | Was the index stale when the event was produced? |
| Deque | What happens to acknowledged or unacknowledged work after worker loss? |
| Heap | How are stale priorities and duplicate entries handled? |
| Graph | Which route version and layout produced the decision? |

## Transfer artifact: replay-and-rebuild record

| Decision | Your answer |
| --- | --- |
| Occurrence and authorized declarer | |
| Event, correlation, and causation identities | |
| Durable source and rebuildable projections | |
| Idempotency and duplicate-handling rule | |
| Replay-safe consumers | |
| Effects requiring fresh authorization | |
| Evidence that replay created no new effect | |

## AI-amplified transfer to other systems

AI tools can generate candidate structures, implementation code, tests, and
diagrams for many domains. The architect supplies the governing decisions the
generated machinery must preserve.

| Transfer case | AI may draft candidates for | Decision the structure cannot settle |
| --- | --- | --- |
| Search-engine indexing | Crawlers, inverted indexes, ranking code, query tests | Content authority, freshness, deletion, ranking policy, and evidence |
| Social-media platforms | Social graphs, feeds, queues, moderation classifiers | Consent, identity, amplification limits, appeal, and causal responsibility |
| Blockchain systems | Transaction parsing, Merkle proofs, graph analysis, contract tests | Signing authority, finality assumptions, off-chain governance, and reversal limits |
| Recommendation systems | Feature pipelines, candidate retrieval, ranking, evaluation | Permitted inputs, objective, fairness, explanation, and user control |
| Online food delivery | Route graphs, order queues, dispatch heaps, ETA models | Order and payment authority, worker custody, retry safety, refunds, and recovery |

Generated machinery still needs approved meaning, authority, failure behavior,
and evidence. This example does not measure implementation speed or quality.
Current rebuild permission must cover its purpose, source slice, and target;
historical identity alone does not authorize replay.

> **Why we did not choose every structure**
>
> Autocomplete systems help predict partial search terms, but Northbridge does
> not need them for core inventory and order operations. Huffman coding
> compresses data, but it does not solve event identity, replay, idempotency,
> routing, or fault tolerance. Choose structures because the problem requires
> their behavior—not because a course or catalog happens to mention them.
