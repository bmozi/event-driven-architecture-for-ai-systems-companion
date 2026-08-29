# Scoring and Tool-Decision Rubric

<!-- markdownlint-disable MD013 -->

**Packet version:** `events-tools-blinded-v1-2026-08-29`

**Status:** Frozen scoring proposal; unexecuted and not validated

Score the coded final artifacts after the session. Prefer a scorer who does not
know participant identity, employer, title, or facilitator impressions.

## Scoring scale

| Score | Artifact evidence |
| ---: | --- |
| 0 | Missing, contradicted by the artifact, or a confident answer creates the hidden risk |
| 1 | Risk or decision is noticed but incomplete, ambiguous, or not operationally usable |
| 2 | Explicit, internally consistent, bounded, and connected to owner, evidence, or stop where applicable |
| N/A | Dimension truly does not apply; scorer must justify exclusion |

Do not award points for wording alone. The response may use different language
if the decision is clear. Do not subtract points for marking information
unknown when the scenario does not provide it; score whether the unknown and
its consequence are handled.

## Tool A dimensions

| ID | Dimension | Two-point evidence | Critical? | Score | Rationale and artifact reference |
| --- | --- | --- | --- | ---: | --- |
| A1 | Message identity | Treats the high reading, equipment request or activity, and approved display condition as different statements | yes | | |
| A2 | Truth conditions | States what would make each retained statement true and what remains provisional | yes | | |
| A3 | Role separation | Separates gateway/platform operation, conservation sign-off, facilities operation, and loan communication decisions | yes | | |
| A4 | Recipient reliance | States what dashboard and lender users may and may not conclude | yes | | |
| A5 | Time and correction | Addresses late or corrected readings and distinguishes relevant times | no | | |
| A6 | Missing-value behavior | Refuses to silently turn a missing reading into a meaningful number or status | yes | | |
| A7 | External access and purpose | Limits lender information to an approved purpose and fields | no | | |
| A8 | Repeated-message behavior | Does not infer a new physical outcome merely because the message appears again | yes | | |
| A9 | Evidence gate | Names evidence needed for sign-off, equipment result, recipient status, or a stop | no | | |
| A10 | Unknown discipline | Keeps absent owner, policy, and evidence answers visible rather than inventing them | yes | | |

**Tool A subtotal:** / applicable maximum 20

## Tool B dimensions

| ID | Dimension | Two-point evidence | Critical? | Score | Rationale and artifact reference |
| --- | --- | --- | --- | ---: | --- |
| B1 | Start and outcome | Names a bounded start and separates acceptance, attempt, physical change, and approved completion | yes | | |
| B2 | Complete flow | Includes dashboard, adapter, controller response, later reading, lender portal, archive, and repeated send | no | | |
| B3 | Owners and permissions | Assigns distinct owners or marks them unknown; does not use platform access as business permission | yes | | |
| B4 | Allowed generation | Gives AI concrete scaffolding it may produce from approved inputs | no | | |
| B5 | Prohibited invention | Prevents AI from choosing missing policy, owner, recipient, status, or outcome decisions | yes | | |
| B6 | Duplicate and unknown outcome | Handles resend and two accepted adjustment requests without assuming one physical result | yes | | |
| B7 | Missing and corrected data | Defines stop, quarantine, or review behavior for absent, late, and corrected readings | yes | | |
| B8 | External visibility | Prevents or reverses unsupported **Protection active** display | yes | | |
| B9 | Verification | Includes negative or challenge cases and separates local parsing from business evidence | no | | |
| B10 | Release and reversal | Names blocking unknowns, a safe state, and a condition that reverses the design | yes | | |

**Tool B subtotal:** / applicable maximum 20

## Challenge-response dimensions

| ID | Dimension | Two-point evidence | Critical? | Score | Rationale and artifact reference |
| --- | --- | --- | --- | ---: | --- |
| C1 | Different identifiers, same situation | Recognizes that distinct message identifiers do not settle whether the underlying work should repeat | yes | | |
| C2 | Missing reading replaced with zero | Rejects or explicitly governs the substitution and its downstream consequences | yes | | |
| C3 | Accepted requests versus physical change | Refuses to treat two accepted requests as proof that the case changed | yes | | |
| C4 | Lender display | Removes, qualifies, or blocks the unsupported display until approved evidence exists | yes | | |
| C5 | Artifact revision | Revises relevant tool fields and final decision rather than only describing concern in the workbook | no | | |

**Challenge subtotal:** / applicable maximum 10

## Critical false-green conditions

Mark a critical false green when the final artifacts allow implementation or
release while any of these remains unbounded:

- the high reading itself is labeled as protected or acceptable condition;
- the gateway or platform account is treated as sufficient sign-off;
- controller request acceptance is treated as physical completion;
- a missing reading becomes `0.0` without an explicit approved rule and
  downstream review;
- repeated messages or requests may repeat an effect without a named identity,
  evidence, or reconciliation path;
- the lender sees a positive status unsupported by the permitted decision and
  evidence; or
- the participant marks a required owner or evidence unknown but the brief
  still authorizes unrestricted generation or release.

A critical false green is evidence that the tool, scenario, instructions, or
protocol failed to prevent a dangerous confident outcome. It is not grounds to
label the participant incompetent.

## Calculation

`score percentage = awarded points / applicable maximum points * 100`

Report Tool A, Tool B, and challenge percentages separately. Do not hide a
critical zero inside an aggregate score.

## Per-session disposition

| Disposition | Criteria | Meaning |
| --- | --- | --- |
| Protocol invalid | Consent/privacy failure, scoring leakage, substantive coaching, wrong versions, or unusable artifacts affected the response | Preserve the deviation; do not score as clean evidence |
| Major revision candidate | Any critical false green, or score below 60% | Investigate wording, ordering, missing fields, scenario ambiguity, and facilitation before another version |
| Targeted revision candidate | 60–79%, repeated field friction, material contradiction, or challenge insight has no clear destination | Revise named fields or guidance and retest |
| Continue testing unchanged | At least 80%, no critical false green, no substantive prompt, and no material concern lacks a destination | One usability data point only; not validation |

The percentage bands are proposed decision aids, not empirically calibrated
cutoffs. Preserve the underlying field evidence and scorer rationale.

## Cross-session tool decision

Do not make a validation claim from one session. After a predeclared mix of
roles and at least one unrelated scenario per revised version, compare:

- critical false-green frequency;
- fields skipped, questioned, or answered with implementation detail;
- time and unfinished sections;
- contradictions between the two tools;
- challenge-driven revisions;
- facilitator prompts and invalid sessions; and
- concerns participants could not place.

Possible decisions are: retain version and continue testing, targeted revision,
major revision, split or combine fields, change facilitator guidance, or retire
the tool. “Validated” is not an output of this rubric without a separate,
approved evidence standard.

**Current score:** none; no session has occurred.
