# Datasheet — DEL-057-03 Construction Work Package (PKG-057 Stabilizers)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-057-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-057` |
| PackageName | Stabilizers |
| ParentWorkbookID | 57 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Source basis | Workbook Packages row 82; 26020-Package_Requirements.docx package heading 12 |
| Decomposition snapshot | `GATE-07_Final_Published_2026-05-24` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Inlet stabilization of raw condensate (MPFF bottoms): flash separation, basket strainers, feed pumps, feed/bottoms exchanger, stabilizer column, product cooler | SCOPE_LEDGER `SOW-0178`, `SOW-0179`, `SOW-0180` |
| Package count | Three (3) Inlet Stabilizer Packages, 3 x 40% configuration | `SOW-0179` |
| Design rate (per package) | 1,272 m3/d (8,000 bbl/d) | `SOW-0179`, `SOW-0180` |
| Turndown ratio | 3:1 | `SOW-0180` |
| Major equipment | Trayed reboiled distillation column with 20 floating valve trays; one (1) LIT; one (1) TIT; feed pumps (electric motor, VFD compatible); product cooler fan (electric motor, VFD compatible); feed/bottoms exchanger; flash feed separator | `SOW-0179`, `SOW-0180` |
| Sour-service applicability | TBD — confirm sour-service classification from DBM SEC-09/SEC-14 (sources referenced via OBJ-009; local source slice not extracted) | `_REFERENCES.md` (deferred slices), OBJ-009 |
| Construction discipline | Mechanical (per PKG-057 register row) | `PACKAGE_REGISTER.csv` row 82 |

## Conditions

| Boundary / Condition | Value | Source |
|---|---|---|
| Flash feed separator — operating pressure | 345 kPag | `SOW-0180` |
| Flash feed separator — operating temperature | 30.6 °C | `SOW-0180` |
| Flash feed separator — retention time | approximately 15 minutes | `SOW-0180` |
| Feed/bottoms exchanger | Liquid hydrocarbons pre-heated to 71 °C; minimum approach 16.7 °C (30 °F) | `SOW-0180` |
| Stabilizer column inlet | 71 °C | `SOW-0180` |
| Stabilizer column — minimum pressure | 793 kPag | `SOW-0180` |
| Flash feed separator — design inlet pressure | 1724 kPag | `SOW-0180` |
| Flash feed separator — design inlet temperature | 60 °C | `SOW-0180` |
| Product cooler design | 130% (basis as stated in source) | `SOW-0180` |
| By others (excluded from package scope) | Interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection | `SOW-0180` |

## Construction (Installation / Tie-in / Turnover Attributes)

| Attribute | Value | Source |
|---|---|---|
| Installation responsibility | EPC Integrator (per PKG-057 responsibility split; "installation / erection" listed as By Others to the Package Vendor) | `PACKAGE_REGISTER.csv` row 82; `SOW-0180` |
| Foundations | EPC Integrator scope (By Others to vendor) | `SOW-0180` |
| Skid-edge interconnect piping | EPC Integrator scope (By Others to vendor) | `SOW-0180` |
| Electrical power supply from MCC | EPC Integrator scope (By Others to vendor) | `SOW-0180` |
| DCS integration | EPC Integrator scope (By Others to vendor) | `SOW-0180` |
| Applicable interface families | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv` row 82 |
| Package count to be installed and tied-in | 3 | `SOW-0179` |
| Constructability constraints | TBD — package-specific lift, layout, and access constraints not extracted from source (slices not copied locally) | `_REFERENCES.md` |
| Turnover record set | TBD — defined by interface and acceptance evidence developed under `DEL-057-06`; this package consumes the turnover checklist artifact listed under anticipated artifacts | `_CONTEXT.md` |

## Anticipated Artifacts (carried into this package)

- Construction work package narrative
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- Decomposition (authoritative basis for this draft):
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row `DEL-057-03_construction-work-package`
  - `.../PACKAGE_REGISTER.csv` row 82 (PKG-057)
  - `.../SCOPE_LEDGER.csv` rows `SOW-0177`, `SOW-0178`, `SOW-0179`, `SOW-0180`
  - `.../OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`
- Source materials referenced by the decomposition row (location TBD — slices not copied locally):
  - `_Sources/26020-Package_Requirements.docx` package heading 12
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 82
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (OBJ-001, OBJ-003, OBJ-005..OBJ-010 source basis)
