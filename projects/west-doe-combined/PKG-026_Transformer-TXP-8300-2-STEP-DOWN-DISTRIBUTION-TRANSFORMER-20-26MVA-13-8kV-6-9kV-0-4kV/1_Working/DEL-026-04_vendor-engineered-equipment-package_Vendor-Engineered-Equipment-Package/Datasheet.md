# Datasheet: DEL-026-04 — Vendor Engineered Equipment Package (PKG-026 Transformer TXP-8300-2)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-026-04_vendor-engineered-equipment-package | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | PKG-026 | `_CONTEXT.md` |
| ParentWorkbookID | 26 | `_CONTEXT.md` |
| PackageName | Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | `_CONTEXT.md` |
| PackageTag | TXP-8300-2 | Package title (Workbook Packages row 28) |
| Discipline | Electrical | `_CONTEXT.md`; PACKAGE_REGISTER.csv (PKG-026 discipline=Electrical) |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-026-04 |
| CoversScopeItem | SOW-0027 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| SupportsObjectives (ASSUMPTION, package heuristic) | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv (package-grouped) |
| DecompositionSnapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |

## Attributes (Vendor-Engineered Equipment Package Definition)

| Attribute | Value | Source |
|---|---|---|
| Production unit subject | Step-down distribution transformer tagged TXP-8300-2 (and its vendor-supplied package scope) | Package title (Workbook Packages row 28) |
| Vendor-owned content | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv PKG-026 |
| EPC-owned content | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv PKG-026 |
| Anticipated artifact A | Vendor engineered physical equipment package | `_CONTEXT.md` |
| Anticipated artifact B | Vendor package design basis and datasheet set | `_CONTEXT.md` |
| Upstream EPC anchors | DEL-026-01 (Scope of Work), DEL-026-02 (Package Datasheet) | DELIVERABLE_REGISTER.csv PKG-026 rows 01,02 |
| Applicable package interface types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv PKG-026 |
| Package exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv PKG-026 |

## Equipment Identity (from Package Title)

| Field | Value | Source |
|---|---|---|
| Equipment tag | TXP-8300-2 | Workbook Packages row 28 (package title) |
| Equipment description | Step-down distribution transformer | Workbook Packages row 28 |
| Rated capacity (nameplate identity) | 20/26 MVA (ASSUMPTION: dual ONAN/ONAF or equivalent rating split inferred from `20/26` notation; not confirmed in accessible sources) | Workbook Packages row 28 |
| Voltage classes (nameplate identity) | 13.8 kV / 6.9 kV / 0.4 kV (three voltage levels carried in package title; transformer winding topology TBD — two-winding vs three-winding allocation not stated in accessible sources) | Workbook Packages row 28 |
| Service environment | Process facility (Comp/Liquids and/or Deepcut electrical scope; specific building/area assignment TBD) | DBM context; specific allocation not confirmed |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Primary feed reference (site) | 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded (LRG) (ASSUMPTION as the site primary class to which TXP-8300-2 may connect) | `3-25_Comp_and_Liquids_DBM.md` §"Incoming Power and Transformers" L732 |
| Medium-voltage service (site, for 6.9 kV class) | 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded; 100 A, 10 s neutral grounding resistor on each 6.9 kV transformer | `4-25_Deepcut_DBM.md` L2935, L2985 |
| Low-voltage service (site) | 600 V or 0.4 kV class served via distribution transformers; grounding per facility electrical design basis | `3-25_Comp_and_Liquids_DBM.md` L734; `4-25_Deepcut_DBM.md` L2937 |
| Site-specific TXP-8300-2 operating conditions (ambient, altitude, sound, BIL, impedance, tap range, cooling class) | TBD — not present in accessible source slices | TBD |

## Construction (Package Composition)

| Element | Value | Source |
|---|---|---|
| Engineering | Vendor-prepared package engineering deliverables (design basis, calculations, datasheets, interface drawings) | PACKAGE_REGISTER.csv PKG-026; DELIVERABLE_REGISTER.csv DEL-026-04 |
| Design | Vendor-prepared package design (general arrangement, electrical schemes, protection/control schemes, accessory selection) | PACKAGE_REGISTER.csv PKG-026 |
| Fabrication / Supply | Vendor-fabricated/supplied transformer and ancillary package components | DELIVERABLE_REGISTER.csv DEL-026-04 |
| Physical equipment | Step-down distribution transformer TXP-8300-2 with package accessories (bushings, surge arresters, cooling system, control cabinet, sensors); detailed bill of materials TBD | Workbook Packages row 28; vendor BOM TBD |
| Integration responsibility | EPC Integrator owns facility-level integration, tie-ins, foundations, cabling termination, area lighting, grounding tie-in, comms, maintenance access | PACKAGE_REGISTER.csv PKG-026 |

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (Gate 7 snapshot pointers)
- DELIVERABLE_REGISTER.csv (GATE-07): DEL-026-04 row
- PACKAGE_REGISTER.csv (GATE-07): PKG-026 row
- OBJECTIVE_DELIVERABLE_MAP.csv (GATE-07): package-grouped objective mapping (PACKAGE_HEURISTIC, ASSUMPTION)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (site electrical conditions; voltage classes)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (6.9 kV class, grounding)
- Workbook Packages row 28 (package identity)
- Sibling deliverables (upstream EPC anchors): DEL-026-01 Scope of Work, DEL-026-02 Package Datasheet
