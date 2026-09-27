# SCA-APP-011 Brief — Retire the Workbench and Pipeline Forms and the Deliverable HTTP Routes

**Status:** `CHECKPOINT_GROUP_1_ACCEPTED` — the owner accepted checkpoint group 1 on revision 2 on 2026-09-27 ("I accept SCA-APP-011 checkpoint group 1"); see `../checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`. Group 2 is in preparation. Nothing is applied.
**Date:** `2026-09-27` (folder time `0155` is UTC)
**Requested by:** Ryan Tufts (repository owner `sgttomas`), in the Claude Code conversation of 2026-09-27
**Prepared by:** WORKING_ITEMS, bounded Claude Code subagent, working in an isolated worktree
**Workflow:** `scope-change` (bundled, `workflows/scope-change/`), three grouped checkpoints
**Decomposition variant:** `SOFTWARE`
**Context root:** `projects/chirality-app-dev/execution`
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Allow renumbering:** `false`
**Basis commit:** `e548d4cfada4d2105de6231516dc6e5fc4bd4689` (`origin/main`, merge of PR #984)
**Stage:** checkpoint-group-1 preparation only (change intake, validation and impact). This package writes no decomposition, register, PRD, SPEC, PLAN, Scope of Work, `_CONTEXT.md`, `_STATUS.md`, dependency register, pointer, decision snapshot, `DECISION.md`, `SCA-APP-011_GROUP-1_AUTHORIZED.md` or `_LATEST.md` byte, and no code.
**Precedent:** SCA-APP-010 (IDs, folder naming, `PARSED_ACTIONS`-style intake); SCA-APP-009 and D-GOV-43/D-APP-127 (DEL-09-07 retired in place). SCA-APP-010 predates the current three-checkpoint layout; this run follows the current contract (`Intake_Actions.csv`, `checkpoint_snapshots/`, amendment-qualified `SCA-APP-011_GROUP-{N}_AUTHORIZED.md` pointers), the layout used by Piping SCA-011 and PEC SCA-005/006.

## Owner request (verbatim)

Given on 2026-09-27 in the Claude Code conversation.

1. "We don't need to carry the Workbench or Pipeline forms any longer. They are obsolete."
2. On the App's HTTP routes for dependencies, status and status transition, whose only caller was those forms, the owner selected the option **"Remove the routes (Recommended)"**, described as: "Delete the three routes and their client fetch functions. Keep the library and the MCP tools. Update DEL-07-04, DEL-07-05 and DEL-09-03 scope and the App SPEC to name MCP as the interface."
3. On how to change the App's accepted scope, the owner selected the option **"Scope-change amendment (Recommended)"**, described as: "I prepare SCA-APP-011: retire DEL-02-02, MODIFY DEL-07-04/07-05/08-03/09-03, and revise PRD FR-010 to FR-012 and the decomposition note. You accept each of its three checkpoints, then the code removal merges. This is the governed path for retiring a deliverable."

These are the owner's direction and route selection. They are not the group-1 acceptance, which is a separate act on this package.

## Owner's stated selections (verbatim; not a checkpoint acceptance)

Given on 2026-09-27 through the AskUserQuestion tool in the Claude Code conversation, relayed by the coordinating session. They answer the choices of the first candidate package (`5843c0b8c9d283ba7c6683ddb2a342d7288f6142`). They are recorded here for the eventual group-1 decision snapshot. They are not the group-1 acceptance, which is still to come.

| Choice | Question (as asked) | Answer (verbatim) | Set |
|---|---|---|---|
| A | "How should DEL-02-02 be treated?" | "Rescope it (Recommended)" | DQ-R |
| B | "Should the amendment also delete the old loop-first shell?" | "Exclude it (Recommended)" | L excluded |
| D | "What should happen to PRD FR-011/FR-012, Journey 7.5 and success metric 7 (the Pipeline controls)?" | "Restate them (Recommended)" | restate |
| S | "The Pipeline form was the only UI caller of POST /api/harness/scaffold ... What should happen to it?" | "Remove the route too" | S-c |

Choice C was informational and was not asked. Choice E was not asked; the package keeps its "no change" recommendation for confirmation together with S-c. The first package said S-c needed a separate SOW-024/DEL-07-02 assessment. That assessment is now in `Impact_Assessment.md` §17, with its rows in `Intake_Actions.csv` rows 33–40.

## Parsed intent

| Intent | Source | Parsed as |
|---|---|---|
| Delete the Workbench and Pipeline forms and their tests | Direction 1 | Supersede SCA-APP-010's "code, routes, and tests retained" and D-APP-74's separate-retirement gate for these two forms |
| Delete `GET /api/working-root/deliverable/status`, `POST …/status/transition`, `GET/PUT …/dependencies` and the client fetch functions `fetchDeliverableStatus`, `transitionDeliverableStatus` (client copy) and `fetchDeliverableDependencies` | Direction 2 | MODIFY DEL-07-04, DEL-07-05 and DEL-09-03 and the App SPEC so the library and MCP tools are the named interface |
| Keep `deliverable-contracts.ts`, `lib/lifecycle`, `lib/dependencies` and the MCP tools (`status_transition`, `deps_read`, `deps_write`) | Direction 2 | Not touched |
| Change accepted scope through SCA-APP-011, then merge the code removal | Direction 3 | This amendment; the code change waits for group-3 acceptance |
| "Retire DEL-02-02" | Direction 3 option text | Offered as set DQ-X; see the premise correction below. The owner's stated answer to choice A is DQ-R |
| Remove `POST /api/harness/scaffold` too | Stated answer to choice S | Set S-c: MODIFY DEL-07-02 and DEL-03-03 and the PRD, SPEC, PLAN and decomposition route clauses; the scaffold library stays |

## Premise correction the owner must see

The option text in direction 3 treats DEL-02-02 as the Workbench and Pipeline deliverable. It is not, at the basis commit. Its folder name (`DEL-02-02_Workbench_and_Pipeline_Selection_UX`) is historical. SCA-APP-010 renamed and rescoped it to **"Right-Panel Coordination, Workflows, and Proposal UX"** (decomposition L313). It now carries the live right-panel **Who is working** view, the **Workflows** view and its forms, the transcript **proposal card**, and role entry (SOW-006, SOW-081, SOW-082; OBJ-001, OBJ-007). This is implemented code under `frontend/src/components/woven-dialogue/` (`agents-projection.tsx`, `workflows-view.tsx`, `coordination-panel.tsx` and related files). Workbench and Pipeline appear in its current contract only as a retained-code clause (obligation 1) and as dated legacy clauses (REQ-001 to REQ-011, CLM-014).

Retiring DEL-02-02 as a whole would therefore also retire that live scope unless the same amendment re-homes it. The package offers two mutually exclusive treatments:

- **DQ-R (recommended):** MODIFY DEL-02-02. Delete the Workbench/Pipeline clauses and keep its ID, name and right-panel scope.
- **DQ-X (the option text as selected):** REMOVE DEL-02-02 and re-home its right-panel scope, either to a new successor deliverable DEL-02-06 (X-a) or to DEL-02-01 (X-b).

The owner chooses at checkpoint group 1.

## Accepted inputs (read-only at this stage)

| Input | SHA-256 at basis | Role |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6` | Decomposition truth |
| `execution/_Decomposition/contract_invariant_coverage_register.csv` | `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944` | Companion register |
| `execution/_ScopeChange/_LATEST.md` | `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3` | Active pointer: SCA-APP-010, `CLOSED_WITH_OBSERVATIONS` for derivative audit/navigation |
| `docs/PRD.md` | `17ca3f3c2b868771a0cbcafeb0928c5416cd8bc88d79639838cefe1462e46054` | Product requirements (App) |
| `docs/SPEC.md` | `4c8c9da13736943b8b525a212bac9a6279e58bc5f293d3266bd140b8aae108c2` | Physical and API contracts (App) |
| `docs/PLAN.md` | `5e9cb5e553a815cba6e3d5bf765c66290bc9e25c15c2e44a0a33bea7ed4d04dc` | Roadmap (App) |
| `docs/CONTRACT.md` | `57411f8df49e6316d8d3bc9674d698b1c8478e639aad331115d4f67bcca97363` | Invariants (App); no change proposed |
| `docs/TYPES.md` / `docs/DIRECTIVE.md` | `334bd496…087835` / `50b816d5…f26099` | Vocabulary / intent; no change proposed |
| `projects/chirality-app-dev/AGENTS.md` | `41995dfe123041e1d0235a73e532fddb913f2c2124a9e8ec43857a87d7e5822c` | App loop instructions |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` | `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25` | App loop procedure |
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | Root doctrine |
| `workflows/scope-change/WORKFLOW.md` | `b5fd144603c70e977a59988cb7dfe94dd710cac28db97a19f35c437399efbca9` | Selected method |
| `workflows/scope-change/resources/contract.md` | `3e097df0fc0fe5f062d4e2e9ded86a1b84b1c7b4e692ef3510fa239ab1963e9a` | Selected method contract |
| `workflows/scope-change/resources/method.md` | `a3bb270b320dae36c728cad352c189c4e29fea177cdb8a1468f46e8d777b7108` | Selected method detail |
| SCA-APP-010 `Brief.md` | `9dd89369139ad8b849f5ab52da495323ee541e0e687b1156a3e33d6289c47e3a` | Predecessor intake; exclusion "Deletion of Workbench, Pipeline, or Work-projection code, routes, or tests" |
| SCA-APP-010 `Amendment_Actions.csv` | `8b579266d3a4f7b73c093467691f2f9d7fe140bf8a0cb6f5d7c6c1ac2ef0a109` | Predecessor accepted register (A015 DEL-02-02) |
| SCA-APP-010 `Supersession_Map.csv` | `2045684e8d2d1aff5a46663016f07c16f0c60462c8c8d729ea3c3c1a64f8dbb6` | Cumulative map; D-006 and D-015 bind "code retained" |
| `_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | `1e59194a4f651346c9a7204ace0084fe8ac2115200881799485a9e70443e5ec3` | L97-99 routes/browser APIs retained "until separately retired"; L107 old-UI retirement needs separate owner acceptance |
| `_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md` | `7ced5e05342de3425673990e5ab3bb37a202cd24198ec6427111ef68c31e64f8` | Q3: `/workbench` and `/pipeline` URLs stay reachable and unlisted |
| `plans/shell-redesign_2026-09-04/01_DECISIONS.md` | `8cc5bc8cb2eb0688ca3db69ed24e00bee9c460aefa1d7165cb1a129688a04ed1` | SR-06 "Workbench and Pipeline are retired; the code stays" |
| Root `D-GOV-49` / `D-GOV-51` | `d132efe8…d7efad` / `2d27b3c1…fd797` | DAG authority and currency; `ScopeChanging` column |
| Code-removal candidate `dcd37f9ae9d22bfedc86b921f6e2ac70b90e1419` | branch `worktree-agent-a0de269a96f5dd4af`, parent `947075c9a` | Evidence of the intended code change; not merged, not authority |

Full SHA-256 values for the abbreviated rows: `docs/TYPES.md` `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835`; `docs/DIRECTIVE.md` `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099`; D-GOV-49 `d132efe8a0dfe43a1f589ca52b35588d53254174c1ffad649b2e66d2234a9c7d`; D-GOV-51 `2d27b3c1619a9c6ac8041ec9d69b40c30c1491e37874511f5ddf2f84071fd797`.

Semantic section binding (by heading text, decomposition at basis): Change Register = `12. Decision Log / Change Log` (L613, Change Log L643); Unit Ledger = `9. Scope Ledger` (L403); Objectives = `6. Objectives` (L263); Primary Partitions = `7. Packages` (L280); Secondary Entities = `8. Deliverables` (L297); Vocabulary Map = `4. Vocabulary Map` (L121); SSOW = `5. SSOW` (L172); Open Issues = `11. Open Issues` (L598); Coverage Basis = `10. Coverage and Telemetry` (L496). Additional sections touched: `3. Intake Summary` Hard Constraints (L96, L102) and `13. Downstream Execution Notes` (L662, L672). All bindings resolved; none by position.

`AMENDMENT_ID`: `SCA-APP-011`, from `tools/query/scan_next_amendment_id.sh projects/chirality-app-dev/execution/_ScopeChange APP` (highest existing `SCA-APP-010`). Tooling note: the helper is a zsh script; invoked explicitly through `bash` it rejects every prefix because bash treats the quoted regex literally. Run through its shebang it returns the correct ID.

## Parsed action envelope

The machine-readable intake is `Intake_Actions.csv` (40 rows, every row `Status = PROPOSED`, `ScopeChanging` filled). It is intake evidence only; the accepted register will be a separate `Amendment_Actions.csv` at checkpoint group 2 and will carry only the sets the owner selects.

| Set | Rows | Meaning |
|---|---|---|
| BASE | 1–19 | Owner-directed changes that apply under either DEL-02-02 treatment: DEL-07-04, DEL-07-05, DEL-09-03, DEL-08-03, DEL-02-03, SOW-001 and SOW-007 notes, decomposition hard constraint and section 13 note, DEC-026, telemetry, PRD, SPEC and PLAN |
| DQ-R | 20 | Recommended: MODIFY DEL-02-02 (keep the right-panel scope, delete the Workbench/Pipeline clauses) |
| DQ-X | 21–27 | Alternative: REMOVE DEL-02-02 and re-home its scope, with sub-choice X-a (ADD DEL-02-06, row 22) or X-b (MODIFY DEL-02-01, row 23) |
| L | 28–32 | Optional legacy loop-first shell removal. **Excluded** (stated selection B) |
| S-c | 33–40 | Remove `POST /api/harness/scaffold` and its client function: MODIFY DEL-07-02 and DEL-03-03; PRD §9.1, Journey 7.3 and route-preservation clauses; SPEC §17.1; PLAN; decomposition hard constraint (stated selection S) |

Counts: BASE 18 MODIFY + 1 ADD; DQ-R 1 MODIFY; DQ-X 1 REMOVE, 1 ADD (X-a) or 1 MODIFY (X-b), 5 MODIFY; L 5 MODIFY; S-c 8 MODIFY. With the stated selections (BASE, DQ-R, S-c) the group-2 register would hold 28 rows: 27 MODIFY and 1 ADD. No RECLASSIFY, MERGE, SPLIT, package change or renumbering.

## Validation

- Every named entity exists at the basis: DEL-02-01, DEL-02-02, DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-02, DEL-08-03, DEL-09-03 (decomposition rows L312, L313, L314, L365, L366, L374, L375, L385; folders present with `_CONTEXT.md`, `_STATUS.md`, `ScopeOfWork.md`), SOW-001, SOW-006, SOW-007, SOW-081, SOW-082, PKG-02, OBJ-001, OBJ-007. None is already retired.
- Proposed new IDs do not collide: `DEC-026` (highest `DEC-025`); `DEL-02-06` (PKG-02 holds DEL-02-01 to DEL-02-05).
- `REMOVE DEL-02-02` (DQ-X only): DEL-02-02 is not a parent partition. PKG-02 keeps four active deliverables, so no parent closes. Its scope items stay IN and are remapped in the same amendment (rows 24–26). The parent-closure rule is satisfied only when X-a or X-b is chosen with it.
- Lifecycle: all eight affected deliverables are `IN_PROGRESS`. No App deliverable is `ISSUED` (53 `IN_PROGRESS`, 1 `OPEN` = retired DEL-09-07). No reopening is authorized or needed. No `CHECKING` hold applies.
- Package discipline: no deliverable crosses a package boundary. DQ-X X-b would breach DEL-02-01's envelope (flagged).
- Contract-level flags: row 7 changes a decomposition hard constraint (browser-facing route stability). Rows 13 and 31 change PRD compatibility clauses that require "separate owner acceptance"; the owner's acceptance of this amendment is recorded as that acceptance.
- Fences: no provider, network, release, issuance, domain-engine or Root-owned semantic change. The MCP tools and the Runtime tool descriptors are untouched.
- Supersession: rows marked `SupersessionBindingPresent = YES` will need `Supersession_Delta.csv` bindings at group 2 against D-APP-74 L97-99 and L107, SCA-APP-010 Supersession_Map D-006 and D-015, and SR-06.

## Pre-change baseline

`Pre_Change_Coverage.json`, built by `Evidence/Group1/build_pre_change_baseline.py` (read-only; reproducible from the repository root). It is a synthesized deterministic baseline from the decomposition plus the registered tools `audit_structure.py`, `analyze_dep_closure.py` and `validate_decomposition_registers.py`. A full `audit-decomp` TASK was not dispatched from this bounded run. The latest full audit (`_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_RECORD_RECON_2026-09-22_2026-09-22_1513/`) was not reused as the baseline because its instruction, workflow and pointer inputs have changed. Its decomposition and companion-register inputs are byte-identical to this basis, so its structural findings (WARNINGS, zero blockers) still describe the decomposition.

| Field | Result |
|---|---|
| Topology | 10 packages / 52 deliverables (DEL-09-07 retired) / 10 objectives / 84 scope items (78 IN, 5 OUT, 1 TBD) |
| Envelopes | S 9, M 41, L 2, XL 0 |
| Forward coverage | 52/52 declared deliverables have folders |
| Reverse coverage | 54 folders; undeclared control folders DEL-00-01 and DEL-00-02 (carried) |
| Unmapped | 0 IN scope items without a deliverable; 0 objectives without a supporting deliverable |
| Structure audit | 54/54 units pass the SOW_V1 production format; carried partition/tool-root issues |
| Dependency closure | 54 nodes, 111 edges, 0 SCCs, no accepted DAG; 2 schema-invalid (the two control folders have no register) |
| Register validator | SCH and DRB clean; XRG skipped (no `Deliverables.csv`/`ScopeLedger.csv` in the App); 592 EVQ-006 (deliverable-relative `EvidenceFile` paths; carried convention) |

**Revision 2 rerun.** The builder now also records the scaffold scope items, DEL-07-02's dependency rows and the frontend references for choice S-c. It was rerun at `5843c0b8c9d283ba7c6683ddb2a342d7288f6142`, whose governed inputs are byte-identical to the original basis `e548d4cf…` (only this SCA folder was added). Its structural results are unchanged: 54 nodes, 111 edges and 0 SCCs; 54/54 SOW_V1; register findings EVQ-006 only.

## Explicit exclusions

- Any change to `deliverable-contracts.ts`, `lib/lifecycle`, `lib/dependencies`, the MCP tools or the Runtime tool descriptors.
- `/api/working-root/deliverable/content` (its caller is the document viewer). `/api/harness/scaffold` is excluded only if the owner does not confirm S-c.
- The App scaffold library `frontend/src/lib/harness/scaffold.ts` (`scaffoldExecutionRoot`, `previewScaffoldExecutionRoot`) and its tests, under every set.
- The Runtime-owned scaffold API (`POST /v1/projects/{id}/scaffold`, `RuntimeClient.scaffold`, `RuntimeService.scaffold`, `ProjectScaffoldPort`). The Runtime loop decides on it after an informational notice.
- `/api/working-root/scope` and `/api/project/deliverables`. The first also loses its only UI caller (the Workbench form); this is recorded as a residual, not proposed.
- The `/`, `/chat`, `/workbench` and `/pipeline` page URLs (D-APP-108 Q3 stands). They remain reachable under every set.
- The Work projection (stays unmounted, unchanged).
- CONTRACT invariant text and the companion register's enforcement-surface wording (no change proposed; see Impact Assessment §5.6).
- The legacy loop-first shell (set L) unless the owner includes it.
- Any lifecycle transition, release, publication, `_LATEST.md` movement, or closure of other open SCA work.

**Owner response (group 1):** Accepted on 2026-09-27: "I accept SCA-APP-011 checkpoint group 1". The accepted selection is BASE + DQ-R + S-c, with D restate, L excluded, E no change, M-a and the scaffold library kept. See `Decision_Log.md` G1-ACCEPT and the group-1 decision snapshot.
