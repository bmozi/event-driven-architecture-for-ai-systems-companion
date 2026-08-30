# Facilitator Guide

**Packet:** EVT-RV-PILOT-001 version 1.2.0
**Status:** Facilitator-only; prepared and unrun

**Revision note:** Version 1.2.0 strengthens exact-file transfer, freeze
provenance, and staged decision evidence after synthetic protocol audit; it has
no human or practitioner validation.

## Purpose

Test the materials, not the participants. Observe whether the reader-value
layer supports a practitioner event decision and an independent decision-owner
read-back.

## Recommended timing

### Stage A — 70 to 85 minutes

- consent and setup: 5 minutes;
- scenario and recognition questions: 10 minutes;
- meaning-and-authority record: 25 minutes;
- multiplier and loop review: 20 minutes;
- live update and revision: 10 minutes; and
- handoff and feedback: 10 minutes.

### Stage B — 35 to 50 minutes

- independent read-back: 15 minutes;
- executive brief and value ledger review: 10 minutes;
- bounded decision: 10 minutes; and
- debrief: 5 to 15 minutes.

Time is evidence, not a speed target.

## Required capture

For each participant, record setup start before the consent notice is first
opened. Obtain consent, then record the exact stage start immediately before
the route is opened. Record the exact file-open order, each pause or question,
and every intervention with time and level. Do not reconstruct these from
memory after the session.

## Sealed flat delivery and manifest rule

Before each stage, copy only the approved exact files into a new sealed flat
input. Preserve every literal local filename named by the packet route. Create
and verify a run-specific delivery manifest before scored work and log each
later staged release. A manifest hashes other files; it never lists or hashes
itself. Do not rely on repository-relative paths.

The planned live update creates the first revised set. It is not a correction
of already frozen revised bytes. A later correction must preserve the old
artifact and create exact new immutable filename, ID/version, hash, reason,
correction timestamp/timezone, replacement freeze record, and replacement
manifest. Never overwrite or reuse the old filename.

## No-coaching rule

During scored work, the facilitator may repeat written text or resolve file
access. Do not name the preferred facts, assign declarer authority, calculate
the multiplier, identify the loop, supply a budget, or confirm an answer.
Record every intervention.

## Stage A sequence

1. Confirm consent and freeze identity. Record Stage A start before opening the
   participant route.
2. Follow the route exactly. Supply the scenario and workbook only, then let the
   participant complete Section 1 before opening companion assets.
3. Supply only the four listed assets in the packet README, in order. The
   Northbridge miniature embedded in the supplied record and generic examples
   already visible in supplied files are allowed; do not allow linked
   comprehensive or completed examples.
4. Freeze the initial workbook and detailed artifacts before the update. Record
   immutable filenames, IDs/versions, timestamps/timezones, hashes, and
   manifest.
5. Read the live update:

> The same high-temperature reading was delivered three times. Two workers
> each produced `ShipmentAtRisk`, and every event triggered a carrier request,
> stock reservation, provisional credit, service case, and notification job.
> One carrier request was accepted but not decided. Its proposed
> `ShipmentRerouted` event caused the store to be told a replacement was
> coming. A late route update triggered the risk service again. Pine Hollow
> now has six risk events, six carrier requests, six reservations, and no
> verified reroute, replacement, or stop owner.

6. Ask only: “What can each party safely say or do now, and what changes in
   your artifacts?”
7. Let the participant revise the workbook, meaning/authority record,
   multiplier, and loop check. Require exactly
   `EVT-A-REVISED-WORKBOOK-v1.md`,
   `EVT-A-REVISED-MEANING-AUTHORITY-v1.md`,
   `EVT-A-REVISED-MULTIPLIER-v1.md`, and
   `EVT-A-REVISED-LOOP-CHECK-v1.md`, each with artifact ID, version,
   completion timestamp/timezone, and pre-hash state `REVISED COMPLETE`.
8. Remove every `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank,
   or equivalent incomplete state, and reject a premature artifact
   self-declaration of `FROZEN`. Create
   `EVT-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`; it hashes the four details and
   does not hash itself.
9. Complete `EVT-A-REVISED-FREEZE-RECORD-v1.md` with exact freeze
   timestamp/timezone, literal filenames, IDs/versions, completion
   timestamps/timezones, pre-hash states, hashes, and governing manifest
   filename/hash. The verified manifest and detached record establish
   `FROZEN`; verify them before opening the handoff.
10. Only then supply `05-one-screen-handoff.md`. Ensure its inventory matches
    the detached record and manifest, complete it as
    `EVT-A-ONE-SCREEN-HANDOFF-v1.md`, and freeze it separately.
11. Preserve initial, revised, record, manifest, and handoff bytes without
    alteration.

## Stage B sequence

1. Use a participant who did not create the Stage A artifact, obtain separate
   consent, verify the sealed Stage B manifest, and record exact Stage B start
   and timezone before opening the route.
2. Supply the route, `EVT-A-ONE-SCREEN-HANDOFF-v1.md` as first substantive
   content, and the decision-owner workbook. Freeze
   `EVT-B-SECTION-1-SCAN-v1.md` before any scenario or detail opens.
3. Supply `02-scenario-and-task.md`, the detached freeze record, its governing
   revised manifest, and all four exact handoff-linked revised details. Verify
   literal filenames, IDs/versions, completion timestamps/timezones, pre-hash
   `REVISED COMPLETE` states, hashes, and detached-record `FROZEN` conditions. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest stops detailed read-back.
4. Freeze `EVT-B-SECTION-2-DETAIL-v1.md` before supplying
   `EXECUTIVE-DECISION-BRIEF.md`, then `VALUE-AND-EVIDENCE-LEDGER.md`.
5. Freeze `EVT-B-SECTIONS-3-5-DECISION-v1.md`. Keep Section 6 closed until all
   three freezes verify and scoring ends.
6. Keep the Stage A participant unavailable until then. End scoring before
   allowing explanation or repair. Record exact Stage B end and timezone.

## Intervention levels

- **L0:** silence or think-aloud reminder;
- **L1:** repeat written text;
- **L2:** neutral probe such as “What fact can the store rely on?”;
- **L3:** define a term without applying it; and
- **L4:** recommend or supply the decision.

L3 is aided. L4 contaminates the affected gate. Preserve the result.

## Stop conditions

Stop and retain partial evidence on consent withdrawal, confidential-data
disclosure, material unblinding, changed frozen bytes, distress, material tool
failure, or coaching that makes the central result uninterpretable.
