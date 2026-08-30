# Validation

Run:

```bash
python3 scripts/validate_repository.py
python3 scripts/test_temporal_protocol.py
```

The validator checks the manifest, required reader entry points, local Markdown
links, gateway first-pass language, comprehensive-example paths, and declared
pilot-packet SHA-256 values. It also validates the structured temporal protocol,
all six release chains, critical instruction fingerprints, packet-version
consistency, correction identity, stale governed fields, and the exact
route-declared live-update input and revision-phase binding. Version 1.2.5 also
enforces exclusive human/synthetic entry, stage boundaries without future end
fields in governed workbooks, scoring-before-debrief, Section 6, immutable
pre-close results, external closeout, one-page proof, and the distinction
between six scored freezes and full-route closure. The mutation suite
runs in disposable copies and proves that the declared forbidden states,
including live-update member omission, rename, route omission, unbinding, and
wording drift with refreshed surrounding hashes, are rejected. These are
repository-integrity checks only. They do not establish
practitioner usability, technical correctness, security, accessibility, legal
sufficiency, production fitness, or book-edition compatibility.
