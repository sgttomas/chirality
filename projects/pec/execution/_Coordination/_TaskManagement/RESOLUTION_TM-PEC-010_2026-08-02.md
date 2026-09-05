# TM-PEC-010 resolution record — D-PEC-78 O-A

**Date:** 2026-08-02
**Mode:** owner-ruled resolution assessment / row maintenance
**Invoking loop:** PEC
**Register home:** `_DomainEngines/pec/_TaskManagement/`
**Authority:** owner ruling `D-PEC-78: O-A`

This is Task Management decision-support and closeout evidence. It does not
amend the D-PEC record, accepted decomposition, source, lifecycle, consumer,
foreign-loop, release, or professional-reliance state.

## Federation preflight

The installed shell had no `taskmgmt` executable on `PATH`, so the repository
helper was invoked directly as
`python3 tools/taskmgmt/taskmgmt.py federation --register
_DomainEngines/pec/_TaskManagement/REGISTER.csv`.

- Coverage: `COMPLETE`; four canonical registers discovered, read, and
  validated.
- Register writes: zero.
- Before the requested mode, PEC reported `OPEN=6`, `DEFERRED=2`,
  `ELEVATED=0`, `CLOSED=0`; archived `2`.
- Program-level typed-field findings: `21 REMOTE_CLOSED_LOCAL_OPEN` and
  `22 LOCAL_CLOSED_REMOTE_OPEN`. No finding was inferred from Notes prose and
  none authorized a register act.

## K-TM-3 assessment

No additional owner disposition is required. The exact earlier Task
Management ruling retained TM-PEC-010 as deferred until the future ruling's
actual effect was known. The owner has now ruled `D-PEC-78: O-A`; the ruled
decision record states that this settles the PRD §16.3 / OI-003 product
decision and supports `TM-PEC-010` closure as `RESOLVED_BY_DECISION`.

That effect exactly resolves the row's concern: the existing PEC-owned
JSON/schema paths and typed core port are the long-term registry home and
shape. The separately required SCOPE_CHANGE propagation updates accepted
decomposition truth; it is not a remaining gate on this session-residue
disposition.

Closure evidence:

| Field | Value |
|---|---|
| EvidenceRef | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md` |
| EvidenceSha | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` |
| EvidenceQuote | `D-PEC-78: O-A` |
| Disposition | `RESOLVED_BY_DECISION` |
| Closed | `2026-08-02` |

The packet presented to the owner remains exactly SHA-256
`426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17`.

## Register delta and archive

- `TM-PEC-010`: `DEFERRED` to `CLOSED / RESOLVED_BY_DECISION`, then
  mechanically relocated from `REGISTER.csv` to `REGISTER_CLOSED.csv` by
  `taskmgmt archive`.
- Live register after archive: `OPEN=6`, `DEFERRED=1`, `ELEVATED=0`,
  `CLOSED=0`; seven rows.
- Closed archive after archive: three rows.
- `TM-PEC-009` remains `DEFERRED` with its trigger unchanged. Its exact CSV
  line SHA-256 is `6aa7f0f537cb6841a021176f2b5cd2db3754321a23f8cdffe0d622aa504130fa`
  both at `HEAD` and after this act.
- No other PEC register row changed.

Final register hashes:

| Path | SHA-256 |
|---|---|
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | `825a792138111dfcb868e6c704b5240be6d9da6ec7af463cc05a116353305532` |
| `_DomainEngines/pec/_TaskManagement/REGISTER_CLOSED.csv` | `89fa0eb4c11967734f1c8a653d918ebe587ccddfe50bdc2b2a2f18329562756a` |

## Checks and echoes

- Live-register validation: `PASS` (seven rows).
- Closed-register validation: `PASS` (three rows).
- Final federation: `COMPLETE`, zero register writes; PEC totals match the
  post-archive counts above.
- Staleness: none for the changed row. Both original source hashes and the
  new evidence hash match the cited live bytes.
- Closure echo: the original `ScopeLedger.csv` SOW-077 source and D-PEC-75
  handoff still describe OI-003 as open. This is an expected, reported echo:
  D-PEC-78 expressly leaves accepted-decomposition propagation to
  SCOPE_CHANGE. Task Management does not rewrite either source and does not
  infer that propagation is complete.
- Escalation: none created here. HELP_HUMAN separately owns fan-in of the
  SCOPE_CHANGE intake already launched for the D-PEC-78 effect.
