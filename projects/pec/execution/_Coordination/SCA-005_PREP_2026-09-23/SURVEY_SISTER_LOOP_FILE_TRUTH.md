# SCA-005 prep — sister-loop file-truth survey (A1)

Run: `HELP-HUMAN-PEC-20260923-SCA005`, node A1. Role: TASK (Type 2), no
delegation. Brief: `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/A1_SURVEY.md`
(`f32e879f043a1205f4cc4eb2a56c8dab9f430a52da069bfe539f7d77246f0b05`).
Accepted basis: `D-PEC-86` §3 I-1
(`7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b`).

**Examined through:** `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (HEAD = `origin/main`
basis named in D-PEC-86). All SHA-256 values are of the HEAD blob for tracked
files and of working-tree bytes for the five untracked run inputs (brief, RUN.md,
SUPPLIED_BASIS.json, D-PEC-86, assessment). One tracked file differs in the
working tree (PEC `_DECISIONS/_REGISTER.md`, an in-run D-PEC-86 row); HEAD bytes
were relied on. `SURVEY_MANIFEST.json` lists every relied-on file.

**Epistemic status.** Derivative observation, not authority, not a ruling and
not a scope proposal. Cited files govern on any disagreement (K-AUTH-1).
Content-minimal (PEC-K-10): only paths, heading and key names, column headers,
counts, states, PR numbers, commit SHAs and hashes are reproduced. Counts marked
"census" are computed over `git ls-files` at HEAD; the individual files counted
are not hashed.

Loop labels: `app` = `projects/chirality-app-dev`, `piping` =
`projects/chirality-piping`, `runtime` = `projects/chirality-runtime`, `pec` =
`projects/pec`, `root` = repository root `execution/` + `docs/governance_harness/`.
`bridge` (`_DomainEngines/bridge/`) is not a brief column but is a PRD §7.1
loop and is reported where relevant.

---

## 1. Ingest-surface matrix

### 1.0 Status grid (rows = PRD surface classes; cells = CURRENT / HISTORICAL-FROZEN / ABSENT)

| Surface class (PEC basis locator) | app | piping | pec | root | runtime | bridge |
|---|---|---|---|---|---|---|
| S1 `_STATUS.md` (PEC-RCN-002; SOW-011) | CURRENT, no `## Remaining` | CURRENT, no `## Remaining` | CURRENT, `## Remaining` live | CURRENT (all RETIRED state) | CURRENT, no `## Remaining` | ABSENT |
| S2 decision register / packets (SOW-012) | CURRENT | CURRENT | CURRENT | CURRENT (different header) | ABSENT (adapter points at a non-register) | CURRENT (tier-0) |
| S3a `loop/LOOP_RECEIPTS.md` ledger (SOW-013) | HISTORICAL-FROZEN at Receipt-264 | HISTORICAL-FROZEN at Receipt-162 | CURRENT | CURRENT (last Receipt 151, 2026-09-09) | CURRENT (3 receipts) | CURRENT (last Receipt 36, 2026-08-02) |
| S3b `AgentRuns/<RunID>/RECEIPT.md` | CURRENT rule, 0 instances | CURRENT rule, 1 instance | ABSENT | ABSENT | ABSENT | ABSENT |
| S4a `WORK_GRAPH.json` (SOW-015) | HISTORICAL-FROZEN (58 tracked) | HISTORICAL-FROZEN (86) | CURRENT-by-own-practice (2) | CURRENT (48; dispatch validator) | HISTORICAL (4) | ABSENT |
| S4b `WorkGraphs/<undertaking>/WORK_GRAPH.md` | CURRENT (1) | CURRENT (2) | ABSENT | ABSENT | ABSENT | ABSENT |
| S4c `STATUS.json` / `RUNTIME_SUMMARY.json` (SOW-014) | HISTORICAL (246 / 39) | HISTORICAL (292 / 34) | CURRENT-by-own-practice (13 / 0) | CURRENT (403 / 23) | — (0 / 8) | ABSENT |
| S5 `Dependencies.csv` (SOW-015) | CURRENT | CURRENT | CURRENT | CURRENT | CURRENT | ABSENT |
| S6 workplans / `LOOP_INIT.md` (SOW-016) | LOOP_INIT CURRENT (evergreen); workplan HISTORICAL | LOOP_INIT CURRENT (evergreen); workplans HISTORICAL | LOOP_INIT CURRENT; workplans retired | LOOP_INIT + `CURRENT_WORKPLAN.md` CURRENT | LOOP_INIT CURRENT; no workplan | LOOP_INIT + workplan CURRENT (dormant) |
| S7 `_harness/adapter.yaml` (SOW-017) | CURRENT (unchanged since 2026-07-01) | CURRENT (unchanged since 2026-07-02) | ABSENT | CURRENT (`root-harness-adapter/v1`) | CURRENT | ABSENT |
| S8 `MEMORY.md` (not in PEC ingest list) | CURRENT (`## Runs` in 1/54) | CURRENT (`## Runs` in 3/101) | CURRENT (1 file) | — (315 under root `execution/`, not surveyed) | ABSENT | ABSENT |
| S9 Task Management register (not in PEC ingest list) | CURRENT | CURRENT | CURRENT | CURRENT | ABSENT | ABSENT |
| S10 presence / session sources (PEC-PRS-001, PEC-STR-003) | App-owned Runtime service (private) | none | none | none | service implementation | none |

"HISTORICAL-FROZEN" for S3a app/piping is by instruction, not by an in-file
banner: the ledgers were last changed at `0407cb978` (2026-09-22) and the
central-receipt tranche's `scope_limits` keep existing ledgers historical
without backfill (`ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml`,
`e56dd83654b35875933a869f3d6ba9494ad10fa110c521f17a632f7aa38a40be`);
Piping `AGENTS.md` (`d9481951912ceffdd5bc47dbb6549bf0044f5d92f9fe6a9b11ba5969bfebc792`) states that historical-receipt
validation requires no new ledger entries.

### 1.1 S1 — `_STATUS.md`

| Loop | Path pattern (adapter glob) | Shape at HEAD | Change event |
|---|---|---|---|
| app | `execution/PKG-*/1_Working/DEL-*/_STATUS.md` (54 files) | `# Status: <DEL>`; bold `**Current State:**`, `**Last Updated:**`, plus `**Authorization Basis:**`/`**Checking Approval SHA:**` on some; `## History`. 0/54 carry `## Remaining`. States: IN_PROGRESS 53, OPEN 1. Dialect declared `prose-bullet-v1`. | Remaining retired: PRs #861, #863 (2026-09-22), final #870 merge `866bfafeb06bbdf5fcbd8b7395f74f54cb4f3813`; manifest `APP-REMAINING-RETIREMENT-20260923.yaml` (`1d20d6ad5b548fa9126f8609038c891138025af524cf0e386d7a6b5cfd22f746`); account `execution/_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/` (not read). |
| piping | `execution/PKG-*/1_Working/*/_STATUS.md` (106 by glob) | Same bold-field shape; 0/106 carry `## Remaining`. States: IN_PROGRESS 100, OPEN 5, ISSUED 1. | PRs #862, #864 (2026-09-22), final #871 merge `23a33eb1d970f8a4f1b4bfa9aa54ffe1c84da17f`; manifest `PIPING-REMAINING-RETIREMENT-20260923.yaml` (`009307b5cf0e35cdc92eb8f481a77d7ba7432104c33b76f0b9f79868291a609e`); account `_TaskManagement/TM_PIP_REMAINING_RETIREMENT_20260922/` (not read). |
| pec | `execution/PKG-*/1_Working/DEL-*/_STATUS.md` (64) | Same shape; 57/64 carry `## Remaining`. States: OPEN 32, INITIALIZED 26, CHECKING 4, IN_PROGRESS 2. Sample DEL-01-03 `73ae042e9204f1884642f74bced1a08a0c0166c6eeec321dbcf91ff08524e5a2`. | Unchanged; PEC retains Remaining-based selection (`loop/LOOP_INIT.md` §4–5, `ec9cc14df99dc627122ec99c6b5b5e9dffd26631445ebec42679205b49835053`). |
| root | `execution/PKG-*/1_Working/DEL-*/_STATUS.md` (53) | All 53 state `RETIRED`; headings `## History`, `## SCA-005 retirement record` (53), `## Remaining` (46). Dialect `root-historical-v1` (`execution/_harness/adapter.yaml`). | Root SCA-005 (2026-09-05/06, `execution/_ScopeChange/SCA-005_*`) — see DR-18 on the ID collision. |
| runtime | `execution/PKG-*/1_Working/*/_STATUS.md` (7) | All INITIALIZED; `## History` only; 0 `## Remaining` although Runtime `loop/LOOP_INIT.md` (`890ed040fd518c2448450583727f159d6059e9bdfed8d532b3209d3130600569`) names `_STATUS.md` Remaining as part of its work surface. | Runtime project migration PR #727 (merge `8209bc54e0d133b19437c93b184cd50ba3d43489`). |

Older shapes on disk: census 1,757 tracked `_STATUS.md` files by name (root
1,283, pec 294, piping 117, app 56, runtime 7); the excess over the adapter
globs is fixture/evidence copies and PEC frozen-corpus fixtures.

### 1.2 S2 — decision registers and packets

| Loop | Path | Header (columns) | Rows (ID-bearing, approx.) | Last change |
|---|---|---|---|---|
| app | `execution/_Coordination/_DECISIONS/_REGISTER.md` (`648117032619476bc6a98506b16225c0922e311a5867a862c96072ac0bca3f79`) | `ID \| Decision \| Blocks \| State \| Packet \| Ruling record` | 132 `D-APP-*` rows | `a89b5ddec` 2026-09-22 |
| piping | `execution/_Coordination/_DECISIONS/_REGISTER.md` (`b4db2b062183f917f2e3dc26796249d41cc99403d291432acfca6a1c98496697`) | same 6 columns | 83 `D-*` rows | `761c02856` 2026-09-23 (D-76) |
| pec | `execution/_Coordination/_DECISIONS/_REGISTER.md` (`fb3a3a6b483522fce3a36a0974cbf98ef2fbba43c495ce8b7b10d3a6dc3a22ba`, HEAD) | same 6 columns | 82 `D-PEC-*` rows (through D-PEC-85 at HEAD) | `863bc4b1c` 2026-09-08 |
| root | `docs/governance_harness/_DECISIONS/_REGISTER.md` (`1daaf65cc2ef6aeabfe769ab99e5918156dbd0c150b62ae060b70bac9e349760`) | `ID \| Decision \| HumanRuling \| Unblocks` (4 columns); supplements as rows (`D-GOV-43 (supplement)`) | 44 `D-*` rows | `fa8a69f0e` 2026-09-21 |
| runtime | none; `_harness/adapter.yaml` `decision_register:` → `execution/_Coordination/MIGRATION_APPLICATION.md` (`93977f5968a08a0e319dd76fc67fc878e378726b72caa099bc59c948206437c3`), a `Successor \| Production SHA256` table | — | 0 decision rows | `b520e0f1f` 2026-09-05 |
| bridge | `_DomainEngines/_DECISIONS/_REGISTER.md` (`ebccf23234c7755a20555397fe12ccb708d7bebf6826fd9806b695f5fcd10e48`) | `ID \| Decision \| My recommendation \| HumanRuling \| Unblocks` (5 columns) | 29 `D-T0-*` rows | `d4f53a70e` 2026-08-02 |

Root also now records un-numbered amendment records outside the register, e.g.
`docs/governance_harness/_DECISIONS/AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md`
(`f934eeec032bc109e4c1180feb74e63c7179e90f087bcd34109d29543e5dc17e`),
which describes itself as an amendment record rather than a numbered D-GOV decision. No decision-register
shape change occurred this week; register grammars are CURRENT.

### 1.3 S3 — receipts

**S3a ledgers** (`loop/LOOP_RECEIPTS.md` unless stated):

| Loop | Path / SHA-256 | Entry grammar | Contract marker / validator | Latest entry |
|---|---|---|---|---|
| app | `97544833c6190f68483de4a92905f1d044567aaa3b029b73b0bb9f9a862c25c4` | `- **YYYY-MM-DD — Receipt N** (title).` + indented `  - Field:` records | `receipt-contract-v2` marker; `D-APP-57`, frozen-through Receipt-52; `tools/validation/validate_app_dev_loop_receipts.py` (`daf01933ecade2e62db95cbb48cdb763ae99f64da85b31e0e8b934ebbfd62f64`) | Receipt 264, 2026-09-22, Examined-Through `379df923…` |
| piping | `9d514ff6f8c5ec87a1ad5627d266170ce7c54ece8832d9c68483fe93eacc60be` | same | marker; `D-44`, frozen-through Receipt-44; `validate_piping_loop_receipts.py` (`b6891b75614a183e4f0e33be8315a8ac49a2a4baa9a9d11ccfd8f704504a7965`) | Receipt 162, 2026-09-22 |
| pec | `b51e17bae1be325e0c3dd9bfa672d3218f07efa55a452f9ac0a4cceabd4403c3` | same | marker; `D-PEC-80`, frozen-through Receipt-166; `validate_pec_loop_receipts.py` (`8eb6299558a4038f5a62f5f979a86460f16fece6ed6e2fcb8dd00ce12952bad9`) | Receipt 178, 2026-09-22 |
| root | `execution/_Coordination/LOOP_RECEIPTS.md` (`9f2f3186742276c641d50ee00ffa02824f268eb404a8124aa3a37e83a8d1dec4`) | `### Receipt N — YYYY-MM-DD — title` headings | none; 0 `Receipt-ID` tokens | Receipt 151, 2026-09-09 |
| runtime | `8ba7de3d37f3dd00fba8444071792cc3f25de2776a081d68df924eea22381802` | `## Receipt N — YYYY-MM-DD — title` + bold-label bullets | none (Runtime LOOP_INIT disclaims any receipt validator) | Receipt 3, 2026-09-06 |
| bridge | `_DomainEngines/bridge/LOOP_RECEIPTS.md` (`16d58c513fc08b08082bdbfd0d31703b45312d0b175cc162493e0e0554b0ee67`) | `- **YYYY-MM-DD — Receipt N** (title).` | none | Receipt 36, 2026-08-02 |

Shared engine: `tools/validation/loop_receipt_contract.py`
(`1b6907f5cc9ec4506a9954562a99df3e43c4fa62fab120f1dbec2726c4f687aa`): heading regex
`^- \*\*(date) — Receipt (N)\*\* \((title)\)\.$`; record regex `^  - Field:`;
allowed fields `Receipt-ID, Examined-Through, Parent-Receipt, Owner-Direction,
Stale-Map-Delta, Pointers, Checks, Model-Attribution, Gate-Outcome`; required
`Receipt-ID, Examined-Through, Parent-Receipt, Gate-Outcome`; Gate-Outcome tokens
`STOPPED|EXECUTED|AWAITING_OWNER`.

**S3b central per-undertaking receipt** (App/Piping only):

- Rule: `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`, one per
  undertaking, `<RunID>` = the graph's stable run identity (App/Piping
  `loop/LOOP_INIT.md` §5: app `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25`,
  piping `c712b6487faa3fab461e181aad1a6c16a2cb0eb734c510744e5037289105df1b`; construct-local-work-graph §3).
- Change event: tranche `ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923`, commit
  `6900f7984caab455bdc2e80f3b3b06a382a230ab`, PR #877 merge
  `b3372a49c1184632fc46d92feaaa1c8adee8afa0`; PEC notice
  `execution/_Coordination/NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md`
  (`8e7170aee2c40ddd0f0be5b72f934d3af3fcdc158a1dc0a4d28a9f4f25850a71`).
- Instances at HEAD: 1 (Piping `PIPING_LINTER_SCOPE_20260923/RECEIPT.md`). App: 0.
- Observed grammar (n = 1): `# Loop receipt — <RunID>`, blockquote status line,
  `## Result`, `## Checks and limits`, `## Cursor and pointers`. The cursor section
  reuses the ledger field names as bold-label bullets (`- **Receipt-ID:**` etc.),
  with `Receipt-ID` = the run ID string (not `Receipt-N`), `Examined-Through` a
  prose-prefixed backticked 40-hex SHA, `Parent-Receipt` "none", and a prose
  `Gate-Outcome` with no token. It is not parseable by `loop_receipt_contract.py`;
  no validator for `RECEIPT.md` exists (`git grep` of `tools/` and `.github/`
  finds no reference).

### 1.4 S4 — graphs and run-evidence JSON

| Loop | Current graph location | Shape | Older shapes on disk (census) |
|---|---|---|---|
| app | `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` | Markdown; headings `## Intent and selected route`, `## Deliverable scope`, `## Work`, `## Current state and recovery`; `## Work` table 5 columns (`ID / outcome \| … \| Completion check \| State / result`); state token as cell prefix (`PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN, COMPLETE`); "Stable run identity" bullet in Intent. No frontmatter or JSON. | `WORK_GRAPH.json` 58 (newest `AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/`, 2026-09-22); non-canonical `WORK_GRAPH.md` 40 under `AgentRuns/`; `STATUS.json` 246, `RUNTIME_SUMMARY.json` 39 |
| piping | same pattern | same template; columns 2–3 labels vary per graph (`Scope and owner` / `Deliverables and work scope`; `Needs` / `Needs / why`); extra headings (`### Warranted authorization rule`, `## Supplied basis`) occur | `WORK_GRAPH.json` 86 (newest 2026-09-22 under `AgentRuns/HELP-HUMAN-PIPING-20260921-RECONCILIATION/` and `_Reconciliation/…/R5/`); non-canonical `WORK_GRAPH.md` 5; `STATUS.json` 292 (newest 2026-09-17), `RUNTIME_SUMMARY.json` 34; archived 2026-09-19 graph `loop/.archive/2026-09-19-clarifications/UI_WORK_GRAPH.pre-clarification.json` |
| pec | own practice: `AgentRuns/<RunID>/WORK_GRAPH.json` or `RUN.md` table; DEL-local `_run_records/<run>/WORK_GRAPH.json` | JSON (2 tracked) / Markdown table | `STATUS.json` 13 |
| root | `execution/_Coordination/AgentRuns/<RunID>/WORK_GRAPH.json` (validator `tools/validation/validate_root_work_graph_dispatch.py`) | JSON | 48 JSON, 4 `.md`; `STATUS.json` 403, `RUNTIME_SUMMARY.json` 23 |
| runtime | none declared | — | `WORK_GRAPH.json` 4, `RUNTIME_SUMMARY.json` 8 |

Change events: `ROOT-LOCAL-WORK-GRAPH-METHODS-20260922` (PR #846 merge
`9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`; `f0894335d6101f59698564e9600e700d240eb385b8306dfa075dffdfc4b79d30`);
`ROOT-DEVELOPMENT-LOOP-MEMORY-20260922` + amendment record (PR #858 merge
`b3e2ce4ec74e01d6f393fc0bc069699bb079df91`; `7df517e6cfe0da4a9dc35cef146aa070edef677e76c0df2afc2fa7222232735b`);
`ROOT-EVERGREEN-DEVELOPMENT-LOOPS-20260923` (PR #878 merge
`3c41c6f59968f792c9f538ce530838a8aa9b72e0`; `bfe305e9461d228d171d5e66102f8dd2ba36f85570aa2fab13bdd6d430e5147f`);
`ROOT-WORKGRAPHS-PATH-ANCHOR-20260923` (merged via PR #872 merge
`db5bb38730f4f59e6c3f3152bea38af2f0c4bb1d`; `e7149e9bd9330e738b650af090f23dec0d2abb927e377cd78a54bdc00b450dc4`),
which adds canonical `projects/*/execution/_Coordination/WorkGraphs/<u>/WORK_GRAPH.md`
to `tools/practitioner_harness/surface_roles.py` line 154
(`7786998c8eb047e770c98b3e846353d40a307f5cfa9862c95681c3405866949e`) and
`tools/validation/validate_path_anchors.py` line 92
(`9981b426b6d9c8bb760ab35ee66b1bb0c91bc6427fde282b33506ec99879e07d`) — the only Root code that
distinguishes the canonical graph from same-named files. Its scope limits exclude
colocated run evidence from live-surface selection.

New evidence-JSON shapes observed in fixtures: `schema:
chirality-software-check-evidence/v1` (keys `profile, project_root, results,
schema, status, workspace_root`; 5 files in the App graph folder), Vitest-style
summaries (keys `generatedAt, status, testCount, results, …`), and a Piping
DEC-025 sweep (`schema_version: 3`, keys `artifact, git, surfaces,
overall_status, …`). None is `STATUS.json` or `RUNTIME_SUMMARY.json`.

### 1.5 S5 — dependency registers

Census at HEAD (`Dependencies.csv`): app 52 (all 29-column, `v3.1`), piping 128
(110 × 29 columns, 18 × 31 columns), runtime 7 (29), pec 64 (29; 63 CRLF), root
728 (723 × 29, 5 × 31). All data rows `RegisterSchemaVersion` `v3.1`. Companion
`_DEPENDENCIES.md` per deliverable. Piping project DAG pointer
`execution/_DAG/_LATEST.md`; App `dag_pointer`
`execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md`.
No change event this week; CURRENT. `WORK_GRAPH.json` is no longer an App/Piping
dependency source (S4).

### 1.6 S6 — workplans and `LOOP_INIT.md`

| Loop | LOOP_INIT (SHA-256; last change) | Workplan status |
|---|---|---|
| app | `loop/LOOP_INIT.md` `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25`; `1fafb0842` 2026-09-23 | `plans/workplans/WORKPLAN_2026-07-18_app_dev_loop.md` carries a historical/superseded banner (`111dc6d9c33d64a1626083f6a56b7bc29a2e5d63ca2a8cb3f7da2493e8abcc17`); 9 workplan-named files in app |
| piping | `loop/LOOP_INIT.md` `c712b6487faa3fab461e181aad1a6c16a2cb0eb734c510744e5037289105df1b`; `1fafb0842` 2026-09-23 | `loop/WORKPLAN_2026-09-19_piping_loop.md` is headed as a standing-procedure pointer (`ae7dd4b65580cf0d5c023bb7f1f5664d011560e477fb1fcf6ff4742c8753d98e`) whose text still says LOOP_INIT points to the selected graph (superseded by #878); five older `WORKPLAN_2026-07-*` in `loop/`; two `loop/.archive/2026-09-19-*` snapshots each holding a prior `LOOP_INIT.md` |
| pec | `loop/LOOP_INIT.md` `ec9cc14df99dc627122ec99c6b5b5e9dffd26631445ebec42679205b49835053`; `b4ee0c577` 2026-09-12 | retired to `plans/workplans/` (D-PEC-80 D); Step 0 script errors if a workplan remains in the loop home |
| root | `execution/_Coordination/LOOP_INIT.md` `e23b86c52a2797ba92a6a2b56e4dc9242a0147579dfdb498f7cff914bd608082`; `b4ee0c577` 2026-09-12 | `CURRENT_WORKPLAN.md` pointer (`f332c0f14c1a25f9d04e7fedcdf0df448d98d6747a5d73db5125471165134fe0`) → `WORKPLAN_2026-08-27_root_v3_rc.md` |
| runtime | `loop/LOOP_INIT.md` `890ed040fd518c2448450583727f159d6059e9bdfed8d532b3209d3130600569`; created 2026-09-05 | none (its LOOP_INIT states that no workplan is selected) |
| bridge | `_DomainEngines/bridge/LOOP_INIT.md` `90e1be2a95cbd2fa90cc514de449f0cf5975de808efc367fb1a122b02766c920`; `5b3b68f14` 2026-07-12 | `WORKPLAN_2026-07-02_bridge_loop.md` (`32c72c2e666fd70fcfab1d19a8f82b9b6df776e8bd72ad3bb01c217ee9dda944`) |

App/Piping LOOP_INIT shape (evergreen, identical apart from the Project pointers
block): `# App|Piping development loop`, `## Project pointers`, `## 0. Read the
steering and recover the situation` … `## 6. Complete the graph and merge the
final PR`. They contain no undertaking pointer, step state or gate state; the
selected graph is recovered from steering (SPEC §9.8). Name-based census:
`LOOP_INIT.md` 11 tracked (6 live; others are proposals, preimages and archives).

### 1.7 S7 — `_harness/adapter.yaml`

| Loop | Schema | Keys present | Graph / receipt / MEMORY / TM keys | Last change |
|---|---|---|---|---|
| app (`f4fbbf1f675b9aa7e9e7b71f26841de7d5031107c498f72e48cee4b5f0009e98`) | `practitioner-harness-adapter/v1` | `plan, coordination, coordination_pointer, decision_register, dag_pointer, status_glob, exclude_globs, states, parser_dialect, dependency_register_structured, dependency_register_summary, drift_baseline_*, validation_commands, guard_*` | none | `a998ed1d3` 2026-07-01 |
| piping (`2de9d3ab3b3e3b2eb622c0959dc292eff06a11c3da7c2665798978df08c20554`) | same | same minus `coordination_pointer`, `dependency_register_*` | none | `b637475ba` 2026-07-02 |
| runtime (`fb70f812656bf51c217dfa104dc96a733fdb713a9071d563a447ca4fd27fff7e`) | same | `plan: docs/PRD_AUTHORITY.md`, `dag_pointer: ''` | none | `b520e0f1f` 2026-09-05 |
| root (`e481e79f1dd28d41bf47db50c58fa1ad50ed14e559fc3975240b6862a31275d4`) | `root-harness-adapter/v1` | `product, working_root, execution_root, prd, coordination, decision_register, status_glob, parser_dialect: root-historical-v1, baselines, mode: governance-only, governance_state, loop_init, receipts` | `loop_init`, `receipts` only | `d25d51fca` 2026-09-05 |
| pec | ABSENT | — | — | — |

Drift baselines are stale against HEAD globs (app 53 declared vs 54 found;
piping 101 vs 106). Two further `adapter.yaml` copies exist as run evidence
under `execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06/`.

### 1.8 S8 — deliverable `MEMORY.md`

- Required shape (template `docs/templates/MEMORY_TEMPLATE.md`,
  `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`): `# MEMORY - {{DEL-ID}}`, `## Runs`,
  table header `Run ID / date | Work in this deliverable | Result and source links`.
  Change events: amendment 2026-09-22 (§1 above; PR #858) and central-receipt
  tranche (#877 changed the template text to point at the central receipt).
- Observed at HEAD (census over `PKG-*/1_Working/*/MEMORY.md`): app 54 files,
  1 with `## Runs` (bullet form), 53 with legacy `## Decisions And Evidence`;
  piping 101 files, 3 with `## Runs` (bullet form); pec 1 file (DEL-01-03), no
  `## Runs`; runtime 0. **Zero `## Runs` tables anywhere.** The DEC-025 run
  (`PIP-DEC025-BASELINE-2026-09-23`) wrote dated `## 2026-09-23 — <RunID>`
  headings in 4 Piping MEMORY files rather than `## Runs` rows. Some MEMORY files
  carry YAML frontmatter (e.g. Piping DEL-10-04, `doc_kind: execution.memory`).

### 1.9 S9 — Task Management registers

`execution/_Coordination/_TaskManagement/REGISTER.csv` + `REGISTER_CLOSED.csv`
per loop; shared 25-column header beginning `RegisterSchemaVersion, ActionItemID,
Title, Concern, SourceRef, SourceSha, …` and ending `…, Opened, LastReviewed,
Closed, Notes`; all rows `RegisterSchemaVersion` `1.0`.

| Loop | Live rows (status) | Closed archive rows | SHA-256 (live / closed) |
|---|---|---|---|
| app | 21 (OPEN 7, DEFERRED 14) | 34 | `5ca17f4a25e72b90f8650779297d883a777623d895de6c6d2761891f499addad` / `4b7fe664a517fc164f23aaaa68202c384a20ed2013d72fa21aec04033bb680a8` |
| piping | 40 (OPEN 7, DEFERRED 32, CLOSED 1) | 12 | `b7c41d0888c2bdc48c24a1fea21ee0c321366cb326e19288bbbce2da8e9afc9d` / `60a3aab90ab26119ebef0a16343b49794e1718571499d61e751a5da8bd3c727d` |
| pec | 10 (OPEN 9, DEFERRED 1) | 15 | `d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d` / `ea730ae06f0805c720bbb29aed6d681c323e6d3b0c4a38d53db27e1075fafd94` |
| root | 18 (OPEN 10, DEFERRED 8) | 109 | `fb7ef7d816d348fa55fee596fbe1a427b745dad7c9b787180d2a9e677e3627af` / `995d7ffd46008e1f8a8e471105e799a89830ced97ff0a98b12b2f7b563692fbc` |
| runtime, bridge | ABSENT | — | — |

Method: `workflows/task-management/WORKFLOW.md` (`db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b`)
and `resources/contract.md` (`e1c97a76b8a411873ca86a6ef4351a7f76303e74331a52307a3705a83827c837`)
give the normal location as `execution/_Coordination/_TaskManagement/REGISTER.csv`
and require a D-GOV-33 federation survey across canonical registers and their
closed-row archives. No register schema change this week.

### 1.10 S10 — presence and session sources

See §3. At HEAD no loop writes a presence or session feed into the checkout.
The only session producer is the Runtime service, now instantiated privately
per owning application. No hooks-CLI or cmux implementation exists outside
`projects/pec` (`git grep` for "hooks cli"/"cmux" outside PEC returns only
2026-07-26 evaluation records and an alignment-manual source list).

---

## 2. Development-loop method facts (what each fixes as a required location or shape)

| Source (SHA-256) | Fixes |
|---|---|
| `workflows/construct-local-work-graph/WORKFLOW.md` (`24268f3545eae68ac86bbfcb830314f5c8539f6da9de08bf4365b14d6f544525`) | App/Piping graph at exactly `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, Git-tracked, committed early in the PR sequence; one current graph; nodes carry stable ID, deliverable binding, prerequisites, write boundary/owner, completion check, state; final closeout = bounded-reconciliation + conditional TM + one central receipt at `AgentRuns/<RunID>/RECEIPT.md` + terse MEMORY entries + final PR; no later commit may be required solely to write the final merge back into the candidate; historical graphs preserved at original paths; other loops keep their adopted recording rules. |
| `…/resources/work-graph-template.md` (`4411d0c25b1dc88da182e05660cb061d8e885ab97f4de8f27b05f7d3b0f12261`) | Headings `## Intent and selected route`, `## Deliverable scope`, `## Work`, `## Current state and recovery`; Work table header `ID / outcome \| Deliverables and work scope \| Needs / why \| Completion check \| State / result`; canonical node IDs W1, V1, P1, C1, M1, F1; state vocabulary PLANNED/READY/ACTIVE/BLOCKED/UNCERTAIN/COMPLETE; "Stable run identity" bullet. |
| `workflows/bounded-reconciliation/WORKFLOW.md` (`b40daec5d14877f32bcee133150ad66fc3fc9501116b5507591c7db0308bf683`) | One bounded closeout stage before the final PR; reads `ScopeOfWork.md`, `Dependencies.csv`/`_DEPENDENCIES.md`, `MEMORY.md`, `_REFERENCES.md`/`_CONTEXT.md`, `_STATUS.md` (lifecycle and history only, not an execution backlog); no deliverable-local decision record; returns pointers for the loop's central receipt and MEMORY entries. |
| `workflows/task-management/WORKFLOW.md` + `resources/contract.md` | Invocations: bounded intake, legacy-source retirement, register review; WORKING_ITEMS owns register writes; no separate Task Management receipt and no MEMORY work list; App/Piping receipt links the outcome; register location as in §1.9; optional `intake/<concern>.md`. |
| `docs/SPEC.md` §9.8 "Multi-agent run record" (`2d8b92471b9e33c58afede827116cfecedb4a1432ac029544418474bd81ca186`, lines 761–790) | Run records under `{EXECUTION_ROOT}/_Coordination/AgentRuns/<RunID>/` when the workflow uses that root; for adopting App/Piping loops the current graph is the WorkGraphs path; LOOP_INIT is evergreen with no undertaking-specific pointer; AgentRuns evidence links the graph and its examined revision rather than a second copy; other loops' graphs are not relocated. Last changed `1fafb0842` (#878). |
| `docs/templates/MEMORY_TEMPLATE.md` | `## Runs` table (§1.8); neither a future-work list nor a decision register. |
| `AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md` (`f934eeec032bc109e4c1180feb74e63c7179e90f087bcd34109d29543e5dc17e`) | Supersedes only D-GOV-17 M4-A's minimum MEMORY section for future entries; keeps `MEMORY.md` filename and `# MEMORY - {{DEL-ID}}` title; no mass rewrite; fixes the App/Piping WorkGraphs location and amends SPEC §9.8 and PRD_ROOT E-1 for adopting loops; other loops keep their accepted graph and evidence basis. |
| `ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml` | One final per-undertaking App/Piping receipt; ledgers and completed-run evidence stay historical, no backfill; PEC and Runtime unchanged. PR #877. |
| `ROOT-EVERGREEN-DEVELOPMENT-LOOPS-20260923.yaml` | Removes undertaking-specific LOOP_INIT pointers; canonical graph and central receipt locations retained; PEC loop and work selection excluded. PR #878. |
| `ROOT-WORKGRAPHS-PATH-ANCHOR-20260923.yaml` | Canonical WorkGraphs graphs classified CONTROL and path-anchor scanned; colocated evidence excluded; PEC cleanup deferred. |
| `ROOT-SCOPED-PR-CI-20260923.yaml` (`d140b2bcec517500c6d61f19274ec484123471e29f16074fb4b493af656b5775`) | CI routing only; `.github/workflows/pec-tests.yml` among surfaces; no loop-shape change. PR #879 merge `42bd234f671508ba9ab157e1981334ba8610279f`. |

Every one of these records routes an M6 notice to PEC that states PEC's loop,
receipts, graph location and work selection are unchanged
(`NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md`
`83515ebd8745372eb63b12b02948d065cbe7a9428eaef2da5a698a46060ac37b`;
`NOTICE_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md`
`545092c1841a55766fd58932216b852db43c3a2663d61125e317140821a35d5e`;
`NOTICE_2026-09-23_EVERGREEN_LOOP_INSTRUCTIONS.md`
`cc62933dd294c31cefa1c2abd5d36a742f5e67d48b9bcac6883dfd34baf95e5b`;
`NOTICE_2026-09-23_SCOPED_PR_CI.md`
`26d763192e88432afb1d996ec99791591b7d72cb94ecb3dcac2acaf16db6f744`).

---

## 3. Runtime topology facts for PEC presence and streams

Sources: `D-GOV-43_codex_host_replatform.md` (`08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899`),
`D-GOV-43_supplement_topology_A2.md` (`fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2`),
both published by PR #767 merge `d2878462be59a43b4afc175a8cce85abca9cf696`;
PEC notice `NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md`
(`3184697759b39db7569d70b5903a856c996ff6faade3cc1a1ba5d3de9213293d`);
`projects/chirality-runtime/README.md` (`025eab1edd95b9dcdd793c410270b491f11bbf52b8f5fb9c98ccb791bdd9d889`);
`docs/APPLICATION_CONSUMER_GUIDE.md` (`2f9f37788a17be9c5030c631dbb53be2f1b59a325bd51bc5bf6ac4e86a781865`, PR #880 merge
`06aff05a412b9e25ad022e5fc629c77ee51efbc6`); `docs/APPLICATION_TOOLS.md` (present,
`59e401d14d566814983ba4c242b8449b71ecdb6f3dec1134289c51f836cc307b`); route table
`packages/contracts/src/protocol.ts` (`efccad4b2198e5f877b724a309b0a3bf171b81a21d80f1d7c56b14b97eb1dc8c`);
SSE writer `packages/daemon/src/runtime-daemon.ts` (`e3c880a83d0bda0ea1a58c0b85809dcf3e52b73e796c1b668f59405c4052febd`);
App host `frontend/electron/runtime-service-host.ts` (`cf7a411531f4253ee669e31272e25a26baa099f988bdef4680339dc874c14801`).

**No longer exists**

- The per-user headless daemon (D-GOV-20 item 2, `a6a4fc4f0c8136f0cdf25eab155c98a03276248776ed9ff779df6c4b88523f11`) and its LaunchAgent/installer, supervisor second socket and job, hosted admission, identity binding, closed event union v2 and notification whitelist (A2 supplement "Item 7"; README `## Retirement note`). D-GOV-43 supersedes D-GOV-20 items 2, 3 and 4 for the App MVP Codex path.
- Root `runtime/` (relocated byte-identically to `projects/chirality-runtime/`, PR #727 merge `8209bc54e0d133b19437c93b184cd50ba3d43489`; notice `NOTICE_ROOT_RUNTIME_PROJECT_MIGRATION_2026-09-05.md` `2c70ea97cb49ec40c613c19fd187760f68cbd4889c75669901bad7fb59a0f363`).
- A global or cross-session event feed: none. The route table has one SSE route, `sessionTurnStream` = `/v1/projects/{projectId}/sessions/{sessionId}/turn/stream` (SSE frames `id: <seq>`, `event: <type>`, `data: <json>`); PRD §16.2's "per-session SSE only" remains true.
- A shared token registry across applications: the guide states the `app-host` client ID is local to one instance's token registry and is not a shared account.

**What a PEC client would need** (as the guide states for any second consumer)

1. Its own Runtime instance and private data directory; the guide directs that a new consumer must not use the running App's socket or token file. A PEC-owned instance would see only sessions created through it, not App sessions.
2. A Node host running `node packages/daemon/dist/standalone-bin.js daemon --config <abs>`; there is no non-Node sidecar distribution.
3. Config schema `chirality-app-owned/v1` with fields `socketPath, runtimeDirectory, instructionRoot, productInstructionsPath (optional), clientTokenFile, codex.{executablePath, userCodexHome, effectiveHome, expectedVersion}`; absolute normalized paths; socket path ≤ 103 UTF-8 bytes; pinned Codex (`expectedVersion` example `0.154.0`).
4. Await the single JSON ready line (`ready, role, socketPath, clientTokenFile`); HTTP/1.1 + SSE over the Unix socket; host token for host-client routes; per-project registration via `/v3/hosted-bootstrap/projects/register` returning `projectId`, `manifestHash` and a separate project token.
5. Default session creation requires a signed-in Codex account and model catalog (guide, step 3).
6. The App's own instance lives under `<userData>/runtime` with a per-launch token (`runtime-service-host.ts` line 66 comment; README "How the App owns the child"); that data is operational and non-authoritative (D-GOV-20 item 5, not superseded).

Runtime README and the A2 supplement both state PEC's integration opportunity
is preserved and its compatibility unverified and not an MVP prerequisite.

---

## 4. Loop registry facts

| Loop | LOOP_INIT | Receipt arrangement | Current graph location | TM register | Decision register | adapter.yaml |
|---|---|---|---|---|---|---|
| chirality-app-dev | `projects/chirality-app-dev/loop/LOOP_INIT.md` | central `AgentRuns/<RunID>/RECEIPT.md` (0 instances); ledger historical at 264 | `execution/_Coordination/WorkGraphs/<u>/WORK_GRAPH.md` | yes | `execution/_Coordination/_DECISIONS/_REGISTER.md` | yes |
| chirality-piping | `projects/chirality-piping/loop/LOOP_INIT.md` | central (1 instance); ledger historical at 162 | same | yes | same pattern | yes |
| pec | `projects/pec/loop/LOOP_INIT.md` | ledger `loop/LOOP_RECEIPTS.md` (D-PEC-80 v2) | own: `AgentRuns/<RunID>/` JSON/RUN.md | yes | same pattern | **no** |
| root | `execution/_Coordination/LOOP_INIT.md` (+ `CURRENT_WORKPLAN.md`) | `execution/_Coordination/LOOP_RECEIPTS.md` | `AgentRuns/<RunID>/WORK_GRAPH.json` | yes | `docs/governance_harness/_DECISIONS/_REGISTER.md` | yes (`execution/_harness/`) |
| chirality-runtime | `projects/chirality-runtime/loop/LOOP_INIT.md` (created 2026-09-05) | `loop/LOOP_RECEIPTS.md` (manual) | none declared | no | none (adapter → `MIGRATION_APPLICATION.md`) | yes |
| bridge | `_DomainEngines/bridge/LOOP_INIT.md` | `LOOP_RECEIPTS.md` (last 2026-08-02) | none | no | `_DomainEngines/_DECISIONS/_REGISTER.md` | no |

Comparison:
- `projects/pec/v2/config/loops.json` (`4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e`) registers one loop (`pec`, `projects/pec/loop/LOOP_INIT.md`); schema (`1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b`) allows only `loop_id` + `loop_init_path`. This matches the P1 design (DEL-01-06 SOW CLM-005, `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8`).
- PRD §7.1/§12/§16.3 (`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`) name five loops (root, app-dev, piping, pec, bridge). HEAD has six LOOP_INIT-bearing loops; `chirality-runtime` is the sixth. Bridge has had no receipt since 2026-08-02.
- For App/Piping, `loop_init_path` alone no longer leads to the graph or receipt: the evergreen LOOP_INIT names only path *patterns*; current undertakings must be enumerated from `WorkGraphs/*/` and `AgentRuns/*/RECEIPT.md`.

---

## 5. Fixture candidates (content-minimal fields only; no scope proposed)

### 5.1 App — `APP-REPLAY-BOUNDARY-2026-09-23`

- Graph folder `projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/` (folder name ≠ stable run ID). Graph `WORK_GRAPH.md` `6dbb884aed7ebf573abf476d54b404a3c6f8620208327dcae2453fef5757081f`.
- Nodes/states: W1, V1, P1, C1, M1 COMPLETE; F1 ACTIVE (on disk). PRs: #866 (merge `2ea7725230c5c370a5b008138d4486ed427b3bd2`), #868 (merge `10b672caed0a0e013ac72508ac72f6b3ce274286`, an ancestor of HEAD). Commits cited: `d82568bc1` (source candidate), `57e3cf680df807e28962d074e1f65cfa99088ac0`, closeout basis `2ea772523`. Graph history: 7 commits `3867a632f`…`d0f523ddb` (2026-09-23).
- Deliverable: app DEL-05-04. No `AgentRuns/<RunID>/` record exists; run evidence is colocated in the graph folder (run predates #877).
- Evidence files (19): `RUN_EVIDENCE.md` `8427cd337c5be32148355748ca0cab5a2063f8dd06d6d0b5ff5995c5b96f2d44` (headings `## Execution and review`, `## Checks on source candidate`, `## Supplied instruction and method basis`, `## Bounded closeout basis`); `REGISTERED_CHECKS.json` (`chirality-software-check-evidence/v1`, status FAIL, 7 results) `fe6c06b670265e59ac327b37393b39fc26454489b5f19040f58550515e723b6d`; `RECORD_CHECKS.json` (PASS, 3) `13ec9533a1b86e1757b37a56f4bb14a03afab5dabf584405d95b0c9b72f44606`; `PATH_REPAIR_CHECKS.json` (PASS, 3) `6c37ec5e48dddb7b5474da84c24f0a15a47d063b4a2199f62ced07bd8b9d609c`; `FINAL_RECORD_CHECKS.json` (PASS, 3) `243525d677ef726dd43c9cd911551365e5270a40b8234556c4bb8e7c22525ead`; `PREMERGE_CHECK_CANONICAL_TMP.json` (PASS, 1) `63d78202070887002202b4170004d38310a1b317469e78404aa4755e85dc2de1`; `SECTION8_SUMMARY.json` (pass, testCount 8) `a89b386d75740d88ab4e7b7daf1907813e1f0172f254dc0e3636a348ef4e348b`; `SECTION9_SUMMARY.json` (pass, 16) `e599171e0cd5d7fe8ace9ffdd2969eacd3674ba6a7456118edcb24b486cdd382`; `SECTION9_MANIFEST.json` (schemaVersion 1, 16 checks) `6a01eb393e93948a66a19fb5a172c38efd80cbd594f4aad827f67502e410b1b8`; `INPUTS.sha256` `4530d1f230ffc017fc3665d50d0ebf28428c102e2cb1b0d7c6b1e7b26ed4513d`; plus six one-line `.txt` checks and two Vitest logs (hashes in manifest; `SECTION9_VITEST.stderr.log` is empty, `e3b0c442…`). The FAIL status is a recorded field; its explanation lives in the graph/run evidence and is not interpreted here.
- MEMORY: `DEL-05-04 …/MEMORY.md` `bbf3ed50c94eda9f2b7cf796ebac170ce64b783e5f7359902e33955a0577b144` — `## Runs` with 1 bullet entry linking graph, `RUN_EVIDENCE.md`, #866, #868; legacy `## Decisions And Evidence` retained.

### 5.2 Piping — `PIPING_LINTER_SCOPE_20260923`

- Graph `WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md` `50933010aef9920d1a615006775ea8997080e5388532ef7d3e9ac8bad92a9a9d` (folder = run ID). Nodes: W1, V1, P1, C1, R1, M1 COMPLETE; F1 ACTIVE (on disk). PRs #867 (merge `8645c269e0b1ba5298ff53ee1ead6f83adb264a3`), #876 (merge `0b276a7fa5dcad7d8f3375ae4f0015a5368e791e`, ancestor of HEAD); graph also cites #872, #873, #874 and commits `a7759882228501e793913c6ca36e87cf2c05f37f`, `896abb37cdd41c554abbd2022bae2fc35d358399`, `23a33eb1d…`.
- Evidence: `evidence/SWEEP_a77598822285.json` (`schema_version` 3, `overall_status` fail, `git.commit_hash` `a7759882…`, branch `codex/piping-loop-trial`) `75621c34f411fa6257b250eb6fd6a8c199587e075af2a19a6efdc1bc35d0d0df`; `evidence/SWEEP_20260923T170102Z_896abb37cdd4.log.gz` `bca122814971809b3695fabe7d4112861108df1b6d9ffb4ca2d75f2130885f22` (later sweep, recorded by commit `b0e9fbe0f`).
- Receipt: `AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md` `eef5434b0ea17d757d4f8a8892d383df4edaab53a571c075af2f3d498c46dfa8` (56 lines; fields as §1.3 S3b; Examined-Through `8645c269e…`; pointers #867, #876; Parent-Receipt none; records the historical ledger as unchanged at Receipt-162).
- MEMORY (3, `## Runs` bullet entries linking the receipt, #867, #876): DEL-08-05 `ec984ac7b59f6be791112b8eae16b2717f58db70fca240c5ec6f5dc4a8ae8bca`; DEL-08-01 `5d4b20e3946abdc86217ad455b22a58ce21229fc20ebe3145513898577f41d2e`; DEL-10-04 `8526eff38ab8b288f0ceb2a0fd2056f82f6ef1b9e676489ff0f066e2db80fa89`.

### 5.3 Piping — `PIP-DEC025-BASELINE-2026-09-23`

- Graph `WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md` `74f068846dd56d97414244635fb6b99c642ffc33ddde5c1f3cf128d30d621428` (folder ≠ run ID). Nodes: W1, W2, V1, P1, C1, M1 COMPLETE; F1 ACTIVE (on disk). PRs #872 (merge `db5bb38730f4f59e6c3f3152bea38af2f0c4bb1d`), #873 (merge `c56ae4a284a747bc6eae7c177011151868064063`, ancestor of HEAD); graph also cites #867 and commits `10b672cae`, `600d963ec`, `8a8a24767`, `d53ed95e2`. Extra heading `## Supplied basis`.
- Run record: `AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md` `f2c8dab41d6af54a916baeebede81e058d8aacf58672d8092b06e4dff421ab4a` (single `#` heading; **no `RECEIPT.md`** — run merged before #877). `checks/` holds five gzip logs: `sweep-host-pass` `3fc0693647d3175ded025423cf15dd61b199a75008d9c07ba1e155cca88e11ff`, `sweep-sandbox-bind-failure` `c6825928455947b6c1a8b4a56ab47db356cb158feb3a84e8cdca4b3360f56fe2`, `vitest-focused-pass` `93394844f7bd33400ffb205184b002ad818fd92b2d2464c34ef7937e614bd16c`, `vitest-full-failure` `0e9ad790b82dc78ebe9a2cf1f7a20e8a0255885101cb037202338cce15e72d04`, `vitest-full-pass` `761359ccacf7e542447aad901215fe4e0a0b5cee258d1708f536925bd922aab4` (pass/fail is in the file name only).
- MEMORY (4, dated `## 2026-09-23 — PIP-DEC025-BASELINE-2026-09-23` headings, not `## Runs` rows): DEL-10-04 (above), DEL-00-08 `ead9e894f9896f6ae879587d0272ff3fe8c74a08f26b7cea2afbfe545c4c48f8`, DEL-12-01 `b8911097102482d528683c35e1de6305b9c15630fda20fa82e7d476d02614100`, DEL-17-06 `af2c9a24338c43b09f60ebd66fe9e4eafe718107760058d7acabb4cd3d0881e6`.

### 5.4 Content-minimal fields a PEC record could carry

Per graph: repo path, blob SHA-256, examined commit, stable run ID string (from
the "Stable run identity" bullet), folder name, node IDs, per-node state token,
count of nodes by state, PR numbers and 40-hex SHAs appearing in cells,
deliverable IDs. Per receipt: path, hash, the eight field names present,
Examined-Through SHA, PR numbers. Per evidence JSON: path, hash, `schema`/
`schema_version`, `status`/`overall_status`, result count. Per MEMORY: path,
hash, run IDs referenced, entry form (`## Runs` bullet / table / dated heading).
Join to Git: merge commit of each cited PR and its ancestry to the examined SHA.

---

## 6. Drift findings (PEC-basis locator vs observed truth; no dispositions)

| ID | PEC-basis locator | Observed current truth (§ ref) | Severity |
|---|---|---|---|
| DR-01 | PRD PEC-RCN-002; §7.1 DependencyEdge; SOW-015; DEL-02-05 SOW REQ/CLM-016 (`192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e`) | App/Piping current graphs are Markdown `WorkGraphs/<u>/WORK_GRAPH.md` (§1.4); App/Piping `WORK_GRAPH.json` last written 2026-09-22 and now historical. No JSON graph shape applies to their current work. | BLOCKING-FOR-PARSER |
| DR-02 | PRD PEC-RCN-002; §7.1 Receipt; SOW-013; DEL-02-03 SOW (`c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872`) | App/Piping receipts are now per-undertaking `AgentRuns/<RunID>/RECEIPT.md` with a new, unvalidated bold-label grammar (n = 1); their ledgers are frozen by instruction at Receipt-264 / Receipt-162 (§1.3). | BLOCKING-FOR-PARSER |
| DR-03 | PRD §7.1 Receipt row and §16.8; SOW-082 / OI-008; DEL-02-03 CLM-017, CON-001 | Three ledgers (App D-APP-57, Piping D-44, PEC D-PEC-80) carry `receipt-contract-v2` markers and shared validation; Root, Runtime and Bridge carry none, with three different heading grammars. A sixth ledger (Runtime) exists. CLM-017's `_DomainEngines/pec/` ledger path no longer exists (PEC loop moved to `projects/pec/loop/`, PR #721 merge `49f9e148cbc5cc21b33368e071e33451ed1d1f33`). | STALE-PREMISE |
| DR-04 | Graph completion state (implied by PEC-ORI-001, PEC-GAT-001) — not yet in any PEC row | All three trial graphs record F1 `ACTIVE` while their final PRs (#868, #873, #876) are merged ancestors of HEAD. The method forbids a write-back commit. The graph file alone therefore misstates completion; completion requires a Git/PR join. Two of three graph folders differ from their stable run ID (§5). | BLOCKING-FOR-PARSER |
| DR-05 | PRD §7.1 Workplan/Step/Gate; SOW-016; DEL-02-06 SOW CLM-015 (`c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8`) | App/Piping LOOP_INIT are evergreen with no step, gate or undertaking state; workplans retired or historical; CLM-015's selection rules ("bytewise-sorted `WORKPLAN_`", "newest `WORKPLAN_*.md`") and `_DomainEngines/pec/` paths no longer describe any live loop. Piping keeps a 2026-09-19 standing-pointer workplan whose text predates #878 (§1.6). | STALE-PREMISE |
| DR-06 | PRD §7.1 Package/Deliverable "remaining items"; PEC-ORI-001; DEL-02-01 SOW CLM-013 (`5d286ec97f4c262be9e106537e3b7527e9756b6dd5bf0f1beb8259e1ca114440`) | `## Remaining` absent from all App (0/54) and Piping (0/106) `_STATUS.md` (retirement PRs #861–#864, #870, #871); PEC 57/64; Root 46/53 but all RETIRED; Runtime 0/7 while its LOOP_INIT still names Remaining. App/Piping work now lives in Scope of Work, decisions, graphs and TM (§1.1). | STALE-PREMISE |
| DR-07 | PRD PEC-RCN-002 / SOW-017 / DEL-02-07 SOW CLM-011 (`d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559`) | Four live adapters (not two); App/Piping adapters predate the new method and declare no graph, receipt, MEMORY or TM location; only Root's adapter has `loop_init`/`receipts`; PEC has none; drift baselines stale (§1.7). The feed manifest cannot locate the new surfaces. | STALE-PREMISE |
| DR-08 | PRD §8, PEC-PRS-001 ("daemon-owned (D-GOV-20)"), PEC-PRS-004, PEC-STR-003 ("runtime-daemon SSE subscriber"); SOW-026, SOW-029, SOW-035; DEL-07-02, DEL-07-05 (no SOW yet) | Per-user daemon retired (D-GOV-43 + A2, PR #767); Runtime is a private per-application service; a second consumer must run its own instance and must not attach to the App's socket or tokens; the only SSE is the per-session turn stream; no global feed (§3). Presence of App sessions is not observable through any documented Runtime interface. | STALE-PREMISE |
| DR-09 | PRD PEC-STR-002 and §16.9 ("root `runtime/`", "`runtime/packages/contracts`"); §16.6 ("daemon's project-scoped token registry"); SOW-074, SOW-083 | Root `runtime/` does not exist; the contracts package is `projects/chirality-runtime/packages/contracts/` (PR #727); token registries are per instance and private to the owning application (§3). | STALE-PREMISE |
| DR-10 | PRD §7.1 Loop, §12 P2 "All five loops", §16.3 "today five"; DEL-01-06 SOW CLM-004/005 | Six LOOP_INIT-bearing loops (adds `chirality-runtime`, 2026-09-05); Bridge dormant since 2026-08-02; for App/Piping, `loop_init_path` no longer leads to graph or receipt instances (§4). `loops.json` registering only `pec` is consistent with P1. | STALE-PREMISE |
| DR-11 | SOW-014; §7.1 RunRecord; DEL-02-04 SOW CLM-014 (`bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87`) | `STATUS.json`/`RUNTIME_SUMMARY.json` persist (954/104 tracked; PEC now 13, not zero) but App/Piping's newest dates from 2026-09-17; new-method runs record evidence as `RECEIPT.md`, `EVIDENCE.md`, gzip logs or `chirality-software-check-evidence/v1` JSON, possibly colocated in the graph folder (§1.4, §5). The 2026-07-25 census counts in DEL-02-04/-05/-06/-07 CLMs are stale. | STALE-PREMISE |
| DR-12 | PEC ingest list omits MEMORY (PRD PEC-RCN-002); PEC LOOP_INIT mentions MEMORY "when present" | MEMORY is now the per-deliverable run index pointing at central receipts (amendment 2026-09-22). Observed form diverges from the template: 0 `## Runs` tables; 4 bullet `## Runs` sections; DEC-025 used dated headings (§1.8). | INFORMATIONAL |
| DR-13 | Assessment table row "one `AgentRuns/<RunID>/RECEIPT.md` per undertaking" (`ASSESSMENT_2026-09-23_APP_PIPING_PEC_UNISON.md`, `0eed76e529a0640d20115413f7125710e8ebb07e9c9c0a4887b1fc70867b1974`); D-PEC-86 §2 rec. 2 fixtures | Of the three 2026-09-23 trials only the Piping linter run has `RECEIPT.md`; the DEC-025 run has `EVIDENCE.md`, and the App run has no AgentRuns record (evidence colocated in the WorkGraphs folder). The assessment's statement that each Piping trial ended with `RECEIPT.md` holds for one of two. | INFORMATIONAL |
| DR-14 | DEL-02-02 decision register/packet parser | Header grammars: App/Piping/PEC 6 columns; Root 4 (`HumanRuling`); Bridge 5; Runtime has no decision register and its adapter points `decision_register` at a production-SHA table; Root amendments are un-numbered records outside the register (§1.2). | INFORMATIONAL |
| DR-15 | No PEC ingest row for Task Management | Four registers with one shared 25-column `1.0` schema plus closed archives; the Piping live register holds 1 CLOSED row (§1.9). | INFORMATIONAL |
| DR-16 | Name-based discovery implicit in SOW-013..017 | Over-selection: `LOOP_INIT.md` 11 tracked / 6 live; `WORK_GRAPH.md` 53 / 3 canonical; `adapter.yaml` 6 / 4 live. The Root canonical-path classifier (`surface_roles.py`) exists as a reference selection rule (§1.4). | INFORMATIONAL |
| DR-17 | PRD §12 generality test "against a structurally different loop" | Root `LOOP_INIT.md` still lists App/Piping `loop/LOOP_RECEIPTS.md` as handoff sources (line 15), though those ledgers are historical; Root's own instructions were not updated by #877. | INFORMATIONAL |
| DR-18 | SCA-005 identifier (D-PEC-86) as a cross-loop key | `SCA-005` also names Root scope changes (`execution/_ScopeChange/SCA-005_2026-09-05_*`, `…_2026-09-06_*`; Root `_STATUS.md` heading `## SCA-005 retirement record`) and an App/Piping `_ScopeChange/SCA-005_2026-07-04_0000`. A cross-loop reader must qualify IDs by loop. | INFORMATIONAL |

---

## 7. Open questions for the manager

1. **Completion join (DR-04).** Should SCA-005 treat an undertaking's completion as
   graph state plus a Git merge join for the cited final PR? If so, is extracting PR
   numbers and state tokens from graph table cells within PEC-K-10 (identifiers from
   prose cells, never the prose)? DEL-02-05 CLM-014 already draws that line for CSV
   prose columns.
2. **Fixture eligibility (DR-13).** The three trials show three evidence arrangements
   (colocated in the graph folder; `AgentRuns/<id>/EVIDENCE.md`; `AgentRuns/<id>/RECEIPT.md`).
   Are all three first external fixtures, or only the post-#877 receipt shape?
3. **Presence topology (DR-08).** Under A2, no documented interface exposes App
   sessions to another consumer. Is SCA-005 to rescope PKG-06/07 (e.g. PEC-owned
   instance only, Git/worktree presence only, hooks only), or to frame a cross-loop
   request to Root/App/Runtime for an observation contract? The latter is outside
   PEC's fences.
4. **Loop set (DR-10).** Should the P2 loop set add `chirality-runtime` and keep
   `bridge`, given bridge has been quiet since 2026-08-02? This is the PRD §16.3 question.
5. **MEMORY shape (DR-12).** Should PEC parse MEMORY to the template's `## Runs` table,
   to the observed bullet form, or both? The template and observed divergence belongs
   to Root/App/Piping; does the manager want it raised with them?
6. **Adapter manifest (DR-07).** Should SCA-005 keep `_harness/adapter.yaml` as the
   feed manifest (App/Piping would then need new keys, a foreign-loop change), or move
   feed-location knowledge into PEC's own registry (`loops.json`, schema v1 → v2)?
7. **Root/Bridge/Runtime receipt grammars (DR-03).** The §16.8 per-loop ruling is now
   partly moot: three ledgers carry v2. Should SCA-005 carry OI-008 as re-framed or
   as closed for those three?
8. **Assessment correction (DR-13).** Should the assessment's Piping-trials sentence be
   corrected by an append note, given that assessment files are dated records that are
   not edited?

## 8. Survey limits

- Only the surfaces named in the brief were examined. Root `execution/**` MEMORY
  (315 files) and Root graph JSON shapes were counted but not characterized.
- Counts are name- and heading-based censuses; decision-row counts are
  approximate (rows matching `| D-…` style ID cells).
- No command was run against any Runtime socket; §3 comes from documents and source.
- `NOTICE_TRIAGE_2026-09-23.md` and the DEL-01-03 REM evidence folders present in
  the working tree are concurrent in-run outputs of other nodes; they were not read
  or relied on.
