# Procedure — DEL-049-03 Construction Work Package (Sales Gas Booster Compressor)

> Operational procedure for producing the CWP deliverable bundle AND for executing CWP-governed site work for `PKG-049 Sales Gas Booster Compressor`. Source-anchored to `_Sources/26020-Package_Requirements.docx` heading 4 (`26020-01-PT-12-004`). Detailed site sequencing (durations, crew sizes, lift plans) is `TBD` until the project execution plan and vendor `MEC-017 / STR-006 / MEC-018` are received.

## Purpose

To assemble, issue, and execute the Construction Work Package for the Sales Gas Booster Compressor so that the installed package is mechanically complete, registered (as applicable), tested, and accepted for handover to commissioning, with traceable records back to `SOW-0169`–`SOW-0172`.

## Prerequisites

### Decomposition / Governance

- Accepted upstream decomposition snapshot `GATE-07_Final_Published_2026-05-24` (cited in `_REFERENCES.md`).
- `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md` for this deliverable.

### Source Materials (Accessible)

- `_Sources/26020-Package_Requirements.docx` heading 4 (SGBC slice).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`.

### Upstream Deliverables in PKG-049

- `DEL-049-01_scope-of-work` — package scope of work (ASSUMPTION: precedes CWP issue).
- `DEL-049-02_package-datasheet` — package technical datasheet (ASSUMPTION: precedes CWP issue).
- `DEL-049-04_vendor-engineered-equipment-package` — vendor package delivery (precedes site setting and tie-in).
- `DEL-049-05_vendor-document-turnover-package` — vendor document set (drives much of the CWP content).

### Required Vendor Inputs Before Site Work

- `MEC-017 Equipment Installation / Setting Drawings`
- `STR-005 Foundation Design Calculations`, `STR-006 Foundation Drawings`, `STR-013 Anchor Bolt / Embedment`
- `MEC-018 Lifting / Handling Study`, `STR-014 Lifting Lug / Transport Analysis`
- `PIP-004 Tie-In List / Tie-In Scope Sheets`, `PIP-006/007/008/009/017 Piping artifacts`
- `ELE-011 Motor Starting Study`, `ELE-016/027/028 Electrical Installation set`
- `INS-005/006/008/009/010/011 Instrumentation set`, `CTL-003/005/026 Controls set`
- `QLT-003 ITP`, `QLT-020 Inspection Release Certificate`

### Project Inputs (currently `TBD`)

- Project hydrotest / NDE specification.
- Project welding specification.
- Project mechanical completion / turnover procedure.
- Pressure equipment registration jurisdictional procedure.
- Site HSE / hot-work / confined-space / lift-plan permit procedures.

## Steps

### Phase A — Assemble the CWP Document Bundle (EPC Integrator office work)

A1. **Confirm scope demarcation.** From `_Sources/26020-Package_Requirements.docx` SGBC Scope Notes, list explicitly the "By others" items as EPC Integrator workface scope: shipping, installation on piles, tie-in piping, electrical connections, mounting platform and stairs.

A2. **Build the SOW-trace matrix.** Map every CWP work item to `SOW-0169`, `SOW-0170`, `SOW-0171`, `SOW-0172`.

A3. **Build the interface plan** from the SGBC Physical Interface Summary, instantiating one workface package per "Yes" interface (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, Area Lighting, EHT, Grounding/Bonding, I&C, F&G, Maintenance Access, Structural/Foundations/Supports).

A4. **Sequence on a CPM basis** (durations TBD). Default sequencing ASSUMPTION: Foundation → Receiving & Setting → Mechanical Alignment → Tie-In Piping → Electrical Termination → I&C Termination & Loop Checks → F&G Functional → Flushing/Drying → Hydrotest → Energization → SAT → Mechanical Completion → Turnover.

A5. **Define record templates** for each verification item in `Specification.md` `R-CWP-12` through `R-CWP-17`.

A6. **Issue the Construction work package, Installation and tie-in workface plan, and Construction interface and turnover checklist** as the three CWP artifacts named in `_CONTEXT.md`.

### Phase B — Site Execution

B1. **Receiving & QA-in.** Witness `QLT-020 Inspection Release Certificate`; perform receiving inspection against `MEC-023 Vendor Data Book` and the shipping documentation from `PRQ-013 Logistics / Shipping Plan`. Record any transit damage.

B2. **Foundation acceptance.** Drive piles per `STR-006`; survey pile cut-off elevations and anchor bolt template per `STR-013`; grout per project standard (procedure TBD); release foundation for setting.

B3. **Set package.** Execute the approved lift plan per `MEC-018` and `STR-014`; check baseplate level and elevation; torque anchor bolts to vendor spec (value TBD — confirm from vendor IOM `MEC-025`); record alignment.

B4. **Install platform and stairs** per `STR-011` (see Guidance Conflict C-2 for supply demarcation).

B5. **Tie-in piping.** Execute weld map against `PIP-008 / PIP-009`; perform NDE per project welding spec (TBD); install valves per `PIP-018`; close tie-ins per `PIP-004`.

B6. **Flush, dry, and pressure-test.** Execute `PIP-025 Flushing / Cleaning / Drying Procedure` upstream of the filter coalescer first to protect coalescer media; execute `PIP-024 Hydrotest Packages` (test pressures TBD; must envelope 12,866 kPag discharge design / 6,137 kPag suction design).

B7. **Electrical installation and energization.** Pull cable per `ELE-014/015`; terminate per `ELE-028`; perform megger/continuity and complete `ELE-030 Energization Package`. Coordinate `ELE-011 Motor Starting Study` results for soft-start parameters.

B8. **Instrumentation install and loop check.** Install instruments per `INS-005/006`; terminate per `INS-009/010/011`; run loops per `INS-008` and verify against `CTL-005 Cause and Effect Matrix` and `CTL-003 Control Narrative`.

B9. **Fire & gas functional test.** Install F&G devices per `TSF-004 Detector Layout`; functional-test per `TSF-011 SRS` and Cause & Effect.

B10. **Pressure equipment registration.** Submit `REG-022` package per jurisdictional procedure (TBD); obtain acceptance prior to pressurization.

B11. **SAT.** Execute `ELE-029` SAT and any site portions of `MEC-021/022` FAT scope re-verified at site.

B12. **Mechanical completion.** Walk down against the Construction interface and turnover checklist; clear punch list (or carry forward with disposition); issue MC certificate (template TBD).

B13. **Turnover to commissioning.** Hand over the turnover dossier: MC certificate; ITP closure; inspection releases; hydrotest packs; cleaning records; electrical test records; loop check sheets; F&G functional records; spares received register (`PRQ-015 SPIR`); `MEC-025 IOM`; as-built drawings (`PIP-028`, `INS-029`, and electrical/structural equivalents — ASSUMPTION).

## Verification

| Step | Verification |
|---|---|
| A1–A6 | CWP bundle issued (three artifacts named in `_CONTEXT.md` present); SOW-trace matrix reviewed |
| B1 | Inspection Release Certificate on file; receiving inspection record signed |
| B2 | Pile, anchor-bolt, and grout records signed; foundation release issued |
| B3 | Lift plan executed without deviation (or deviations logged); alignment record on file |
| B4 | Platform/stairs install inspection; code-of-practice access walk-down |
| B5 | Weld map closed; NDE acceptance reports filed |
| B6 | Flush certification before coalescer; hydrotest charts/sign-offs filed |
| B7 | Megger, continuity, motor solo run results; energization checklist closed |
| B8 | Loop check sheets reconciled to `INS-008` / `CTL-005` |
| B9 | F&G functional test records filed |
| B10 | Pressure equipment registration acceptance evidence on file |
| B11 | SAT closure report filed |
| B12 | MC certificate issued with punch-list dispositioned |
| B13 | Turnover dossier accepted by commissioning lead |

## Records

The CWP must produce, collect, or route the following records at close-out (origin in parentheses):

- Construction work package (this deliverable bundle).
- Installation and tie-in workface plan (this deliverable bundle).
- Construction interface and turnover checklist (this deliverable bundle).
- Inspection Release Certificate `QLT-020` (vendor).
- Material Test Reports / Certificates `QLT-013` (vendor).
- Manufacturing Record Book / Vendor Data Book `QLT-021` (vendor).
- Pile / foundation / grout records (site).
- Lift plan and execution record (site).
- Weld map, NDE reports (site).
- Flush, dry, and hydrotest packs `PIP-024 / PIP-025` (vendor procedure / site execution).
- Electrical test records and energization package `ELE-030` (site).
- Loop check sheets (site, against `INS-008` / `CTL-005`).
- F&G functional test records (site).
- Pressure equipment registration acceptance `REG-022` (jurisdiction).
- SAT records (site / vendor).
- Mechanical completion certificate (project MC procedure — TBD).
- Punch list and dispositions.
- Spares received register `PRQ-015 SPIR`; `MEC-025 IOM`.
- As-built drawings `PIP-028`, `INS-029`, and electrical/structural as-builts (ASSUMPTION on the latter).
