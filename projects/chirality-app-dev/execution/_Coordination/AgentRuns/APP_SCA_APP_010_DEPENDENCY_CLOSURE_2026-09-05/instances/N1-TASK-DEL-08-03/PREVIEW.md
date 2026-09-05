# PREVIEW — N1-TASK-DEL-08-03 — TASK + dependency-extract (report-only)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-08-03` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, Node N1) |
| Carrier | `DEL-08-03` Pipeline Category and Task Scope Dispatch (UX_UI_SLICE, PKG-08); folder `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch` |
| Basis | `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` (HEAD is exactly this commit; branch `claude/sca-app-010-dependency-closure`) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (recomputed: MATCH); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (MATCH); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (MATCH) |
| Applied row | L370; amended Scope Ledger row SOW-007 L177; reverse view L410 (SOW-007), L429 (SOW-026); objectives L262 (OBJ-001), L268 (OBJ-007); OI-008 L602; DEC-025 L634 |
| Pre-image `Dependencies.csv` | SHA-256 `263656d18eee89339ceeca1f3cde386f88b98ba8369a7f21d96248eedd35d3fe` (MATCH; 10 data rows) |
| Pre-image `_DEPENDENCIES.md` | SHA-256 `ec4d6861aa2662326a7ede29c920825a8df9e299d307a4487d604dbb2d2a7b3f` (MATCH) |
| Post-image `POSTIMAGE_Dependencies.csv` | SHA-256 `7981ea6078052e96eebbaed06dade989e094260d659347e2eb8812f8a3fb7727` |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | SHA-256 `d8fbef7de157f70276c0cc90bd752802f4b8f61ba8f820a80c6a4620c8cf9294` |
| Row census (pre) | total 10 / ACTIVE 10 / RETIRED 0 / ANCHOR 5 / EXECUTION 5 |
| Row census (post) | total 10 / ACTIVE 10 / RETIRED 0 / ANCHOR 5 / EXECUTION 5 |
| Rows added / retired / deleted | 0 / 0 / 0 |
| Carrier bytes changed | none (`Dependencies.csv`, `_DEPENDENCIES.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` re-hashed unchanged after the run; `git status` shows only the untracked run folder) |

Runtime overrides in effect: `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`, `ANCHOR_DOC=ScopeOfWork.md`, `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]` (`_STATUS.md` `## Remaining` only; it is empty), `ApplyEdits=false`. Quoting convention preserved: every data field fully quoted, header unquoted, LF endings.

## 2. Row-level diff

`UNCHANGED` means byte-identical. Every row below keeps its `DependencyID`, `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, target identifiers, `TargetLocation`, `Explicitness`, `RequiredMaturity`, `ProposedMaturity`, `SatisfactionStatus`, `Confidence`, `Origin`, `FirstSeen`, and `Status` exactly as in the pre-image; `LastSeen` moves from `2026-05-20` (`2026-06-21` on row 009) to `2026-09-05` on every row.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-08-03-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | WBS_NODE DEL-08-03 (PKG-08) | `ScopeOfWork.md#front matter (deliverable_id, decomposition_basis); ScopeOfWork.md#CLM-002 — Identification; Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L370` | Fields changed: EvidenceFile, SourceRef, EvidenceQuote, LastSeen, Notes. Was `Datasheet.md#Identification; Datasheet.md#Attributes`. |
| DEP-08-03-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-007 | `ScopeOfWork.md#front matter (project_scope_refs); ScopeOfWork.md#Current responsibility; Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L177; #L410` | Fields changed: TargetName (`Pipeline selectors` -> `Presentation-neutral DECOMP/PREP/TASK/AUDIT dispatch lane semantics without an active-shell mount`), Statement (records the presentation half retired by SCA-APP-010), EvidenceFile, SourceRef, EvidenceQuote, LastSeen, Notes. This is the revised SOW-007 relation DEP-023 permits. |
| DEP-08-03-003 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-026 | `ScopeOfWork.md#front matter (project_scope_refs); ScopeOfWork.md#CLM-003 — Attributes; Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L429` | Fields changed: EvidenceFile, SourceRef, LastSeen, Notes. Label unchanged (L429 unchanged by SCA-APP-010). |
| DEP-08-03-004 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-001 | `ScopeOfWork.md#front matter (package_objective_refs); ScopeOfWork.md#Purpose and Objective Traceability; Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L262` | Fields changed: EvidenceFile, SourceRef, EvidenceQuote, LastSeen, Notes. Existing `TargetType=REQUIREMENT` objective convention preserved. |
| DEP-08-03-005 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-007 | `ScopeOfWork.md#front matter (package_objective_refs); ScopeOfWork.md#Purpose and Objective Traceability; Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L268` | Fields changed: EvidenceFile, SourceRef, EvidenceQuote, LastSeen, Notes. Notes carry an OBSERVATION that L268 omits SOW-007/SOW-026 while L410/L429 map them to OBJ-007. |
| DEP-08-03-006 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-004 `docs/TYPES.md#Section 4.4` | `ScopeOfWork.md#CLM-022 — Prerequisites; ScopeOfWork.md#CLM-029 — Principles; ScopeOfWork.md#CLM-014 — Standards` | Fields changed: EvidenceFile, SourceRef, LastSeen, Notes. Was `Guidance.md#Principles`; quote unchanged (same sentence lives in CLM-029). |
| DEP-08-03-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DOCUMENT REF-003 `docs/SPEC.md#Section 17.2` | `ScopeOfWork.md#CLM-013 — Requirements (DEL-08-03-REQ-010); ScopeOfWork.md#CLM-022 — Prerequisites; ScopeOfWork.md#CLM-014 — Standards` | Fields changed: EvidenceFile, SourceRef, EvidenceQuote, LastSeen, Notes. Notes record the `/api/project/deliverables` vs `/api/working-root/scope` label conflict inside `ScopeOfWork.md`; target unchanged. |
| DEP-08-03-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | DOCUMENT REF-002 `docs/CONTRACT.md#Section 1.8` | `ScopeOfWork.md#CLM-013 — Requirements (DEL-08-03-REQ-011); ScopeOfWork.md#CLM-014 — Standards; ScopeOfWork.md#CLM-031 — Boundary Rationale` | Fields changed: EvidenceFile, SourceRef, LastSeen, Notes. Was `Specification.md#Requirements`; quote unchanged (REQ-011). |
| DEP-08-03-009 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DOCUMENT REF-006 `docs/PRD.md#Section 8.2` | `ScopeOfWork.md#CLM-013 — Requirements (DEL-08-03-REQ-001 to DEL-08-03-REQ-008); ScopeOfWork.md#CLM-022 — Prerequisites` | Fields changed: EvidenceFile, SourceRef, LastSeen, Notes. Was `Specification.md#Requirements`; quote unchanged (REQ-001). |
| DEP-08-03-010 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | UNKNOWN (tests/records; consumer TBD) | `ScopeOfWork.md#CLM-025 — Records; ScopeOfWork.md#Current responsibility (applied row outputs); Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L370` | Fields changed: EvidenceFile, SourceRef, LastSeen, Notes. Was `Procedure.md#Records`; quote unchanged (CLM-025 opening sentence). Consumer stays `UNKNOWN`/`TBD` because L370 states no active presentation consumer exists. |

No `ADDED`, `RETIRED`, or `UNCHANGED` rows. No `Origin=DECLARED` row exists in this register. `Status=CANDIDATE` is not emitted.

## 3. Fence results

| Fence | Result |
|---|---|
| F1 (SCC-001 membership) | `NONE`. SCC-001 = {DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05} (`Evidence/baseline_closure/scc_summary.csv`). DEL-08-03 is not a member; no post-image row targets a member; no SCC-internal retirement. |
| F2 (Root path) | `NONE`. Every `TargetLocation` is either `execution/_Decomposition/...` (under `projects/chirality-app-dev/`), a repo-root `docs/*.md` file pinned by this carrier's `_REFERENCES.md` (REF-002, REF-003, REF-004, REF-006), or `TBD`. No Root-owned semantics are consumed by this carrier, so no `EXTERNAL`/`TBD` row was required. |
| F3 (permitted effect) | `NONE`. The only substantive change is the SOW-007 relation revised by SCA-APP-010 (row 002); all other changes are re-evidencing of live-byte pointers and `LastSeen`. No edge was inferred from SCC ordering, schedule, or "keep aligned" statements. |
| NEEDS_HUMAN_GRAPH_DECISION | none |
| FENCE_F1_CANDIDATES | none |
| FENCE_F2_CANDIDATES | none |

### Considered candidates not emitted (reported, not suppressed)

| Candidate | Would-be evidence | Why withheld |
|---|---|---|
| `DEL-08-03 -> DEL-02-02` DOWNSTREAM INTERFACE (presentation consumer of dispatch semantics) | `ScopeOfWork.md#CLM-004 — Conditions` ("Presentation ownership | DEL-02-02 presents re-hosted Workbench/Pipeline..."), `#CLM-012 — Scope`, `#CLM-013 — Requirements (DEL-08-03-REQ-013)`, `#CLM-023 — Steps` (step 9), `_CONTEXT.md#SCA-APP-004 Ownership Boundary` | These are dated compatibility clauses. The controlling `## SCA-APP-010 Gate-5 Current Contract` section, applied row L370 ("no active presentation consumer exists"), reverse view L410 ("no presentation consumer is mapped"), and DEL-02-02's applied row L308 ("Workbench and Pipeline are retired from the active shell") supersede them (DEC-025; SOW-007 presentation half retired by owner ruling G2-CONFIRM). The owner has already ruled, so no graph decision is open. Not an F1 candidate (DEL-02-02 is not in SCC-001); no prior row existed, so nothing to retire. DEL-02-02's own register still holds `DEP-02-02-009` (CONSTRAINT toward DEL-08-03, legacy `Guidance.md` evidence); that is `N1-TASK-DEL-02-02`'s scope. |
| Partition statements toward DEL-08-05, DEL-05-04, DEL-08-02 | `ScopeOfWork.md#CLM-004` ("Child-record boundary"), `#CLM-013 (DEL-08-03-REQ-016)`, `_CONTEXT.md#SCA-APP-004 Ownership Boundary`, applied row L370 Notes | Ownership/non-ownership statements with no named artifact, contract, tool, event, or policy consumed or supplied by this carrier; coordination or boundary, not information flow (brief Method 3; skill "Information flow only"). Existing inbound rows `DEP-02-03-009` and `DEP-08-02-013` belong to their carriers. |
| "Any later consumer may not infer plans/tasks from conversational prose" (L370 Notes; `ScopeOfWork.md#Current acceptance obligations` item 3) | applied row L370; `ScopeOfWork.md#Current acceptance obligations` | A rule attached to this carrier's semantics for an unnamed future consumer; no target and no artifact transfer. Recorded in Run Notes and in row 010 Notes context, not as an edge. |
| SOW-081 to SOW-084 anchors | reverse view L484 to L487 | Not carried by DEL-08-03 (applied row L370 lists only SOW-007, SOW-026); brief Method 2 adds them only "where this carrier carries them". |

## 4. Validator outputs (verbatim)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py .../POSTIMAGE_Dependencies.csv`, exit 0):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-08-03/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 10
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct value present in the post-image; all exit 0):

```text
DEPENDENCY_CLASS ANCHOR -> exit=0 VALID: ANCHOR is a valid DEPENDENCY_CLASS
DEPENDENCY_CLASS EXECUTION -> exit=0 VALID: EXECUTION is a valid DEPENDENCY_CLASS
ANCHOR_TYPE IMPLEMENTS_NODE -> exit=0 VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
ANCHOR_TYPE TRACES_TO_REQUIREMENT -> exit=0 VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
ANCHOR_TYPE NOT_APPLICABLE -> exit=0 VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
DIRECTION UPSTREAM -> exit=0 VALID: UPSTREAM is a valid DIRECTION
DIRECTION DOWNSTREAM -> exit=0 VALID: DOWNSTREAM is a valid DIRECTION
DEPENDENCY_TYPE OTHER -> exit=0 VALID: OTHER is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE PREREQUISITE -> exit=0 VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE INTERFACE -> exit=0 VALID: INTERFACE is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE CONSTRAINT -> exit=0 VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE HANDOVER -> exit=0 VALID: HANDOVER is a valid DEPENDENCY_TYPE
TARGET_TYPE WBS_NODE -> exit=0 VALID: WBS_NODE is a valid TARGET_TYPE
TARGET_TYPE REQUIREMENT -> exit=0 VALID: REQUIREMENT is a valid TARGET_TYPE
TARGET_TYPE DOCUMENT -> exit=0 VALID: DOCUMENT is a valid TARGET_TYPE
TARGET_TYPE UNKNOWN -> exit=0 VALID: UNKNOWN is a valid TARGET_TYPE
EXPLICITNESS EXPLICIT -> exit=0 VALID: EXPLICIT is a valid EXPLICITNESS
CONFIDENCE HIGH -> exit=0 VALID: HIGH is a valid CONFIDENCE
CONFIDENCE MEDIUM -> exit=0 VALID: MEDIUM is a valid CONFIDENCE
ORIGIN EXTRACTED -> exit=0 VALID: EXTRACTED is a valid ORIGIN
STATUS ACTIVE -> exit=0 VALID: ACTIVE is a valid STATUS
SATISFACTION_STATUS TBD -> exit=0 VALID: TBD is a valid SATISFACTION_STATUS
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; the known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```text
INVALID: DEL-08-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
exit=1
INVALID: PKG-08 does not match PKG format (^PKG-[0-9]{3}$)
exit=1
INVALID: DEP-08-03-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
exit=1
INVALID: SOW-007 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
exit=1
VALID: OBJ-001 matches OBJ format
exit=0
```

Anchor check and other Function 5 checks (deterministic script over the post-image):

```text
unique ids True ['DEP-08-03-001', ..., 'DEP-08-03-010']
census total 10 ACTIVE 10 RETIRED 0 ANCHOR 5 EXECUTION 5
active IMPLEMENTS_NODE 1
active rows w/o evidence []
FromDeliverableID ['DEL-08-03']; FromPackageID ['PKG-08']; EvidenceFile ['ScopeOfWork.md']; LastSeen ['2026-09-05']
```

Every `SourceRef` heading or identifier resolves to live bytes in the carrier's `ScopeOfWork.md` (each of `## Purpose and Objective Traceability`, `### Current responsibility`, `### CLM-002 — Identification`, `### CLM-003 — Attributes`, `### CLM-013 — Requirements`, `### CLM-014 — Standards`, `### CLM-022 — Prerequisites`, `### CLM-025 — Records`, `### CLM-029 — Principles`, `### CLM-031 — Boundary Rationale`, the front-matter keys, and REQ-001/008/010/011 found by grep) and the decomposition line pointers L177, L262, L268, L370, L410, L429 were read at the pinned identity. `_DEPENDENCIES.md` post-image counts (Total 10 / ACTIVE 10 / RETIRED 0 / ANCHOR 5 / EXECUTION 5; SatisfactionStatus TBD 10) reconcile to the CSV; the new Run History row sits under `## Run History`. Whitespace: no trailing whitespace, no CR, final newline on every written file.

## 5. Epistemic notes

- FACT (all ten rows): each relation is restated verbatim or near-verbatim in the live `ScopeOfWork.md` (SOW_V1) at the cited heading; the four legacy kit files do not exist in the carrier, which is why every row was re-evidenced rather than left on dead pointers.
- FACT (row 002): the amended label and the presentation retirement come from decomposition L177/L410 and DEC-025 at the pinned identity, and from the carrier's own controlling section; the legacy label is preserved in `Notes`.
- FACT (row 010): the applied row's outputs list is the live basis for the handover; the consumer is unresolved by the sources, not by omission.
- ASSUMPTION (none material): `SatisfactionStatus` and `ProposedMaturity` were left at `TBD` on purpose rather than promoted; CLM-007 states satisfaction is TBD until dependency closure accepts the register. Promoting them would be an acceptance act this preview cannot make.
- PROPOSAL (not emitted as rows): the `/api/project/deliverables` vs `/api/working-root/scope` wording in `ScopeOfWork.md` and the `_CONTEXT.md#Anticipated Artifacts` vs L370 outputs wording are document-consistency items for RECONCILIATION; they do not change the graph.
- OBSERVATION: OBJ-007 row L268 does not list SOW-007/SOW-026 while the ledger reverse view does; the anchor stands on the applied row and ledger, which the decomposition declares authoritative for scope-item assignment (L400).
- Convention note: this carrier's existing objective anchors use `TargetType=REQUIREMENT` (not `UNKNOWN`); that existing convention was preserved unchanged per the brief's "keep the existing convention" instruction.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
