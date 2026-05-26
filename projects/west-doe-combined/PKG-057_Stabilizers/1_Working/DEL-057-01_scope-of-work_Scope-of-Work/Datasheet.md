# Datasheet — DEL-057-01_scope-of-work — Scope of Work (PKG-057 Stabilizers)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-057-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Parent Package | PKG-057 — Stabilizers (WBS 01) | PACKAGE_REGISTER.csv |
| Workbook Row | Packages row 82 | PACKAGE_REGISTER.csv `_source_basis` |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| Vendor Tag | 26020-01-PT-17-005 — Inlet Stabilizers | PACKAGE_REGISTER.csv `_responsibility_tag` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0177, SOW-0178, SOW-0179, SOW-0180 | SCOPE_LEDGER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package process function | Receive raw condensate from MPFF bottoms; pass through stabilizer flash-feed separator (produced-water knockout); through basket strainers and stabilizer feed pumps to the stabilizer feed/bottoms exchanger; into the stabilizer column. | SOW-0178; 26020-Package_Requirements.docx pkg heading 12 |
| Package count | Three (3) Inlet Stabilizer Packages | SOW-0178; SOW-0179 |
| Per-package design rate | 1,272 m3/d (8,000 bbl/d) | SOW-0179; SOW-0180; DBM-Deepcut SEC-04 (line 612) |
| Train design basis | 3 x 40% installed; plot provision for a future fourth unit | DBM-Deepcut SEC-04 (line 612) |
| MPFF–Stabilizer pairing | One MPFF assigned to one stabilizer; loss of stabilizer takes paired MPFF out of service | DBM-Deepcut SEC-04 (line 608–610) |
| Capacity loss on single-unit trip | Loss of one installed unit leaves 80% capacity | DBM-Deepcut SEC-04 (line 612) |
| Tower configuration | Trayed, reboiled distillation column; 20 floating-valve trays | SOW-0179; DBM-Deepcut SEC-04 (line 678) |
| Tower turndown | 3:1 | SOW-0180; DBM-Deepcut SEC-04 (line 678) |
| Stabilizer feed pumps | Two 100% multistage horizontal centrifugal pumps, basket strainers upstream | DBM-Deepcut SEC-04 (line 706) |
| Feed/bottoms exchanger | Shell-and-tube BEU; inlet liquids on shell side; 16.7 °C (30 °F) minimum approach | SOW-0180; DBM-Deepcut SEC-04 (line 706) |
| Reboiler | Vertical NEN single-pass thermosiphon; process fluid tube-side; tubes seal-welded to tubesheet; hot heat medium | DBM-Deepcut SEC-04 (line 706) |
| Product cooler | 130% excess area at design; single fan; cools product to ~110 °F (43.3 °C) | SOW-0180; DBM-Deepcut SEC-04 (line 708) |
| Reboiler / column duty target | Heat to ~71 °C (160 °F) at column top tray | SOW-0180; DBM-Deepcut SEC-04 (line 678) |

## Operating Conditions

| Parameter | Value | Source |
|---|---|---|
| Flash feed separator operating pressure | 345 kPag (50 psig) | SOW-0180; DBM-Deepcut SEC-04 (line 704) |
| Flash feed separator operating temperature | 30.6 °C (per Word source); ~87 °F (~30.6 °C) per DBM | SOW-0180; DBM-Deepcut SEC-04 (line 704) |
| Flash feed separator retention | ~15 minutes (TBC); ≥10 min LLL–HLL liquid retention | DBM-Deepcut SEC-04 (line 704) |
| Stabilizer inlet temperature | 71 °C (140 °F upstream of inlet LCV per DBM) | SOW-0180; DBM-Deepcut SEC-04 (line 702) |
| Stabilizer inlet pressure upstream of LCV | 250 psig (~1724 kPag) | DBM-Deepcut SEC-04 (line 702) |
| Stabilized product outlet temperature | 110 °F (43.3 °C) at product cooler outlet | SOW-0180; DBM-Deepcut SEC-04 (line 708) |

## Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Flash feed separator design pressure | 1,724 kPag | SOW-0180 |
| Flash feed separator design temperature | 60 °C | SOW-0180 |
| Stabilizer column minimum design pressure | 793 kPag | SOW-0180 |
| Feed/bottoms exchanger minimum approach | 16.7 °C (30 °F) | SOW-0180 |
| Product cooler excess area | 130% of design point | SOW-0180 |
| Turndown ratio | 3:1 | SOW-0180 |

## Construction / Drivers / Vendor Responsibility

| Item | Value | Source |
|---|---|---|
| Feed pump driver | Electric motor; VFD compatible | SOW-0180 |
| Product cooler fan driver | Electric motor; VFD compatible | SOW-0180 |
| Vendor scope (Package Vendor) | Package engineering, package design, vendor documentation, and physical equipment package | PACKAGE_REGISTER.csv `_responsibility`; DELIVERABLE_REGISTER.csv |
| EPC Integrator scope | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv `_responsibility` |
| Items "by others" (i.e., outside skid edge) | Interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, installation/erection | SOW-0180 |

## Applicable Interface Types (package-level)

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. (Source: PACKAGE_REGISTER.csv `_interface_types`.)

## Tagged Equipment / Identity (best-evidence)

| Item | Tag(s) | Source |
|---|---|---|
| Stabilizer column (per package) | T-7200-1 / T-7400-1 (per train; third package tag set TBD) | DBM-Deepcut SEC-04 Equipment Table (line 754) |
| Stabilizer flash feed separator | V-7210-1 / V-7410-1 | DBM-Deepcut SEC-04 Equipment Table (line 749) |
| MPFF (paired upstream) | V-7110-1 / V-7310-1 (paired; not in PKG-057 scope) | DBM-Deepcut SEC-04 Equipment Table (line 756) |
| Stabilizer feed pumps | Two 100% per package; specific tags TBD | DBM-Deepcut SEC-04 (line 706) |
| Stabilizer reboiler | One per package; specific tag TBD | DBM-Deepcut SEC-04 (line 706) |
| Feed/bottoms exchanger | One per package; specific tag TBD | DBM-Deepcut SEC-04 (line 706) |
| Product cooler | One per package; specific tag TBD | DBM-Deepcut SEC-04 (line 708) |

ASSUMPTION: source equipment table lists tags for two trains; tags for the third (and future fourth) stabilizer package are TBD pending detailed tag-numbering schedule.

## References

- Workbook Packages row 82 (PACKAGE_REGISTER.csv row PKG-057)
- 26020-Package_Requirements.docx, package heading 12 — scope items SOW-0177 through SOW-0180 (SCOPE_LEDGER.csv)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04: Inlet, Separation, Stabilization, and Stabilizer Overheads Basis (lines ~569–712)
- Bid Docs/Budgetary/26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx (TBD: not locally accessible as text; cited in PACKAGE_REGISTER `_source_basis`; location TBD)
- DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv (Gate 7 snapshot)
