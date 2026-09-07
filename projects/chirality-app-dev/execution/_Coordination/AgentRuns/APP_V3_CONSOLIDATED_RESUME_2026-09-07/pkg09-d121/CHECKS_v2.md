# Deterministic checks — corrected preparation v2

Configured Python: `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python` with PyYAML `6.0.3`.

| Check | Result |
|---|---|
| Direct SHA-256 of `ACCEPTED.patch` | PASS — `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32` |
| Direct SHA-256 of three live preimages | PASS — exact frozen identities in `PREFLIGHT_AND_IDENTITIES_v2.json` |
| Direct SHA-256 of three retained postimages | PASS — `af33c262…1960`, `0f4b65b5…e6ba`, `02725ce6…7d0` |
| `git apply -p0 --check ACCEPTED.patch` | PASS |
| Isolated `git apply -p0 ACCEPTED.patch` from exact current preimages | PASS |
| Byte comparison of each isolated result to retained postimage | PASS, 3/3 |
| SOW validator over exact isolated patch result | PASS — `SOW_V1`, no issues |
| Review-checklist derivation | PASS — one `DEL-09-06-AC-001` item with `DEL-09-06-VER-001` |
| App receipt validator | PASS — exit 0; reported frozen through Receipt-52 |
| App authority-corpus status | PASS — v20, all eight members MATCH, no drift |
| APP-HOLD reliance, DEL-09-06 | ALLOW — register `c08a2948…cafc`, scan `b30a5461…f437` |
| APP-HOLD accepted-dependency-consumption, DEL-09-06 | ALLOW — same register/scan |
| Practitioner harness `status --project chirality-app-dev` | PASS — exit 0, no finding severities |
| Practitioner harness `self-check` | PASS — exit 0 with pre-existing reported baseline findings (`REVIEW=4`, `WARN=55`, `INFO=14`, `NOT_APPLICABLE=1`); no repair inferred or attempted |
| `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python -m pytest -q tools/practitioner_harness` | PASS — `379 passed in 29.45s` |

Frontend checks were not run because this correction changes preparation evidence only. No carrier, product source, test, build configuration, or runtime process changed.
