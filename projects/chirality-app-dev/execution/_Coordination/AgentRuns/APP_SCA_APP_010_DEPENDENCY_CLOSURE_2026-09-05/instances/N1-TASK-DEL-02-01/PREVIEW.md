# PREVIEW — N1-TASK-DEL-02-01 — DEL-02-01 dependency extraction (report-only; amendment v1.1 rerun)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-02-01` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, Node N1); rewritten in place under `AMENDMENT_v1.1_N1_PREVIEWS.md` section D (v1 brief still binding; amendment narrows only) |
| Carrier | `DEL-02-01` Woven Dialogue Shell and Compatibility Navigation (UX_UI_SLICE, PKG-02); folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation` |
| Basis | `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` (HEAD verified equal) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (SCA-APP-010); authority corpus v20 (all `_REFERENCES.md` rows MATCH) |
| Pre-image `Dependencies.csv` | `5ca2d96b48ac962d4a9f9afef8bc07957fcac81889fc1ba441b94d899bcacd99` (verified) |
| Pre-image `_DEPENDENCIES.md` | `f60ddd1687e169bf3c0904f361d09601f4c9e7fa6a0966f939a92e90f8c83109` (verified) |
| Post-image `POSTIMAGE_Dependencies.csv` | `4af3d115b79d403c190661ba57050abe9bda04539cadf09cf9b07edf2d49c254` (v1 was `11da42b4ec14ac2beca22a86215d2ded987653640cb8bd10091399cfdb1aef92`) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `26a99f29ef68e00a9cc02839802142f099f67f7c5816cb461971a9ccb9a3ef49` (v1 was `51fbfeda61eaee9500d1b67757c1886cfbe649640d4c4d4e72b74554e2d7a5e0`) |
| Row census pre | total 8 / ACTIVE 8 / RETIRED 0 / ANCHOR 4 / EXECUTION 4 |
| Row census post | total 13 / ACTIVE 13 / RETIRED 0 / ANCHOR 4 / EXECUTION 9 (v1 was 14 / 14 / 0 / 4 / 10; one row held under amendment v1.1 section A, ID reserved) |
| Carrier folder | unchanged by this run (source hashes recorded in `POSTIMAGE__DEPENDENCIES.md` Run Notes) |

## 2. Row-level diff

`UNCHANGED` means byte-identical. No row is byte-identical because every row found this run carries `LastSeen=2026-09-05` and the applied deliverable name in `FromDeliverableName`.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-02-01-001 | REFRESHED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PACKAGE PKG-02 | `_CONTEXT.md#identity` | Package label refreshed to applied L280 name; validated against L307. |
| DEP-02-01-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-001 | `_CONTEXT.md#traceability` | Label refreshed to reverse view L404; amended ledger L171 (DEC-025). |
| DEP-02-01-003 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-005 | `_CONTEXT.md#traceability` | Label refreshed to reverse view L408; ledger L175 not amended. |
| DEP-02-01-004 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-001 | `_CONTEXT.md#traceability` | Label refreshed to L262; existing `TargetType=REQUIREMENT` convention kept (brief's `UNKNOWN` note does not match this pre-image). |
| DEP-02-01-005 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | UNKNOWN TBD (implementation workspace) | `ScopeOfWork.md#CLM-018` | Was `Procedure.md#prerequisites`; `frontend/**` paths withheld from `TargetLocation` (F2). |
| DEP-02-01-006 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | DELIVERABLE DEL-08-02 | `ScopeOfWork.md#CLM-027` | Was `Guidance.md#considerations`; label refreshed to L369; HGD-1 direction question. |
| DEP-02-01-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/INTERFACE | DELIVERABLE DEL-02-02 | `ScopeOfWork.md#CLM-027` | Was `Guidance.md#considerations`; label refreshed to L308; HGD-2 retire-or-keep. |
| DEP-02-01-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/INTERFACE | DELIVERABLE DEL-08-03 | `ScopeOfWork.md#CLM-027` | Was `Guidance.md#considerations`; HGD-2 retire-or-keep. |
| DEP-02-01-009 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-07-01 | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling); Current acceptance obligations 3` | Folder validation consumed; amended SOW-002 L172; seated V3-01/V3-03 Depends. |
| DEP-02-01-011 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | EXTERNAL `ROOT-DAEMON-SESSION-RECORD`, `TargetLocation=TBD`, PENDING | `_STATUS.md#remaining (DEL-02-01-V3-03 Depends)` | Composer context line and provider root from Root-owned session record; amended SOW-010 L180; OI-008. |
| DEP-02-01-012 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | UNKNOWN TBD (redaction helper, Q6) | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling); Current acceptance obligations 4` | Amended SOW-008 L178; likely owner DEL-05-03 is fenced (FC-1). |
| DEP-02-01-013 | ADDED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | DELIVERABLE DEL-09-04 | `_STATUS.md#remaining (DEL-02-01-V3-04 Return)` | Icon reproducibility record handed to DEL-09-04-V3-02. |
| DEP-02-01-014 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | DELIVERABLE DEL-01-03 | `_STATUS.md#remaining (DEL-02-01-V3-01 Return)` | Professional-boundary copy unchanged by the copy pass; MEDIUM confidence. |

Rows RETIRED: none (every legacy-kit relation is restated in live `ScopeOfWork.md` bytes; the brief's retirement rule therefore did not fire — see HGD-2 for the decomposition-level retirement question).

The ID `DEP-02-01-010` is absent from the post-image by design: it is reserved for the held proposal below and is not renumbered over.

## Held proposals (amendment v1.1)

Held under `AMENDMENT_v1.1_N1_PREVIEWS.md` section A: removed from the post-image, never written to the carrier, ID reserved, recorded as a non-emitted proposal for the owner's separate cycle transaction. Not a register deletion and not a ruling.

| H-id | Reserved ID | Edge | Evidence it would have cited | Why held |
|---|---|---|---|---|
| H-001 | DEP-02-01-010 | DEL-02-01 UPSTREAM INTERFACE on DEL-02-04 (Dialogue Toolkit, Context, and Local UI State): the chat navigator and composer read and write known folders (knownRoots), chat annotations (titles, pins, groups, archive), and the chat rung as DEL-02-04-owned local convenience state; workspace-state schema changes belong to DEL-02-04 and chat deletion never mutates the runtime session record. HIGH; SatisfactionStatus TBD. | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling); Current acceptance obligations 4` ("Chat organisation acts on local convenience state owned by DEL-02-04 only"); amended Scope Ledger SOW-008 L178 (chat annotations, known folders, chat rung as local convenience state; reverse view L411 maps DEL-02-04) and SOW-004 L174; `_STATUS.md#remaining` DEL-02-01-V3-01, V3-02, V3-03 Depends on DEL-02-04-V3-01 additive fields; D-APP-108 Q1 (deletion is a local hide). | Fan-in simulation `Evidence/fanin_simulation_v1/edge_analysis.json` lists the new pair `DEL-02-01 -> DEL-02-04` carried by `DEP-02-04-017 (DOWNSTREAM)` and `DEP-02-01-010 (UPSTREAM)` among the 15 newly proposed edges that lie on cycles collectively (a 20-node merge of SCC-001 when all thirteen post-images are substituted; no single one changes anything). Keeping a subset would be a cut, human-gated per `docs/CYCLE_DRIVEN_RESOLUTION.md`; `DOWNSTREAM_HANDOFFS.csv` row 3 requires SCC state unchanged unless separately ruled. See `HELD_EDGE_PROPOSALS.csv` H-001 (`HELD_NON_EMITTED_PENDING_OWNER_RULING`). |

Effect on this carrier's graph position: removing the edge cannot create reachability, so the v1 finding stands a fortiori — SCC-001 stays at nine nodes, DEL-02-01 stays outside it, and DEL-02-01's deliverable out-edges in the post-image are now `DEL-01-03` (DEP-02-01-014) and `DEL-07-01` (DEP-02-01-009) only.

## 3. Fence results

- **F1 (SCC-001 membership):** emitted rows PASS. Simulation S0 (all 52 registers with this post-image substituted) keeps SCC-001 at its nine nodes (`DEL-02-05; DEL-03-02; DEL-03-03; DEL-03-04; DEL-04-03; DEL-04-05; DEL-05-02; DEL-05-03; DEL-05-05`) and DEL-02-01 outside it. Finding: DEL-02-01 has no path into SCC-001, but every SCC-001 member already reaches DEL-02-01 through the recorded DOWNSTREAM row DEP-02-01-006 (`DEL-04-04 -> DEL-08-02 -> DEL-02-01`, edge convention of `analyze_dep_closure.py`). No SCC-001 member holds a direct row to DEL-02-01, so the brief's direct-back-row test is not tripped; the transitive test is, for any UPSTREAM row into SCC-001. Candidates below were therefore not emitted.
- **F2 (Root path):** NONE. Root-owned target emitted as `EXTERNAL` with `TargetLocation=TBD` (DEP-02-01-011). No candidate needed a Root path. `frontend/**` implementation paths (CLM-021; seated write loci) were withheld from `TargetLocation` because they are neither under `projects/chirality-app-dev/**` nor pinned by `_REFERENCES.md`.
- **F3 (permitted effect):** NONE. No row was derived from SCC ordering, schedule, or keep-aligned statements. Considered and not emitted: the seated-item Electron constraint (`frontend/electron/**` under D-APP-98 and the existing IPC sender policy; not introduced by an amended row, no deliverable target) and the SOW-002 L405 DEL-02-03 "UI touchpoint" ownership split (coordination, no named artifact flow in this carrier's sources).
- **NEEDS_HUMAN_GRAPH_DECISION** (unchanged by amendment v1.1; section C item 5 carries HGD-1, HGD-2, and HGD-3 to the owner slate with the rows unchanged in the post-image):
  - **HGD-1 — DEP-02-01-006 direction.** Recorded as DOWNSTREAM HANDOVER ("leaves persona alias and deeper routing-contract ownership to DEL-08-02", CLM-027). The applied reverse view L408 ("DEL-02-01 presents; DEL-08-02 owns aliases, routing, selection guards, and legacy compatibility") and CLM-015 read as DEL-02-01 consuming DEL-08-02's contract, that is UPSTREAM INTERFACE. Graph effect (simulation S1): inverting to UPSTREAM removes every SCC-001 member's reach into DEL-02-01 and creates no cycle (DEL-08-02 reaches no SCC-001 member). Preserved as recorded in the post-image.
  - **HGD-2 — DEP-02-01-007 and DEP-02-01-008 retire or keep.** Both are restated verbatim in live CLM-027 (dated compatibility evidence), so the brief's rule kept them ACTIVE. SCA-APP-010 (DEC-025) retires Workbench and Pipeline presentation from the active shell: SOW-001 L171 notes (retired routes reachable but unmounted, Q3), SOW-007 L177 and reverse view L410 ("no presentation consumer is mapped"), DEL-02-02 applied row L308, DEL-08-03 applied row L370. Proposal: `RETIRED 2026-09-05` with those citations if the owner rules the matrix-era interfaces stale; keep as compatibility-only otherwise. Simulation S1b (006/007/008 RETIRED) leaves SCC-001 unchanged and removes SCC-001 reach into DEL-02-01.
  - **HGD-3 — DEL-02-02-V3-03 prerequisite.** `_STATUS.md` DEL-02-01-V3-01 Depends: "DEL-02-02-V3-03 (the woven route this item re-frames)" is an owner-adopted signal for an UPSTREAM PREREQUISITE on DEL-02-02. With DEP-02-02-005 (DEL-02-02 UPSTREAM INTERFACE on DEL-02-01) and DEP-02-01-007 present, emitting it creates a new four-node SCC `{DEL-02-01, DEL-02-02, DEL-08-02, DEL-08-03}` (simulation S2). Held non-gating and not emitted; `DOWNSTREAM_HANDOFFS.csv` row 3 requires SCC state unchanged unless separately ruled. Options per `docs/CYCLE_DRIVEN_RESOLUTION.md`: decompose (record at seated-item level only; keep the deliverable-level edge non-gating), invert (retire the matrix-era pair DEP-02-01-007 here and DEP-02-02-005 in the DEL-02-02 preview, then emit), merge (human-gated), cut (human-gated).
- **FENCE_F1_CANDIDATES** (not emitted; each would merge DEL-02-01, DEL-04-02, DEL-04-04, and DEL-08-02 into a thirteen-node SCC, simulations S3 to S5):
  - **FC-1 — redaction helper -> DEL-05-03.** Evidence that would have been cited: `_STATUS.md#remaining` DEL-02-01-V3-02 Depends "the redaction helper under `frontend/src/lib/harness/**` consumed, not changed"; `ScopeOfWork.md` obligation 4 "derived titles pass the redaction helper (Q6)"; owner by amended-ledger inference SOW-041 L444 -> DEL-05-03 (SCC-001 member). Emitted instead as DEP-02-01-012 with `TargetType=UNKNOWN`.
  - **FC-2 — session-record binding -> DEL-03-02.** Evidence: `_STATUS.md#remaining` DEL-02-01-V3-03 Depends (provider root from the active session's registered project identity; session-record fields Root-owned); SOW-010 L180 and reverse view L413 map DEL-03-02 (SCC-001 member) as the App-side carrier. Emitted instead as DEP-02-01-011 `EXTERNAL` per the brief's Root-owned convention.
  - **FC-3 — account-row host -> DEL-02-05; DEL-02-05-V3-05 gate.** Evidence: applied row L307 "the account row host"; `ScopeOfWork.md` obligation 6 "the account row is hosted here and its presentation is DEL-02-05's" (UPSTREAM INTERFACE on DEL-02-05, SCC-001 member); `_STATUS.md` DEL-02-01-V3-04 gate `NOT_SELECTABLE_UNTIL: DEL-02-05-V3-05 landed` (sequencing only; also F3). Neither emitted.
- **FENCE_F2_CANDIDATES:** none.

## 4. Validator outputs (verbatim; re-run on the v1.1 post-image)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py <instance>/POSTIMAGE_Dependencies.csv`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-01/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 13
```

Enum (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct emitted pair; still 25 pairs after the held row's removal because every value it carried remains on another row; 0 invalid):

```text
validate_enum.py ANCHOR_TYPE IMPLEMENTS_NODE: exit=0 VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
validate_enum.py ANCHOR_TYPE NOT_APPLICABLE: exit=0 VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
validate_enum.py ANCHOR_TYPE TRACES_TO_REQUIREMENT: exit=0 VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
validate_enum.py CONFIDENCE HIGH: exit=0 VALID: HIGH is a valid CONFIDENCE
validate_enum.py CONFIDENCE MEDIUM: exit=0 VALID: MEDIUM is a valid CONFIDENCE
validate_enum.py DEPENDENCY_CLASS ANCHOR: exit=0 VALID: ANCHOR is a valid DEPENDENCY_CLASS
validate_enum.py DEPENDENCY_CLASS EXECUTION: exit=0 VALID: EXECUTION is a valid DEPENDENCY_CLASS
validate_enum.py DEPENDENCY_TYPE CONSTRAINT: exit=0 VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
validate_enum.py DEPENDENCY_TYPE HANDOVER: exit=0 VALID: HANDOVER is a valid DEPENDENCY_TYPE
validate_enum.py DEPENDENCY_TYPE INTERFACE: exit=0 VALID: INTERFACE is a valid DEPENDENCY_TYPE
validate_enum.py DEPENDENCY_TYPE OTHER: exit=0 VALID: OTHER is a valid DEPENDENCY_TYPE
validate_enum.py DEPENDENCY_TYPE PREREQUISITE: exit=0 VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
validate_enum.py DIRECTION DOWNSTREAM: exit=0 VALID: DOWNSTREAM is a valid DIRECTION
validate_enum.py DIRECTION UPSTREAM: exit=0 VALID: UPSTREAM is a valid DIRECTION
validate_enum.py EXPLICITNESS EXPLICIT: exit=0 VALID: EXPLICIT is a valid EXPLICITNESS
validate_enum.py ORIGIN EXTRACTED: exit=0 VALID: EXTRACTED is a valid ORIGIN
validate_enum.py SATISFACTION_STATUS NOT_APPLICABLE: exit=0 VALID: NOT_APPLICABLE is a valid SATISFACTION_STATUS
validate_enum.py SATISFACTION_STATUS PENDING: exit=0 VALID: PENDING is a valid SATISFACTION_STATUS
validate_enum.py SATISFACTION_STATUS TBD: exit=0 VALID: TBD is a valid SATISFACTION_STATUS
validate_enum.py STATUS ACTIVE: exit=0 VALID: ACTIVE is a valid STATUS
validate_enum.py TARGET_TYPE DELIVERABLE: exit=0 VALID: DELIVERABLE is a valid TARGET_TYPE
validate_enum.py TARGET_TYPE EXTERNAL: exit=0 VALID: EXTERNAL is a valid TARGET_TYPE
validate_enum.py TARGET_TYPE PACKAGE: exit=0 VALID: PACKAGE is a valid TARGET_TYPE
validate_enum.py TARGET_TYPE REQUIREMENT: exit=0 VALID: REQUIREMENT is a valid TARGET_TYPE
validate_enum.py TARGET_TYPE UNKNOWN: exit=0 VALID: UNKNOWN is a valid TARGET_TYPE
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; known `PROJECT_ID_FORMAT_PROFILE` warning, no ID changed):

```text
validate_id_format.sh DEL DEL-02-01: exit=1 INVALID: DEL-02-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
validate_id_format.sh PKG PKG-02: exit=1 INVALID: PKG-02 does not match PKG format (^PKG-[0-9]{3}$)
validate_id_format.sh DEP DEP-02-01-009: exit=1 INVALID: DEP-02-01-009 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
validate_id_format.sh SOW SOW-001: exit=1 INVALID: SOW-001 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
validate_id_format.sh OBJ OBJ-001: exit=0 VALID: OBJ-001 matches OBJ format
validate_id_format.sh DEL DEL-07-01: exit=1 INVALID: DEL-07-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
```

Anchor and register checks (computed over the post-image):

```text
active IMPLEMENTS_NODE: 1
unique ids: True from ok: True
active rows lacking evidence: []
census total/active/retired/anchor/exec: 13 13 0 4 9
sat: TBD 8, NOT_APPLICABLE 4, PENDING 1
type: INTERFACE 5, OTHER 4, HANDOVER 2, PREREQUISITE 1, CONSTRAINT 1
notes referencing DEP-02-01-010: []
```

Evidence resolution: `_CONTEXT.md` `## Identity` (L3) and `## Traceability` (L51); `ScopeOfWork.md` `## SCA-APP-010 Gate-5 Current Contract (Controlling)` (L73) with `### Current acceptance obligations` (L102), `### CLM-015` (L310), `### CLM-018` (L332), `### CLM-021` (L389), `### CLM-027` (L449); `_STATUS.md` `## Remaining` (L10). Every `EvidenceQuote` was grep-confirmed in its source file in v1; the rerun changed no evidence field, and the carrier source hashes recorded in `POSTIMAGE__DEPENDENCIES.md` Run Notes were re-verified unchanged. `_DEPENDENCIES.md` post-image counts reconciled to the post-image CSV (summary, register table, Run History ACTIVE count, lifecycle, satisfaction).

Graph simulations (v1 record, ad hoc, read-only; functions of `tools/coordination/analyze_dep_closure.py` re-used from the session scratchpad over all 52 registers with the v1 post-image substituted; not a skill-allowlisted tool, disclosed here and in both run records). The v1.1 rerun ran no simulation: the only change is an edge removal, which is monotone for reachability, so every S0 conclusion holds a fortiori with `out-edges=['DEL-01-03', 'DEL-07-01']`; the cross-carrier interaction that held the edge is HELP_HUMAN's fan-in simulation in `Evidence/fanin_simulation_v1/`.

```text
S0 proposed post-image (v1): SCCs=[(9, 'SCC-001')]; DEL-02-01 in an SCC=False; out-edges=['DEL-01-03', 'DEL-02-04', 'DEL-07-01']; SCC-001 members reaching DEL-02-01=all nine; DEL-02-01 reaches SCC-001=[]
S1 DEP-02-01-006 inverted to UPSTREAM: SCCs=[(9, 'SCC-001')]; DEL-02-01 in an SCC=False; SCC-001 members reaching DEL-02-01=[]
S1b 006/007/008 RETIRED: SCCs=[(9, 'SCC-001')]; DEL-02-01 in an SCC=False; SCC-001 members reaching DEL-02-01=[]
S2 + HGD-3 UPSTREAM PREREQUISITE DEL-02-02: SCCs=[(4, ['DEL-02-01', 'DEL-02-02', 'DEL-08-02', 'DEL-08-03']), (9, 'SCC-001')]
S3 + FC-3 UPSTREAM INTERFACE DEL-02-05: SCCs=[(13, SCC-001 + DEL-02-01, DEL-04-02, DEL-04-04, DEL-08-02)]
S4 + FC-1 UPSTREAM INTERFACE DEL-05-03: SCCs=[(13, SCC-001 + DEL-02-01, DEL-04-02, DEL-04-04, DEL-08-02)]
S5 + FC-2 UPSTREAM INTERFACE DEL-03-02: SCCs=[(13, SCC-001 + DEL-02-01, DEL-04-02, DEL-04-04, DEL-08-02)]
```

## 5. Epistemic notes

- FACT (all rows): `FromDeliverableName` refreshed to "Woven Dialogue Shell and Compatibility Navigation" from applied row L307 and `_CONTEXT.md` Identity; no `DependencyID` changed; no `Origin=DECLARED` row exists in this register.
- FACT (001-004): labels are the applied decomposition text (L280, L404, L408, L262). ASSUMPTION (004): keeping `TargetType=REQUIREMENT` for the objective anchor follows this register's pre-image rather than the brief's `UNKNOWN` wording; either is enum-valid and no graph edge depends on it.
- FACT (005-008): each relation is restated verbatim in live `ScopeOfWork.md` CLM-018/CLM-027, which is why none was retired; PROPOSAL (HGD-2): the decomposition-level retirement of Workbench/Pipeline presentation makes 007/008 compatibility-only.
- FACT (009): stated in the controlling SCA-APP-010 obligation 3 and in the amended ledger row L172; corroborated by the seated Depends lines. The equally factual DEL-02-04 relation (obligation 4; L178/L174) is held as H-001 for graph reasons, not evidential ones.
- FACT (011): stated in the seated V3-03 Depends and obligation 2; the Root DEL-02-11 field ownership is L180/L602 text. `EXTERNAL`/`TBD`/`PENDING` is the brief's convention, not an inference.
- FACT (012) relation; PROPOSAL target: the helper's owner is not named in this carrier's sources; SOW-041 -> DEL-05-03 is a ledger inference and is fenced (FC-1).
- FACT (013, 014): stated in the seated V3-04 and V3-01 Return contracts; both are owner-seated items traced to SOW-001 L171, which is how they pass F3. 014 is MEDIUM because it appears only in the Return line.
- ASSUMPTION (normalization): `CHIRALITY_INSTRUCTION_ROOT` was not exported in this session; the sealed brief's repository root was taken as the instruction root (the Chirality checkout during source execution, `docs/DIRECTIVE.md` section 2.6), matching the Gate-5 precedent declaration form.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched. v1 written by the 0043 instance; rewritten in place by a fresh instance under amendment v1.1 (run record `_run_records/TASK_RUN_2026-09-05_0102.md`; the v1 record `TASK_RUN_2026-09-05_0043.md` stays).
