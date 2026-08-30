# Blinded Practitioner Test Packet

<!-- markdownlint-disable MD013 -->

**Packet version:** `events-tools-blinded-v1-2026-08-29`

**Execution status:** Ready to run; no session has occurred

**Tools under test:**

- [Event Meaning-and-Authority Record](../event-meaning-and-authority-record.md)
- [Event Flow and AI Implementation Brief](../event-flow-and-ai-implementation-brief.md)

**Purpose:** Learn whether a practitioner can use the two tools without chapter
context or facilitator coaching, where the field language causes confusion,
and whether the tools expose consequential missing decisions before a proposed
implementation proceeds.

This packet tests tool usability in one fictional exercise. It is not a test of
the participant, an experiment proving architectural effectiveness, or evidence
that either tool is validated.

## Packet contents and separation

### Participant-facing files

Share only these files and writable copies of the two tools:

1. [Consent and privacy boundaries](participant/CONSENT-AND-PRIVACY.md)
2. [Harborlight participant scenario](participant/SCENARIO.md)
3. [Participant response workbook](participant/RESPONSE-WORKBOOK.md)

Do not share the facilitator or scoring files until the participant has
submitted the final response. The scenario contains no Northbridge details and
does not name the architectural diagnoses the tools are intended to reveal.

### Facilitator and scoring files

1. [Neutral facilitator guide](facilitator/FACILITATOR-GUIDE.md)
2. [Observation rubric](facilitator/OBSERVATION-RUBRIC.md)
3. [Scoring and decision rubric](facilitator/SCORING-AND-DECISION-RUBRIC.md)
4. [Results-log template](facilitator/RESULTS-LOG-TEMPLATE.md)

Where practical, use a separate blinded scorer who receives the coded response,
scenario, rubrics, tool versions, and protocol-deviation record but not the
participant's identity, employer, or facilitator impressions.

## Roles

| Role | Responsibility | Must not do |
| --- | --- | --- |
| Participant | Use the tools and workbook on the fictional scenario | Supply real employer, customer, system, incident, or secret information |
| Facilitator | Preserve timing, neutrality, consent, and stop conditions | Teach target concepts, repair answers, or score during the session |
| Observer | Record behavior and exact clarification requests | Infer motives or turn observations into coaching |
| Scorer | Apply the frozen rubric to coded artifacts | Use participant identity, seniority, or employer reputation |
| Packet owner | Retain negative results and decide revisions | Claim validation from one session or discard confusing responses |

One person may serve as facilitator and observer, but scoring should be delayed
until the response is final.

## Ready-to-run sequence

| Segment | Time | Material | Facilitator behavior |
| --- | ---: | --- | --- |
| Consent and privacy | 5 minutes | Consent file | Confirm voluntary participation and the no-secrets boundary |
| Scenario read | 8 minutes | Scenario only | Answer logistics, not architectural questions |
| Tool A | 18 minutes | Writable Tool A and workbook | Observe without explaining fields |
| Tool B | 20 minutes | Writable Tool B and workbook | Observe without explaining fields |
| Challenge | 8 minutes | Facilitator reads the frozen challenge card | Allow revisions; give no hints |
| Retrospective | 6 minutes | Workbook | Ask the frozen neutral questions |
| **Total** | **65 minutes** | | |

Record actual elapsed time. Do not rush a participant to create artificial
completion; mark unfinished sections and preserve why they were unfinished.

## Pre-session setup

- [ ] Assign a participant code that contains no name, employer, or email.
- [ ] Freeze and record packet and tool versions.
- [ ] Create writable copies of both tools labeled with participant code only.
- [ ] Confirm the participant has not read the facilitator or scoring files.
- [ ] Disable recording unless separately approved and explicitly accepted.
- [ ] Remove document metadata that could identify prior participants.
- [ ] Confirm a private workspace and a method for the participant to withdraw.
- [ ] Prepare the challenge card without revealing it early.
- [ ] Decide retention, access, and destruction dates before collecting data.

## Stop conditions

Stop the session and record only the minimum necessary reason when:

- consent is declined or withdrawn;
- the participant begins sharing employer, customer, production, incident,
  security, personal, contractual, or otherwise confidential information;
- the participant requests a break or shows discomfort;
- the wrong tool or packet version is used;
- a required file is inaccessible or writable responses cannot be preserved;
- the facilitator accidentally reveals the scoring key or teaches an answer;
- recording occurs without the agreed permission; or
- the time boundary is reached and the participant chooses not to continue.

If secret information is disclosed, stop transcription, ask the participant not
to continue that disclosure, quarantine the affected artifact, and follow the
predeclared deletion process. Do not copy the secret into the results log.

## Evidence and decision boundary

Permitted session statements are limited to:

- the participant completed, skipped, misunderstood, or questioned a named
  field under this scenario and protocol;
- the frozen challenge caused a stated revision or did not;
- the facilitator used a recorded neutral clarification or deviated; and
- the scorer assigned rubric values with a retained rationale.

The packet cannot establish tool effectiveness across roles, domains, teams, or
production systems. A smooth session is not validation. Confusion, skipped
fields, incorrect confident answers, unfinished work, and disagreement are
valuable results and must be retained.

## Post-session close

1. Participant submits final coded artifacts.
2. Facilitator marks protocol deviations and stops without scoring answers.
3. Observer completes the rubric using behavior, not interpretation.
4. Scorer independently applies the scoring rubric.
5. Packet owner logs positive and negative findings without participant identity.
6. Any proposed tool revision receives a new version and another test; do not
   rewrite the artifact that produced the finding.
7. Destroy or retain materials according to the accepted privacy boundary.

**Current result:** unexecuted; no participant data, score, observation, or
usability claim exists.

## Separate reader-value packet

The [Events Reader-Value Pilot Packet](events-reader-value-v1/README.md),
currently version 1.2.5, is a separately versioned, prepared, and human-unrun
protocol for the newer role-transfer,
multiplier, loop, value-ledger, and decision-owner materials. It does not
change this packet's two-tool scope or inherit any result from it.
