# PREVIEW — N1-TASK-DEL-08-01 — report-only dependency-extract post-image for DEL-08-01 (rerun under brief amendment v1.1)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-08-01` (run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N1) |
| Brief | `LAUNCH_BRIEF.md` v1 (binding) as narrowed by `AMENDMENT_v1.1_N1_PREVIEWS.md` (sections A, C.3, C.4, D); this rerun rewrites the v1 preview in place, holds DEP-08-01-018 (H-018), and changes no fence |
| Carrier | `DEL-08-01` Instruction Root Packaging and Agent Conformance (TEST_SUITE, PKG-08); folder `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance` |
| Basis | `git rev-parse HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` (exact, re-verified at the rerun); working tree clean except the untracked run packet |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches the carrier `ScopeOfWork.md` pin); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` |
| Pre-image `Dependencies.csv` | `a3013604e7f6d918028dfcdf80918842fd399ce1abcfe31144beedec094bf4c4` (matched) |
| Pre-image `_DEPENDENCIES.md` | `d1cf1551c0519da3faf215cd1b3324fbefc14fbc98271b218cb1eebeca3b7c42` (matched) |
| Post-image `POSTIMAGE_Dependencies.csv` | `1f616ed9ed997a5cbd6e19114930e9c9055bd44313be7fe5954ac93d03c768f6` (v1 preview `c64602be84cfd2d9681571a687da95793917dfbac8e1a4053984d8929c878e61` superseded) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `09321d20219a27017c74f99da5d84f8c2f8bed10832b008304bf09d38ca3e57a` (v1 preview `20a2b3d80870453161602f05b4ef94c0cf0e777c8585396db238fe346f9b76be` superseded) |
| Row census pre | 15 total / 15 ACTIVE / 0 RETIRED / 6 ANCHOR / 9 EXECUTION |
| Row census post | 20 total / 20 ACTIVE / 0 RETIRED / 8 ANCHOR / 12 EXECUTION (v1 preview: 21 / 21 / 0 / 8 / 13; one row held, ID reserved, no renumbering) |
| Quoting convention | Pre-image uses fully quoted data fields with an unquoted header, LF, final newline; Python `csv.QUOTE_ALL` round-trip of the pre-image is byte-identical, and the post-image is written with the same writer |

Carrier bytes were not changed: `git status --porcelain` shows only the untracked run packet; `git diff --stat` against HEAD is empty.

## 2. Row-level diff

`UNCHANGED` means byte-identical. Every pre-existing row received `LastSeen=2026-09-05` (all fifteen relations are still observed), so no pre-existing row is byte-identical; the change class names the substantive reason.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-08-01-001 | REFRESHED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PACKAGE PKG-08 | `_CONTEXT.md#Identity; ScopeOfWork.md#CLM-002; decomposition#L286,#L368` | Stale `decomposition:262,340-344` re-pointed (PKG-08 row is L286, applied row L368). ID and relation preserved. |
| DEP-08-01-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-030 | `_CONTEXT.md#Traceability` + `ScopeOfWork.md#Purpose and Objective Traceability; decomposition#L200,#L368,#L433` | Stale `_CONTEXT.md:34-40; decomposition:182,344,406` re-pointed. SOW-030 remains on L368. |
| DEP-08-01-003 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-031 | `_CONTEXT.md#Traceability` + `ScopeOfWork.md#…; decomposition#L201,#L368,#L434` | As above. |
| DEP-08-01-004 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-073 | `_CONTEXT.md#Traceability` + `ScopeOfWork.md#…; decomposition#L243,#L368,#L476` | As above; SOW-073 still `TBD` upstream. |
| DEP-08-01-005 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-007 | `_CONTEXT.md#Traceability` + `ScopeOfWork.md#…; ScopeOfWork.md#CLM-020; decomposition#L268,#L368` | `Guidance.md:3-5` (retired kit) replaced by CLM-020, which restates the Guidance purpose. `TargetType=REQUIREMENT` is this carrier's pre-existing objective convention and is preserved (the brief's generic `UNKNOWN` note does not match this pre-image). |
| DEP-08-01-006 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-008 | as 005 with `decomposition#L269` | As 005. |
| DEP-08-01-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-001 `docs/DIRECTIVE.md` | `ScopeOfWork.md#CLM-015; #CLM-006; #CLM-004; #DEL0801-REQ002; _REFERENCES.md:7` | `Procedure.md`/`Guidance.md` replaced. `docs/…` resolves to `projects/chirality-app-dev/docs/` (REF-001 hash `50b816d5…` matches that file, not the repo-root copy). |
| DEP-08-01-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-002 `docs/CONTRACT.md` | `ScopeOfWork.md#CLM-015; #CLM-006; #CLM-010; #DEL0801-REQ001; #DEL0801-REQ012; _REFERENCES.md:8` | `Procedure.md`/`Specification.md` replaced. |
| DEP-08-01-009 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-003 `docs/SPEC.md` | `ScopeOfWork.md#CLM-015; #CLM-006; #CLM-010; #DEL0801-REQ003; #DEL0801-REQ006; _REFERENCES.md:9` | As 008. |
| DEP-08-01-010 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-004 `docs/TYPES.md` | `ScopeOfWork.md#CLM-015; #CLM-006; #CLM-010; #DEL0801-REQ010; #DEL0801-REQ011; _REFERENCES.md:10` | As 008. |
| DEP-08-01-011 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-005 `docs/PLAN.md` | `ScopeOfWork.md#CLM-006; #CLM-015; _REFERENCES.md:11` | `Datasheet.md` replaced; quote "docs/PLAN.md R3 subagent implementation targets and section 6.1." is live at CLM-006. |
| DEP-08-01-012 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-006 `docs/PRD.md` | `ScopeOfWork.md#CLM-004; #CLM-006; #CLM-010; #DEL0801-REQ004; #CLM-024; _REFERENCES.md:12` | `Specification.md`/`Guidance.md` replaced; `EvidenceQuote` replaced with the live CLM-004 sentence because the prior quote is not present in SOW_V1 bytes. |
| DEP-08-01-013 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-007 `AGENT_SOFTWARE_DECOMP.md` | `ScopeOfWork.md#CLM-006; _REFERENCES.md:13` | `Datasheet.md` replaced. `TargetLocation` (pre-existing REF-007 absolute pointer to a Root `agents/` surface) preserved unchanged; flagged under NEEDS_HUMAN_GRAPH_DECISION. |
| DEP-08-01-014 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT DEC-004 decomposition v3.2 | `ScopeOfWork.md#CLM-015; #SCA-APP-010 Gate-5 Current Contract (Controlling); _REFERENCES.md#Decomposition Entry; decomposition#L368` | `Procedure.md` replaced; stale `decomposition:340-344` re-pointed to L368; `TargetRefID=DEC-004` preserved, DEC-025 noted. |
| DEP-08-01-015 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | UNKNOWN TBD current instruction-root source tree | `ScopeOfWork.md#CLM-015; #CLM-003` | `Procedure.md`/`Datasheet.md` replaced; target still `UNKNOWN`/`TBD` (unchanged warning). |
| DEP-08-01-016 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-082 | `ScopeOfWork.md#Purpose and Objective Traceability; #Current responsibility; decomposition#L252,#L368,#L485` | New scope ref on the applied row (SCA-APP-010, DEC-025). `SatisfactionStatus=SATISFIED` per this carrier's anchor convention. |
| DEP-08-01-017 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-084 | `ScopeOfWork.md#…; decomposition#L254,#L368,#L487` | New scope ref on the applied row (Q14 ruled 2026-09-04). |
| DEP-08-01-019 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-07-01 (PKG-07) | `_STATUS.md#Remaining (DEL-08-01-V3-01 Depends); ScopeOfWork.md#Current acceptance obligations; decomposition#L254,#L487` | The organisation-layer protections the checks verify (K-ROOT-1 on both layers). Target exists at decomposition L357. Not an SCC-001 member. |
| DEP-08-01-020 | ADDED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/CONSTRAINT | EXTERNAL `AGENTS.md#agent-index-change-notice-rule`, `TargetLocation=TBD` | `ScopeOfWork.md#Current acceptance obligations; #Current responsibility; _STATUS.md#Remaining (Write locus, Checks); decomposition#L368` | Routed agent-index change notice and G4 manifest for any `agents/`/`skills/` change. Root-owned rule, so `EXTERNAL`/`TBD` (F2 convention). |
| DEP-08-01-021 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | EXTERNAL `OWNER-WRITE-SCOPE-GRANT-AGENTS-SKILLS`, `TargetLocation=TBD` | `_STATUS.md#Remaining (DEL-08-01-V3-01 Depends)` | Owner write-scope grant for `agents/**` and `skills/**` at selection; a human act. |

No row was retired or deleted; no `Origin=DECLARED` row exists in this register; `Status=CANDIDATE` is not emitted. `DependencyID` `DEP-08-01-018` is absent from the post-image by amendment v1.1 section A and stays reserved for the held proposal below; DEP-08-01-019 to DEP-08-01-021 are not renumbered.

## Held proposals (amendment v1.1)

Held per `AMENDMENT_v1.1_N1_PREVIEWS.md` section A: removed from the post-image (never written to the carrier, so not a register deletion), recorded as a non-emitted proposal for the owner's separate transaction, ID reserved.

| HeldID | Reserved DependencyID | Edge | Direction/Type | Would form or join | Evidence it would have cited |
|---|---|---|---|---|---|
| H-018 | DEP-08-01-018 | DEL-08-01 -> DEL-06-03 (Initial Chirality MCP Read Tools): DEL-08-01's proposal-clause conformance checks consume the DEL-06-03 `propose` tool contract (the named triggers the Agent 0 and Agent 1 clauses invoke; once-per-chat refusal of an already-declined trigger) as the interface the clauses are checked against | UPSTREAM/INTERFACE, `TargetType=DELIVERABLE`, `PKG-06`, `SatisfactionStatus=PENDING`, `Confidence=HIGH` | New two-node SCC DEL-06-03/DEL-08-01 together with DEL-06-03's reciprocal proposal H-017 (DEP-06-03-014); `Evidence/fanin_simulation_v1/scc_summary.csv`, `edge_analysis.json` | `_STATUS.md#Remaining` (DEL-08-01-V3-01 Depends: "DEL-06-03-V3-01 (the tool the clauses invoke)"); `ScopeOfWork.md#Current acceptance obligations`; decomposition `#L252` (SOW-082) and `#L485` (Scope Ledger: the tool is DEL-06-03's, instruction-clause conformance is DEL-08-01's). FACT for the relation; the hold is a graph disposition, not a finding against the evidence. |

Row text as it stood in the v1 preview is preserved verbatim in `HELD_EDGE_PROPOSALS.csv` H-018. The v1 F1 check for this row (DEL-06-03 is not an SCC-001 member) stands; the hold arises from the fan-in of all thirteen previews, which no single preview could see.

## 3. Fence results

- **F1 (DEL-08-01 is not a member of SCC-001):** `NONE`. New EXECUTION rows target DEL-07-01 and two EXTERNAL targets (the held DEL-06-03 proposal is not in the post-image); none is in SCC-001 (DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05). A repo-wide scan of the 52 registers finds no SCC-001 member with an active row to DEL-08-01 (the only inbound row is DEL-04-04's DEP-04-04-005).
- **F2 (Root path):** `NONE`. Every new `TargetLocation` is `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (under `projects/chirality-app-dev/**`) or `TBD`. Root-owned targets (the `AGENTS.md` change-notice rule and G4 manifest validator; the owner grant) are `EXTERNAL`/`TBD`. Pre-existing DEP-08-01-013's REF-007 pointer is not a new emission and is listed under NEEDS_HUMAN_GRAPH_DECISION.
- **F3 (permitted effect):** `NONE` violated. Considered and not emitted, with the evidence that would have been cited: (a) `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected` (`_STATUS.md#Remaining`) — a selection/schedule gate, not an information flow; (b) DEL-07-03 governed workflow file contract (SOW-081, L484) — SOW-081 is not on this carrier's applied row and no source names the file contract as an input to the template-discoverability check; (c) DEL-06-02 catalog/collision validation, DEL-05-02 `proposal.*` consumption, DEL-02-02 proposal card (SOW-082 L485), DEL-09-04 packaging (SOW-030/SOW-073) — ownership statements with no artifact this carrier consumes or supplies.
- **NEEDS_HUMAN_GRAPH_DECISION:**
  1. Reciprocal DEL-04-04 edge. Scope Ledger L487: "DEL-08-01 owns packaging and conformance checks; DEL-04-04 composes from both layers." DEL-04-04's register already carries ACTIVE UPSTREAM PREREQUISITE DEP-04-04-005 to DEL-08-01 ("PersonaComposer requires a readable instruction root with required governance and agent resources"). This carrier's sources say DEL-08-01 *verifies* packaging and pins; they do not state an artifact DEL-08-01 supplies to DEL-04-04, so no DOWNSTREAM row is emitted under CONSERVATIVE strictness. The owner or reviewer may rule that the reciprocal edge is wanted for graph symmetry. HELP_HUMAN disposition (amendment v1.1 C.4, disposition-class, not a ruling): not invented; no change in this rerun; carried to the owner slate in `HANDOFF_STATE.md`. Remains open.
  2. DEP-08-01-013 `TargetLocation=/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md`. This is the pre-existing REF-007 pointer pinned by `_REFERENCES.md` (hash `ad849d9a…` equals this checkout's `agents/AGENT_SOFTWARE_DECOMP.md`, a Root `agents/` surface outside `projects/chirality-app-dev/**`). The relation is still stated (CLM-006) and the permitted effect covers only new relations and retirement of stale rows, so the field is preserved unchanged. A later reviewed write could convert it to `EXTERNAL`/`TBD` if ruled. HELP_HUMAN disposition (amendment v1.1 C.3, disposition-class, not a ruling): preserved unchanged (byte-identical to the v1 preview row); outside DEP-021's permitted effect; carried to the owner slate in `HANDOFF_STATE.md`. Remains open and is the one row-level `NEEDS_HUMAN_GRAPH_DECISION`, so `STATUS.json.status` stays `WARNINGS` under amendment section D.
- **FENCE_F1_CANDIDATES:** `none`.
- **FENCE_F2_CANDIDATES:** `none` (no candidate needed a Root path; the two Root-owned relations were emitted as `EXTERNAL`/`TBD`).

## 4. Validator outputs (verbatim)

Re-run at the amendment v1.1 rerun on the revised post-image.

Schema — `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-08-01/POSTIMAGE_Dependencies.csv` (exit 0):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-08-01/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 20
```

Enum summary — `python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct (enum, value) pair present in the post-image: 24 pairs, 24 `VALID`, 0 failures.

```text
ANCHOR_TYPE IMPLEMENTS_NODE -> VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE exit 0
ANCHOR_TYPE NOT_APPLICABLE -> VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE exit 0
ANCHOR_TYPE TRACES_TO_REQUIREMENT -> VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE exit 0
CONFIDENCE HIGH -> VALID: HIGH is a valid CONFIDENCE exit 0
CONFIDENCE MEDIUM -> VALID: MEDIUM is a valid CONFIDENCE exit 0
DEPENDENCY_CLASS ANCHOR -> VALID: ANCHOR is a valid DEPENDENCY_CLASS exit 0
DEPENDENCY_CLASS EXECUTION -> VALID: EXECUTION is a valid DEPENDENCY_CLASS exit 0
DEPENDENCY_TYPE CONSTRAINT -> VALID: CONSTRAINT is a valid DEPENDENCY_TYPE exit 0
DEPENDENCY_TYPE INTERFACE -> VALID: INTERFACE is a valid DEPENDENCY_TYPE exit 0
DEPENDENCY_TYPE OTHER -> VALID: OTHER is a valid DEPENDENCY_TYPE exit 0
DEPENDENCY_TYPE PREREQUISITE -> VALID: PREREQUISITE is a valid DEPENDENCY_TYPE exit 0
DIRECTION DOWNSTREAM -> VALID: DOWNSTREAM is a valid DIRECTION exit 0
DIRECTION UPSTREAM -> VALID: UPSTREAM is a valid DIRECTION exit 0
EXPLICITNESS EXPLICIT -> VALID: EXPLICIT is a valid EXPLICITNESS exit 0
ORIGIN EXTRACTED -> VALID: EXTRACTED is a valid ORIGIN exit 0
SATISFACTION_STATUS PENDING -> VALID: PENDING is a valid SATISFACTION_STATUS exit 0
SATISFACTION_STATUS SATISFIED -> VALID: SATISFIED is a valid SATISFACTION_STATUS exit 0
STATUS ACTIVE -> VALID: ACTIVE is a valid STATUS exit 0
TARGET_TYPE DELIVERABLE -> VALID: DELIVERABLE is a valid TARGET_TYPE exit 0
TARGET_TYPE DOCUMENT -> VALID: DOCUMENT is a valid TARGET_TYPE exit 0
TARGET_TYPE EXTERNAL -> VALID: EXTERNAL is a valid TARGET_TYPE exit 0
TARGET_TYPE PACKAGE -> VALID: PACKAGE is a valid TARGET_TYPE exit 0
TARGET_TYPE REQUIREMENT -> VALID: REQUIREMENT is a valid TARGET_TYPE exit 0
TARGET_TYPE UNKNOWN -> VALID: UNKNOWN is a valid TARGET_TYPE exit 0
```

ID format — `zsh tools/validation/validate_id_format.sh <TYPE> <value>` (known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```text
DEL DEL-08-01 -> INVALID: DEL-08-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)  exit=1
PKG PKG-08 -> INVALID: PKG-08 does not match PKG format (^PKG-[0-9]{3}$)  exit=1
DEP DEP-08-01-001 -> INVALID: DEP-08-01-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)  exit=1
DEP DEP-08-01-017 -> INVALID: DEP-08-01-017 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)  exit=1
DEP DEP-08-01-021 -> INVALID: DEP-08-01-021 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)  exit=1
SOW SOW-082 -> INVALID: SOW-082 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)  exit=1
SOW SOW-084 -> INVALID: SOW-084 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)  exit=1
OBJ OBJ-007 -> VALID: OBJ-007 matches OBJ format  exit=0
OBJ OBJ-008 -> VALID: OBJ-008 matches OBJ format  exit=0
```

Anchor check — rows with `Status=ACTIVE`, `DependencyClass=ANCHOR`, `AnchorType=IMPLEMENTS_NODE`: **1** (DEP-08-01-001). No `FLOATING_NODE`, no `AMBIGUOUS_ANCHOR`.

Other Function 5 checks — every ACTIVE row's `EvidenceFile` is a live SOW_V1 file and every `SourceRef` heading/CLM/REQ id, line number, and decomposition `#L<n>` resolves to non-empty live bytes (scripted check, 0 unresolved); every `EvidenceQuote` is at most 30 words; `FromDeliverableID=DEL-08-01` on all 20 rows; 20 unique `DependencyID`s (DEP-08-01-018 absent and reserved); `POSTIMAGE__DEPENDENCIES.md` metric, register-table, and lifecycle counts reconcile to the CSV (16 counts compared, 0 mismatches; register-table ID sequence equals the CSV sequence); the Run History row under `## Run History` carries ACTIVE 20; both post-images LF-only, no trailing whitespace, final newline. The `QUOTE_ALL` writer round-trips the v1 post-image byte-identically before the row removal, so the surviving 20 rows are byte-identical to their v1 preview bytes.

## 5. Epistemic notes

- FACT (016, 017): SOW-082 and SOW-084 are on the applied row L368 and in `ScopeOfWork.md` front matter and L14; the decomposition Scope Ledger names DEL-08-01 on both.
- FACT (019; held H-018): the owner-adopted seated item DEL-08-01-V3-01 (D-APP-108) names DEL-06-03-V3-01 "the tool the clauses invoke" and DEL-07-01-V3-01 "the layer protections the checks verify"; Scope Ledger L485/L487 make the same ownership split. `DependencyType=INTERFACE` is the extractor's classification of that stated consumption (a tool contract; a protection policy); PROPOSAL: a reviewer may prefer `PREREQUISITE` for either, which would not change direction, target, or SCC posture. The DEL-06-03 relation is unchanged as evidence; only its emission is held (graph disposition, amendment v1.1 A).
- FACT (020): the applied row Notes and acceptance obligation 3 state the routed-notice obligation; the G4 manifest is named in the same obligation and in the seated item's Checks line. ASSUMPTION: modelling the obligation as one DOWNSTREAM CONSTRAINT row on the Root rule (rather than one HANDOVER row per affected loop) because the affected loops are not enumerated in any allowed source.
- FACT (021): the seated item's `Depends` line states the owner grant verbatim.
- FACT (007–015): every retired-kit relation is restated in `ScopeOfWork.md` CLM-004/006/010/015 and the REQ table; nothing was retired. FACT (012): the prior `EvidenceQuote` sentence does not exist in SOW_V1 bytes, so it was replaced by the live CLM-004 sentence; the relation is unchanged.
- FACT: `_CONTEXT.md` `CoversScopeItems` (L45) still lists SOW-030, SOW-031, SOW-073 — the known Gate-5 audit `_CONTEXT.md` lag; `ScopeOfWork.md` and decomposition L368 are used as the anchor authority for SOW-082/SOW-084.
- ASSUMPTION (recorded, not acted on): `CHIRALITY_INSTRUCTION_ROOT` is not exported in this harness; the sealed brief's repository root is treated as the instruction root that owns `agents/`, `skills/`, and `tools/` (same posture as the Gate-5 precedent's additive runtime declaration).

## 6. Attribution

Rerun under amendment v1.1: Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
