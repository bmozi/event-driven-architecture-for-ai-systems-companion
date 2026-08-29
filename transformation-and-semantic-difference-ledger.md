# Transformation and Semantic-Difference Ledger

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Decide whether routing, filtering, normalization, enrichment,
redaction, aggregation, or derivation preserves a claim, changes its
representation, or creates a new claim requiring new authority.

Use one row per transformation stage. Link consequential outputs to the
[Event Provenance-and-Causality Record](event-provenance-and-causality-record.md).

## 1. Ledger control

| Field | Value |
| --- | --- |
| Ledger identifier and revision | |
| Input event type and semantic revision | |
| Input declarer and contract owner | |
| Business subject and tenant boundary | |
| Flow or implementation brief | |
| Ledger owner and reviewers | |
| Validation state | proposed / unrun |

## 2. Transformation inventory

| Stage | Transformation type | Input revision | Policy, code, model, or mapping revision | Output event or view | Executor | Output declarer or authority | Evidence state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | route / filter / normalize / enrich / redact / aggregate / derive | | | | | | proposed / unrun |

## 3. Field-level semantic differences

Add rows for copied fields as well as changed, defaulted, derived, or removed
fields. A mechanically unchanged value can still acquire a different meaning in
a new temporal or authority context.

| Stage | Input field and meaning | Output field and meaning | Operation | Unknown/null/absent/redacted handling | Time or version used | Information lost | Privacy or purpose change | Semantic-equivalence decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | copy / rename / convert / default / join / infer / remove | | | | | preserved / changed / unknown |

## 4. Claim and authority decision

| Question | Decision and rationale | Evidence | Unknown or countercondition |
| --- | --- | --- | --- |
| Does the output assert the same fact? | | | |
| Did the subject, scope, tenant, or granularity change? | | | |
| Did current data enrich a historical fact? | | | |
| Did the effective or observed time change? | | | |
| Did an observation become an inference, recommendation, command, or fact? | | | |
| Is the transformer now a new declarer? | | | |
| Does the output require a new event identifier or semantic revision? | | | |
| Which consumer inferences changed? | | | |
| Which original provenance must remain available? | | | |

## 5. AI-generated or model-derived transformation

| Field | Value or rule |
| --- | --- |
| Model, agent, tool, and version | |
| Prompt, mapping, policy, or plan revision | |
| Context and retrieval sources | |
| Output category | observation / inference / recommendation / command / fact |
| Human decision authority | |
| Confidence or evaluation and its limits | |
| Behavior when evidence is missing or conflicting | |
| Generation and action stop | |

Confidence, fluent output, and a passing schema check do not grant business
authority.

## 6. Semantic-difference mutations

| Mutation | Expected decision or invariant | Detection layer | Result | Evidence location | What remains unknown |
| --- | --- | --- | --- | --- | --- |
| `unknown` becomes zero or false | | | unrun | | |
| absent becomes not applicable | | | unrun | | |
| source time replaced with processing time | | | unrun | | |
| current enrichment applied during historical replay | | | unrun | | |
| source authority removed or replaced | | | unrun | | |
| tenant or subject identifier remapped | | | unrun | | |
| field remains schema-valid but changes business meaning | | | unrun | | |
| AI inference labeled as an authoritative fact | | | unrun | | |
| Custom mutation | | | unrun | | |

## 7. Operational and lifecycle consequences

| Concern | Decision | Owner | Evidence state |
| --- | --- | --- | --- |
| Duplicate and ordering behavior | | | proposed / unrun |
| Backfill and replay transformation revision | | | proposed / unrun |
| Correction and supersession | | | proposed / unrun |
| Materialized-view rebuild | | | proposed / unrun |
| Retention and deletion of source and derived copies | | | proposed / unrun |
| Failure, quarantine, and reconciliation | | | proposed / unrun |

## 8. Close

**Supported evidence:**

**Negative evidence:**

**Known unknowns:**

**Decision:** preserve / new representation / new claim / reject / unresolved

**Reversal trigger:**

**Safe response if the assumption is wrong:**

Completing this ledger documents the intended semantic relationship. It does
not validate the transformation implementation or prove consumer understanding.
