"""SCA-APP-012 checkpoint-group-2 exact amendment, as data.

Each edit replaces one exact `old` substring (which must occur exactly once in
the file as it stands after the earlier edits to the same file) with `new`.
`seq` is the `ActionSeq` of `Amendment_Actions.csv`. `{APPLICATION_DATE}` is
the only acceptance-conditional slot. The group-3 candidate carries the prior
bytes; after group-3 acceptance the slot is filled with the date of the
group-3 decision folder `SCA-APP-012_GROUP-3_{YYYY-MM-DD}` and nowhere else.

Paths are repository-relative. The edits are written into the working tree
only by `build_amendment_preview.py --candidate` during checkpoint-group-3
preparation, after checkpoint group 2 is accepted (method.md, checkpoint group
3 preparation, step 1).

Register rows (ActionSeq) and the accepted intake rows they carry:
  1-22 = intake rows 1-22; 23 = intake row 26 (W-b, DEL-02-02);
  24 = intake row 27 (W-b, read-route carve-outs).
"""

APP = "projects/chirality-app-dev"
E = f"{APP}/execution"
D = f"{E}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
PRD = f"{APP}/docs/PRD.md"
SPEC = f"{APP}/docs/SPEC.md"
PLAN = f"{APP}/docs/PLAN.md"
P2 = f"{E}/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working"
P6 = f"{E}/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working"
P7 = f"{E}/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working"
P8 = f"{E}/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working"
SOW0201 = f"{P2}/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/ScopeOfWork.md"
SOW0202 = f"{P2}/DEL-02-02_Workbench_and_Pipeline_Selection_UX/ScopeOfWork.md"
SOW0203 = f"{P2}/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/ScopeOfWork.md"
SOW0603 = f"{P6}/DEL-06-03_Initial_Chirality_MCP_Read_Tools/ScopeOfWork.md"
SOW0702 = f"{P7}/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/ScopeOfWork.md"
SOW0703 = f"{P7}/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts/ScopeOfWork.md"
SOW0802 = f"{P8}/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract/ScopeOfWork.md"
SOW0803 = f"{P8}/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/ScopeOfWork.md"

ONTOLOGY = "## Deliverable Definition — Ontology\n"
RETIRED_ROUTES_012 = "`/api/working-root/scope` and `/api/working-root/workflow`"
OWNER_SCAFFOLD = "\"Scaffolding through the agent is enough.\""
RUNTIME_PR = ("PR #1012 (merge commit `49bbc9787238d59fe2945c8e9413206d554e56b7`; Runtime Receipt 5), as "
              "`execution/_Coordination/NOTICE_2026-09-27_RUNTIME_SCAFFOLD_API_RETIRED.md` records")

EDITS = [
    # ---------------------------------------------------------------- Row 1 DEL-02-01
    dict(id="E01", seq=1, file=SOW0201,
         old="2. Keep the existing loop-first and matrix UI reachable until separately\n",
         new="2. [RETIRED — SCA-APP-012] Keep the existing loop-first and matrix UI reachable until separately\n"),
    dict(id="E02", seq=1, file=SOW0201,
         old="5. Existing routes, queries, aliases, and the loop-first UI remain compatibility surfaces; the retired Workbench and Pipeline routes stay reachable by URL and unlisted (Q3).",
         new="5. Existing routes, queries, and aliases remain compatibility surfaces; the loop-first UI is retired by SCA-APP-012; the retired Workbench and Pipeline routes stay reachable by URL and unlisted (Q3)."),
    dict(id="E03", seq=1, file=SOW0201,
         old=ONTOLOGY,
         new=(
             "## SCA-APP-012 Current Contract (Controlling)\n\n"
             "SCA-APP-012 (owner direction 2026-09-27; DEC-027) is the separate owner decision that retires the "
             "loop-first compatibility UI. Where any earlier section or clause in this document keeps the loop-first "
             "UI, the matrix UI or the `?legacy=1` link reachable or as a compatibility surface, this section "
             "controls; the earlier text remains dated history and is not deleted.\n\n"
             "- Retired: the loop-first shell (`frontend/src/components/shell/loop-shell.tsx`, "
             "`portal-loop-shell.tsx`, `loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx` and "
             "`tertiary-sidebar-tabs.tsx`), the role-directory panel `frontend/src/components/portal/agent-matrix.tsx`, "
             "the discarded `legacy` prop of `WovenDialogueRoute`, and the discarded `?legacy=1` link (`legacyHref`) "
             "with its only test. None of them has rendered since 2026-09-09 (commit `9b005c23a`).\n"
             "- `/`, `/chat`, `/workbench` and `/pipeline` keep rendering the dialogue shell; `/workbench` and "
             "`/pipeline` stay reachable by URL and unlisted (D-APP-108 Q3). Existing routes, known query parameters, "
             "unknown-parameter preservation and aliases remain compatibility surfaces; `?legacy=1` is an ordinary "
             "unknown query parameter.\n"
             "- Obligation 2 of the SCA-APP-004 section is retired, and obligation 5 of the SCA-APP-010 section is "
             "restated there. The TYPES §4 route/query compatibility question stays keyed with DEL-08-02, unchanged.\n"
             "- Verification hooks: the hooks named in this document stay. "
             "`frontend/src/__tests__/components/woven-dialogue-route.test.tsx` covers the route surfaces without a "
             "`legacy` prop, and `frontend/src/__tests__/components/loop-tertiary-routes.test.ts` checks that "
             "`/workbench` and `/pipeline` open the dialogue shell.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 2 DEL-02-03 scope route + provider
    dict(id="E04", seq=2, file=SOW0203,
         old="> | Workspace APIs surfaced by this UI | `/api/working-root/validate`, `/api/working-root/tree`, `/api/working-root/scope`, `/api/project/deliverables` | `docs/SPEC.md` §17.2; `docs/PRD.md` §9.2 |",
         new="> | Workspace APIs surfaced by this UI | `/api/working-root/validate`, `/api/working-root/tree`, `/api/project/deliverables` ([RETIRED — SCA-APP-012] `/api/working-root/scope`) | `docs/SPEC.md` §17.2; `docs/PRD.md` §9.2 |"),
    dict(id="E05", seq=2, file=SOW0203,
         old=ONTOLOGY,
         new=(
             "## SCA-APP-012 Current Contract (Controlling)\n\n"
             "SCA-APP-012 (owner direction 2026-09-27; DEC-027) retires `GET /api/working-root/scope`, the "
             "unconsumed `DeliverablesProvider` (`frontend/src/components/workspace/deliverables-provider.tsx`) and "
             "DEL-02-03-REQ-009, and restates DEL-02-03-REQ-010. Where any earlier clause in this document names that "
             "route, deliverable-row routing to PIPELINE `TASK*`, dispatch preselection, route targets or route "
             "consumers, or status/dependency contract snapshots with transition controls, this section controls; "
             "the earlier clauses remain dated history and are not deleted.\n\n"
             "- The scope-scan surface this UI consumes is `/api/project/deliverables`, as DEL-08-03-REQ-010 already "
             "states. The scan library `scanProjectScopes` stays for the retained `scope_scan` tool contract "
             "(SPEC §14.2), and `frontend/src/lib/workspace/task-scope.ts` stays as a library.\n"
             "- DEL-02-03-REQ-009 is retired, with its verification row and the D-APP-56 R4-P29 launcher "
             "confirmation (CLM-015). No deliverable summary widget routes to a dispatch intent. DEL-08-03 keeps the "
             "TASK scope semantics (PRD FR-012, SOW-007); any later deliverable-row entry to a dispatch intent needs "
             "its own amendment.\n"
             "- DEL-02-03-REQ-010 is restated: deliverable summaries present lifecycle status read-only from "
             "`/api/project/deliverables` and carry no transition control. Transitions go through the lifecycle "
             "library (PRD FR-052 to FR-057). Dependency snapshots have no browser API (SCA-APP-011) and are read "
             "through the dependency library and tool contracts.\n"
             "- The other requirements, SOW-002 and SOW-003, OBJ-001 and OBJ-006, and the verification hooks are "
             "unchanged.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 3 DEL-02-03-REQ-010
    dict(id="E06", seq=3, file=SOW0203,
         old="> | DEL-02-03-REQ-010 | The UI shall consume status and dependency contract snapshots read-only where applicable; transition controls belong only where supported by the active workflow. | `docs/PRD.md` FR-010 |",
         new="> | DEL-02-03-REQ-010 | Deliverable summaries shall present lifecycle status read-only from `/api/project/deliverables` and carry no transition control; transitions go through the lifecycle library, and dependency snapshots are read through the dependency library and tool contracts, not a browser API (restated by SCA-APP-012; formerly sourced to the retired FR-010). | `docs/PRD.md` §9.2, FR-052 to FR-057 |"),
    dict(id="E07", seq=3, file=SOW0203,
         old="> | DEL-02-03-REQ-010 | Read-only contract snapshot rendering test; transition-control behavior TBD by owning workflow. |",
         new="> | DEL-02-03-REQ-010 | Rendering test that a deliverable summary shows the `status` returned by `/api/project/deliverables` read-only and offers no transition control (SCA-APP-012). |"),
    # ---------------------------------------------------------------- Row 4 DEL-07-03
    dict(id="E08", seq=4, file=SOW0703,
         old="ASSUMPTION: Scanner outputs should be consumable by `/api/working-root/scope` or adjacent working-root/project APIs without changing their public route shapes.",
         new="ASSUMPTION: Scanner outputs should be consumable by `/api/project/deliverables` or adjacent working-root/project APIs without changing their public route shapes (`/api/working-root/scope` is retired by SCA-APP-012)."),
    dict(id="E09", seq=4, file=SOW0703,
         old="Integration evidence for `/api/working-root/scope` or an accepted adjacent API, if scanner output is exposed there.",
         new="Integration evidence for `/api/project/deliverables` or an accepted adjacent API, if scanner output is exposed there (`/api/working-root/scope` is retired by SCA-APP-012)."),
    dict(id="E10", seq=4, file=SOW0703,
         old="> - If scanner results feed `/api/working-root/scope` or `/api/project/deliverables`, keep route shapes stable",
         new="> - If scanner results feed `/api/project/deliverables` (SCA-APP-012 retired `/api/working-root/scope`), keep route shapes stable"),
    # ---------------------------------------------------------------- Row 5 DEL-08-02
    dict(id="E11", seq=5, file=SOW0802,
         old="| `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` is compatibility evidence, not an active matrix acceptance check. |",
         new="| `frontend/src/__tests__/lib/persona-resolution.test.ts` carries the direct-entry registry case ported from the retired `agent-matrix-cells.test.ts` (SCA-APP-012: TASK is not direct-entry; HELP_HUMAN is the new-chat default); no matrix helper remains. |"),
    dict(id="E12", seq=5, file=SOW0802,
         old="| `frontend/src/__tests__/lib/guarded-session-selection.test.ts` and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`; live query-preservation and continuation/isolation verification remain open. |",
         new="| `frontend/src/__tests__/lib/guarded-session-selection.test.ts` and `frontend/src/__tests__/components/chat-panel-role-picker-guard.test.tsx` (the role picker is disabled while a turn runs; added by SCA-APP-012); live query-preservation and continuation/isolation verification remain open. |"),
    dict(id="E13", seq=5, file=SOW0802,
         old="| D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` Type 2 vocabulary | Negative alias resolver unit test and matrix guard test. |",
         new="| D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` Type 2 vocabulary | Negative alias resolver unit test in `persona-resolution.test.ts`, including the direct-entry registry case ported by SCA-APP-012. |"),
    dict(id="E14", seq=5, file=SOW0802,
         old="| D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` matrix vocabulary | Negative alias resolver unit test and matrix guard test. |",
         new="| D-APP-28 loop-first routing; D-APP-24 Type 0/1 direct-chat guard; `docs/TYPES.md` matrix vocabulary | Negative alias resolver unit test in `persona-resolution.test.ts`, including the direct-entry registry case ported by SCA-APP-012. |"),
    dict(id="E15", seq=5, file=SOW0802,
         old="`docs/PRD.md` FR-023; current loop-first shell contract |",
         new="`docs/PRD.md` FR-023; current dialogue-shell contract (the loop-first shell is retired by SCA-APP-012) |"),
    dict(id="E16", seq=5, file=SOW0802,
         old="if they change from the current loop-first launch contract.",
         new="if they change from the current dialogue-shell route/query contract (the loop-first launch contract is retired by SCA-APP-012)."),
    dict(id="E17", seq=5, file=SOW0802,
         old="> 16. Record the active loop-first route-state behavior for selected agent, row, and column.",
         new="> 16. Record the dialogue-shell route-state behavior for selected agent, row, and column (the loop-first route state is retired by SCA-APP-012)."),
    dict(id="E18", seq=5, file=SOW0802,
         old=ONTOLOGY,
         new=(
             "## SCA-APP-012 Current Contract (Controlling)\n\n"
             "SCA-APP-012 (owner direction 2026-09-27; DEC-027) retires the loop-first shell and the two "
             "`lib/portal` matrix helpers, `frontend/src/lib/portal/agent-matrix-cells.ts` and "
             "`frontend/src/lib/portal/agent-matrix-launch.ts`, with their tests. Where any earlier clause in this "
             "document names those helpers or their tests, a matrix guard test, the loop-first shell contract or "
             "loop-first route state as a current obligation, this section controls; the earlier clauses remain "
             "dated history and are not deleted. D-APP-28 citations stay as historical sources.\n\n"
             "- Aliases, persona resolution, guarded selection, the TYPES §4 route/query/alias semantics, "
             "SOW-005, SOW-006 and SOW-017, and the requirements are unchanged.\n"
             "- Aliases live in `frontend/src/lib/shell/persona-resolution.ts`, tested by "
             "`frontend/src/__tests__/lib/persona-resolution.test.ts`, which also carries the direct-entry registry "
             "case ported from `agent-matrix-cells.test.ts` (TASK is not direct-entry; HELP_HUMAN is the new-chat "
             "default; both read from `CHIRALITY_ROLES`).\n"
             "- The recorded-session guard lives in `frontend/src/lib/woven-dialogue/guarded-session-selection.ts` "
             "(`frontend/src/__tests__/lib/guarded-session-selection.test.ts`). The role picker in "
             "`frontend/src/components/shell/chat-panel.tsx` is disabled while a turn runs, tested by "
             "`frontend/src/__tests__/components/chat-panel-role-picker-guard.test.tsx` (added by the SCA-APP-012 "
             "code change).\n"
             "- `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts` keeps its role-boundary case, "
             "reading the three direct-entry roles from `CHIRALITY_ROLES`, and its dispatch case; its matrix-helper "
             "round-trip case is retired with the helpers.\n"
             "- Unknown-query-parameter preservation stays an open obligation, to be verified against the live "
             "dialogue-shell route.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 6 DEL-08-03
    dict(id="E19", seq=6, file=SOW0803,
         old="> | Working-root scope API | `/api/project/deliverables` scans deliverables and knowledge types for the active root. |",
         new="> | Deliverable scan API | `/api/project/deliverables` scans deliverables and knowledge types for the active root. |"),
    # ---------------------------------------------------------------- Row 7 SOW-001
    dict(id="E20", seq=7, file=D,
         old="The centre dialogue is never hidden, unmounted, or replaced; existing routes and the loop-first UI remain compatibility surfaces;",
         new="The centre dialogue is never hidden, unmounted, or replaced; existing routes remain compatibility surfaces and the loop-first UI is retired by SCA-APP-012;"),
    dict(id="E21", seq=7, file=D,
         old="| DEC-004; DEC-025; DEC-026 | FALSE | Existing routes and loop-first UI remain compatibility surfaces;",
         new="| DEC-004; DEC-025; DEC-026; DEC-027 | FALSE | Existing routes remain compatibility surfaces and the loop-first UI is retired (SCA-APP-012);"),
    # ---------------------------------------------------------------- Row 8 hard constraint (with Row 24)
    dict(id="E22", seq=8, file=D,
         old="`/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`.\n",
         new="`/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`; and the routes retired by SCA-APP-012: "
             + RETIRED_ROUTES_012 + ".\n"),
    # ---------------------------------------------------------------- Row 9 section 13 note
    dict(id="E23", seq=9, file=D,
         old="and any live registration of them is governed by DEL-06-04-REQ-010.\n- REVIEW should check",
         new="and any live registration of them is governed by DEL-06-04-REQ-010.\n"
             "- SCA-APP-012 retires the loop-first shell (the loop, portal and tertiary shells, their sidebar layout "
             "and tab factory, and the role-directory panel), the discarded `legacy` prop and `?legacy=1` link, the "
             "two `lib/portal` matrix helpers, `DeliverablesProvider`, `/api/working-root/scope`, and the unmounted "
             "flat-file workflow view with `/api/working-root/workflow`. It ends the loop-first compatibility period "
             "that the SCA-APP-004 note above preserves; that note stays as history. The `/workbench` and "
             "`/pipeline` URLs stay unlisted entries into the dialogue shell (D-APP-108 Q3). The scope-scan, "
             "task-scope, dispatch, lifecycle, dependency and scaffold libraries remain. DEL-02-03-REQ-009 is "
             "retired. No App-side scaffold entry and no write-capable scaffold tool is planned: execution roots are "
             "scaffolded by the agent through the Root `project-setup` workflow.\n"
             "- REVIEW should check"),
    # ---------------------------------------------------------------- Row 10 DEC-027 and Change Log
    dict(id="E24", seq=10, file=D,
         old="the Runtime-owned scaffold API is the Runtime loop's decision. |\n",
         new="the Runtime-owned scaffold API is the Runtime loop's decision. |\n"
             "| DEC-027 | 2026-09-27 | SCA-APP-012 retires the loop-first compatibility UI (its shells, role-directory "
             "panel, discarded `legacy` prop and `?legacy=1` link, and the `lib/portal` matrix helpers), "
             "`DeliverablesProvider`, `GET /api/working-root/scope`, the unmounted flat-file workflow view with "
             "`GET /api/working-root/workflow`, and DEL-02-03-REQ-009; it keeps the `/workbench` and `/pipeline` URLs "
             "as unlisted entries into the dialogue shell and records that no App-side scaffold entry is planned, "
             "without changing topology, scope-item mappings, context envelopes or lifecycle; it writes no "
             "dependency register (dependency re-extraction is a downstream handoff). | Ryan Tufts directed the "
             "change on 2026-09-27 and decided " + OWNER_SCAFFOLD + " The owner's SCA-APP-012 checkpoint decisions "
             "(R-b; W-b; P-keep; L-lib; S-tool; E no change) are recorded in its checkpoint snapshots. This is the "
             "separate owner decision on retiring the loop-first UI that D-APP-74, PRD §6.4 and KG-033 and SPEC "
             "§17.9 reserved; the Runtime loop retired its scaffold API in PR #1012. |\n"),
    dict(id="E25", seq=10, file=D,
         old="dependency registers (re-extraction is downstream), estimates, schedule, implementation authority, or release authority.\n\n---\n",
         new="dependency registers (re-extraction is downstream), estimates, schedule, implementation authority, or release authority.\n"
             "- 2026-09-27: SCA-APP-012 retired the loop-first compatibility UI, `DeliverablesProvider`, "
             "`/api/working-root/scope`, the flat-file workflow view with `/api/working-root/workflow`, and "
             "DEL-02-03-REQ-009, kept the `/workbench` and `/pipeline` URLs, and recorded that no App-side scaffold "
             "entry is planned, without changing package/deliverable topology, scope-item mappings, lifecycle, "
             "dependency registers (re-extraction is downstream), estimates, schedule, implementation authority, or "
             "release authority.\n\n---\n"),
    # ---------------------------------------------------------------- Row 11 telemetry
    dict(id="E26", seq=11, file=D,
         old="| Revision | v3.2 source-governed working surface amended by SCA-APP-011 |\n| Date | 2026-09-27 |\n",
         new="| Revision | v3.2 source-governed working surface amended by SCA-APP-012 |\n| Date | {APPLICATION_DATE} |\n",
         conditional=True),
    # ---------------------------------------------------------------- Row 12 PRD loop-first decision (with 14, 24)
    dict(id="E27", seq=12, file=PRD,
         old="Journeys 7.3 and 7.5, FR-010 to FR-013 and §9.1-9.2 revised; route-preservation clauses carry the exception\n",
         new="Journeys 7.3 and 7.5, FR-010 to FR-013 and §9.1-9.2 revised; route-preservation clauses carry the exception\n\n"
             "**Amended (SCA-APP-012):** owner direction 2026-09-27: the loop-first compatibility UI, "
             "`/api/working-root/scope` and `/api/working-root/workflow` retired; §3.1, §6.1, §6.3, §6.4, §7.2, §8.13, "
             "§9.2, FR-001, FR-007, FR-119, §12.1, §14 and KG-033 revised; the scaffold tool reads as the read-only "
             "preview\n"),
    dict(id="E28", seq=12, file=PRD,
         old="25. Preserve legacy routes, query parameters, aliases, matrix behavior, API/SSE contracts, provider composition, and the existing loop-first UI through a compatibility period. SCA-APP-011 records the owner's separate retirement of `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition`, `/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`.",
         new="25. Preserve legacy routes, query parameters, aliases, matrix behavior, API/SSE contracts, and provider composition through a compatibility period. SCA-APP-011 records the owner's separate retirement of `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition`, `/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`. SCA-APP-012 records the owner's separate retirement of the loop-first compatibility UI, "
             + RETIRED_ROUTES_012 + "."),
    dict(id="E29", seq=12, file=PRD,
         old="browser API shapes (apart from the four routes SCA-APP-011 retired), and the loop-first implementation through the Woven Dialogue compatibility period.",
         new="browser API shapes (apart from the four routes SCA-APP-011 retired and the two SCA-APP-012 retired, "
             + RETIRED_ROUTES_012 + ") through the Woven Dialogue compatibility period; SCA-APP-012 retires the loop-first implementation."),
    dict(id="E30", seq=12, file=PRD,
         old="SCA-APP-011 is the separate owner acceptance for the four routes it retires.\n",
         new="SCA-APP-011 is the separate owner acceptance for the four routes it retires. SCA-APP-012 is the separate owner acceptance for retiring the loop-first compatibility UI, "
             + RETIRED_ROUTES_012 + "; the loop-first UI had not rendered since 2026-09-09, and the packaged Desktop evidence for the dialogue shell stays open under KG-033.\n"),
    dict(id="E31", seq=12, file=PRD,
         old="and `/api/harness/scaffold` returned ENGINE_UNAVAILABLE in the shipped composition.",
         new="and `/api/harness/scaffold` returned ENGINE_UNAVAILABLE in the shipped composition. SCA-APP-012 retired the loop-first compatibility UI, which had not rendered since 2026-09-09, and "
             + RETIRED_ROUTES_012 + ", which had no caller; the packaged Desktop evidence for the dialogue shell stays open under KG-033."),
    dict(id="E32", seq=12, file=PRD,
         old="replay transcript-item rendering against a real daemon session, the mock-only `[data-legacy]` test contract, and recorded navigator presentation divergences.",
         new="replay transcript-item rendering against a real daemon session, and recorded navigator presentation divergences; the mock-only `[data-legacy]` test contract closes with the `legacy` prop (SCA-APP-012)."),
    dict(id="E33", seq=12, file=PRD,
         old="do not retire the existing legacy loop-first UI without a separate owner decision. |",
         new="SCA-APP-012 is the separate owner decision that retired the legacy loop-first UI. |"),
    # ---------------------------------------------------------------- Row 13 PRD live-shell text (with 24)
    dict(id="E34", seq=13, file=PRD,
         old="- A loop-first, chat-dominant compatibility shell across `/`, `/chat`, `/pipeline`, and `/workbench`; it is the live baseline, not the selected permanent target architecture.",
         new="- The Woven Dialogue shell across `/`, `/chat`, `/pipeline`, and `/workbench`; it has been the live baseline since 2026-09-09. The earlier loop-first, chat-dominant compatibility shell is retired by SCA-APP-012."),
    dict(id="E35", seq=13, file=PRD,
         old="6. Legacy route/query/alias/matrix launches remain available through the\n   compatibility period.\n",
         new="6. Legacy route/query/alias launches remain available through the\n   compatibility period; the matrix survives as the TYPES §4 route/query/alias\n   vocabulary and the persona resolver, not as a launch surface (SCA-APP-012).\n"),
    dict(id="E36", seq=13, file=PRD,
         old="Shared intent is not a stored UI object; existing routes and the loop-first UI remain compatibility surfaces until separately retired. |",
         new="Shared intent is not a stored UI object; existing routes remain compatibility surfaces until separately retired; the loop-first UI is retired by SCA-APP-012. |"),
    dict(id="E37", seq=13, file=PRD,
         old="| Legacy 3x4 matrix, route/query mappings, unavailable-persona behavior, and deep links remain compatible. |",
         new="| Route/query mappings, aliases, unavailable-persona behavior, and deep links remain compatible; the 3x4 matrix is presentation history and survives as TYPES §4 vocabulary, not as a launch surface (SCA-APP-012). |"),
    dict(id="E38", seq=13, file=PRD,
         old="- legacy routes, known and unknown query parameters, aliases/matrix behavior, browser APIs, SSE names/order, provider composition, security boundaries, and the existing UI remain compatible until separately retired;",
         new="- legacy routes, known and unknown query parameters, aliases/matrix behavior, browser APIs (apart from the routes retired by SCA-APP-011 and SCA-APP-012), SSE names/order, provider composition, and security boundaries remain compatible until separately retired; the loop-first UI is retired by SCA-APP-012;"),
    # ---------------------------------------------------------------- Row 14 PRD 9.2 scope route
    dict(id="E39", seq=14, file=PRD,
         old="| `/api/working-root/scope` | GET | Scan deliverables and knowledge-type directories. |\n",
         new=""),
    dict(id="E40", seq=14, file=PRD,
         old="\nSCA-APP-011 retired `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition` and `/api/working-root/deliverable/dependencies`. Lifecycle status read",
         new="\nSCA-APP-012 retired `/api/working-root/scope`. `/api/project/deliverables` is the scope-scan surface, and the scan library stays for the retained `scope_scan` tool contract.\n\n"
             "SCA-APP-011 retired `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition` and `/api/working-root/deliverable/dependencies`. Lifecycle status read"),
    # ---------------------------------------------------------------- Row 15 SPEC 17.2 / 17.9 scope route
    dict(id="E41", seq=15, file=SPEC,
         old="§17.3 drops the Workbench and Pipeline forms; §5.2 dependency-read wording\n",
         new="§17.3 drops the Workbench and Pipeline forms; §5.2 dependency-read wording\n"
             "**Amended (SCA-APP-012):** owner direction 2026-09-27: §17.2 retires `/api/working-root/scope`; §17.9 "
             "records the loop-first UI retirement; §14.2 narrows `mcp__chirality__scaffold` to the read-only preview\n"),
    dict(id="E42", seq=15, file=SPEC,
         old="| `/api/working-root/scope` | GET | Scan deliverables and knowledge types. |\n",
         new=""),
    dict(id="E43", seq=15, file=SPEC,
         old="\nSCA-APP-011 retired `/api/working-root/deliverable/status`,\n",
         new="\nSCA-APP-012 retired `/api/working-root/scope`. `/api/project/deliverables`\n"
             "is the scope-scan surface, and the scan library `scanProjectScopes` stays for\n"
             "the retained `scope_scan` tool contract (§14.2).\n\n"
             "SCA-APP-011 retired `/api/working-root/deliverable/status`,\n"),
    dict(id="E44", seq=15, file=SPEC,
         old="Browser API shapes in §17.1-17.2 (apart from the four routes SCA-APP-011\nretired), the event",
         new="Browser API shapes in §17.1-17.2 (apart from the four routes SCA-APP-011\nretired and `/api/working-root/scope`, retired by SCA-APP-012), the event"),
    # ---------------------------------------------------------------- Row 16 SPEC 17.9 loop-first
    dict(id="E45", seq=16, file=SPEC,
         old="architecture. The existing loop-first UI remains a compatibility\nimplementation until parity evidence and a separate owner retirement decision\nexist.\n",
         new="architecture. The loop-first UI, formerly kept as a compatibility\nimplementation until a separate owner retirement decision, is retired by\nSCA-APP-012, which is that decision; `/`, `/chat`, `/pipeline` and\n`/workbench` render the dialogue shell.\n"),
    # ---------------------------------------------------------------- Row 17 PLAN 3, R1, 13 (with 24)
    dict(id="E46", seq=17, file=PLAN,
         old="**Amended (SCA-APP-011):** owner direction 2026-09-27: baseline, compatibility and §13 entries record the retired forms and routes\n",
         new="**Amended (SCA-APP-011):** owner direction 2026-09-27: baseline, compatibility and §13 entries record the retired forms and routes\n"
             "**Amended (SCA-APP-012):** owner direction 2026-09-27: baseline, compatibility and §13 entries record the "
             "retired loop-first UI, `/api/working-root/scope` and `/api/working-root/workflow`\n"),
    dict(id="E47", seq=17, file=PLAN,
         old="public route/API/query shapes (apart from the four routes SCA-APP-011\nretired), provider composition, security boundaries, and the loop-first UI\nthrough the compatibility period.\n",
         new="public route/API/query shapes (apart from the four routes SCA-APP-011\nretired and `/api/working-root/scope` and `/api/working-root/workflow`,\nretired by SCA-APP-012), provider composition and security boundaries\nthrough the compatibility period. SCA-APP-012 retired the loop-first UI.\n"),
    dict(id="E48", seq=17, file=PLAN,
         old="- Route shapes and SSE event names are unchanged (SCA-APP-011 later retired `/api/harness/scaffold` and the three deliverable routes).",
         new="- Route shapes and SSE event names are unchanged (SCA-APP-011 later retired `/api/harness/scaffold` and the three deliverable routes, and SCA-APP-012 "
             + RETIRED_ROUTES_012 + ")."),
    dict(id="E49", seq=17, file=PLAN,
         old="keeps the lifecycle, dependency and scaffold libraries; rescopes DEL-02-02 without retiring it. |\n",
         new="keeps the lifecycle, dependency and scaffold libraries; rescopes DEL-02-02 without retiring it. |\n"
             "| `SCA-APP-012` | 2026-09-27 | Retires the loop-first compatibility UI (its shells, role-directory panel, "
             "discarded `legacy` prop and `?legacy=1` link, and the `lib/portal` matrix helpers), "
             "`DeliverablesProvider`, `GET /api/working-root/scope`, the unmounted flat-file workflow view with "
             "`GET /api/working-root/workflow`, and DEL-02-03-REQ-009; keeps the `/workbench` and `/pipeline` URLs as "
             "unlisted entries into the dialogue shell; records that no App-side scaffold entry is planned. |\n"),
    # ---------------------------------------------------------------- Row 18 PLAN live-shell text (with 24)
    dict(id="E50", seq=18, file=PLAN,
         old="- Live loop-first PORTAL, matrix, toolkit, file-tree, and replay surfaces; these remain the compatibility baseline while the owner-selected Woven Dialogue target is implemented and validated. SCA-APP-011 retired the WORKBENCH and PIPELINE forms.",
         new="- The Woven Dialogue shell with toolkit, file-tree, and replay surfaces is the live baseline on `/`, `/chat`, `/workbench` and `/pipeline` (since 2026-09-09). SCA-APP-011 retired the WORKBENCH and PIPELINE forms; SCA-APP-012 retired the loop-first PORTAL and matrix shell."),
    dict(id="E51", seq=18, file=PLAN,
         old="- Existing routes, queries, aliases/matrix behavior, APIs, SSE, provider composition, and old UI remain compatible until a separate owner retirement decision.",
         new="- Existing routes, queries, aliases/matrix behavior, APIs (apart from the routes SCA-APP-011 and SCA-APP-012 retired), SSE, and provider composition remain compatible until a separate owner retirement decision; SCA-APP-012 is that decision for the old loop-first UI."),
    dict(id="E52", seq=18, file=PLAN,
         old="   while keeping the provider composition and primary dialogue controller\n   singular.\n",
         new="   while keeping the provider composition and primary dialogue controller\n   singular. (History: the selection was removed on 2026-09-09, commit\n   `9b005c23a`, and SCA-APP-012 retired the loop-first side.)\n"),
    dict(id="E53", seq=18, file=PLAN,
         old="The existing loop-first UI remains the compatibility implementation after\nthis sequence until parity evidence is accepted and the owner separately\nauthorizes retirement.",
         new="After this sequence the existing loop-first UI remained the compatibility\nimplementation until the owner separately authorized retirement; SCA-APP-012\nrecords that authorization."),
    # ---------------------------------------------------------------- Row 19 DEL-07-02 (S)
    dict(id="E54", seq=19, file=SOW0702,
         old="The Runtime's own scaffold API (`/v1/projects/{id}/scaffold`, `ProjectScaffoldPort`) is Runtime-owned; the Runtime loop receives an informational notice with this amendment and decides on it.",
         new="The Runtime's own scaffold API (`/v1/projects/{id}/scaffold`, `ProjectScaffoldPort`) was Runtime-owned. On the owner's direction of 2026-09-27 (" + OWNER_SCAFFOLD + ") the Runtime loop retired it in " + RUNTIME_PR + " (SCA-APP-012)."),
    dict(id="E55", seq=19, file=SOW0702,
         old="- Follow-up (recorded, not scheduled): any later App-side scaffold entry, such as a Runtime application tool (a read-only preview under DEL-06-03; any write-capable scaffold registration under DEL-06-04-REQ-010) or a composed `ProjectScaffoldPort`, needs its own amendment and should default to `<project>/execution`, as `project-setup` does. The retained library accepts any execution root contained in the project.",
         new="- [RETIRED — SCA-APP-012] The follow-up for a later App-side scaffold entry is withdrawn. No App-side scaffold entry is planned: no App UI, HTTP, application-tool or Runtime-port entry, and no write-capable scaffold tool. Execution roots are scaffolded by the agent through the Root `project-setup` workflow into `<project>/execution`. The composed `ProjectScaffoldPort` option no longer exists, so any later App scaffold entry would need a Runtime amendment as well as an App one. The retained library accepts any execution root contained in the project, and the read-only scaffold preview stays under DEL-06-03."),
    dict(id="E56", seq=19, file=SOW0702,
         old="The live Runtime composition does not supply ProjectScaffoldPort.",
         new="The Runtime no longer has a `ProjectScaffoldPort` (retired in PR #1012; SCA-APP-012)."),
    dict(id="E57", seq=19, file=SOW0702,
         old="the live App-owned Runtime composition lacks its ProjectScaffoldPort, and SCA-APP-011 retired the App route that depended on it.",
         new="the Runtime retired its `ProjectScaffoldPort` in PR #1012 (SCA-APP-012), and SCA-APP-011 retired the App route that depended on it."),
    # ---------------------------------------------------------------- Row 20 DEL-06-03 CLM-031 (S)
    dict(id="E58", seq=20, file=SOW0603,
         old="and move any write-capable scaffold execution to the later governed write/path-hook surface.",
         new="and plan no write-capable scaffold tool: on the owner's direction of 2026-09-27 (" + OWNER_SCAFFOLD + "), execution roots are scaffolded by the agent through the Root `project-setup` workflow, and no App-side scaffold entry is planned (SCA-APP-012)."),
    # ---------------------------------------------------------------- Row 21 SPEC 14.2 and PRD scaffold tool (S-tool)
    dict(id="E59", seq=21, file=SPEC,
         old="| `mcp__chirality__scaffold` | Wrap scaffold service or dry-run preview. | Gated. |",
         new="| `mcp__chirality__scaffold` | Read-only scaffold preview (dry run); no write-capable scaffold tool is planned (SCA-APP-012). | Gated. |"),
    dict(id="E60", seq=21, file=PRD,
         old="17. Prefer in-process Chirality MCP tools for `_STATUS.md`, `Dependencies.csv`, scope scan, scaffold, and future deterministic Chirality adapters.",
         new="17. Prefer in-process Chirality MCP tools for `_STATUS.md`, `Dependencies.csv`, scope scan, scaffold preview, and future deterministic Chirality adapters."),
    dict(id="E61", seq=21, file=PRD,
         old="initially for status read/transition, dependency CSV read/write, scope scan, and scaffold.",
         new="initially for status read/transition, dependency CSV read/write, scope scan, and scaffold preview."),
    dict(id="E62", seq=21, file=PRD,
         old="Status read/transition, dependency CSV read/write, scope scan, and scaffold use `createSdkMcpServer()`",
         new="Status read/transition, dependency CSV read/write, scope scan, and scaffold preview use `createSdkMcpServer()`"),
    dict(id="E63", seq=21, file=PRD,
         old="2. Chirality status/dependency/scope/scaffold MCP tools.",
         new="2. Chirality status/dependency/scope/scaffold-preview MCP tools."),
    # ---------------------------------------------------------------- Row 22 DEL-02-03-REQ-009 (R-b)
    dict(id="E64", seq=22, file=SOW0203,
         old="> | Deliverable summary widgets | Present deliverable identity, status/dependency snapshots where available, and routeable deliverable rows for TASK workflows | `docs/PRD.md` §7.5; `docs/PRD.md` FR-010, FR-012 |",
         new="> | Deliverable summary widgets | Present deliverable identity and lifecycle status read-only from `/api/project/deliverables` (SCA-APP-012 retired the routeable deliverable rows for TASK workflows and moved dependency snapshots out of this UI) | `docs/PRD.md` §9.2; `docs/PRD.md` FR-052 to FR-057 |"),
    dict(id="E65", seq=22, file=SOW0203,
         old="> - Deliverable summary widgets sufficient for operator routing and read-only inspection.",
         new="> - Deliverable summary widgets sufficient for read-only inspection (operator routing retired by SCA-APP-012 with DEL-02-03-REQ-009)."),
    dict(id="E66", seq=22, file=SOW0203,
         old="> | DEL-02-03-REQ-009 | Deliverable summary widgets shall support routing",
         new="> | DEL-02-03-REQ-009 | [RETIRED — SCA-APP-012] Deliverable summary widgets shall support routing"),
    dict(id="E67", seq=22, file=SOW0203,
         old="shall drive deliverable identity in summary widgets and route targets. |",
         new="shall drive deliverable identity in summary widgets (route targets retired by SCA-APP-012 with DEL-02-03-REQ-009). |"),
    dict(id="E68", seq=22, file=SOW0203,
         old="> | DEL-02-03-REQ-009 | Routing test from deliverable row",
         new="> | DEL-02-03-REQ-009 | [RETIRED — SCA-APP-012] Routing test from deliverable row"),
    dict(id="E69", seq=22, file=SOW0203,
         old="> | DEL-02-03-REQ-013 | Rename/path-label fixture test confirming route identity uses stable deliverable ID. |",
         new="> | DEL-02-03-REQ-013 | Rename/path-label fixture test confirming summary identity uses stable deliverable ID (route targets retired by SCA-APP-012). |"),
    dict(id="E70", seq=22, file=SOW0203,
         old="Scope-scan/deliverable summary/status/dependency widgets are not demonstrated on the live shell; their exact carrier/compatibility obligations remain open,",
         new="Scope-scan and deliverable summary/status widgets are not demonstrated on the live shell; their exact carrier/compatibility obligations remain open (SCA-APP-012 retired the routing obligation and moved dependency snapshots out of this UI),"),
    dict(id="E71", seq=22, file=SOW0203,
         old="> R4-P29 confirms that the portal deliverable-rows launcher is within the existing DEL-02-03 REQ-009 claim.",
         new="> [RETIRED — SCA-APP-012: DEL-02-03-REQ-009 and the portal deliverable-rows launcher are retired; this confirmation is dated history.] R4-P29 confirms that the portal deliverable-rows launcher is within the existing DEL-02-03 REQ-009 claim."),
    dict(id="E72", seq=22, file=SOW0203,
         old="keep absent scope-scan/summary/route consumers visible as unresolved carrier work.",
         new="keep absent scope-scan/summary consumers visible as unresolved carrier work (route consumers retired by SCA-APP-012)."),
    dict(id="E73", seq=22, file=SOW0203,
         old="The missing scope-scan/summary/status/route consumers and their tests remain explicit delivery/alignment work.",
         new="The missing scope-scan/summary/status consumers and their tests remain explicit delivery/alignment work (route consumers retired by SCA-APP-012)."),
    dict(id="E74", seq=22, file=SOW0203,
         old="making filesystem project truth visible enough for routing and inspection while",
         new="making filesystem project truth visible enough for inspection (routing retired by SCA-APP-012) while"),
    dict(id="E75", seq=22, file=SOW0203,
         old="deliverable summaries and routing should key on deliverable IDs, not mutable labels or paths alone.",
         new="deliverable summaries should key on deliverable IDs, not mutable labels or paths alone (routing retired by SCA-APP-012)."),
    dict(id="E76", seq=22, file=SOW0203,
         old="Use paths for navigation context, but use stable IDs for identity and dispatch preselection. |",
         new="Use paths for navigation context, but use stable IDs for identity (dispatch preselection retired by SCA-APP-012 with DEL-02-03-REQ-009). |"),
    dict(id="E77", seq=22, file=SOW0203,
         old="Exact scope-scan/summary/route carriers and D-APP-121",
         new="Exact scope-scan/summary carriers (route carriers retired by SCA-APP-012) and D-APP-121"),
    dict(id="E78", seq=22, file=SOW0203,
         old="- **APP-R024:** Preserve scope scan, summary, status and route consumers alongside",
         new="- **APP-R024:** Preserve scope scan, summary and status consumers (route consumers retired by SCA-APP-012 with DEL-02-03-REQ-009; scope scan through `/api/project/deliverables`) alongside"),
    # ---------------------------------------------------------------- Row 23 DEL-02-02 (W-b)
    dict(id="E79", seq=23, file=SOW0202,
         old="6. If implementation review finds cross-domain churn between the coordination and workflow views, a split is proposed before the envelope widens (row split trigger).\n",
         new="6. If implementation review finds cross-domain churn between the coordination and workflow views, a split is proposed before the envelope widens (row split trigger).\n\n"
             "SCA-APP-012 record (no obligation changes): the unmounted flat-file workflow list "
             "`frontend/src/components/woven-dialogue/workflows-view.tsx` and `workflow-detail.tsx`, their test "
             "`woven-workflows.test.tsx`, and its read route `GET /api/working-root/workflow` are retired; the live "
             "Workflows view (`method-library-view.tsx`) carries obligation 3, and flat `.chirality/workflows/*.md` "
             "files stay readable as ordinary documents through the Files view.\n"),
    dict(id="E80", seq=23, file=SOW0202,
         old="and workflow/roadmap/proposal presentation versus current method-library/draft registration remain bounded source-alignment questions.",
         new="and workflow/roadmap/proposal presentation versus current method-library/draft registration (the flat-file workflow list is retired by SCA-APP-012) remain bounded source-alignment questions."),
]

# Register rows whose text is carried, in whole or in part, by an edit listed under another row.
# Row 24 (W-b read route) joins every clause the scope route joins; its text is in these edits.
CARRIED_BY = {24: ["E22", "E28", "E29", "E30", "E31", "E38", "E47", "E48", "E51"]}
