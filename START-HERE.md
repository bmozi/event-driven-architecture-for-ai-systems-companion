# Start Here: One Message in Thirty Minutes

**Reader route:** Complete the thirty-minute exercise output first. The
facilitator-only freeze, manifest, and evidence protocol is a separate route
for controlled pilots; do not open it until the first-pass artifact is done.

**Plain language:** Causal identity connects a message, retry, or action to the
thing that caused it. Semantic difference means a change in meaning, not just
a renamed field or changed format.

Choose one message another team, system, partner, automation, or agent treats as
important. Do not begin with the broker or schema.

If you do not have a message to bring, use the [supplied library-hold case and
worked answer](supplied-practice-route.md). Try it before adapting the forms.
For optional executable practice, the [portable event-pattern lab](labs/portable-event-pattern-lab/README.md)
runs five small in-memory fixtures with the Python standard library.

## 0–5 minutes: say why it matters

Complete three sentences:

1. Another party needs to know that ___;
2. so it can legitimately ___;
3. but a wrong or repeated reaction could ___.

If the first sentence describes a request rather than something that happened,
you may be holding a command rather than an event.

## 5–15 minutes: define the fact

Complete the [six-line first pass](event-meaning-and-authority-record.md#ten-minute-first-pass)
in the Event Meaning-and-Authority Record. Compare it with the
[miniature Northbridge example](event-meaning-and-authority-record.md#miniature-example).

Stop if two reasonable readers name different facts or different declaring
authorities.

## 15–25 minutes: expose multiplication

Use the [Traffic, Cost, and Action Multiplier Calculator](traffic-cost-action-multiplier-calculator.md)
to sketch one normal path and one credible failure path. Count deliveries,
retries, downstream calls, stored copies, and automated actions. Approximation
is acceptable; invisible assumptions are not.

## 25–30 minutes: ask for a read-back

Give the six lines to someone outside the producing team. Ask them to restate
the fact, name one permitted reaction, and name one conclusion the message does
not support.

## Your first result

You now have a reviewable event hypothesis and an initial multiplier sketch,
not an approved contract or topology. Continue with the
[comprehensive Northbridge example](examples/northbridge-events-integrated-example.md)
and the failure, loop, replay, and reconciliation tools required by the flow.
