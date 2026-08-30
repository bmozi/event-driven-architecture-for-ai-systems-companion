# Pine Hollow Scenario: Protect One Refrigerated Shipment

**Packet:** EVT-RV-PILOT-001 version 1.2.2
**Status:** Fictional, prepared, and unrun

**Revision note:** Version 1.2.2 retains the version 1.2.1 temporal repair and
adds machine-enforced protocol checks after independent challenge; it has no
human or practitioner validation.

Pine Hollow Foods ships refrigerated products to grocery stores. The business
wants faster intervention when a shipment may be warming. The proposed design
sounds simple:

> Turn every temperature alert into `ShipmentAtRisk`. Let an AI routing agent
> react automatically, publish `ShipmentRerouted`, and let warehouse, billing,
> customer-service, and notification systems respond.

You are reviewing what the messages are allowed to mean before producers,
consumers, routes, or agent reactions are generated.

## Known facts

1. A sensor vendor sends a notification when one reading crosses a configured
   threshold. Pine Hollow has not authorized the vendor to declare that a
   shipment is unsafe, spoiled, delayed, or eligible for replacement.
2. One trailer can contain three sensors. A gateway can redeliver a reading,
   and different sensors may report the same physical condition.
3. The risk service combines readings with product, duration, and calibration
   data. It can produce an assessment, but its owner and decision authority
   have not been recorded.
4. The routing agent consumes `ShipmentAtRisk` and calls a carrier API. The API
   may return `accepted` before a dispatcher or route system decides.
5. The proposed `ShipmentRerouted` event is published as soon as the carrier
   accepts the request, not when a route actually changes.
6. Warehouse planning reserves replacement stock after `ShipmentAtRisk`.
   Billing creates a provisional credit, and customer service opens a case.
7. A notification service tells the store that a replacement is coming after
   receiving `ShipmentRerouted`.
8. The risk service also consumes route updates because route duration affects
   risk. Its proposed rule can emit another `ShipmentAtRisk` for the same
   shipment and condition.
9. Each new risk event can cause another carrier request, warehouse
   reservation, credit, case, and notification attempt.
10. The current design has a message ID but no shared causal identity covering
    duplicate readings, repeated assessments, retries, route requests, and
    downstream effects.
11. No one has set a per-shipment action budget, loop breaker, stop owner,
    replay rule, or evidence required before communicating an outcome.
12. No implementation, failure test, practitioner session, cost measurement,
    or business-result evidence exists.

## Stage A task

Without discussing the intended answer with a facilitator:

1. Explain in plain language what Pine Hollow and the receiving store need.
2. Complete the first pass and relevant portions of the supplied Event
   Meaning-and-Authority Record for the smallest useful set of distinct facts.
3. Estimate the initial downstream actions and explain where the simple
   multiplier stops being trustworthy.
4. Use the loop checklist to name one causal boundary, one budget, one breaker,
   and either an authorized stop owner or `UNASSIGNED` plus the authority or
   trigger needed to assign one.
5. State what each consumer may safely infer and what evidence would prove a
   shipment was actually rerouted or replaced.
6. Leave missing authority or evidence unknown. Do not invent it.
7. Complete the separate one-screen handoff only after the live update. Link it
   to the detailed artifacts rather than copying their contents.

## Live update

The facilitator will provide one update after the initial artifact is frozen.
Revise only after hearing it. Record the original and revised answer.

That planned revision creates the first revised artifact set. It is not a
later correction of already frozen revised bytes.

## Boundary

This exercise asks for a reviewable event decision. It does not ask you to
select a broker, write handlers, approve production, or estimate savings.
