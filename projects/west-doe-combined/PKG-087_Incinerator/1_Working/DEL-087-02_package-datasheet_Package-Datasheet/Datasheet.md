# Datasheet: DEL-087-02 — PKG-087 Incinerator Package Datasheet

> Source-grounding note: Substantive equipment values are drawn from `26020-Package_Requirements.docx` package heading 40 (`26020-02-PT-25-003 — Incinerator`), referenced by the PROJECT_DECOMP row for PKG-087 and accessible locally under `_Sources/`. Cross-facility interface context is drawn from `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic treating and shared-interface incinerator language). The Source Basis pointer `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` is referenced by the package row but is not locally accessible; entries that depend solely on it are marked `location TBD` or `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-087-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | PKG-087 | `_CONTEXT.md` |
| Parent Workbook ID | 87 | `_CONTEXT.md` |
| Package Name | Incinerator | `_CONTEXT.md` |
| Package Tag (vendor handoff) | 26020-02-PT-25-003 — Incinerator | `PACKAGE_REGISTER.csv` row PKG-087, `ArtifactName` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row PKG-087 |
| Responsible Party (deliverable owner) | EPC Integrator | `_CONTEXT.md` |
| Package Vendor Scope | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row PKG-087 |
| EPC Integrator Scope | Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | `PACKAGE_REGISTER.csv` row PKG-087 |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; PROJECT_DECOMP objective mapping (ASSUMPTION — package-grouped) |
| Covers Scope Items | SOW-0111, SOW-0112, SOW-0113, SOW-0114 | `_CONTEXT.md` |

## Attributes — Process and Mechanical Basis

| Attribute | Value | Source |
|---|---|---|
| Process function | Vapours from the spent caustic storage tank and the caustic regeneration column overheads flow to the incinerator | `26020-Package_Requirements.docx` heading 40, Basic Scope |
| Service location | Physically near 3-25 flare stacks; services 4-25 NGL mercaptan treating | `26020-Package_Requirements.docx` heading 40, Location/Status |
| Facility allocation context | Shared-interface incinerator governed by current 03-25/04-25 allocation; exact service split and owner interface carried as open interface items | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC "Exclusions and Superseded Scope" / Emissions section |
| Number of incinerator stacks | 1 | `26020-Package_Requirements.docx` heading 40, Basic Scope |
| Number of KO drums | 1 | `26020-Package_Requirements.docx` heading 40, Basic Scope |
| Number of transfer pumps | 1 | `26020-Package_Requirements.docx` heading 40, Basic Scope |
| Number of blowers | 1 | `26020-Package_Requirements.docx` heading 40, Basic Scope |
| Design throughput (incinerator and KO drum) | 0.6 MMSCFD (17 E3M3D), preliminary | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| Spare philosophy | Single-train (1 x 100 percent); no installed spare stated in source | `26020-Package_Requirements.docx` heading 40 (ASSUMPTION based on stated equipment counts) |
| Modularization | Self-framing building to be erected at site | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Foundation responsibility | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes ("By others: ... foundations") |
| DCS integration | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| Electrical supply to MCC | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| Detailed metallurgy basis | location TBD — Source Basis RFQ `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` not locally accessible | TBD |

## Conditions — Process Operating Envelope

| Item | Value | Source |
|---|---|---|
| Design ambient temperature, min | -40 deg C | `26020-Package_Requirements.docx` heading 40, Scope Notes (Design conditions) |
| Design ambient temperature, max | +35 deg C | `26020-Package_Requirements.docx` heading 40, Scope Notes (Design conditions) |
| Incinerator operating pressure | 1 psig (7 kPag) | `26020-Package_Requirements.docx` heading 40, Scope Notes (Design conditions) |
| KO drum design pressure | 345 kPag (50 psig) | `26020-Package_Requirements.docx` heading 40, Scope Notes (Design conditions) |
| KO drum design temperature | -45.5 deg C to 260 deg C | `26020-Package_Requirements.docx` heading 40, Major Included Equipment (V-6900-1) |
| KO drum corrosion allowance | 1.59 mm C.A. | `26020-Package_Requirements.docx` heading 40, Major Included Equipment (V-6900-1) |
| Transfer pump capacity | 70 USGPM | `26020-Package_Requirements.docx` heading 40, Major Included Equipment (P-6900-1) and Scope Notes |
| Fluid operating conditions / pressures / temperatures (detailed) | location TBD — "See Appendix A for Fluid Operating Conditions, Pressures, Temperatures" not in accessible slice | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| Capacity of stack vs. tank-farm/VRU max relief rate | Stack capable of handling max relief rate from tank farm and VRU with less | `26020-Package_Requirements.docx` heading 40, Major Included Equipment (FL-6920-1) |

## Construction — Package Equipment Scope

| Item | Tag | Detail | Source |
|---|---|---|---|
| Incinerator Knock Out Drum | V-6900-1 | 2,896 mm (114 in) ID x 9,144 mm (30 ft) S/S; 345 kPag @ -45.5 / +260 deg C; 1.59 mm C.A. | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Incinerator KO Drum Transfer Pump | P-6900-1 | Vertical inline centrifugal pump; 70 USGPM; 5 hp, 575 V / 3 Ph / 60 Hz motor; Class 1 Div 2 | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Incinerator (low-pressure flare stack) | FL-6920-1 | NPS 6 x 54,861 mm (180 ft) tall; capable of max relief rate from tank farm and VRU | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Incinerator Blower | B-6920-1 | ARR-4 discharge vent; TEFC; 405T frame; 74 kW (100 hp), 575 V / 3 Ph / 60 Hz, 1800 rpm motor; Type VJ, Class II | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Instrumentation | — | See PFD for instrumentation (PFD not accessible in source slice; location TBD) | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Self-framing building | — | Erected at site | `26020-Package_Requirements.docx` heading 40, Major Included Equipment |
| Motor starting | — | VFD or soft start required for motors >= 100 hp (applies to B-6920-1 at 100 hp) | `26020-Package_Requirements.docx` heading 40, Scope Notes (Driver) |
| Foundations | — | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| Electrical supply to MCC | — | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes |
| DCS integration | — | By others (EPC) | `26020-Package_Requirements.docx` heading 40, Scope Notes |

### Applicable Interface Types (carried as evidence per `_CONTEXT.md` Notes)

From PACKAGE_REGISTER.csv row PKG-087 and corroborated by `26020-Package_Requirements.docx` heading 40, Physical Interface Summary:

- Process Piping (Yes)
- Utility Piping (Yes)
- Relief / Flare / Vent (Yes)
- Drain / Containment (Yes)
- Electrical Power (Yes)
- Area / Exterior Lighting (Yes — cross-reference `26020-Packages_Interfaces.3.xlsx` column M row 64; location TBD for the row content)
- Grounding / Bonding (Yes)
- I&C / Control Cabling (Yes)
- Building HVAC / Services — listed Yes in PACKAGE_REGISTER.csv row PKG-087; source heading 40 records "No" for Building HVAC / Services. See Conflict Table in `Guidance.md` (C-01).
- Fire & Gas / Safety Systems (Yes)
- Maintenance Access (Yes)
- Structural / Foundations / Supports (Yes)

Interfaces marked "No" in the source heading 40 (recorded for completeness):
- EHT (No)
- Cathodic Protection (No)
- Communications / Network (No)
- Grading / Site Drainage / Spill Containment (No)
- Product Loading (No)
- Pipeline / Pigging (No)

Source-grounded interface anchors (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`):
- Spent caustic tank vents through a flame arrestor to the incinerator header (DBM caustic treating section).
- Caustic regeneration column overheads route to the incinerator (heading 40 Basic Scope; cross-referenced by DBM caustic treating section).
- Shared-interface incinerator governed by current 03-25 / 04-25 allocation; exact service split is an open interface item (DBM Emissions/Exclusions sections).
- Incinerator overhead / dilution / enrichment-gas interfaces noted at the caustic mercaptan treating package (DBM caustic treating section).

## References

- Authoritative: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` heading 40 (`26020-02-PT-25-003 — Incinerator`)
- Supporting (cross-facility allocation and caustic interfaces): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Decomposition row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` PKG-087
- Deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` DEL-087-02
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable)
- TBD / inaccessible: `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` (Source Basis RFQ — location TBD); `26020-Packages_Interfaces.3.xlsx` / `26020-Packages_Interfaces_4_export.xlsx` row 64 detail content (xlsx not parsed in source slice; location TBD); Appendix A fluid operating conditions (location TBD)
