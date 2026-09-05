"""Vendor-neutral, deterministic teaching fixture for event-pattern decisions.

This module intentionally models neither a broker nor a production event
runtime. It makes a few field-guide invariants executable: preserve uncertainty,
quarantine poison work with identity and reason, stop pressure before it becomes
invisible abandonment, and bound feedback generations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Disposition(str, Enum):
    ROUTED = "ROUTED"
    QUARANTINED = "QUARANTINED"
    STOPPED = "STOPPED"
    MANUAL_INTERVENTION_REQUIRED = "MANUAL_INTERVENTION_REQUIRED"


@dataclass(frozen=True)
class Event:
    event_id: str
    root_id: str
    subject: str
    kind: str
    body: dict[str, Any]
    generation: int = 0


@dataclass(frozen=True)
class Receipt:
    event_id: str
    root_id: str
    disposition: Disposition
    reason: str
    normalized_value: str | None = None


@dataclass
class PortableEventLab:
    per_subject_limit: int = 3
    quarantine_limit: int = 2
    max_generation: int = 2
    seen_by_subject: dict[str, int] = field(default_factory=dict)
    quarantine_count: int = 0

    def process(self, event: Event) -> Receipt:
        if event.generation > self.max_generation:
            return Receipt(
                event.event_id,
                event.root_id,
                Disposition.STOPPED,
                "feedback generation limit reached; escalation owner required",
            )

        if event.kind == "shipment.exception.detected":
            return self._process_shipment_exception(event)

        return self._quarantine(event, "unsupported event kind")

    def _process_shipment_exception(self, event: Event) -> Receipt:
        required = {"tenant", "availability"}
        missing = required - set(event.body)
        if missing:
            return self._quarantine(event, f"missing required fields: {sorted(missing)}")

        count = self.seen_by_subject.get(event.subject, 0) + 1
        self.seen_by_subject[event.subject] = count
        if count > self.per_subject_limit:
            return self._quarantine(
                event,
                "subject pressure limit reached; preserve ordering and escalate",
            )

        availability = event.body["availability"]
        if availability is None:
            normalized = "unknown"
        elif availability == 0:
            normalized = "zero"
        elif isinstance(availability, int) and availability > 0:
            normalized = "positive"
        else:
            return self._quarantine(event, "availability is not a permitted value")

        return Receipt(
            event.event_id,
            event.root_id,
            Disposition.ROUTED,
            "eligible for the approved route",
            normalized,
        )

    def _quarantine(self, event: Event, reason: str) -> Receipt:
        self.quarantine_count += 1
        if self.quarantine_count > self.quarantine_limit:
            return Receipt(
                event.event_id,
                event.root_id,
                Disposition.MANUAL_INTERVENTION_REQUIRED,
                "quarantine capacity limit reached; do not silently accept more poison work",
            )
        return Receipt(event.event_id, event.root_id, Disposition.QUARANTINED, reason)


def event(event_id: str, root_id: str, subject: str, **body: Any) -> Event:
    return Event(event_id, root_id, subject, "shipment.exception.detected", body)


def test_unknown_is_not_zero() -> None:
    lab = PortableEventLab()
    unknown = lab.process(event("evt-1", "root-1", "shipment-1", tenant="north", availability=None))
    zero = lab.process(event("evt-2", "root-2", "shipment-2", tenant="north", availability=0))
    assert unknown.disposition is Disposition.ROUTED
    assert unknown.normalized_value == "unknown"
    assert zero.normalized_value == "zero"


def test_hot_subject_is_quarantined() -> None:
    lab = PortableEventLab(per_subject_limit=2)
    lab.process(event("evt-1", "root-1", "shipment-1", tenant="north", availability=1))
    lab.process(event("evt-2", "root-2", "shipment-1", tenant="north", availability=1))
    receipt = lab.process(event("evt-3", "root-3", "shipment-1", tenant="north", availability=1))
    assert receipt.disposition is Disposition.QUARANTINED
    assert "pressure limit" in receipt.reason


def test_poison_event_retains_identity_and_reason() -> None:
    lab = PortableEventLab()
    receipt = lab.process(event("evt-poison", "root-poison", "shipment-9", tenant="north"))
    assert receipt.disposition is Disposition.QUARANTINED
    assert receipt.event_id == "evt-poison"
    assert receipt.root_id == "root-poison"
    assert "missing required fields" in receipt.reason


def test_dead_letter_capacity_fails_closed() -> None:
    lab = PortableEventLab(quarantine_limit=1)
    first = lab.process(event("evt-1", "root-1", "shipment-1", tenant="north"))
    second = lab.process(event("evt-2", "root-2", "shipment-2", tenant="north"))
    assert first.disposition is Disposition.QUARANTINED
    assert second.disposition is Disposition.MANUAL_INTERVENTION_REQUIRED


def test_feedback_generation_is_bounded() -> None:
    lab = PortableEventLab(max_generation=1)
    looping = Event("evt-loop", "root-loop", "shipment-3", "shipment.exception.detected", {"tenant": "north", "availability": 1}, generation=2)
    receipt = lab.process(looping)
    assert receipt.disposition is Disposition.STOPPED
    assert "generation limit" in receipt.reason


def main() -> None:
    tests = [
        test_unknown_is_not_zero,
        test_hot_subject_is_quarantined,
        test_poison_event_retains_identity_and_reason,
        test_dead_letter_capacity_fails_closed,
        test_feedback_generation_is_bounded,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print("PASS 5 constructed teaching fixtures; no production claim established")


if __name__ == "__main__":
    main()
