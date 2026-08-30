# External Closeout Record Template

**Packet:** EVT-RV-PILOT-001 version 1.2.5
**Status:** Facilitator-only blank template; no closeout result exists

Complete this record only after immutable run results are complete, the
execution/access log is closed and validated, and a byte-identical copy is
bound by an external checksum manifest. Export
`EVT-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md`.

## Run-results and closed-log binding

- Packet ID/version: `EVT-RV-PILOT-001` / `1.2.5`
- Attempt ID:
- Run-results filename: `EVT-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md`
- Run-results SHA-256 and completion event ID/timestamp/timezone:
- Active closed-log filename: `EVT-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`
- Active closed-log SHA-256:
- Closed-log validation command and complete observed output:
- Integer exit status and validation timestamp/timezone:
- Closeout-copy filename: `EVT-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl`
- Copy byte-identical to active closed log: yes / no
- Closeout-copy SHA-256:
- External manifest filename:
  `EVT-RUN-EXECUTION-ACCESS-LOG-SHA256SUMS-<attempt-id>.txt`
- External manifest SHA-256:
- External verification command/output/exit/timestamp/timezone:

## Closeout completion

- Final event in closed log: `RUN_LOG_CLOSED` / invalid
- Closed-log hash absent from earlier results bytes: yes / no
- Future closeout timestamp absent from earlier results bytes: yes / no
- Record completion timestamp/timezone:
- Record state: `EXTERNAL CLOSEOUT COMPLETE` / invalid

This record binds actual later bytes. It does not embed its own hash or pretend
that the earlier results or closed log predicted this external evidence.
