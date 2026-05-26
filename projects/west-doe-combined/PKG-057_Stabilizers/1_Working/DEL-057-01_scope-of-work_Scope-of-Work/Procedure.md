# Procedure — DEL-057-01_scope-of-work — Scope of Work (PKG-057 Stabilizers)

This Procedure describes how to **produce** the EPC Scope of Work deliverable for PKG-057. (Operate/use procedures for the physical packages themselves are vendor scope, not part of this deliverable.)

## Prerequisites

1. Read deliverable-local metadata:
   - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` placeholder.
2. Open authoritative sources (locally accessible):
   - `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-057).
   - `_Decomposition/.../DELIVERABLE_REGISTER.csv` (rows DEL-057-01 through DEL-057-06).
   - `_Decomposition/.../SCOPE_LEDGER.csv` (rows SOW-0177, SOW-0178, SOW-0179, SOW-0180).
   - `_Decomposition/.../OBJECTIVE_REGISTER.csv` (rows OBJ-001, 003–010).
   - `_Decomposition/.../INTERFACE_REGISTER.csv` (rows scoped to PKG-057, where present).
   - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 (Inlet, Separation, Stabilization, and Stabilizer Overheads Basis).
3. Mark as **location TBD** any clause from the vendor RFQ (`26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`) until the source is opened.
4. Confirm declared upstream/downstream dependencies in `_DEPENDENCIES.md` (currently none declared).

## Steps

1. **Identity block.** Populate package identity from PACKAGE_REGISTER.csv (PKG-057, Stabilizers, vendor tag 26020-01-PT-17-005, WBS 01, discipline Mechanical) and DELIVERABLE_REGISTER row for DEL-057-01.
2. **Process function statement.** Write a single paragraph mirroring SOW-0178 ("Receive raw condensate from MPFF bottoms; through stabilizer flash feed separator for produced-water knockout; through basket strainers and feed pumps to feed/bottoms exchanger; into stabilizer column"). Extend with stabilized-product disposition (to NGL mercaptan treating) and overhead disposition (to SOC) per DBM-Deepcut SEC-04 lines 678, 710, 712.
3. **Package count, sparing, and train.** State three (3) Inlet Stabilizer Packages, 1,272 m3/d (8,000 bbl/d) each, 3 x 40% installed, 3:1 turndown, plot provision for a future fourth unit, and the MPFF-to-stabilizer 1:1 pairing rule (loss of stabilizer takes paired MPFF; single-unit outage leaves 80% capacity). (Source: SOW-0179; SOW-0180; DBM-Deepcut SEC-04 lines 608–612.)
4. **Equipment set.** Enumerate per-package equipment from SOW-0179 and DBM-Deepcut SEC-04 lines 706–708: trayed reboiled column (20 floating-valve trays), flash feed separator, two 100% multistage centrifugal feed pumps with basket strainers, feed/bottoms BEU exchanger, vertical NEN thermosiphon reboiler with seal-welded tubes, product cooler with 130% excess area and single fan, 1 LIT, 1 TIT (minimum).
5. **Operating and design conditions.** Tabulate values from SOW-0180 (flash feed separator 345 kPag / 30.6 °C operating; 1,724 kPag / 60 °C design; stabilizer column inlet 71 °C; minimum column design pressure 793 kPag; feed/bottoms minimum approach 16.7 °C; product cooler 130% excess area; outlet 110 °F) and cross-cite DBM-Deepcut SEC-04 lines 678, 702, 704, 706, 708.
6. **Drivers.** State electric-motor / VFD-compatible drivers for feed pumps and product cooler fan. (Source: SOW-0180.)
7. **Package boundary / "by others".** Spell out the SOW-0180 boundary: interconnecting piping at skid edge, DCS integration, foundations, electrical supply from plant MCC, installation/erection — all by others.
8. **Vendor / EPC responsibility split.** Write the OBJ-004-aligned responsibility paragraph: Package Vendor owns engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv `_responsibility`.)
9. **Interface narrative.** Walk the 13 package-level interface types from PACKAGE_REGISTER `_interface_types` in order; for each, cite the corresponding INTERFACE_REGISTER row(s) for PKG-057 where present, otherwise mark the interface fact **location TBD**.
10. **Integration routing items.** Document required routings: stabilized C5+ to NGL mercaptan treating (with single-package divert to slop tank); stabilizer flash feed overhead to SOC first-stage suction; tower overhead to SOC second-stage suction; relief and blowdown from flash feed and tower to HP flare. (Source: DBM-Deepcut SEC-04 lines 678, 704, 710, 712, 813.)
11. **Open items / TBDs.** List unresolved engineering items: strainer mesh, pump seal type, reboiler heat-medium temperature, product cooler elevation trade-off, stabilizer feed source mix beyond MPFF bottoms, RFQ-derived clauses (location TBD), third-package tag set (TBD). (Source: DBM-Deepcut SEC-04 lines 702, 706, 708.)
12. **Cross-document consistency sweep.** Verify Datasheet ↔ Specification ↔ Guidance ↔ Procedure use identical numeric values and unit choices for the parameters in Step 5; reconcile any rounding/units discrepancies.
13. **Conflict Table check.** Confirm Conflict Table entries (currently CONF-057-01-01 through CONF-057-01-03) remain accurate; add new rows when source disagreements are discovered.
14. **Issue for review.** Set `_STATUS.md` to `INITIALIZED` (already handled by Pass 1/2 status update step); the deliverable is then ready for `WORKING_ITEMS` review and, on acceptance, status progression by an authorized agent.

## Verification

- All four documents exist and use the default schema sections.
- Every non-trivial numeric value in Datasheet/Specification is traceable to SOW-0178/0179/0180 or DBM-Deepcut SEC-04 line numbers.
- Vendor / EPC responsibility paragraph matches PACKAGE_REGISTER `_responsibility` text and OBJ-004 description.
- Interface-type list matches PACKAGE_REGISTER `_interface_types` exactly.
- Anticipated artifacts listed in `_CONTEXT.md` (package scope of work; tagged equipment list; package function and integration narrative; responsibility assignment record) are all addressed.
- Open items captured as TBD; no values invented.
- Conflict Table present in Guidance with at least the three current rows.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four-document kit (this folder).
- `_STATUS.md` history line recording the OPEN → INITIALIZED transition.
- `_run_records/TASK_RUN_2026-05-25_0425.md` — this run's audit record.
- Downstream evidence (produced by later deliverables, not this one): DEL-057-02 (Datasheet artifact), DEL-057-03 (CWP), DEL-057-04 (vendor package), DEL-057-05 (vendor doc turnover), DEL-057-06 (EPC review/acceptance).
