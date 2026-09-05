# PREVIEW — N1-TASK-DEL-06-03 — TASK + dependency-extract (REPORT-ONLY) — amendment v1.1 rerun

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-06-03` (run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N1, parent HELP_HUMAN) |
| Brief | `LAUNCH_BRIEF.md` v1 (still binding) narrowed by `AMENDMENT_v1.1_N1_PREVIEWS.md` section A (hold DEP-06-03-014 as H-017), section C item 6 (H-1 stays non-emitted; analyzer replay disclosure accepted as non-load-bearing), and section D (rerun contract). This rerun supersedes the 00:41 v1 preview of the same instance; the v1 run record `_run_records/TASK_RUN_2026-09-05_0041.md` stays. |
| Carrier | `DEL-06-03` Initial Chirality MCP Read Tools (BACKEND_FEATURE_SLICE, PKG-06); folder `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools` (untouched) |
| Authorization | SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-015 / DEP-016 (report-only preview; no carrier write) |
| Basis | `HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` (origin/main, PR #713 merge); carrier, decomposition, and pointer paths unchanged from basis |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches) at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; applied row L348; SOW-082 L252; reverse view L404-487; OI-008 L602; DEC-025 L634 |
| Companion identities | `contract_invariant_coverage_register.csv` `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (matches); `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (matches); authority corpus v20, `_REFERENCES.md` REF-001..REF-007 all MATCH |
| Pre-image `Dependencies.csv` | `b9802d035476e9781c89e71cb49415bcb98206c0ad310420ae61b1bf8361918c` (matches brief; 9 data rows; recomputed at rerun start) |
| Pre-image `_DEPENDENCIES.md` | `9dc38450f2525d2d59cd8356b94e4331ec789b0de41d070b3ebc451dbbc18e9c` (matches brief; recomputed at rerun start) |
| Post-image `POSTIMAGE_Dependencies.csv` | `89a579e740656560f565c41c9f536dbfe99038d86d65faae93f882134f682d02` (17 data rows, 29 columns, LF, final newline; v1 was `80451a3ade2c9dad3ea0de976a4d7ee19abf35efef5f67fa52ecfbe11563b84e` with 18 rows) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `d9140c2f599150cd3f7ab82124b12a3aad6b0a137a6c5636d4cf37f89bba3800` (v1 was `9cf2b811aacbc317c78f1ec0193927f7ea9a4381bd1e198b7fff3cd29b4ecb5c`) |
| Source identities read | `ScopeOfWork.md` `041009ac09e0996185598aa14b92b1343d2c7f1e34eacc2db1499267f6db7c47`; `_CONTEXT.md` `4a554b7099fd221a0e8f4f000f9b1113ecfdd735583fef3d4b2103ff62f4047a`; `_STATUS.md` `80f318ddef30469f261d455af85163a541731e4ed18f4a2fd70eae3f8281d79f`; `_REFERENCES.md` `1365d3e113487568b61f90597df0d3008036b2ed9ddf9eac1f85ff7bcca0e947` (identical to the v1 preview; unchanged after the rerun) |

Row census (total / ACTIVE / RETIRED / ANCHOR / EXECUTION):

| Image | Total | ACTIVE | RETIRED | ANCHOR | EXECUTION |
|---|---:|---:|---:|---:|---:|
| Pre | 9 | 9 | 0 | 3 | 6 |
| Post (v1, superseded) | 18 | 18 | 0 | 7 | 11 |
| Post (v1.1, this rerun) | 17 | 17 | 0 | 7 | 10 |

Satisfaction across all post-image rows: SATISFIED 9 / PENDING 4 / TBD 4. Post-image by type: OTHER 7, PREREQUISITE 3, INTERFACE 4, HANDOVER 2, CONSTRAINT 1. Every pre-image `DependencyID` is preserved; nothing is deleted from the carrier register; nothing is retired (every pre-image relation is still stated in live sources); `Status=CANDIDATE` is not emitted. One v1-proposed row (DEP-06-03-014) is held under amendment v1.1: it was never written to the carrier, so its removal from the post-image is not a register deletion; the ID stays reserved for H-017 and rows 015 to 018 are not renumbered.

## 2. Row-level diff (every post-image row)

`UNCHANGED` means byte-identical to the pre-image line. No retained row is byte-identical because every row received `LastSeen=2026-09-05` and a refreshed `Notes`; the classification distinguishes rows whose `EvidenceFile` moved off the retired kit (`RE-EVIDENCED`) from rows whose pointers were only refreshed (`REFRESHED`). Every row below is byte-identical to its v1 post-image line; the only CSV change in this rerun is the removal of the DEP-06-03-014 line.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-06-03-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | WBS_NODE PKG-06 | `ScopeOfWork.md#CLM-002 Identification lines 73-88` | Was `Datasheet.md#Identification`; identity also in `_CONTEXT.md` lines 5-16; applied row L348. SATISFIED. |
| DEP-06-03-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-048 | `_CONTEXT.md#Traceability lines 41-47` | Pointer moved from lines 34-40; quote now includes SOW-064; reverse view L451. SATISFIED. |
| DEP-06-03-003 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-050 | `_CONTEXT.md#Traceability lines 41-47` | As 002; reverse view L453. SATISFIED. |
| DEP-06-03-004 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT DECOMP-v3.2 | `ScopeOfWork.md#CLM-019 Prerequisites lines 304-316` | Was `Procedure.md#Prerequisites`; front matter line 5 pins `@dbd812a5…`. SATISFIED. |
| DEP-06-03-005 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-002/REF-003/REF-006 | `ScopeOfWork.md#CLM-019 Prerequisites lines 304-316` | Was `Procedure.md#Prerequisites`; `TargetLocation` names repo-root `docs/*.md` already pinned by `_REFERENCES.md` (F2-permitted); corpus v20. SATISFIED. |
| DEP-06-03-006 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-06-01 | `ScopeOfWork.md#REQ-06-03-006 line 203` | Was `Specification.md#Requirements`; DEL-06-01 named at CLM-019 line 313 and CLM-021 step 11 line 378. TBD. |
| DEP-06-03-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-07-05 | `ScopeOfWork.md#CLM-028 Considerations lines 472-485` | Was `Guidance.md#Considerations`; exact quote at line 480; REQ-06-03-015 line 212. TBD. |
| DEP-06-03-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | UNKNOWN status lifecycle API owner | `ScopeOfWork.md#CLM-005 Construction lines 122-135` | Was `Datasheet.md#Construction`; target kept UNKNOWN; CLM-020 line 326 names DEL-07-04 (NEEDS_HUMAN_GRAPH_DECISION 2). TBD. |
| DEP-06-03-009 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | UNKNOWN Chirality runtime event path | `ScopeOfWork.md#CLM-021 Steps lines 368-370` | Was `Procedure.md#Steps`; `EvidenceQuote` replaced with the exact live step-9 sentence (the pre-image quote was a comma-stripped paraphrase that no longer resolved). TBD. |
| DEP-06-03-010 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-064 | `ScopeOfWork.md#Purpose and Objective Traceability line 14` | On applied row L348 and front matter line 6 but never anchored (D-APP-80 note, lines 18-20); reverse view L467. SATISFIED. |
| DEP-06-03-011 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-082 | `ScopeOfWork.md#Purpose and Objective Traceability line 14` | New on the applied row under DEC-025; SOW-082 L252 / L485; seated as DEL-06-03-V3-01. SATISFIED. |
| DEP-06-03-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-005 | `ScopeOfWork.md#Purpose and Objective Traceability line 14` | Objective anchor; `TargetType=UNKNOWN` objective convention with the existing note (amendment C.7); label from Section 6 L267. SATISFIED. |
| DEP-06-03-013 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-006 | `ScopeOfWork.md#Purpose and Objective Traceability line 14` | As 012; label from Section 6 L268. SATISFIED. |
| DEP-06-03-015 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | UNKNOWN instruction-root roster and policy values | `_STATUS.md#Remaining DEL-06-03-V3-01 Depends line 14` | Owner not named in carrier sources; PROPOSAL only (SOW-030 L433; SOW-084 L487). PENDING. |
| DEP-06-03-016 | ADDED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | DELIVERABLE DEL-02-02 | `_STATUS.md#Remaining DEL-06-03-V3-01 Depends line 14` | `proposal.offered` consumed by the proposal card and rung forms (SOW-082 L485); the `NOT_SELECTABLE_UNTIL` gate is not encoded. PENDING. |
| DEP-06-03-017 | ADDED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | DELIVERABLE DEL-05-02 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L485` | DEL-05-02 consumes the additive `proposal.*` event types after Root acceptance (L252). SCC-001 adjacency disclosed in section 3. PENDING. |
| DEP-06-03-018 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | EXTERNAL `ROOT:DEL-02-10` (TargetLocation TBD) | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L252` | Additive `proposal.*` acceptance against closed `HarnessEvent` schema v2 (K-EVENT-3), OI-008 L602; Q13 ruled (`_STATUS.md` line 13). PENDING. |

Reserved, not in the post-image: **DEP-06-03-014** (held proposal H-017; see the next section). Held candidate with no `DependencyID` allocated: **H-1** DEL-06-02 catalog validation and collision prevention of the registered `propose` tool — see NEEDS_HUMAN_GRAPH_DECISION 1.

## Held proposals (amendment v1.1)

| HeldID | Reserved DependencyID | Edge | Relation | Evidence it would have cited | Why held |
|---|---|---|---|---|---|
| H-017 | DEP-06-03-014 | DEL-06-03 -> DEL-08-01 | UPSTREAM INTERFACE, DELIVERABLE DEL-08-01 Instruction Root Packaging and Agent Conformance; Statement: "The propose tool offers only the few triggers named by DEL-08-01 instruction-package clauses in the Agent 0 and Agent 1 packages and resolves plan references from Agent 1 procedures."; SatisfactionStatus PENDING; Confidence HIGH | `_STATUS.md#Remaining DEL-06-03-V3-01 Depends line 14` quote `DEL-08-01-V3-01 (clauses naming the triggers)` (owner-adopted seating, D-APP-108); amended Scope Ledger row SOW-082 L252 (instruction-package clauses naming the few triggers) and reverse view L485 (DEL-08-01 owns instruction-clause conformance); `ScopeOfWork.md` line 52 (resolves plan references from Agent 1 procedures); DEL-08-01 applied row L368 (proposal clauses and named triggers) | The fan-in simulation with all thirteen post-images substituted (`Evidence/fanin_simulation_v1/edge_analysis.json`, `held_by_carrier.json`) shows this edge and the reciprocal DEL-08-01 proposal `DEP-08-01-018` (H-018) together form a new two-node SCC DEL-06-03/DEL-08-01, while either alone changes nothing. SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3 requires the SCC set unchanged unless separately ruled; `docs/CYCLE_DRIVEN_RESOLUTION.md` makes the choice a human-gated cut. Recorded in `HELD_EDGE_PROPOSALS.csv` H-017 with disposition `HELD_NON_EMITTED_PENDING_OWNER_RULING`; carried to the owner's separate transaction. |

The v1 preview's own F1 test for this row was correct as stated (DEL-08-01 is not an SCC-001 member and no SCC-001 member reaches DEL-06-03); the hold arises only from the cross-carrier combination that no single preview could see.

## 3. Fence results

- **F1 (SCC-001 membership): NONE.** DEL-06-03 is not a member of SCC-001 (`DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05`). Direct test from the brief, re-run 2026-09-05 01:00 over all 52 live registers: the only rows anywhere that target DEL-06-03 are `DEP-06-02-006` (DEL-06-02, ACTIVE), `DEP-09-02-020` (DEL-09-02, ACTIVE), and `DEP-06-01-013` (DEL-06-01, RETIRED); no SCC-001 member holds an active row back to this carrier. The v1 preview's supplementary read-only replay of the registered analyzer over all 52 registers with the v1 post-image substituted found SCCs unchanged (the single nine-node SCC-001) and DEL-06-03 with no path into it; the v1.1 post-image differs from v1 only by removing the edge DEL-06-03 -> DEL-08-01, and removing an edge cannot create a cycle, so that finding stands for the revised post-image without a second replay (none was run in this rerun).
  - **SCC-001 adjacency disclosure:** DEP-06-03-017 targets SCC-001 member DEL-05-02 as a DOWNSTREAM handover (analyzer edge DEL-05-02 -> DEL-06-03). This is not an edge inside SCC-001 and does not enlarge it, because SCC-001 already reached DEL-06-03 through DEL-06-02 and DEL-09-02 and DEL-06-03 reaches no member. Listed so the N2 reviewer and N4 audit can confirm rather than discover it.
- **F2 (Root path): NONE.** No `TargetLocation` names a Root path. The Root-owned target (DEP-06-03-018) is `EXTERNAL` with `TargetLocation=TBD`. Retained `TargetLocation` values name `execution/_Decomposition/...` (under `projects/chirality-app-dev/**`) or repo-root `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/PRD.md`, which `_REFERENCES.md` pins as REF-002/REF-003/REF-006.
- **F3 (permitted effect): NONE.** Every added row traces to SOW-082 (L252/L485), the applied row prose (L348), the ScopeOfWork Gate-5 section (line 52), or the owner-adopted DEL-06-03-V3-01 `Depends` line (`_STATUS.md` line 14). No edge was inferred from the item's `NOT_SELECTABLE_UNTIL` gate, from SCC ordering, or from a keep-aligned statement. The anchors for the pre-existing ref SOW-064 and the objectives OBJ-005/OBJ-006 are Pass 1 anchors required by the brief's Method step 2, not execution edges.
- **NEEDS_HUMAN_GRAPH_DECISION** (both carried unchanged from v1; amendment C.6 confirms H-1 stays non-emitted and is carried to the owner slate):
  1. **H-1 (held, not emitted; no `DependencyID` allocated): DEL-06-02 catalog validation.** Evidence: `_STATUS.md` line 14 `Depends: ... DEL-06-02 catalog validation`; applied row L348 Notes `catalog validation and collision prevention remain DEL-06-02`; SOW-082 L485 `DEL-06-02 retains catalog and collision validation`; ScopeOfWork CLM-035 (D-APP-68 composition) lines 560-581. Read as UPSTREAM CONSTRAINT (this carrier requires DEL-06-02 validation of the registered `propose` descriptor) it adds analyzer edge DEL-06-03 -> DEL-06-02, and DEL-06-02 already holds ACTIVE `DEP-06-02-006` (UPSTREAM INTERFACE: "The resolver must register or reference Chirality MCP read tool definitions from DEL-06-03"), so the pair forms a **new two-node SCC {DEL-06-02, DEL-06-03}**; the cycle is visible from `DEP-06-02-006` alone. Per `docs/CYCLE_DRIVEN_RESOLUTION.md` the cycle is surfaced, not linearized. Options: **decompose** (two non-cyclic edges: descriptor supply DOWNSTREAM from DEL-06-03 into the catalog; validation verdict as an EXTERNAL/PENDING constraint or as DEL-06-02's own DOWNSTREAM row), **invert** (hold it only as DEL-06-03 DOWNSTREAM HANDOVER of the `propose` descriptor into the DEL-06-02 catalog, mirroring DEP-06-02-006 without a reverse edge), **merge** (human-gated), **cut** (human-gated). The write instance allocates a `DependencyID` only after the ruling.
  2. **DEP-06-03-008 target resolution.** Live `ScopeOfWork.md` CLM-020 line 326 states the status reader's "final ownership should align with DEL-07-04", and decomposition SOW-028 L431 maps status lifecycle to DEL-07-04. Resolving `TargetType=UNKNOWN` to `DELIVERABLE DEL-07-04` would add analyzer edge DEL-06-03 -> DEL-07-04 but is outside the DEP-015 permitted effect (SOW-081..084 and revised SOW-001/002/004/006/007/008/010 relations). The post-image keeps the row UNKNOWN/TBD with a PROPOSAL note.
- **FENCE_F1_CANDIDATES:** none (no candidate would place DEL-06-03 inside SCC-001).
- **FENCE_F2_CANDIDATES:** none (no candidate needed a Root path; DEP-06-03-018 was expressible as EXTERNAL/TBD).

Considered and not emitted (no explicit transfer stated in this carrier's sources; unchanged from v1): declined-trigger and chat-rung state held by DEL-02-04 under revised SOW-008 (`_STATUS.md` line 15 places the once-per-chat state in this carrier's own write locus); the per-chat delegation-policy session-record field (SOW-083/SOW-010, Root DEL-02-11), which the specification tuple proposes rather than reads; DEL-04-04 plan-reference or roadmap-injection seams (SOW-081), which this carrier's sources do not name.

## 4. Validator outputs (verbatim)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py .../POSTIMAGE_Dependencies.csv`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-06-03/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 17
exit=0
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct value in the revised post-image across the ten enum fields; 26 invocations, all exit 0; the held row's values INTERFACE, DELIVERABLE, PENDING, and HIGH all remain present on other rows, so the distinct set is unchanged from v1):

```text
ANCHOR_TYPE IMPLEMENTS_NODE: VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
ANCHOR_TYPE NOT_APPLICABLE: VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
ANCHOR_TYPE TRACES_TO_REQUIREMENT: VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
CONFIDENCE HIGH: VALID: HIGH is a valid CONFIDENCE
CONFIDENCE MEDIUM: VALID: MEDIUM is a valid CONFIDENCE
DEPENDENCY_CLASS ANCHOR: VALID: ANCHOR is a valid DEPENDENCY_CLASS
DEPENDENCY_CLASS EXECUTION: VALID: EXECUTION is a valid DEPENDENCY_CLASS
DEPENDENCY_TYPE CONSTRAINT: VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE HANDOVER: VALID: HANDOVER is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE INTERFACE: VALID: INTERFACE is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE OTHER: VALID: OTHER is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE PREREQUISITE: VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
DIRECTION DOWNSTREAM: VALID: DOWNSTREAM is a valid DIRECTION
DIRECTION UPSTREAM: VALID: UPSTREAM is a valid DIRECTION
EXPLICITNESS EXPLICIT: VALID: EXPLICIT is a valid EXPLICITNESS
ORIGIN EXTRACTED: VALID: EXTRACTED is a valid ORIGIN
SATISFACTION_STATUS PENDING: VALID: PENDING is a valid SATISFACTION_STATUS
SATISFACTION_STATUS SATISFIED: VALID: SATISFIED is a valid SATISFACTION_STATUS
SATISFACTION_STATUS TBD: VALID: TBD is a valid SATISFACTION_STATUS
STATUS ACTIVE: VALID: ACTIVE is a valid STATUS
TARGET_TYPE DELIVERABLE: VALID: DELIVERABLE is a valid TARGET_TYPE
TARGET_TYPE DOCUMENT: VALID: DOCUMENT is a valid TARGET_TYPE
TARGET_TYPE EXTERNAL: VALID: EXTERNAL is a valid TARGET_TYPE
TARGET_TYPE REQUIREMENT: VALID: REQUIREMENT is a valid TARGET_TYPE
TARGET_TYPE UNKNOWN: VALID: UNKNOWN is a valid TARGET_TYPE
TARGET_TYPE WBS_NODE: VALID: WBS_NODE is a valid TARGET_TYPE
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```text
INVALID: DEL-06-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
exit=1
INVALID: PKG-06 does not match PKG format (^PKG-[0-9]{3}$)
exit=1
INVALID: DEP-06-03-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
exit=1
INVALID: DEP-06-03-018 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
exit=1
INVALID: SOW-082 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
exit=1
VALID: OBJ-005 matches OBJ format
exit=0
```

Anchor, integrity, evidence, and reconciliation checks (deterministic script over the revised post-image; the evidence check compares each `EvidenceQuote` to the cited line range after stripping markdown backticks, since the register quotes are the backtick-stripped live text):

```text
unique DependencyIDs: True 17
DEP-06-03-014 absent: True
FromDeliverableID all DEL-06-03: True
ACTIVE IMPLEMENTS_NODE count: 1 -> PASS
CANDIDATE status absent: True
non-deliverable targets have empty TargetDeliverableID: True
DELIVERABLE targets have TargetDeliverableID: True
EvidenceFile+SourceRef present on ACTIVE: True
No TargetLocation names a Root path: True | EXTERNAL rows TargetLocation: ['TBD']
DEP-06-03-001..018 (014 reserved): EvidenceFile resolves to a live file; every EvidenceQuote found within the cited line range after stripping markdown backticks: True []
total 17 ACTIVE 17 RETIRED 0 class {'ANCHOR': 7, 'EXECUTION': 10} type {'OTHER': 7, 'PREREQUISITE': 3, 'INTERFACE': 4, 'HANDOVER': 2, 'CONSTRAINT': 1} sat {'SATISFIED': 9, 'TBD': 4, 'PENDING': 4}
MD register rows: 17 == CSV ids: True
MD counts match: True [True, True, True, True, True, True, True]
2026-09-05 history row under Run History: True | 17 ACTIVE rows in that row: True
HELD bullet present in Run Notes: True
POSTIMAGE_Dependencies.csv: CR=0 trailing-ws=0 final-nl=0a
POSTIMAGE__DEPENDENCIES.md: CR=0 trailing-ws=0 final-nl=0a
```

Direct F1 register read (all 52 live `Dependencies.csv` registers):

```text
rows anywhere targeting DEL-06-03: [('DEL-06-01', 'DEP-06-01-013', 'UPSTREAM', 'INTERFACE', 'RETIRED'), ('DEL-06-02', 'DEP-06-02-006', 'UPSTREAM', 'INTERFACE', 'ACTIVE'), ('DEL-09-02', 'DEP-09-02-020', 'UPSTREAM', 'INTERFACE', 'ACTIVE')]
ACTIVE rows from SCC-001 members targeting DEL-06-03: []
```

Quoting convention: the retained v1 lines were kept byte-for-byte (per-field quoting preserved for retained rows; minimal quoting for added rows, as in v1); only the DEP-06-03-014 line was removed. Write scope: the carrier's `Dependencies.csv` and `_DEPENDENCIES.md` still hash to their pre-image values after the rerun.

## 5. Epistemic notes

- FACT (RE-EVIDENCED 001, 004-009): each relation is restated verbatim or near-verbatim (backticks stripped) in live `ScopeOfWork.md` CLM/REQ text; the cited line ranges were checked to contain the quotes.
- FACT (010, 011): scope refs are on the applied row and in the front matter; anchors only, no graph edge.
- FACT with convention (012, 013): objectives are explicit; `TargetType=UNKNOWN` follows the brief's objective convention (kept by amendment C.7) rather than claiming a requirement or WBS node.
- FACT (016): the owner-adopted `Depends` line states both the party and the transferred thing (`proposal.offered` consumption). Direction follows the flow of the event, not the selection gate.
- FACT, held (H-017 / reserved DEP-06-03-014): the relation to DEL-08-01 is stated with the same strength as 016 and is held only for the cross-carrier cycle; nothing about its evidence changed.
- FACT with unresolved owner (015): the input is stated; the owner is a PROPOSAL only.
- FACT, MEDIUM confidence (017): DEL-05-02's consumption is stated in the amended row rather than in a carrier-local document; Explicitness EXPLICIT because both parties and the artifact are named.
- FACT (018): Root-owned semantic stated in L252 and OI-008; carried as EXTERNAL/TBD by convention.
- PROPOSAL (008 note; H-1): graph changes held for owner decision as listed in section 3.
- ASSUMPTION: none required.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview, amendment v1.1 rerun), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
