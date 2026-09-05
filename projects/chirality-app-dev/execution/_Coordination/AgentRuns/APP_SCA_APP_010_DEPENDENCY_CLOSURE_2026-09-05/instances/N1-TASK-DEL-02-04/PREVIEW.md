# PREVIEW - N1-TASK-DEL-02-04 - TASK + dependency-extract (report-only; amendment v1.1 rerun)

## 1. Header

- Instance: `N1-TASK-DEL-02-04`; RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`; node N1; parent HELP_HUMAN (Agent 0). Brief: `LAUNCH_BRIEF.md` v1 (still binding) as narrowed by `AMENDMENT_v1.1_N1_PREVIEWS.md` (section A held rows; section D rerun contract). This rerun supersedes the 00:39 preview in place; the v1 run record `_run_records/TASK_RUN_2026-09-05_0039.md` stays.
- Carrier: `DEL-02-04` Dialogue Toolkit, Context, and Local UI State (UX_UI_SLICE, PKG-02); folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State`.
- Basis: HEAD `d66395d101143df68d956984f7ab93f5027418ec` (= pinned `origin/main`); working tree clean apart from this run folder (untracked).
- Decomposition identity: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches) at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (matches); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (matches).
- Pre-image hashes (re-verified before the rerun): `Dependencies.csv` `7f986d37a117f3e9812dd978a4ab00031878be50f2c351c4693713ae087c1010` (14 data rows); `_DEPENDENCIES.md` `a81ae0ee95103979cfd923f6666e74680d3d69c66a43a86418d9a55424251b1d`.
- Post-image hashes (v1.1): `POSTIMAGE_Dependencies.csv` `c6bdffd1aef83f0c04764a8f8f01d5f67abc1928c9630866f6f48dd83d16ac62`; `POSTIMAGE__DEPENDENCIES.md` `1fffa1ec5e37709dcb26f0c1b0cd611e3ae474690db63593a85e6bd2c50ba35e`. (Superseded v1 hashes: `53dd60e943c206e6e31ca05134c7f24f5239d1d310b45774863a998c7d4c4718`; `b50b7050f7c84896b8038085f85a27c8aa3a4d447ba703877bc8fe0e2f4e80ac`.)
- Row census pre: 14 total / 14 ACTIVE / 0 RETIRED / 6 ANCHOR / 8 EXECUTION.
- Row census post (v1.1): 16 total / 16 ACTIVE / 0 RETIRED / 6 ANCHOR / 10 EXECUTION. (v1 was 21 / 21 / 0 / 6 / 15; five rows held.)
- Change counts: ADDED 2, RE-EVIDENCED 14, HELD (removed from the post-image, IDs reserved) 5.
- Carrier bytes untouched: this instance wrote only under its own folder (`POSTIMAGE_Dependencies.csv`, `POSTIMAGE__DEPENDENCIES.md`, `PREVIEW.md`, `RETURN.md`, `STATUS.json`, `_run_records/TASK_RUN_2026-09-05_0102.md`).

## 2. Row-level diff (every post-image row)

`UNCHANGED` would mean byte-identical; no row is byte-identical because every still-observed row received `LastSeen=2026-09-05` and the applied deliverable name (`FromDeliverableName` refreshed from `Toolkit Options and Local UI State` to `Dialogue Toolkit, Context, and Local UI State` per applied row L310). Rows DEP-02-04-001..014, 020, and 021 are byte-identical to the v1 post-image; only the five held rows were removed.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-02-04-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PACKAGE PKG-02 | `_CONTEXT.md#Identity` | Package label resolved to applied name; SourceRef moved to live `## Identity`; TargetLocation pinned to L280; LastSeen refreshed. |
| DEP-02-04-002 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-004 | `ScopeOfWork.md#Purpose and Objective Traceability` | Datasheet.md > Identification -> live front matter/Purpose line; label from reverse view L407; TargetLocation L174 (amended, SR-02/SR-05/SR-07). |
| DEP-02-04-003 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-008 | `ScopeOfWork.md#Purpose and Objective Traceability` | Datasheet.md > Identification -> live front matter/Purpose line; label from reverse view L411; TargetLocation L178 (amended, SR-03/SR-24). |
| DEP-02-04-004 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-016 | `ScopeOfWork.md#Purpose and Objective Traceability` | Datasheet.md > Identification -> live front matter/Purpose line; label from reverse view L419; TargetLocation L186 (not amended by SCA-APP-010). |
| DEP-02-04-005 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | WBS_NODE OBJ-001 | `ScopeOfWork.md#Purpose and Objective Traceability` | Datasheet.md > Identification -> live front matter/Purpose line; WBS_NODE objective convention preserved; TargetLocation L262. |
| DEP-02-04-006 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | WBS_NODE OBJ-004 | `ScopeOfWork.md#Purpose and Objective Traceability` | Guidance.md > Purpose -> live front matter/Purpose line (former sentence survives at CLM-023); WBS_NODE convention preserved; TargetLocation L265. |
| DEP-02-04-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-001 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; REF-001 MATCH (corpus v20). |
| DEP-02-04-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-002 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; REF-002 MATCH (corpus v20). |
| DEP-02-04-009 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-003 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; REF-003 MATCH (corpus v20). |
| DEP-02-04-010 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-004 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; REF-004 MATCH (corpus v20). |
| DEP-02-04-011 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-005 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; REF-005 MATCH (corpus v20). |
| DEP-02-04-012 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-006 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; stale hash-mismatch wording removed from Statement/EvidenceQuote; REF-006 MATCH. |
| DEP-02-04-013 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT DECOMP-v3.2 | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; pinned identity (c7c05169 at dbd812a5) recorded in Notes. |
| DEP-02-04-014 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | UNKNOWN TBD | `ScopeOfWork.md#CLM-018` | Procedure.md > Prerequisites -> CLM-018; target stays UNKNOWN/TBD; PROPOSAL (not emitted) to resolve to DEL-04-02/DEL-06-01 recorded in Notes. |
| DEP-02-04-020 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | DEL-07-03 (SOW-081) | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | Applied row L310 Notes / SOW-008 L178: workflow file (contract owned by DEL-07-03 per SOW-081 L484) owns rung-related truth. Not on any simulated cycle (`Evidence/fanin_simulation_v1/edge_analysis.json`). |
| DEP-02-04-021 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | EXTERNAL TBD | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | Same clause: session record; Root retains session-record semantics (DEC-025, OI-008); EXTERNAL, TargetLocation=TBD, no Root path; Confidence MEDIUM. |

Reserved, not emitted: DEP-02-04-015, DEP-02-04-016, DEP-02-04-017, DEP-02-04-018, DEP-02-04-019 (see section 2a). No row was renumbered.

## 2a. Held proposals (amendment v1.1)

Removed from `POSTIMAGE_Dependencies.csv` and the `POSTIMAGE__DEPENDENCIES.md` register table per amendment section A; recorded as non-emitted proposals in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` for the owner's separate transaction. They were never written to the carrier, so this is not a register deletion. Each `POSTIMAGE__DEPENDENCIES.md` Run Notes bullet for these rows uses the amendment's prescribed `HELD (non-emitted proposal, pending owner ruling): ...` form.

| H-id | Reserved ID | Edge | Direction/Type | Evidence it would have cited | Would form or join |
|---|---|---|---|---|---|
| H-008 | DEP-02-04-015 | DEL-02-04 -> DEL-02-02 (item DEL-02-02-V3-03) | UPSTREAM/PREREQUISITE | `_STATUS.md#Remaining`: "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed ... Depends: DEL-02-02-V3-03" (owner-adopted gate and Depends line, D-APP-108, 2026-09-04); target row L308; Confidence HIGH; SatisfactionStatus PENDING. | Deliverable-level pair DEL-02-04 <-> DEL-02-02 with H-011 (acyclic at item level: DEL-02-02-V3-03 -> DEL-02-04-V3-01 -> DEL-02-02-V3-04); joins SCC-001 into the simulated 20-node SCC with the other held edges. |
| H-009 | DEP-02-04-016 | DEL-02-04 -> DEL-02-03 (item DEL-02-03-V3-01) | UPSTREAM/PREREQUISITE | `_STATUS.md#Remaining`: "the Activity view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it, while the strip and the additive fields can" (owner-adopted Depends line; partial prerequisite, Activity view only); target row L309; Confidence HIGH; PENDING. | Mutual dependency DEL-02-04 <-> DEL-02-03 with H-012 at deliverable and item level; the carrier Depends line already partitions DEL-02-04-V3-01 (decompose move); joins the simulated 20-node SCC. |
| H-010 | DEP-02-04-017 | DEL-02-01 <- DEL-02-04 (items DEL-02-01-V3-02, DEL-02-01-V3-03) | DOWNSTREAM/HANDOVER | `_STATUS.md#Remaining`: "DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-02-V3-04, and DEL-02-03-V3-01 consume the additive fields"; additive v1 workspace-state fields are an applied-row output (L310) and a `_CONTEXT.md` anticipated artifact; convenience state only, no session authority transfers (SOW-008 L178); target row L307; Confidence HIGH; PENDING. | Joins the simulated 20-node SCC with the other held edges (reciprocal of DEL-02-01 H-001). |
| H-011 | DEP-02-04-018 | DEL-02-02 <- DEL-02-04 (item DEL-02-02-V3-04) | DOWNSTREAM/HANDOVER | Same Depends line as H-010; target row L308; Confidence HIGH; PENDING. | Pair with H-008 (above); joins the simulated 20-node SCC (reciprocal of DEL-02-02 H-007). |
| H-012 | DEP-02-04-019 | DEL-02-03 <- DEL-02-04 (item DEL-02-03-V3-01) | DOWNSTREAM/HANDOVER | Same Depends line as H-010; target row L309; Confidence HIGH; PENDING. | Mutual with H-009 (above); joins the simulated 20-node SCC. |

## 3. Fence results

- F1 (SCC-001 membership; members DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05): `NONE`. No post-image row targets an SCC-001 member; the baseline closure lists DEL-02-04 as an orphan and no other register carries an emitted row to DEL-02-04 (the DEL-02-01 and DEL-02-02 reciprocal rows H-001 and H-007 are likewise held). With the five held rows removed, the post-image carries no deliverable-to-deliverable edge except DEP-02-04-020 (DEL-07-03, not an SCC-001 member and not on any simulated cycle).
- F2 (Root path): `NONE` emitted. Every `TargetLocation` is `execution/**` of the App project, a repo-root file pinned by `_REFERENCES.md` (`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md`), or `TBD`. The one Root-owned target (DEP-02-04-021) is `TargetType=EXTERNAL`, `TargetLocation=TBD`, `SatisfactionStatus=PENDING`.
- F3 (permitted effect): `NONE`. Both emitted new rows derive from the applied row L310 Notes, amended SOW-008 (L178), SOW-081 (L484), and the SCA-APP-010 Gate-5 Current Contract in `ScopeOfWork.md`. No edge was inferred from SCC ordering, schedule, or keep-aligned language. The five seated-item rows that section A holds were themselves within F3 (owner-adopted gate and Depends lines); they are held for the cycle reason stated in the amendment, not for a fence breach.
- NEEDS_HUMAN_GRAPH_DECISION: `none` open in this post-image. The two pairs the v1 preview surfaced (DEP-02-04-015/018 -> DEL-02-04 <-> DEL-02-02; DEP-02-04-016/019 -> DEL-02-04 <-> DEL-02-03) are thereby held rather than open: every participating row is a held non-emitted proposal (H-008, H-009, H-011, H-012), so the register carries no cycle-participating edge and nothing was linearized. The resolution questions (decompose / invert / merge / cut; cut and merge human-gated per `docs/CYCLE_DRIVEN_RESOLUTION.md`) travel with the held proposals to the owner's separate transaction and are not counted against this instance's status.
- FENCE_F1_CANDIDATES: `none`.
- FENCE_F2_CANDIDATES (would need a repo-root path not pinned by `_REFERENCES.md`; listed, not emitted; unchanged from v1):
  1. `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`) as a DOCUMENT/PREREQUISITE design basis for DEL-02-04-V3-01. Evidence I would have cited: `_STATUS.md#Remaining`, "Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` ... cited only for what the tranche means when complete, never as a queue". Confidence would have been MEDIUM because the owner frames it as a meaning reference, not a queue.
  2. `loop/LOOP_INIT.md` section 7 Evidence contract as a DOCUMENT/CONSTRAINT on the item's Return. Evidence I would have cited: `_STATUS.md#Remaining`, "durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` section 7 Evidence contract". Confidence would have been LOW (generic process contract shared by every seated item).

## 4. Validator outputs (verbatim, re-run on the v1.1 post-image)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py <POSTIMAGE_Dependencies.csv>`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-04/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 16
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct value present in the post-image; 25 checks; `DOWNSTREAM` and `HANDOVER` no longer occur because the only rows carrying them are held):

```text
VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
VALID: HIGH is a valid CONFIDENCE
VALID: MEDIUM is a valid CONFIDENCE
VALID: ANCHOR is a valid DEPENDENCY_CLASS
VALID: EXECUTION is a valid DEPENDENCY_CLASS
VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
VALID: OTHER is a valid DEPENDENCY_TYPE
VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
VALID: UPSTREAM is a valid DIRECTION
VALID: EXPLICIT is a valid EXPLICITNESS
VALID: EXTRACTED is a valid ORIGIN
VALID: NOT_APPLICABLE is a valid SATISFACTION_STATUS
VALID: PENDING is a valid SATISFACTION_STATUS
VALID: SATISFIED is a valid SATISFACTION_STATUS
VALID: TBD is a valid SATISFACTION_STATUS
VALID: ACTIVE is a valid STATUS
VALID: DELIVERABLE is a valid TARGET_TYPE
VALID: DOCUMENT is a valid TARGET_TYPE
VALID: EXTERNAL is a valid TARGET_TYPE
VALID: PACKAGE is a valid TARGET_TYPE
VALID: REQUIREMENT is a valid TARGET_TYPE
VALID: UNKNOWN is a valid TARGET_TYPE
VALID: WBS_NODE is a valid TARGET_TYPE
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; known `PROJECT_ID_FORMAT_PROFILE` warning, no ID changed; DEL-02-01/02/03 no longer appear because their rows are held):

```text
INVALID: DEL-02-04 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-02 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-02-04-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-02-04-021 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEL-07-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-07 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: SOW-004 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-008 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-016 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-001 matches OBJ format
VALID: OBJ-004 matches OBJ format
```

Anchor check: ACTIVE rows with `DependencyClass=ANCHOR` and `AnchorType=IMPLEMENTS_NODE` = 1 (PASS; no FLOATING_NODE, no AMBIGUOUS_ANCHOR). MISSING_DECOMPOSITION: not raised (decomposition present at the pinned identity).

Evidence resolution (local check over every ACTIVE row against the carrier's live bytes): `EvidenceFile` exists in the carrier folder; `SourceRef` heading / CLM id resolves to a live heading; `EvidenceQuote` found verbatim in that file - 16/16 PASS. `TargetLocation#L<n>` pointers resolve to the row naming the target identifier - 7/7 PASS. `FromDeliverableID=DEL-02-04` on 16/16 rows; 16 unique `DependencyID`s, none colliding with the five reserved IDs; `Status` in {ACTIVE, RETIRED} only (no CANDIDATE). `_DEPENDENCIES.md` register table lists the same 16 IDs in CSV order; metric, Run History ACTIVE, lifecycle, and satisfaction counts (6 NOT_APPLICABLE / 7 SATISFIED / 2 PENDING / 1 TBD) match the CSV; five `HELD` Run Notes bullets present. Hygiene: 0 CR bytes, 0 trailing-whitespace lines, single final LF on both post-images; the CSV is ASCII; the MD contains the em dashes of the amendment's prescribed HELD bullet form (UTF-8, otherwise ASCII).

## 5. Epistemic notes

- FACT (all re-evidenced rows 002..014): the legacy kit sections were migrated verbatim into `ScopeOfWork.md` CLM blockquotes (CLM-002 Identification, CLM-018 Prerequisites, CLM-023 Purpose); the controlling SOW_V1 text (front matter `project_scope_refs`/`package_objective_refs`, the Purpose line, OUT-001) restates every anchor, so anchors cite the controlling text and Notes name the CLM lineage.
- FACT (001..006 labels): `TargetName` values were resolved to the applied decomposition's canonical labels (PKG-02 L280; SOW reverse view L407/L411/L419); objective labels were left as the existing accurate paraphrases. The brief text "keep the existing `TargetType=UNKNOWN` convention for objectives" was read as "keep the carrier's existing objective convention", which here is `TargetType=WBS_NODE` with the existing enum note; amendment section C.7 confirms the carrier convention; no objective row changed type.
- FACT (012): the pre-image Statement "with hash mismatch warning" contradicted `_REFERENCES.md` (REF-006 MATCH since D-APP-38); the Statement now states the relation only.
- FACT (held H-008..H-012): the five held edges were sourced solely from this carrier's `_STATUS.md` `## Remaining` seated item DEL-02-04-V3-01 (D-APP-108, 2026-09-04) and remain within F3; they are held for the collective-cycle reason recorded in the amendment (fan-in simulation), not because their evidence failed. Their removal changes no other row's bytes.
- FACT (020): "the workflow file and the session record own rung-related truth" is applied-row L310 Notes text restated in the Gate-5 Current Contract; DEL-07-03's ownership of the workflow file contract is stated at SOW-081 L484 and DEL-07-03 L359. The named artifact makes this a constraint edge rather than coordination.
- FACT / ASSUMPTION (021): Root retention of session-record semantics is FACT (DEC-025 L634; OI-008 L602). ASSUMPTION: the rung-related session-record field belongs to the same Root session-record semantics as the OI-008 delegation-policy field; hence Confidence MEDIUM and `TargetRefID=TBD`.
- PROPOSAL (014, not emitted): resolve the TBD adjacent-deliverable target to DEL-04-02 (SOW-016 co-carrier, L419) and DEL-06-01 (permission-policy mode mapping, L346). Outside the SCA-APP-010 permitted effect; owner ruling required.
- Considered and not emitted (no explicit transfer in this carrier's sources; F3 discipline; unchanged from v1): DEL-05-04 replay semantics for the stored replay reference; DEL-07-01 filesystem policy for known folders (SOW-002); `proposal.*` event consumption behind the declined-trigger field (SOW-082; Root DEL-02-10); the SCA-APP-004/SCA-APP-010 instruments REF-008..REF-013; `docs/ui/UI_POLISH_EXECUTION_PLAN.md` (listed under CLM-018 but unpinned and evidence-routing only); the seated item's registered check gates and independent-review path (process, not information flow).
- ASSUMPTION (runtime): `CHIRALITY_INSTRUCTION_ROOT` was not exported to the subagent shell; `INSTRUCTION_ROOT=REPO_ROOT` was taken from the sealed brief's own reading list and recorded as `[WARNING] INSTRUCTION_ROOT_DECLARED_BY_BRIEF`.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
