# SCA-APP-012 Brief — Retire the Loop-First Shell and the Remaining Legacy UI

**Status:** `CHECKPOINT_GROUP_3_ACCEPTED` — the owner accepted checkpoint group 1 on 2026-09-27 ("Accept SCA-APP-012 group 1: R-b, W-b, P-keep (keeping the two pages, as recommended), defaults."; `../checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`), checkpoint group 2 on 2026-09-27 ("Accept SCA-APP-012 group 2: T-a, Q-a."; `../checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`) and checkpoint group 3 on 2026-09-27 ("I accept SCA-APP-012 checkpoint group 3"; `../checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/`). Revision 4 of this brief is bound at SHA-256 `3924974af3cd4ffe81169b6f8654657e9e880181d8a217747158255ad8c56d49` (the bytes before this status line changed). This folder is the active snapshot named by `_LATEST.md`.
**Date:** `2026-09-27` (folder time `1828` is UTC)
**Requested by:** Ryan Tufts (repository owner `sgttomas`), in the Claude Code conversation of 2026-09-27, relayed by the coordinating session
**Prepared by:** WORKING_ITEMS, bounded Claude Code subagent, working in an isolated worktree
**Workflow:** `scope-change` (bundled, `workflows/scope-change/`), three grouped checkpoints
**Decomposition variant:** `SOFTWARE`
**Context root:** `projects/chirality-app-dev/execution`
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Allow renumbering:** `false`
**Basis commit:** `adc8bdae18b2e1e48dcf01a304cc055d2cbf84e0` (`origin/main`, merge of PR #1013). Revision 4 moved the package onto this basis. Earlier revisions were prepared at `0adfbc747` (PR #1009), `ec81ef2c7` (PRs #1011 and #1010) and `e1af32fc4` (PR #1007, after PR #1012). Between `0adfbc747` and this basis the only changes outside `projects/chirality-app-v4/` and `projects/pec/` are: the Runtime scaffold-API retirement (PR #1012, merge commit `49bbc9787238d59fe2945c8e9413206d554e56b7`) with its App notice `execution/_Coordination/NOTICE_2026-09-27_RUNTIME_SCAFFOLD_API_RETIRED.md` and three App files that construct `RuntimeService`; and the Root EvidenceFile-resolution tranche (PR #1013), which changes `tools/validation/validate_decomposition_registers.py` and adds an App notice `NOTICE_2026-09-27_EVIDENCEFILE_RESOLUTION.md`, a loop receipt and two `_Evaluation` pointer updates. Every input hashed below is byte-identical at all four commits. The builder reports `governed_inputs_identical_to_basis: true` at this basis.
**Revision:** 4 (revision 2 folded in the additional conflicts and added choice W; revision 3 recorded the Runtime scaffold-API retirement as merged; revision 4 answers the independent review of `647fbf919`: it states that P-keep departs from the approved proposal, moves the register-only and code-only items out of the intake register, and completes the W-b, L-lib and S-tool carriers)
**Stage:** checkpoint-group-1 preparation only (intake, validation and impact). This package writes no decomposition, register, PRD, SPEC, PLAN, Scope of Work, `_CONTEXT.md`, `_STATUS.md`, dependency register, pointer, decision snapshot, `DECISION.md`, `SCA-APP-012_GROUP-1_AUTHORIZED.md` or `_LATEST.md` byte, and no code.
**Precedent:** SCA-APP-011 (PRs #995 and #1009). Its group-1 `Impact_Assessment.md` (choice B) and `Intake_Actions.csv` rows 28–32 assessed this legacy-shell removal as set L, which the owner excluded from SCA-APP-011 ("Exclude it (Recommended)"). This run reuses that analysis, re-verified at the basis, and follows the same package layout and the `checkpoint_snapshots/` decision-snapshot layout.

## Owner direction (verbatim)

Given on 2026-09-27 in the Claude Code conversation, as relayed verbatim by the coordinating session.

1. "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary."
2. "Scaffolding through the agent is enough."

Direction 1 answered the coordinating session's proposal, whose opening sentence was, verbatim: "The rest of the dead legacy UI: a small scope-change amendment, SCA-APP-012." The coordinating session summarizes the rest of that proposal as follows (its summary, not the owner's words):

- it covers the loop-first shell, the `legacy` prop, `DeliverablesProvider`, `/api/working-root/scope`, and the `/workbench` and `/pipeline` pages (that is, it listed the two pages for retirement);
- it folds in the DEL-02-03 REQ-009 residual (restate REQ-009 as task-scope preselection, or retire it; settle DEP-02-03-009);
- it needs the owner at the same three checkpoints as SCA-APP-011, but is smaller, with no new or retired deliverables.

Direction 2 is the owner's authority for retiring the Runtime project-scaffold API. The Runtime loop did so in PR #1012 (merge commit `49bbc9787238d59fe2945c8e9413206d554e56b7`, Runtime Receipt 5) and informed the App with the notice `execution/_Coordination/NOTICE_2026-09-27_RUNTIME_SCAFFOLD_API_RETIRED.md`. The coordinating session asked this package to restate the App texts that still name a future App-side scaffold entry.

These are the owner's direction and route selection. They are not the group-1 acceptance, which is a separate act on this package. Accepted App instruments require a separate owner decision before the loop-first UI is retired (PRD KG-033, PRD §6.4, D-APP-74 L107). That decision is made through this amendment's checkpoints; nothing in this package claims it.

## Parsed intent

| Intent | Source | Parsed as |
|---|---|---|
| Delete the loop-first shell (`loop-shell`, `portal-loop-shell`, `loop-tertiary-shell`, `sidebar-right-loop-layout`, `tertiary-sidebar-tabs`), the role-directory panel `portal/agent-matrix`, the discarded `legacy` prop, and the tests and CSS used only by them | Direction 1; proposal item 1 | Supersede PRD KG-033, §6.4 and D-APP-74 L97-99/L107 for the loop-first UI. MODIFY DEL-02-01 and the PRD, SPEC, PLAN and decomposition clauses that keep "the loop-first UI" as a compatibility surface |
| Also delete the discarded `?legacy=1` link (`legacyHref`) and its only test | Found at the basis; same dead thread (revision 2: coordinator's item 2) | Code only, in the code specification (Impact Assessment §15) under DEL-02-01 (Row 1); closes the KG-033 "mock-only `[data-legacy]` test contract" residual |
| Correct the PRD, SPEC and PLAN text that still calls the loop-first shell live or keeps it as the compatibility implementation | Found at the basis (revision 2: coordinator's item 1) | MODIFY PRD §6.3, FR-001, §12.1, §7.2 step 6, FR-007 (Row 13), SPEC §17.9 (Row 16), PLAN §1, §6.5, §13.2 (Row 18) |
| Restate DEL-02-03-REQ-010, which cites the retired FR-010 | Found at the basis (revision 2: item 3) | MODIFY DEL-02-03 (Row 3), the same under either R answer |
| Record the expected dependency re-extraction outcomes and the Task Management note | Found at the basis (revision 2: items 5 and 6) | Not register rows (the workflow writes neither file). Expected outcomes DX-01 to DX-05 and the TM-APP-051 handoff, carried to the group-2 propagation plan (Impact Assessment §11 and §13) |
| Restate the app layout metadata string and the page loading copy | Found at the basis (revision 2: item 7; revision 4: the Suspense fallback text) | Code only, in the code specification (Impact Assessment §15) |
| Decide the unmounted flat-file workflow view (`workflows-view.tsx`, `workflow-detail.tsx`) | Found at the basis (revision 2: item 8) | Owner choice W (remove with its read route, remove the view only, or leave) |
| Delete `lib/portal/agent-matrix-launch.ts` and `agent-matrix-cells.ts` | Proposal item 1 (launch); cells found at the basis | MODIFY DEL-08-02 verification hooks and REQ-003/004 verification (Row 5); PRD §7.2 step 6 and FR-007 (Row 13); SPEC §17.9 L1275-1277 and DIRECTIVE L234 NO_CHANGE with reasons (Impact Assessment §3.4). Departs from SCA-APP-011 set L row 29, which kept those helpers; TYPES §4 alias and route/query semantics stay |
| Delete `DeliverablesProvider` | Proposal item 2 | Code only, under DEL-02-03; no consumer |
| Delete `GET /api/working-root/scope` | Proposal item 3 | MODIFY DEL-02-03, DEL-07-03, PRD §9.2, SPEC §17.2, the decomposition hard constraint and the route-preservation carve-outs; keep `scanProjectScopes` and the `scope_scan` tool contract |
| Retire the `/workbench` and `/pipeline` pages | Proposal item 4 (the approved proposal listed them for retirement) | Owner choice P. P-r (redirect to `/`) and P-d (delete) carry out the approved proposal; the reviewer prefers P-r of the two. The package recommends P-keep, which is a **departure from the approved proposal**: both URLs are enumerated by the Electron renderer-security probe and the packaged security proof and pinned by contract pins, so retiring them needs a new DEL-09-06 native witness; `chat-panel.tsx` keys session mode, drafts and session reuse on them; and D-APP-108 Q3 ruled them reachable and unlisted. Under P-keep only their dead `legacy` element goes. The owner decides |
| Settle DEL-02-03 REQ-009 and DEP-02-03-009 | Proposal item 5; "Include the items with the other owners" | Owner choice R (retire or restate) |
| No App-side scaffold entry is planned | Direction 2 | MODIFY DEL-07-02, DEL-06-03 CLM-031, SPEC §14.2 and PRD goal 17, §6.1, FR-119 and §8.13 wording; the Runtime loop already retired its API (PR #1012) |
| "Include the items with the other owners" | Direction 1 | Read here as: include the residuals held in other deliverables' contracts (DEL-02-03, DEL-07-03, DEL-08-02, DEL-07-02, DEL-06-03), the dependency settlement (DEP-02-03-009) and the Task Management consequence (TM-APP-051). The Runtime scaffold API belongs to another project loop, which retired it in PR #1012; this amendment aligns the App texts with that. The owner can correct this reading at group 1 |
| "You can make changes as necessary" | Direction 1 | Authority to include the items found at the basis beyond the proposal list, each named in the Impact Assessment. It is not the group-1 acceptance |

## Accepted inputs (read-only at this stage)

| Input | SHA-256 at basis | Role |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876` | Decomposition truth (as amended by SCA-APP-011) |
| `execution/_Decomposition/contract_invariant_coverage_register.csv` | `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944` | Companion register; no change proposed |
| `execution/_ScopeChange/_LATEST.md` | `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637` | Active pointer: SCA-APP-011, `OPEN_PENDING_DERIVATIVE_CLOSURE` |
| `docs/PRD.md` | `952451212c0a8f54d6aaeade06eefbab19e110b37c1bdea0b1247f78e1249997` | Product requirements (App) |
| `docs/SPEC.md` | `5a6fcf1577e4d481ad9d25845ac1a1194241cf5c4a696d7da18f8d05946e017f` | Physical and API contracts (App) |
| `docs/PLAN.md` | `e5e3045ba7f867d925e45c480b0d8f077bf6e9e0576d03b896c231a91dbcc093` | Roadmap (App) |
| `docs/CONTRACT.md` | `57411f8df49e6316d8d3bc9674d698b1c8478e639aad331115d4f67bcca97363` | Invariants (App); no change proposed |
| `docs/TYPES.md` | `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835` | Vocabulary (App); no change under P-keep |
| `docs/DIRECTIVE.md` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | Intent (App); no change under P-keep |
| `projects/chirality-app-dev/AGENTS.md` | `41995dfe123041e1d0235a73e532fddb913f2c2124a9e8ec43857a87d7e5822c` | App loop instructions |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` | `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25` | App loop procedure |
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | Root doctrine |
| `workflows/scope-change/WORKFLOW.md` | `b5fd144603c70e977a59988cb7dfe94dd710cac28db97a19f35c437399efbca9` | Selected method |
| `workflows/scope-change/resources/contract.md` | `3e097df0fc0fe5f062d4e2e9ded86a1b84b1c7b4e692ef3510fa239ab1963e9a` | Selected method contract |
| `workflows/scope-change/resources/method.md` | `a3bb270b320dae36c728cad352c189c4e29fea177cdb8a1468f46e8d777b7108` | Selected method detail |
| SCA-APP-011 `Brief.md` / `Impact_Assessment.md` | `146941ee37bd7fbcbe434da7fa29ed4c53e6f4918790a98b4ecf88e582a23109` / `5b74f07668e91ae06f89b1dcb0b612c9dd1871d96fa170df39ce8228e9be9af7` | Precedent; set L analysis (choice B) |
| SCA-APP-011 `Intake_Actions.csv` / `Amendment_Actions.csv` | `e35a3aa84d1943ba8fd41c194691267a893940bb6a4cc2628185007052a8e339` / `416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22` | Precedent intake rows 28–32; accepted register |
| SCA-APP-011 `Supersession_Map.csv` | `9847a4d0d05b65bfbf8d431ba0fb3c24662d73c2574f186e7c259413aa6e65d6` | Cumulative map (SCA-APP-004, 010, 011 bindings) |
| `_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | `1e59194a4f651346c9a7204ace0084fe8ac2115200881799485a9e70443e5ec3` | L97-99: routes, APIs and current UI stay compatibility surfaces "until separately retired"; L107: old-UI retirement needs separate owner acceptance |
| `_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md` | `7ced5e05342de3425673990e5ab3bb37a202cd24198ec6427111ef68c31e64f8` | Q3 (L48): `/workbench` and `/pipeline` stay reachable and unlisted, no 404 |
| DEL-02-01 / DEL-02-02 / DEL-02-03 `ScopeOfWork.md` | `e6b9bdd6ee8529af0d0577645f6cfb74f3b21d67e60c3764a24dca08fa521caf` / `6cb61fe4fd0c1b6678c6f6655c2350439e9dec335cd8c3879183b4494c555582` / `e55fa6e2899c061ac68d426a4386a1a583eb2a19b8724056fa15e3198115b3f8` | Affected contracts |
| DEL-06-03 / DEL-07-02 / DEL-07-03 `ScopeOfWork.md` | `6a8c4674840942dce7734258000e904a87fd3e45673a176305717e2b477215b7` / `697754d4324058cc2b8aa27e30bd1a34b3b6383ea780fb1c22b0f0b263b121a4` / `78b7aaef7d238cb22fb71fbb39b4299747b056ba58403dde8d3fcf5dff9a578f` | Affected contracts |
| DEL-08-02 / DEL-08-03 / DEL-09-06 `ScopeOfWork.md` | `2a9dc258d8e79627b8fb36ed7dc72dc8ea0b22b396b80260942289fe6389c607` / `cf968ae8134e690f22d35a702666a7f704f2a16f39fdbce4549258685a2e0651` / `5f2e06a98a8bdd521dffc8c4ff67469ad588ca66b275dc1350722120282d6c89` | Affected contracts (DEL-08-03 only under R-a; DEL-09-06 evidence only under P-x) |
| DEL-02-03 / DEL-08-02 / DEL-08-03 `Dependencies.csv` | `cee2c96dae648f22685d840c4b8a7960383a18dfe7776062cf5be6d976427681` / `3e9d9df14f6ee143c294d76f37d6921d0a3e44c8c359c4e09f833bedc559c47a` / `fa48f3683fa805aa521df3c5c8d7e3b18cd39deaa222840bc386b1cb8ddc349e` | DEP-02-03-009, DEP-02-03-004, DEP-08-02-013, DEP-08-03-007 |
| `_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md` | `58492b91dfe0ae0296fd104642a0cb728ad9bb525b7e530b4f63b08a808f57ae` | DX-15: DEP-02-03-009 kept with the REQ-009 tension recorded as a residual |
| `_Coordination/_TaskManagement/REGISTER.csv` | `5ca17f4a25e72b90f8650779297d883a777623d895de6c6d2761891f499addad` | TM-APP-051 (APP-R024: scope-scan, summary, status and route consumers), `DEFERRED` |
| Reused full audit `_Evaluation/DecompCoverage/COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500/` (`INPUT_MANIFEST.sha256` / `coverage_summary.json`) | `680b08f02e82b6229d087f1ab08c6a7616e120613cb4de716866a4e0fdcb5dfa` / `44e859cc68d4f0c33d1a309994c39ede14f8074305b6f416e6b86f81d20f1316` | Pre-change coverage basis; all 122 recorded inputs byte-identical at this basis |
| `frontend/src/components/woven-dialogue/woven-dialogue-route.tsx` | `7a8ec779dfb043c3e8bacf6369f1fbe1362f5b078a78dddff3750438727dd57e` | `void legacy` |
| `frontend/src/app/layout.tsx` / `components/workspace/deliverables-provider.tsx` | `9790aa536df6292569e2ca52a68e6031b9a48fbff5d94d8b2d80e196f3fe446c` / `71c38b81f67c09f59f13f98d368af10d29aec19c5ce804a56764cd89f974623d` | `DeliverablesProvider` mount |
| `frontend/src/app/api/working-root/scope/route.ts` | `cc251a77a61ca8534c71eb6630ec4652657fa5c3d26c90a1796c48761b1a7c3b` | The route |
| `frontend/src/components/shell/chat-panel.tsx` | `eef3e49f11a6f4c9fefb077c9b852e854bab973fa03fd69acbe1bd41b831fae1` | L194-208 `resolveMode` maps `/workbench` and `/pipeline` |
| `frontend/electron/main.ts` / `frontend/scripts/run-packaged-security-proof.mjs` / `frontend/src/__tests__/contract-pins.manifest.ts` | `747bd71dd6a827445bbcf9bd400811c066926115b19ffbb55ec006965a99793c` / `5585d6a471661bf1984448b9f5b75c47509f2388707ad9d546cdab93783ee5de` / `df42a6f398cf65978ca73510a402db1adb750122c785b265f8a5347870d2208e` | The four page routes are probed and pinned (choice P) |
| `frontend/src/components/woven-dialogue/workflows-view.tsx` / `workflow-detail.tsx` / `app/api/working-root/workflow/route.ts` / `components/woven-dialogue/right-panel.tsx` | `0f47a87cbd1e3bda048fd99d6a64568e96e377de326d86c46022829a5fd9ddd2` / `4488d3a4e29526d505979077e09548b7a1f18920e6ce7e54b0ad65abc4246330` / `f206a554686f2da2459db7892296029272745329e23056156c33b297054c15df` / `59d88d5c77b597ee35f64ac80a3e3e8911a7eaae87e504feb1a384e984e1da7f` | Choice W: the unmounted flat-file view, its detail and read route; the live Workflows tab (`MethodLibraryView`, L14, L190) |
| `execution/_Coordination/NOTICE_2026-09-27_RUNTIME_SCAFFOLD_API_RETIRED.md` | `5be3999622b233fe326081485ec92a38f5bbd38e43989a4b3652db1c334916ab` | Runtime loop's informational notice: the Runtime scaffold API is retired (PR #1012) |
| `frontend/electron/renderer-window-policy.ts` | `e2d63d32423d1ef6b0a03259235676ac9cefadde00e4f067be4f13e5ed2cc3ed` | D-APP-121 frozen source identity; L13-14 comment names the "open legacy interface" link; NO_CHANGE (Impact Assessment §15) |
| `frontend/src/lib/portal/agent-matrix-cells.ts` / `agent-matrix-launch.ts` | `30a796dca3bdd721744b74fa192f8fa8b6036a50ac7bbc839b1232601141a638` / `3e71713f27b8ed8a4b65f791f08fdcd75bbb5e8ea5d4c3e5f68519ea537022a2` | Default L-lib: deleted |
| `frontend/src/lib/shell/persona-resolution.ts` / `lib/woven-dialogue/guarded-session-selection.ts` | `48eae60bc10e13133a19c7107ef083d32f5dd5ae4d1e79773700b3c796bcdad7` / `36e85943c5d6ce40a6242eb40da7e6d3740dc4fc7d2fb5cb356b40f33e65132c` | Where alias and guard semantics live after L-lib (unchanged) |
| `tools/query/scan_next_amendment_id.sh` | `2310630d2888858d35d6415001d7374e4e0bef821107da5750f73337816d9bdb` | Amendment-ID helper |

Semantic section binding (by heading text, decomposition at basis): Change Register = `12. Decision Log / Change Log` (L613; Change Log L644); Unit Ledger = `9. Scope Ledger` (L403); Objectives = `6. Objectives` (L263); Primary Partitions = `7. Packages` (L280); Secondary Entities = `8. Deliverables` (L297); Vocabulary Map = `4. Vocabulary Map` (L121); SSOW = `5. SSOW` (L172); Open Issues = `11. Open Issues` (L598); Coverage Basis = `10. Coverage and Telemetry` (L496). Additional sections touched: `3. Intake Summary` Hard Constraints (L96, L102) and `13. Downstream Execution Notes` (L664). All bindings resolved; none by position.

`AMENDMENT_ID`: `SCA-APP-012`, confirmed by running `tools/query/scan_next_amendment_id.sh projects/chirality-app-dev/execution/_ScopeChange APP` through its `zsh` shebang (exit 0; highest existing `SCA-APP-011`).

## Parsed action envelope

The machine-readable intake is `Intake_Actions.csv`: 35 rows (revision 4; revisions 2 and 3 had 41, revision 1 had 29), every row `Status = PROPOSED`, with `SupersessionBindingPresent` and `ScopeChanging` filled. It is intake evidence only. The accepted register will be a separate `Amendment_Actions.csv` at checkpoint group 2 and will carry only the sets the owner selects.

| Set | Rows | Meaning |
|---|---|---|
| BASE | 1–18 | Owner-directed: the loop-first shell, legacy prop and link, role-directory panel and portal helpers (DEL-02-01, DEL-08-02); `DeliverablesProvider`, `/api/working-root/scope` and REQ-010 (DEL-02-03, DEL-07-03, DEL-08-03 label); SOW-001 notes, hard constraint, §13 note, DEC-027, telemetry; PRD, SPEC and PLAN, including the text that still calls the loop-first shell live |
| S | 19–21 | Owner-directed scaffold decision: DEL-07-02, DEL-06-03 CLM-031, SPEC §14.2 and PRD goal 17, §6.1, FR-119 and §8.13 wording. Aligned with the Runtime scaffold-API retirement merged in PR #1012 |
| R-b | 22 | Recommended answer to choice R: retire DEL-02-03-REQ-009 (DEP-02-03-009 is retired at re-extraction, expected outcome DX-01) |
| R-a | 23–25 | Alternative: restate REQ-009 as task-scope preselection; DEL-08-03, SOW-007 and PRD §7.5 admit it as a declared consumer (DEP-02-03-009 restated, DX-01) |
| W-b | 26–27 | Recommended answer to choice W: delete the unmounted flat-file workflow view, its detail and its only-called read route `GET /api/working-root/workflow`; DEL-02-02 note and the route's API-preservation carve-outs |
| W-a | 28 | Alternative: delete the view and detail only; the read route stays with no caller |
| W-c | — | Alternative: leave them. No register row |
| P-keep | — | Recommended answer to choice P, a departure from the approved proposal: keep `/workbench` and `/pipeline` as URL compatibility. Code only; no register row |
| P-x | 29–35 | Carries out the approved proposal: redirect (P-r, preferred by the reviewer) or remove (P-d) the two pages; DEL-02-01, DEL-08-02, DEL-02-02, SOW-001/SOW-005, PRD, SPEC/DIRECTIVE/TYPES and the hard constraint |

Counts: BASE 17 MODIFY + 1 ADD; S 3 MODIFY; R-b 1 MODIFY; R-a 3 MODIFY; W-b 2 MODIFY; W-a 1 MODIFY; P-x 7 MODIFY. With the recommended selections (BASE, S, R-b, W-b, P-keep) the group-2 register would hold 24 rows: 23 MODIFY and 1 ADD; with P-r or P-d instead of P-keep, 31 rows. The dependency outcomes (DX-01 to DX-05), the TM-APP-051 note and the code items are not register rows: they go to the group-2 propagation plan and the code specification, as in SCA-APP-011. No REMOVE, RECLASSIFY, MERGE, SPLIT, package change or renumbering under any selection.

## Validation

- **Entities exist and are active.** Every named entity exists at the basis: DEL-02-01, DEL-02-02, DEL-02-03, DEL-06-03, DEL-07-02, DEL-07-03, DEL-08-02, DEL-08-03 (decomposition rows L312, L313, L314, L353, L363, L364, L374, L375; folders with `_CONTEXT.md`, `_STATUS.md` and `ScopeOfWork.md`). Also SOW-001, SOW-003, SOW-005, SOW-007, SOW-024, SOW-081, OBJ-001, OBJ-006 and OBJ-007, the dependency rows DEP-02-03-004, DEP-02-03-009, DEP-08-02-013 and DEP-08-03-007, and Task Management row TM-APP-051. None is retired.
- **New ID.** `DEC-027` does not collide (highest `DEC-026`, L642).
- **Parent closure.** No REMOVE, RECLASSIFY, MERGE or SPLIT; no package or deliverable is retired or added. The parent-closure rule is not engaged.
- **Lifecycle.** All affected deliverables are `IN_PROGRESS`. The App has no `ISSUED` and no `CHECKING` deliverable (53 `IN_PROGRESS`, 1 `OPEN` = retired DEL-09-07). No reopening is authorized or needed.
- **Package discipline.** No deliverable crosses a package boundary; no envelope changes.
- **Contract-level flags.**
  - Row 8 and, under W-b and P-x, rows 27 and 35 change a decomposition hard constraint (browser-facing route stability).
  - Rows 12, 13, 16, 17 and 18 change PRD, SPEC and PLAN clauses that require "separate owner acceptance" or "a separate owner retirement decision". The owner's acceptance of this amendment is recorded as that decision.
  - Under P-x, row 34 changes the App DIRECTIVE.
- **Fences.** No provider, network, release, issuance, domain-engine or Root-owned semantic change. No MCP tool, Runtime tool descriptor or Runtime source changes under this amendment. The Runtime scaffold-API retirement is the Runtime loop's own change.
- **Supersession.** Rows with `SupersessionBindingPresent = YES` need `Supersession_Delta.csv` bindings at group 2. The superseded facts are D-APP-74 L97-99 and L107, D-APP-108 Q3 (P-x only), the SCA-APP-011 DEL-07-02 follow-up text, and the D-APP-56 R4-P29 ownership confirmation (R-b); see Impact Assessment §18.

## Pre-change baseline

`Pre_Change_Coverage.json` is built by `Evidence/Group1/build_pre_change_baseline.py`. The builder is read-only and reproducible from the repository root; two consecutive runs of revision 4 gave byte-identical output (see the Impact Assessment evidence table). Earlier outputs were `4504d70e…0018cb` (revision 1), `e676e10d…1b31e9` (revision 2) and `4e03a9d6…d69880` (revision 3). Revision 2 added the choice-W and layout-metadata code references; revision 3 moved the basis and recorded the Runtime notice by hash; revision 4 moves the basis to `adc8bdae1` and adds the dead-selector candidates, the Suspense fallback copy and the matrix-guard clause scan. At this basis the Runtime scan finds no `ProjectScaffoldPort` or `ScaffoldExecutionRoot{Request,Response}`.

It reuses the latest full `audit-decomp` run, `COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500`, because all 122 of its recorded inputs are byte-identical to this basis (method step 5). It adds:

- the registered structure, dependency-closure and register tools;
- a static import-reachability analysis of the frontend;
- the legacy-only CSS tokens and further dead selector candidates;
- a code reference scan (App, Electron, scripts, Runtime packages);
- a line-level scan of the scope and governance texts.

| Field | Result |
|---|---|
| Topology | 10 packages / 52 deliverables (DEL-09-07 retired) / 10 objectives / 84 scope items (78 IN, 5 OUT, 1 TBD) |
| Coverage | 52/52 declared deliverables have folders; 54 folders (DEL-00-01, DEL-00-02 undeclared control folders, carried); 0 IN scope items without a deliverable; 0 objectives without a supporter |
| Reused audit | `WARNINGS` (57 warnings), 0 blockers; closure readiness `FAIL` (carried) |
| Structure audit | 54/54 units pass the SOW_V1 production format; carried partition/tool-root issues |
| Dependency closure | 54 nodes, 103 edges, 0 SCCs, no accepted DAG; 2 schema-invalid (the two control folders) |
| Register validator | exit 1 on 36 `EVQ-006` only (EvidenceFile cells that resolve in none of the forms PR #1013 tries; revision 1–3 counted 595 under the older resolution); XRG skipped |
| Governed inputs vs basis | identical (`git diff` of `projects/chirality-app-dev` against the basis, this folder excluded) |

## Explicit exclusions

- Any change to `deliverable-contracts.ts`, `lib/lifecycle`, `lib/dependencies`, `lib/pipeline/pipeline-dispatch-contract.ts`, `lib/workspace/task-scope.ts`, `lib/workspace/filesystem.ts` (`scanProjectScopes`, `scanProjectDeliverables`), the MCP tools or the Runtime tool descriptors.
- `/api/project/deliverables`, `/api/working-root/{validate,tree,file,deliverable/content,workflow-drafts}` and all `/api/harness/*` routes. `GET /api/working-root/workflow` stays unless the owner chooses W-b.
- The `/` and `/chat` page URLs, and the `/workbench` and `/pipeline` URLs unless the owner chooses P-x.
- TYPES §4 legacy matrix vocabulary, persona aliases and the route/query compatibility semantics keyed with DEL-08-02 (their open TYPES §4 alignment stays with DEL-08-02).
- The versioned local-state schema. `WovenWorkspaceSurface` keeps `'workbench' | 'pipeline'` values, and existing keys stay readable (SPEC §17.8).
- The Work projection and the retained SDK-path modules that have no product importer at the basis. They are recorded as an observation (Impact Assessment §10.3) and are not proposed. `workflows-view.tsx` and `workflow-detail.tsx` are owner choice W.
- Every Runtime-owned surface. The Runtime scaffold API was retired by the Runtime loop in PR #1012; this amendment only aligns the App texts with that.
- CONTRACT invariant text and the companion register.
- Any lifecycle transition, release, publication, `_LATEST.md` movement, or closure of other open SCA-APP-011 work.
