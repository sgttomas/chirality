# Dependencies: DEL-02-05 API Key UI and Runtime Feedback

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been declared by a human.

## Declared Downstream

TBD - no accepted dependency edges have been declared by a human.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | TargetType | Target | Status | Evidence |
|---|---|---|---|---|---|---|---|
| DEP-02-05-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-02 Woven Dialogue Shell, Navigation, and Operator State | ACTIVE | `_CONTEXT.md` Identity; applied decomposition PKG-02 (L280) |
| DEP-02-05-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-013 Typed runtime errors | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition Scope Ledger (L416) |
| DEP-02-05-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-019 App credential UI and packaged-daemon single-owner safeStorage conformance | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition Scope Ledger (L422) |
| DEP-02-05-004 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge | ACTIVE | `ScopeOfWork.md` CLM-016; applied decomposition DEL-04-05 (L330) (SCC-001 internal; graph fields frozen) |
| DEP-02-05-005 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT | `@chirality/harness-contract` typed error taxonomy | ACTIVE | `ScopeOfWork.md` CLM-010 DEL-02-05-R10 |
| DEP-02-05-006 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE | `ScopeOfWork.md` CLM-010 DEL-02-05-R07; applied decomposition DEL-03-03 (L319) (SCC-001 internal; graph fields frozen) |
| DEP-02-05-007 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-023 Attachment UI and recovery | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition Scope Ledger (L426) |
| DEP-02-05-008 | EXECUTION | INTERFACE | UPSTREAM | EXTERNAL | Root-owned `HostedEngineConsentPort` | ACTIVE | applied decomposition DEL-02-05 (L311) |
| DEP-02-05-009 | EXECUTION | CONSTRAINT | UPSTREAM | EXTERNAL | accepted Root/App account/consent contract; G3; G-CSP; G4 | ACTIVE | applied decomposition DEL-02-05 (L311) |
| DEP-02-05-010 | EXECUTION | ENABLES | DOWNSTREAM | DELIVERABLE | DEL-09-06 Network, Key, Attachment, and Renderer Security Checks | ACTIVE | `ScopeOfWork.md` D-APP-80 note; applied decomposition DEL-09-06 (L383) |
| DEP-02-05-011 | ANCHOR | OTHER | UPSTREAM | UNKNOWN | OBJ-001 governed local desktop harness centred on human-agent dialogue | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition objectives (L262) |
| DEP-02-05-012 | ANCHOR | OTHER | UPSTREAM | UNKNOWN | OBJ-008 explicit and repeatable validation, packaging, release, network, key, and instruction-root checks | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition objectives (L269) |
| DEP-02-05-013 | EXECUTION | CONSTRAINT | UPSTREAM | EXTERNAL | Root DEL-02-09 root-private login home and shared-login amendment (OI-008) | ACTIVE | applied decomposition DEL-02-05 (L311); OI-008 (L602) |

Counts:

- ACTIVE rows: 13
- RETIRED rows: 0
- ANCHOR rows: 6
- EXECUTION rows: 7
- UNKNOWN targets: 2 (objective anchors DEP-02-05-011 and DEP-02-05-012, by the objective convention)
- Reserved, not emitted: DEP-02-05-014 and DEP-02-05-015 (held proposals H-013 and H-014; see Run Notes)

## Run Notes

### 2026-09-05 UPDATE (SCA-APP-010 DEP-007/DEP-008; preview N1-TASK-DEL-02-05, amended v1.1)

- Run timestamp: 2026-09-05T00:36:40-0600 (preview v1); rerun 2026-09-05T01:03:00-0600 under brief amendment v1.1 (`AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`, sections A, B, and D). The bytes of this file and of `Dependencies.csv` were produced as a report-only preview under `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-05/` and applied by the reviewed write authorized by SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-007 and DEP-008.
- Runtime overrides: `SCOPE=DEL-02-05_API_Key_UI_and_Runtime_Feedback`; `RUN_ROOT=projects/chirality-app-dev/execution`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`. No default was left to auto-discovery.
- Instruction root: the repository checkout (`agents/`, `skills/`, `tools/` at the Git toplevel).
- Decomposition path: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (SCA-APP-010 Gate 5); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`. Recomputed before extraction and again before the v1.1 rerun; no mismatch.
- Source docs used for row evidence: `ScopeOfWork.md` (front matter, Purpose and Objective Traceability, SCA-APP-010 Gate-5 Current Contract, CLM-010, CLM-016), `_CONTEXT.md` (Identity, Deliverable Scope), `_STATUS.md` (`## Remaining` only: the seated items' Depends, Write locus, and gate lines), `_REFERENCES.md` (pointer resolution only), and the applied decomposition at L262, L269, L280, L307, L309, L311, L319, L330, L383, L404 to L487, L602, and L634. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` were excluded as sources.
- Anchor doc choice: `ScopeOfWork.md` front matter `decomposition_basis`, `project_scope_refs`, `package_objective_refs`, and Purpose and Objective Traceability, with `_CONTEXT.md` Identity for the parent anchor. The applied row L311 carries SOW-013, SOW-019, SOW-023, OBJ-001, and OBJ-008; none of SOW-081 to SOW-084 is on this carrier, and no scope ref left the row, so no anchor was retired.
- Execution doc order: `ScopeOfWork.md`, `_CONTEXT.md`, then `_STATUS.md` `## Remaining`; the applied decomposition resolved targets and labels.
- Stable IDs DEP-02-05-001 through DEP-02-05-010 are preserved; no row was deleted or retired; `Status=CANDIDATE` was not emitted. DEP-02-05-005 was re-evidenced from the excluded `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md` to `ScopeOfWork.md` CLM-010 DEL-02-05-R10, which restates the relation. DEP-02-05-001, -002, -003, -007, and -010 had their decomposition line pointers refreshed (PKG-02 L286 to L280; Scope Ledger L401/L407/L411 to L416/L422/L426; DEL-09-06 L369 to L383); DEP-02-05-008 and -009 had their applied-row pointer refreshed from L297 to L311.
- New rows: DEP-02-05-011 and -012 (objective trace anchors OBJ-001 and OBJ-008, `TargetType=UNKNOWN` by the objective convention); DEP-02-05-013 (Root DEL-02-09 root-private login home and shared-login amendment, OI-008, `EXTERNAL`/`TBD`/`PENDING`, introduced by the L311 Notes).
- HELD (non-emitted proposal, pending owner ruling): DEP-02-05-014 reserved — DEL-02-05 UPSTREAM PREREQUISITE DEL-02-01 (account row host, revised SOW-001; seated DEL-02-05-V3-05 Depends line) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-013
- HELD (non-emitted proposal, pending owner ruling): DEP-02-05-015 reserved — DEL-02-05 UPSTREAM PREREQUISITE DEL-02-03 (right-panel view switcher for the Settings view; seated DEL-02-05-V3-05 Depends line; target CONFLICT against the applied DEL-02-03 row L309 and SOW-001 L404 recorded on the held row) — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-014
- Held-row basis: the fan-in simulation of all thirteen N1 previews (`AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/Evidence/fanin_simulation_v1/`) shows the fifteen newly proposed deliverable edges lie on cycles collectively (SCC-001 would merge into a 20-node SCC); SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3 requires SCC unchanged unless separately ruled, and `docs/CYCLE_DRIVEN_RESOLUTION.md` makes cut and merge human-gated. The two IDs stay reserved and are not renumbered; the rows were never written to the carrier, so this is not a register deletion.
- Fence F1 (DEL-02-05 is an SCC-001 member): no new `EXECUTION` row has both endpoints inside SCC-001. The SCC-internal rows DEP-02-05-004 (DEL-04-05) and DEP-02-05-006 (DEL-03-03) remain evidenced by live bytes (CLM-016 line 320; CLM-010 DEL-02-05-R07 line 235). Under amendment v1.1 section B their `TargetLocation` line pointers were refreshed to the live applied rows (L316 to L330; L305 to L319) with a Notes provenance clause; `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, and `FirstSeen` are byte-identical to the pre-image. The seated DEL-02-05-V3-03 Depends line naming DEL-04-05-V3-02 maps onto existing DEP-02-05-004 and adds no edge. `NEEDS_HUMAN_GRAPH_DECISION`: none.
- Fence F2 (no Root path): every Root-owned target (DEP-02-05-008, -009, -013) is `EXTERNAL` with `TargetLocation=TBD`; no new or changed `TargetLocation` names a path outside `projects/chirality-app-dev/**`. Observation: pre-existing DEP-02-05-005 `TargetLocation=frontend/packages/harness-contract` (an App-owned repo path, not a Root path) lies outside the F2 whitelist and is preserved unchanged for reviewer disposition.
- Fence F3 (permitted effect): the seated DEL-02-05-V3-03 Depends line also names DEL-09-06-V3-03 as an upstream prerequisite for live consent flows; that relation predates SCA-APP-010 (A12 seating, 2026-09-03) and is not among the SOW-081 to SOW-084 or revised SOW-001/002/004/006/007/008/010 relations, so no reverse row to DEL-09-06 was emitted; existing DEP-02-05-010 continues to carry the retained-validation relation. No edge was inferred from SCC ordering, schedule, or coordination-only statements.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `tools/validation/validate_id_format.sh` profile rejects the accepted App identifiers `DEL-02-05`, `PKG-02`, `DEP-02-05-001` to `DEP-02-05-013`, `SOW-013`, `SOW-019`, and `SOW-023` (three-digit package/deliverable and four-digit SOW shapes expected); `OBJ-001` and `OBJ-008` pass. No identifier was changed.
- Parent anchor check: PASS - exactly one ACTIVE `IMPLEMENTS_NODE` anchor (DEP-02-05-001).
- Schema check: `validate_dependencies_schema.py` VALID, 29 columns, 13 data rows; every emitted enum value VALID under `validate_enum.py`.
- Source-preservation check: no byte under the carrier folder, the decomposition, the companion register, the pointer, or any Root surface was modified by the preview or its v1.1 rerun; the reviewed write touches only `Dependencies.csv`, this file, and the carrier-local TASK run record.

### 2026-08-24 UPDATE (retained)

- Run timestamp: 2026-08-24T00:54:31-0600.
- Runtime overrides: `SCOPE=DEL-02-05`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Instruction root: `/Users/ryan/.codex/worktrees/ef5e/chirality`, supplied by the supervising runtime in additive `V2_INSTRUCTION_ROOT_RUNTIME_DECLARATION.md` after an initial missing-environment preflight; the sealed task scope and method were unchanged.
- Decomposition path: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Decomposition SHA-256: `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` (exact post-application basis).
- Source docs used for row evidence: `_CONTEXT.md`, `ScopeOfWork.md`, `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md`, `_REFERENCES.md`, and the exact post-application decomposition. Assessment and semantic records were read only as scoped context and do not supply row evidence.
- Anchor doc choice: `ScopeOfWork.md` purpose/traceability plus `_CONTEXT.md` identity; the exact decomposition validates PKG-02, DEL-02-05, SOW-013, SOW-019, and SOW-023.
- Execution doc order: `ScopeOfWork.md`, `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md`, then the applied decomposition for target resolution and newly applied carrier interfaces.
- Stable IDs DEP-02-05-001 through DEP-02-05-007 are preserved. DEP-02-05-004 is conservatively resolved to DEL-04-05 for its credential/safeStorage slice; DEP-02-05-006 is resolved to DEL-03-03; DEP-02-05-005 normalizes legacy `TargetType=ARTIFACT` to canonical `DOCUMENT`.
- DEP-02-05-008 and DEP-02-05-009 record the newly applied account/consent interface and live-claim gates exactly as stated by the decomposition. Their Root-owned target locations remain `TBD`; no Root path is invented.
- DEP-02-05-010 records the explicit DEL-09-06 validation handoff as information/evidence flow, not a schedule gate.
- A2-B / E-018 posture: no row was emitted for DEL-05-04 feedback to DEL-02-05 because the permitted scoped sources contain no explicit DEL-05-04 information-transfer statement. The accepted SCC ordering remains non-gating and was not silently linearized.
- `[WARNING] ID_FORMAT_VALIDATOR_MISMATCH`: the generic validator rejects live decomposition IDs `DEL-02-05`, `PKG-02`, `DEP-02-05-001`, and `SOW-013` because it expects three-digit package/deliverable and four-digit SOW shapes. The exact live decomposition identities are preserved; `OBJ-001` passes.
- Parent anchor check: PASS - exactly one ACTIVE `IMPLEMENTS_NODE` anchor.
- Source-preservation check: scoped source documents, current v19 `_REFERENCES.md`, and the decomposition were not modified by this TASK.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` present | TARGET_UNRESOLVED; ID_FORMAT_VALIDATOR_MISMATCH; SOURCE_WARNING; TRACEABILITY_DELTA | ANCHOR=3; EXECUTION=3; TOTAL=6 |
| 2026-07-12 | UPDATE / reconciliation annotation | CONSERVATIVE | decomposition v3.2 | none current; earlier warnings retained as dated history | ANCHOR=4; EXECUTION=3; TOTAL=7 |
| 2026-08-24T00:54:31-0600 | UPDATE | CONSERVATIVE | applied SHA `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` | E-018 not emitted: no scoped source evidence | ANCHOR=4; EXECUTION=6; TOTAL=10 |
| 2026-09-05T00:36:40-0600 (rerun 2026-09-05T01:03:00-0600, amendment v1.1) | UPDATE | CONSERVATIVE | found at pinned identity SHA `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`) | PROJECT_ID_FORMAT_PROFILE; F2 observation on pre-existing DEP-02-05-005 TargetLocation; F3 non-emission of the DEL-09-06 reverse prerequisite; DEP-02-05-014 and -015 HELD as non-emitted proposals H-013/H-014 (IDs reserved) | ANCHOR=6; EXECUTION=7; TOTAL=13 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 6 |
| PENDING | 6 |
| SATISFIED | 1 |

Closure state:

- Required derivative package regenerated: `Dependencies.csv` v3.1 (13 rows; 6 ANCHOR, 7 EXECUTION; DEP-02-05-014 and -015 reserved for held proposals H-013 and H-014).
- Required dependency index refreshed: `_DEPENDENCIES.md`.
- Remaining blockers: Root-owned account/consent target locations (DEP-02-05-008, -009, -013) are intentionally unresolved pending the accepted Root/App account/consent contract and the routed Root DEL-02-09 return (OI-008); the accepted contract and G3/G-CSP/G4 remain live-claim gates; the DEL-02-01 account row host and DEL-02-03 right-panel view switcher prerequisites stated by the seated DEL-02-05-V3-05 Depends line are held as non-emitted proposals H-013 and H-014 pending the owner's separate cycle-resolution ruling; the SCC-001 membership of this carrier is unchanged and its internal edges (DEP-02-05-004, -006) keep their frozen graph fields for the cycle-resolution workflow.

## Downstream Handoff Notes

- Consumer context: `RECONCILIATION`.
- Reconciliation should treat DEP-02-05-008, DEP-02-05-009, and DEP-02-05-013 as Root-owned interface/constraint evidence with unresolved App-local target paths, not as application, contract-acceptance, or gate-satisfaction claims; DEP-02-05-013 is the OI-008 login-home dependency and is satisfied only when Root DEL-02-09's accepted return is routed to App.
- Reconciliation should read DEP-02-05-011 and DEP-02-05-012 as objective traceability (`TargetType=UNKNOWN` by convention), not as requirement rows.
- Reconciliation should not expect rows for the DEL-02-01 account row host or the DEL-02-03 right-panel view switcher: those relations are held as non-emitted proposals H-013 and H-014 in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` (IDs DEP-02-05-014 and -015 reserved) pending the owner's ruling; the H-014 target question (DEL-02-03 versus DEL-02-01) travels with the held proposal.
- Reconciliation should note the pre-existing DEP-02-05-005 `TargetLocation=frontend/packages/harness-contract` as an App-owned repo path outside the F2 whitelist, preserved for disposition.
- Reconciliation should keep the DEL-05-04-to-DEL-02-05 E-018 SCC move and the DEL-09-06-V3-03 upstream prerequisite named in DEL-02-05-V3-03 non-gating unless a later accepted source adds an explicit information-flow edge within a permitted write set; SCC-001 remains unchanged by this pass.

## Historical Register Annotations

- D-APP-56 R5 P40 (2026-07-12): REF-006 is MATCH under D-APP-38; any HASH_MISMATCH token retained in dated history is provenance, not current state.
- D-APP-56 R5 P45 (2026-07-12): UPD-112 added stable anchor DEP-02-05-007 from the explicit SOW-023 decomposition mapping.
- SCA-APP-010 DEP-007/DEP-008 (2026-09-05): objective anchors DEP-02-05-011/-012 and execution row DEP-02-05-013 added from the applied row L311 and OI-008; DEP-02-05-005 re-evidenced to `ScopeOfWork.md` after the legacy kit and evidence-file sources were excluded; SCC-internal rows DEP-02-05-004/-006 had their decomposition line pointers refreshed under brief amendment v1.1 section B; DEP-02-05-014/-015 reserved for held proposals H-013/H-014 (amendment v1.1 section A).
