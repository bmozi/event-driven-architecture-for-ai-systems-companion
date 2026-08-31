# Events synthetic revised loop check

Artifact ID/version: EVT-A-REVISED-LOOP-CHECK/v1
Completion timestamp/timezone: 2026-08-30T14:18:00-0600 MDT
Pre-hash state: REVISED COMPLETE

- Causal boundary: route updates may inform a new assessment only under a new condition revision; they do not silently recreate the ancestor assessment.
- Budget: one assessment, carrier request, reservation, credit, case, and notification attempt per shipment-condition case unless explicitly reopened.
- Breaker: reject or quarantine events whose causal ancestor is already active or whose case budget is exhausted.
- Stop owner: UNASSIGNED; operations authority must assign a stop owner before automated reactions.
- Safe restart: reconcile ledgers first, then restart from an authorized new assessment; never replay a notification as proof of reroute.
