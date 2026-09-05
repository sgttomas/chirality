# PREVIEW — N1-TASK-DEL-04-04 — DEL-04-04 dependency extraction (report-only)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-04-04` in run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` (Node N1; parent HELP_HUMAN) |
| Carrier | `DEL-04-04` PersonaComposer from Instruction Root (BACKEND_FEATURE_SLICE, PKG-04); folder `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root` |
| Basis | `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` = `HEAD` on `claude/sca-app-010-dependency-closure` (exact; verified) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (exact match; content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (exact); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (exact) |
| Pre-image `Dependencies.csv` | `23a9370244149417f785706608f5507ef091b45d62a34365dfbdd0ce01a32850` (exact; 8 data rows) |
| Pre-image `_DEPENDENCIES.md` | `d418bf2e51b0e73676429af96a6cb94943aba147907d688c53588e64ee768c2d` (exact) |
| Post-image `POSTIMAGE_Dependencies.csv` | `1cb90e1ff30b50fb08c9f9f06aa65ad74ac63b92ab0ebbcecdf52ec93cde8034` |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `1896ed236a76269842419a20021d9b1691da2e3b30dea3e5db9dbd2df42cb352` |
| Row census pre | 8 total / 7 ACTIVE / 1 RETIRED / 3 ANCHOR / 5 EXECUTION |
| Row census post | 14 total / 13 ACTIVE / 1 RETIRED / 7 ANCHOR / 7 EXECUTION (ACTIVE: 7 ANCHOR, 6 EXECUTION) |
| Authorization | SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-011, DEP-012 (report-only preview); no byte under the carrier folder was changed |

Sources read for extraction: `ScopeOfWork.md` (anchor and execution), `_CONTEXT.md`, `_STATUS.md` (`## Remaining` only), `_REFERENCES.md` (pointer resolution only), the applied decomposition at L329, L251, L254, L265, L268, L357, L359, L404 to L487, L602, L634. Excluded: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_INSP-03_DEL-04-04.md`, `_run_records/**`. Other deliverable folders were opened only to confirm that DEL-07-01, DEL-07-03, DEL-08-01, DEL-08-02, and DEL-04-02 exist and to quote their applied rows.

## 2. Row-level diff (every post-image row)

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-04-04-001 | REFRESHED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PACKAGE PKG-04 | `_CONTEXT.md#Identity` | `LastSeen` 2026-05-20 to 2026-09-05; sole parent anchor preserved |
| DEP-04-04-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-017 | `_CONTEXT.md#Traceability` | `LastSeen` refreshed; SOW-017 remains on applied row L329 |
| DEP-04-04-003 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-030 | `_CONTEXT.md#Traceability` | `LastSeen` refreshed; SOW-030 remains on applied row L329 |
| DEP-04-04-004 | UNCHANGED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-04-02 | `Procedure.md#Prerequisites` (legacy, RETIRED row) | Byte-identical; stays RETIRED under RUL-SCC-001-TRANCHE-001; see NEEDS_HUMAN_GRAPH_DECISION |
| DEP-04-04-005 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DELIVERABLE DEL-08-01 | `ScopeOfWork.md#PC-REQ-001` | From `Procedure.md#Prerequisites`; Statement extended to the organisation layer and pins per SOW-084 (L254, L487); `LastSeen` refreshed; `SatisfactionStatus` stays TBD |
| DEP-04-04-006 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-08-02 | `ScopeOfWork.md#PC-REQ-005` | From `Specification.md#Requirements`; Notes cite CLM-007 (UPD-122 accepted alias delegation); Confidence stays MEDIUM (resolver interface unnamed) |
| DEP-04-04-007 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | DOCUMENT `docs/PRD.md` | `ScopeOfWork.md#CLM-029` | From `Guidance.md#Source-State-Warning`; Statement rewritten (REF-006 MATCH under D-APP-38); `SatisfactionStatus` TBD to SATISFIED (PROPOSAL) |
| DEP-04-04-008 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/HANDOVER | UNKNOWN runtime boundary fingerprint integration | `ScopeOfWork.md#CLM-018` | From `Procedure.md#Steps`; target stays UNKNOWN/TBD; payload note adds layer pin and roadmap hash from seated item |
| DEP-04-04-009 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-081 (PKG-07) | `ScopeOfWork.md#Purpose and Objective Traceability` | New scope ref on applied row L329; ledger L251; reverse view L484 names DEL-04-04 owner of the roadmap-injection seam |
| DEP-04-04-010 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-084 (PKG-07) | `ScopeOfWork.md#Purpose and Objective Traceability` | New scope ref on applied row L329; ledger L254; reverse view L487 (Q14 ruled) |
| DEP-04-04-011 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-004 | `ScopeOfWork.md#Purpose and Objective Traceability` | Objective anchor; `TargetType=UNKNOWN` convention with the existing note |
| DEP-04-04-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-007 | `ScopeOfWork.md#Purpose and Objective Traceability` | Objective anchor; same convention |
| DEP-04-04-013 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-07-03 (PKG-07) | `_STATUS.md#Remaining` | Governed workflow file contract the seam reads; SOW-081 L251/L484; obligation 2; `SatisfactionStatus=PENDING` (gate: DEL-07-03-V3-01 landed) |
| DEP-04-04-014 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-07-01 (PKG-07) | `_STATUS.md#Remaining` | Organisation-layer protection and pin the composer verifies before use; SOW-084 L254/L487; obligation 1; `SatisfactionStatus=PENDING` (gate: DEL-07-01-V3-01 selected) |

`_DEPENDENCIES.md` post-image: declared sections and headings preserved; `## Extracted Dependency Register` refreshed (the pre-image count table listed DEP-04-04-004 as ACTIVE INTERFACE; the post-image shows it RETIRED, matching the D-APP-56 correction); new `## Run Notes - 2026-09-05 ...` section; one new row appended under `## Run History`; `## Lifecycle Summary` refreshed (ACTIVE 13 / RETIRED 1; NOT_APPLICABLE 8, PENDING 2, SATISFIED 1, TBD 3); new `## Downstream Handoff Notes` for RECONCILIATION; the D-APP-56 mirror block kept with one dated supersession note.

## 3. Fence results

- **F1 (SCC-001 membership):** NONE. DEL-04-04 is not in SCC-001 (`Evidence/baseline_closure/scc_summary.csv`: DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05). No new EXECUTION row targets an SCC-001 member; the new targets are DEL-07-03 and DEL-07-01. No SCC-internal retirement.
- **F2 (Root path):** NONE. Every `TargetLocation` is under `execution/_Decomposition/...` (project-relative, under `projects/chirality-app-dev/**`), `docs/PRD.md` (pinned by `_REFERENCES.md` REF-006), or `TBD`. No Root-owned target was needed: this carrier's applied row consumes none of the OI-008 Root semantics (login home, `proposal.*` events, delegation-policy field).
- **F3 (permitted effect):** NONE. New rows derive only from SOW-081 (L251), SOW-084 (L254), the applied row L329 prose, the `ScopeOfWork.md` Gate-5 Current Contract, and the owner-adopted seated `Remaining` item. No edge was inferred from SCC ordering, schedule, or "keep aligned" statements; the `NOT_SELECTABLE_UNTIL` gate is recorded as `SatisfactionStatus=PENDING` on interface rows, not as a schedule edge.
- **NEEDS_HUMAN_GRAPH_DECISION:**
  - `DEP-04-04-004` (DEL-04-02 resolved mode/tool-surface interface, RETIRED by RUL-SCC-001-TRANCHE-001). The relation is restated in live bytes (`ScopeOfWork.md` CLM-017 "Use resolved mode and permitted tool-surface inputs supplied by the runtime/options layer"; CLM-025 "accept that resolved surface rather than reconstruct it"), so brief rule 4 (re-evidence when still stated) collides with the standing ruling. Reactivation would recreate the DEL-04-02 <-> DEL-04-04 bidirectional pair against ACTIVE `DEP-04-02-007` (a new two-node SCC). Proposed default: keep RETIRED byte-identical (as done). Options per `docs/CYCLE_DRIVEN_RESOLUTION.md`: keep cut (default) / re-evidence and reactivate (creates a pair; owner-gated) / invert by retiring `DEP-04-02-007` instead (owner-gated; outside this carrier).
- **FENCE_F1_CANDIDATES:** none.
- **FENCE_F2_CANDIDATES:** none.

## 4. Validator outputs (verbatim)

`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-04-04/POSTIMAGE_Dependencies.csv`

```
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-04-04/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 14
```

`python3 tools/validation/validate_enum.py <ENUM> <value>` over every distinct emitted value (27 checks, 0 failures):

```
DEPENDENCY_CLASS ANCHOR: VALID: ANCHOR is a valid DEPENDENCY_CLASS (exit 0)
DEPENDENCY_CLASS EXECUTION: VALID: EXECUTION is a valid DEPENDENCY_CLASS (exit 0)
ANCHOR_TYPE IMPLEMENTS_NODE: VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE (exit 0)
ANCHOR_TYPE NOT_APPLICABLE: VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE (exit 0)
ANCHOR_TYPE TRACES_TO_REQUIREMENT: VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE (exit 0)
DIRECTION DOWNSTREAM: VALID: DOWNSTREAM is a valid DIRECTION (exit 0)
DIRECTION UPSTREAM: VALID: UPSTREAM is a valid DIRECTION (exit 0)
DEPENDENCY_TYPE CONSTRAINT: VALID: CONSTRAINT is a valid DEPENDENCY_TYPE (exit 0)
DEPENDENCY_TYPE HANDOVER: VALID: HANDOVER is a valid DEPENDENCY_TYPE (exit 0)
DEPENDENCY_TYPE INTERFACE: VALID: INTERFACE is a valid DEPENDENCY_TYPE (exit 0)
DEPENDENCY_TYPE OTHER: VALID: OTHER is a valid DEPENDENCY_TYPE (exit 0)
DEPENDENCY_TYPE PREREQUISITE: VALID: PREREQUISITE is a valid DEPENDENCY_TYPE (exit 0)
TARGET_TYPE DELIVERABLE: VALID: DELIVERABLE is a valid TARGET_TYPE (exit 0)
TARGET_TYPE DOCUMENT: VALID: DOCUMENT is a valid TARGET_TYPE (exit 0)
TARGET_TYPE PACKAGE: VALID: PACKAGE is a valid TARGET_TYPE (exit 0)
TARGET_TYPE REQUIREMENT: VALID: REQUIREMENT is a valid TARGET_TYPE (exit 0)
TARGET_TYPE UNKNOWN: VALID: UNKNOWN is a valid TARGET_TYPE (exit 0)
EXPLICITNESS EXPLICIT: VALID: EXPLICIT is a valid EXPLICITNESS (exit 0)
CONFIDENCE HIGH: VALID: HIGH is a valid CONFIDENCE (exit 0)
CONFIDENCE MEDIUM: VALID: MEDIUM is a valid CONFIDENCE (exit 0)
ORIGIN EXTRACTED: VALID: EXTRACTED is a valid ORIGIN (exit 0)
STATUS ACTIVE: VALID: ACTIVE is a valid STATUS (exit 0)
STATUS RETIRED: VALID: RETIRED is a valid STATUS (exit 0)
SATISFACTION_STATUS NOT_APPLICABLE: VALID: NOT_APPLICABLE is a valid SATISFACTION_STATUS (exit 0)
SATISFACTION_STATUS PENDING: VALID: PENDING is a valid SATISFACTION_STATUS (exit 0)
SATISFACTION_STATUS SATISFIED: VALID: SATISFIED is a valid SATISFACTION_STATUS (exit 0)
SATISFACTION_STATUS TBD: VALID: TBD is a valid SATISFACTION_STATUS (exit 0)
```

`zsh tools/validation/validate_id_format.sh <TYPE> <value>` (generic profile; known `PROJECT_ID_FORMAT_PROFILE` warning, no ID changed):

```
INVALID: DEL-04-04 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-04 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-04-04-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-04-04-014 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-017 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-081 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-084 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-004 matches OBJ format
VALID: OBJ-007 matches OBJ format
INVALID: DEL-07-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEL-07-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEL-08-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEL-08-02 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-07 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: PKG-08 does not match PKG format (^PKG-[0-9]{3}$)
```

Anchor and integrity checks (scripted over the post-image CSV): exactly one ACTIVE `IMPLEMENTS_NODE` (PASS; no FLOATING_NODE / AMBIGUOUS_ANCHOR); 14 unique `DependencyID`s (PASS); `FromDeliverableID=DEL-04-04` on all 14 rows (PASS); every ACTIVE row has `EvidenceFile` and `SourceRef` (PASS); every `SourceRef` heading/ID and every `EvidenceQuote` resolves to live bytes in `ScopeOfWork.md`, `_CONTEXT.md`, or `_STATUS.md` (grep-verified PASS); decomposition line anchors L251, L254, L265, L268, L357, L359, L484, L487 verified against the pinned file (PASS); `_DEPENDENCIES.md` count tables reconciled to the CSV (PASS); `Status=CANDIDATE` absent (PASS); row 004 byte-identical to the pre-image (PASS); both post-images LF, no trailing whitespace, final newline (PASS); `git status` shows only the untracked run folder (PASS: no carrier or other repository byte changed).

## 5. Epistemic notes

- DEP-04-04-005 — FACT: PC-REQ-001 and CLM-017 restate the prerequisite. ASSUMPTION (bounded): extending the Statement to "including the client-owned organisation layer and its pins" relies on SOW-084 L254/L487 assigning packaging and pin checks to DEL-08-01; the carrier's own `_STATUS.md` `Depends` line does not name DEL-08-01. `SatisfactionStatus` left TBD rather than PENDING because no local gate names DEL-08-01.
- DEP-04-04-006 — FACT: PC-REQ-005 and CLM-025 restate the interface; CLM-007 records UPD-122 accepted delegation to the shell persona resolver. Confidence kept MEDIUM because the resolver interface is still unnamed in local sources.
- DEP-04-04-007 — FACT: `_REFERENCES.md` REF-006 expected and actual SHA-256 are equal (MATCH). PROPOSAL: `SatisfactionStatus=SATISFIED`; the alternative is RETIRED (constraint no longer operative). CLM-004 still carries contradictory residue ("has MATCH ... require confirmation"), which is why the row is kept ACTIVE as a document dependency rather than retired.
- DEP-04-04-008 — FACT: CLM-018 step 8 and CLM-020 restate the handoff. Cross-register observation (for RECONCILIATION only; not used as evidence): DEL-04-02 `DEP-04-02-007` self-declares consumption of PersonaComposer output. Target remains UNKNOWN because no local source names it.
- DEP-04-04-009 / -010 — FACT: both scope refs are on the applied row L329 and in the front matter. CONFLICT (non-blocking, surfaced): `_CONTEXT.md#Traceability` still lists only SOW-017, SOW-030; the applied row controls.
- DEP-04-04-011 / -012 — FACT: objectives explicit in front matter and L14; `TargetType=UNKNOWN` per the brief's stated convention (other App carriers use REQUIREMENT for the same purpose; the brief's instruction was followed).
- DEP-04-04-013 — FACT: the seated `Depends` line and SOW-081 ownership notes name the relation; typed INTERFACE (the seam consumes a named file contract) rather than PREREQUISITE; the landed/selected gates are expressed as PENDING satisfaction, not as edges.
- DEP-04-04-014 — FACT: seated `Depends` line, SOW-084 notes, and acceptance obligation 1. K-PATH-2 containment of the roadmap source file is recorded in Notes, not as a separate edge, because path containment is already DEL-07-01's ownership under this same row.
- Not emitted — DEL-02-02 (Workflows view: no stated transfer to the composer beyond view ownership; PROPOSAL for RECONCILIATION if a later source names which followed workflow the composer receives and from where); DEL-03-02 and other SCC-001 members (no stated transfer); Root `EXTERNAL` rows (none consumed by this carrier).
- Environment — ASSUMPTION: `CHIRALITY_INSTRUCTION_ROOT` was unset in the dispatch shell; `INSTRUCTION_ROOT` resolved to `REPO_ROOT` per `docs/TYPES.md` and the brief's repo-root-relative instruction paths. Scratchpad note: a concurrent sibling instance overwrote the shared scratch filename `gen_postimage.py`; this instance regenerated from a uniquely named script; no repository byte outside this instance folder was touched.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
