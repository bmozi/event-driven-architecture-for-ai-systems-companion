The same high-temperature reading was delivered three times. Two workers each
produced `ShipmentAtRisk`, and every event triggered a carrier request, stock
reservation, provisional credit, service case, and notification job. One
carrier request was accepted but not decided. Its proposed `ShipmentRerouted`
event caused the store to be told a replacement was coming. A late route
update triggered the risk service again. Pine Hollow now has six risk events,
six carrier requests, six reservations, and no verified reroute, replacement,
or stop owner.
