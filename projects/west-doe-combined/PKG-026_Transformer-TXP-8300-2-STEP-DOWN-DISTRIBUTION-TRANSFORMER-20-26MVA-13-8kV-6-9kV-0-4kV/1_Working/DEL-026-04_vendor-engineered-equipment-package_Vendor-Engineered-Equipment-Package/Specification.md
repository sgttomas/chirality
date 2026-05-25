# Specification: DEL-026-04 — Vendor Engineered Equipment Package (PKG-026 TXP-8300-2)

## Scope

This specification defines the normative content of the Vendor Engineered Equipment Package production unit for PKG-026 (step-down distribution transformer TXP-8300-2, 20/26 MVA, 13.8 kV/6.9 kV/0.4 kV).

**Covers:**
- Vendor-owned package engineering work product (design basis, calculations, datasheets).
- Vendor-owned package design work product (general arrangement, electrical schemes, protection/control schemes, accessory selection).
- Vendor-supplied physical equipment package (transformer TXP-8300-2 and integral accessories).
- Vendor package design basis and datasheet set as the technical envelope of the supplied equipment.
(Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-026-04; PACKAGE_REGISTER.csv PKG-026.)

**Excludes:**
- Facility-level integration, tie-ins, foundations, structural supports, area lighting, comms/network, grounding tie-ins, and constructability — owned by the EPC Integrator (PACKAGE_REGISTER.csv PKG-026; DEL-026-03 Construction Work Package).
- Acceptance and review evidence — owned by EPC Integrator (DEL-026-06).
- Vendor turnover document register — covered by DEL-026-05 (Vendor Document Turnover Package).

## Requirements

| ReqID | Requirement | Source / Authority |
|---|---|---|
| R-026-04-001 | The package shall be engineered, designed, fabricated/supplied, and integrated as a single vendor production unit anchored by the EPC Scope of Work (DEL-026-01) and EPC Package Datasheet (DEL-026-02). | DELIVERABLE_REGISTER.csv DEL-026-04 ("Notes" + "Description") |
| R-026-04-002 | Vendor scope shall cover package engineering, package design, vendor documentation, and the physical equipment package, with the EPC Integrator performing integration review. | PACKAGE_REGISTER.csv PKG-026 |
| R-026-04-003 | The supplied equipment shall be the step-down distribution transformer tagged TXP-8300-2 with nameplate identity 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV. Winding topology (two-winding vs three-winding) shall be confirmed against the EPC Package Datasheet (DEL-026-02). | Workbook Packages row 28 (package title); DEL-026-02 (basis, TBD) |
| R-026-04-004 | Each 6.9 kV transformer winding (where applicable) shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2985 |
| R-026-04-005 | Where the package serves 600 V (0.4 kV class) loads, 600 V transformer grounding shall use a 5 A continuous high-resistance grounding resistor. (ASSUMPTION: applicable if a 0.4 kV winding feeds a 600 V-class system; site uses 600 V LV class.) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L734; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2985 |
| R-026-04-006 | The vendor package shall accommodate the applicable PKG-026 interface types: Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. | PACKAGE_REGISTER.csv PKG-026 |
| R-026-04-007 | Vendor deliverables shall include (a) the engineered physical equipment package and (b) a vendor package design basis and datasheet set. | `_CONTEXT.md` Anticipated Artifacts |
| R-026-04-008 | Detailed nameplate, electrical, mechanical, environmental, and accessory parameters (BIL, impedance, tap range, vector group, cooling class ONAN/ONAF, sound power, ambient design temperature, altitude, enclosure rating, sensors, control voltage) shall be specified by the EPC Package Datasheet (DEL-026-02) and confirmed by the vendor. **TBD** in this deliverable; not present in accessible source slices. | TBD — DEL-026-02 not yet drafted; no source slice |
| R-026-04-009 | Vendor documents and document turnover register shall be delivered through DEL-026-05 (Vendor Document Turnover Package), not within this production unit. | DELIVERABLE_REGISTER.csv DEL-026-05 |
| R-026-04-010 | Integration acceptance of the vendor package against the EPC SOW, Package Datasheet, and Construction Work Package shall be performed through DEL-026-06 (EPC Vendor Package Review and Acceptance). | DELIVERABLE_REGISTER.csv DEL-026-06 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project Electrical Specifications and detailed design (facility) | Cable tray, conduit, grounding, bonding | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L768 — location TBD for the specification document itself |
| CEC (Canadian Electrical Code) — grounding conductor sizing | Distribution transformers, panelboards, 3-phase motors >100 hp | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2991 — clause TBD |
| Transformer construction/test standards (e.g., IEEE/IEC/CSA C88, IEC 60076, IEEE C57 series) | ASSUMPTION: typical for distribution transformer vendor packages; not named in accessible sources | location TBD |

## Verification

| ReqID | Verification Approach |
|---|---|
| R-026-04-001 | Document review confirming the vendor production-unit envelope matches DEL-026-01 SOW and DEL-026-02 Package Datasheet. |
| R-026-04-002 | Responsibility matrix review against PACKAGE_REGISTER.csv PKG-026 vendor/EPC split. |
| R-026-04-003 | Nameplate inspection and factory acceptance test (FAT) report cross-checked against the EPC Package Datasheet (DEL-026-02). |
| R-026-04-004 | NGR rating and timing confirmed on vendor schematics and protection coordination study; verified on site by IR/continuity tests. |
| R-026-04-005 | Confirmation that the 0.4 kV winding usage (if 600 V LV serving) matches site grounding convention; verified by vendor schematic review. |
| R-026-04-006 | Interface checklist review against PACKAGE_REGISTER.csv PKG-026 interface types (handled within DEL-026-06 acceptance). |
| R-026-04-007 | Deliverable completeness check — physical equipment received; vendor design basis and datasheet set received. |
| R-026-04-008 | Held until DEL-026-02 is issued; vendor datasheet to be cross-checked against EPC Package Datasheet. |
| R-026-04-009 | Confirmation that vendor documentation flows through DEL-026-05 register, not this production unit. |
| R-026-04-010 | DEL-026-06 acceptance record cites this deliverable's package contents. |

## Documentation

Vendor package shall produce:

- Vendor package design basis (electrical, mechanical, environmental).
- Vendor equipment datasheet set (transformer nameplate, NGR, accessories, sensors, control).
- General arrangement and outline drawings.
- Electrical single-line and protection scheme drawings.
- Interface drawings for the applicable PKG-026 interface types.
- FAT procedures and reports.
- Shipping, handling, storage, and installation instructions (issued to EPC for DEL-026-03 Construction Work Package).
- Operating and maintenance manuals (issued through DEL-026-05 Vendor Document Turnover Package).

(Source: `_CONTEXT.md` anticipated artifacts; DELIVERABLE_REGISTER.csv rows DEL-026-04, DEL-026-05, DEL-026-06; ASSUMPTION for individual document list items not enumerated in accessible sources.)
