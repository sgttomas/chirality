# PREVIEW — N1-TASK-DEL-07-01 — TASK + dependency-extract (report-only)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-07-01` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, Node N1) |
| Carrier | `DEL-07-01` Working Root Validation and Instruction Root Protection (SECURITY_CONTROL, PKG-07) |
| Basis | `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` (HEAD equals basis; branch `claude/sca-app-010-dependency-closure`) |
| Decomposition identity | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (recomputed: match); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (match); pointer `_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (match) |
| Pre-image `Dependencies.csv` | `0584937814e740879a05178547536c49ba9d03ef36bbbc0e6a83c15b4726224c` (5 data rows; match) |
| Pre-image `_DEPENDENCIES.md` | `a40fe07268822d3247b0f8790c09f91b4a60857f8ab55c71b7e2640b7af2f5c9` (match) |
| Post-image `POSTIMAGE_Dependencies.csv` | `9c8e0405599f5077d450d92e8934c0664e25b5c193bb12e90d1c11b2af6a982f` |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `b6b1fbb7436f9d1ef10fdad5af82e04c48bb9a0f5fe5db64fe4d3bb2847adac9` |
| Row census pre | total 5 / ACTIVE 4 / RETIRED 1 / ANCHOR 3 / EXECUTION 2 (satisfaction: NOT_APPLICABLE 4, SATISFIED 1) |
| Row census post | total 12 / ACTIVE 11 / RETIRED 1 / ANCHOR 7 / EXECUTION 5 (ACTIVE by class: 7 ANCHOR, 4 EXECUTION; satisfaction: NOT_APPLICABLE 8, SATISFIED 1, PENDING 3) |
| Carrier bytes | unchanged (`git status` shows only this run folder as untracked; pre-image hashes re-verified after writing) |

## 2. Row-level diff (every post-image row)

`UNCHANGED` means byte-identical to the pre-image row.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-07-01-001 | RE-EVIDENCED | ANCHOR / IMPLEMENTS_NODE | UPSTREAM / OTHER | WBS_NODE DEL-07-01 | `ScopeOfWork.md#Current responsibility; #CLM-002 — Identification; decomposition #L357` | Was `Datasheet.md#Identification` (file gone). Statement refreshed to the applied row L357 scope (adds the organisation layer); EvidenceQuote is the L357 Scope text; LastSeen 2026-09-05. ID, class, target preserved. |
| DEP-07-01-002 | REFRESHED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT SOW-002 | `_CONTEXT.md#Traceability; ScopeOfWork.md front matter; decomposition #L172; #L405` | EvidenceFile unchanged and live. TargetName/Statement refreshed to the amended SOW-002 label (L405) and ownership note (L172); EvidenceQuote corrected to the live `_CONTEXT.md` line (`SOW-002, SOW-027, SOW-075`); LastSeen 2026-09-05. |
| DEP-07-01-003 | REFRESHED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT SOW-027 | `_CONTEXT.md#Traceability; ScopeOfWork.md front matter; decomposition #L197; #L430` | EvidenceQuote corrected to the live line; SourceRef gains line pointers; LastSeen 2026-09-05; Notes record that DEL-06-04 stays a coordination note (X-002 open). |
| DEP-07-01-004 | UNCHANGED | EXECUTION / NOT_APPLICABLE | UPSTREAM / CONSTRAINT | DOCUMENT REF-006 `docs/PRD.md` | `_REFERENCES.md#Authoritative Source Corpus` | RETIRED row preserved byte-identically. |
| DEP-07-01-005 | RE-EVIDENCED | EXECUTION / NOT_APPLICABLE | UPSTREAM / PREREQUISITE | UNKNOWN (landed implementation modules) | `ScopeOfWork.md#CLM-018 — Prerequisites; #CLM-014 — Documentation; _STATUS.md#Remaining (DEL-07-01-V3-01 Write locus)` | Was `Specification.md#Documentation; Procedure.md#Prerequisites` (files gone). Relation still stated (CLM-018 prerequisite row; seated write locus names `instruction-root.ts` and path-policy helpers). TargetLocation (`frontend/...` modules) predates fence F2 and is preserved unchanged; SATISFIED retained for the landed modules. |
| DEP-07-01-006 | ADDED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT SOW-075 | `ScopeOfWork.md front matter project_scope_refs; #Purpose and Objective Traceability (D-APP-80 note); _CONTEXT.md#Traceability; decomposition #L245; #L478` | On the applied row L357 and in `_CONTEXT.md` since D-APP-80 (2026-07-28) but never extracted. NOT_APPLICABLE (anchor). |
| DEP-07-01-007 | ADDED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | REQUIREMENT SOW-084 | `ScopeOfWork.md front matter; #Current acceptance obligations; decomposition #L254; #L487; _STATUS.md#Remaining` | Introduced by SCA-APP-010 (DEC-025). NOT_APPLICABLE (anchor); the work is seated as DEL-07-01-V3-01. |
| DEP-07-01-008 | ADDED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | UNKNOWN OBJ-006 | `ScopeOfWork.md front matter package_objective_refs; #Purpose and Objective Traceability; _CONTEXT.md#Traceability; decomposition #L267; #L357` | `TargetType=UNKNOWN` per the brief's objective-anchor convention; raw reference in TargetRefID/TargetName. |
| DEP-07-01-009 | ADDED | ANCHOR / TRACES_TO_REQUIREMENT | UPSTREAM / OTHER | UNKNOWN OBJ-008 | as DEP-07-01-008 with `decomposition #L269` | Same convention. |
| DEP-07-01-010 | ADDED | EXECUTION / NOT_APPLICABLE | DOWNSTREAM / INTERFACE | DELIVERABLE DEL-04-04 (PKG-04) PersonaComposer from Instruction Root | `_STATUS.md#Remaining (DEL-07-01-V3-01 Depends and Return); decomposition #L487; #L329; ScopeOfWork.md#Current acceptance obligations` | "DEL-04-04-V3-01 consumes the pins"; L487 "DEL-04-04 composes from both layers". EXPLICIT, HIGH, PENDING. Not an SCC-001 endpoint. |
| DEP-07-01-011 | ADDED | EXECUTION / NOT_APPLICABLE | DOWNSTREAM / INTERFACE | DELIVERABLE DEL-02-03 (PKG-02) Working Root File Tree and Scope Scan UI | `decomposition #L172; #L405; #L309; ScopeOfWork.md#CLM-003 — Attributes (Validation endpoint)` | L172 "DEL-07-01 retains validation ownership"; L405 "DEL-02-03 provides the UI touchpoint"; L309 "UI consumes workspace APIs"; CLM-003 names `/api/working-root/validate`. EXPLICIT, **MEDIUM**, PENDING. Not an SCC-001 endpoint. |
| DEP-07-01-012 | ADDED | EXECUTION / NOT_APPLICABLE | UPSTREAM / CONSTRAINT | DOCUMENT REF-002 `docs/CONTRACT.md` K-ROOT-1 | `ScopeOfWork.md#Current acceptance obligations; decomposition #L254; _REFERENCES.md#Authoritative Source Corpus (REF-002 MATCH)` | L254 "K-ROOT-1 applies to both layers". REF-002's pinned hash resolves to `projects/chirality-app-dev/docs/CONTRACT.md` (K-ROOT-1 at L42); TargetLocation uses the register's project-relative REF convention (as DEP-07-01-004). EXPLICIT, HIGH, PENDING. |

No row was deleted; no `Status=CANDIDATE`; no `Origin=DECLARED` row existed to preserve; every `DependencyID` preserved; new IDs continue the sequence.

## 3. Fence results

- **F1 (SCC-001 membership):** `NONE`. DEL-07-01 is not an SCC-001 member (`Evidence/baseline_closure/scc_summary.csv`: DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05). The only new deliverable targets are DEL-04-04 and DEL-02-03, neither an SCC-001 member, so no reverse-edge condition can make this carrier a member. No other register was read for this fence because no candidate targeted an SCC-001 member.
- **F2 (Root path):** `NONE`. `TargetLocation` values in the post-image: the project-relative decomposition path (anchors), two project-relative deliverable folders (DEP-07-01-010, -011), `docs/CONTRACT.md` and `docs/PRD.md` as pinned by `_REFERENCES.md` (DEP-07-01-012, -004), and the pre-existing `frontend/...` module list on DEP-07-01-005 (preserved unchanged; repository frontend paths, not a Root project path). No Root-owned semantic applies to this carrier (OI-008 names SOW-010/081/082/083, none on L357), so no `EXTERNAL`/`TBD` row was required.
- **F3 (permitted effect):** `NONE`. Every new row traces to the applied row L357, the amended SOW-002 row L172, the amended SOW-084 row L254 (and their reverse-view lines), or the seated `## Remaining` item; no edge was inferred from SCC ordering, schedule, or "keep aligned" statements. Retirement was not needed (no stale relation).
- **NEEDS_HUMAN_GRAPH_DECISION:** `none`.
- **FENCE_F1_CANDIDATES:** `none`.
- **FENCE_F2_CANDIDATES:** `none`.

### Considered and not emitted (reported, not suppressed)

| Candidate | Evidence that was weighed | Why not emitted |
|---|---|---|
| DEL-08-01 (packaging and conformance checks over the organisation layer) | L487 "DEL-08-01 owns packaging and conformance checks"; `_STATUS.md#Remaining` "DEL-08-01-V3-01 owns the packaging checks"; L254 "packaging-checked"; DEL-08-01 row L368 "organisation-layer packaging and pins" | Ownership split only. The live sources do not state that DEL-07-01 supplies to or consumes from DEL-08-01 a named artifact, contract, tool, event, or policy; both read the client-owned pin file, whose contract owner is unstated. Under the brief's rule this is coordination, not an edge. The owner may seat a pin-contract owner and add the edge later; DEL-08-01's own register may carry its side if its sources state it. |
| DEL-06-04 (SOW-027 shared) | `ScopeOfWork.md` CLM-026 and CLM-030 X-002 | Explicitly "a coordination note, not an accepted dependency edge" pending human ruling X-002 (unchanged posture since 2026-05-20). |
| `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` | `_STATUS.md#Remaining` Plan line | Cited "only for what the tranche means when complete, never as a queue"; not a required input; not a `_REFERENCES.md`-pinned file (would also fail F2 as a TargetLocation). |
| `frontend/electron/daemon-instruction-root.ts` (D-APP-98) | `_STATUS.md#Remaining` Write locus | A conditional write locus of this carrier's own work, not a dependency. |
| Known-folder set (SOW-008, DEL-02-04) | L172 "app-scoped set of known folders" | No transfer to or from DEL-07-01 is stated on the amended rows; DEL-02-04 is not named on SOW-002. |

## 4. Validator outputs (verbatim)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py <POSTIMAGE_Dependencies.csv>`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-07-01/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 12
exit=0
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct value in every enum column of the post-image):

```text
DEPENDENCY_CLASS ANCHOR, EXECUTION: VALID
ANCHOR_TYPE IMPLEMENTS_NODE, NOT_APPLICABLE, TRACES_TO_REQUIREMENT: VALID
DIRECTION DOWNSTREAM, UPSTREAM: VALID
DEPENDENCY_TYPE CONSTRAINT, INTERFACE, OTHER, PREREQUISITE: VALID
TARGET_TYPE DELIVERABLE, DOCUMENT, REQUIREMENT, UNKNOWN, WBS_NODE: VALID
EXPLICITNESS EXPLICIT: VALID
CONFIDENCE HIGH, MEDIUM: VALID
ORIGIN EXTRACTED: VALID
STATUS ACTIVE, RETIRED: VALID
SATISFACTION_STATUS NOT_APPLICABLE, PENDING, SATISFIED: VALID
ENUM SUMMARY: 25 checks, 0 invalid
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; known `PROJECT_ID_FORMAT_PROFILE` warning, no ID changed):

```text
INVALID: DEL-07-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-07 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-07-01-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-07-01-012 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-002 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-075 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-084 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-006 matches OBJ format
VALID: OBJ-008 matches OBJ format
INVALID: DEL-04-04 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEL-02-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
```

Anchor and row checks (scripted over the post-image):

```text
unique DependencyIDs: True 12
FromDeliverableID all DEL-07-01: True
FromPackageID all PKG-07: True
RegisterSchemaVersion all v3.1: True
Status=CANDIDATE present: False
ACTIVE IMPLEMENTS_NODE count: 1
ACTIVE rows with EvidenceFile+SourceRef: True of 11
EvidenceQuote max words: 28
```

Evidence resolution: every cited `ScopeOfWork.md` heading (`Current responsibility`, `Current acceptance obligations`, `Purpose and Objective Traceability`, `CLM-002`, `CLM-003`, `CLM-014`, `CLM-018`), front-matter key, `_CONTEXT.md#Traceability` line, `_STATUS.md#Remaining` phrase, `_REFERENCES.md` heading, and decomposition line (`L172, L197, L245, L254, L267, L269, L309, L329, L357, L405, L430, L478, L487, L634`) was grepped and found exactly once at the stated location. `_DEPENDENCIES.md` post-image counts (12 / 11 / 1 / 7 / 5; NOT_APPLICABLE 8, SATISFIED 1, PENDING 3) equal the CSV census. Pre-image CSV round-trips byte-identically through the same writer settings used for the post-image (quoting convention preserved). Line hygiene: LF only, no trailing whitespace, final newline on every written file.

## 5. Epistemic notes

- DEP-07-01-001 — FACT: applied row L357 and `ScopeOfWork.md#Current responsibility` state the definition verbatim. The Statement refresh is a restatement, not a new claim.
- DEP-07-01-002 / -003 — FACT: `_CONTEXT.md#Traceability` still lists both; the only substantive change is the amended SOW-002 text. The pre-image EvidenceQuote (`SOW-002, SOW-027`) no longer matched live bytes and was corrected.
- DEP-07-01-005 — FACT: the prerequisite relation is still stated (CLM-018 row "Code module locations for implementation"; seated write locus). ASSUMPTION (pre-existing, preserved): the module list in TargetLocation came from UPD-130 and was not re-verified against `frontend/` by this run (out of read scope). Observation for the owner: those `frontend/...` locations are repository paths outside `projects/chirality-app-dev/**` and not `_REFERENCES.md`-pinned; they predate F2 and were preserved rather than rewritten.
- DEP-07-01-006 — FACT that SOW-075 is on L357/`_CONTEXT.md`; FACT that it predates SCA-APP-010 (D-APP-80). `FirstSeen=2026-09-05` records first extraction, not first assignment.
- DEP-07-01-007 — FACT (DEC-025, L254, L487, seated item).
- DEP-07-01-008 / -009 — FACT for the objective references. Convention note: the brief prescribes `TargetType=UNKNOWN` for objective anchors; the DEL-08-04 precedent register used `REQUIREMENT` for its objective rows. The brief was followed; the reviewer may normalize either way without changing evidence.
- DEP-07-01-010 — FACT for the consumption statement ("DEL-04-04-V3-01 consumes the pins"; "DEL-04-04 composes from both layers"). PROPOSAL: the pin-file format (SHA-256 per asset) is described only in the seated Return contract; the concrete schema is not yet in a governed source.
- DEP-07-01-011 — FACT for ownership (L172), UI touchpoint (L405), and UI consumption of workspace APIs (L309); FACT that CLM-003 names `/api/working-root/validate` from `docs/SPEC.md`. ASSUMPTION: the transferred artifact is the validation result over that endpoint (REQ-07-01-011's downstream-reuse claim is itself labelled ASSUMPTION), hence `Confidence=MEDIUM`. This is the one emitted row a reviewer could reasonably downgrade to coordination; it is emitted because the brief authorizes the revised SOW-002 relation and the sources name a consumed policy/API rather than mere alignment.
- DEP-07-01-012 — FACT (L254; `ScopeOfWork.md#Current acceptance obligations` item 1). REF-002 target resolved by hash, not by name: the repository-root `docs/CONTRACT.md` does not contain K-ROOT-1 and has a different hash; the pinned hash matches `projects/chirality-app-dev/docs/CONTRACT.md`.
- Normalization: `CHIRALITY_INSTRUCTION_ROOT` was unset in the runtime; `INSTRUCTION_ROOT` was taken as the repository root because the sealed brief names the instruction files there (ASSUMPTION-labelled in the run record; same posture as the precedent run's additive declaration). No scope, write target, or acceptance term changed.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
