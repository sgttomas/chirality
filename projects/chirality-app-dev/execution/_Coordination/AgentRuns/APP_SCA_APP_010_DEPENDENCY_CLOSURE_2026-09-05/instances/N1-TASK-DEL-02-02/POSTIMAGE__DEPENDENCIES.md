# Dependencies: DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (found).
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selected: `Datasheet.md`; execution doc order selected: `Specification.md`, `Guidance.md`, `Procedure.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records a hash mismatch for `docs/PRD.md`; dependency extraction treated this as a source warning, not a blocker.
- [WARNING] SOW_007_OWNER_OVERLAP: `_CONTEXT.md` and the deliverable ledger list SOW-007 under DEL-02-02, while the scope ledger marks PKG-08 / DEL-08-03 as primary owner for Pipeline selectors. Rows preserve this as conflict/TBD rather than resolving it.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (UPDATE)

- Authorization: SCA-APP-010 `FUTURE_WRITE_SET.csv` rows `DEP-003` and `DEP-004`, triggered by the owner's 2026-09-05 acceptance of the WORKING_ITEMS alignment; previewed report-only by `N1-TASK-DEL-02-02` (v1 preview, then the amendment v1.1 rerun) and applied by the reviewed N3 write under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`.
- Brief amendment v1.1 (HELP_HUMAN supervisory disposition after fan-in of the thirteen N1 previews; `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`): the fan-in simulation showed that fifteen newly proposed deliverable edges across nine carriers lie on cycles collectively (they would merge SCC-001 into a 20-node SCC and create a new two-node SCC) while any one alone changes nothing; choosing among them would be a cut, which `docs/CYCLE_DRIVEN_RESOLUTION.md` makes human-gated. Six of this carrier's proposed rows are therefore held as non-emitted proposals for the owner's separate transaction and removed from this register; their IDs stay reserved and are not reused. This is not a register deletion (the rows were never written to the carrier) and not an owner ruling.
- Runtime overrides: `SCOPE=DEL-02-02_Workbench_and_Pipeline_Selection_UX`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`. `DOC_ROLE_MAP=DEFAULT` was not needed because every doc role was explicit.
- Decomposition found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches the `ScopeOfWork.md` front matter `decomposition_basis`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010; basis `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`.
- Sources: `ScopeOfWork.md` (front matter, Purpose and Objective Traceability, SCA-APP-010 Gate-5 Current Contract, CLM blocks as dated compatibility history), `_CONTEXT.md`, `_STATUS.md` `## Remaining` only (seated items DEL-02-02-V3-01 to V3-04; lifecycle, history, and approval fields excluded), `_REFERENCES.md` for pointer resolution, and the applied decomposition at row L308, Scope Ledger rows SOW-006 L176, SOW-081 L251, SOW-082 L252, reverse view L404 to L487, OI-008 L602, DEC-025 L634. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` were not used.
- Pass 1 (ANCHOR): parent anchor DEP-02-02-001 preserved and re-evidenced to `ScopeOfWork.md#CLM-002` with the canonical PKG-02 label from L280. SOW-006 (DEP-02-02-002) and OBJ-001 (DEP-02-02-004) preserved and re-evidenced to `ScopeOfWork.md#Purpose and Objective Traceability`. New trace anchors DEP-02-02-010 (SOW-081), DEP-02-02-011 (SOW-082), and DEP-02-02-012 (OBJ-007) added from the front matter and applied row L308; objectives keep the existing `TargetType=UNKNOWN` convention. DEP-02-02-003 (SOW-007) retired: SOW-007 is no longer on applied row L308 and DEC-025 L634 retired its presentation half.
- Pass 2 (EXECUTION): legacy-kit rows DEP-02-02-005 to DEP-02-02-009 re-evidenced to live `ScopeOfWork.md` bytes (`DEL-02-02-REQ-002`, `CLM-025`, `DEL-02-02-REQ-003`, and the SCA-APP-010 controlling section); they remain stated as dated compatibility history for the retained Workbench/Pipeline code, so they stay ACTIVE at `Confidence=MEDIUM` with a retirement PROPOSAL tied to a future owner act. New rows emitted: DEP-02-02-013 (DEL-07-03 workflow file contract), 014 (DEL-06-03 `propose` tool), 016 (Root DEL-02-10 acceptance, EXTERNAL/TBD), and 021 (DEL-02-03 right-panel view-switcher host). The v1 preview also proposed rows 015, 017, 018, 019, 020, and 022; those are held under amendment v1.1 (next six bullets) and are not in this register.
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-015 reserved — DEL-02-02 UPSTREAM INTERFACE to DEL-05-02 (live `proposal.*` consumption through the App HarnessEvent path after Root acceptance) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-002
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-017 reserved — DEL-02-02 UPSTREAM INTERFACE to DEL-08-05 (recorded managed and native descendant records presented by the Who is working view) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-003
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-018 reserved — DEL-02-02 UPSTREAM INTERFACE to DEL-05-04 (replay lens and Agent projection semantics composed by selected-session presentation) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-004
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-019 reserved — DEL-02-02 UPSTREAM CONSTRAINT to DEL-08-04 (role/delegation semantics behind the role-entry controls and posture labels) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-005
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-020 reserved — DEL-02-02 UPSTREAM CONSTRAINT to DEL-08-02 (routing, guarded selection, and legacy compatibility semantics behind recorded selections and query tests) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-006
- HELD (non-emitted proposal, pending owner ruling): DEP-02-02-022 reserved — DEL-02-02 UPSTREAM INTERFACE to DEL-02-04 (chat-rung and declined-trigger convenience fields consumed by the rung forms and the proposal card) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-007
- Cross-references reconciled to the holds: the `Notes` of DEP-02-02-011 and DEP-02-02-014 now point to held proposal H-002 (DEP-02-02-015 reserved) instead of to a register row; no other field of those rows changed.
- Not emitted (no named artifact transfer stated for this carrier): DEL-04-04 roadmap-injection seam (both DEL-02-02 and DEL-04-04 consume the DEL-07-03 file contract; no direct transfer is stated), DEL-08-01 instruction-clause conformance, Root DEL-02-11 session-record delegation-policy field (the New workflow form's delegation policy is the file's field under SOW-081), Root DEL-02-09 login home (account row is DEL-02-01), and DEL-02-01 hosting of the right-panel frame (recorded only in the DEP-02-02-021 note).
- Fence F1: NONE. DEL-02-02 is not an SCC-001 member. After amendment v1.1 no row in this register targets an SCC-001 member (the v1 candidate DEP-02-02-015 to DEL-05-02 is held as H-002), and no SCC-001 member holds an ACTIVE row targeting DEL-02-02 (the sole inbound row is DEL-02-01 `DEP-02-01-007`, DOWNSTREAM supply), so no cycle through this carrier is created.
- Fence F2: NONE. Every `TargetLocation` is under the applied decomposition or `TBD`; the Root-owned target (DEP-02-02-016) is `EXTERNAL` with `TargetLocation=TBD`.
- Fence F3: NONE. Every emitted new row traces to applied row L308 prose, amended rows SOW-081/SOW-082, OI-008, or a seated `## Remaining` Depends line; no edge was inferred from SCC ordering, schedule, or a keep-aligned statement.
- NEEDS_HUMAN_GRAPH_DECISION: none remaining. The v1 preview flagged DEP-02-02-021 (right-panel view-switcher host). Amendment v1.1 C.1 (HELP_HUMAN disposition-class, not an owner ruling) keeps the target at DEL-02-03 with `Confidence=MEDIUM` and an ASSUMPTION note: the evidence is the owner-adopted `_STATUS.md` DEL-02-02-V3-04 Depends line (DEL-02-03-V3-01, D-APP-108); the reason for MEDIUM is that applied rows L307 and L309 are silent about a right-panel view switcher (SOW-001 L404 maps the one-view-at-a-time right panel to DEL-02-01). Any re-target to DEL-02-01 is an owner act.
- [WARNING] CONTEXT_SOW_007_RESIDUE: `_CONTEXT.md#Traceability` still lists SOW-007 under CoversScopeItems and names Workbench/Pipeline views under Anticipated Artifacts, while applied row L308 carries SOW-006, SOW-081, SOW-082. The applied row governs; the residue is an alignment note for the WORKING_ITEMS loop, not a dependency decision.
- [WARNING] V3_01_ROLE_ENTRY_SEATING_CONFLICT: seated item DEL-02-02-V3-01 says the Codex role-entry offer and posture labels are unseated from DEL-02-02 (S-7; former row L294), while applied row L308 places role-entry controls and the posture labels on this carrier; `_STATUS.md` history 2026-09-04 reads V3-01/V3-02 under the applied row. The proposed DEL-08-04 row that recorded this conflict (DEP-02-02-019) is held as H-005; the conflict itself remains an alignment note for the WORKING_ITEMS loop.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` expects `PKG-NNN`, `DEL-NNN-NN`, `DEP-NNN-NN-NNN`, and `SOW-NNNN`; the accepted App decomposition uses `PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, and `SOW-NNN`, so the helper reports those IDs invalid by its generic profile. No accepted ID was changed.
- Schema: `validate_dependencies_schema.py` VALID, 29 columns, 16 data rows; every emitted enum value VALID under `validate_enum.py`; `DependencyID` unique (reserved IDs 015, 017, 018, 019, 020, and 022 are absent by design); `FromDeliverableID=DEL-02-02` on every row; every ACTIVE row's `SourceRef` heading or ID and `EvidenceQuote` resolve to live bytes; every non-`TBD` `TargetLocation` line begins with its `TargetRefID`.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. No `[WARNING] FLOATING_NODE`; no `[WARNING] AMBIGUOUS_ANCHOR`; no `[WARNING] MISSING_DECOMPOSITION`.
- `FromDeliverableName` refreshed on every row to the applied row L308 display name; the stable ID `DEL-02-02` and the physical folder name are unchanged.

## Extracted Dependency Register

`Dependencies.csv` v3.1 now contains 16 rows: 15 ACTIVE and 1 RETIRED (7 ANCHOR, 9 EXECUTION). IDs DEP-02-02-015, 017, 018, 019, 020, and 022 are reserved for held proposals H-002 to H-007 and are not present.

| DependencyID | Class | Type | Direction | Target | Status | Note |
|---|---|---|---|---|---|---|
| DEP-02-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-02 | ACTIVE | Parent package anchor; re-evidenced to `ScopeOfWork.md#CLM-002`. |
| DEP-02-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-006 | ACTIVE | Who is working view and Codex role-entry trace (amended row L176). |
| DEP-02-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-007 | RETIRED | Not on applied row L308; presentation half retired by DEC-025. |
| DEP-02-02-004 | ANCHOR | OTHER | UPSTREAM | OBJ-001 | ACTIVE | Objective trace; target type kept `UNKNOWN` because schema has no objective enum. |
| DEP-02-02-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-01 | ACTIVE | Matrix/compatibility routing interface for retained routes (dated history). |
| DEP-02-02-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-03 | ACTIVE | Scope scan / stale selection interface for retained Pipeline code (dated history). |
| DEP-02-02-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-04 | ACTIVE | Status summary interface for retained Workbench code (dated history). |
| DEP-02-02-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-05 | ACTIVE | Dependency summary interface for retained Workbench code (dated history). |
| DEP-02-02-009 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-08-03 | ACTIVE | Dispatch-semantics ownership boundary; no active-shell consumer. |
| DEP-02-02-010 | ANCHOR | OTHER | UPSTREAM | SOW-081 | ACTIVE | Workflows view and forms trace (new row L251). |
| DEP-02-02-011 | ANCHOR | OTHER | UPSTREAM | SOW-082 | ACTIVE | Proposal card trace (new row L252); live DEL-05-02 path is held proposal H-002. |
| DEP-02-02-012 | ANCHOR | OTHER | UPSTREAM | OBJ-007 | ACTIVE | Objective trace; target type kept `UNKNOWN`. |
| DEP-02-02-013 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-03 | ACTIVE | Governed workflow file contract read/written by the Workflows view; PENDING on DEL-07-03-V3-01. |
| DEP-02-02-014 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 | ACTIVE | `propose` tool emits the `proposal.offered` payload the card renders; PENDING. |
| DEP-02-02-016 | EXECUTION | CONSTRAINT | UPSTREAM | ROOT-PROPOSAL-EVENT-ACCEPTANCE | ACTIVE | Root DEL-02-10 acceptance of additive `proposal.*` types; EXTERNAL, location TBD; PENDING. |
| DEP-02-02-021 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-02-03 | ACTIVE | Right-panel view-switcher host of the Workflows view; ASSUMPTION per amendment v1.1 C.1 (seated Depends line; L307/L309 silent); MEDIUM; PENDING. |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Active Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:24:27-0600 | UPDATE | CONSERVATIVE | found | 9 | PRD_HASH_MISMATCH; SOW_007_OWNER_OVERLAP |
| 2026-09-05T01:05:00-0600 | UPDATE | CONSERVATIVE | found at pinned identity `c7c05169` (commit `dbd812a5`) | 15 | CONTEXT_SOW_007_RESIDUE; V3_01_ROLE_ENTRY_SEATING_CONFLICT; PROJECT_ID_FORMAT_PROFILE; six proposals held under amendment v1.1 (H-002 to H-007) |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 15 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 12 |
| PENDING | 4 |

Closure note: dependency rows are evidence-backed but not satisfaction-closed. All `RequiredMaturity` values are `SEMANTIC_READY`; `ProposedMaturity` remains `TBD`. The four PENDING rows wait on named seated items (DEL-07-03-V3-01 for DEP-02-02-013, DEL-02-03-V3-01 for DEP-02-02-021), on the DEL-06-03 `propose` tool and event path (DEP-02-02-014), or on the Root DEL-02-10 `proposal.*` acceptance being routed to App (DEP-02-02-016, OI-008). ACTIVE rows: 6 ANCHOR and 9 EXECUTION; the RETIRED row is the SOW-007 anchor. Six further proposed edges (DEL-05-02, DEL-08-05, DEL-05-04, DEL-08-04, DEL-08-02, DEL-02-04) are held outside this register pending the owner's cycle ruling.

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (PKG-02), five trace anchors (SOW-006, SOW-081, SOW-082, OBJ-001, OBJ-007), one retired SOW-007 anchor, five re-evidenced compatibility-history execution rows (DEL-02-01, DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-03), and four new execution rows introduced by SCA-APP-010 (DEL-07-03, DEL-06-03, Root DEL-02-10 EXTERNAL, DEL-02-03 host).
- Held proposals (not in this register; owner's separate transaction under `docs/CYCLE_DRIVEN_RESOLUTION.md`): H-002 DEL-05-02, H-003 DEL-08-05, H-004 DEL-05-04, H-005 DEL-08-04, H-006 DEL-08-02, H-007 DEL-02-04, recorded in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` with reserved IDs DEP-02-02-015, 017, 018, 019, 020, 022. Do not treat their absence as a finding that the relations are unstated.
- Cross-register checks worth running: DEL-02-01 `DEP-02-01-007` (DOWNSTREAM to DEL-02-02) against DEP-02-02-005; DEL-07-03, DEL-06-03, and DEL-02-03 registers for any reciprocal DOWNSTREAM row naming DEL-02-02 as the consumer of the workflow file contract, the `propose` tool payload, or the view switcher.
- SCC posture: DEL-02-02 remains outside SCC-001 and this register holds no edge into SCC-001; the held DEL-05-02 edge (H-002) must not be emitted, nor paired with a reverse edge from DEL-05-02, without an owner ruling under `docs/CYCLE_DRIVEN_RESOLUTION.md`.
- DEP-02-02-021 host identity is carried at `Confidence=MEDIUM` under the amendment v1.1 C.1 ASSUMPTION (DEL-02-03 as seated); re-target to DEL-02-01 only by owner act.
- Root boundary: DEP-02-02-016 stays `EXTERNAL`/`TBD` until the Root DEL-02-10 return is routed to App; no Root path may be recorded in this register.
