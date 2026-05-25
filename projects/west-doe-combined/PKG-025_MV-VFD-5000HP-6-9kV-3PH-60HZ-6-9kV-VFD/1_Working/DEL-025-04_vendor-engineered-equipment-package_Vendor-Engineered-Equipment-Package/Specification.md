# Specification — DEL-025-04 Vendor Engineered Equipment Package (PKG-025 MV VFD)

## Scope

This specification governs the Package Vendor production unit for PKG-025 "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD". It covers vendor package engineering, package design, fabrication/supply, vendor documentation, and the physical equipment package itself, developed from the EPC Scope of Work (DEL-025-01) and EPC Package Datasheet (DEL-025-02) (`_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-025-04).

Out of scope: facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration outside the package boundary — these are EPC Integrator scope (PACKAGE_REGISTER.csv row PKG-025).

DOMAIN unsupported variant check: this is `PROJECT_DECOMP`; the four-document set applies.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-025-04-01 | The VFD shall function as a Starting VFD for the Inlet/Sales Gas Compressor motors (KM-2150/2250 service basis), with synchronous transfer to a normal-service 6.9 kV bus after the motor reaches full speed. | DBM-Deepcut/4-25_Deepcut_DBM.md lines 893, 2955 |
| REQ-025-04-02 | Output service shall be compatible with 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage system. | DBM line 2935 |
| REQ-025-04-03 | The VFD shall be installed within the 6.9 kV Inlet/Sales Compressor Electrical Building, a prefabricated modular building in a general-purpose area with n+1 HVAC. | DBM lines 2921, 2973, 2975 |
| REQ-025-04-04 | The VFD shall interconnect with the 6.9 kV motor control center (MCC-8200 reference) which provides mechanically latched fused contactors with motor protection relays and an Ethernet communication port to the plant PLC central control panel. | DBM line 2955 |
| REQ-025-04-05 | No power-factor-correction capacitor banks shall be installed on the MCC-8200 synchronous-transfer bus associated with the Starting VFD. | DBM line 2955 |
| REQ-025-04-06 | Low-voltage power cable fed from VFDs shall be copper TECK cable; 6.9 kV cabling between VFD/MCC and motor shall be three-conductor copper TECK rated 8 kV with 100 percent insulation, shielded. | DBM lines 3008, 3013 |
| REQ-025-04-07 | Where the VFD-fed motor is located in a Zone 2 area, the motor shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. | DBM line 2961 |
| REQ-025-04-08 | The 6.9 kV transformer feeding the VFD bus shall be grounded using a 100 A, 10 s neutral grounding resistor and operate as a tripping system. (Interface requirement on upstream EPC scope; vendor shall accommodate.) | DBM line 2985 |
| REQ-025-04-09 | Vendor shall deliver vendor package design basis and datasheet set for the engineered equipment package as an integral artifact. | DELIVERABLE_REGISTER.csv DEL-025-04 anticipated artifacts |
| REQ-025-04-10 | Vendor scope shall include package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration and interface tie-ins. | PACKAGE_REGISTER.csv row PKG-025 |
| REQ-025-04-11 | Applicable interface types to be addressed in vendor design: Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. | PACKAGE_REGISTER.csv row PKG-025 |
| REQ-025-04-12 | Motor nameplate horsepower rating: TBD pending human ruling. Title basis is 5,000 HP (workbook); DBM states 6,700 hp with unresolved 7,000 hp legacy conflict. The accepted final value shall govern motor sizing and VFD continuous current selection. | PACKAGE_REGISTER.csv; DBM lines 893, 1086, 2196 |
| REQ-025-04-13 | Shop-fabricated wiring within the package shall be conduit and wire suitable for the applicable area classification; control signals shall be wired to skid-mounted remote I/O panels where applicable. | DBM line 2997 |
| REQ-025-04-14 | Equipment doors of the housing building shall be sized for, or include removable transom sections to allow, removal of the largest single equipment item. (Interface requirement on the building; vendor shall confirm largest-component envelope.) | DBM line 2979 |
| REQ-025-04-15 | Harmonic distortion limits, input/output filter requirements, and power-quality compliance: TBD. Not stated in accessible source slice. | location TBD |
| REQ-025-04-16 | Cooling method, efficiency class, redundancy, and bypass configuration: TBD. Not stated in accessible source slice. | location TBD |

## Standards

| Standard / Code | Applicability | Source |
|---|---|---|
| Canadian Electrical Code (CEC) | Spacing, installation, grounding sizing; large oil-filled transformer spacing; grounding conductor sizing | DBM lines 2949, 2991 |
| NEMA VE2 | Cable tray support where no detail is included | DBM line 3017 (location TBD for VFD-specific clauses) |
| CSA enclosure types (Type 12 indoor general purpose; Type 4X outdoor non-hazardous; hazardous-area-approved methods) | Enclosure selection per location | DBM line 2981 |
| `26020-Package_Requirements.docx` | Referenced authoritative package-requirements specification (Workbook Packages row 27). Locally inaccessible as readable text; clause-level requirements TBD until extracted. | `_REFERENCES.md`; source listing |
| IEEE 519 / harmonic standards | Likely applicable to MV VFD power-quality boundary. ASSUMPTION: likely applicable. Clause-level adoption TBD. | ASSUMPTION |

## Verification

| Verification Item | Method | Linked Requirement |
|---|---|---|
| Starting/transfer function | Factory acceptance test (FAT) demonstrating starting profile and synchronous transfer logic; on-site commissioning test against MCC-8200 transfer scheme. | REQ-025-04-01, REQ-025-04-04 |
| Voltage compatibility | Nameplate verification; insulation/withstand test reports. | REQ-025-04-02 |
| Building/HVAC integration | Vendor-EPC integration review confirming enclosure fit, cable entry, and HVAC heat-load coordination. | REQ-025-04-03 |
| No PFC capacitors on transfer bus | Drawing review of MCC-8200 single line; vendor design submittal review. | REQ-025-04-05 |
| Cable basis | Vendor cable schedule review against DBM Cable Specifications table. | REQ-025-04-06 |
| Zone 2 motor marking | Motor nameplate inspection where applicable. | REQ-025-04-07 |
| Grounding interface | Construction verification of 100 A NGR coordination; protective-relay coordination study sign-off. | REQ-025-04-08 |
| Vendor design basis & datasheet | Document submittal review under DEL-025-05 Vendor Document Turnover and DEL-025-06 EPC Review and Acceptance. | REQ-025-04-09 |
| Interface coverage | EPC Interface Register cross-check (`26020-Packages_Interfaces_4_export.xlsx` once accessible). | REQ-025-04-11 |
| Motor rating resolution | Human ruling captured before final VFD continuous-current selection; documented in EPC Package Datasheet (DEL-025-02). | REQ-025-04-12 |
| Harmonic / power quality | TBD method pending REQ-025-04-15 closure. | REQ-025-04-15 |

## Documentation

Vendor shall produce, and EPC Integrator shall review/accept (DEL-025-06), at minimum:

- Vendor engineered physical equipment package (the equipment itself with manufacturer's data tag) — `_CONTEXT.md` anticipated artifacts.
- Vendor package design basis — `_CONTEXT.md` anticipated artifacts.
- Vendor package datasheet set — `_CONTEXT.md` anticipated artifacts.
- Vendor document register / submittals — interface with DEL-025-05 Vendor Document Turnover Package — DELIVERABLE_REGISTER.csv DEL-025-05.
- Test/inspection evidence (FAT, on-site commissioning) — interface with DEL-025-06 — DELIVERABLE_REGISTER.csv DEL-025-06.
- Turnover records — interface with DEL-025-05 — DELIVERABLE_REGISTER.csv DEL-025-05.
- Detailed clause-level documentation deliverable list from `26020-Package_Requirements.docx`: TBD pending source extraction.
