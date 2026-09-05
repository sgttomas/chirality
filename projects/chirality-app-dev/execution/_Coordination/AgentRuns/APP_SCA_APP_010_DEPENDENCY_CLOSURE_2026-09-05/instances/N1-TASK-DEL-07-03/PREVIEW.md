# PREVIEW — N1-TASK-DEL-07-03 — DEL-07-03 dependency extraction (report-only)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-07-03` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N1) |
| Role | `TASK` (Agent 2) + `TaskSkill: dependency-extract`; report-only preview; no carrier byte changed |
| Carrier | `DEL-07-03` Deliverable Metadata and Document Kit Contracts (BACKEND_FEATURE_SLICE, PKG-07); folder `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts` |
| Basis | `HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` (exact; PR #713 merge), branch `claude/sca-app-010-dependency-closure`, working tree clean except this run folder |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches brief) at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches `ScopeOfWork.md` front matter `decomposition_basis`) |
| Companion register | `contract_invariant_coverage_register.csv` SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (match) |
| Pointer | `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (match; names SCA-APP-010) |
| Authorization | SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-019 (`Dependencies.csv`) and DEP-020 (`_DEPENDENCIES.md`); this instance writes only under its own folder |
| Pre-image `Dependencies.csv` | SHA-256 `20d27430ebc0e7069a39820b692fb97068396600c1a9cd5fcceb757786a30487` (match; 10 data rows) |
| Pre-image `_DEPENDENCIES.md` | SHA-256 `874220f71f851ff64eaabc387212ba40dc3231ce6348926b5c3da6400eebad77` (match) |
| Post-image `POSTIMAGE_Dependencies.csv` | SHA-256 `54d8dc8cff7338b164264eee9a7dd6a48e6bd364177a38e50ee4991e166715ed` |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | SHA-256 `8c8fe0324138c219493cae174545d6e5b4674f6db16ba8a6700059945fbfb297` |

Row census (total / ACTIVE / RETIRED / ANCHOR / EXECUTION):

| Image | Total | ACTIVE | RETIRED | ANCHOR | EXECUTION | UPSTREAM | DOWNSTREAM |
|---|---:|---:|---:|---:|---:|---:|---:|
| Pre-image | 10 | 10 | 0 | 2 | 8 | 10 | 0 |
| Post-image | 14 | 14 | 0 | 3 | 11 | 12 | 2 |

Runtime overrides in effect: `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`, `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`, `ANCHOR_DOC=ScopeOfWork.md`, `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`, `ApplyEdits=false`. `_STATUS.md` was used only for its `## Remaining` section. `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` were not used as evidence.

## 2. Row-level diff

`UNCHANGED` means byte-identical to the pre-image row. `RE-EVIDENCED` means the relation is still stated in live sources and only `EvidenceFile`, `SourceRef`, `EvidenceQuote`, `LastSeen`, and an appended `Notes` clause changed (all other fields byte-identical).

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-07-03-001 | RE-EVIDENCED | ANCHOR / IMPLEMENTS_NODE | UPSTREAM / OTHER | WBS_NODE SOW-026 Metadata files and document kit | `ScopeOfWork.md#CLM-002 — Identification; #front matter project_scope_refs; _CONTEXT.md#Traceability; decomposition#L359; #L429` | Sole parent anchor preserved with its ID. Was `Datasheet.md#Identification` (file retired). SOW-026 remains on applied row L359. `LastSeen=2026-09-05`. |
| DEP-07-03-002 | RE-EVIDENCED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT OBJ-006 | `ScopeOfWork.md#Purpose and Objective Traceability; #front matter package_objective_refs; _CONTEXT.md#Traceability; decomposition#L267` | Was `Datasheet.md#Identification`. `TargetType=REQUIREMENT` kept: this register's existing objective convention (the brief's `UNKNOWN` clause describes other registers; DEL-08-04 precedent also uses REQUIREMENT). `EvidenceQuote` refreshed to the live phrase. |
| DEP-07-03-003 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT DEL-07-03 decomposition entry | `ScopeOfWork.md#CLM-020 — Prerequisites; #front matter decomposition_basis; decomposition#L359` | Was `Procedure.md#Prerequisites`. Restated verbatim in CLM-020 row 1. |
| DEP-07-03-004 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT REF-003 `docs/SPEC.md` | `ScopeOfWork.md#CLM-020 — Prerequisites; #CLM-013 — Standards; _REFERENCES.md#REF-003` | Was `Procedure.md#Prerequisites`. Restated in CLM-020 row 2; REF-003 MATCH. |
| DEP-07-03-005 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT REF-006 `docs/PRD.md` | `ScopeOfWork.md#CLM-020 — Prerequisites; #CLM-013 — Standards; _REFERENCES.md#REF-006` | Was `Procedure.md#Prerequisites`. Restated in CLM-020 row 3; REF-006 MATCH (D-APP-38 note preserved). |
| DEP-07-03-006 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT REF-004 `docs/TYPES.md` | `ScopeOfWork.md#CLM-020 — Prerequisites; #CLM-013 — Standards; _REFERENCES.md#REF-004` | Was `Procedure.md#Prerequisites`. Restated in CLM-020 row 4; REF-004 MATCH. |
| DEP-07-03-007 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT REF-001 `docs/DIRECTIVE.md` | `ScopeOfWork.md#CLM-020 — Prerequisites; #CLM-013 — Standards; _REFERENCES.md#REF-001` | Was `Procedure.md#Prerequisites`. Restated in CLM-020 row 5; REF-001 MATCH. |
| DEP-07-03-008 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | DOCUMENT REF-002 `docs/CONTRACT.md` | `ScopeOfWork.md#CLM-020 — Prerequisites; #CLM-013 — Standards; _REFERENCES.md#REF-002` | Was `Procedure.md#Prerequisites`. Restated in CLM-020 row 5; REF-002 MATCH. |
| DEP-07-03-009 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / CONSTRAINT | DELIVERABLE DEL-07-04 Status Transition API and MCP Tool | `ScopeOfWork.md#CLM-021 — Steps; #CLM-008 — Scope; decomposition#L360` | Was `Procedure.md#Steps`. Restated in CLM-021 step 8 and CLM-008 out-of-scope; DEL-07-04 exists at L360. Notes add that the SOW-081 steer-never-record rule keeps status in deliverable records (boundary unchanged). |
| DEP-07-03-010 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / CONSTRAINT | DELIVERABLE DEL-07-05 Dependencies.csv v3.1 Reader Writer and Linter | `ScopeOfWork.md#CLM-021 — Steps; #CLM-008 — Scope; decomposition#L361` | Was `Procedure.md#Steps`. Restated in CLM-021 step 8 and CLM-008; DEL-07-05 exists at L361. |
| DEP-07-03-011 | ADDED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT SOW-081 Governed workflow files under `.chirality/workflows/` and the right-panel Workflows view with follow, pause, create, library, and bind | `ScopeOfWork.md#front matter project_scope_refs; #Current responsibility; decomposition#L359; #L251; #L484` | SOW-081 is new on applied row L359 (DEC-025 L634). `TargetLocation=execution/_Decomposition/...#scope-ledger-sow-081` follows DEP-07-03-001's convention. `SatisfactionStatus=TBD` as for the existing anchors. |
| DEP-07-03-012 | ADDED | EXECUTION / NOT_APPLICABLE | DOWNSTREAM / INTERFACE | DELIVERABLE PKG-02 DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX | `execution/_Decomposition/...#L484; #L308; ScopeOfWork.md#Current acceptance obligations` | Ownership split on L484 ("DEL-07-03 owns the file contract; DEL-02-02 owns the view and forms") plus L308 ("Workflows view, roadmap, New workflow form, library, and bind actions over governed workflow files"): this carrier supplies a named contract that DEL-02-02 consumes. `SatisfactionStatus=PENDING` until DEL-07-03-V3-01 lands. |
| DEP-07-03-013 | ADDED | EXECUTION / NOT_APPLICABLE | DOWNSTREAM / INTERFACE | DELIVERABLE PKG-04 DEL-04-04 PersonaComposer from Instruction Root | `execution/_Decomposition/...#L484; #L329; #L251; ScopeOfWork.md#Current acceptance obligations` | L484 ("DEL-04-04 owns the delimited roadmap-injection seam"), L329 ("clearly delimited roadmap-injection block for a followed governed workflow"), L251 ("steers the chat by delimited context injection"): DEL-04-04 consumes the roadmap grammar, `roadmapSource`, and hash this carrier defines. `PENDING`. |
| DEP-07-03-014 | ADDED | EXECUTION / NOT_APPLICABLE | UPSTREAM / CONSTRAINT | EXTERNAL K-PATH-2 path-containment invariant for governed workflow file writes; `TargetLocation=TBD` | `execution/_Decomposition/...#L251; #L329; ScopeOfWork.md#CLM-009 — Requirements` | "Writes obey K-PATH-2 containment." (L251) is an explicit constraint introduced by the amended row. K-PATH-2 is not defined in the pinned `docs/CONTRACT.md` (REF-002; `grep` over `docs/*.md` finds no definition), so the owning document is unresolved: `EXTERNAL` / `TBD` / `PENDING` per the Root-owned convention, `Confidence=MEDIUM`. No Root path is named. |

No row was retired: every pre-image relation is restated in live `ScopeOfWork.md` bytes, and no scope ref left the applied row. No `Origin=DECLARED` row exists in the pre-image. No `UNCHANGED` row exists because every pre-image row cited a retired kit file and had to be re-evidenced.

## 3. Fence results

- **F1 (SCC-001 membership): `NONE`.** DEL-07-03 is not an SCC-001 member (`Evidence/n1_preimages.json` `scc_001_member: false`; `Evidence/baseline_closure/scc_summary.csv` lists DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05). The new EXECUTION targets DEL-02-02 and DEL-04-04 are not SCC-001 members. A grep over every `Dependencies.csv` under `projects/chirality-app-dev/execution/PKG-*/1_Working/` finds only DEL-02-03 (`DEP-02-03-006`, not an SCC-001 member) holding an active row back to DEL-07-03. No SCC-internal retirement.
- **F2 (Root path): `NONE`.** `TargetLocation` values: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#…` (existing project-relative convention), `docs/SPEC.md`, `docs/PRD.md`, `docs/TYPES.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md` (all pinned by `_REFERENCES.md` REF-001 to REF-006), and `TBD` (DEP-07-03-014). No Root path.
- **F3 (permitted effect): `NONE`.** DEP-07-03-011 to DEP-07-03-014 derive only from amended Scope Ledger row SOW-081 (L251), its reverse-view row (L484), the co-carrier rows the reverse view names (L308, L329), and applied row L359 prose. No edge was taken from SCC ordering, schedule, gates, or "keep aligned" statements.
- **NEEDS_HUMAN_GRAPH_DECISION: `none`.**
- **FENCE_F1_CANDIDATES: `none`.**
- **FENCE_F2_CANDIDATES: `none`.** (The seated item's `plans/shell-redesign_2026-09-04/` design-basis pins are neither Root paths nor `_REFERENCES.md`-pinned files; they were excluded under F3 and CONSERVATIVE strictness before F2 was reached, see section 5.)

Considered and not emitted (for the reviewer's completeness, each with the evidence that would have been cited):

| Candidate | Would have cited | Why not emitted |
|---|---|---|
| DEL-08-03 (SOW-026 co-carrier) | decomposition L429 | Structural adjacency on an unamended row (DEC-004); no artifact transfer stated. F3 / skill "structural adjacency" exclusion. |
| DEL-08-01 skill-declared workflow templates; app-scoped known-folder set behind the library | L251 ("library of other known folders and skill-declared templates"), L368, L405 | The library is the view's half (DEL-02-02); no consumption by this carrier's file contract is stated. CONSERVATIVE. |
| Root DEL-02-11 delegation-policy session-record field (OI-008) as an input to the front-matter `delegation policy` declaration | L251, L602, L486, `_STATUS.md` Remaining | Not stated for this carrier; OI-008 binds the field to SOW-010/SOW-083 carriers; the seated item records `Depends: none`. Would have been an ASSUMPTION-level EXTERNAL row; not emitted under CONSERVATIVE. |
| `plans/shell-redesign_2026-09-04/03_TARGET_SPEC.md` §5.10 and `04_IMPLEMENTATION_PLAN.md` (SHA-pinned in the seated item) | `_STATUS.md#Remaining` DEL-07-03-V3-01 Plan line | Cited "only for what the tranche means when complete, never as a queue"; not on the applied or amended rows (F3); owner-seated Remaining work is "not decomposition scope" (DEC-025). |
| Seated item gates and checks (frontend gates, APP-HOLD-1, `software-code-review`, A1 re-stage) | `_STATUS.md#Remaining` Checks line | Verification/schedule gates, not information flow. |
| OI-008 Q15/Q16 owner rulings as a CONSTRAINT | L251, L602 | Conflicts with the D-APP-108 seating (see section 5); no edge either way is decisive; recorded as `CONFLICT`, not a graph decision. |

## 4. Validator outputs (verbatim)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py …/N1-TASK-DEL-07-03/POSTIMAGE_Dependencies.csv`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-07-03/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 14
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for each of the 23 distinct (enum, value) pairs present in the post-image; every line as printed):

```text
VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
VALID: HIGH is a valid CONFIDENCE
VALID: MEDIUM is a valid CONFIDENCE
VALID: ANCHOR is a valid DEPENDENCY_CLASS
VALID: EXECUTION is a valid DEPENDENCY_CLASS
VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
VALID: INTERFACE is a valid DEPENDENCY_TYPE
VALID: OTHER is a valid DEPENDENCY_TYPE
VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
VALID: DOWNSTREAM is a valid DIRECTION
VALID: UPSTREAM is a valid DIRECTION
VALID: EXPLICIT is a valid EXPLICITNESS
VALID: EXTRACTED is a valid ORIGIN
VALID: PENDING is a valid SATISFACTION_STATUS
VALID: TBD is a valid SATISFACTION_STATUS
VALID: ACTIVE is a valid STATUS
VALID: DELIVERABLE is a valid TARGET_TYPE
VALID: DOCUMENT is a valid TARGET_TYPE
VALID: EXTERNAL is a valid TARGET_TYPE
VALID: REQUIREMENT is a valid TARGET_TYPE
VALID: WBS_NODE is a valid TARGET_TYPE
enum pairs 23 valid 23
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; known `PROJECT_ID_FORMAT_PROFILE` warning, no ID changed):

```text
INVALID: DEL-07-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-07 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-07-03-011 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-081 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-006 matches OBJ format
```

Anchor and provenance checks (Python over the post-image; each line as printed):

```text
unique ids: True 14
from ok: True
ACTIVE IMPLEMENTS_NODE: 1
evidence populated: True
census total 14 active 14 retired 0 anchor 3 execution 11
dir Counter({'UPSTREAM': 12, 'DOWNSTREAM': 2})
sat Counter({'TBD': 11, 'PENDING': 3})
reqmat Counter({'SEMANTIC_READY': 14})
candidate present: False
```

`_DEPENDENCIES.md` reconciliation (every metric in the post-image tables compared to the post-image CSV): Total 14, ACTIVE 14, RETIRED 0, ANCHOR 3, EXECUTION 11, UPSTREAM 12, DOWNSTREAM 2, SatisfactionStatus TBD 11 / PENDING 3, RequiredMaturity SEMANTIC_READY 14 — all `OK`; all 14 `DependencyID`s present in the compact table. Line endings LF, no trailing whitespace, final newline on every written file. `git status --short` shows only the untracked run folder; `git diff --check` clean.

Evidence resolution to live bytes: every `ScopeOfWork.md#<heading>` cited exists in the current file (front matter lines 5 to 7; `## Purpose and Objective Traceability`; `### Current responsibility`; `### Current acceptance obligations`; `### CLM-002 — Identification`; `### CLM-008 — Scope`; `### CLM-009 — Requirements`; `### CLM-013 — Standards`; `### CLM-020 — Prerequisites`; `### CLM-021 — Steps`); `_CONTEXT.md#Traceability` exists; `_REFERENCES.md#REF-00n` rows exist with MATCH; decomposition line numbers L251, L267, L308, L329, L359, L360, L361, L429, L484 resolve to the quoted rows at the pinned hash.

## 5. Epistemic notes

- DEP-07-03-001 to DEP-07-03-010 — **FACT**: each relation is restated verbatim or near-verbatim in `ScopeOfWork.md` (CLM-020 Prerequisites table; CLM-021 step 8; CLM-008 out-of-scope; CLM-002 Identification; Purpose and Objective Traceability). Re-evidencing changed no relation, target, status, or maturity field.
- DEP-07-03-002 — **FACT** for the anchor; **interpretation**: `TargetType=REQUIREMENT` retained because the brief's "existing `TargetType=UNKNOWN` convention" does not exist in this register (its existing objective row already uses REQUIREMENT). Changing it would alter a preserved field without source basis.
- DEP-07-03-011 — **FACT**: `project_scope_refs: [SOW-026, SOW-081]`; L359 lists SOW-026, SOW-081; L251 and L484 define SOW-081; DEC-025 records the addition. Interpretation: SOW-026 stays the sole `IMPLEMENTS_NODE`; SOW-081 is a trace anchor, so exactly one parent anchor remains.
- DEP-07-03-012 and DEP-07-03-013 — **FACT** for the ownership split and consumption statements (L484, L308, L329, L251). **Interpretation**: typed `INTERFACE` (a contract shared across an ownership boundary) rather than `HANDOVER`; `DOWNSTREAM` because the contract flows from this carrier to the consumers. **PROPOSAL** (not encoded): the DEL-02-02 and DEL-04-04 registers should carry the reciprocal `UPSTREAM` rows from their own passes.
- DEP-07-03-014 — **FACT**: "Writes obey K-PATH-2 containment." (L251) and "K-PATH-2-contained file" (L329); REQ-008 states working-root containment. **ASSUMPTION** (labelled in `Notes`): K-PATH-2 is a Root-owned CONTRACT invariant; the pinned App `docs/CONTRACT.md` (REF-002) does not define it, and the decomposition cites it next to Root-attributed K-KEY-1 and K-EVENT-3. Hence `EXTERNAL`, `TargetLocation=TBD`, `SatisfactionStatus=PENDING`, `Confidence=MEDIUM`. If the owner resolves K-PATH-2 to an App-pinned document, the reviewed write may re-type it as `DOCUMENT` with a pinned path.
- **CONFLICT** (documentary, no edge): decomposition L251 and OI-008 L602 say Q16 (shared-folder position advance) "remain[s] OI-008", while `_STATUS.md` `## Remaining` DEL-07-03-V3-01 and `ScopeOfWork.md` Current acceptance obligations record "Q16 ruled D-APP-108" (app-maintained position with who-advanced attribution). Surfaced in the post-image Run Notes and handoff notes for RECONCILIATION and the OI-008 register owner; not resolved here.
- Instruction-root normalization note: `CHIRALITY_INSTRUCTION_ROOT` is unset in this process environment and no `V2_INSTRUCTION_ROOT_RUNTIME_DECLARATION.md` exists in the checkout; `INSTRUCTION_ROOT` was resolved from the sealed brief's declared repository root (the checkout that owns `agents/`, `skills/`, and `tools/`). Recorded as a warning in the run record; no write or read outside the brief followed from it.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
