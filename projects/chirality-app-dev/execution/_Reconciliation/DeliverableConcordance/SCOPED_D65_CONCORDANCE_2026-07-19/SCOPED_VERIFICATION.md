# SCOPED_VERIFICATION — V1 Adversarial Verifier Report

RunID: SCOPED_CONCORDANCE_2026-07-19 — instance V1
Basis: live tree at HEAD `ff2f68c82`; drift window `c313325b74d37da1aacc4d988046cfbd26c88bf4` → `ff2f68c82`
Prior ledger: `RUN_D55_CONCORDANCE_2026-07-11_1904Z/CLAIM_CONCORDANCE.csv` (1,115 data rows)
Method: read-only Bash per amendment v2 (`grep`/`ls`/`find`/`sed -n`/`head`/`tail`/`wc`/`git log|show|diff`); every citation below re-read against the live tree, not the discovery evidence. All verdicts here are agent claims, not owner acts.

Tool-fence disclosure (V1's own): shell loops/conditionals composed exclusively of the authorized commands were used for the exhaustive cross-check; one `shasum -a 256` of a `git show` stream was used to confirm the live `docs/PRD.md` hash (read-only, no file written); no mutation, no network, no test execution; sole write is this file via the Write tool.

---

## Check 1 — Schema / coverage: PARTIALLY REFUTED (2 rows), otherwise CONFIRMED

- All 11 ledgers carry the exact 9-column header
  `ClaimID,DeliverableID,InScopeReason,PriorDisposition,ScopedDisposition,Evidence,DriftClass,ProposedRepair,HumanDecisionNeeded`.
- Every data row terminates in `,YES` or `,NO` and no ledger contains embedded-newline continuation lines (row count = YN-terminated line count in all 11 files). Parse verdict: CONFIRMED.
- Row-count reconciliation (ledger total = prior-package rows + new SCOPED rows): PKG-00 28=27+1; PKG-01 94=89+5; PKG-02 107=107+0; PKG-03 90=89+1; PKG-04 116=115+1; PKG-05 123=116+7; PKG-06 142=131+11; PKG-07 127=125+2; PKG-08 101=98+3; PKG-09 116=113+3; PKG-10 106=105+1. Total 1,150 = 1,115 prior + 35 new. CONFIRMED, except the G3 return's prose claim "PKG-04 = 116 (all prior rows)" — the prior ledger holds 115 PKG-04 rows (F-4). The PKG-04 ledger itself is internally consistent.
- **Exhaustive PriorDisposition cross-check (all 1,115 carried rows, keyed ClaimID+DeliverableID against the prior ledger):** 1,113 match; every key resolved uniquely (zero KEYFAIL). Two rows REFUTED:
  - `DEL-01-02-RBR-009` (PKG-01, G1): ledger records PriorDisposition `ALIGNED`; prior ledger row ends `...OVERTAKEN by ADQ-02 (RB-PERMISSION row line 42); no superseding note on the assessment,STALE_ASSESSMENT,HIGH,...` → prior was `STALE_ASSESSMENT` (F-1).
  - `DEL-02-01-REQ-011` (PKG-02, G2): ledger records PriorDisposition `ALIGNED`; prior row carries `,STALE_ASSESSMENT,HIGH,` (F-2).
  In both, ScopedDisposition=ALIGNED/DriftClass=NONE, so a real prior-drift closure (or persistence) went unadjudicated and the instances' delta counts are each understated by one.

## Check 2 — Delta sample (drift→ALIGNED / RESOLVED): CONFIRMED 15/15

Fifteen rows claiming resolved drift, spread across all six instances, re-verified at HEAD with live citations:

| # | Row (pkg / instance) | Live evidence re-read at HEAD |
|---|---|---|
| 1 | DEL-00-01-REQ-003 (00/G1) | `PKG-00.../DEL-00-01.../README.md` L22-23: DEP-10-02-004 `RETIRED`,`NOT_APPLICABLE`; DEP-10-03-006 `ACTIVE`,`SATISFIED` |
| 2 | REQ-DEL-00-02-005 (00/G1) | `DEL-00-02.../_STATUS.md` L26: 2026-07-12 D-APP-56 R5 P43 UPD-084 append-only INSP-03 superseding annotation |
| 3 | DEL-02-03-EXC-003 (02/G2, self-flagged recheck) | `R6_D55_BACKCHECK.../R6_BACKCHECK.md` L20: "255 CONFIRMED, 0 REFUTED, 0 UNVERIFIABLE"; DEL-02-03 SOW L219/L345 carries the UPD-108 deferral-supersession note the instance had not re-read — its gap closes CONFIRMED |
| 4 | DEL-03-02-REQ-009 (03/G2) | DEL-03-02 SOW L143-144: stub-adapter durable-terminal-persistence exclusion, "test scaffolding, not K-EVENT-3 parity" |
| 5 | DEL-03-04-REQ-006 (03/G2) | DEL-03-04 SOW L127-128: identical exclusion text |
| 6 | DEL-04-01-REQ-003 (04/G3, PI→ALIGNED) | `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` L28-35: live query() sequence + result top-level keys |
| 7 | DEL-04-01-REQ-008 (04/G3, PI→ALIGNED) | same probe L36-40 (transcript placement, session_id); `_STATUS.md` L28 (D-APP-52 owner in-session act, rows 007/011/013 SATISFIED); `sdk-options-builder.ts` L155 `resume: input.session.sdkSessionId` |
| 8 | DEL-04-02-REQ-005 (04/G3, PI→ALIGNED) | DEL-04-02 SOW L108/L218 UPD-119/120/121 runtime-vs-builder split text; `turn-engine.ts` L163 `assertKnownAgentSdkTools` |
| 9 | DEL-04-02-REQ-012 (04/G3, PI→ALIGNED) | same SOW lines; probe-backed property names |
| 10 | DEL-05-03-R12 (05/G4) | `D-APP-67_PACKET...md` L3-4 Status RULED Option B 2026-07-19, §Human Ruling L172; `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md` exists in the deliverable folder |
| 11 | REGISTER-2 / DEL-05-02 (05/G4) | `_DEPENDENCIES.md` L79-84: dated "D-APP-56 R5 P45 current register summary", ACTIVE 11 / RETIRED 1, "Correction: DEP-05-02-007 is RETIRED" (UPD-125) |
| 12 | DEL-07-04-REQ-014 (07/G5, →ACCEPTED_DIVERGENCE) | `TASK_RUN_2026-07-19_DAPP66_ruling_closure.md` L17-22: "Option C — status quo", revalidation NOT added, survives to issuance (F-APP-4); commit e18da2956 records D-APP-66 ruled C |
| 13 | DEL-07-04-REQ-017 (07/G5) | `frontend/src/lib/lifecycle/transition.ts` L67 `normalizeActor`, invoked L170 |
| 14 | DEL-09-01-REQ-003 (09/G6) | `validate-harness-premerge.test.ts` L39-48: RUNTIME_SURFACE_MISSING fixture with nonzero-exit assertions |
| 15 | DEL-10-01-REQ-002 (10/G6) | DEL-10-01 SOW L65 (Release-scope row) and L184 (out-of-scope) state the D-APP-49..52 staged-live surface with endpoints/apply/hooks future-gated |

Zero refutations in the delta sample.

## Check 3 — New rows: CONFIRMED 35/35 real, in-window; two rows carry a refuted premise clause

**Count note:** the V1 brief says "ALL 22 SCOPED-S rows"; the ledgers contain **35** SCOPED-S rows, matching the six returns' own arithmetic (6+1+1+18+5+4). All 35 were verified; the brief's 22 appears to be a stale planning number (F-5, orchestrator-side, not a discovery error).

- **Kit→SOW consolidation class (18 rows: DEL-05-0{1..5}-S01, DEL-06-0{1..6}-S01, plus the consolidation clauses inside DEL-01-0x/DEL-09-01/DEL-10-01 rows):** `git diff --name-status c313325b74..ff2f68c82` over `projects/chirality-app-dev/execution/PKG-*` shows exactly 53 `Datasheet.md` deletions, 159 Specification/Guidance/Procedure deletions, and 53 `ScopeOfWork.md` additions — the conversion is real, in-window, corpus-wide. Per-deliverable commit citations spot-verified (e.g. `8c8b0ef22` "Migrate DEL-05-01 to ScopeOfWork v1", 2026-07-13; `548caa731` for DEL-04-01; both ancestors of HEAD inside the window).
- **Migration-residue rows (G1: DEL-00-02-S01, DEL-01-01-S01/S02, DEL-01-02-S01, DEL-01-03-S01, DEL-01-04-S01):** spot-verified live — DEL-01-01 SOW L160 still requires "Datasheet.md, Specification.md, Guidance.md, and Procedure.md exist and are non-empty" (files deleted); L117 "ResponsibleParty remains TBD" vs the recorded D-APP-65 assignment; DEL-00-02 SOW L371 vs L36 contradiction; DEL-01-04 SOW L66 doubled "the current the current". All real, produced in-window by the migration/partial updates. CONFIRMED.
- **Managed-orchestration rows (G4: DEL-05-01-S02, DEL-05-02-S02, DEL-06-0{1,2,3,4,5}-S02; G5: DEL-07-01-S01, DEL-08-04-S01/S02, DEL-08-05-S01):** verified live at HEAD — `SessionRecord` delegation fields at `types.ts` L43+; `coordination.notice/update/acknowledged` at `event-schema.ts` L44-46; `CHIRALITY_MCP_COORDINATION_TOOL_NAMES` (4 tools) at `mcp/tool-names.ts` L24-29; `harness-permission.v7.coordination-mode` at `permission-overlay.ts` L12; `harness-shell.v2.managed-child-scopes` at `tool-shell-policy.ts` L7 with the project-root read+write Bash gate at L196-201; managed-read/write-scope deny classes at `tool-path-policy.ts` L266; `subagent-bridge.ts` L5 `subagent-bridge.v4.disabled-after-managed-delegation` and L84-90 `return undefined`; `subagent-governance.ts` L159-168 parent-type-relative eligibility. Originating commits `62e563e47`/`c9734a6ee`/`ee35409f5` confirmed in-window. CONFIRMED — none phantom, none pre-existing.
- **Hash-lag rows (G6: DEL-09-01-S02, DEL-09-05-S01):** `docs/PRD.md` changed in-window (commits incl. `62e563e47`); live PRD SHA-256 = `d95d826a1...` exactly matching the rebaselined `_REFERENCES.md` REF-006 L12; SOW L365 (09-01) and L68 (09-05) still pin `ac35fba40...`. CONFIRMED.
- **DEL-04-01-S01 (G3):** `Evidence_CODEV-001_SDK_Probe_Record.md` L64/L79 still assert BLOCKED_TBD with no supersession note, contradicted since 2026-07-18 by the D-APP-52 probe. CONFIRMED.
- **DEL-03-03-S01 (G2):** `DEL-03-03/_STATUS.md` L10 carries the R4-P48 deferral with the literal "revisit: next concordance pass" instruction; the route file exists. Honest carried item, correctly classed PERSISTING. CONFIRMED.
- **Conversion-provenance rows (G6: DEL-09-01-S01, DEL-10-01-S01):** the drift they describe (dangling kit-file citations; no D-APP register row for the conversion) is real — see Check 5. However their evidence clause "the D-GOV register was not locatable by this discovery / could not locate in-repo" is **refuted** (F-3): the register exists at `docs/governance_harness/_DECISIONS/_REGISTER.md`. The rows stand as drift records; their premise needs amendment at fan-in.

## Check 4 — HumanDecisionNeeded: CONFIRMED, with one convention finding

- 25 rows flagged YES across the 11 ledgers (PKG-00:3, PKG-01:5, PKG-05:4, PKG-06:7, PKG-08:4, PKG-09:1, PKG-10:1) — exactly matching the six returns (8+0+0+11+4+2).
- Flag-quality review (all 25 read; 8 in full detail): each states a genuine owner-class question — the G1 live-normative-surface-vs-preserved-quotation interpretive question (e.g. DEL-00-01-REQ-001, DEL-01-04-ACC-001); ownership/mapping assignments for unclaimed surfaces (G4/G5 S02 rows, UNMAPPED rows); policy ratification (DEL-06-05 timeouts); provenance recording (DEL-09-01/10-01-S01, premise caveat per F-3, residual ask still owner-class). None is an agent-resolvable fact dressed as an owner question. CONFIRMED.
- Unflagged PERSISTING sample (6 rows ≥ the required 5: DEL-04-01-REQ-002, DEL-04-01 REGISTER-1, DEL-04-03-REQ008, DEL-04-04 PC-REQ-010, DEL-02-03-UNMAPPED-1, DEL-02-05-UNMAPPED-1): anchors re-verified live (e.g. `persona-manager.ts` L266 `getBootFingerprint`; `_DEPENDENCIES.md` L14/L18 TBD-stub vs 13-row table). No hidden fresh owner question in the PKG-04 rows (the adoption verdict is an already-assigned owner act; register hygiene is agent-repairable). **Caveat (F-6):** PKG-02's carried scope-adoption questions (DEL-02-03/02-05 UNMAPPED-1 — "adopt X into a requirement or record deliberate non-requirement") are flagged NO while structurally identical standing items in PKG-05/06/08 are flagged YES (e.g. DEL-06-01 UNMAPPED-1 "standing", DEL-06-05 UNMAPPED-1). G2's rationale (already-recorded R4-gated questions, category-4 outcome not located) is stated in its NOTES, so nothing is hidden — but the cross-instance convention is inconsistent and will skew any fan-in count of open owner questions.

## Check 5 — Systemic kit→ScopeOfWork.md migration finding: PARTIALLY REFUTED

- Migration commits: CONFIRMED — per-deliverable "Migrate DEL-xx-yy to ScopeOfWork v1" commits dated 2026-07-13 (e.g. `548caa731`, `8c8b0ef22`), corpus finalization "Finalize clean production ScopeOfWork corpus (#237)" at `74b9804cf`; all inside the drift window; 53/53 deliverables converted (Check 3 diff counts).
- D-GOV citation trail: CONFIRMED and **stronger than the discovery instances reported** — `docs/governance_harness/_DECISIONS/_REGISTER.md` rows for D-GOV-15 ("RULED 2026-07-12: all nine items APPROVED", published `58aa81d62`) and D-GOV-16 ("RULED 2026-07-12: items 1–10 APPROVED exactly as proposed", published `7584718aa`); `D-GOV-16_deliverable_scope_of_work_stage2.md` carries Status RULED, the verbatim owner ruling, ratifies schema `chirality-deliverable-sow/v1`, and approves the "bounded remaining-144 conversion". An in-repo authorizing record for the conversion therefore **exists and is locatable**.
- Instance representations: G4 correctly cited `docs/governance_harness/_DECISIONS/D-GOV-16_...` (DEL-05-01-S01 evidence). G6's ledger rows and return, and G1's ancillary note, claim the register/authorizing record could not be located in-repo — REFUTED (F-3). The six-instance "systemic finding" is therefore heterogeneous, not unanimous, and the strong form ("no locatable authorizing record") is false.
- App-dev register gap: CONFIRMED — `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` enumerates through D-APP-67 with no row recording the conversion tranche (the only "conversion" hit is unrelated D-APP-41). The residual owner question — whether the app-dev register should carry a cross-pointer to D-GOV-16 and how dangling kit-file provenance cells are dispositioned — remains genuine.

## Check 6 — Fence audit: CONFIRMED

`git status --porcelain` shows exactly two untracked trees and zero modified tracked files: the run's `_Coordination/AgentRuns/SCOPED_CONCORDANCE_2026-07-19/` (orchestrator briefs + 6 verbatim returns) and this run folder (`MANIFESTS/` 23 orchestrator-provisioned files; `PKG_LEDGERS/` exactly 11 ledgers + 11 notes). No write outside `PKG_LEDGERS/` is attributable to any discovery instance; no `_DomainEngines/**` or `projects/chirality-piping/**` path appears anywhere in the working-tree state (F-APP-3 clean). The disclosed stray no-op `true` Bash calls (G2/G5/G6) and read-only Bash substitutes (G3/G4) left no filesystem trace.

---

## Findings

- **F-1 (REFUTED row, G1/PKG-01):** `DEL-01-02-RBR-009` PriorDisposition transcribed as ALIGNED; prior ledger says STALE_ASSESSMENT. The STALE_ASSESSMENT→ALIGNED closure is plausible (INSP-03 superseding-annotation tranche) but is neither recorded as a delta nor evidenced in the row. Correct the row and G1's delta count (+1) at fan-in.
- **F-2 (REFUTED row, G2/PKG-02):** `DEL-02-01-REQ-011` — same defect class, same correction needed.
- **F-3 (REFUTED premise, G6 rows + G1 ancillary note):** the claim that the D-GOV register / conversion-authorizing record is not locatable in-repo is false — `docs/governance_harness/_DECISIONS/_REGISTER.md` and `D-GOV-16_deliverable_scope_of_work_stage2.md` (Status RULED, remaining-corpus conversion approved) exist at HEAD. Amend `DEL-09-01-SCOPED-S01` / `DEL-10-01-SCOPED-S01` evidence text; the narrower app-dev-register-gap question survives and the HDN=YES flags may stand on that narrower basis.
- **F-4 (return misstatement, G3):** "PKG-04: 116 prior rows" — the prior ledger holds 115 PKG-04 rows; the PKG-04 ledger itself (115 carried + 1 new = 116) is consistent.
- **F-5 (orchestrator/brief discrepancy):** the V1 brief's "ALL 22 SCOPED-S rows" does not match the 35 SCOPED-S rows actually present (which do match the six returns). Reconcile the fan-in arithmetic against 35.
- **F-6 (convention inconsistency, non-blocking):** standing scope-adoption questions are HDN=NO in PKG-02 but HDN=YES for structurally identical items in PKG-05/06/08; disclosed in G2's NOTES, but harmonize before counting open owner questions.

## Sample lists

- Delta sample (15): rows 1–15 in the Check 2 table.
- New-row verification (35): all rows listed in Check 3, by class.
- PriorDisposition cross-check: exhaustive, all 1,115 carried rows (automated grep/sed loop; 2 failures = F-1/F-2).
- Unflagged-PERSISTING sample (6): DEL-04-01-REQ-002; REGISTER-1/DEL-04-01; DEL-04-03-REQ008; PC-REQ-010/DEL-04-04; DEL-02-03-UNMAPPED-1; DEL-02-05-UNMAPPED-1.
- YES-row full-text review (8): DEL-00-01-REQ-001; REQ-DEL-00-02-002; DEL-01-04-ACC-001; UNMAPPED-1/DEL-05-03; UNMAPPED-1/DEL-06-05; DEL-08-03-UNMAPPED-1; DEL-09-01-SCOPED-S01; DEL-10-01-SCOPED-S01.

## Verdict

**FAN_IN_SAFE** — conditional on fan-in applying the F-1/F-2 row corrections and the F-3 premise amendment before any owner-facing synthesis. The discovery corpus is otherwise verified at high fidelity: 15/15 delta claims, 35/35 new-drift rows, 1,113/1,115 prior-disposition transcriptions, 25/25 owner-question flags genuine, fence clean. Nothing found suggests fabricated evidence or systematic verdict inflation; all refutations are localized transcription/premise errors that fan-in can correct without re-dispatch.
