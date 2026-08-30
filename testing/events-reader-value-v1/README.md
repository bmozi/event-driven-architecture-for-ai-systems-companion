# Events Reader-Value Pilot Packet

**Packet ID:** EVT-RV-PILOT-001
**Version:** 1.2.2
**Status:** `PREPARED/UNRUN` for human participants; no participant recruited or
consented
**Scenario:** Pine Hollow Foods, entirely fictional

Version 1.2.2 preserves the non-self-referential freeze sequence introduced in
version 1.2.1 and adds a machine-readable protocol plus executable negative
mutation tests. That internal work was not a human or practitioner session and
provides no usability, safety, architecture, or business-value validation.

The normative release inventory and invariants are in
[`temporal-protocol.json`](temporal-protocol.json). The human instructions must
agree with that file; the repository validator checks both their exact frozen
bytes and their structured release rows.

## What this packet tests

This packet tests whether the Events companion helps a reader move through the
complete value chain:

`RECOGNIZE THE NEED -> EXPLAIN THE FACT -> RECORD AUTHORITY -> TRACE REACTIONS`
`-> FIND MULTIPLICATION OR A LOOP -> HAND OFF A DECISION -> NAME NEXT EVIDENCE`

It does not replace the older Harborlight technical-transfer packet. That
packet keeps its frozen two-tool scope. This packet separately tests the newer
reader routes, multiplier and loop tools, value ledger, and executive decision
language.

## Sealed flat run inputs

Before either stage, copy the exact approved immutable files into a new sealed,
flat stage-input directory. Preserve every literal filename below. Do not
deliver repository-relative paths, aliases, regenerated copies, or summaries.
Create and verify a run-specific SHA-256 delivery manifest before the scored
stage starts. A manifest hashes other files; it never lists or hashes itself.

For every later freeze, use this exact temporal order:

1. finish the governed artifact bytes, including ID/version, completion
   timestamp/timezone, and complete pre-hash state;
2. create a governing manifest that hashes only those completed artifacts;
3. verify that manifest and observe the exact verification timestamp/timezone;
4. only then create a detached freeze-verification record describing the
   observed event, artifact and manifest identities, and hashes; and
5. have the next phase's sealed input manifest hash the completed artifacts,
   their governing manifest, and that later detached record.

The governing manifest never hashes itself or the later record that describes
its verification. The record never claims its own hash.

The planned live-update revision creates the first revised artifact set. It is
not a correction of already frozen revised bytes. If a revised byte changes
after its freeze, retain the old artifact and create a new immutable filename,
ID/version, hash, governing manifest, and detached verification record. Record the exact
reason and correction timestamp with timezone. Never overwrite, rename, or
relabel the prior evidence.

## Two stages

### Stage A — practitioner

Record setup start before the consent notice is first opened. Complete consent
before scored work. Then record the Stage A start and timezone before the route
is opened and follow its exact order. Supply only these exact local filenames:

1. [Consent and privacy notice](participant/01-consent-and-privacy.md), during
   setup rather than as scored architecture work
2. `00-packet-route.md`
3. `02-scenario-and-task.md`
4. `03-practitioner-workbook.md`
5. `START-HERE.md`
6. `event-meaning-and-authority-record.md`
7. `traffic-cost-action-multiplier-calculator.md`
8. `event-loop-prevention-checklist.md`
9. after the live-update revision, `06-revised-artifact-freeze-record.md`; and
10. only after that record verifies, the blank `05-one-screen-handoff.md`.

The Northbridge miniature embedded in the supplied meaning-and-authority record
and short generic examples already visible in supplied files are allowed. Do
not follow links to the comprehensive Northbridge example or any other
completed example. All full worked examples are withheld. Do not supply the
repository Failure Lab, facilitator materials, executive brief, or value
ledger during Stage A. Before the live update, freeze the initial workbook,
meaning/authority record, multiplier, and loop check as
`EVT-A-INITIAL-WORKBOOK-v1.md`,
`EVT-A-INITIAL-MEANING-AUTHORITY-v1.md`,
`EVT-A-INITIAL-MULTIPLIER-v1.md`, and
`EVT-A-INITIAL-LOOP-CHECK-v1.md`. Each must be marked `INITIAL COMPLETE` with
an ID/version and completion timestamp/timezone. Govern them with
`EVT-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`, verify it, and only then create
`EVT-A-INITIAL-FREEZE-VERIFICATION-v1.md`. The sealed revision-phase manifest
must hash the four artifacts, governing manifest, and detached record before
the live update is delivered.

The required revised detail filenames are:

- `EVT-A-REVISED-WORKBOOK-v1.md`;
- `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`;
- `EVT-A-REVISED-MULTIPLIER-v1.md`; and
- `EVT-A-REVISED-LOOP-CHECK-v1.md`.

Each revised file must contain its artifact ID, version, completion
timestamp/timezone, and pre-hash state `REVISED COMPLETE`; `DRAFT`, `PENDING`,
`PENDING FREEZE`, `AWAITING FREEZE`, a blank state, or an equivalent marker is
not complete. The governing manifest is
`EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`. It hashes the four revised detail
files and does not hash itself. After verifying that manifest, complete
`EVT-A-REVISED-FREEZE-VERIFICATION-v1.md` from the supplied
[detached record template](participant/06-revised-artifact-freeze-record.md).
That record must verify exact filenames, IDs, versions, completion
timestamps/timezones, pre-hash states, hashes, and manifest filename/hash and
record the observed manifest-verification timestamp/timezone. It is created
after the manifest and is not governed by the manifest it describes. Before
the blank handoff opens, a sealed handoff-phase input manifest must hash the
revised artifacts, governing manifest, and detached record.

Complete the handoff as `EVT-A-ONE-SCREEN-HANDOFF-v1.md` with an ID/version,
completion timestamp/timezone, and `HANDOFF COMPLETE` state. Hash only that
completed handoff in `EVT-A-HANDOFF-SHA256SUMS-v1.txt`, verify the manifest,
and then create `EVT-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. The Stage B phase-1
input manifest must hash the handoff, its governing manifest, and its detached
verification record.

### Stage B — independent decision owner

Record setup start before the consent notice is first opened. Complete consent,
then record the Stage B start and timezone before the route is opened. Build a
separate sealed flat Stage B input and supply in the route's exact order:

1. [Consent and privacy notice](participant/01-consent-and-privacy.md), during
   setup;
2. `00-packet-route.md`;
3. `EVT-A-ONE-SCREEN-HANDOFF-v1.md` as the first substantive decision content,
   plus its governing manifest and detached verification record as sealed
   provenance;
4. `04-decision-owner-workbook.md`;
5. after the Section 1 freeze, `02-scenario-and-task.md`,
   `EVT-A-REVISED-FREEZE-VERIFICATION-v1.md`,
   `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, and all four literal revised
   detail files named above;
6. after the Section 2 freeze, `EXECUTIVE-DECISION-BRIEF.md`; and
7. `VALUE-AND-EVIDENCE-LEDGER.md`.

The handoff's literal detail inventory, detached record, governing manifest,
and delivered Stage B files must match exactly. A rename, regenerated copy,
summary, substitution, omission, hash mismatch, pre-hash state other than
`REVISED COMPLETE`, or missing detached `FROZEN` verification stops detailed
read-back and is recorded as a deviation.

Use a different person for Stage B during the first calibration round. For each
of the three exports, complete its ID/version, completion timestamp/timezone,
and `SECTION COMPLETE` state before hashing it. Create a governing manifest
that hashes only that export, verify it, and then create a detached verification
record. The next phase's sealed input manifest hashes the export, its manifest,
and its detached record. Apply this sequence to Section 1 from the handoff
alone, Section 2 after exact detail verification, and Sections 3-5 after the
executive files. Keep Section 6 closed until the Sections 3-5 record verifies
and the debrief-phase input manifest seals the last export, manifest, and
record. Do not let the Stage A participant explain or repair an artifact before
then.

## Facilitator only

- [Facilitator guide](facilitator-only/01-facilitator-guide.md)
- [Observation and scoring rubric](facilitator-only/02-observation-and-scoring-rubric.md)
- [Results and deviation log](facilitator-only/03-results-and-deviation-log.md)
- [Temporal freeze protocol and record templates](facilitator-only/04-temporal-freeze-protocol-and-record-templates.md)

Never supply these files before either scored stage ends.

## Execution prerequisites

Before recruitment:

1. assign an accountable execution owner;
2. approve storage, access, retention, redaction, and deletion;
3. decide whether further ethics, legal, privacy, or organizational review is
   required;
4. create sealed flat stage inputs and freeze the exact files and referenced
   asset bytes;
5. record SHA-256 values and observed verification timestamps/timezones in
   detached run-specific evidence;
6. keep scheduling identity separate from participant codes; and
7. assign a facilitator and evaluator with disclosed relationships.

The checked-in `SHA256SUMS` records the prepared source packet. See the
[static protocol validation note](facilitator-only/04-temporal-freeze-protocol-and-record-templates.md)
for the exact freeze inventory and record schema. A run-specific
delivery manifest must also hash every supplied referenced asset under its
exact local filename while excluding itself. Any byte change requires a new
manifest and, when meaning changes, a new packet version.

## Evidence boundary

A completed pair can reveal wording defects, unsafe interpretations, transfer
failures, and useful behavior for the exact participants and materials. It
cannot prove event correctness, loop safety, business value, broad usability,
or publication readiness.
