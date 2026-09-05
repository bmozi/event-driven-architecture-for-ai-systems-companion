# Practice with supplied facts: a library hold

This fictional public-library case lets you try the method without bringing
an employer's design or installing a broker. All policies, times, identifiers,
and quantities are stipulated teaching inputs. No practitioner or production
result is claimed. Try the task before reading the answer.

## Supplied facts

A library accepts patron P's request for book copy C as request R at 09:00.
Acceptance means the request was recorded, not that a copy is ready. At 09:05
the circulation authority sets hold H, revision 4, to READY until 17:00. A
notifier may send one ready notice per hold revision using effect identity
`notice/H/4`. It may read the current contact address only through the library's
purpose-bound contact capability. The event itself contains no address.

The circulation service commits its hold state and outbox item together. The
relay can redeliver. The notifier's endpoint is stipulated to enforce the same
effect identity atomically for 48 hours and to expose outcome lookup by that
identity. An acknowledgement is lost after a possible send.

The next day, an operator has current permission to rebuild an isolated hold
view from retained records. That permission grants no notices. Current hold
state is revision 5, EXPIRED. There is no permission to renew the hold.

## Your task

1. Name the fact at 09:00 and the fact at 09:05. State what each fails to prove.
2. Write a six-line meaning-and-authority record for the READY declaration.
3. Decide how to handle the lost acknowledgement without inventing another notice.
4. Choose a replay mode for the view and notifier. State what the rebuilt view
   must do with revision 4 after revision 5.
5. Name the evidence needed before saying the patron received the notice.

## Worked answer

The first fact is `HoldRequestAccepted`: request R entered the intake boundary.
It does not establish availability. The second is `HoldReady`: circulation
committed hold H at revision 4, ready until 17:00. It does not prove collection,
notice delivery, or an indefinite right to the copy.

The six-line record is:

| Field | Completed decision |
| --- | --- |
| Fact | Hold H became READY, revision 4, until 17:00 |
| Declarer and evidence | Circulation authority; committed hold revision and policy decision |
| Subject and context | Hold H for patron P and copy C; library boundary |
| Permitted inference | The copy is held within that revision and expiry, subject to later correction |
| Prohibited inference | The patron collected it or received a notice |
| Reaction boundary | One currently permitted ready notice under `notice/H/4`; no renewal |

After the timeout, query `notice/H/4`. A same-identity retry may be allowed
within the stipulated endpoint contract; a fresh identity could create a second
notice. Keep the outcome unknown until evidence resolves it. A send receipt
does not establish that the patron read the message.

For the rebuild, permit isolated view writes and deny the notifier at both its
route and effect boundary. Preserve revisions and apply the contract's latest
authorized revision rule: final state is EXPIRED at revision 5. Neither replay
delivery time nor an old READY event renews the hold. Reconcile eligible input
identities, exclusions, final subject state, and any denied effect attempts.

## Change the assumption

Replay is requested 72 hours later, after the notice endpoint's identity record
has expired. The operator still has only view-rebuild permission. Is the old
key enough to send another notice?

No. Expired deduplication evidence cannot supply either current permission or
the old outcome. Keep notices disabled. If a new notice is needed, a responsible
owner must establish present purpose, contact entitlement, hold state, and the
appropriate reconciliation or new-intent decision. The old event remains
history; it is not approval to act now.

## Transfer your result

Use the [Meaning-and-Authority Record](event-meaning-and-authority-record.md),
[Replay and Effect Ledger](replay-backfill-authorization-and-effect-ledger.md),
[Invariant Matrix](ordering-duplication-and-idempotency-invariant-matrix.md),
and [Reconciliation Map](asynchronous-evidence-and-business-reconciliation-map.md).
Replace the library facts only after you can explain the worked decision.

Self-check: Did you separate accepted from ready, notice attempt from outcome,
historical identity from current authority, and replay input from current state?
A correct self-check is practice evidence for you, not an independently observed
practitioner session or approval of a real system.
