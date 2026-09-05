# Dependencies: DEL-04-04 PersonaComposer from Instruction Root

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

## Extracted Dependency Register

Generated register: `Dependencies.csv` v3.1

| Class | Type | Status | Count |
|---|---|---:|---:|
| ANCHOR | OTHER | ACTIVE | 7 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |
| EXECUTION | HANDOVER | ACTIVE | 1 |
| EXECUTION | INTERFACE | ACTIVE | 3 |
| EXECUTION | INTERFACE | RETIRED | 1 |
| EXECUTION | PREREQUISITE | ACTIVE | 1 |

| DependencyID | Class | Direction | Type | Target | Status | Confidence |
|---|---|---|---|---|---|---|
| DEP-04-04-001 | ANCHOR | UPSTREAM | OTHER | PKG-04 SDK Adapter, Prompt, Provider, and Settings | ACTIVE | HIGH |
| DEP-04-04-002 | ANCHOR | UPSTREAM | OTHER | SOW-017 Persona resolution and prompt composition | ACTIVE | HIGH |
| DEP-04-04-003 | ANCHOR | UPSTREAM | OTHER | SOW-030 Instruction-root resources | ACTIVE | HIGH |
| DEP-04-04-004 | EXECUTION | UPSTREAM | INTERFACE | DEL-04-02 SdkOptionsBuilder and Settings Isolation | RETIRED | HIGH |
| DEP-04-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DEL-08-01 Instruction Root Packaging and Agent Conformance | ACTIVE | HIGH |
| DEP-04-04-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-08-02 Persona Alias and Agent Matrix Routing Contract | ACTIVE | MEDIUM |
| DEP-04-04-007 | EXECUTION | UPSTREAM | CONSTRAINT | docs/PRD.md PRD source snapshot | ACTIVE | HIGH |
| DEP-04-04-008 | EXECUTION | DOWNSTREAM | HANDOVER | UNKNOWN Runtime boundary boot/session fingerprint integration | ACTIVE | MEDIUM |
| DEP-04-04-009 | ANCHOR | UPSTREAM | OTHER | SOW-081 Governed workflow files and Workflows view (delimited roadmap-injection seam) | ACTIVE | HIGH |
| DEP-04-04-010 | ANCHOR | UPSTREAM | OTHER | SOW-084 Layered instruction root (bundled base plus organisation layer) | ACTIVE | HIGH |
| DEP-04-04-011 | ANCHOR | UPSTREAM | OTHER | OBJ-004 App integration, packaging, and conformance for the provider-adapter runtime | ACTIVE | HIGH |
| DEP-04-04-012 | ANCHOR | UPSTREAM | OTHER | OBJ-007 Agent-suite integrity and project delegation authority | ACTIVE | HIGH |
| DEP-04-04-013 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-03 Deliverable Metadata and Document Kit Contracts | ACTIVE | HIGH |
| DEP-04-04-014 | EXECUTION | UPSTREAM | INTERFACE | DEL-07-01 Working Root Validation and Instruction Root Protection | ACTIVE | HIGH |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract update run timestamp: 2026-05-20T19:35:58-0600.
- Runtime overrides: `SCOPE=DEL-04-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; existing `_SEMANTIC.md` was not read or consumed.
- Anchor document selection: `Datasheet.md` and `_CONTEXT.md` traceability, validated against decomposition PKG-04 / DEL-04-04 / SOW rows.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, then `Datasheet.md`.
- Parent anchor status: one ACTIVE `IMPLEMENTS_NODE` anchor found; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-only details remain constrained until accepted snapshot confirmation.
- [WARNING] UNKNOWN_TARGET: runtime boundary boot/session fingerprint integration is explicit, but the local evidence does not name a stable consuming deliverable/interface; target preserved as `UNKNOWN` / `TBD`.
- No downstream handoff section was added because `CONSUMER_CONTEXT=NONE`.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (report-only preview)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N1-TASK-DEL-04-04`; `TASK + dependency-extract` as a Claude Code subagent dispatched by HELP_HUMAN; report-only preview under SCA-APP-010 `FUTURE_WRITE_SET.csv` rows DEP-011 and DEP-012. This file is the proposed post-image; it becomes live only when the owner accepts the preview.
- Runtime overrides: `SCOPE=DEL-04-04_PersonaComposer_from_Instruction_Root`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ApplyEdits=false`. `DOC_ROLE_MAP` default not used because the brief fixed the document roles.
- Source boundary: `_STATUS.md` was read as execution evidence only for its `## Remaining` section (seated item `DEL-04-04-V3-01` `Depends`, `Write locus`, and gate lines); `_REFERENCES.md` resolved document pointers only. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_INSP-03_DEL-04-04.md`, and `_run_records/**` were excluded. No source document was modified.
- Decomposition authority found at the pinned identity: SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`, content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, basis `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`; companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`. Applied row L329; amended ledger rows SOW-081 L251 and SOW-084 L254; reverse view L484 and L487; OI-008 L602; DEC-025 L634.
- Pass 1 (ANCHOR): parent anchor DEP-04-04-001 preserved and refreshed; SOW-017 and SOW-030 anchors (DEP-04-04-002, DEP-04-04-003) refreshed because both remain on the applied row; SOW-081 and SOW-084 anchors added as DEP-04-04-009 and DEP-04-04-010; OBJ-004 and OBJ-007 trace anchors added as DEP-04-04-011 and DEP-04-04-012 using the existing `TargetType=UNKNOWN` objective convention. No anchor was retired because no scope ref left the applied row.
- Pass 2 (EXECUTION): DEP-04-04-005, -006, -007, and -008 re-evidenced from the retired four-document kit to live `ScopeOfWork.md` bytes (PC-REQ-001, PC-REQ-005, CLM-029, CLM-018). DEP-04-04-013 (DEL-07-03 governed workflow file contract the seam reads) and DEP-04-04-014 (DEL-07-01 organisation-layer protection and pin the composer trusts) added from the seated `Remaining` item and the SOW-081/SOW-084 amended rows. DEP-04-04-004 retained byte-identical as RETIRED under RUL-SCC-001-TRANCHE-001.
- Not emitted (information-flow rule): no DEL-02-02 edge, because no local source states what the Workflows view supplies to the composer beyond ownership of the view; no DEL-03-02 or other SCC-001 edge, because no local source states a transfer; no Root-owned `EXTERNAL` row, because this carrier's applied row consumes none of the OI-008 Root semantics (login home, `proposal.*` events, delegation-policy field).
- Fence results: F1 (SCC-001 membership) NONE; F2 (Root path) NONE; F3 (permitted effect) NONE. `FENCE_F1_CANDIDATES` none; `FENCE_F2_CANDIDATES` none.
- NEEDS_HUMAN_GRAPH_DECISION: DEP-04-04-004. The DEL-04-02 resolved mode/tool-surface relation is restated in live bytes (`ScopeOfWork.md` CLM-017 and CLM-025) but the row stays RETIRED per RUL-SCC-001-TRANCHE-001; reactivating it would recreate the DEL-04-02 <-> DEL-04-04 bidirectional pair against ACTIVE DEP-04-02-007. Default proposed: keep RETIRED; no change was made.
- CONFLICT (non-blocking): `_CONTEXT.md#Traceability` still lists `CoversScopeItems | SOW-017, SOW-030` while the applied row L329 and the `ScopeOfWork.md` front matter list SOW-017, SOW-030, SOW-081, SOW-084. The applied row controls; the anchors follow it. Surfaced for the WI alignment owner.
- [WARNING] PROJECT_ID_FORMAT_PROFILE: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities (`PKG-NN`, `DEL-NN-NN`, `DEP-NN-NN-NNN`, `SOW-NNN`); OBJ IDs pass. No accepted ID was changed.
- [WARNING] UNKNOWN_TARGET: DEP-04-04-008 consuming deliverable/interface remains `UNKNOWN` / `TBD`; the fingerprint payload now includes the organisation-layer pin and roadmap hash per the seated item.
- [WARNING] INSTRUCTION_ROOT_ENV: `CHIRALITY_INSTRUCTION_ROOT` was not set in the dispatch shell; `INSTRUCTION_ROOT` was resolved to `REPO_ROOT` per `docs/TYPES.md` (root-product development) and the brief's repo-root-relative `agents/` and `skills/` paths. ASSUMPTION recorded in the run record.
- [RESOLVED] PRD_HASH_MISMATCH: `_REFERENCES.md` REF-006 is MATCH under D-APP-38; DEP-04-04-007 re-evidenced and marked SATISFIED (PROPOSAL; owner may prefer RETIRED).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present. Schema: `validate_dependencies_schema.py` VALID, 29 columns, 14 data rows; all emitted enum values VALID; `DependencyID` unique; `FromDeliverableID=DEL-04-04` on every row.

## Run History

| Timestamp | Mode | Strictness | Decomposition | ACTIVE Anchors | ACTIVE Execution | Warnings |
|---|---|---|---|---:|---:|---|
| 2026-05-20T19:35:58-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found | 3 | 5 | PRD_HASH_MISMATCH; UNKNOWN_TARGET |
| 2026-09-05T00:37:34-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at pinned identity `c7c05169...771e61` (commit `dbd812a5`) | 7 | 6 | PROJECT_ID_FORMAT_PROFILE; UNKNOWN_TARGET; INSTRUCTION_ROOT_ENV; NEEDS_HUMAN_GRAPH_DECISION (DEP-04-04-004) |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 13 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 8 |
| PENDING | 2 |
| SATISFIED | 1 |
| TBD | 3 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Reconcile one parent anchor (DEP-04-04-001), four scope-ref trace anchors (SOW-017, SOW-030, SOW-081, SOW-084), two objective trace anchors (OBJ-004, OBJ-007), four re-evidenced ACTIVE execution rows (DEP-04-04-005 to -008), two new ACTIVE upstream interface rows (DEP-04-04-013 DEL-07-03; DEP-04-04-014 DEL-07-01), and one retained RETIRED row (DEP-04-04-004).
- Cross-register observation for reconciliation only (not a source for this register): DEL-04-02 `DEP-04-02-007` self-declares consumption of PersonaComposer output, and DEL-08-02 `DEP-08-02-012` declares the shared persona-name contract downstream to DEL-04-04; DEP-04-04-008's consumer stays `UNKNOWN` until an accepted local source names it.
- Graph posture: DEL-04-04 is not a member of SCC-001; no new edge targets an SCC-001 member; DEP-04-04-004 remains the owner-ruled retired reciprocal. Resolve the DEP-04-04-004 question under `docs/CYCLE_DRIVEN_RESOLUTION.md` before any reactivation.
- Open items for the seated work: DEP-04-04-013 and -014 are PENDING until `DEL-07-03-V3-01` lands and `DEL-07-01-V3-01` is selected per the `_STATUS.md` gate line.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-123
- **Current counts:** ACTIVE 7; RETIRED 1; NOT_APPLICABLE=4; TBD=4.
- **Correction:** DEP-04-04-004 is RETIRED; range citations exclude that row.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- 2026-09-05 note: the counts above are the dated D-APP-56 mirror; the Lifecycle Summary above supersedes them after the SCA-APP-010 dependency-closure pass.
