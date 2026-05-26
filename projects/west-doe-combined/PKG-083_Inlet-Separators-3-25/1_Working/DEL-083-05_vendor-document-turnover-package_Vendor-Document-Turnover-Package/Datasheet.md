# Datasheet — DEL-083-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-083-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-083` |
| PackageName | Inlet Separators 3-25 |
| PackageTag | `26020-02-PT-17-003` |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Anticipated Artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment governed | Two (2) Identical Horizontal three-phase separators (sour gas / sour raw condensate / sour water service) | `26020-Package_Requirements.docx` heading 36 ("26020-02-PT-17-003 - Inlet Separators"), Basic Scope |
| Sparing basis | 2 x 50% | Same source, Major Included Equipment |
| RFQ / Source basis | `Bid Docs/Budgetary/26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx` | Same source, Source Basis |
| Design pressure | 4973 kPag | Same source, Scope Notes / Open Items, Design conditions |
| Operating pressure range | 862 to 3944 kPag (125 to 572 psig) | Same source, Operating conditions |
| Throughput | 1,132 - 2,264 e3m3/d (40 - 80 MMSCFD) | Same source, Capacity/design throughput |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row PKG-083; mirrored in 26020 Word source physical interface table |

## Conditions

| Attribute | Value | Source |
|---|---|---|
| Service environment | 3-25 West Doe Compressor Station; sour service (H2S handling implied by three-phase sour separation duty) | `26020-Package_Requirements.docx` heading 36, Location / Status + Basic Scope |
| Lifecycle states covered by turnover | Engineering submittals through manufacturing records, FAT records, IOM manuals, and final Vendor Data Book | Derived from vendor deliverable list (`MEC-021/022/023/025`, `PRQ-016`) in source |
| Coordination mode | DECLARED; no upstream/downstream dependencies declared in `_DEPENDENCIES.md` | `_DEPENDENCIES.md` |

## Construction (Composition of the Turnover Package)

The turnover package is a controlled aggregation of vendor-produced documents drawn from the vendor engineering deliverable list issued for PKG-083 in `26020-Package_Requirements.docx` (heading 36). The package SHALL include, at minimum, the following vendor deliverable rows from that source:

### Core vendor documents
- `PRQ-009` Vendor Document Index
- `DOC-008` Vendor Document Control Procedure
- `QLT-006` Supplier Quality Plan
- `QLT-003` Inspection and Test Plan (ITP)
- `QLT-013` Material Test Reports / Certificates
- `QLT-020` Inspection Release Certificate
- `QLT-021` Manufacturing Record Book / Vendor Data Book
- `PRQ-013` Logistics / Shipping Plan
- `PRQ-015` Spare Parts Interchangeability Record (SPIR)
- `PRQ-016` Vendor Data Book / Final Supplier Documentation

### Core package engineering
- `MEC-001` Mechanical Design Basis
- `MEC-002` Mechanical Equipment List
- `MEC-003` Mechanical Equipment Data Sheets
- `MEC-006` Package Equipment Specifications
- `MEC-014` Mechanical Calculation Package
- `MEC-016` Equipment General Arrangement Drawing
- `MEC-017` Equipment Installation / Setting Drawings
- `MEC-018` Lifting / Handling Study for Major Equipment
- `MEC-021` Equipment FAT / Performance Test Procedure
- `MEC-022` Equipment FAT / Performance Test Report
- `MEC-023` Vendor Data Book / Mechanical Final Documentation
- `MEC-024` Mechanical Spares / Special Tools Requirements
- `MEC-025` Mechanical Equipment IOM Manual

### Static pressure equipment
- `MEC-005` Static Equipment Specifications
- `MEC-009` Pressure Vessel Data Sheets
- `REG-022` Pressure Equipment Registration Package

### Relief / flare / vent
- `PRO-014` Relief and Flare Design Basis
- `PRO-015` PSV / Pressure Relief Sizing Calculations
- `PRO-016` Relief Valve Data Sheets
- `PRO-017` Flare Load Summary / Flare System Study
- `PRO-018` Blowdown / Depressurization Study

### Process piping interfaces
- `PRO-008` P&IDs
- `PIP-003` Piping Line List
- `PIP-004` Tie-In List / Tie-In Scope Sheets
- `PIP-006` Equipment Arrangement / Piping General Arrangement
- `PIP-007` Piping Plans and Sections
- `PIP-008` Piping Isometric Drawings
- `PIP-009` Fabrication Isometrics with BOM
- `PIP-017` Piping MTO
- `PIP-018` Valve Data Sheets
- `PIP-024` Hydrotest / Pressure Test Packages
- `PIP-025` Flushing / Cleaning / Drying Procedure
- `PIP-028` Piping As-Built Drawings

### Utility, drainage, electrical/EHT/grounding, I&C, building/HVAC, fire & gas, structural
See `Specification.md` Requirements section for the full vendor deliverable roster derived from the source table (utility, drainage, ELE/EHT/grounding, INS/CTL, TSF, STR families). Each row in the source vendor engineering deliverables table is an artifact slot in this turnover package.

## References

- `_REFERENCES.md` (this deliverable)
- `26020-Package_Requirements.docx` heading 36 — "26020-02-PT-17-003 - Inlet Separators" (vendor engineering deliverable table is the source of record for the turnover composition)
- `PACKAGE_REGISTER.csv` row `PKG-083` (Gate-07 snapshot)
- `DELIVERABLE_REGISTER.csv` row `DEL-083-05_vendor-document-turnover-package` (Gate-07 snapshot)
- Identified vendor RFQ basis: `Bid Docs/Budgetary/26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx` — referenced by 26020 source; local accessibility `TBD`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — DBM context for the 3-25 area
