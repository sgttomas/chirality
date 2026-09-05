# Reconciliation Report — SCA-APP-010 post-alignment read-only checks

**Date:** 2026-09-05
**Basis:** `d66395d101143df68d956984f7ab93f5027418ec` (`HEAD` = `origin/main`, branch `claude/sca-app-010-dependency-closure`) plus the thirteen refreshed dependency registers in the working tree
**Result:** `FINDINGS` — no BLOCKER, no MAJOR; seventeen MINOR/observation-grade `MISMATCH` claims and two `UNKNOWN` claims out of 489 claim rows; the applied pair, pointer, corpus, lifecycle, fences, and refreshed registers all reconcile
**Posture:** read-only checks executed for the RECONCILIATION manager before any activation; **not an activated claim-level concordance run** (no activation ruling, no human-calibrated convention set); nothing here is authority and nothing here claims closure

## 1. Authority corpus

From the App working root:

`PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`

Exit zero; `corpus current_version: v20`; all eight governed members `[MATCH]`; `no drift.` Verbatim output in `Evidence/corpus_status.txt`. The decomposition and companion register are not corpus members, so no corpus bump is implied.

## 2. Applied pair and pointer

| Check | Result |
| --- | --- |
| Live decomposition SHA-256 | `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (expected; equals Gate-5) |
| Live companion SHA-256 | `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (expected; equals Gate-5) |
| Pointer `_ScopeChange/_LATEST.md` SHA-256 | `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (expected; `OPEN_PENDING_DERIVATIVE_CLOSURE`, active snapshot SCA-APP-010) |
| Companion structure | 83 rows, 83 unique IDs, 50 families, 18 columns (equals Gate-5) |
| Decomposition pins | 83 of 83 rows carry `#candidate-sha256=c7c05169…` (equals Gate-5) |
| Contract pins | all 83 `ContractSourceSHA256` = `842bf170…`; live `docs/CONTRACT.md` = `51ec0d48…` = corpus v20 member (unchanged) |
| K-PATH-2 | `AppDeliverableIDs` contains `DEL-07-03`; `RationaleEvidenceAnchor` contains `#SOW-081` (the Gate-5 semantic delta, still present) |
| `decomposition_basis` pin `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` | a commit ("wip: SCA-APP-010 Gate-5 application"), ancestor of `HEAD`; the decomposition and companion at that commit hash to the two values above, so every carrier's front-matter pin resolves to the applied bytes |

Evidence: `Evidence/applied_pair.txt`.

## 3. Carrier concordance (claim level, read-only)

`CARRIER_CONCORDANCE.csv` holds 489 claim rows over the thirteen carriers (columns `Carrier,Claim,DecompositionValue,CarrierSurface,CarrierValue,Disposition,Evidence`). Totals: **ALIGNED 470 · MISMATCH 17 · UNKNOWN 2**.

| Carrier | Row | ALIGNED | MISMATCH | UNKNOWN | Validator | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| DEL-02-01 | L307 | 38 | 1 | 0 | PASS | F-2 |
| DEL-02-02 | L308 | 38 | 4 | 0 | PASS | F-1, F-2, F-3 (two items) |
| DEL-02-04 | L310 | 35 | 1 | 0 | PASS | F-2 |
| DEL-02-05 | L311 | 37 | 0 | 1 | PASS | F-5 |
| DEL-03-02 | L318 | 38 | 1 | 0 | PASS | F-1 |
| DEL-04-04 | L329 | 37 | 1 | 0 | PASS | F-1 |
| DEL-05-02 | L337 | 37 | 2 | 0 | PASS | F-1, F-3 |
| DEL-06-03 | L348 | 37 | 1 | 0 | PASS | F-1 |
| DEL-07-01 | L357 | 37 | 1 | 0 | PASS | F-1 |
| DEL-07-03 | L359 | 31 | 2 | 0 | PASS | F-1, F-4 |
| DEL-08-01 | L368 | 39 | 1 | 0 | PASS | F-1 |
| DEL-08-03 | L370 | 33 | 0 | 0 | PASS | no seated item (record-only, by owner mapping) |
| DEL-08-04 | L371 | 33 | 2 | 1 | PASS | F-1, F-4, F-5 |

What reconciles on every carrier: `_CONTEXT.md` identity (DeliverableName, PackageName, Type, ContextEnvelope, revision/path); `_CONTEXT.md` Deliverable Scope equals the applied row Description; `_CONTEXT.md` SupportsObjectives; `ScopeOfWork.md` front matter (`decomposition_basis` pin, `project_scope_refs`, `package_objective_refs`); the "SCA-APP-010 Gate-5 Current Contract" heading, row line, responsibility text, and applied-row outputs; `_REFERENCES.md` H1 and applied identities; the Scope Ledger reverse view names the carrier for every scope ref on its row; `Dependencies.csv` carries the applied name on every row, exactly one ACTIVE `IMPLEMENTS_NODE`, an ACTIVE trace for every objective, and no ACTIVE trace to a scope or objective ref that is not on the applied row (the one SCA-APP-010 removal, SOW-007 from DEL-02-02, is RETIRED as `DEP-02-02-003`); SCA-APP-010-seated items cite the applied row line and on-row refs; `validate_scope_of_work.py` PASS `format=SOW_V1` (`Evidence/validator.txt`).

Evidence: `Evidence/surfaces.txt`, `Evidence/anchors.txt`, `CARRIER_CONCORDANCE.csv`.

## 4. Lifecycle and fences

| Check | Result |
| --- | --- |
| `Current State` vs `origin/main` | `IN_PROGRESS` on all thirteen, unchanged |
| `Checking Approval SHA` vs `origin/main` | `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` on all thirteen, unchanged |
| `_STATUS.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, `MEMORY.md` | byte-identical to `origin/main` on all thirteen |
| F-APP-1 to F-APP-5 | `loop/LOOP_INIT.md` byte-identical to `origin/main`; no carrier surface that cites a fence changed |
| Working-tree change set per carrier | exactly `Dependencies.csv` (M), `_DEPENDENCIES.md` (M), one new `_run_records/TASK_RUN_2026-09-05_<HHMM>.md` (??); nothing else |
| Refreshed registers vs reviewed post-images | live `Dependencies.csv` and `_DEPENDENCIES.md` SHA-256 equal `Evidence/n3_reviewed_postimages.json` and `Evidence/n3_postwrite_identities.json` for all thirteen |

Evidence: `Evidence/lifecycle_fences.txt`, `Evidence/register_parity.txt`.

## 5. Derivative state (SCA-APP-010)

| Derivative package | State at read time | Evidence |
| --- | --- | --- |
| Applied decomposition + companion | current (truth complete; hashes above) | `Evidence/applied_pair.txt` |
| Active pointer `_ScopeChange/_LATEST.md` | current at the approved post-image; status `OPEN_PENDING_DERIVATIVE_CLOSURE` | `Evidence/applied_pair.txt` |
| Thirteen carrier working surfaces | current with the applied rows (merged, PR #713 under D-APP-108), with the MINOR lags in F-1 to F-3 | section 3; `Evidence/surfaces.txt` |
| Thirteen carrier dependency registers | current in the working tree; refreshed 13/13, equal to the N2-reviewed post-images; **not yet committed or merged** | `Evidence/register_parity.txt`; `git status` |
| Closure audit `DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/` | **present and still being written** by N4 at read time: `Brief.md`, `analyze_closure.py`, `Evidence/*`; `Evidence/closure_summary.json` reports 52 files, 635 rows, 48 nodes, 109 edges, `scc_count` 1 (size 9), 4 orphans, 1 bidirectional pair — the same figures as the N2 fan-in parity; no closure report or verdict file existed yet; `DepClosure/_LATEST.md` unchanged (`CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`), an owner act | `Evidence/derivative_state.txt` |
| Decomposition audit (N6 `AUDIT_DECOMP`) | no surface present at read time | `Evidence/derivative_state.txt` |
| This reconciliation package | this snapshot; `_Reconciliation/_LATEST.md` not moved | — |

Open (not closed by this pass, none within its authority):

- **SCA-APP-009 derivative closure** — open: its `Handoff_State.md` verdict remains `OPEN_PENDING_DERIVATIVE_CLOSURE` (last touched `87f2d2a75`); `DOWNSTREAM_HANDOFFS.csv` row 10 (owner disposition or SCA-APP-010-as-active ruling) has no ruling after D-APP-108 in `_DECISIONS/_REGISTER.md`.
- **TM-001 (DEL-02-02 label)** — open as a TASK_MANAGEMENT act: no row in `_TaskManagement/REGISTER.csv` or `REGISTER_CLOSED.csv` carries the pre-image name (TM-APP-036 references DEL-02-02 by ID only), so the refresh may be vacuous, but no TASK_MANAGEMENT disposition record dated after the merge exists.
- **Owner disposition of SCA-APP-010 `Handoff_State.md`** — open: its derivative fields still read `DerivativePackageState INCOMPLETE`, `MetadataAlignmentState NOT_STARTED`, `DownstreamRerunState FROZEN` (last commit `91402dcda`), which lag PR #713 and this run; per the orchestration plan they change only on the owner's disposition.
- **Root notice (row 7)** — routed: seating commit `db0dff954` added `execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` at the repository root (the Root loop's coordination surface); the receiving loop's receipt is not evidenced here.
- **N4 acceptance, N6, N7 fan-in** — separately owned.

## 6. Findings

Severity: MINOR = wording, stale anchor, or unrefreshed derivative field with no authority, lifecycle, or graph effect; observation = no repair proposed. No BLOCKER or MAJOR finding.

### F-1 — MINOR — nine carriers — `_CONTEXT.md ## Traceability | CoversScopeItems` not refreshed to the applied scope refs

DEL-02-02 lists `SOW-006, SOW-007` (retired SOW-007 retained; SOW-081, SOW-082 missing); DEL-03-02 lacks SOW-083; DEL-04-04 lacks SOW-081, SOW-084; DEL-05-02 lacks SOW-082; DEL-06-03 lacks SOW-082; DEL-07-01 lacks SOW-084; DEL-07-03 lacks SOW-081; DEL-08-01 lacks SOW-082, SOW-084; DEL-08-04 lacks SOW-083. The four carriers whose scope refs SCA-APP-010 did not change (DEL-02-01, DEL-02-04, DEL-02-05, DEL-08-03) are aligned. In every case the `ScopeOfWork.md` front matter, the Gate-5 section, the `_CONTEXT.md` Deliverable Scope prose, and the ANCHOR rows are current, so the lag is confined to one table row; DEL-08-04's `DEP-08-04-012` Notes already disclosed it. Route: WORKING_ITEMS (carrier working-surface refresh); not repaired here.

### F-2 — MINOR — DEL-02-01, DEL-02-02, DEL-02-04 — `_CONTEXT.md ## Source Authority` names SCA-APP-004 as controlling

Each of the three PKG-02 paragraphs still reads "SCA-APP-004 and its owner-approved amendment prospectively control the current presentation target"; the applied SCA-APP-010 row (DEC-025, decomposition L634) controls, and each carrier's `ScopeOfWork.md` Gate-5 section says so where earlier clauses disagree. DEL-02-02's paragraph also keeps "Work and Agents remain rebuildable, evidence-conditional projections" although the applied row L308 unmounts the Work projection and names the "Who is working" view. Route: WORKING_ITEMS; not repaired here.

### F-3 — MINOR — DEL-02-02-V3-01, DEL-02-02-V3-02, DEL-05-02-V3-01 — stale applied-row line anchors in pre-existing Remaining items

The two DEL-02-02 items cite "applied decomposition row L294" and the DEL-05-02 item "row L323". In the applied decomposition L294 is the `### PKG-01` heading and L323 is blank; L294 and L323 were the DEL-02-02 and DEL-05-02 rows in the pre-SCA-APP-010 revision `d6f6cadb2` (2026-08-24). The items were seated by the SCA-APP-009 pathway seating and were not re-anchored by D-APP-108 (which adopted the presented list). Their parentheticals remain consistent with the applied rows. DEL-02-02-V3-01's "Work/Agents presentation" title predates the applied row's "Who is working" view; whether to re-frame it is an owner/WORKING_ITEMS decision, not decided here. Route: WORKING_ITEMS for the line anchors, with owner visibility for the re-framing question.

### F-4 — observation — DEL-07-03 SOW-026, DEL-08-04 SOW-063 — scope ref anchored on the `IMPLEMENTS_NODE` row, not on a `TRACES_TO_REQUIREMENT` row

`DEP-07-03-001` and `DEP-08-04-001` are ACTIVE `IMPLEMENTS_NODE` anchors with `TargetType=WBS_NODE` and the scope ref as target; no `TRACES_TO_REQUIREMENT` row exists for those two refs. This is a register convention that predates SCA-APP-010 (DEL-07-01 and DEL-08-03 anchor `IMPLEMENTS_NODE` to the deliverable itself, the other nine to the package), and the N2 review accepted "exactly one ACTIVE `IMPLEMENTS_NODE` per carrier". Scope-ref coverage is present; the ledger records `MISMATCH` only against the brief's literal expectation. No repair proposed; the anchor-shape heterogeneity is noted for the `dependency-extract` skill owner if a uniform shape is wanted.

### F-5 — UNKNOWN — DEL-02-05-V3-03, DEL-08-04-V3-01 — pre-existing items without an applied-row citation

Both items predate SCA-APP-010 and trace to OUT/REQ/AC/VER, DEP, and CLM identifiers rather than to a decomposition row; this pass did not re-evaluate them against the applied rows. Owner-seated wording stands.

### Observations without a disposition

- Seated Trace lines cite some scope refs owned by other carriers (DEL-02-01-V3-01: SOW-002; V3-02: SOW-008; V3-03: SOW-002, SOW-010; DEL-02-02-V3-03: SOW-001, SOW-007) as related requirements with owner cross-references; treated as cross-references, not scope claims.
- DEL-02-02's folder keeps the pre-image physical name `DEL-02-02_Workbench_and_Pipeline_Selection_UX` (stated as compatibility in `_CONTEXT.md`); this is the "name lag" already routed by `_ScopeChange/_LATEST.md` and is outside the claims this brief asked for.
- DEL-08-03 has no SCA-APP-010 item seated (`## Remaining` empty), matching the owner mapping ("none; record-only history line") and the applied row's note that no active presentation consumer exists.

## 7. Not reconciled here

- No claim-level ledger over requirements, implementation, tests, or evidence (an activated RECONCILIATION run under an owner ruling would do that); this pass compares identity, scope, traceability, register-anchor, lifecycle, and fence claims only.
- No verdict on the N4 closure audit (in progress at read time), no N6 decomposition audit, no acceptance of any snapshot, no `_LATEST.md` movement anywhere.
- SCA-APP-009 closure, the TM-001 label disposition, the owner's `Handoff_State.md` disposition, the Root loop's receipt of the routed notice, Q15/Q16 acceptance text, and the nine-node SCC remain with their owners.
- No repair to any deliverable; findings F-1 to F-3 are routed, not applied.

## 8. Rerun method

From the repository root at basis `d66395d1…` with the refreshed registers in the working tree: run the corpus status command in section 1; `shasum -a 256` over the three applied-pair files; `git show dbd812a5…:<decomposition>` hashed to confirm the pin; `validate_scope_of_work.py` per carrier; `git status --short` and `git show origin/main:<path>` diffs per carrier; `sha256` of each carrier's `Dependencies.csv` and `_DEPENDENCIES.md` against `n3_reviewed_postimages.json`; and a CSV/regex pass reproducing `CARRIER_CONCORDANCE.csv` from the decomposition rows, `_CONTEXT.md` tables, `ScopeOfWork.md` front matter and Gate-5 section, `_REFERENCES.md`, `_STATUS.md` Trace lines, and the ANCHOR rows. The helper scripts used are private scratchpad files; their SHA-256 values head `Evidence/anchors.txt` and `Evidence/surfaces.txt`, and the ledger generator is `a0f793b3…`.

## Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting for RECONCILIATION's read-only checks, dispatched by HELP_HUMAN; not an activated concordance run; role not mechanically enforced; no descendant launched.
