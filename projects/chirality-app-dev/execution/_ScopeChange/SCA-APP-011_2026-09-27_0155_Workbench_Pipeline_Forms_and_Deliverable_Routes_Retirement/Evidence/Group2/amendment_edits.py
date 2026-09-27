"""SCA-APP-011 checkpoint-group-2 exact amendment, as data.

Each edit replaces one exact `old` substring (which must occur exactly once in
the file as it stands after the earlier edits to the same file) with `new`.
`seq` is the `ActionSeq` of `Amendment_Actions.csv`. `{APPLICATION_DATE}` is
the only acceptance-conditional slot; it is filled with the date in the
heading of the group-3 `DECISION.md` (YYYY-MM-DD) and nowhere else.

Paths are repository-relative. Nothing here is applied before checkpoint
group 3 is accepted.
"""

APP = "projects/chirality-app-dev"
E = f"{APP}/execution"
D = f"{E}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
PRD = f"{APP}/docs/PRD.md"
SPEC = f"{APP}/docs/SPEC.md"
PLAN = f"{APP}/docs/PLAN.md"
P2 = f"{E}/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working"
P3 = f"{E}/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working"
P7 = f"{E}/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working"
P8 = f"{E}/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working"
P9 = f"{E}/PKG-09_Validation_Packaging_Security_and_Release/1_Working"
DEL0202 = f"{P2}/DEL-02-02_Workbench_and_Pipeline_Selection_UX"
DEL0203 = f"{P2}/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI"
DEL0303 = f"{P3}/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter"
DEL0702 = f"{P7}/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition"
DEL0704 = f"{P7}/DEL-07-04_Status_Transition_API_and_MCP_Tool"
DEL0705 = f"{P7}/DEL-07-05_Dependencies_csv_v3_1_Reader_Writer_and_Linter"
DEL0803 = f"{P8}/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch"
DEL0903 = f"{P9}/DEL-09-03_Unit_and_Integration_Test_Expansion"

ONTOLOGY = "## Deliverable Definition — Ontology\n"
TOOLS_M_A = (
    "The Chirality tool contracts that wrap this library (SPEC §14.2) run only on "
    "the retained SDK path today; their exposure through the Runtime "
    "application-tool interface is DEL-06-03's open work. On the Codex path an "
    "agent uses the Root tools (for example `tools/scaffolding/write_status.sh` "
    "and the dependency workflows) or edits the governed files directly."
)

EDITS = [
    # ---------------------------------------------------------------- Row 1 DEL-07-04
    dict(id="E01", seq=1, file=D,
         old="| Status parser; transition API/tool; approval SHA tests | SOW-028 |",
         new="| Status parser; transition library and tool; approval SHA tests | SOW-028 |"),
    dict(id="E02", seq=1, file=f"{DEL0704}/_CONTEXT.md",
         old="Status parser; transition API/tool; approval SHA tests",
         new="Status parser; transition library and tool; approval SHA tests"),
    dict(id="E03", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="> | API surface | `GET /api/working-root/deliverable/status` reads status; `POST /api/working-root/deliverable/status/transition` applies allowed transition. |",
         new="> | API surface | [RETIRED — SCA-APP-011] `GET /api/working-root/deliverable/status` and `POST /api/working-root/deliverable/status/transition` are retired; the status library in `frontend/src/lib/workspace/deliverable-contracts.ts` is the interface (SCA-APP-011 section). |"),
    dict(id="E04", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="`frontend/src/__tests__/lib/amendment-reopen-parity.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. They cover the gates",
         new="`frontend/src/__tests__/lib/amendment-reopen-parity.test.ts` and `frontend/src/__tests__/lib/deliverable-contracts.test.ts`. They cover the gates"),
    dict(id="E05", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="The Workbench and Pipeline forms take the `ruling` and `amendment` inputs (`frontend/src/__tests__/components/lifecycle-transition-gates.test.tsx`). The live caller",
         new="The Workbench and Pipeline forms that took the `ruling` and `amendment` inputs are retired with their test (SCA-APP-011). The live caller"),
    dict(id="E06", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="> Named verification hooks are `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. They check parser and transition behavior through the status API.",
         new="> Named verification hooks are `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/lib/deliverable-contracts.test.ts`. They check parser and transition behavior through the status library."),
    dict(id="E07", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="the lifecycle validator, and the status API routes. Retained MCP modules",
         new="the lifecycle validator, and the status library in `frontend/src/lib/workspace/deliverable-contracts.ts` (SCA-APP-011 retired the status API routes). Retained MCP modules"),
    dict(id="E08", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="`frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. As of 2026-09-26",
         new="`frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` (ported by SCA-APP-011 to `frontend/src/__tests__/lib/deliverable-contracts.test.ts`). As of 2026-09-26"),
    dict(id="E09", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="> | DEL-07-04-REQ-007 | The implementation SHALL expose",
         new="> | DEL-07-04-REQ-007 | [RETIRED — SCA-APP-011] The implementation SHALL expose"),
    dict(id="E10", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="> | DEL-07-04-REQ-008 | The implementation SHALL expose",
         new="> | DEL-07-04-REQ-008 | [RETIRED — SCA-APP-011] The implementation SHALL expose"),
    dict(id="E11", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="candidate-bound human approval, API responses, and applicable write protection. The parser and transition implementation evidence is `frontend/src/lib/lifecycle/status-parser.ts` and `frontend/src/lib/lifecycle/transition.ts`; named verification is `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`.",
         new="candidate-bound human approval, library results, and applicable write protection. The parser and transition implementation evidence is `frontend/src/lib/lifecycle/status-parser.ts` and `frontend/src/lib/lifecycle/transition.ts`; named verification is `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/lib/deliverable-contracts.test.ts`."),
    dict(id="E12", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old="> 6. Implement the status API surface.\n",
         new="> 6. [RETIRED — SCA-APP-011] Implement the status API surface. The HTTP routes below are retired; the status library is the interface (SCA-APP-011 section).\n"),
    dict(id="E13", seq=1, file=f"{DEL0704}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) retires the HTTP status routes "
             "`GET /api/working-root/deliverable/status` and `POST /api/working-root/deliverable/status/transition` "
             "and the client fetch functions that called them (`frontend/src/lib/workspace/deliverable-api.ts`). "
             "Where any earlier clause in this document names those routes, their route test or the Workbench and "
             "Pipeline forms, this section controls; the earlier clauses remain dated history and are not deleted.\n\n"
             "- The status read and transition interface is the library: `readDeliverableStatus` and "
             "`transitionDeliverableStatus` in `frontend/src/lib/workspace/deliverable-contracts.ts`, over "
             "`frontend/src/lib/lifecycle/`. " + TOOLS_M_A + "\n"
             "- DEL-07-04-REQ-007 and DEL-07-04-REQ-008 are retired. The other requirements are unchanged.\n"
             "- Verification hooks: `frontend/src/__tests__/lib/lifecycle-status.test.ts`, "
             "`frontend/src/__tests__/lib/amendment-reopen-parity.test.ts` and "
             "`frontend/src/__tests__/lib/deliverable-contracts.test.ts`. The last carries, against the library, "
             "every status read, transition, human-ruled `CHECKING -> IN_PROGRESS` reversal and "
             "`ISSUED -> IN_PROGRESS` reopening case formerly in the route test "
             "`frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts` (retired by SCA-APP-011), with each HTTP status "
             "expectation restated as the library's `WorkspaceValidationError` code and status. "
             "`frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` remains retained tool-contract evidence.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 2 DEL-07-05
    dict(id="E14", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old="with API/MCP integration, schema and lifecycle preservation",
         new="with library and Chirality tool integration, schema and lifecycle preservation"),
    dict(id="E15", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old="> | API surface | `/api/working-root/deliverable/dependencies` supports GET/PUT for `Dependencies.csv` snapshot rows |",
         new="> | API surface | [RETIRED — SCA-APP-011] `/api/working-root/deliverable/dependencies` is retired; the dependency library in `frontend/src/lib/workspace/deliverable-contracts.ts` is the interface (SCA-APP-011 section) |"),
    dict(id="E16", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old="> - Expose read/write behavior through the product dependency contract surface, including `/api/working-root/deliverable/dependencies` and Chirality MCP dependency tools.",
         new="> - Expose read/write behavior through the product dependency library (`frontend/src/lib/workspace/deliverable-contracts.ts`) and the Chirality dependency tool contracts; the `/api/working-root/deliverable/dependencies` route is retired (SCA-APP-011)."),
    dict(id="E17", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old="> | REQ-DEL-07-05-013 | The dependency API surface MUST support GET/PUT for `Dependencies.csv` snapshot rows at `/api/working-root/deliverable/dependencies`. | `docs/PRD.md` Section 17.2 |",
         new="> | REQ-DEL-07-05-013 | The dependency library MUST support read and write of `Dependencies.csv` snapshot rows through `readDeliverableDependencies` and `writeDeliverableDependencies` (restated by SCA-APP-011; the `/api/working-root/deliverable/dependencies` route is retired). | `docs/PRD.md` Section 8.9; SCA-APP-011 |"),
    dict(id="E18", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old="> | REQ-DEL-07-05-013 | GET/PUT contract, write failures and symlink handling; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. |",
         new="> | REQ-DEL-07-05-013 | Read/write contract, write failures and symlink handling; `frontend/src/__tests__/lib/deliverable-contracts.test.ts`. |"),
    dict(id="E19", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old=">    - Expose read/write behavior through `/api/working-root/deliverable/dependencies` GET/PUT.",
         new=">    - [RETIRED — SCA-APP-011] Expose read/write behavior through `/api/working-root/deliverable/dependencies` GET/PUT; the dependency library is the interface."),
    dict(id="E20", seq=2, file=f"{DEL0705}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) retires the HTTP route "
             "`GET/PUT /api/working-root/deliverable/dependencies` and the client fetch function that called it. "
             "Where any earlier clause names that route or its route test, this section controls; the earlier "
             "clauses remain dated history.\n\n"
             "- The dependency read and write interface is the library: `readDeliverableDependencies` and "
             "`writeDeliverableDependencies` in `frontend/src/lib/workspace/deliverable-contracts.ts`, over "
             "`frontend/src/lib/dependencies/`. " + TOOLS_M_A + "\n"
             "- REQ-DEL-07-05-013 is restated to the library. Its verification is "
             "`frontend/src/__tests__/lib/deliverable-contracts.test.ts`, which carries the dependency read, write, "
             "recorded-register, write-failure and symlink cases formerly in the route test.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 3 DEL-09-03
    dict(id="E21", seq=3, file=f"{DEL0903}/ScopeOfWork.md",
         old="> | API tests | `/api/harness/turn`, `/api/harness/interrupt`, `/api/working-root/deliverable/status`, and `/api/working-root/deliverable/dependencies` route tests where implemented. |",
         new="> | API tests | `/api/harness/turn` and `/api/harness/interrupt` route tests where implemented. Status and dependency behavior is tested at the library (`frontend/src/__tests__/lib/deliverable-contracts.test.ts`); SCA-APP-011 retired the status and dependency routes. |"),
    # ---------------------------------------------------------------- Row 4 DEL-08-03
    dict(id="E22", seq=4, file=D,
         old="| Dispatch contract tests; Pipeline selector tests; knowledge-type discovery; dynamic-scope and disabled-option handling | SOW-007, SOW-026 |",
         new="| Dispatch contract tests; task-scope selection tests; knowledge-type discovery; dynamic-scope and disabled-option handling | SOW-007, SOW-026 |"),
    dict(id="E23", seq=4, file=D,
         old="the contextual Pipeline presentation is retired from the active shell by SCA-APP-010 (code retained), so no active presentation consumer exists; any later consumer may not infer plans/tasks from conversational prose. |",
         new="the contextual Pipeline presentation is retired from the active shell by SCA-APP-010 and its code and tests by SCA-APP-011, so no presentation consumer exists; any later consumer may not infer plans/tasks from conversational prose. |"),
    dict(id="E24", seq=4, file=f"{DEL0803}/_CONTEXT.md",
         old="shell by SCA-APP-010 (code retained), so no active presentation consumer exists;",
         new="shell by SCA-APP-010 (its code and tests retired by SCA-APP-011), so no presentation consumer exists;"),
    dict(id="E25", seq=4, file=f"{DEL0803}/_CONTEXT.md",
         old="Dispatch contract tests; Pipeline selector tests; knowledge-type discovery;",
         new="Dispatch contract tests; task-scope selection tests; knowledge-type discovery;"),
    dict(id="E26", seq=4, file=f"{DEL0803}/_CONTEXT.md",
         old="presentation is retired from the active shell by SCA-APP-010 (DEC-025; code,\n  routes, and tests retained), so DEL-08-03's dispatch semantics have no",
         new="presentation is retired from the active shell by SCA-APP-010 (DEC-025) and its\n  code and tests by SCA-APP-011 (DEC-026), so DEL-08-03's dispatch semantics have no"),
    dict(id="E27", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="is retired from the active shell by SCA-APP-010 (code retained), so no active\npresentation consumer exists;",
         new="is retired from the active shell by SCA-APP-010 and its code and tests by\nSCA-APP-011, so no presentation consumer exists;"),
    dict(id="E28", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="Applied row outputs: Dispatch contract tests; Pipeline selector tests;",
         new="Applied row outputs: Dispatch contract tests; task-scope selection tests;"),
    dict(id="E29", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="2. The contextual Pipeline presentation is retired from the active shell by SCA-APP-010 (code retained); no active presentation consumer exists.",
         new="2. The contextual Pipeline presentation is retired from the active shell by SCA-APP-010, and its code and tests are retired by SCA-APP-011; no presentation consumer exists."),
    dict(id="E30", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="`frontend/src/__tests__/components/pipeline-surface.test.ts` is retained presentation/compatibility evidence; its existence does not establish an active shell consumer.",
         new="The Pipeline form test `frontend/src/__tests__/components/pipeline-surface.test.ts` is retired with the form (SCA-APP-011)."),
    dict(id="E31", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="The retained `frontend/src/components/pipeline/pipeline-surface.tsx` and its component tests provide compatibility presentation evidence under D-APP-108, not an active product-surface claim.",
         new="The former `frontend/src/components/pipeline/pipeline-surface.tsx` and its component tests are retired by SCA-APP-011."),
    dict(id="E32", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="> | DEL-08-03-REQ-012 | Selector tests shall cover pipeline selector behavior, knowledge-type discovery,",
         new="> | DEL-08-03-REQ-012 | Tests shall cover task-scope selection behavior at the dispatch-contract and task-scope level, knowledge-type discovery,"),
    dict(id="E33", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="re-hosted or contextual consumers owned by DEL-02-02 MUST use the same",
         new="any later contextual consumer MUST use the same"),
    dict(id="E34", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old=">\n> - Pipeline selector tests.\n> - Knowledge-type discovery tests.",
         new=">\n> - Task-scope selection tests (SCA-APP-011 retired the Pipeline selector tests).\n> - Knowledge-type discovery tests."),
    dict(id="E35", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="proving contextual Run/Workbench/Work-panel consumers preserve Pipeline taxonomy",
         new="proving any later contextual consumer preserves the dispatch taxonomy"),
    dict(id="E36", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old="Prove re-hosted Pipeline/Workbench and contextual Run controls consume",
         new="Prove any later contextual consumer uses"),
    dict(id="E37", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old=">\n> - Pipeline selector tests.\n> - Category-specific option-list source or fixture inventory.",
         new=">\n> - Task-scope selection tests.\n> - Category-specific option-list source or fixture inventory."),
    dict(id="E38", seq=4, file=f"{DEL0803}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) retires the Pipeline form code and tests "
             "(`frontend/src/components/pipeline/pipeline-surface.tsx`, "
             "`frontend/src/components/pipeline/lifecycle-gate-fields.tsx`, "
             "`frontend/src/__tests__/components/pipeline-surface.test.ts`). Where the SCA-APP-010 section or any "
             "earlier clause says the Pipeline code is retained or names Pipeline selector tests, this section "
             "controls; earlier clauses remain dated history.\n\n"
             "- Semantic ownership is unchanged: DECOMP/PREP/TASK/AUDIT lane semantics, dynamic task scope and "
             "disabled-option rules (`frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`, "
             "`frontend/src/lib/workspace/task-scope.ts`). No presentation consumer exists; any later consumer "
             "needs its own amendment.\n"
             "- Verification is at the dispatch-contract and task-scope level: "
             "`frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`, "
             "`frontend/src/__tests__/lib/task-scope-selection.test.ts`, "
             "`frontend/src/__tests__/api/project/deliverables-route.test.ts` and "
             "`frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 5 SOW-007
    dict(id="E39", seq=5, file=D,
         old="(presentation half retired by owner ruling; code, routes, and tests retained, not deleted); DEL-08-03 retains dispatch semantics;",
         new="(presentation half retired by owner ruling), and its code and tests are retired by SCA-APP-011; DEL-08-03 retains dispatch semantics;"),
    dict(id="E40", seq=5, file=D,
         old="| DEC-004; DEC-025 | FALSE | DEL-08-03 is semantic owner; the contextual Pipeline presentation is retired from the active shell (code retained), so no presentation consumer is mapped. |",
         new="| DEC-004; DEC-025; DEC-026 | FALSE | DEL-08-03 is semantic owner; the contextual Pipeline presentation is retired from the active shell and its code and tests by SCA-APP-011, so no presentation consumer is mapped. |"),
    # ---------------------------------------------------------------- Row 6 SOW-001
    dict(id="E41", seq=6, file=D,
         old="existing routes and the loop-first UI remain compatibility surfaces, and the retired `/workbench` and `/pipeline` routes remain reachable but unmounted from the active shell until separately ruled (Q3); shared intent is not a stored UI object. |",
         new="existing routes and the loop-first UI remain compatibility surfaces; the `/workbench` and `/pipeline` URLs remain reachable, unlisted entries into the dialogue shell (D-APP-108 Q3), and the Workbench and Pipeline forms are retired by SCA-APP-011; shared intent is not a stored UI object. |"),
    dict(id="E42", seq=6, file=D,
         old="| DEC-004; DEC-025 | FALSE | Existing routes and loop-first UI remain compatibility surfaces; retired Workbench/Pipeline routes stay reachable but unmounted pending Q3. |",
         new="| DEC-004; DEC-025; DEC-026 | FALSE | Existing routes and loop-first UI remain compatibility surfaces; the `/workbench` and `/pipeline` URLs stay reachable and unlisted (Q3); the Workbench and Pipeline forms are retired (SCA-APP-011). |"),
    # ---------------------------------------------------------------- Row 7 hard constraint (with Row 27)
    dict(id="E43", seq=7, file=D,
         old="- Browser-facing route shapes and SSE event names remain stable during the runtime pivot.\n",
         new="- Browser-facing route shapes and SSE event names remain stable during the runtime pivot, except the routes retired by SCA-APP-011: `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition`, `/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`.\n"),
    # ---------------------------------------------------------------- Row 8 section 13 note
    dict(id="E44", seq=8, file=D,
         old="proposals are human acts; the organisation layer is instruction root, not working root.\n",
         new="proposals are human acts; the organisation layer is instruction root, not working root.\n- SCA-APP-011 retires the Workbench and Pipeline forms and their tests, the deliverable status, status-transition and dependency HTTP routes with their client fetch functions, and `/api/harness/scaffold` with its client function; the Work projection stays unmounted. The lifecycle, dependency and scaffold libraries remain, and the Chirality tool contracts that wrap them await live Runtime exposure under DEL-06-03.\n"),
    # ---------------------------------------------------------------- Row 9 DEC-026 and Change Log
    dict(id="E45", seq=9, file=D,
         old="and ruled Q14's organisation-layer default. Root retains login-home, event-schema, and session-record semantics (OI-008); the direct shell items are owner-seated Remaining work, not decomposition scope. |\n",
         new="and ruled Q14's organisation-layer default. Root retains login-home, event-schema, and session-record semantics (OI-008); the direct shell items are owner-seated Remaining work, not decomposition scope. |\n"
             "| DEC-026 | 2026-09-27 | SCA-APP-011 retires the obsolete Workbench and Pipeline forms and their tests, the deliverable status, status-transition and dependency HTTP routes and their client fetch functions, and `POST /api/harness/scaffold` with its client function; it rescopes DEL-02-02 to its right-panel scope and names the lifecycle, dependency and scaffold libraries as the interfaces, without changing topology, scope-item mappings, context envelopes, lifecycle, or dependencies. | Ryan Tufts directed the retirement on 2026-09-27 and accepted SCA-APP-011 at its three checkpoints (DQ-R; set L excluded; D restate; S-c; E no change; M-a; scaffold library kept). The Chirality tool contracts remain retained SDK-path interfaces pending DEL-06-03; the Runtime-owned scaffold API is the Runtime loop's decision. |\n"),
    dict(id="E46", seq=9, file=D,
         old="changing the Scope Ledger from 80 to 84 rows without changing package/deliverable topology, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.\n",
         new="changing the Scope Ledger from 80 to 84 rows without changing package/deliverable topology, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.\n"
             "- 2026-09-27: SCA-APP-011 retired the Workbench and Pipeline forms, the three deliverable HTTP routes and `/api/harness/scaffold`, rescoped DEL-02-02, and named the lifecycle, dependency and scaffold libraries as the interfaces, without changing package/deliverable topology, scope-item mappings, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.\n"),
    # ---------------------------------------------------------------- Row 10 telemetry
    dict(id="E47", seq=10, file=D,
         old="| Revision | v3.2 source-governed working surface amended by SCA-APP-010 |\n| Date | 2026-09-04 |\n",
         new="| Revision | v3.2 source-governed working surface amended by SCA-APP-011 |\n| Date | {APPLICATION_DATE} |\n",
         conditional=True),
    # ---------------------------------------------------------------- Row 11 PRD 8.2
    dict(id="E48", seq=11, file=PRD,
         old="### 8.2 Dialogue Routing, Work/Agents Coordination, Workbench, and Pipeline\n",
         new="### 8.2 Dialogue Routing, Work/Agents Coordination, and Dispatch Semantics\n"),
    dict(id="E49", seq=11, file=PRD,
         old="| FR-010 | P1 | WORKBENCH shall consume deliverable contract APIs for read-only checks and permitted lifecycle transitions. | Status/dependency summaries load for selected deliverables; transition controls are disabled for unsupported agents. |",
         new="| FR-010 | P1 | [RETIRED — SCA-APP-011] WORKBENCH shall consume deliverable contract APIs for read-only checks and permitted lifecycle transitions. | Retired with the Workbench form and the deliverable routes; lifecycle and dependency behavior is FR-052 to FR-057. |"),
    dict(id="E50", seq=11, file=PRD,
         old="| FR-011 | P0 | Contextual PIPELINE shall expose presentation-neutral `DECOMP`, `PREP`, `TASK`, and `AUDIT` category controls. | Each category retains documented semantics; unsupported options are visible and disabled, and Coordination presentation does not become dispatch authority. |",
         new="| FR-011 | P0 | Presentation-neutral dispatch semantics shall define the `DECOMP`, `PREP`, `TASK`, and `AUDIT` categories (DEL-08-03); no Pipeline form presents them (SCA-APP-011). | Each category retains documented semantics; unsupported options are declared disabled and refused, and Coordination presentation does not become dispatch authority. |"),
    dict(id="E51", seq=11, file=PRD,
         old="| FR-012 | P0 | PIPELINE `TASK` shall retain split selectors for task agent and scope. |",
         new="| FR-012 | P0 | A `TASK` dispatch intent shall keep task agent and scope as separate fields. |"),
    dict(id="E52", seq=11, file=PRD,
         old="| FR-013 | P1 | Dynamic scope and projected Work state shall disclose",
         new="| FR-013 | P1 | Dynamic task scope and projected Work state shall disclose"),
    # ---------------------------------------------------------------- Row 12 PRD 9.2
    dict(id="E53", seq=12, file=PRD,
         old="| `/api/working-root/deliverable/status` | GET | Read `_STATUS.md` snapshot for a deliverable. |\n| `/api/working-root/deliverable/status/transition` | POST | Apply an allowed lifecycle transition. |\n| `/api/working-root/deliverable/dependencies` | GET/PUT | Read/write `Dependencies.csv` snapshot rows. |\n\n### 9.3 SSE Event Contract",
         new="\nSCA-APP-011 retired `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition` and `/api/working-root/deliverable/dependencies`. Lifecycle status read and transition and dependency read and write are served by the library in `frontend/src/lib/workspace/deliverable-contracts.ts` and by the Chirality tool contracts `status_read`, `status_transition`, `deps_read` and `deps_write` that wrap it. Those tools run only on the retained SDK path today; their exposure through the Runtime application-tool interface is DEL-06-03's open work.\n\n### 9.3 SSE Event Contract"),
    # ---------------------------------------------------------------- Row 13 PRD route preservation (with Row 28)
    dict(id="E54", seq=13, file=PRD,
         old="25. Preserve legacy routes, query parameters, aliases, matrix behavior, API/SSE contracts, provider composition, and the existing loop-first UI through a compatibility period.",
         new="25. Preserve legacy routes, query parameters, aliases, matrix behavior, API/SSE contracts, provider composition, and the existing loop-first UI through a compatibility period. SCA-APP-011 records the owner's separate retirement of `/api/working-root/deliverable/status`, `/api/working-root/deliverable/status/transition`, `/api/working-root/deliverable/dependencies` and `/api/harness/scaffold`."),
    dict(id="E55", seq=13, file=PRD,
         old="legacy aliases/matrix behavior, browser API shapes, and the loop-first implementation through the Woven Dialogue compatibility period.",
         new="legacy aliases/matrix behavior, browser API shapes (apart from the four routes SCA-APP-011 retired), and the loop-first implementation through the Woven Dialogue compatibility period."),
    dict(id="E56", seq=13, file=PRD,
         old="- Deleting or retiring the loop-first compatibility UI or any existing route before Woven Dialogue parity, accessibility, migration, performance, runtime regression, packaged Desktop proof, and separate owner acceptance.",
         new="- Deleting or retiring the loop-first compatibility UI or any existing route before Woven Dialogue parity, accessibility, migration, performance, runtime regression, packaged Desktop proof, and separate owner acceptance. SCA-APP-011 is the separate owner acceptance for the four routes it retires."),
    dict(id="E57", seq=13, file=PRD,
         old="20. Existing routes, queries, APIs, SSE, provider composition, runtime ownership, security controls, and the loop-first compatibility UI pass regression and packaged Desktop checks before any retirement decision.",
         new="20. Existing routes, queries, APIs, SSE, provider composition, runtime ownership, security controls, and the loop-first compatibility UI pass regression and packaged Desktop checks before any retirement decision. The four routes retired by SCA-APP-011 had no live caller besides the retired forms, and `/api/harness/scaffold` returned ENGINE_UNAVAILABLE in the shipped composition."),
    # ---------------------------------------------------------------- Row 14 PRD surfaces
    dict(id="E58", seq=14, file=PRD,
         old="provenance-bearing artifacts can be inspected inline or in focused views, and Workbench/Pipeline remain governed contextual surfaces.",
         new="provenance-bearing artifacts can be inspected inline or in focused views. SCA-APP-011 retired the Workbench and Pipeline forms."),
    dict(id="E59", seq=14, file=PRD,
         old="- Woven Dialogue GUI for human–agent collaboration, provenance-bearing inline/focused artifacts, and contextual Workbench/Pipeline work.",
         new="- Woven Dialogue GUI for human–agent collaboration and provenance-bearing inline/focused artifacts."),
    dict(id="E60", seq=14, file=PRD,
         old="- Disabled or unsupported variants remain visible as coming soon rather than silently disappearing.",
         new="- Unsupported dispatch variants remain declared as disabled in the DEL-08-03 dispatch contract and are refused rather than silently dropped."),
    dict(id="E61", seq=14, file=PRD,
         old="1. User enters Woven Dialogue directly or through a compatible WORKBENCH/persona deep link.\n2. The dialogue resolves persona aliases to instruction-file names while Workbench may appear as a contextual work view.",
         new="1. User enters Woven Dialogue directly or through a compatible persona deep link, including the `/workbench` URL.\n2. The dialogue resolves persona aliases to instruction-file names."),
    dict(id="E62", seq=14, file=PRD,
         old="- Inline/focused artifacts, Work/Agents selection, and Workbench/Pipeline presentation do not unmount or replace the primary live dialogue.",
         new="- Inline/focused artifacts and Work/Agents selection do not unmount or replace the primary live dialogue."),
    dict(id="E63", seq=14, file=PRD,
         old="### 7.5 Run an Operative Pipeline Intent\n\n1. User opens the contextual PIPELINE surface from Woven Dialogue or a compatible `/pipeline` deep link.\n2. User selects one of `DECOMP`, `PREP`, `TASK`, or `AUDIT`.\n3. User selects a category-specific agent or lane.\n4. For `TASK`, user selects scope mode and dynamic scope from the working root.\n5. User inspects deliverable status/dependency contract snapshots and may apply allowed lifecycle transitions.\n\nAcceptance:\n\n- Deliverable selections reset when the project root or scan results become stale.\n- `KNOWLEDGE_TYPES` mode is shown only when a knowledge decomposition marker is detected.\n- Lifecycle transitions enforce authorized actors and approval SHA requirements for human gate states.\n- Pipeline presentation does not convert conversational prose into a plan/task or transfer dispatch authority to the Coordination Panel.\n",
         new="### 7.5 Express an Operative Dispatch Intent\n\nSCA-APP-011 retired the Pipeline form; no App surface presents this journey. It states the DEL-08-03 dispatch semantics that any later consumer, or a compatible `/pipeline` deep link, must honor.\n\n1. An operative intent names one of `DECOMP`, `PREP`, `TASK`, or `AUDIT`.\n2. The intent names a category-specific agent or lane.\n3. For `TASK`, the intent names a scope mode and a dynamic scope from the working root.\n4. Lifecycle status and dependency snapshots are read, and allowed lifecycle transitions applied, through the lifecycle and dependency library (FR-052 to FR-057), not through a UI form.\n\nAcceptance:\n\n- Deliverable selections reset when the project root or scan results become stale.\n- `KNOWLEDGE_TYPES` mode is admitted only when a knowledge decomposition marker is detected.\n- Lifecycle transitions enforce authorized actors and approval SHA requirements for human gate states.\n- A dispatch intent does not convert conversational prose into a plan/task or transfer dispatch authority to the Coordination Panel.\n"),
    dict(id="E64", seq=14, file=PRD,
         old="7. Unsupported PIPELINE variants remain visible as disabled options, preserving operator awareness of roadmap scope, while deep links and dispatch semantics remain unchanged.",
         new="7. Unsupported dispatch variants remain declared as disabled options in the DEL-08-03 dispatch contract and are refused, while deep links and dispatch semantics remain unchanged."),
    dict(id="E65", seq=14, file=PRD,
         old="| Primary dialogue, inline/focused artifacts, Navigator, Work/Agents Coordination Panel, Activity Shelf, re-hosted WORKBENCH/PIPELINE/toolkit/settings, compatibility navigation, local UI state |",
         new="| Primary dialogue, inline/focused artifacts, Navigator, Work/Agents Coordination Panel, Activity Shelf, re-hosted toolkit/settings, compatibility navigation, local UI state (SCA-APP-011 retired the WORKBENCH/PIPELINE forms) |"),
    dict(id="E66", seq=14, file=PRD,
         old="legacy matrix compatibility, presentation-neutral Pipeline dispatch, Type 2 subagent governance and child records |",
         new="legacy matrix compatibility, presentation-neutral dispatch semantics, Type 2 subagent governance and child records |"),
    dict(id="E67", seq=14, file=PRD,
         old="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: daemon, admission, supplier, harness-port and SSE clauses revised to the application-owned Runtime service; Section 17 re-expressed; residency pilot retired\n",
         new="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: daemon, admission, supplier, harness-port and SSE clauses revised to the application-owned Runtime service; Section 17 re-expressed; residency pilot retired\n\n**Amended (SCA-APP-011):** owner direction 2026-09-27: the Workbench and Pipeline forms, the three deliverable routes and `/api/harness/scaffold` retired; Journeys 7.3 and 7.5, FR-010 to FR-013 and §9.1-9.2 revised; route-preservation clauses carry the exception\n"),
    # ---------------------------------------------------------------- Row 15 SPEC 17.2 and 17.9 (with Row 25)
    dict(id="E68", seq=15, file=SPEC,
         old="| `/api/working-root/deliverable/status` | GET | Read `_STATUS.md` snapshot. |\n| `/api/working-root/deliverable/status/transition` | POST | Apply allowed lifecycle transition. |\n| `/api/working-root/deliverable/dependencies` | GET/PUT | Read/write `Dependencies.csv`. |\n\n### 17.3 Woven Dialogue Physical UI Contract",
         new="\nSCA-APP-011 retired `/api/working-root/deliverable/status`,\n`/api/working-root/deliverable/status/transition` and\n`/api/working-root/deliverable/dependencies`. Lifecycle status read and\ntransition and dependency read and write are served by `readDeliverableStatus`,\n`transitionDeliverableStatus`, `readDeliverableDependencies` and\n`writeDeliverableDependencies` in `frontend/src/lib/workspace/deliverable-contracts.ts`\nand by the Chirality tool contracts `status_read`, `status_transition`,\n`deps_read` and `deps_write` (§14.2) that wrap them. Those tools run only on\nthe retained SDK path today; their exposure through the Runtime\napplication-tool interface is DEL-06-03's open work.\n`/api/working-root/deliverable/content` is unaffected.\n\n### 17.3 Woven Dialogue Physical UI Contract"),
    dict(id="E69", seq=15, file=SPEC,
         old="Browser API shapes in §17.1-17.2, the event representation",
         new="Browser API shapes in §17.1-17.2 (apart from the four routes SCA-APP-011\nretired), the event representation"),
    dict(id="E70", seq=15, file=SPEC,
         old="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: the browser event contract, harness-port and SSE clauses, release verification and §25 shared runtime revised to the application-owned Runtime service; residency subsections retired to history\n",
         new="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: the browser event contract, harness-port and SSE clauses, release verification and §25 shared runtime revised to the application-owned Runtime service; residency subsections retired to history\n**Amended (SCA-APP-011):** owner direction 2026-09-27: §17.1-17.2 retire the three deliverable routes and `/api/harness/scaffold`; §17.3 drops the Workbench and Pipeline forms; §5.2 dependency-read wording\n"),
    # ---------------------------------------------------------------- Row 16 SPEC 17.3
    dict(id="E71", seq=16, file=SPEC,
         old="6. re-hosted Workbench, Pipeline, toolkit, working-root, credential, runtime,\n   and settings controls under their existing semantic and security owners.\n",
         new="6. toolkit, working-root, credential, runtime, and settings controls under\n   their existing semantic and security owners. SCA-APP-011 retired the former\n   Workbench and Pipeline forms; lifecycle status, transition and dependency\n   rules are served by the library in\n   `frontend/src/lib/workspace/deliverable-contracts.ts` and the Chirality tool\n   contracts in §14.2, not by a UI form or an HTTP route.\n"),
    dict(id="E72", seq=16, file=SPEC,
         old="The primary live dialogue MUST remain mounted across inline/focused artifact,\nWork, Agents, Workbench, Pipeline, and compatibility-surface changes. Its",
         new="The primary live dialogue MUST remain mounted across inline/focused artifact,\nWork, Agents, and compatibility-surface changes. Its"),
    # ---------------------------------------------------------------- Row 17 SPEC 5.2 dependency reads
    dict(id="E73", seq=17, file=SPEC,
         old="App dependency reads (the working-root dependencies API, the MCP `deps_read`\ntool and the workbench and pipeline contract panels) compute blockers from the\n",
         new="App dependency reads (`readDeliverableDependencies` in\n`frontend/src/lib/workspace/deliverable-contracts.ts` and the retained\n`deps_read` tool that wraps it; SCA-APP-011 retired the working-root\ndependencies route and the Workbench and Pipeline contract panels) compute\nblockers from the\n"),
    dict(id="E74", seq=17, file=SPEC,
         old="absence of a blocker is still not a complete readiness judgment, and the panels\nstate this caveat beside the verdict.",
         new="absence of a blocker is still not a complete readiness judgment, and a reader\nthat presents the verdict states this caveat beside it."),
    # ---------------------------------------------------------------- Row 18 PLAN
    dict(id="E75", seq=18, file=PLAN,
         old="- Live loop-first PORTAL, WORKBENCH, PIPELINE, matrix, toolkit, file-tree, and replay surfaces; these remain the compatibility baseline while the owner-selected Woven Dialogue target is implemented and validated.",
         new="- Live loop-first PORTAL, matrix, toolkit, file-tree, and replay surfaces; these remain the compatibility baseline while the owner-selected Woven Dialogue target is implemented and validated. SCA-APP-011 retired the WORKBENCH and PIPELINE forms."),
    dict(id="E76", seq=18, file=PLAN,
         old="- Deliverable status and dependency APIs.\n",
         new="- Deliverable status and dependency library (`frontend/src/lib/workspace/deliverable-contracts.ts`); SCA-APP-011 retired its HTTP routes.\n"),
    dict(id="E77", seq=18, file=PLAN,
         old="public route/API/query shapes, provider composition, security boundaries, and\nthe loop-first UI through the compatibility period.",
         new="public route/API/query shapes (apart from the four routes SCA-APP-011\nretired), provider composition, security boundaries, and the loop-first UI\nthrough the compatibility period."),
    dict(id="E78", seq=18, file=PLAN,
         old="and strict primary-dialogue/read-only-replay separation. |\n",
         new="and strict primary-dialogue/read-only-replay separation. |\n| `SCA-APP-011` | 2026-09-27 | Retires the obsolete Workbench and Pipeline forms and their tests, the deliverable status, status-transition and dependency HTTP routes with their client fetch functions, and `POST /api/harness/scaffold` with its client function; keeps the lifecycle, dependency and scaffold libraries; rescopes DEL-02-02 without retiring it. |\n"),
    dict(id="E79", seq=18, file=PLAN,
         old="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: the D-APP-73 shared-runtime order and SCA-APP-003 effects are read with the application-owned Runtime service; residency steps retired\n",
         new="**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: the D-APP-73 shared-runtime order and SCA-APP-003 effects are read with the application-owned Runtime service; residency steps retired\n**Amended (SCA-APP-011):** owner direction 2026-09-27: baseline, compatibility and §13 entries record the retired forms and routes\n"),
    # ---------------------------------------------------------------- Row 19 DEL-02-03
    dict(id="E80", seq=19, file=f"{DEL0203}/ScopeOfWork.md",
         old="Scope-scan/deliverable-routing examples from the old Pipeline surface remain unverified current compatibility obligations, not live observations.",
         new="Scope-scan/deliverable-routing examples from the old Pipeline surface are withdrawn with the form (SCA-APP-011) and are not compatibility obligations."),
    # ---------------------------------------------------------------- Row 20 DEL-02-02 (DQ-R)
    dict(id="E81", seq=20, file=D,
         old="Workbench and Pipeline are retired from the active shell (code, routes, and tests retained) and the Work projection is unmounted until an explicitly recorded plan/task source exists. |",
         new="The Workbench and Pipeline forms are retired (SCA-APP-010 unmounted them; SCA-APP-011 retired their code and tests) and the Work projection is unmounted until an explicitly recorded plan/task source exists. |"),
    dict(id="E82", seq=20, file=f"{DEL0202}/_CONTEXT.md",
         old="`proposal.*` events. Workbench and Pipeline are retired from the active shell\n(code, routes, and tests retained) and the Work projection is unmounted until an\n",
         new="`proposal.*` events. The Workbench and Pipeline forms are retired (SCA-APP-010\nunmounted them; SCA-APP-011 retired their code and tests) and the Work projection\nis unmounted until an\n"),
    dict(id="E83", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="`proposal.*` events. Workbench and Pipeline are retired from the active shell\n(code, routes, and tests retained) and the Work projection is unmounted until an\n",
         new="`proposal.*` events. The Workbench and Pipeline forms are retired (SCA-APP-010\nunmounted them; SCA-APP-011 retired their code and tests) and the Work projection\nis unmounted until an\n"),
    dict(id="E84", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="1. The primary dialogue is invariant; Workbench and Pipeline are unmounted from the active shell with code, routes, and tests retained and the routes reachable by URL (Q3);",
         new="1. The primary dialogue is invariant; the Workbench and Pipeline forms are retired (SCA-APP-011) and the `/workbench` and `/pipeline` URLs stay reachable and unlisted (Q3);"),
    dict(id="E85", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="## SCA-APP-004 Gate-5 Current Contract (Controlling until SCA-APP-010)\n",
         new="## SCA-APP-004 Gate-5 Current Contract (Controlling until SCA-APP-010)\n\n> [RETIRED — SCA-APP-011] The Workbench and Pipeline re-hosting and obligation 4 of this section are retired with the forms; the section remains dated history.\n"),
    dict(id="E86", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="### CLM-010 — Requirements\n",
         new="### CLM-010 — Requirements [RETIRED — SCA-APP-011; history only]\n"),
    dict(id="E87", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="### CLM-014 — D-APP-56 PIPELINE surface amendment (2026-07-12)\n",
         new="### CLM-014 — D-APP-56 PIPELINE surface amendment (2026-07-12) [RETIRED — SCA-APP-011; history only]\n"),
    dict(id="E88", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old="Current hooks: frontend/src/__tests__/components/woven-dialogue-shell.test.tsx and woven-dialogue-controls.test.tsx, with workspace-deliverable-api.test.ts for the read-only contract.",
         new="Current hooks: frontend/src/__tests__/components/woven-dialogue-shell.test.tsx and woven-dialogue-controls.test.tsx; the read-only contract test workspace-deliverable-api.test.ts is retired with its client module (SCA-APP-011)."),
    dict(id="E89", seq=20, file=f"{DEL0202}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) rescopes this deliverable. The Workbench and "
             "Pipeline forms and their tests are retired, and this deliverable keeps its right-panel scope unchanged "
             "(SOW-006, SOW-081, SOW-082; OBJ-001, OBJ-007; name, ID, folder and envelope unchanged). Where any "
             "earlier section or clause disagrees, this section controls; earlier sections remain dated history and "
             "are not deleted.\n\n"
             "- Obligation 1 of the SCA-APP-010 section is restated there. Obligations 2 to 6 are unchanged.\n"
             "- [RETIRED — SCA-APP-011] The Workbench and Pipeline content of CLM-003, CLM-004, CLM-005, CLM-008 to "
             "CLM-010 (including DEL-02-02-REQ-001 to DEL-02-02-REQ-011), CLM-012 to CLM-014, CLM-016, CLM-019 and "
             "CLM-023 to CLM-027 is history only; none of it is a current obligation.\n"
             "- Retired code and tests: `frontend/src/components/workbench/workbench-surface.tsx`, "
             "`frontend/src/components/pipeline/pipeline-surface.tsx`, "
             "`frontend/src/components/pipeline/lifecycle-gate-fields.tsx`, their tests "
             "(`workbench-surface.test.ts`, `pipeline-surface.test.ts`, `lifecycle-transition-gates.test.tsx`), "
             "and the client module `frontend/src/lib/workspace/deliverable-api.ts` with "
             "`frontend/src/__tests__/lib/workspace-deliverable-api.test.ts`.\n"
             "- Current right-panel verification hooks are those in CLM-018.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 21 DEL-07-02 (S-c)
    dict(id="E90", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> | Runtime surface | `/api/harness/scaffold` must provide scaffolding through the App-owned Runtime service; the missing ProjectScaffoldPort composition and resulting 501 remain open. |",
         new="> | Runtime surface | [RETIRED — SCA-APP-011] `/api/harness/scaffold` is retired; the App has no HTTP or UI scaffold entry (SCA-APP-011 section). |"),
    dict(id="E91", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="This lift neither retires scaffolding nor claims that a module test repairs the live gap.",
         new="This lift neither retires scaffolding nor claims that a module test repairs the live gap. SCA-APP-011 later retired the App route; see its section."),
    dict(id="E92", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> - Support the `/api/harness/scaffold` runtime route or its backend service layer.",
         new="> - Provide the backend scaffold service layer (`frontend/src/lib/harness/scaffold.ts`); the `/api/harness/scaffold` route is retired (SCA-APP-011)."),
    dict(id="E93", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> | DEL-07-02-REQ-009 | The scaffold route MUST expose",
         new="> | DEL-07-02-REQ-009 | [RETIRED — SCA-APP-011] The scaffold route MUST expose"),
    dict(id="E94", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> 1. Scaffold route API test for `POST /api/harness/scaffold`.",
         new="> 1. [RETIRED — SCA-APP-011] Scaffold route API test for `POST /api/harness/scaffold`."),
    dict(id="E95", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> - API contract notes for `/api/harness/scaffold`.",
         new="> - [RETIRED — SCA-APP-011] API contract notes for `/api/harness/scaffold`."),
    dict(id="E96", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="the live App-owned Runtime composition lacks its ProjectScaffoldPort.",
         new="the live App-owned Runtime composition lacks its ProjectScaffoldPort, and SCA-APP-011 retired the App route that depended on it."),
    dict(id="E97", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old=">    - Run API route tests for `POST /api/harness/scaffold`.",
         new=">    - [RETIRED — SCA-APP-011] Run API route tests for `POST /api/harness/scaffold`."),
    dict(id="E98", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> | API route | `POST /api/harness/scaffold` invokes scaffold behavior and returns summary payload. | DEL-07-02-REQ-009 |",
         new="> | API route | [RETIRED — SCA-APP-011] `POST /api/harness/scaffold` invokes scaffold behavior and returns summary payload. | DEL-07-02-REQ-009 |"),
    dict(id="E99", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="> - Source code for scaffold parser/service and route integration.",
         new="> - Source code for the scaffold parser and service (route integration retired by SCA-APP-011)."),
    dict(id="E100", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="Keep `/api/harness/scaffold` thin and place behavior in a reusable scaffold service, consistent with PRD route principles.",
         new="Place behavior in a reusable scaffold service (the `/api/harness/scaffold` route is retired by SCA-APP-011)."),
    dict(id="E101", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old="Identify the live handoff and repair/prove the gap before claiming scaffold delivery.",
         new="Identify the live handoff and repair/prove the gap before claiming scaffold delivery. Closed by SCA-APP-011: the App scaffold route is retired, so no App live scaffold operation remains to repair."),
    dict(id="E102", seq=21, file=f"{DEL0702}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) retires the App HTTP scaffold entry "
             "`POST /api/harness/scaffold`, its client function `scaffoldHarnessExecutionRoot` and the App-side "
             "`scaffold` member of `DaemonHarnessPort`. Where any earlier clause names that route, its route test or a "
             "live App scaffold operation, this section controls; the earlier clauses remain dated history.\n\n"
             "- DEL-07-02 keeps SOW-024 and SOW-025 and the scaffold library `frontend/src/lib/harness/scaffold.ts` "
             "(`scaffoldExecutionRoot`, `previewScaffoldExecutionRoot`) with "
             "`frontend/src/__tests__/lib/harness-scaffold.test.ts`. The library's parser, layout, idempotence, "
             "fail-fast and path-policy requirements are unchanged.\n"
             "- DEL-07-02-REQ-009 is retired. The App has no UI or HTTP scaffold entry. Execution roots are "
             "scaffolded by the Root `project-setup` workflow into `<project>/execution` with the packaged "
             "`tools/scaffolding` scripts, run by an agent under the user's approval and sandbox policy.\n"
             "- APP-R058 is closed by removal: no App live scaffold operation remains to repair. The Runtime's own "
             "scaffold API (`/v1/projects/{id}/scaffold`, `ProjectScaffoldPort`) is Runtime-owned; the Runtime loop "
             "receives an informational notice with this amendment and decides on it.\n"
             "- Follow-up (recorded, not scheduled): any later App-side scaffold entry, such as a Runtime "
             "application tool under DEL-06-03 or a composed `ProjectScaffoldPort`, needs its own amendment and "
             "should default to `<project>/execution`, as `project-setup` does. The retained library accepts any "
             "execution root contained in the project.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 22 DEL-03-03 (S-c)
    dict(id="E103", seq=22, file=D,
         old="| Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services. |",
         new="| Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services; `/api/harness/scaffold` is retired by SCA-APP-011. |"),
    dict(id="E104", seq=22, file=f"{DEL0303}/ScopeOfWork.md",
         old="> | `/api/harness/scaffold` | POST | TBD | TBD | TBD | TBD |",
         new="> | `/api/harness/scaffold` | POST | [RETIRED — SCA-APP-011] | — | — | — |"),
    dict(id="E105", seq=22, file=f"{DEL0303}/ScopeOfWork.md",
         old=ONTOLOGY,
         new=(
             "## SCA-APP-011 Current Contract (Controlling)\n\n"
             "SCA-APP-011 (owner direction 2026-09-27; DEC-026) retires `POST /api/harness/scaffold` and its client "
             "function `scaffoldHarnessExecutionRoot`. It is no longer a supported route, and the route compatibility "
             "obligations in this document do not cover it. Every other `/api/harness/*` route and the browser SSE "
             "event names are unchanged.\n\n"
             + ONTOLOGY)),
    # ---------------------------------------------------------------- Row 23 PRD 9.1 (S-c)
    dict(id="E106", seq=23, file=PRD,
         old="| `/api/harness/scaffold` | POST | Scaffold execution root from decomposition markdown. |\n\nCompatibility requirement:\n\n- Existing `/api/harness/*` route shapes remain stable; under D-GOV-43",
         new="\nSCA-APP-011 retired `POST /api/harness/scaffold` (Journey 7.3).\n\nCompatibility requirement:\n\n- Existing `/api/harness/*` route shapes remain stable, except `/api/harness/scaffold`, retired by SCA-APP-011; under D-GOV-43"),
    # ---------------------------------------------------------------- Row 24 PRD 7.3 (S-c)
    dict(id="E107", seq=24, file=PRD,
         old="4. App stores the selected root as local UI state and uses it for file tree, scan, chat session, scaffold, and contract APIs.",
         new="4. App stores the selected root as local UI state and uses it for file tree, scan, chat session, and document views."),
    dict(id="E108", seq=24, file=PRD,
         old="1. User selects a working root.\n2. User opens PIPELINE.\n3. User enters a decomposition markdown path and coordination mode.\n4. App calls `POST /api/harness/scaffold`.\n5. Runtime parses package/deliverable tables, creates tool roots, copies decomposition, writes `INIT.md`, writes `_Coordination/_COORDINATION.md`, creates packages and deliverable folders, and returns validation summaries.\n",
         new="1. User selects a working root.\n2. User asks an agent in the chat to run the `project-setup` workflow (for example WORKING_ITEMS, `INITIAL` mode) with a decomposition markdown path and coordination mode.\n3. The agent scaffolds into `<project>/execution` with the packaged Root scaffolding tools (`scaffold_tool_root.sh`, `scaffold_package.sh`, `scaffold_deliverable.sh`, `write_status.sh`) under the user's approval and sandbox policy, and stops at the workflow's human scaffold gate.\n4. The workflow creates tool roots, copies the decomposition, writes `INIT.md` and `_Coordination/_COORDINATION.md`, creates package and deliverable folders, and reports validation summaries.\n\nSCA-APP-011 retired the App HTTP entry `POST /api/harness/scaffold` and its Pipeline form. The App scaffold library (`frontend/src/lib/harness/scaffold.ts`) remains, without an App UI or HTTP entry.\n"),
    dict(id="E109", seq=24, file=PRD,
         old="2. A decomposition markdown can be used to scaffold a SPEC-conformant execution root without manual folder creation.",
         new="2. A decomposition markdown can be used to scaffold a SPEC-conformant execution root without manual folder creation, through the `project-setup` workflow and its packaged scaffolding tools (Journey 7.3)."),
    # ---------------------------------------------------------------- Row 25 SPEC 17.1 (S-c)
    dict(id="E110", seq=25, file=SPEC,
         old="| `/api/harness/scaffold` | POST | Scaffold execution root from decomposition markdown. |\n",
         new=""),
    dict(id="E111", seq=25, file=SPEC,
         old="Existing route shapes remain stable during adapter adoption and TurnEngine extraction.",
         new="Existing route shapes remain stable during adapter adoption and TurnEngine extraction, except `POST /api/harness/scaffold`, retired by SCA-APP-011."),
    # ---------------------------------------------------------------- Row 26 PLAN (S-c)
    dict(id="E112", seq=26, file=PLAN,
         old="- Execution-root scaffolding.\n",
         new="- Execution-root scaffolding library (`frontend/src/lib/harness/scaffold.ts`); SCA-APP-011 retired its App HTTP entry, and execution roots are scaffolded through the Root `project-setup` workflow and its packaged tools.\n"),
    dict(id="E113", seq=26, file=PLAN,
         old="- Route shapes and SSE event names are unchanged.\n",
         new="- Route shapes and SSE event names are unchanged (SCA-APP-011 later retired `/api/harness/scaffold` and the three deliverable routes).\n"),
    # Row 27 (hard constraint, scaffold) and Row 28 (PRD route preservation, scaffold) are carried by
    # E43 and E54-E57, whose text names `/api/harness/scaffold` together with the three deliverable routes.
]

# Register rows whose text is carried by an edit listed under another row.
CARRIED_BY = {27: ["E43"], 28: ["E54", "E55", "E56", "E57"]}
