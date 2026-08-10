# TM-PEC-011 owner ruling and row-maintenance application — 2026-08-09

> **Record type:** owner-ruling preservation and mechanical application
> evidence.
> **Scope:** exactly `TM-PEC-011` in the live PEC Task Management register.
> **Archive:** not authorized in this tranche; the closed row remains live.

## Verbatim owner ruling

> TM-PEC-011: RESOLVED_WITH_CHANGE.

The ruling was received on 2026-08-09 after preparation artifact
`_DomainEngines/pec/_TaskManagement/TM-PEC-011_DISPOSITION_PREP_2026-08-09.md`,
SHA-256
`2465d4916730364bd063054c729f1fa6938b21ccbfa73e490001c7218d5c2596`.
It selects Option A exactly. No additional owner direction authorized archive,
receipt, acceptance, lifecycle, source, review, plan, PRD, Git, or foreign-loop
effects.

## Basis and preflight

- Checkout HEAD:
  `d269f0e04204bc463a11684499213b2283bd28f7`.
- `origin/main` advanced concurrently to
  `6ada6f257b55c20265bd0e82bf19fa96bb86c0bc`; read-only comparison found no
  change between those commits in the PEC live/closed Task Management
  registers or the TM-PEC-011 DEL-01-06 source/control/REVIEW evidence paths.
- Reliance-hold exact-correction preparation check: `ALLOW`.
- Preflight federation: `COMPLETE`; 4/4 canonical live registers and archives
  valid; zero invalid, unreadable, or ambiguous inputs; zero register writes
  by the helper; zero PEC-presented findings.
- Preflight PEC counts: `OPEN=17 / DEFERRED=1 / ELEVATED=0 / CLOSED=0`;
  archive 7.

## Exact before row

Live-register SHA-256 before:
`7fd9fbd7a3b42923ab0eed6e0088bb3fe5b53c8cbab749fa0a46ca8581d71fa4`.

```csv
"1.0","TM-PEC-011","DEL-01-06 SCA-004 ScopeOfWork currency","DEL-01-06 RF-002 records that its accepted revision-1.3 ScopeOfWork covers only SOW-094 and says OI-003 is open, while revision 1.4 adds SOW-077 and resolves OI-003, so contract currency requires later owner-gated repair and review.","projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv row RF-002","a5e15e978e970bf76ce8497bd622ee41d73334366aeae9716c7424de96130a32","CAND-PEC-2026-08-03-01","Checking; Deliverables; Approval; Work","DEL-01-06; RF-002; SCA-004; D-PEC-78; SOW-077; OI-003","NONE","SCA-004","TBD (owner promotion reserves assignment for next TASK_MANAGEMENT triage; no agent A, K-TM-3)","TBD","Owner promotion 2026-08-03 reserves priority for the next TASK_MANAGEMENT triage","OPEN","","","","","","","2026-08-03","2026-08-03","","Owner-promoted concern only; routing reserved for next TASK_MANAGEMENT triage; no handoff, dispatch, repair, lifecycle act, artifact acceptance, release, or professional reliance"
```

## Applied Option A effects

Only these fields changed:

- `SourceSha`:
  `a5e15e978e970bf76ce8497bd622ee41d73334366aeae9716c7424de96130a32`
  → `f114d52b264109d9c89b9f519b6c532a3dc4cf4f1e38a1b1297055dbd647fd8c`;
- `Status`: `OPEN` → `CLOSED`;
- `Disposition`: blank → `RESOLVED_WITH_CHANGE`;
- `EvidenceRef`: populated with current RF-002, immutable Review Summary, and
  accepted successor SOW paths;
- `EvidenceSha`: populated in corresponding order with `f114d52b...`,
  `c5919cd3...`, and `5fdcfd96...`;
- `EvidenceQuote`: populated with the Gate 4 / RF-002 resolution statement;
- `LastReviewed`: `2026-08-03` → `2026-08-09`;
- `Closed`: blank → `2026-08-09`; and
- `Notes`: appended with the ruling record, opening-source provenance, and
  non-effects.

`Assignment`, `Priority`, `PriorityBasis`, `Trigger`, `ElevatedTo`, and every
other row field remain unchanged.

## Exact after row

Live-register SHA-256 after:
`6f7eb2a528a8a38ee01b94f5a028632d95297c82f4fa197f4c62f7102fef9264`.

```csv
"1.0","TM-PEC-011","DEL-01-06 SCA-004 ScopeOfWork currency","DEL-01-06 RF-002 records that its accepted revision-1.3 ScopeOfWork covers only SOW-094 and says OI-003 is open, while revision 1.4 adds SOW-077 and resolves OI-003, so contract currency requires later owner-gated repair and review.","projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv row RF-002","f114d52b264109d9c89b9f519b6c532a3dc4cf4f1e38a1b1297055dbd647fd8c","CAND-PEC-2026-08-03-01","Checking; Deliverables; Approval; Work","DEL-01-06; RF-002; SCA-004; D-PEC-78; SOW-077; OI-003","NONE","SCA-004","TBD (owner promotion reserves assignment for next TASK_MANAGEMENT triage; no agent A, K-TM-3)","TBD","Owner promotion 2026-08-03 reserves priority for the next TASK_MANAGEMENT triage","CLOSED","","","RESOLVED_WITH_CHANGE","projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv row RF-002; projects/pec/execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-04_1113/Review_Summary.md; projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md","f114d52b264109d9c89b9f519b6c532a3dc4cf4f1e38a1b1297055dbd647fd8c; c5919cd313dece639c2c3ff11f6c6ad86a47c3c9aef4bfb9291668f76300f8fd; 5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8","Gate 4: COMPLETE — owner-adopted REVISE becomes RF-002's final disposition at exact SOW acceptance; RF-002 is RESOLVED.","2026-08-03","2026-08-09","2026-08-09","Owner-promoted concern only; routing reserved for next TASK_MANAGEMENT triage; no handoff, dispatch, repair, lifecycle act, artifact acceptance, release, or professional reliance; CLOSED RESOLVED_WITH_CHANGE by verbatim owner ruling 2026-08-09 preserved in TM-PEC-011_RULING_APPLICATION_2026-08-09.md; opening SourceSha a5e15e978e970bf76ce8497bd622ee41d73334366aeae9716c7424de96130a32 preserved here as pre-resolution provenance; closure records exact successor SOW change and REVIEW acceptance only and creates no artifact acceptance, lifecycle advance, source change, release, or professional reliance"
```

## Post-write checks

- Live PEC register validation: PASS, 18 rows.
- Closed PEC register validation: PASS, 7 rows.
- Post-write federation: `COMPLETE`; 4/4 canonical live registers and archives
  valid; zero invalid, unreadable, or ambiguous inputs; zero register writes by
  the helper; zero PEC-presented findings.
- Post-write PEC counts:
  `OPEN=16 / DEFERRED=1 / ELEVATED=0 / CLOSED=1`; archive 7.
- Other namespaces remain ROOT `12 / 9 / 0 / 0`, APP `13 / 3 / 0 / 0`, and
  PIP `10 / 24 / 0 / 0` (`OPEN / DEFERRED / ELEVATED / CLOSED`).
- The 22 disclosed program-wide typed status divergences remain outside PEC
  and are not acted on here.
- `git diff --check` for the register: PASS.
- Register diff scope: one removed row plus one added row, both TM-PEC-011;
  all unrelated live rows are byte-identical.
- Archive SHA-256 before and after:
  `bf0d5537686d3dba23ad2e3c1b91d989850cda04e98e92dc545516829c9242b6`.

## Archive state and non-effects

Archive remains pending an ordinary closeout authorization. Option A's
preparation explicitly placed archive/receipt after a separate authorization,
and the received ruling selected only `RESOLVED_WITH_CHANGE`; therefore this
tranche leaves TM-PEC-011 `CLOSED` in the live register.

This row-maintenance act records the owner's disposition only. It does not:

- accept or change DEL-01-06 product/source/configuration/test artifacts;
- modify RF-001, RF-002, the accepted SOW, `_REVIEW.md`, `_STATUS.md`, or any
  immutable review evidence;
- advance Gate 5 or lifecycle (`HOLD` / `INITIALIZED` remain unchanged);
- alter decomposition, SCA-004, D-PEC-78, dependencies, receipts, plans, PRD,
  source, another Task Management row, or another loop's register;
- create priority, assignment, scope, release, reliance, or receiving-loop
  duty; or
- stage, commit, push, merge, archive, or create a pull request.
