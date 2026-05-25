# Specification: DEL-020-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-020`, the 13.8kV SWITCHGEAR EQUIPMENT package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design of the plant main power distribution center.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-011). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, final breaker selections, relay settings, and protection-coordination studies are excluded from this EPC datasheet unless later provided as vendor data.
- Detailed breaker count and ratings, bus ampacity, short-circuit/withstand rating, arc-flash mitigation scheme, metering, relaying, and protection coordination are `TBD` because the accessible source set does not assign package-specific numeric values; these are governed by ELC-QAS-000007-001 (Medium Voltage Switchgear) and the detailed engineering studies cited in the DBM.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-020-02-001 | The Package Datasheet shall identify `PKG-020`, workbook row 22, WBS 01, CoA tracking number 26020-01-30-011, discipline Electrical, and package name "13.8kV SWITCHGEAR EQUIPMENT." Source: Workbook Packages row 22; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-020-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-020`. | Responsibility statement review against Gate 7 package register. |
| REQ-020-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 22; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-020`. |
| REQ-020-02-004 | The Package Datasheet shall identify the 13.8 kV switchgear as the plant main power distribution center, fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer, with the bus sized for the full facility scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (lines 2917-2919). | Source citation review against DBM Power System paragraphs. |
| REQ-020-02-005 | The Package Datasheet shall specify the bus electrical basis as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table (line 2934). | Source citation review. |
| REQ-020-02-006 | The Package Datasheet shall identify the radial distribution feeders from the 13.8 kV switchgear to the five named downstream electrical buildings (6.9 kV; 4.16 kV Acid Gas/Overheads; 600 V Acid Gas; 600 V Sales/Overheads; 4.16 kV/600 V General Area/Tank Farm/Process). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (lines 2919-2925). | Feeder list review. |
| REQ-020-02-007 | The Package Datasheet shall identify the 03-25 sub-feed from the 04-25 13.8 kV Main Switchgear Electrical Building as a cross-facility tie at 13.8 kV LRG. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Power Supply (lines 732, 740). | Cross-facility tie review against the 03-25 DBM. |
| REQ-020-02-008 | The Package Datasheet shall preserve the standby-power basis: the prior centralized 13.8 kV emergency-generator concept has been replaced by TOU standby generators at the 600 V MCC level with transfer switches; the 13.8 kV switchgear shall not be designed around a centralized 13.8 kV standby generator. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power (line 2943); 03-25 DBM (line 505). | Standby-power scope review. |
| REQ-020-02-009 | The Package Datasheet shall require utility-transformer neutral grounding via a 200 A, 10 s neutral grounding resistor operating as a tripping system, and shall require coordination with the plant grounding/bonding basis (two-point grounding for major equipment, #2/0 green insulated main grounding conductor, ground wells at electrical buildings). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding (lines 2985-2989). | Grounding interface review against DBM grounding paragraphs. |
| REQ-020-02-010 | The Package Datasheet shall specify housing of the 13.8 kV main switchgear in the 810-1 13.8kV Switchgear Electrical Building (prefabricated, modular, general-purpose-area location, n+1 HVAC, bottom cable entry). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings list (line 2811); Electrical Buildings (lines 2973-2977). | Housing requirement review. |
| REQ-020-02-011 | The Package Datasheet shall specify 13.8 kV medium-voltage cabling as three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways (line 3007). | Cable specification review. |
| REQ-020-02-012 | The Package Datasheet shall require separation of 13.8 kV power circuits from control and instrument circuits by distance, shielding, or routing. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line 768). | Routing review. |
| REQ-020-02-013 | The Package Datasheet shall specify that medium-voltage breaker control circuits and medium-voltage protective relays are supplied from 120 VAC / 125 VDC UPS systems. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages (line 2939). | Control-power interface review. |
| REQ-020-02-014 | The Package Datasheet shall identify source gaps for breaker count, breaker ratings (continuous and interrupting), short-circuit/withstand rating, bus ampacity, metering scheme, relaying/protection-coordination scheme, and arc-flash mitigation as `TBD` rather than invented values; these are governed by ELC-QAS-000007-001 (Medium Voltage Switchgear) and shall be confirmed during detailed engineering. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 (lines 2872-2889). | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Governing code for electrical design and installation. | Applicable; specific clauses TBD. |
| ELC-QAS-000007-001 Medium Voltage Switchgear (Rev. 1) | Project electrical specification governing this package's switchgear design and procurement basis. | Applicable as primary project spec; document text not in deliverable folder (location TBD). |
| ELC-QAS-000002-001 Electrical Design (Rev. 1) | Project electrical design specification. | Applicable; document location TBD. |
| ELC-QAS-000001-001 Electrical Construction (Rev. 1) | Project electrical construction specification. | Applicable; document location TBD. |
| ELC-QAS-000003-001 Electrical Requirements for Packaged Equipment (Rev. 2) | Applies to vendor packaged equipment integration. | Applicable; document location TBD. |
| Applicable BC provincial/local electrical codes; Technical Safety BC; WorkSafeBC; BCER | Regulatory bodies cited by the electrical basis. | Applicable; clause-level requirements TBD. |
| CSA, API, IEEE, ISA, NEMA | Cited applicable standards in the electrical basis. | Applicable; specific standards TBD at clause level. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 22 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-020`. | All six applicable interfaces are present (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). |
| Source fidelity | Check every non-trivial value or requirement against cited DBM source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Standby-power basis fidelity | Check that the datasheet does not impose a centralized 13.8 kV emergency-generator design. | Aligns with current TOU-LV standby-power basis. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, voltages, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet (`ART-52BE7C60A3`).
- Vendor engineering handoff basis (`ART-5502C482A0`).
- Package interface requirements matrix (`ART-5089BC8CE1`).
- Interface fact evidence rows for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports (`ART-96F3259450`, `ART-3BE5EC993A`, `ART-247B070DE4`, `ART-7AFC53B74A`, `ART-9D12EA92DC`, `ART-0D56AE6EA1`).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 22, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV switchgear basis.
