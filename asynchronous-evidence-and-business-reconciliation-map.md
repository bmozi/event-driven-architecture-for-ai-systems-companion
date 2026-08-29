# Asynchronous Evidence and Business Reconciliation Map

<!-- markdownlint-disable MD013 -->

**Status:** Working template; not practitioner validated

**Purpose:** Connect distributed technical evidence to one named business
outcome without treating logs, traces, acknowledgments, or local success as
complete proof.

Use the
[Event Provenance-and-Causality Record](event-provenance-and-causality-record.md)
to define event ancestry. Use this map to show which permitted evidence can
reconstruct the flow and which business ledger resolves discrepancies.

## 1. Map control and outcome

| Field | Decision |
| --- | --- |
| Map identifier and revision | |
| Root business stimulus | |
| Root causal identity | |
| Subject and tenant | |
| Accepted condition | |
| Completed business outcome | |
| Named invariant | |
| Reconciliation owner | |
| Evidence retention window | |
| Validation state | proposed / unrun |

## 2. Evidence path

Add one row for every material transition. Distinguish a correlation aid from
evidence of causation or commitment.

| Stage | Claim or operation | Evidence producer | Evidence identifier | Causal, correlation, or trace relationship | Storage and retention | Sampling or loss condition | Access and privacy boundary | What it proves | What it cannot prove |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Declaration | | | | | | | | | |
| Publication | | | | | | | | | |
| Broker acceptance | | | | | | | | | |
| Delivery or receive | | | | | | | | | |
| Processing attempt | | | | | | | | | |
| Output publication | | | | | | | | | |
| Action attempt | | | | | | | | | |
| Committed effect | | | | | | | | | |
| Reconciliation | | | | | | | | | |

## 3. Evidence quality and completeness

| Question | Decision or evidence | State | Stop or escalation condition |
| --- | --- | --- | --- |
| Which records are authoritative for acceptance? | | unknown | |
| Which records are authoritative for completion? | | unknown | |
| Are trace or telemetry records sampled? | | unknown | |
| Can transformations preserve root ancestry? | | unknown | |
| Can actor, subject, tenant, and delegated authority be reconstructed? | | unknown | |
| Can duplicate attempts be separated from distinct effects? | | unknown | |
| Can missing evidence be distinguished from missing work? | | unknown | |
| Are privacy deletion or retention limits expected to create evidence gaps? | | unknown | |
| Is clock uncertainty recorded? | | unknown | |
| Can operators query evidence during dependency failure? | | unknown | |

## 4. Business reconciliation equation and scope

Define identities and inclusion rules before adding counts.

| Term | Identity and scope | Expected source | Count or state | Evidence status |
| --- | --- | --- | ---: | --- |
| Eligible stimuli | | | | unrun |
| Accepted stimuli | | | | unrun |
| Explicitly rejected stimuli | | | | unrun |
| Deferred or quarantined stimuli | | | | unrun |
| Action attempts | | | | unrun |
| Distinct committed effects | | | | unrun |
| Corrected or compensated effects | | | | unrun |
| Completed business outcomes | | | | unrun |
| Unexplained gap | | | | unrun |

**Reconciliation relationship:**

**Permitted tolerance and why:**

**Deadline after which a gap becomes an incident:**

**System of record for discrepancy disposition:**

## 5. Reconstruction exercise

| Challenge | Expected answer or safe behavior | Result | Missing evidence | Privacy or retention countercondition | Required repair |
| --- | --- | --- | --- | --- | --- |
| Trace one successful outcome | | unrun | | | |
| Trace one duplicate attempt with one effect | | unrun | | | |
| Trace one unknown external outcome | | unrun | | | |
| Trace one partial fan-out | | unrun | | | |
| Trace one reordered or stale event | | unrun | | | |
| Trace one shed or expired item | | unrun | | | |
| Trace one replayed item | | unrun | | | |
| Trace one feedback stop | | unrun | | | |
| Reconstruct when primary telemetry is unavailable | | unrun | | | |

## 6. Incident and correction path

| Gap type | Detection | Containment | Correction or compensation | Authority | Evidence preserved |
| --- | --- | --- | --- | --- | --- |
| Accepted but no completed outcome | | | | | |
| Effect without accepted stimulus | | | | | |
| Duplicate committed effect | | | | | |
| Conflicting outcomes | | | | | |
| Unattributed actor, tenant, or authority | | | | | |
| Unreconstructable due to missing or deleted evidence | | | | | |

## 7. Close

**Evidence accepted:**

**Negative evidence retained:**

**Known unknowns:**

**Known blind spots:**

**Reversal trigger:**

**Safe operational response:**

**Decision:** insufficient evidence / revise / exercise / bounded release / release

This map proves no more than the retained evidence can support. Complete local
telemetry can coexist with a missing, duplicated, or unauthorized business
outcome; reconciliation must remain a separate evidence layer.
