# Procedure — Producing the Package Datasheet for Storage Bullets (PKG-059)

> Operational steps for the EPC Integrator (or delegated TASK) to produce, review, and turn over the `DEL-059-02_package-datasheet` deliverable. Interpretation per skill convention: this procedure addresses how to **produce** the datasheet artifact. Steps for vendor *use* of the package are out of scope (covered by `DEL-059-04`, `DEL-059-05`, and `DEL-059-06`).

## Purpose

Produce a source-grounded EPC Package Datasheet for PKG-059 that satisfies the requirements in `Specification.md`, captures the design basis from the SCOPE_LEDGER package heading 14 extract and the Deepcut DBM API 2510 spacing table, and surfaces interface facts and open items for downstream vendor engineering against RFQ `26020-01-PT-RFQ-17-007`.

## Prerequisites

### Inputs / references

- `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (placeholder) for this deliverable.
- GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `DELIVERABLE_REGISTER.csv` (DEL-059-02 row)
  - `PACKAGE_REGISTER.csv` (PKG-059 row)
  - `SCOPE_LEDGER.csv` (SOW-0181..SOW-0184)
  - `INTERFACE_REGISTER.csv` (ten PKG-059 rows)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM-Deepcut source file at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, especially:
  - Sec. Pressurized Bullet Spacing (lines 245-259)
  - Sec. Atmospheric Tank and General Plant Spacing (lines 261-268)
  - Sec. Flare and Fired-Heater Spacing (lines 284, 299)
  - Sec. Storage and Disposition tables (lines 448, 492)
  - Sec. NGL Storage Bullets (lines 1627-1629)
- DBM-Comp_and_Liquids source file at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (context only; condensate/LPG disposition narrative).
- Native source files (to be parsed in a follow-up pass): `26020-Package_Requirements.docx` (package heading 14), `26020-Packages_Interfaces_4_export.xlsx`, RFQ `26020-01-PT-RFQ-17-007`.

### Declared dependencies

- Per `_DEPENDENCIES.md`: no upstream or downstream dependencies declared during PREPARATION. Coordination mode is DECLARED. Treat extracted info-flow summaries as context only.

### State precondition

- `_STATUS.md` must be in `OPEN` or `INITIALIZED` (within `ALLOW_OVERWRITE_STATES`) for the four-document kit to be overwritten by the four-documents skill.

## Steps

1. **Read deliverable-local context.** Open `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, and `_SEMANTIC.md`. Extract identity (PKG-059, DEL-059-02), discipline (Mechanical), responsible party (EPC Integrator), scope items (`SOW-0181`..`SOW-0184`), and supported objectives.
2. **Locate the decomposition rows.** In GATE-07:
   - `DELIVERABLE_REGISTER.csv` — confirm DEL-059-02 row (anticipated artifacts, source basis, interface-evidence note).
   - `PACKAGE_REGISTER.csv` — capture responsibility split, applicable interface types, and RFQ source basis (`26020-01-PT-RFQ-17-007`).
   - `SCOPE_LEDGER.csv` — capture SOW-0182, SOW-0183, SOW-0184 verbatim (these are the source-text extractions of `26020-Package_Requirements.docx` package heading 14).
   - `INTERFACE_REGISTER.csv` — list all ten PKG-059 interface rows.
3. **Open accessible source slices.**
   - DBM-Deepcut Sec. Pressurized Bullet Spacing (lines 245-259) for API 2510 spacing constraints.
   - DBM-Deepcut Sec. Atmospheric Tank and General Plant Spacing (lines 261-268) for adjacent atmospheric-tank and containment spacing.
   - DBM-Deepcut Sec. Flare/Fired-Heater Spacing (lines 284, 299) for distances to flare and fired heaters.
   - DBM-Deepcut Sec. NGL Storage Bullets and storage-disposition tables (lines 448, 492, 1627-1629) for the project-level storage basis and the NGL-vs-LPG framing.
4. **Identify Conflicts.**
   - CONF-01: SCOPE_LEDGER "sixteen LPG product storage bullets ... C3, C4, C3/C4 LPG mix from the depropanizer" vs DBM-Deepcut "16 x 120,000 USG NGL storage bullets" with retired depropanizer.
   - CONF-02: Facility-of-record not named in PACKAGE_REGISTER; DBM places 16 x 120,000 USG bullets at 04-25.
   - CONF-03: Production-rate / storage-duration basis (15,400 bbl/d, 2.5 days) present in DBM but absent from SCOPE_LEDGER.
   - Record all three in `Guidance.md` Conflict Table.
5. **Draft `Datasheet.md`** using the default schema (Identification, Attributes, Conditions, Construction, References). Plus add an Interface Requirements Matrix section (per `_CONTEXT.md` Notes mandating that interface facts live inside this deliverable).
   - Identification: populate from `_CONTEXT.md` and PACKAGE_REGISTER, plus facility-of-record ASSUMPTION pointing to CONF-02.
   - Attributes / Conditions: cite SCOPE_LEDGER SOW-0182..SOW-0184 character-for-character for counts, dimensions, volume, fill, design P/T, full vacuum, mounting, access, service, "by others" exclusions, vapour-equalization and butane-blanket constraints.
   - Conditions (spacing): cite DBM-Deepcut lines 245-259, 265-267, 284, 299 for API 2510 spacing values.
   - Construction: capture mounting, access, "by others" exclusions; mark MOC, MAWP, internals, nozzle schedule, etc. as TBD.
   - Interface Requirements Matrix: list all ten INTERFACE_REGISTER rows for PKG-059 with PROPOSAL EPC/Vendor split text.
   - References: GATE-07 registers, DBM-Deepcut sections, native .docx/.xlsx and RFQ as `location TBD`.
   - Open Items / TBD: list source-not-available items.
6. **Draft `Specification.md`** with normative requirements REQ-DS-01..REQ-DS-16 traceable to SCOPE_LEDGER, PACKAGE_REGISTER, INTERFACE_REGISTER, DBM-Deepcut, and `_CONTEXT.md`. Populate Standards (API 2510 from DBM; ASME BPVC Sec. VIII Div. 1 as ASSUMPTION; BC PV registration as ASSUMPTION; NFPA 30 context; OGAOM and BCER context; native .docx/.xlsx and RFQ as `location TBD`). Define Verification and Documentation accordingly.
7. **Draft `Guidance.md`** with Purpose, Principles, Considerations, Trade-offs, Examples, and Conflict Table (CONF-01, CONF-02, CONF-03).
8. **Draft this `Procedure.md`** (covering production of the datasheet artifact and its review/turnover steps).
9. **Run Pass 2 cross-reference consistency checks** as specified in `skills/four-documents/SKILL.md` Step 5:
   - **Datasheet ↔ Specification:** count of bullets (2 + 16 = 18), bullet ID (3658 mm), S/S length (42494 mm), volume (454 m3 / 120,000 USG), fill (84%), design pressure (1724 kPag), design temperature (66 C), full vacuum, mounting (outdoor, saddle), access (stairs/platforms), service descriptions, "by others" exclusions, spacing constants (15.24 m, 38.1 m, 30.48 m, 3.05 m, 2.804 m, 6 per cluster), and the ten interface IDs are consistent across the two documents.
   - **Specification ↔ Guidance:** every REQ has rationale in Principles or Considerations (REQ-DS-04..REQ-DS-09 → SCOPE_LEDGER faithful citation; REQ-DS-10 → spacing-is-hard-input principle; REQ-DS-11 → interfaces-as-evidence principle; REQ-DS-12/13 → mark-don't-invent principle; REQ-DS-16 → surface-don't-reconcile principle).
   - **Specification ↔ Procedure:** every REQ has a verification hook (datasheet-review cross-checks listed in Step 5/6 of this procedure).
   - **Terminology:** "Storage Bullets", "unstable condensate storage bullets", "LPG product storage bullets", "PKG-059", "DEL-059-02", "API 2510", "26020-Package_Requirements.docx package heading 14", "SCOPE_LEDGER", "DBM-Deepcut" used consistently across all four documents.
   - **Values:** the numeric set above is quoted identically across documents.
10. **Update `_STATUS.md`** from `OPEN` to `INITIALIZED` using `tools/scaffolding/write_status.sh` (or equivalent safe write) with the `TASK+four-documents` reason token, only if current state is `OPEN`.
11. **Write the run record** at `_run_records/TASK_RUN_<timestamp>.md` with full input echo, resolved state, tools used, outputs produced, missing items, and TBD/conflict surfacing.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents exist | Directory listing | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present |
| Default schema sections present | Heading scan in each doc | All default sections from the skill schema table present |
| At least one accessible source was read | Citations in `Datasheet.md` / `Specification.md` | SCOPE_LEDGER and DBM-Deepcut line citations present |
| Non-trivial values are cited or marked TBD/ASSUMPTION | Manual review | No bare numeric values without a source or label |
| Cross-document consistency | Manual sweep using Step 9 checklist | All checks pass; otherwise Conflict Table entry exists |
| Interface coverage | Compare Datasheet matrix against INTERFACE_REGISTER | All ten PKG-059 interface rows represented |
| `_STATUS.md` lifecycle | Read updated `_STATUS.md` | Current state = `INITIALIZED`; History entry appended |
| Run record written | List `_run_records/` | `TASK_RUN_<timestamp>.md` exists with run-status `SUCCESS` |
| No out-of-scope writes | Review changed paths | All writes confined to this deliverable folder |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file).
- Updated `_STATUS.md` (`OPEN` → `INITIALIZED`).
- Run record at `_run_records/TASK_RUN_<timestamp>.md`.
- Conflict Table entries (CONF-01, CONF-02, CONF-03) in `Guidance.md` awaiting human ruling.
- Open Items / TBDs surfaced in `Datasheet.md` Open Items section, to be resolved during Pass 3 semantic lensing (`RUN_PASSES: P3_ONLY` after `_SEMANTIC_LENSING.md` is produced) and during detailed design / RFQ document parsing.
