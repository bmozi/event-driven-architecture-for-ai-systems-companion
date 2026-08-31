# Events synthetic Stage A revised workbook

Artifact ID/version: EVT-A-REVISED-WORKBOOK/v1
Completion timestamp/timezone: 2026-08-30T14:15:00-0600 MDT
Pre-hash state: REVISED COMPLETE
Participant branch: SYNTHETIC - NO HUMAN PARTICIPANT OR HUMAN DATA

## Recognition and explanation

Pine Hollow needs to protect a shipment and give the store an honest status. A sensor notification is not authority to declare unsafe or replacement-eligible. An assessment, route request, and completed reroute are distinct claims; only an accountable declarer with supporting evidence may make each claim.

## Distinct facts and reactions

- `TemperatureReadingObserved`: sensor/vendor may declare the reading, not spoilage.
- `ShipmentRiskAssessed`: risk-service owner is `UNKNOWN`; it may be an assessment, not a final business decision.
- `CarrierRerouteRequested`: routing agent may request only under declared authority.
- `ShipmentRerouted`: carrier/route authority may declare only after the route actually changes.
- Replacement, credit, case, and notification are reactions/effects, not implied by the first alert.

## Multiplier and loop

Initial scenario estimate: one reading can fan out to warehouse reservation, provisional credit, case, notification, and carrier request: five downstream action attempts per risk assessment, before retries or duplicates. Three sensors and gateway redelivery make the simple count unreliable. The shared causal identity must cover physical shipment/condition, observation set, assessment, requests, and effects. Budget: one risk assessment and one carrier request per shipment-condition window until an owner explicitly reopens it. Breaker: stop new reactions when the budget or ancestor-condition threshold is reached. Stop owner: `UNASSIGNED`; Pine Hollow must assign operations authority.

## Live update and incident sequence

The exact update reports six risk events, six carrier requests, six reservations, and no verified reroute, replacement, or stop owner. Immediate containment is `PROPOSED`: stop automated reactions for the shipment. Evidence preservation is `PROPOSED`: retain sensor, assessment, request, delivery, and effect ledgers. Effect reconciliation is `PROPOSED`: reconcile by shipment-condition identity, not message ID. Store correction is `PROPOSED` and may say only “investigation/pending” until route and replacement evidence exists. Redesign/restart is `PROPOSED` only after 1-4. Authority/evidence for all are `UNKNOWN` until assigned.

## Material feedback

The strongest prompt was “what may each consumer safely infer?” The multiplier worksheet makes units visible, but the scenario requires a plain reminder that alert, assessment, request, and outcome are different. Synthetic completion cannot establish human comprehension, cost reduction, or operational safety.
