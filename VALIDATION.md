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
consistency, correction identity, and stale governed fields. The mutation suite
runs in disposable copies and proves that the declared forbidden states are
rejected. These are repository-integrity checks only. They do not establish
practitioner usability, technical correctness, security, accessibility, legal
sufficiency, production fitness, or book-edition compatibility.
