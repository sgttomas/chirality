# PREGATHER — DEL-06-03 Initial Chirality MCP Read Tools

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-06. Read-only evidence map against the frozen tree
(`00115c719`). No dispositions, alignment judgments, or ledger rows. REACH tags come from
`R2/PKG-06/EVIDENCE_PACK/REACHABILITY.csv`; none of the code paths below appears in `TOUCHED_PATHS.csv`
(so no `TOUCHED` flags). Test files carry no REACH row; their TestCount is from `VERIFICATION_INDEX.csv`.

## Deliverable key files (frozen tree)

Folder: `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/`

| File | Bytes |
|---|---|
| ScopeOfWork.md | 41161 |
| _SEMANTIC.md | 47997 |
| _SEMANTIC_LENSING.md | 31068 |
| _DEPENDENCIES.md | 24106 |
| Dependencies.csv | 18292 |
| Assessment_INSP-03_DEL-06-03.md | 7258 |
| _STATUS.md | 6106 |
| _REFERENCES.md | 4481 |
| _CONTEXT.md | 3166 |
| MEMORY.md | 2918 |
| _run_records/ | 12 run records (2026-05-20 … 2026-09-05) |

`_STATUS.md`: Current State IN_PROGRESS; one Remaining item DEL-06-03-V3-01 (`propose` tool, NOT_SELECTABLE_UNTIL DEL-02-02-V3-04).

**Decision IDs cited most** (ScopeOfWork + _STATUS + _CONTEXT counts): D-APP-38 (18), D-APP-56 (6), SCA-APP-010 (5), D-APP-68 (5), SCA-APP-001 (3), D-APP-55 (3), D-APP-54 (2), D-APP-19 (2), D-APP-108 (2); single mentions D-APP-80, D-APP-72, SCA-APP-002.

**Main code areas** (IMPLEMENTATION_SURFACES Area):
- HARNESS — `frontend/src/lib/harness/mcp/read-tools.ts` (1280 LOC), `mcp/coordination-tools.ts` (364), `sdk-options-builder.ts` (258), `tool-pool.ts` (112), `permission-overlay.ts` (494), `tool-evidence.ts`, `tool-path-policy.ts`, `session-events.ts`, `scaffold.ts` (954).
- WORKSPACE — `frontend/src/lib/workspace/deliverable-contracts.ts` (558), `workspace/filesystem.ts` (1302).
- RTCONTRACT — `chirality-runtime/packages/contracts/src/harness/mcp/tool-names.ts` (70), `tool-descriptor.ts` (1401), `tool-catalog.ts` (159).
- BUILD — `frontend/scripts/harness-section9-manifest.json`, `scripts/validate-harness-section9.mjs`.

REACH summary for the core paths:

| Path | REACH | Entry point / basis |
|---|---|---|
| projects/chirality-app-dev/frontend/src/lib/harness/mcp/read-tools.ts | LEGACY_ONLY | self (no live import chain) |
| projects/chirality-app-dev/frontend/src/lib/harness/mcp/coordination-tools.ts | LEGACY_ONLY | self |
| projects/chirality-app-dev/frontend/src/lib/harness/sdk-options-builder.ts | LEGACY_ONLY | self |
| projects/chirality-app-dev/frontend/src/lib/harness/tool-pool.ts | LEGACY_ONLY | self |
| projects/chirality-app-dev/frontend/src/lib/harness/permission-overlay.ts | LEGACY_ONLY | self |
| projects/chirality-app-dev/frontend/src/lib/harness/tool-evidence.ts, tool-path-policy.ts, session-events.ts, event-factory.ts, turn-engine.ts | LEGACY_ONLY | self |
| projects/chirality-app-dev/frontend/src/lib/harness/scaffold.ts | LIVE | frontend/src/app/api/harness/scaffold/route.ts |
| projects/chirality-app-dev/frontend/src/lib/workspace/deliverable-contracts.ts | LIVE | frontend/src/app/api/working-root/deliverable/content/route.ts |
| projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts | LIVE | frontend/src/app/api/project/deliverables/route.ts |
| projects/chirality-runtime/packages/contracts/src/harness/{mcp/tool-names,tool-descriptor,tool-catalog}.ts | LIVE | chirality-runtime/packages/daemon/src/standalone-bin.ts |

Shorthand used below: `RT` = `projects/chirality-runtime/packages/contracts/src/harness/`; `FE` = `projects/chirality-app-dev/frontend/`; `T` = `projects/chirality-app-dev/frontend/src/__tests__/lib/`.

Core symbol anchors:
- `FE/src/lib/harness/mcp/read-tools.ts`: `runReadMcpToolWithEvidence` :153 (emits `tool.started` :173, `tool.completed` :193, `tool.failed` :211 via `appendHarnessEvent`); `assertReadMcpPermission` :227 (default mode `readOnly` :240); `assertLexicallyWithinProjectRoot` :464; `assertExistingPathWithinProjectRoot` :486; `statusReadTool` :709; `dependenciesReadTool` :722; `scopeScanTool` :735; `scaffoldPreviewTool` :754; `createChiralityReadMcpServer` :1002 (`createSdkMcpServer` :1005); `buildChiralityMcpTools` :1048 (per-tool gating on allowed names :1056/:1069/:1082/:1093; coordination composition :1109); `createChiralityMcpServers` :1243; `filterChiralityMcpAllowedToolNames` :1276.
- `RT/mcp/tool-names.ts`: `CHIRALITY_MCP_SERVER_NAME='chirality'` :1; `CHIRALITY_MCP_READ_TOOL_NAMES` :4 (`status_read, deps_read, scope_scan, scaffold_preview`); `MUTATING` :11; `DOMAIN` :16; `COORDINATION` :24; `isChiralityMcpAllowedToolName` :66.
- `RT/tool-descriptor.ts`: descriptor type fields `concurrency`/`interruptBehavior` :84-93; `UNKNOWN_TOOL` issue type :109; `chiralityReadMcpDescriptor` :267; `chiralityCoordinationMcpDescriptor` :400; read MCP descriptor entries `status_read` :555, `deps_read` :575, `scope_scan` :593, `scaffold_preview` :607; `delegate_agent` :635; `getHarnessToolDescriptor` :1379.
- `FE/src/lib/harness/sdk-options-builder.ts`: imports :20-21; `filterChiralityMcpAllowedToolNames` :163; `mcpServers: { ...createChiralityMcpServers(` :236.
- `FE/src/lib/harness/tool-pool.ts`: `UNKNOWN_TOOL` structured issue :66.
- `FE/src/lib/workspace/deliverable-contracts.ts`: `readDeliverableStatus` :199 (`_STATUS.md` path :210); `readDeliverableDependencies` :431 (`_DEPENDENCIES.md` `secondarySummaryPresent` :443-470).
- `FE/src/lib/workspace/filesystem.ts`: `normalizeProjectRoot` :309; `scanProjectScopes` :1082.
- `FE/src/lib/harness/scaffold.ts`: `previewScaffoldExecutionRoot` :501 (write helpers `mkdir` :456 / `writeFile` :474 are separate functions in the same file).
- `FE/scripts/harness-section9-manifest.json`:73 `section9.chirality_mcp_status_dependencies` (testFiles `chirality-read-mcp.test.ts`, `dependencies-register-contract.test.ts`; evidenceFiles `read-tools.ts`).

Candidate tests (TestCount): `T/chirality-read-mcp.test.ts` (10), `T/chirality-mutating-mcp.test.ts` (5), `T/tool-descriptor.test.ts` (15), `T/sdk-options-builder.test.ts` (20), `T/permission-overlay.test.ts` (13), `T/agent-sdk-mcp-behavior-probe.test.ts` (1), `T/coordination-tools.test.ts` (2), `T/dependencies-register-contract.test.ts` (10), `FE/src/__tests__/scripts/validate-harness-section9.test.ts` (4).

## SCA-APP-010 Gate-5 Current Contract (Controlling)

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#SEC-1 | Current responsibility | read MCP wrappers: `FE/src/lib/harness/mcp/read-tools.ts`:709-785, :1002, :1048 (LEGACY_ONLY); names `RT/mcp/tool-names.ts`:4-9 (LIVE); descriptors `RT/tool-descriptor.ts`:555-620 (LIVE); catalog text `RT/tool-catalog.ts`:111 (LIVE). `propose` tool: NO_CANDIDATE | `T/chirality-read-mcp.test.ts`:185-633; `T/tool-descriptor.test.ts`:143, :410 | `propose` grep terms tried: `mcp__chirality__propose`, `proposal.offered`, `proposalOffered`, `once.per.chat`, `declinedTrigger`, `specification.ladder` — no hit in FE src/electron or runtime packages/tests. Only `'propose'` hits are the pec `domain_propose_operation` mode enum (`read-tools.ts`:1212; `domain-proposal-tools.ts`:61, :451; `RT/tool-descriptor.ts`:892). HINTS `propose` hit is `FE/scripts/run-dapp52-live-llm-demo.ts` (pec demo script). |
| DEL-06-03#SEC-2 | Current acceptance obligations | (1) in-process/no-network: server instructions strings `read-tools.ts`:1009, :1263 (LEGACY_ONLY); (2) `propose` tuple validation / plan refs / declined trigger / `proposal.offered`: NO_CANDIDATE; (3) catalog validation: `RT/tool-descriptor.ts`:1333 `createDescriptorLookup`, `FE/src/lib/harness/tool-pool.ts`:55-72 (LEGACY_ONLY) | `T/tool-descriptor.test.ts`:121 (name disjointness), :552 (unknown tool issues) | Item 2 search terms as SEC-1. Item 3 is stated as DEL-06-02-owned. `domain_*` pec tools use loopback HTTP per `read-tools.ts`:1263 text. |
| DEL-06-03#SEC-3 | Seating and rulings | DOC_ONLY | — | Refers to D-APP-108, Q11–Q13, WI-036..WI-040, DEP-015/016; matches `_STATUS.md` Remaining DEL-06-03-V3-01 (:11-18). |

## Deliverable Definition — Ontology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#CLM-001 | Datasheet heading | DOC_ONLY | — | REF-006 MATCH note (D-APP-38 / D-APP-56). |
| DEL-06-03#CLM-002 | Identification | DOC_ONLY | — | Scope row lists four read tools; `propose` not in this row. |
| DEL-06-03#CLM-003 | Attributes | namespace `RT/mcp/tool-names.ts`:1, :45-58 (LIVE); tool names :4-9; adjacent write tools :11-14; wrapper metadata fields `RT/tool-descriptor.ts`:84-106, `chiralityReadMcpDescriptor` :267 (LIVE); ordering/allow `read-tools.ts`:1048-1123 (LEGACY_ONLY); Section 9 marker `FE/scripts/harness-section9-manifest.json`:73 | `T/tool-descriptor.test.ts`:143, :410, :448; `T/chirality-read-mcp.test.ts`:588 | SoW names `mcp__chirality__scaffold`; code name is `scaffold_preview` (`tool-names.ts`:8; alias `scaffold_dry_run` at `tool-descriptor.ts`:608). |
| DEL-06-03#CLM-004 | Conditions | readOnly default `read-tools.ts`:240, :1114, :1122 (LEGACY_ONLY); permission overlay `FE/src/lib/harness/permission-overlay.ts` (LEGACY_ONLY); status source `deliverable-contracts.ts`:199 (LIVE); dependency source :431 (LIVE); scaffold preview `scaffold.ts`:501 (LIVE) | `T/permission-overlay.test.ts`:166, :236; `T/sdk-options-builder.test.ts`:510, :608; `T/tool-descriptor.test.ts`:410 | `allowedTools` handling: `sdk-options-builder.ts`:163, :236. |
| DEL-06-03#CLM-005 | Construction | `createSdkMcpServer`/`tool()` `read-tools.ts`:1-7, :1005, :1011-1040, :1259 (LEGACY_ONLY); shared wrapper `runReadMcpToolWithEvidence` :153; status :709; deps :722; scope :735; scaffold :754 | `T/chirality-read-mcp.test.ts`:186, :247, :263, :560 | Deps-only `_DEPENDENCIES.md` path: `deliverable-contracts.ts`:443-470 `secondarySummaryPresent`. |
| DEL-06-03#CLM-006 | Pass 3 Notes (C-001) | `deliverable-contracts.ts`:431-470 (LIVE) | `T/chirality-read-mcp.test.ts`:186 | Pass-3 drafting record. |
| DEL-06-03#CLM-007 | References | DOC_ONLY | — | Lists governing docs sections. |

## Completion and Reliance Basis — Epistemology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#CLM-008 | Specification heading | DOC_ONLY | — | REF-006 note. |
| DEL-06-03#CLM-009 | Scope | as CLM-005; exclusions: mutating tools `read-tools.ts`:925 `statusTransitionTool`, :967 `dependenciesWriteTool`, gated at :1125/:1143 (LEGACY_ONLY) | `T/chirality-mutating-mcp.test.ts`:184; `T/sdk-options-builder.test.ts`:313 | Mutating tools exist in same module, gated to workspaceWrite. Domain tools also on the same server (:1161-1240). |
| DEL-06-03#CLM-010 | Requirements REQ-06-03-001..015 | 001 `RT/mcp/tool-names.ts`:52-70; 002 :4-9; 003 `read-tools.ts`:754-785 + `scaffold.ts`:501; 004 `RT/tool-descriptor.ts`:84-106, :267-308; 005 `read-tools.ts`:1048-1123; 006 `read-tools.ts`:153-225, :227-265; 007 `read-tools.ts`:1056-1100 (per-name gating); 008 `sdk-options-builder.ts`:163-236; 009 `read-tools.ts`:240; 010 `read-tools.ts`:170-215; 011 `deliverable-contracts.ts`:199; 012/015 `deliverable-contracts.ts`:431-470; 013 `filesystem.ts`:309, :1082, `read-tools.ts`:464-506; 014 `tool-pool.ts`:55-72, `RT/tool-descriptor.ts`:109 | `T/tool-descriptor.test.ts`:121, :143, :410, :552; `T/chirality-read-mcp.test.ts`:186, :247, :263, :560, :588; `T/sdk-options-builder.test.ts`:63, :282, :608; `T/permission-overlay.test.ts`:166, :236; `T/agent-sdk-mcp-behavior-probe.test.ts`:450 | REACH: read-tools/sdk-options-builder/tool-pool LEGACY_ONLY; deliverable-contracts/filesystem/scaffold/RT LIVE. Probe test :450 records SDK MCP messages do not auto-invoke permission/hook callbacks. |
| DEL-06-03#CLM-011 | Standards | DOC_ONLY | — | Contract/section citations only. |
| DEL-06-03#CLM-012 | Verification | as CLM-010; Section 9 `FE/scripts/harness-section9-manifest.json`:73; `FE/scripts/validate-harness-section9.mjs` | `T/chirality-read-mcp.test.ts`; `T/dependencies-register-contract.test.ts`:55-215; `FE/src/__tests__/scripts/validate-harness-section9.test.ts` | Proposed test names (`chirality-mcp-descriptor-schema` etc.) not found as file names; nearest are `tool-descriptor.test.ts` cases :143, :410. |
| DEL-06-03#CLM-013 | Acceptance Evidence Register | as CLM-012; events `read-tools.ts`:170-215 | as CLM-012 | Register rows all say TBD in SoW text. |
| DEL-06-03#CLM-014 | Documentation | definitions `read-tools.ts`:1002-1123; metadata `RT/tool-descriptor.ts`:555-620; catalog `RT/tool-catalog.ts`:94-140 | as CLM-010 | — |
| DEL-06-03#CLM-015 | Conflict Table | DOC_ONLY | — | REF-006 MATCH. |
| DEL-06-03#CLM-016 | Pass 3 Notes (sub-item AC-001) | AC-001: as CLM-010 (naming, metadata, deny, status/deps, bounded scan, no-write scaffold) | as CLM-010 | "legacy source line with hash-bound migration markers" refers to SoW conversion; no code candidate for that clause. |

## Production and Verification Method — Praxeology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#CLM-017 | Procedure heading | DOC_ONLY | — | — |
| DEL-06-03#CLM-018 | Purpose | DOC_ONLY | — | — |
| DEL-06-03#CLM-019 | Prerequisites | DOC_ONLY | — | States implementation locations TBD; locations now exist (see CLM-020). |
| DEL-06-03#CLM-020 | Implementation Location Worklist | MCP defs `read-tools.ts`:1048 (LEGACY_ONLY); wrapper metadata `RT/tool-descriptor.ts`:267 (LIVE) + `FE/src/lib/harness/tool-evidence.ts` (LEGACY_ONLY); status reader `deliverable-contracts.ts`:199 (LIVE); dependency reader :431 (LIVE); scope scan `filesystem.ts`:1082 (LIVE); scaffold preview `scaffold.ts`:501 (LIVE) | `T/chirality-read-mcp.test.ts` | Worklist rows all TBD in SoW text. |
| DEL-06-03#CLM-021 | Steps 1–11 | steps 2–10 map to the anchors in CLM-010; step 9 events `read-tools.ts`:170-215 via `FE/src/lib/harness/session-events.ts` (LEGACY_ONLY) | as CLM-010 | Step 8 names `mcp__chirality__scaffold`; code tool is `scaffold_preview`. |
| DEL-06-03#CLM-022 | Verification checks | as CLM-010; unknown names `tool-pool.ts`:66 | `T/tool-descriptor.test.ts`:552; `T/chirality-read-mcp.test.ts`:263, :560; `T/permission-overlay.test.ts`:166 | — |
| DEL-06-03#CLM-023 | Records | Section 9 mapping `harness-section9-manifest.json`:73 | `FE/src/__tests__/scripts/validate-harness-section9.test.ts` | Other records are process artefacts. |
| DEL-06-03#CLM-024 | Pass 3 Notes (sub-item VER-001) | VER-001: as CLM-010 / CLM-012 | as CLM-012 | Includes human review of TBD dependency interfaces (no code candidate). |

## Governing Values and Decisions — Axiology

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#CLM-025 | Guidance heading | DOC_ONLY | — | — |
| DEL-06-03#CLM-026 | Purpose | as CLM-005 | as CLM-005 | — |
| DEL-06-03#CLM-027 | Principles 1–5 | shared wrapper `read-tools.ts`:153, :227; determinism `read-tools.ts`:1048; deny posture `permission-overlay.ts`; file truth `deliverable-contracts.ts`:199, :431 | `T/permission-overlay.test.ts`:236; `T/sdk-options-builder.test.ts`:608 | — |
| DEL-06-03#CLM-028 | Considerations | exclusions `read-tools.ts`:1125, :1143 (LEGACY_ONLY); scaffold `scaffold.ts`:501 (LIVE) | `T/chirality-mutating-mcp.test.ts`:184 | `deps_write` hint hits point at `read-tools.ts`:967 / `RT/mcp/tool-names.ts`:13. |
| DEL-06-03#CLM-029 | Source-State Posture | DOC_ONLY | — | — |
| DEL-06-03#CLM-030 | Trade-offs | shared wrapper `read-tools.ts`:153 + descriptors `RT/tool-descriptor.ts`:267; deps absence `deliverable-contracts.ts`:443-470 | as CLM-005 | — |
| DEL-06-03#CLM-031 | Scaffold Boundary Rationale | `read-tools.ts`:754-785; `scaffold.ts`:501 (LIVE) | `T/chirality-read-mcp.test.ts`:263, :560 | — |
| DEL-06-03#CLM-032 | Examples | as CLM-020 | as CLM-020 | Example uses `mcp__chirality__scaffold`; code `scaffold_preview`. |
| DEL-06-03#CLM-033 | Conflict Table (for human ruling) | DOC_ONLY | — | — |
| DEL-06-03#CLM-034 | Pass 3 Notes | DOC_ONLY | — | — |
| DEL-06-03#CLM-035 | D-APP-68 Coordination Composition (sub-items AC-002, VER-002) | composition `read-tools.ts`:62, :1109 (LEGACY_ONLY); factory `FE/src/lib/harness/mcp/coordination-tools.ts`:264 `buildCoordinationMcpTools` (LEGACY_ONLY); names `RT/mcp/tool-names.ts`:24-29 (LIVE); descriptors `RT/tool-descriptor.ts`:400, :635 (LIVE); server assembly `sdk-options-builder.ts`:236 (LEGACY_ONLY) | `T/coordination-tools.test.ts`:45, :145; `T/permission-overlay.test.ts`:102 | SoW evidence paths `frontend/src/lib/harness/sdk-options-builder.ts` and `.../mcp/coordination-tools.ts` both exist in frozen tree. |

## _STATUS Remaining

| Unit | Label | Candidate code (REACH) | Candidate tests | Remarks |
|---|---|---|---|---|
| DEL-06-03#REM-1 | DEL-06-03-V3-01 `propose` tool | NO_CANDIDATE | NO_CANDIDATE | Grep terms tried as SEC-1 (`mcp__chirality__propose`, `proposal.offered`, `proposalOffered`, `once.per.chat`, `declinedTrigger`, `specification.ladder`); no `propose` entry in `RT/mcp/tool-names.ts`:4-29. Item gated NOT_SELECTABLE_UNTIL DEL-02-02-V3-04. |
