# SCA-005 prep: PEC basis impact inventory

| | |
|---|---|
| Run | `HELP-HUMAN-PEC-20260923-SCA005`, node A2 (TASK, read-only) |
| Brief | `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/A2_IMPACT_INVENTORY.md` |
| Accepted basis | `D-PEC-86` §3 I-1..I-3; checkout `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (= `origin/main` at run time) |
| Companion register | `IMPACT_INVENTORY_PEC_BASIS.csv` (201 rows), SHA-256 `f0bba13aa7fbce3b618e4132a91a634e16d4558ba521393380e2f5894130e3bc` |
| Status | Derivative evidence for the SCA-005 checkpoint-group-1 package. This is not a ruling, a scope change, an Impact Assessment, or an amendment. The cited files govern if they disagree with it. |

Prepared by a TASK instance served as `claude-opus-5-5` (as reported by the
host). The role is instruction-asserted and not mechanically enforced. This run
wrote only this file and the CSV.

## 1. Method and verification

- Every inventory row cites one live claim. Each `ClaimExcerpt` was checked
  by a script against the live bytes of `SurfacePath` after whitespace
  normalization, and the `(Lnnn)` in `Locator` is the line where the excerpt
  starts, computed by the same script. The build failed closed on any excerpt
  it could not find. None failed. Excerpts are at most 200 characters, and a
  trailing `…` marks truncation.
- There are two exceptions to single-file rows: `projects/pec/execution (16
  ScopeOfWork.md front matter)` and `projects/pec/execution (13
  ScopeOfWork.md)`. Each groups one repeated sentence and names its member
  DELs in Notes. The sentence was confirmed present in exactly those 16 and
  13 files.
- Scope read in full: PRD v2.2; SOFTWARE_DECOMP rev 1.4; `Deliverables.csv`;
  the PRD v2.3 postimage (diffed); the TM-PEC-023 decision surface and owner
  rulings; `loops.json` and its schema; `pec.yaml`; `ADRs.md`; `SPEC.md`.
- Scope read by targeted search plus reading the matched context: all 32
  `ScopeOfWork.md`, all 64 `_CONTEXT.md`, all 64 `_REFERENCES.md`, and
  `ScopeLedger.csv`. The heavily touched parser SOWs (DEL-02-03, DEL-02-06,
  DEL-02-07) were read in full. The search terms covered every D1–D9 surface
  name, and a broader search for runtime/daemon/token/SSE/loop-set terms was
  used to confirm the "no touching claim" results.
- Sister-loop facts used to key the drift were spot-checked at this basis
  (§3). A1 (`SURVEY_SISTER_LOOP_FILE_TRUTH.md`) landed during this run. Its
  §6 findings DR-01..DR-18 were cross-read and reconciled into the rows and
  into §3 (see §3 "A1 cross-reference"). A1's hash bindings take precedence
  wherever the two differ. One of my figures changed after the cross-read:
  the Piping `## Remaining` count (see D3).
- `PackageRole` convention: `docs/PRD.md` is labelled `working surface`
  because it is the product definition's live amendment surface. The allowed
  role list has no separate "source corpus" value.
- **Twin rows:** the SSOW §2 tables duplicate `ScopeLedger.csv` identity
  columns by design (DL-15). Both loci are inventoried, and Notes say
  "Twin of …". One semantic change therefore produces two atomic register
  edits.
- **ADD rows** sit at the adjacent existing SSOW row, because that is where
  an append-only insertion would be reviewed. Their `ClaimExcerpt` is that
  anchor, not a claim the ADD changes.

## 2. Totals

### 2.1 By surface

| Surface | Rows | MODIFY | ADD | REMOVE | RECLASSIFY | NOTE-ONLY |
|---|---:|---:|---:|---:|---:|---:|
| ScopeOfWork.md contracts (32 in scope) | 48 | 26 | 0 | 0 | 0 | 22 |
| _CONTEXT.md mirrors | 11 | 11 | 0 | 0 | 0 | 0 |
| `_DomainEngines/profiles/pec.yaml` | 2 | 0 | 0 | 0 | 0 | 2 |
| `projects/pec/docs/PRD.md` | 36 | 28 | 0 | 0 | 0 | 8 |
| `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` | 4 | 1 | 0 | 0 | 0 | 3 |
| `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | 3 | 1 | 0 | 0 | 0 | 2 |
| `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md` | 3 | 0 | 0 | 0 | 0 | 3 |
| `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/DECISION_SURFACE.md` | 9 | 9 | 0 | 0 | 0 | 0 |
| `projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` | 1 | 0 | 0 | 0 | 0 | 1 |
| `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` | 4 | 0 | 0 | 0 | 0 | 4 |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | 16 | 12 | 0 | 0 | 0 | 4 |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | 45 | 27 | 3 | 0 | 6 | 9 |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | 17 | 14 | 0 | 0 | 3 | 0 |
| `projects/pec/v2/config/loops.json` | 1 | 0 | 0 | 0 | 0 | 1 |
| `projects/pec/v2/config/loops.schema.json` | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **201** | **129** | **3** | **0** | **9** | **60** |

### 2.2 By affected work-domain package

A row's package is taken from its path. For register, decomposition and PRD
rows it is taken from the DEL/SOW ID in the locator or excerpt, with the SOW
mapped through `ScopeLedger.csv` (OUT/TBD rows have no package).

| Affected work-domain package | Rows | MODIFY | ADD | REMOVE | RECLASSIFY | NOTE-ONLY |
|---|---:|---:|---:|---:|---:|---:|
| PKG-00 | 17 | 9 | 0 | 0 | 0 | 8 |
| PKG-01 | 14 | 10 | 0 | 0 | 0 | 4 |
| PKG-02 | 46 | 31 | 3 | 0 | 0 | 12 |
| PKG-03 | 5 | 3 | 0 | 0 | 0 | 2 |
| PKG-04 | 7 | 5 | 0 | 0 | 0 | 2 |
| PKG-05 | 3 | 1 | 0 | 0 | 0 | 2 |
| PKG-06 | 9 | 9 | 0 | 0 | 0 | 0 |
| PKG-07 | 14 | 14 | 0 | 0 | 0 | 0 |
| PKG-08 | 8 | 4 | 0 | 0 | 0 | 4 |
| PKG-09 | 3 | 0 | 0 | 0 | 0 | 3 |
| PKG-10 | 4 | 1 | 0 | 0 | 0 | 3 |
| cross-cutting (PRD / decomposition / config) | 58 | 36 | 0 | 0 | 3 | 19 |
| multi-PKG (aggregate SOW rows) | 1 | 0 | 0 | 0 | 0 | 1 |
| none (OUT/TBD) | 12 | 6 | 0 | 0 | 6 | 0 |
| **Total** | **201** | **129** | **3** | **0** | **9** | **60** |

PKG-05 and PKG-09 appear only through register or PRD rows (DEL-05-01
receipt ancestry, and DEL-09-01/-03). PKG-06 and PKG-07 have no Scope of
Work yet, so their drift is carried entirely by the PRD, the decomposition,
the registers, and the `_CONTEXT.md` mirrors.

### 2.3 By drift dimension (a row may carry several)

| Dim | Meaning | Rows (any) | MODIFY | ADD | REMOVE | RECLASSIFY | NOTE-ONLY |
|---|---|---:|---:|---:|---:|---:|---:|
| D1 | WORK_GRAPH/STATUS/RUNTIME_SUMMARY JSON -> WorkGraphs/<undertaking>/WORK_GRAPH.md | 38 | 23 | 1 | 0 | 0 | 14 |
| D2 | per-loop LOOP_RECEIPTS.md / D-APP-57 -> AgentRuns/<RunID>/RECEIPT.md | 57 | 29 | 1 | 0 | 3 | 24 |
| D3 | ## Remaining retired as App/Piping selection surface | 16 | 12 | 0 | 0 | 0 | 4 |
| D4 | workplans retired; evergreen LOOP_INIT (no steps/gates/pointers) | 41 | 25 | 0 | 0 | 0 | 16 |
| D5 | shared daemon / D-GOV-20 -> D-GOV-43 A2 app-owned Runtime per application | 84 | 64 | 0 | 0 | 6 | 14 |
| D6 | MEMORY ## Runs index | 10 | 7 | 1 | 0 | 0 | 2 |
| D7 | _harness/adapter.yaml as feed manifest | 12 | 5 | 0 | 0 | 0 | 7 |
| D8 | loop registry: one registered loop vs "five loops" | 18 | 11 | 0 | 0 | 0 | 7 |
| D9 | other stale premises | 23 | 17 | 0 | 0 | 0 | 6 |
| NONE | no drift (I-3 carry-in / register row) | 6 | 5 | 0 | 0 | 0 | 1 |

### 2.4 By owning workflow

| OwningWorkflow | Rows |
|---|---:|
| PRD amendment | 39 |
| PROJECT_SETUP metadata | 11 |
| WORKING_ITEMS SOW currency | 55 |
| scope-change direct | 93 |
| task-management | 3 |

## 3. Drift evidence at this basis (spot checks; A1 binds)

| Dim | Observed at `d61981ee2` |
|---|---|
| D1 | App: `execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md`. Piping: `WorkGraphs/{PIPING_LINTER_SCOPE_20260923,dec025-clean-base-repair-2026-09-23}/WORK_GRAPH.md`. Both LOOP_INITs (§1) direct new graphs to `WorkGraphs/<undertaking>/WORK_GRAPH.md`. Repo-wide: 199 `WORK_GRAPH.json` (historical) and 53 `WORK_GRAPH.md`. |
| D2 | App and Piping ledgers are frozen (A1 DR-02). App (D-APP-57), Piping (D-44) and **PEC (D-PEC-80)** ledgers carry `receipt-contract-v2` markers; `projects/pec/loop/LOOP_RECEIPTS.md` L1865 reads `receipt-contract-v2 frozen-through=Receipt-166`. PRD §7.1's "pec/bridge ledgers are prose-structured" is therefore stale for pec too (A1 DR-03). Both LOOP_INITs §5: "write one receipt for the undertaking at `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`". Neither LOOP_INIT names `LOOP_RECEIPTS.md`. Only **one** `AgentRuns/*/RECEIPT.md` exists in this checkout (`chirality-piping/.../PIPING_LINTER_SCOPE_20260923/RECEIPT.md`). The App trial and the Piping DEC-025 trial have a WORK_GRAPH.md here but no RECEIPT.md. See §8 M-3. |
| D3 | `## Remaining` is absent from all canonical App (0/54) and Piping (0/106) `_STATUS.md` (A1 DR-06). My first count of Piping 10/116 included SCA-011 candidate copies under `_ScopeChange/`; excluding them, it agrees. PEC keeps `## Remaining` (57/64) as its selection surface (`projects/pec/loop/LOOP_INIT.md` §4). |
| D4 | App and Piping LOOP_INITs are 146 lines each and reference no workplan. PEC's own workplans are retired under D-PEC-80 D and live at `projects/pec/plans/workplans/`. Root still has `execution/_Coordination/CURRENT_WORKPLAN.md`. |
| D5 | `docs/DIRECTIVE.md` (A2): "the Chirality App starts, owns, and stops one simplified Runtime service as a child process… The per-user daemon, its LaunchAgent, and local-model residency are retired". D-GOV-43 supersedes D-GOV-20 items 2–4 on the App path. `APPLICATION_CONSUMER_GUIDE.md`: "Use a separate Runtime instance and private data directory for each owning application… Do not point a new consumer at the running Chirality App's socket or token file." The D-GOV-43 A2 supplement says: "PEC's integration opportunity is preserved, its compatibility unverified and not an MVP prerequisite." Root `runtime/` does not exist; contracts are at `projects/chirality-runtime/packages/contracts`. |
| D6 | LOOP_INIT §5: "add a terse entry to each affected deliverable's `MEMORY.md`… MEMORY is a local run index". Files with a `## Runs` heading: App 1/56, Piping 3/108. A1 DR-12 finds these are bullet sections: 0 template tables, and DEC-025 used dated headings. The PEC basis mentions MEMORY nowhere (zero hits in PRD, decomposition and SOWs). |
| D7 | `_harness/adapter.yaml` exists for root (`execution/_harness/adapter.yaml`, `root-harness-adapter/v1`), App, Piping and Runtime (`practitioner-harness-adapter/v1`). None exists for PEC. App/Piping/Runtime declare `plan, coordination, decision_register, dag_pointer, status_glob, exclude_globs, states, parser_dialect, drift baselines, validation_commands, guard_*`. Only the root adapter declares `loop_init` and `receipts`. **None declares WorkGraphs, RECEIPT.md or MEMORY runs.** Every path App/Piping declare resolves. The adapter remains the practitioner-harness config and is not a feed manifest for the new surfaces. |
| D8 | `projects/pec/v2/config/loops.json` registers exactly one loop (`pec`, `projects/pec/loop/LOOP_INIT.md`). The PRD says "five loops" (§2, §12 P2, §16.3). Six governed loops have a `LOOP_INIT.md` + `LOOP_RECEIPTS.md`: root, app-dev, piping, pec, bridge, and **runtime** (`projects/chirality-runtime/loop/`). |
| D9 | `_DomainEngines/pec/` was removed by `ca49b846d` ("Migrate PEC loop and evidence to canonical project homes", 2026-09-05). Stale citations are in PRD §13, SOFTWARE_DECOMP R4, and DEL-02-03/DEL-02-06 SOWs. DEL-03-04 quotes the pre-v2.1 P1 row ("piping or root"). DEL-01-06 and DEL-02-03 quote "all five registered loops", which is no longer in `Deliverables.csv`. 16 SOWs pin `@3623b958b`, which does not resolve in this clone. 13 SOWs claim `_REFERENCES.md` "still names revision 1.1", but all 64 now name revision 1.4. The `pec.yaml` header says "Candidate only… awaiting owner ruling" while its body is `ADOPTED`. |

A1 cross-reference: DR-01→D1 rows. DR-02/DR-03→D2 rows. DR-05→D4 rows. DR-06→D3
rows. DR-07→D7 rows. DR-08/DR-09→D5 rows. DR-10→D8 rows. DR-11→INV rows on
DEL-02-04 (CON-003 now MODIFY: PEC holds 13 `STATUS.json`). DR-12→D6. DR-13→M-3.
DR-14→DEL-02-02 note. DR-04 (graph completion needs a Git/PR join) and DR-15
(Task Management registers not ingested) have no existing PEC claim to key a
row to, so they appear as candidates C-13 and C-14. DR-16 (name-based discovery
over-selects) is folded into C-2. DR-17 and DR-18 concern Root surfaces and ID
qualification and are outside this inventory.

## 4. Scope of Work coverage (all 32)

23 of 32 SOWs carry at least one touching row, and 9 carry no
touching claim. "D9 aggregate" marks membership in INV rows for the
`@3623b958b` basis pin and the stale `_REFERENCES.md` claim. Those are
currency items, not sister-loop drift.

| DEL | Lifecycle | Touching rows (InvID) | MODIFY | NOTE-ONLY | Disposition | D9 aggregate rows |
|---|---|---|---:|---:|---|---|
| DEL-00-01 | CHECKING | INV-130 | 1 | 0 | Touched: SOW currency action needed | — |
| DEL-00-03 | CHECKING | INV-131, INV-132 | 0 | 2 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-01-01 | INITIALIZED | INV-133, INV-134, INV-135, INV-136 | 4 | 0 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-01-03 | IN_PROGRESS | INV-137 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | basis pin @3623b958b |
| DEL-01-04 | INITIALIZED | — | 0 | 0 | No touching claim. Logging scope names no feed, loop set, runtime or receipt surface. | basis pin @3623b958b |
| DEL-01-05 | IN_PROGRESS | INV-138 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-01-06 | INITIALIZED | INV-139, INV-140 | 2 | 0 | Touched: SOW currency action needed | — |
| DEL-02-01 | INITIALIZED | INV-141, INV-142 | 0 | 2 | Touched: quotation/observation only (NOTE-ONLY) | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-02 | INITIALIZED | INV-143 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-03 | INITIALIZED | INV-144, INV-145, INV-146, INV-147, INV-148 | 5 | 0 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-04 | INITIALIZED | INV-149, INV-150, INV-151 | 3 | 0 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-05 | INITIALIZED | INV-152, INV-153, INV-154 | 2 | 1 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-06 | INITIALIZED | INV-155, INV-156, INV-157, INV-158 | 3 | 1 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-02-07 | INITIALIZED | INV-159, INV-160 | 1 | 1 | Touched: SOW currency action needed | — |
| DEL-03-01 | INITIALIZED | INV-161 | 1 | 0 | Touched: SOW currency action needed | — |
| DEL-03-02 | INITIALIZED | — | 0 | 0 | No touching claim. Its only related text is an upstream quotation ("every loop the registry names"), unaffected. | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-03-03 | INITIALIZED | — | 0 | 0 | No touching claim of its own; L118 quotes DEL-01-01's entity list as upstream context only (covered by INV rows on DEL-01-01). | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-03-04 | INITIALIZED | INV-162, INV-163, INV-164 | 1 | 2 | Touched: SOW currency action needed | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-03-06 | INITIALIZED | — | 0 | 0 | No touching claim. Performance bounds are corpus-relative; no feed or topology premise. | — |
| DEL-04-01 | INITIALIZED | INV-165, INV-166 | 2 | 0 | Touched: SOW currency action needed | — |
| DEL-04-02 | INITIALIZED | — | 0 | 0 | No touching claim. SSE mentions refer to PEC's own DEL-08-05 subscription, not the retired daemon feed. | — |
| DEL-04-03 | INITIALIZED | INV-167 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-04-05 | INITIALIZED | INV-168 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-08-01 | INITIALIZED | INV-169, INV-170 | 1 | 1 | Touched: SOW currency action needed | — |
| DEL-08-02 | CHECKING | — | 0 | 0 | No touching claim. Sibling-boundary text only. | basis pin @3623b958b |
| DEL-08-03 | INITIALIZED | INV-171 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-08-04 | INITIALIZED | INV-172 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-10-01 | CHECKING | INV-173 | 0 | 1 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-10-02 | INITIALIZED | — | 0 | 0 | No touching claim. "representative governed workflows" is unenumerated; the new loop method does not change the kill-test contract. | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-10-03 | INITIALIZED | — | 0 | 0 | No touching claim. TBD-005's SSE mention is PEC-side. | basis pin @3623b958b; stale _REFERENCES claim |
| DEL-10-10 | INITIALIZED | INV-174, INV-175 | 0 | 2 | Touched: quotation/observation only (NOTE-ONLY) | — |
| DEL-10-11 | INITIALIZED | — | 0 | 0 | No touching claim. | — |

## 5. Candidate new scope items and deliverable adjustments

Every item below is a **CANDIDATE**. None has any status, and none is
selected, ruled, or implied by this inventory. IDs are illustrative only.
Real IDs are append-only and assigned by SCA-005.

| # | Candidate | Drift | Shape options (for the manager, not decided) | Touches |
|---|---|---|---|---|
| C-1 | CANDIDATE: Markdown work-graph parser for `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (nodes, dependencies, states; content-minimal) | D1 | New SOW + new DEL-02-xx, or MODIFY SOW-015/DEL-02-05 to add the `.md` form | INV-079; SOW-015/DEL-02-05 rows; PRD §7.1 DependencyEdge, PEC-RCN-002 |
| C-2 | CANDIDATE: WorkGraphs discovery. Enumerate undertakings per loop without a manifest entry, since adapter.yaml declares none and `loops.schema.json` has only `loop_init_path`. Name-based discovery over-selects: 53 `WORK_GRAPH.md` exist, of which 3 are canonical (A1 DR-16) | D1;D7;D8 | Part of C-1, a PEC-side convention, or a `loops.json` schema v2 field (owner-gated config; A1 open question 6) | INV-199, SOW-017 rows |
| C-3 | CANDIDATE: central-receipt parser for `AgentRuns/<RunID>/RECEIPT.md`, emitting Receipt and/or RunRecord | D2 | New SOW + DEL, or MODIFY SOW-013/DEL-02-03 into "ledger + central receipt" (re-envelope; OI-008 reclassified) | INV-080; SOW-013, SOW-082, DEL-02-03 rows |
| C-4 | CANDIDATE: MEMORY `## Runs` index parser (deliverable-local run-to-receipt join) | D6 | New SOW + DEL, or fold into C-3 or SOW-014/DEL-02-04 | INV-081; PRD RunRecord row |
| C-5 | CANDIDATE: Workplan/Step/Gate entity and DEL-02-06 reclassification. Retire the workplan feed and re-source "gate states" from decision registers and graph state, or narrow DEL-02-06 to LOOP_INIT identity/entrypoint discovery | D4 | MODIFY or RECLASSIFY SOW-001 (entity list), SOW-016, DEL-01-01 (14 types), DEL-02-06, PEC-ORI-001 "gate states" | PRD §7.1, SOW-016 rows |
| C-6 | CANDIDATE: per-application Runtime client instance. Replace the "shared-runtime client seam" (SOW-087/DEL-07-05) and the "daemon SSE subscriber" (SOW-035/DEL-07-02) with a PEC-owned Runtime instance, its own data directory and token registry, and the Runtime client over its own socket, never the App's | D5 | MODIFY SOW-087/SOW-035 (and DEL names), or REMOVE SOW-035 if no feed exists; needs a `pec.yaml` profile amendment before invocation | SOW-035/087, DEL-07-02/-05, PKG-07 charter, TM-PEC-023 rows 4 and 7 |
| C-7 | CANDIDATE: presence-tier reconsideration. Under A2, sessions are app-instance-scoped and no cross-application daemon exists. Decide the presence source (each application's Runtime instance reports via hooks CLI, checkout-contained graph/receipt parentage, or narrowed P3/P4 scope) | D5 | MODIFY PEC-PRS-001/-004, SOW-026/029, DEL-06-01/-04; possibly RECLASSIFY SOW-076 (global feed) | PRD §7.2, §9.4 |
| C-8 | CANDIDATE: reclassify the three daemon- or ledger-premised TBDs: SOW-076/OI-002 (daemon global feed), SOW-080/OI-006 (daemon token registry), SOW-082/OI-008 (D-APP-57 adoption) | D2;D5 | RECLASSIFY each to a restated question or close as moot. Re-assess the DEL-02-03 L envelope and the DEL-08-01 MEDIUM risk | 9 RECLASSIFY rows |
| C-9 | CANDIDATE: `## Remaining` per-loop availability. "remaining items" becomes an optional per-loop field. Absence is a stated limitation for App/Piping and not a defect | D3 | MODIFY PRD §7.1 Package/Deliverable, SOW-001, DEL-02-01 notes | INV-008 and related |
| C-10 | CANDIDATE: external self-ingestion fixtures. Use the 2026-09-23 App and Piping trial runs as the first "structurally different loop" (assessment recommendation 2) | D1;D2 | Owner names the loop (DEL-10-10 TBD-005); fixtures pinned by hash (A1). Note M-3 (missing RECEIPT.md for 2 of 3 trials) | DEL-10-10 rows, PRD §12 closing |
| C-11 | CANDIDATE: loop-set wording. Replace "five loops" with registry-relative wording and acknowledge the runtime loop | D8 | MODIFY PRD §2, §12 P2, §7.1 Loop, the vocabulary row and DEL-01-06 CLM-004/005. The D-PEC-79 postimage already fixes §16.3 | D8 rows |
| C-13 | CANDIDATE: undertaking completion join. Graph files record F1 `ACTIVE` after their final PRs merged, and the method forbids write-back, so completion needs a Git/PR join (A1 DR-04). Extracting PR numbers and state tokens from table cells has to be checked against PEC-K-10 | D1 | New SOW, or a clause in C-1 plus PEC-ORI-001/PEC-GAT-001 wording | PRD §9.1, §9.3 |
| C-14 | CANDIDATE: Task Management register feed. Four registers share one 25-column `1.0` schema and now carry App/Piping selectable work (A1 DR-15) | D3 | New SOW, or CandidateBrief re-sourcing (INV-011) | PRD §7.1 CandidateBrief |
| C-12 | CANDIDATE: event-contract home restatement. "Shared runtime contracts" now lives in `projects/chirality-runtime/packages/contracts` under the Runtime loop, and root `runtime/` is gone | D5;D9 | MODIFY SOW-034/074/083, PEC-STR-002, §16.9 | D5/D9 rows |

## 6. PRD v2.2 → v2.3 postimage: exact delta

Compared `projects/pec/docs/PRD.md` (527 lines, SHA-256
`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`) with
`PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md`
(543 lines, SHA-256
`92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0`) using
`diff`. The live file is byte-identical to the preimage pinned in
`OWNER_RULING_2026-08-09.md`, `HANDOFF_STATE.md`, and the D-PEC-79 carrier.
The postimage hash matches the ruling. The carrier hashes to `bc3a4bd5…`
and the ruling to `d1995cef…`, both as recorded. No `D-PEC-79` file or
register row exists in live `_DECISIONS/` (withheld, as ruled). The
difference is exactly six hunks and +16 lines:

| # | Live v2.2 lines | Postimage lines | Change |
|---|---|---|---|
| 1 | 5–7 (header table) | 5–7 | Version `2.2`→`2.3`. Date `2026-07-27`→`2026-08-09`. Status "Adopted 2026-07-27 by owner ruling (`D-PEC-68`)" becomes "Adopted 2026-08-09 by owner ruling (`D-PEC-79`)", and the lineage list gains "§16.3 loop-registry disposition concordance adopted as v2.3 by `D-PEC-79`" |
| 2 | 15–16 (epistemic status) | 15–18 | Inserts ", and amended to v2.3 on 2026-08-09 (`D-PEC-79`) to reconcile §16.3 to D-PEC-78 O-A and accepted SCA-004 decomposition truth" before "Adoption makes a PRD…" |
| 3 | after 28 | 31–37 (new) | Adds a blockquote "v2.3 provenance labels". It labels the §16 heading and closing sentence `CLARIFIED` and the §16.3 disposition `TRANSCRIBED` from D-PEC-78 O-A / SCA-004 rev 1.4, and states that it "creates no new product meaning and changes no decomposition, source, configuration, consumer, lifecycle, or release authority" |
| 4 | 493 | 502 | `## 16. Open product decisions (owner)` → `## 16. Product decisions (owner)` |
| 5 | 499 | 508–515 | Item 3 "Home and shape of the loop registry (which loops PEC serves; today five)." is replaced by "**Resolved 2026-08-02 by `D-PEC-78` O-A.**…". The replacement says the strict-version-1 JSON/schema paths plus the core-owned typed `LoopRegistry` port are the home; PEC owns only its configured service set; row changes are owner-gated; listing creates no duty, and no governed act depends on PEC or the registry |
| 6 | 515 | 531 | "None of these blocks P0–P2." → "None of the remaining open decisions blocks P0–P2." |

Consequence for SCA-005 (observation, not a decision): §§1–15 and §16 items
1, 2 and 4–9 are identical in the postimage. Every PRD drift row in the CSV
(INV-001..INV-036) therefore applies to v2.2 and the v2.3 postimage alike,
except INV-033 (§16.3), which the postimage already resolves. Under I-2,
SCA-005's PRD candidate must either (a) apply the D-PEC-79 bytes first and
amend on top, or (b) carry hunks 1–6 forward verbatim inside a successor
candidate. Choosing between them is checkpoint-2 material.

## 7. TM-PEC-023: the nine rows as prepared

Source: `TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/DECISION_SURFACE.md`
(status `PREPARED / AWAITING_DEDICATED_OWNER_SESSION`; every checkbox
unselected). Its pinned basis hashes still equal live bytes: `ScopeLedger.csv`
`2103afa2…` and `Deliverables.csv` `49f90448…`. `REGISTER.csv` row TM-PEC-023
is `OPEN`. Per D-PEC-86 I-3, each row enters SCA-005 intake as a candidate
MODIFY of `ObjectiveIDs`/`SupportsObjectives`, and the owner selects row by
row at checkpoint 2. Every row also offers an **OWNER REPLACEMENT** free-text
option. Calibrations are the prep package's own "non-binding" notes.

| Row | DEL / SOW | Prepared options (AuthorityStatus) | Non-binding calibration in prep | Sister-loop drift interplay |
|---|---|---|---|---|
| 1 | DEL-00-02 / SOW-034 (PEC-STR-002) | MAP-A `OBJ-001;OBJ-003` (INDIRECT_SUPERSESSION_CANDIDATE) · NONMAP `SHARED_INFRASTRUCTURE_INDIRECT_ONLY` | MAP-A only as indirect supersession; NONMAP source-faithful if indirect attribution is rejected | D5: the statement says "consumable by daemon". If SOW-034 is MODIFIED, the mapping applies to the new statement |
| 2 | DEL-03-05 / SOW-038 (PEC-STR-004) | MAP-A `OBJ-001` (INDIRECT) · MAP-B `OBJ-001;OBJ-003` (INDIRECT) · NONMAP `INVARIANT_GUARANTEE_NO_DIRECT_OBJECTIVE` | NONMAP strongest source-faithful (PEC-K-07 is an invariant) | None |
| 3 | DEL-05-01 / SOW-022 + SOW-023 (PEC-GAT-001/-002) | MAP-A `OBJ-004` (**DIRECT_ACCEPTED_LINK**, the package's only direct link) · NONMAP `ADVISORY_GATE_CAPABILITY_NO_DIRECT_OUTCOME` | MAP-A is the only direct accepted link | D2 (NOTE): the "receipt ancestry" precondition presumes ledger chains |
| 4 | DEL-07-02 / SOW-035 (PEC-STR-003) | MAP-A `OBJ-001;OBJ-003` (INDIRECT) · MAP-B `OBJ-003` (INDIRECT) · NONMAP `SHARED_BRIDGE_INFRASTRUCTURE_INDIRECT_ONLY` | Both mappings indirect; MAP-B narrower | **D5: target (daemon SSE feed) retired.** A MODIFY or REMOVE of SOW-035 may moot or re-scope this row |
| 5 | DEL-07-03 / SOW-036 (PEC-STR-003) | MAP-A `OBJ-003` (INDIRECT) · MAP-B `OBJ-001;OBJ-003` (INDIRECT) · NONMAP `SHARED_BRIDGE_INFRASTRUCTURE_INDIRECT_ONLY` | MAP-A tighter indirect candidate | None observed (hooks CLI is not daemon-premised in the text) |
| 6 | DEL-07-04 / SOW-037 (PEC-STR-003) | MAP-A `OBJ-003` (INDIRECT) · MAP-B `OBJ-001;OBJ-003` (INDIRECT) · NONMAP `OPTIONAL_ENRICHER_NO_DIRECT_OBJECTIVE` | NONMAP source-faithful if optional enrichers are not mapped | None |
| 7 | DEL-07-05 / SOW-087 (§13, D-PEC-56) | MAP-A `OBJ-003` (NEW_OWNER_ATTRIBUTION) · MAP-B `OBJ-001;OBJ-003` (NEW_OWNER_ATTRIBUTION) · NONMAP `SHARED_RUNTIME_SEAM_INDIRECT_ONLY` | NONMAP source-faithful; both maps are new attributions | **D5: the "shared runtime" premise is retired** (candidate C-6). Authority A10 cites D-PEC-56 |
| 8 | DEL-08-05 / SOW-044 (PEC-API-005) | MAP-A `OBJ-003` (INDIRECT) · MAP-B `OBJ-001;OBJ-003;OBJ-004` (NEW_OWNER_ATTRIBUTION) · NONMAP `TRANSPORT_CAPABILITY_INDIRECT_ONLY` | MAP-A indirect; MAP-B new attribution | None (PEC-side SSE) |
| 9 | DEL-10-08 / SOW-063 (§12 P4) | MAP-A `OBJ-001;OBJ-003` (NEW_OWNER_ATTRIBUTION; supersedes DL-14) · NONMAP `INVARIANT_EVIDENCE_OBJECTIVE_FREE` | NONMAP is the recommended source-faithful option | None |

The session-wide rulings the prep says remain open are:

1. the NONMAP recording mechanic (M1 keyed §3 table, M2 ledger Notes plus
   index, or M3 snapshot plus §3 only; annotating the objective field is
   rejected);
2. §3 table form;
3. the SCA ID;
4. the Gate 3 postimage and Gate 4 plan;
5. the Gate 5 act.

The owner ruling of 2026-08-03 (1c) requires TM-PEC-023 to close
`RESOLVED_BY_DECISION` citing the amendment, and COV-062..070 to retire
against it.

## 8. For the manager to resolve

- **M-1: Topology-first ordering for TM-PEC-023 rows 1, 4 and 7.** Mapping
  objectives onto SOW-034/035/087 before deciding whether those items are
  modified, renamed or removed (C-6) risks mapping a retired premise.
  Recommend sequencing the D5 decisions ahead of those three rows within
  checkpoint 2.
- **M-2: D-PEC-79 path.** Choose apply-then-amend or supersede-with-carry
  (§6). All other PRD drift is untouched by the postimage.
- **M-3: Fixture completeness.** Only one of the three 2026-09-23 trials
  (Piping linter scope) has an `AgentRuns/<RunID>/RECEIPT.md`. The DEC-025
  run has `AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md`, and the
  App run keeps its evidence in the WorkGraphs folder. This is independently
  confirmed by A1 DR-13, and the assessment now carries an appended
  correction. Decide fixture eligibility (A1 open question 2) before relying
  on C-10.
- **M-4: Rename vs retain stable names and paths** for DEL-02-03, DEL-02-04,
  DEL-02-06 and DEL-07-02, whose names embed retired surfaces. SCA-003 and
  SCA-004 preserved names and paths. A rename is a PROJECT_SETUP path act
  beyond metadata.
- **M-5: New feeds vs extended feeds** (C-1, C-3, C-4). DL-4's
  one-feed-per-item convention favours new SOW IDs, but envelopes and PKG-02
  counts change either way.
- **M-6: DEL-01-06 overlap.** Owner ruling 2 of 2026-08-03 already
  authorizes an RF-002 revision of DEL-01-06's SOW (Gate 5 HOLD at
  INITIALIZED). The D8/D9 rows INV-139/140 should be folded into that
  revision rather than creating a second currency act.
- **M-7: Foreign surfaces.** `pec.yaml` (header staleness; profile amendment
  required before any runtime client), the sister loops' `adapter.yaml`
  (declares none of the new surfaces), and `projects/pec/AGENTS.md` §Shared
  Runtime Boundary are outside D-PEC-86 §4 write targets. Route them through
  notices or Task Management, not SCA-005 edits.
- **M-8: SOW currency list.** Independent of drift, 16 SOW basis pins
  (`@3623b958b`) do not resolve here, and 13 SOWs carry a now-false
  `_REFERENCES.md` "revision 1.1" claim. Both belong in the SCA-005 Scope of
  Work currency list as currency items, not scope actions.

## 9. Observed outside the inventory scope (no rows)

- `projects/pec/AGENTS.md` §Shared Runtime Boundary still states that
  "`D-GOV-20` and `D-T0-23` place PEC agent execution on the root-owned
  shared runtime. The runtime daemon remains the **sole owner**…". This is
  D5 drift in an instruction surface, which is an instruction change needing
  its own scope (root AGENTS.md).
- `docs/STATUS.md` currency is handled by node E1.

## 10. Supplied-basis cross-check

| Supplied-basis key | Supplied SHA-256 (prefix) | Live SHA-256 (prefix) | Match |
|---|---|---|---|
| projects/pec/docs/PRD.md (v2.2 live) | `6833553c33aadca0` | `6833553c33aadca0` | yes |
| projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md (rev 1.4) | `7cca5cdbb1ba4bd8` | `7cca5cdbb1ba4bd8` | yes |
| projects/pec/execution/_Decomposition/ScopeLedger.csv | `2103afa279bc7df8` | `2103afa279bc7df8` | yes |
| projects/pec/execution/_Decomposition/Deliverables.csv | `49f904488a7402e2` | `49f904488a7402e2` | yes |
| PRD_V2_3_CANDIDATE_POSTIMAGE.md (D-PEC-79 adopted, not applied) | `92627ee1d384dd8e` | `92627ee1d384dd8e` | yes |
| TM-PEC-023 DECISION_SURFACE.md | `3a61a24db9a0c501` | `3a61a24db9a0c501` | yes |

## 11. SHA-256 of every inventoried file

### 11.1 Primary surfaces

| SHA-256 | Path |
|---|---|
| `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | `projects/pec/docs/PRD.md` |
| `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` | `projects/pec/execution/_Decomposition/ScopeLedger.csv` |
| `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` | `projects/pec/execution/_Decomposition/Deliverables.csv` |
| `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` | `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` |
| `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` |
| `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` |
| `bc3a4bd59d4542e3d686c4663cc5b5b4fc59f4f3abc6bc4a40ea65063716b5d2` | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/D-PEC-79_prd_v2_3_section16_3_concordance.md` |
| `d8c24c5b03f2d001060c526e17d0d4f14c49985a4c891cf1094d8658bd305ee5` | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/HANDOFF_STATE.md` |
| `d1995cef187116913e675f2cf55e3bb75a0e469ec21ea03c8762927faf037c97` | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/OWNER_RULING_2026-08-09.md` |
| `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0` | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md` |
| `3a61a24db9a0c5019302588831e5245e5c9436ef03b9e4595ea70615941071ef` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/DECISION_SURFACE.md` |
| `62e7984ed42178ee19bfaa58de01c8d8543e86f30630c68ee009766a07f30162` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/HANDOFF_STATE.md` |
| `d827c7442b32d957fa71a538b208827d33c817284b480f6c96c8964859b6d33f` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/MANIFEST.md` |
| `579230cf7ed303f7722b88e0ac9abff2b768c3a5e5a7d475092c3407a0327f64` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/OWNER_RULINGS_2026-08-03.md` |
| `6f4e870e49d43b402e413b7d74bb53ffe0744410820da35abe4a12305c54146e` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/SCHEMA_MECHANICS_PROPOSAL.md` |
| `5e5e865aa8c347c90d31379f944de15b184d4af05956a5e93aee2de363f7849a` | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/VALIDATION.md` |
| `d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d` | `projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` |
| `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` | `projects/pec/v2/config/loops.json` |
| `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | `projects/pec/v2/config/loops.schema.json` |
| `6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f` | `_DomainEngines/profiles/pec.yaml` |

### 11.2 Scope of Work contracts (32)

| SHA-256 | Path |
|---|---|
| `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` |
| `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/ScopeOfWork.md` |
| `43f1f57a13bb96b3235bbbb460342bd03518c503f23cb8b0560914f27a2f0170` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` |
| `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md` |
| `4dd777f8f30cf5483d3c33bd002359e7266f8e411e74ba8655e2afc5aa367e62` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/ScopeOfWork.md` |
| `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md` |
| `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` |
| `5d286ec97f4c262be9e106537e3b7527e9756b6dd5bf0f1beb8259e1ca114440` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/ScopeOfWork.md` |
| `5f20b1c48f4f383a07240e04bdf524e8b2443af37cb745c549f939cd6bb8db6e` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/ScopeOfWork.md` |
| `c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md` |
| `bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md` |
| `192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md` |
| `c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md` |
| `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` |
| `564955235aeab60f169e6377dd9d5bb5fbe2a88a8cc66094e17f6f83987792d2` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` |
| `d1335c01c54686427d6a04658a43ce9e5c4abe2e446e0acf4d1e87df3a7785b5` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md` |
| `5ce8ab72425ab417c90c3e64a152912a7e39b243f3905e65477dbfd91a40eaa7` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md` |
| `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md` |
| `90de9c2d93d8350805410753a21f19c5cf141e48c3e94ffc8096621b3a42c97e` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` |
| `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` |
| `a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` |
| `6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` |
| `933c012cf16bb161b0ac1acdbf3caeaac408fa441b6e175b8fc2e7d8b265a579` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md` |
| `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` |
| `eb171e9dac40b313be8ea8ff75ad395171b599a41d2a1dbf290a9c5b44290c20` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md` |
| `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` |
| `6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` |
| `40d47fb636ca72e52213929b2337dbbc3a02f0f7c073758c996f5d651e1a5a7e` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/ScopeOfWork.md` |
| `99730e4e85ce4920d676d9fd62d26c193d5fd714ea0592c15462f37a62011a82` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md` |
| `cbcabbde6882baf5330e90cdd6e1cf4a9d9aa1da076643a27f84ff4cb7696ff8` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` |
| `640f23711f93ec7e987742ed5ed998bea04c681f14bff06bdf2e35a669fcbd5e` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` |
| `9b90f33ba03a07ab829e7743176df48e6b88ca96d0de18d98c16332a7624cdf9` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/ScopeOfWork.md` |

### 11.3 `_CONTEXT.md` (all 64 scanned; 11 carry rows)

| SHA-256 | Path |
|---|---|
| `70e70f495817dbab5c25c67c4b4bd5aac756816d3df9103e57ad991c286817c5` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md` |
| `01cddc447f614885b23e6a7fe978b5cbf51803868acf52048e319389d2e699e2` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_CONTEXT.md` |
| `59fec8afea9544061dcd9fb0a6510c5492b2480e7d71b35624cf64ced9b81a8c` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md` |
| `d53e451a0e90a7ab2929ca3342dee740fbb6f26cc4c68b52efe663cd2febdf98` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md` |
| `4d49f17b8a6aadb9961780ac3fc425df3e4fccd10f9321bb2c84427b32214337` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_CONTEXT.md` |
| `ed453eaa112e1c8af9b1c201d0e4c3b5bb00b11e776c7658cbd333d430a6e058` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_CONTEXT.md` |
| `b479ce57949d78b9db78a54c8b77eae418d8e345843d303c69fc54087e694afa` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_CONTEXT.md` |
| `4bf394696c386f6a5f792a8f9967abc03e1d1339dc6715de09647f296ad25da1` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_CONTEXT.md` |
| `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md` |
| `6829fef13bd2b65dbb79ced9225cb91b806016d5d363a1135e194901311d7746` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_CONTEXT.md` |
| `8cfabfe6bffb9325246e4d94be47c2da2b65a22eebae8e01dde7292f48aec382` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_CONTEXT.md` |
| `a787e6379cd1d099ce1237c603c1696f7e3d30b1fde1bb5f3759c6c848d0be46` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md` |
| `e5460afb03737fcc61594fb17a769d8b5d5de1faa40f4769c855d282b407f48d` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md` |
| `c4eee6211db66a8d5305741a999ee5b054f40b79d83ecefd2e29964a3c604156` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md` |
| `ff59149c1f01bf47976f412d585481e421c1453134ac6a8e9f6c3d97c3632da0` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md` |
| `5f2647cf1e65f29e9ce539707891e7b3259d1f9f7e3da8702eb803826b5a7f81` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md` |
| `fcf60b19d2be414dbf6d1572b035ceb5404aa86ac8240709c5e6405762af3346` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_CONTEXT.md` |
| `0d9ccb791028d4d59c345612fd27e7e755882899161be15076875bc7a78b0271` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_CONTEXT.md` |
| `215f30967b8ea683eaba6b0e43d1f4be44838b76ab927481a79e15ec03c94a4e` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_CONTEXT.md` |
| `006c508a849aa2b5316166029aa5f737494e781ca9b2d12594dbca9ed53e5c5c` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_CONTEXT.md` |
| `912abd1d8b18a166d324deec0f8f2780243d3d5dda95d684c1fcca04eef95ef9` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_CONTEXT.md` |
| `bfe3b987d85cd13dde55cc0db22caddf68c8525180b026a2bb3977cbeac5855a` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_CONTEXT.md` |
| `b6816f9a2878d057d28b182c16ae64d6ec3385e6d44cc71e8062ff76128986ea` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_CONTEXT.md` |
| `242107d811521e1ae2b6645b6ce12a198e8b2ca91c4d53298a1c5f5e804807f6` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_CONTEXT.md` |
| `0b56862a83014d469cc00ddd663dc2e60cb93ac4249eeed169480b88e7ec9b21` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md` |
| `3f068736b91bfdb60681e9019f5c936edd2d74b29e0f918989f0122015b1e700` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_CONTEXT.md` |
| `20710c09a9524586b9efd61bcd20a768df4ffe37b33862c80a00e069e189bed6` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_CONTEXT.md` |
| `83230f78ef5e98bfaff1ecd0bb326220a8974fcc2d3f1c945458013955410989` | `projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_CONTEXT.md` |
| `ab427727f5e9049f9e2b341b201929b2485d1a97654b51bab7d2391605defaed` | `projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_CONTEXT.md` |
| `8d867899d0facb0e8ecd79538ac3dd9cc5ed3f32ee61c9dd187dc77f6c3e9d5d` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_CONTEXT.md` |
| `7ae79b2138fb458203f7105cd863419769f60308e17072ab4e2b0a13b610ba40` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_CONTEXT.md` |
| `1ed76ac629d33bad7d077b50a70026f90d25fba858df9b93a0084711f7490071` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_CONTEXT.md` |
| `2df7d3d4d569ab828c13dcb8c85c62db89519e807e599a4f895610a9cb393cbf` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_CONTEXT.md` |
| `ad7fe45e8b9b2b2f541ea97607625af108700dc7228077a8ef0701e6d03f9ec1` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_CONTEXT.md` |
| `3db26dc1456daa09654fca7d88186563611db462a5788d46e2e0b84fa4538f95` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_CONTEXT.md` |
| `e20c22ee0d6fb78e54519194a8e1eb1e0ef9594b96fa5854525a0006df13a986` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_CONTEXT.md` |
| `8aadd01be7375624c26989163d4f7e72cb22ad608c1fcea56538fe100fd97e1d` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_CONTEXT.md` |
| `984841782d524e77c912e03fb8ce9a6a0231b69ffe1ca660d7441e71327c894a` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_CONTEXT.md` |
| `805a32c90214b9c3f401e06399d9e205207c629696e432829195975ab03097f9` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_CONTEXT.md` |
| `b32196a0e7bdbbd44de79916f97d63ce68cf75d7f5350fc1f6d5ac823ce90f4b` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md` |
| `3393b45003a6ab0ae3e54e36831f7bb32399be4fa8aa1b15bbdc213ebed4dc15` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md` |
| `375f46713bd275576a8343feb6a1768abbe0c1f5cfd61e888bb60111abe44cc9` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_CONTEXT.md` |
| `d9b84e656c69f09de9f3b0cc55fa87663ad39cb3236200493ca0720a46da1c58` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md` |
| `787d462878730161f667e6c8edb928f2248a8ab460c409566f826ed9c6265a6d` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_CONTEXT.md` |
| `d1bbae9720e13b66b9ab2267657b10910e134564dfcb1c4fc616637817ef8daa` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_CONTEXT.md` |
| `2ed591ad9008ebfa144e9c5b9a7f0a1d5f2ff858002c9b6a49939dbe46b3ccb0` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_CONTEXT.md` |
| `f757ca97a8f822bd74876b03ef3cbb4f5a61846cef0b369487cf730b680d4832` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_CONTEXT.md` |
| `e53497585ebce826bd16244f924a9164f5cb46334e935daae50a55ebed1a9996` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_CONTEXT.md` |
| `1e5957cd85780fa5dbb4b6f6353564a49ec79c4cf436b62726e17bf269d0d01f` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_CONTEXT.md` |
| `6c5455c38b85003e3632e52a961e0aae150eb4e25567bd6378d0c05207085569` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_CONTEXT.md` |
| `a146fc6acb4fe5da4d513312f11c8c2db3c3d2cff77aa4720b484b260a1f86bf` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_CONTEXT.md` |
| `21c858156a5f4636bc3d79765f9c88a5438efa0e90254097e30b77603e9dd54d` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_CONTEXT.md` |
| `b216baa191be3309f98f938b06f2a9df1204b8d02d20088705e70c41561845ba` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_CONTEXT.md` |
| `43a5587fa48498909290540492de137c38ab3c82a96c4caea035ce6831a9edca` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_CONTEXT.md` |
| `244b635d3864c91d768c0dba6874168fb851062fdaa309587af1240ea0a6248d` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_CONTEXT.md` |
| `c57966413a2174ad2d979d31de4fee08e7e9b02a6e53c2e157fb4c19f577ddc4` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_CONTEXT.md` |
| `ccbbfb44c7143aea9067d1d0cf38247aee71dd4cb07fb97249d1fa121bab4d33` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_CONTEXT.md` |
| `1898159dc8cfb1f33e75a4e1330b63f533a5acc4775ffea7a97e192376a4f657` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_CONTEXT.md` |
| `88bdda5d9c590df9969d22bfddeafa441cec74a11e31e2e27e9488d66af50af9` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_CONTEXT.md` |
| `9c320e3795b874819dde7db11e0a4c3550dad32b3488ef1ba70b347ffaa7a51c` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_CONTEXT.md` |
| `0fd365a5b1f86bbc1e5f596ee0ea945275e3693f4c78d68cfcf6a6fed02f55cd` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_CONTEXT.md` |
| `7ad8761a61727297478eaaac5737af6cea9bc0cc7e1f146c70ff4966d52154c7` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_CONTEXT.md` |
| `6bfde0e0f01a12c3d4d48cf067872b2752a41dd334def4bdc339af9e83e0b6aa` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_CONTEXT.md` |
| `c7e16840930fb534e9591364a9cc772aa00d74f8441d196d07323b83495fd222` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_CONTEXT.md` |

### 11.4 `_REFERENCES.md` (all 64 scanned; none carries a drift premise)

| SHA-256 | Path |
|---|---|
| `21560f41e7fb075fb72fcbe419ce0c7136941622134cecfdf125d7ed4b904fd4` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REFERENCES.md` |
| `d4bee4effb1c47744438f691d1821ce7953f4da40aa17eecd200cdc88386fa74` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_REFERENCES.md` |
| `481b34847cbbc9bb15d792e0990b0b8f0b2a5750c82a041d65bb50bff4ff615f` | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REFERENCES.md` |
| `e72764eb33fe0deadb9d7f4e33b43e3a3e10e44949f5cd7aa46fc7c56e6611b2` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_REFERENCES.md` |
| `e323c6a086b2ed7907fc5c80d502197b56c1983cb14e0fd67f24aa33ba319774` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_REFERENCES.md` |
| `8a661ac88c3047e1c6892a6e24544f2714329579c6717f0c05ac840e4f468bcc` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_REFERENCES.md` |
| `53ffa97f12951dd4086fc80ce3e907cf57ca273381b30018b922644f100e3dd9` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_REFERENCES.md` |
| `20c53f9b060f24c5278199c8357c64cc5f1a36fabf218da6d855f2f12a40647a` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_REFERENCES.md` |
| `a4da999cef5d3c94d9ed61f2cddca297481be7ebdde52d13d2f8a9e213a35693` | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REFERENCES.md` |
| `42c74660a51bd92fb8df13d0b1c3109651d2304b35413b25ac5b6b281d7cd882` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_REFERENCES.md` |
| `25ba5e5b64588948a5c5e66e083367fd696e9d36a6fc109fe4b5f5ea51db1c5d` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_REFERENCES.md` |
| `b5e3211557729e3eaeca9d257417a1fccd64374aea66833639bb011b67c771f8` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_REFERENCES.md` |
| `9275945f28d5722112a20e2329c5b6723f13c28cc1431942bbcfb463d9946125` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_REFERENCES.md` |
| `57cdc7bc7e6229c19e144352b8de2f8868c0039d6faaa025caf08b46008e4843` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_REFERENCES.md` |
| `5c3ddbf2269e91165e8a2df5cd1eb3c88aa4a8e219afeda65a12530d2215f82c` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_REFERENCES.md` |
| `228c49f4b1ff8a54f99e58510e8f145535b6ffba69c922aeb88493cfdcabaf25` | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_REFERENCES.md` |
| `682edec873d4771213845ed35ce2afe2b8b6ed218bcc920e63bf08abe79a937f` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_REFERENCES.md` |
| `8a5a1e1824365c365024fb08f0333d2ea0fd0bef80e0b99cc57d068342491ec5` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_REFERENCES.md` |
| `8d12f602e86792c6ebd02db6e540b41e219201adae8bab8a6dd2d79f3abbe9b5` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_REFERENCES.md` |
| `f0ff68a4c268e11f9d9d32d87a377d3b2877832eb9b3ea21d438115aaec177c9` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_REFERENCES.md` |
| `7200cda06600495b7b5321fcfadcdbfbc27762ba7521d3513e4e56a5647e9224` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_REFERENCES.md` |
| `73b4e4cc9116a115201f23a5296edf0e905355d6ac2e2b0da558609ec5c9d4ab` | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_REFERENCES.md` |
| `fb2348289bbd2da6df823a1c9dc001bf62fa460aea8132e413c0266d322d7e0d` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_REFERENCES.md` |
| `55eea82370f608dd7ea75418004af9a77cc1417d08d7b8baaf55db2b22eeebab` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_REFERENCES.md` |
| `d3a41d79d4687fd15052d95186626c4dc6db3f45d1c900d1cbc835b977920058` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_REFERENCES.md` |
| `873889e0812dc9e0f808f75ebe0425b82ebfa6cdb2b04ff63c2388805f213038` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_REFERENCES.md` |
| `bd866c34c6c7d5daffd3a136cdd2541da8f1c2585a8890cca466743a27b3a71a` | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_REFERENCES.md` |
| `fd226572dd115a54fed3bf651d6b58fead77b86777165d7a27331c402c1886a8` | `projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_REFERENCES.md` |
| `6beaa2761fb978ba07a4b6e1259b51bf939dfe6a67bc4a0053e7dc02c55368b8` | `projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_REFERENCES.md` |
| `d052d61c1b38925f298bc659bb796c8a5eb796811558cdefd8139e4361fe01a9` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_REFERENCES.md` |
| `d00ed531a857aa0ca172e3dc3f17cefda433e7073b189610615938d026e44ece` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_REFERENCES.md` |
| `a38bc032d32d811e10db9ec2dfe8359c5b1192e811d16341aa0efd25747ed182` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_REFERENCES.md` |
| `93303124d4e8db243c0b6f95753a0887d22b35e32cb8e8b756bd96d1dc0bd407` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_REFERENCES.md` |
| `68f93f33b49245085d8726226f0f60b5dff2a8e33504505eceb3d971e81dc80f` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_REFERENCES.md` |
| `11bfe2a700df99ae0d963c28b1733e2f636039337944fb34748d3624ee4709d3` | `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_REFERENCES.md` |
| `7db708f869b0579b009238744fbece05b43275c960f3c0ae544da233f6a34860` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_REFERENCES.md` |
| `69d76c3e9eba29d2c160fd68c024ff21fcbcebe7833c726244c2876e993c9c74` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_REFERENCES.md` |
| `896c1f6926360a9ae5db919f8506794ca2e2890d817dbf2c592e99733bb416fe` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_REFERENCES.md` |
| `2289938931aaacc4cd29fdfdb3fc49cbc02b6e7f7f281d10c45f401082713dc4` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_REFERENCES.md` |
| `5d4cdd94f23b89411fcd4b16d4ae6e7f25258390cafb63c0e7ddbf798cbe821f` | `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_REFERENCES.md` |
| `83e25138dc8ebf7e7102c651742c77e1ea9748b9417c9ac89d166f81bdfb39fe` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_REFERENCES.md` |
| `734258088c76a48636751b5f7bdd7e5467e2e939e2158dff7037d1833a8396ca` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_REFERENCES.md` |
| `ae13d4f030682b0d90db4f2a7884cc01a1f47abd2baed9dbb4646cf6346111f8` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_REFERENCES.md` |
| `9948422bcf701bb31d4738c4d2655fa7975178fa87c14264a2f0f23c6d089fb4` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_REFERENCES.md` |
| `66489416f3dfe9c61f7a25865238cf1bf4a54c9e398b53c076e1fcc56af86b1d` | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_REFERENCES.md` |
| `7cc4faf411a85a3cf17a33a0a50f5065aace83ef3eef003298dc721bbe6dac0d` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_REFERENCES.md` |
| `0d34444f7faaa91e4e5aa8b4a16cb05707d491a353c863bb12387fedd9c08487` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_REFERENCES.md` |
| `78ab3bb0f5957b152a05bd712b6f55fe900ebd4f47234bfa1c878daa8a620537` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_REFERENCES.md` |
| `3275cdc25d61bdab3baa276ac917af67a666b7091dfe73078391c41f544c9f55` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_REFERENCES.md` |
| `57c637d457886cda3c23a51b02167484eef670f4bcb7d41dae98547a61721145` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_REFERENCES.md` |
| `7d814916e089a74cfc54c330e4041af2c40b7339b774b10d1062b4a6004f8580` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_REFERENCES.md` |
| `d74fa83df09a07d1a96b7407c2a748b7e9821861e3556a54d0d0eb9ad859d168` | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_REFERENCES.md` |
| `c50bb2b69a39901a60866c2b2bb3d652f570ae10b827f7845b4b3e3fd1542c7c` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_REFERENCES.md` |
| `106baf2082bd0b82e1475f56b15f1bf0d2280a83188f017d7c261b2ad2ec1181` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_REFERENCES.md` |
| `99b871635d9a3a4ec61393c63138211f9ff8bfaae0a4175596b3b85644a847d4` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_REFERENCES.md` |
| `0dc254ab57227b1fbf0109d2ebfc14a41654ec0c85c1eda3050ac569671d5b58` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_REFERENCES.md` |
| `6e64cb640b394c931f1c20306b28fc5f95fa60d8f5dd4280911c739c825b8f02` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_REFERENCES.md` |
| `1052ada927f89b19705ec27e9de9701cb9024cb08d4ec71210e4ef7de63b4944` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_REFERENCES.md` |
| `bdc61af4db54085784362cd33149c4ec90ce60c09b5df5fcecda62add0f15e45` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_REFERENCES.md` |
| `7884c0402107ed45b37e170094f83c0dac26d276439604b70e3c9b86cfc67fed` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_REFERENCES.md` |
| `a52cbe5b267ead64a733aa3383e14b7761ab2fa6bb0523c4257e68a6bad60a52` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_REFERENCES.md` |
| `d8efe5e540b8b0ae32ca1e9c26b85d8abdbcc01898c31694165934fa9958a20b` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_REFERENCES.md` |
| `94d1fd3dae2d8453907db80eb2368cac713889e940d97bb846f329b97e01202d` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_REFERENCES.md` |
| `9f0d557bda938e1a9180af89c5b98bed308fbdaa19032fa12c90eb0067beb151` | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_REFERENCES.md` |

### 11.5 Reference evidence consulted (not inventoried; cited in §3 and Notes)

| SHA-256 | Path |
|---|---|
| `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` |
| `40630ed1952ca44e4a1a1b04977f77e6d3604cc39fd52bb9b801822929108c48` | `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/A2_IMPACT_INVENTORY.md` |
| `f532a666f3a49cf0dba19944da33979b2b947a98f620cb2e3eeece92a23b5e31` | `projects/pec/execution/_Coordination/ASSESSMENT_2026-09-23_APP_PIPING_PEC_UNISON.md` |
| `ec9cc14df99dc627122ec99c6b5b5e9dffd26631445ebec42679205b49835053` | `projects/pec/loop/LOOP_INIT.md` |
| `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25` | `projects/chirality-app-dev/loop/LOOP_INIT.md` |
| `c712b6487faa3fab461e181aad1a6c16a2cb0eb734c510744e5037289105df1b` | `projects/chirality-piping/loop/LOOP_INIT.md` |
| `890ed040fd518c2448450583727f159d6059e9bdfed8d532b3209d3130600569` | `projects/chirality-runtime/loop/LOOP_INIT.md` |
| `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899` | `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` |
| `fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2` | `docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md` |
| `5346d950c4981096f92f2a34d942889e06982c582542e47f72449c1d2bbe5c61` | `docs/DIRECTIVE.md` |
| `2f9f37788a17be9c5030c631dbb53be2f1b59a325bd51bc5bf6ac4e86a781865` | `projects/chirality-runtime/docs/APPLICATION_CONSUMER_GUIDE.md` |
| `e481e79f1dd28d41bf47db50c58fa1ad50ed14e559fc3975240b6862a31275d4` | `execution/_harness/adapter.yaml` |
| `f4fbbf1f675b9aa7e9e7b71f26841de7d5031107c498f72e48cee4b5f0009e98` | `projects/chirality-app-dev/_harness/adapter.yaml` |
| `2de9d3ab3b3e3b2eb622c0959dc292eff06a11c3da7c2665798978df08c20554` | `projects/chirality-piping/_harness/adapter.yaml` |
| `fb70f812656bf51c217dfa104dc96a733fdb713a9071d563a447ca4fd27fff7e` | `projects/chirality-runtime/_harness/adapter.yaml` |
| `eef5434b0ea17d757d4f8a8892d383df4edaab53a571c075af2f3d498c46dfa8` | `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md` |
| `6dbb884aed7ebf573abf476d54b404a3c6f8620208327dcae2453fef5757081f` | `projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md` |
| `50933010aef9920d1a615006775ea8997080e5388532ef7d3e9ac8bad92a9a9d` | `projects/chirality-piping/execution/_Coordination/WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md` |
| `74f068846dd56d97414244635fb6b99c642ffc33ddde5c1f3cf128d30d621428` | `projects/chirality-piping/execution/_Coordination/WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md` |
