# Dependencies: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

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
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Defaults used: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`, `EXECUTION_DOC_ORDER=AUTO` resolved to `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Human read boundary applied: `_STATUS.md` was not read because it was not in the allowed evidence list for dependency extraction.
- `[WARNING] REF-006_HASH_MISMATCH`: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived details remain source-state-warning context.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row is present.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-05-02-011` from a coarse deliverable edge into document-scoped UIEvent/HarnessEvent separation evidence; the row remains active and in objective.

## Extracted Dependency Register

Source register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| ACTIVE rows | 15 |
| RETIRED rows | 1 |
| ANCHOR rows | 6 |
| EXECUTION rows | 10 |

### Active Rows

| DependencyID | Class | Type | Target | Status |
|---|---|---|---|---|
| DEP-05-02-001 | ANCHOR | OTHER | PKG-05 Session Audit Replay and Tool Result Records | ACTIVE |
| DEP-05-02-002 | ANCHOR | OTHER | SOW-014 App accepted-input submission and daemon pre-execution record conformance | ACTIVE |
| DEP-05-02-003 | ANCHOR | OTHER | SOW-015 App terminal-outcome presentation and durable daemon-record conformance | ACTIVE |
| DEP-05-02-004 | ANCHOR | OTHER | SOW-039 App consumption and conformance for append-only daemon HarnessEvent JSONL | ACTIVE |
| DEP-05-02-005 | ANCHOR | OTHER | OBJ-003 Make App-consumed accepted turns provider/SDK messages terminal outcomes tool activity and replay auditable while distinguishing daemon operational records from checkout-contained project evidence | ACTIVE |
| DEP-05-02-006 | EXECUTION | INTERFACE | DEL-05-01 Canonical Session Folder and Legacy Session Migration | ACTIVE |
| DEP-05-02-008 | EXECUTION | ENABLES | DEL-05-04 Runtime Replay Dialogue and Agent Transcript Projection | ACTIVE |
| DEP-05-02-009 | EXECUTION | CONSTRAINT | DEL-05-03 Redacted RunLogger and Secret Hygiene | ACTIVE |
| DEP-05-02-010 | EXECUTION | INTERFACE | DEL-05-05 ToolResultStore and Session Artifacts | ACTIVE |
| DEP-05-02-011 | EXECUTION | INTERFACE | DOCUMENT DEL-03-03-UIEVENT_HARNESSEVENT_SEPARATION UIEvent/HarnessEvent separation contract | ACTIVE |
| DEP-05-02-012 | EXECUTION | INTERFACE | DEL-04-03 SdkMessageMapper and Provider-Neutral Translation | ACTIVE |
| DEP-05-02-013 | EXECUTION | INTERFACE | Root-owned daemon HarnessEvent records (closed schema v2) | ACTIVE |
| DEP-05-02-014 | ANCHOR | OTHER | SOW-082 Prompted specification ladder: propose tool additive proposal.* event consumption proposal card and instruction-package proposal clauses | ACTIVE |
| DEP-05-02-015 | EXECUTION | PREREQUISITE | Root DEL-02-10 acceptance of the additive proposal.* event types against HarnessEvent schema v2 (routed return notice) | ACTIVE |
| DEP-05-02-016 | EXECUTION | INTERFACE | DEL-02-02 Right-Panel Coordination Workflows and Proposal UX | ACTIVE |

### Retired Rows

| DependencyID | Class | Type | Target | Status |
|---|---|---|---|---|
| DEP-05-02-007 | EXECUTION | INTERFACE | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | RETIRED |

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-05-02-013`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L323`; quote: "Consume Root-owned daemon HarnessEvent records for App audit/replay surfaces".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run Notes - 2026-09-05 SCA-APP-010 dependency closure (report-only preview)

- `TASK + dependency-extract` (Claude Code subagent; TASK role not mechanically enforced) dispatched by HELP_HUMAN as `N1-TASK-DEL-05-02` under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`; authorization SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-013 and DEP-014 (report-only preview; `ApplyEdits: false`). This file is the proposed post-image; the carrier register is unchanged until the reviewed write pass. Revised 2026-09-05 under brief amendment v1.1 (`execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md`, sections A, B, and D) by a fresh instance; this post-image supersedes the v1 preview.
- Overrides: `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `_STATUS.md` read only for its `## Remaining` section; `_REFERENCES.md` read for pointer resolution; `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` excluded.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches the `ScopeOfWork.md` pin); companion register SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`; basis `origin/main` `d66395d101143df68d956984f7ab93f5027418ec`. Applied row L337; Scope Ledger L417 (SOW-014), L418 (SOW-015), L442 (SOW-039), L485 (SOW-082); SSOW L252; OBJ-003 L264; PKG-05 L283; OI-008 L602; DEC-025 L634.
- Pass 1 (ANCHOR): the parent anchor and the SOW-014/015/039 and OBJ-003 trace anchors are preserved with their IDs and re-evidenced from the retired `Datasheet.md` to `ScopeOfWork.md` (front matter `project_scope_refs` / `package_objective_refs`, the Purpose section, and CLM-002); anchor labels refreshed to the applied ledger and objective text. New anchor `DEP-05-02-014` (SOW-082) added from the applied row scope refs. No scope ref left the applied row, so no anchor is retired.
- Pass 2 (EXECUTION): rows 006, 008, 011, and 013 re-evidenced to live bytes (`ScopeOfWork.md#CLM-017`, `#CLM-009`, decomposition `#L337`); `DEP-05-02-011` document pointer moved from the retired DEL-03-03 `Specification.md` to DEL-03-03 `ScopeOfWork.md#CLM-009` (DEL-03-03-REQ-005); `DEP-05-02-015` (Root DEL-02-10 acceptance of the additive `proposal.*` types; EXTERNAL; `TargetLocation=TBD`; PENDING) added from the applied row prose, Scope Ledger L485, OI-008, and the seated `DEL-05-02-V3-02` item; the DEL-02-02 proposal-card edge first proposed as `DEP-05-02-016` was held at preview and is emitted 2026-09-05 under D-APP-109 (see the EMITTED bullet below and the D-APP-109 Run Notes). Under amendment v1.1 section B, SCC-internal rows `DEP-05-02-009`, `-010`, and `-012` are re-evidenced (evidence fields only) from the retired `Specification.md#scope` / `Procedure.md#steps` to `ScopeOfWork.md#CLM-009` (lines 183 and 185) and `ScopeOfWork.md#CLM-017` (step 8, line 337); each row's existing `EvidenceQuote` is verbatim in those live lines and is unchanged; `TargetLocation` on these rows is a section anchor (no line pointer to refresh); `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, `FirstSeen`, and `Notes` are unchanged.
- Fence F1 (SCC-001 member: DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05 per `Evidence/baseline_closure/scc_summary.csv`): no new EXECUTION row has both endpoints inside SCC-001; no SCC-internal row is retired; SCC-internal rows `DEP-05-02-009`, `-010`, `-012` differ from the pre-image only in `EvidenceFile`, `SourceRef`, and `LastSeen` (amendment v1.1 section B; every frozen field byte-identical); `DEP-05-02-007` (RETIRED) is byte-identical. Result: NONE.
- Fence F2 (Root path): every Root-owned target (`DEP-05-02-013`, `DEP-05-02-015`) is `EXTERNAL` with `TargetLocation=TBD`; every other `TargetLocation` is under `projects/chirality-app-dev/**`. Result: NONE.
- Fence F3 (permitted effect): new rows are limited to the SOW-082 relations introduced by the amended applied row. Considered and not emitted: DEL-06-03 (`propose` tool owner; the events reach this carrier only through the Root-owned record), DEL-08-01 (instruction-clause conformance; no artifact exchanged), DEL-09-02/DEL-09-03 (ledger co-listing; structural), D-APP-68 `coordination.*` vocabulary ownership boundary (CLM-028; ownership statement, not a transfer), and the reciprocal DEL-02-02-V3-04 "fixture path first" signal in `_STATUS.md` (co-development ordering; would create a bidirectional pair). Result: NONE.
- EMITTED under D-APP-109 (H-016): DEP-05-02-016 — DEL-05-02 -> DEL-02-02 (DOWNSTREAM INTERFACE; consumed `proposal.*` events supplied to the DEL-02-02 transcript proposal card) — cycle-participating, non-gating until the SCC is resolved by a recorded move. Held at preview under amendment v1.1 section A (AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-016) because the fan-in simulation (`Evidence/fanin_simulation_v1/`) showed it lies on a cycle with the other held edges; written 2026-09-05 by `N9-TASK-DEL-05-02` under the owner ruling `execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`.
- `NEEDS_HUMAN_GRAPH_DECISION`: none. The v1 preview listed `DEP-05-02-009`, `-010`, `-012` because their evidence pointers named the retired legacy kit; amendment v1.1 section B permits the evidence-field refresh, which this revision applied, and every ACTIVE row now resolves to live bytes. The v1 `SCC_INTERNAL_EVIDENCE_POINTER_STALE` warning is cleared and no longer emitted.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities (`DEL-05-02`, `PKG-05`, `DEP-05-02-0nn`, `DEL-02-02`, `SOW-082`); no ID changed.
- `ASSUMPTION`: the outbound App notice `execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` named by `_STATUS.md` `DEL-05-02-V3-02` was not found at the basis commit; `DEP-05-02-015` records the Root return as TBD.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor. Schema validation: PASS (29 columns, 15 data rows). Enum validation: 25 distinct emitted values, all VALID. `DependencyID` unique (`DEP-05-02-016` reserved and absent at preview; emitted 2026-09-05 under D-APP-109); `FromDeliverableID=DEL-05-02` on every row; `Status=CANDIDATE` absent; no row deleted.
- Register convention preserved: no quoted CSV fields; commas omitted from refreshed labels (as the OBJ-003 row already did).

## Run Notes - 2026-09-05 D-APP-109 held-edge emission (additive UPDATE)

- `TASK + dependency-extract` (Claude Code subagent; TASK role not mechanically enforced) dispatched by HELP_HUMAN as `N9-TASK-DEL-05-02` under run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/` (plan amendment v1.2, node N9); `ApplyEdits: true`; authorization: owner ruling D-APP-109 (`execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md`), `AMENDMENT_v1.2_OWNER_RULING.md`, and SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-013 / DEP-014. Basis: candidate branch `claude/sca-app-010-dependency-closure` at `f38f1448675b8e9f40f33932a11b7ffa4126fe69`; pre-images `Dependencies.csv` `7a6da98003c9fc93caf3c602c09e242abb6105e90a1e45cff25e67d4a18f5380`, `_DEPENDENCIES.md` `8823be430d59a5060bff63a17d1474ff48c09ddc77a2ee7006dec0c7a91539a0` (both matched before the write).
- Overrides: `MODE=UPDATE` (additive; exactly the reserved row); `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; no re-extraction of existing rows (every pre-existing row byte-identical; no `LastSeen` refresh; no retirement).
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed); DEL-02-02 resolved at applied row L308 (`Right-Panel Coordination, Workflows, and Proposal UX`, PKG-02; label written without commas per this register's convention).
- Row written: `DEP-05-02-016` (H-016) — EXECUTION / NOT_APPLICABLE / DOWNSTREAM / INTERFACE / DELIVERABLE DEL-02-02 (PKG-02); `Confidence=MEDIUM`; `SatisfactionStatus=TBD`; `EvidenceFile=ScopeOfWork.md`, `SourceRef=ScopeOfWork.md#current-responsibility` (live lines 35-36; quote verbatim once the backticks around `proposal.*` are dropped and the wrapped lines joined, the same disclosed convention as rows 001-004, 006, 011, and 013). Statement, evidence, confidence, and the FACT/PROPOSAL note are as captured in `HELD_EDGE_PROPOSALS.csv` H-016 and `instances/N1-TASK-DEL-05-02/PREVIEW.md` Section 2a. `TargetRefID` empty and `TargetLocation` `#8-deliverables`, following this register's other DELIVERABLE rows (the brief's `#L<n>` form is carried in `Notes` as L308). `Notes` is the only quoted CSV field (the mandated D-APP-109 clause contains commas).
- `CONFLICT` corrected at emission: the H-016 `Notes` as captured ended "Neither endpoint is an SCC-001 member"; `Evidence/baseline_closure/scc_summary.csv` lists DEL-05-02 among the nine SCC-001 members (as the preview header and the N3 run record also state) and DEL-02-02 is not a member. The written row carries the corrected sentence and names the source; no other captured text changed.
- SCC posture (recorded, not linearized): under D-APP-109 the fifteen held edges are emitted together; the fan-in simulation (`Evidence/fanin_simulation_v1/`) showed this edge lies on a cycle with the other held edges and joins SCC-001 into the enlarged SCC. `DEP-05-02-016` is `CYCLE_PARTICIPATING` and non-gating (no blocker queue, wave, dispatch-readiness, or implementation-readiness effect) until that SCC is resolved by a recorded decompose, invert, merge, or cut move (`docs/CYCLE_DRIVEN_RESOLUTION.md`). No SCC is resolved by this run. The fresh AUDIT_DEP_CLOSURE run (N11) records the post-emission picture.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities (`DEL-05-02`, `PKG-05`, `DEP-05-02-016`, `DEL-02-02`, `PKG-02`); no ID changed.
- `[WARNING] CYCLE_PARTICIPATING`: one ACTIVE row (`DEP-05-02-016`) is inside an unresolved SCC after emission; treat it as non-gating pending a recorded move.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor. Schema validation: PASS (29 columns, 16 data rows). Enum validation: every enum value on the written row VALID. `DependencyID` unique (`DEP-05-02-016` present exactly once); `FromDeliverableID=DEL-05-02` on every row; `Status=CANDIDATE` absent; no row deleted; register stays ID-ordered.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:22-06:00 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used | REF-006_HASH_MISMATCH | 12 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | 12 |
| 2026-09-05T01:00:46-06:00 | UPDATE (report-only preview; SCA-APP-010 DEP-013/DEP-014; brief v1 + amendment v1.1) | CONSERVATIVE | applied `dbd812a52` SHA-256 `c7c05169…771e61` found at the pinned identity | PROJECT_ID_FORMAT_PROFILE; one held proposal (DEP-05-02-016 reserved; H-016) | 14 |
| 2026-09-05T07:58-0600 (D-APP-109 emission) | UPDATE (additive; held row DEP-05-02-016 emitted; amendment v1.2 N9) | CONSERVATIVE | applied `dbd812a52` SHA-256 `c7c05169…771e61` found at the pinned identity | PROJECT_ID_FORMAT_PROFILE; CYCLE_PARTICIPATING (DEP-05-02-016 non-gating pending SCC resolution) | 15 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 15 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| PENDING | 2 |
| NOT_APPLICABLE | 7 |
| TBD | 7 |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`. This register is deliverable-local; the project graph is rebuilt by AUDIT_DEP_CLOSURE (`tools/coordination/analyze_dep_closure.py`) after the reviewed write pass and again after the D-APP-109 emission (N11).
- Cycle-participating rows: this carrier now carries one cycle-participating, non-gating row, `DEP-05-02-016` (DEL-05-02 -> DEL-02-02, DOWNSTREAM INTERFACE), emitted 2026-09-05 under D-APP-109 together with the other held edges; it lies inside the enlarged SCC-001 after emission and drives no blocker queue, wave, dispatch-readiness, or implementation-readiness claim until that SCC is resolved by a recorded decompose, invert, merge, or cut move (`docs/CYCLE_DRIVEN_RESOLUTION.md`). The seated items' own `Depends` lines and named gates remain the executable ordering.
- SCC-001 rows from the reviewed write pass: no SCC-internal edge was retired or re-pointed; SCC-internal rows 009, 010, and 012 cite live `ScopeOfWork.md` bytes (evidence fields only, amendment v1.1 section B); their endpoints, direction, type, and status are byte-identical to the pre-image of that pass.
- Root-gated rows: `DEP-05-02-013` (closed `HarnessEvent` schema v2) and `DEP-05-02-015` (additive `proposal.*` acceptance) stay `PENDING` with `TargetLocation=TBD` until the Root DEL-02-10 returns are routed to App (OI-008); the seated items `DEL-05-02-V3-01` and `DEL-05-02-V3-02` are `NOT_SELECTABLE_UNTIL` those returns.
- The DEL-05-02 -> DEL-02-02 proposal-card edge (H-016) is now emitted as `DEP-05-02-016`; the reciprocal DEL-02-02 -> DEL-05-02 UPSTREAM row is H-002 (`DEP-02-02-015`) in the DEL-02-02 register under the same ruling. Reconciliation should read both as cycle-participating and non-gating pending SCC resolution; `DEP-05-02-016` consumption remains gated by `DEP-05-02-015` (Root DEL-02-10 acceptance).
- Labels on anchor rows now match the applied Scope Ledger and objective text; concordance checks should compare against decomposition lines L417, L418, L442, L485, and L264.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-125
- **Current counts:** ACTIVE 11; RETIRED 1; NOT_APPLICABLE=6; TBD=6.
- **Correction:** DEP-05-02-007 is RETIRED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
