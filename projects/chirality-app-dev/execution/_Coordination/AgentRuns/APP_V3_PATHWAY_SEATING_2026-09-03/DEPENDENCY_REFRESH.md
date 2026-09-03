# DEPENDENCY REFRESH — additive v3 gate/handoff rows and closure audit

**RunID:** `APP_V3_PATHWAY_SEATING_2026-09-03` · **Node:** N2

## Method

The registered `TASK + dependency-extract` method (`skills/dependency-extract/SKILL.md`,
`TOOL_POLICY.md`, `QA_CHECKS.md`) was applied in-line by the ephemeral Agent 2
generalist with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`,
`CONSUMER_CONTEXT=RECONCILIATION`, decomposition
`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at
`d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f` (SHA-256
`932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`) —
the same overrides the Gate-5 run record used for its four carriers
(`execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N4-SCOPE-CHANGE-01/children/TASK-DEL-*/LAUNCH_BRIEF.md`).
Differences from Gate 5, stated so nothing is over-claimed:

- The pass is **additive and bounded**: exactly one new `EXECUTION` row per
  listed carrier, making the gate or handoff edge a seated `Remaining` item
  needs explicit. Existing rows are preserved byte-identically — no
  `LastSeen` refresh and no retirement — so a full two-pass re-extraction is
  not claimed for them.
- No TASK run record was written under `_run_records/` because that path is
  outside the sealed write set; this file is the durable run record.
- Root-owned targets keep `TargetLocation=TBD`; no Root path is invented
  (Gate-5 convention).

## Rows added

| Carrier | Row | Type / TargetType | Target | Evidence (file, ref) | Consumed by |
|---|---|---|---|---|---|
| DEL-08-04 | DEP-08-04-011 | CONSTRAINT / EXTERNAL | Root WP-03/WP-05 fixtures (DEL-02-07, DEL-02-10 accepted returns) | `ScopeOfWork.md#REQ-005` | DEL-08-04-V3-01 |
| DEL-09-06 | DEP-09-06-011 | INTERFACE / DELIVERABLE | DEL-04-05 credential bridge (shared `frontend/electron/api-key-ipc.ts` surface) | `ScopeOfWork.md` verification CLM (key storage checks) | DEL-09-06-V3-01 |
| DEL-05-01 | DEP-05-01-013 | INTERFACE / EXTERNAL | Root-owned daemon session store and resume semantics | decomposition `#L322` | DEL-05-01-V3-02 |
| DEL-03-01 | DEP-03-01-009 | INTERFACE / EXTERNAL | Root-owned runtime contracts: API v2 / event schema v2 | decomposition `#L303` | DEL-03-01-V3-01 |
| DEL-03-03 | DEP-03-03-011 | INTERFACE / EXTERNAL | closed Root API/event schema v2 behind services | decomposition `#L305` | DEL-03-03-V3-01 |
| DEL-05-02 | DEP-05-02-013 | INTERFACE / EXTERNAL | Root-owned daemon `HarnessEvent` records (schema v2) | decomposition `#L323` | DEL-05-02-V3-01 |
| DEL-05-03 | DEP-05-03-014 | INTERFACE / EXTERNAL | Root-runtime operational records and closed field vocabulary | decomposition `#L324` | DEL-05-03-V3-01 |
| DEL-04-05 | DEP-04-05-013 | CONSTRAINT / DOCUMENT | `docs/CONTRACT.md` K-NET-1 accepted endpoint set and K-KEY-1 (REF-002) | `ScopeOfWork.md` requirements CLM (RQ-010) | DEL-04-05-V3-02 |

Pre/post SHA-256 for each `Dependencies.csv` and `_DEPENDENCIES.md` are in
`Evidence/dependency_rows_added.json` and `SOW_IDENTITY_LEDGER.md`. The
other eleven carriers' registers are unchanged: their seated items' gates are
already expressed by existing rows (for example DEP-02-05-008/009,
DEP-09-05-015, DEP-08-05-004/011) or are owner acts that are not information
flow.

## Deterministic checks (Function 5)

- `python3 tools/validation/validate_dependencies_schema.py <Dependencies.csv>`: PASS on all eight changed registers (29 required columns; parseable).
- `python3 tools/validation/validate_enum.py <ENUM> <value>` on every enum field of each new row: PASS.
- `tools/validation/validate_id_format.sh`: the generic three-digit profile rejects the accepted two-digit App identities (`[WARNING] PROJECT_ID_FORMAT_PROFILE`), the same finding recorded by the Gate-5 refresh; accepted decomposition IDs are preserved.
- Parent anchor check: PASS on all eight (exactly one ACTIVE `IMPLEMENTS_NODE`).
- `_DEPENDENCIES.md` count tables were reconciled to the CSV after the append. The reconciler also corrected pre-existing count drift that predates this tranche (recorded here rather than silently absorbed): DEL-03-01 (`ACTIVE rows`, `RETIRED rows`, `EXECUTION rows`, `PENDING rows` had not reflected the retired DEP-03-01-006), DEL-03-03 (retired DEP-03-03-009 uncounted), DEL-05-02 (retired DEP-05-02-007 uncounted), DEL-05-01 (`CONSTRAINT` type count), DEL-05-03 (`EXECUTION rows`, `UPSTREAM rows`), DEL-08-04 (`EXECUTION rows`, Lifecycle `ACTIVE`). Row bytes were not changed by the reconciler.

## Closure audit (as in the Gate-5 run record)

Command (repo root):

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/Evidence/dep_closure
```

Analyzer identity: `tools/coordination/analyze_dep_closure.py` SHA-256
`e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91` (identical
to the copy preserved by the Gate-5 audit). Exit status 0. Outputs under
`Evidence/dep_closure/` (`closure_summary.json`, `coverage.csv`,
`orphans.csv`, `scc_summary.csv`, `hubs.csv`, `bidirectional_pairs.csv`,
`id_normalization.csv`).

Result and parity with the accepted Gate-5 post-application audit
(`execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/SCA-APP-008-GATE5-POST-APPLICATION_2026-08-24/Evidence/`):

| Measure | Gate-5 audit | This run | Delta |
|---|---|---|---|
| registers schema-valid | 51 of 51 | 51 of 51 | none |
| total rows / evidence populated | 564 / 564 | 572 / 572 | +8 (the rows above) |
| ACTIVE deliverable endpoints resolved | 112 of 112 | all resolved; zero dangling | none |
| distinct directed edges | 98 | 99 | +1 (DEL-09-06 → DEL-04-05) |
| SCC (size > 1) | one, nine nodes: DEL-02-05; DEL-03-02; DEL-03-03; DEL-03-04; DEL-04-03; DEL-04-05; DEL-05-02; DEL-05-03; DEL-05-05 | identical membership | none |
| isolated deliverables | DEL-01-01, DEL-01-03, DEL-02-04, DEL-10-04, DEL-10-05 | identical | none |
| bidirectional pairs | DEL-02-05 / DEL-04-05 | identical | none |
| hubs (degree ≥ 20) / ID normalizations | 0 / 0 | 0 / 0 | none |

Verdict: `WARNINGS`, non-blocking, unchanged in kind from Gate 5. The
nine-node SCC is preserved as an objective-relative finding and is not
linearized; the accepted A2-B `DECOMPOSE` / `DECOMPOSE` / `INVERT` moves and
the non-gating E-018/E-020/E-032 posture remain in force. The new
DEL-09-06 → DEL-04-05 edge does not join the SCC (DEL-09-06 has no inbound
edge from an SCC member). DEL-01-01 remains an isolate by design: its
AT-053 item consumes routed notices and registers, which are not
deliverable-to-deliverable information flow in the App register grammar.
