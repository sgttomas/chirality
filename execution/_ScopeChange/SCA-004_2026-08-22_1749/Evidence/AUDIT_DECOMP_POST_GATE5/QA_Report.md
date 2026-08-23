# AUDIT_DECOMP post-Gate-5 QA report

## Input identities

| Input | Observed SHA-256 | Result |
|---|---|---|
| Working surface | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` | PASS |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | PASS |
| Scope ledger | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` | PASS |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | PASS |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | PASS |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | PASS |
| Coverage telemetry | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` | PASS |
| Gate-1 baseline | `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45` | PASS — preserved |
| `_LATEST.md` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` | PASS — unchanged |

## Deterministic checks

- CSV parse and exact row counts: PASS.
- Deliverable IDs and parent distribution: PASS.
- Every new deliverable is parented and mapped: PASS.
- Every objective has supporting deliverables and scope items: PASS.
- IN scope items missing package/deliverable mapping: 0.
- Reverse units not `TRACED`: 0.
- Telemetry counts reconcile with the registers: PASS.
- Applied validator: PASS 65/65, zero failures.

QA verdict: `PASS`.
