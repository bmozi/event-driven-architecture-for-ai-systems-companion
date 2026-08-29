# Harborlight Museum Climate-Messaging Exercise

<!-- markdownlint-disable MD013 -->

**Scenario status:** Entirely fictional

Use only the information below. You may identify information you would need,
but do not fill gaps with a real employer or customer example.

## Setting

Harborlight Museum is preparing to display a watercolor borrowed from another
museum. The watercolor will sit in climate-controlled case G-12. Opening day is
three weeks away.

The case has humidity sensors, a local gateway, a facilities controller, a
conservation dashboard, and a lender portal. The museum director wants timely
updates and has asked the software team to “make the case protection flow real
time before opening day.”

## How the teams currently work

- Conservation staff sign off on whether display conditions are acceptable for
  an artwork.
- Facilities staff maintain the climate equipment. Their controller can accept
  an adjustment request before the physical case reaches the requested state.
- Loan-services staff decide which updates are sent to the lending museum.
- The platform team operates the shared messaging service and application
  accounts.
- The lender portal may show only approved information about the borrowed item.

The team has not named an owner for the draft message described below.

## Generated proposal

An AI coding assistant produced a proposal centered on one message named
`ArtifactProtected`:

```json
{
  "messageType": "ArtifactProtected",
  "artifactId": "HL-LOAN-447",
  "caseId": "G-12",
  "humidityPercent": 67.8,
  "limitPercent": 60.0,
  "status": "protected",
  "source": "case-gateway-2",
  "timestamp": "2026-09-18T09:14:00Z"
}
```

The generated proposal says the gateway will send this message when a reading
is above the configured limit. It has four recipients:

1. The conservation dashboard changes the case badge to **Protected**.
2. A facilities adapter sends `SetDehumidifier` to the case controller.
3. The lender portal displays **Protection active**.
4. An archive stores the message for later review.

After the facilities adapter receives a response from the controller, the
gateway sends `ArtifactProtected` again “to keep every screen current.”

The generated tests verify that the JSON fields exist, the reading is numeric,
and all four recipients can parse the message.

## Additional operating notes

- A sensor reading may arrive late or may later be corrected.
- During a sensor restart, the reading field can be missing.
- The messaging client may send again after a timeout because it cannot tell
  whether the first send was accepted.
- The facilities controller first reports that a request was accepted. A later
  device reading is currently the only indication that the case changed.
- Loan-services staff have not decided when the lender should see an alert,
  equipment activity, or an approved display-condition update.
- The AI assistant is ready to generate the message schema, applications,
  infrastructure configuration, tests, and dashboards as soon as the team says
  to proceed.

## Your assignment

Use the two supplied worksheets and the response workbook to review this
proposal. Work from the facts provided. Mark missing information instead of
inventing it. You are not being asked to write code or choose a vendor.

The facilitator will provide one additional scenario update after you complete
your initial review.
