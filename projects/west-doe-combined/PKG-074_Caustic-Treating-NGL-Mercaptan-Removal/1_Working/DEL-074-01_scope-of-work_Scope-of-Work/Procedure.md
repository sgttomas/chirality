# Procedure — DEL-074-01 Scope of Work (PKG-074 Caustic Treating, NGL Mercaptan Removal)

> Operational procedure for **producing and maintaining** the PKG-074 EPC Scope of Work deliverable. (This is not a unit-operating procedure; operation of the caustic treating package is the Package Vendor's scope under DEL-074-04.)

## Purpose

Produce a source-anchored, internally consistent PKG-074 Scope of Work that fixes package identity, function, equipment scope, building/materials/safety constraints, interfaces, responsibility split, and open items. The output is fit-for-issue to the Package Vendor for engineering (DEL-074-04) and to downstream PKG-074 deliverables (DEL-074-02, -03, -05, -06). (`_CONTEXT.md`; DELIVERABLE_REGISTER.csv)

## Prerequisites

### Required inputs (must be present and accessible)

- `_CONTEXT.md` (deliverable identity, scope, package mapping). Present.
- `_REFERENCES.md` (decomposition snapshot pointers and source basis). Present.
- `_DEPENDENCIES.md` (declared upstream/downstream). Present; no declared dependencies (PREPARATION default).
- Accepted decomposition snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv). Present.
- 04-25 Deepcut DBM at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. Present; SEC-07 "Current-Scope NGL Mercaptan Treating" is the authoritative process slice for this deliverable.
- `26020-Package_Requirements.docx` package heading 28. Present as `.docx` only; clause-level extracted slice is **not** locally available — open item CFT-003 carries this.

### Declared upstream dependencies

- None declared during PREPARATION (`_DEPENDENCIES.md`). The Scope of Work is the upstream anchor for the other five PKG-074 deliverables.

### Required references (per Authority Hierarchy)

- DELIVERABLE_REGISTER.csv (PKG-074 rows) — authority for package identity, deliverable set, supported objectives, scope items.
- SCOPE_LEDGER.csv (SOW-0059 through SOW-0062) — authority for package definition, basic scope, major equipment list, and open items.
- OBJECTIVE_REGISTER.csv (OBJ-001, -003, -004, -005, -006, -007, -008, -009, -010) — authority for cross-cutting facility outcomes.
- 4-25_Deepcut_DBM.md SEC-07 — authority for current-scope process basis, design parameters, equipment, building, and interfaces.

## Steps

1. **Confirm scope and identity.** Read `_CONTEXT.md` and DELIVERABLE_REGISTER.csv; confirm DeliverableID, parent package, discipline, type, responsible party, supported objectives, covered scope items, and source basis match. Record any mismatch as `CONFLICT:` and stop. *Verification:* identity fields in `Datasheet.md` Identification table match `_CONTEXT.md` and the register.
2. **Extract the SOW-level requirements from the SCOPE_LEDGER.** For each of SOW-0059, SOW-0060, SOW-0061, SOW-0062, identify the in-scope statements, equipment categories, and open items. Map each to one or more REQ-074-01-* requirements in `Specification.md`. *Verification:* every SOW-0059..62 statement is reflected in at least one REQ.
3. **Anchor the process basis to the 04-25 DBM SEC-07.** Extract design rate, inlet/outlet pressure, inlet temperature low/design/high, fresh and circulating caustic concentration, tank quantities, downstream service, and incinerator routing. Populate `Datasheet.md` Attributes/Conditions/Construction and `Specification.md` REQ-074-01-010..014, -022..023, -040. Mark `TBC` / `TBD` exactly as the source does. *Verification:* every quantitative value in `Datasheet.md` cites a source row or the source section.
4. **Capture building, materials, and safety constraints.** From DBM SEC-07 "NGL Mercaptan Treating Equipment and Utilities", populate REQ-074-01-030..032 (indoor installation, no aluminum, stainless steel cladding/straps, safety showers, control-room alert). *Verification:* `Specification.md` and `Guidance.md` agree on material prohibitions.
5. **State the responsibility split.** Apply OBJ-004 to write REQ-074-01-050..051 (Package Vendor vs. EPC Integrator scope; third-party proprietary process provider role). *Verification:* responsibility wording matches OBJ-004 and the DEL-074-04/-05/-06 register entries.
6. **Flow down cross-cutting facility requirements.** Reference OBJ-005..010 (electrical, controls/instrumentation, utilities, civil/structural, safety/regulatory, operability/handoff) in REQ-074-01-060..061 without re-deriving facility-wide standards. Mark code lists `TBD` where DBM SEC-15 slice is not locally extracted. *Verification:* `Specification.md` Standards section is honest about what is and is not locally available.
7. **Surface open items and conflicts.** Record the regenerative-vs.-non-regenerative process basis conflict (CFT-001) and the SOW-0061 "caustic regeneration equipment" line vs. DBM SEC-07 "no on-site regen column" conflict (CFT-002), the heading 28 tagged-item reconciliation (CFT-003), and the shared incinerator responsibility (CFT-004) in `Guidance.md` Conflict Table. *Verification:* each conflict cites both sources and proposes an authority pending human ruling.
8. **Cross-document consistency sweep.** Confirm terminology (e.g., "Caustic Treating (NGL Mercaptan Removal)", "PKG-074", "DEL-074-01_scope-of-work"), tag identifiers (V-6940-1), units (m3/d, bbl/d, kPag, deg C, wppm S), and numeric values (2,385 m3/d / 15,000 bbl/d; 2,213/1,978 kPag; 26.7/43.3/48.8 deg C; 50 wt% / 14.7 wt% NaOH; 970/4,166 ppmw S; 175 wppm S sales spec; 400 bbl tank size) are identical across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. *Verification:* no value disagreement between documents; any disagreement returns to Step 3.
9. **Mark all unsupported claims `TBD` or `ASSUMPTION`.** Re-scan all four documents for claims that lack a source citation. Convert to `TBD` (unknown) or `ASSUMPTION` (inferred), per the deliverable's "no invention" rule. *Verification:* every non-trivial value or requirement has a `SourcePath` and section reference or is explicitly `TBD` / `ASSUMPTION` / `location TBD`.
10. **Update `_STATUS.md` (safe update only).** If current state is `OPEN`, advance to `INITIALIZED` using `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If current state is not `OPEN`, do not modify. *Verification:* `_STATUS.md` reflects the new state and history line.
11. **Write the run record.** Persist a TASK run record under `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing input echo, resolved skill/profile, tools used, outputs produced, missing items, conflicts, and applied changes. *Verification:* run record exists, has YAML frontmatter, and lists all four production documents plus the status update.

## Verification

| Check | What to confirm | Pass criterion |
|---|---|---|
| Four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist in `{DELIVERABLE_PATH}` | All four files present |
| Default schema sections present | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records) | All default headings present |
| Source grounding | Each quantitative or normative claim cites a SourcePath + section, or is `TBD` / `ASSUMPTION` / `location TBD` | No uncited substantive claims |
| Cross-document consistency | Terminology, tag IDs, numeric values, and unit conventions identical across all four documents | No disagreement |
| Conflict capture | CFT-001..004 present in `Guidance.md` Conflict Table with both sources and proposed authority | Table present and complete |
| Status discipline | `_STATUS.md` advanced only OPEN → INITIALIZED; never regressed | History reflects safe update |
| Run record | `_run_records/TASK_RUN_*.md` present and structurally complete | File exists with YAML and all required headings |

## Records

The following records constitute the deliverable's evidence trail:

- `Datasheet.md` — descriptive datasheet (this run)
- `Specification.md` — normative scope-of-work requirements (this run)
- `Guidance.md` — directional guidance and Conflict Table (this run)
- `Procedure.md` — this procedure (this run)
- `_STATUS.md` — lifecycle state (safe update OPEN → INITIALIZED)
- `_run_records/TASK_RUN_<timestamp>.md` — run record for this invocation
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` — read-only metadata; not modified by this skill

Downstream PKG-074 evidence will be created under DEL-074-02 through DEL-074-06 (not produced by this run).
