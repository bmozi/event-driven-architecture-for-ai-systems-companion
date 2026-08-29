# Event Provenance-and-Causality Record

**Status:** Working template; not yet practitioner validated
**Purpose:** Preserve enough authority, lineage, causality, time, and
transformation context to explain a consequential event without pretending an
identifier proves more than it does.

Use this record to design required fields and evidence paths. Do not place
protected or unnecessary data in an event merely because a template asks for it.

## 1. Event identity

| Field | Value or design rule |
| --- | --- |
| Event identifier and uniqueness scope | |
| Event type and semantic revision | |
| Subject and subject-version boundary | |
| Business declarer | |
| Technical publisher | |
| Occurred or effective time | |
| Recorded time | |
| Published time | |

## 2. Authority provenance

| Question | Decision or evidence reference |
| --- | --- |
| Which actor or system caused the declaration? | |
| Under which tenant, contract, policy, or delegated authority? | |
| Which source established the fact? | |
| Was authority valid at effective time? | |
| Who approved a correction, override, or manual declaration? | |
| What must consumers not infer from publisher identity? | |

## 3. Causal structure

| Relationship | Identifier or rule | What the relationship proves | What it does not prove |
| --- | --- | --- | --- |
| Direct causal parent | | | |
| Root business stimulus | | | |
| Initiating command or intent | | | |
| Correlation group | | | |
| Trace context | | | |
| Workflow or transaction context | | | |
| Supersedes or corrects | | | |
| Derived from | | | |

Correlation, shared trace context, or temporal proximity is not by itself proof
of business causation.

## 4. Transformation lineage

Add one row per intermediary that routes, filters, normalizes, enriches,
redacts, aggregates, or derives.

| Stage | Input revision | Transformation or policy revision | Fields added, removed, or changed | Authority of derived claim | Output identifier | Evidence location |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

**Original event retained or referenced:**

**Semantic difference test:**

**Unknown, absent, null, redacted, and not-applicable treatment:**

## 5. AI and agent provenance

Complete when generated inference, content, routing, or action participates.

| Field | Value or reference |
| --- | --- |
| Model or agent identity and version | |
| Policy, prompt, plan, or instruction revision | |
| Context and memory source references | |
| Retrieval or tool evidence references | |
| Output category: observation, inference, recommendation, command, or fact | |
| Human review and decision authority | |
| Action budget and stop condition | |
| Evaluation or confidence value and its limits | |

Confidence does not establish authority, causation, or truth.

## 6. Access, purpose, and lifecycle

| Field | Decision |
| --- | --- |
| Classification and minimization | |
| Allowed consumer groups | |
| Allowed purpose by group | |
| Geographic or contractual boundary | |
| Retention and deletion | |
| Backup, materialization, and derived-copy handling | |
| Replay eligibility and authority | |
| Audit access and separation of duties | |

## 7. Reconstruction test

Choose one consequential outcome and attempt to answer:

1. What happened?
2. Who or what had authority to declare it?
3. Which fact or intent directly caused it?
4. Which transformations changed representation or meaning?
5. Which version and temporal claims applied?
6. Which human, AI, and system participants contributed?
7. Which reactions followed, and were they allowed?
8. Which parts cannot be reconstructed from permitted evidence?

**Result:** passed / failed / partial
**Unreconstructable edges:**
**Privacy or retention limits:**
**Required correction:**
**Reversal trigger:**
