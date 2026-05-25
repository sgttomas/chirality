# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-020-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-020` - 13.8kV SWITCHGEAR EQUIPMENT |
| Workbook row | 22 |
| WBS | 01 |
| CoA tracking number | `26020-01-30-011` |
| Discipline | Electrical |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Construction Work Package |
| Scope item | `SOW-0021` |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-020-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-020`.

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | `PACKAGE_REGISTER.csv` row `PKG-020`; Workbook Packages row 22 |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Package scope basis | Workbook-defined vendor-owned Electrical package for '13.8kV SWITCHGEAR EQUIPMENT' under WBS 01, with Package Vendor owning package engineering/design/equipment and EPC Integrator owning facility integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row `PKG-020`; `INTERFACE_REGISTER.csv` rows `IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004` |
| Construction work package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` row `DEL-020-03_construction-work-package`; `ARTIFACT_REGISTER.csv` rows `ART-9A5E2DBA11`, `ART-7343A1CFCD`, `ART-14E7FF268C` |
| Facility role of 13.8 kV switchgear | Plant main power distribution center: designed, purchased, and installed to distribute power to the electrical buildings stationed across the facility. Bus sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section (lines 2917-2919) |
| Source-side feed basis | BC Hydro utility 25 kV supply (TBC) feeds a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer that steps down to local 13.8 kV switchgear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section (line 2917) |
| Load-side radial distribution basis | Radial distribution through step-down transformers to: 6.9 kV Inlet/Sales Compressor Electrical Building; 4.16 kV Acid Gas/Overheads Compressor Electrical Building; 600 V Acid Gas Compressor Electrical Building; 600 V Sales/Overheads Compressor Electrical Building; 4.16 kV/600 V General Area/Tank Farm/Process Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section (lines 2919-2926) |
| System voltage basis | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; this voltage class is used for BC Hydro utility distribution and for the facility backbone distribution to electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table (lines 2933-2934) |
| Grounding basis at utility transformer | The BC Hydro utility transformer is grounded using a 200 A, 10 s neutral grounding resistor and operates as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding section (line 2985) |
| Plant ground grid basis | Driven piles used as ground electrodes interconnected by a main #2/0 green insulated grounding conductor in the highest-voltage carrying tray; all major electrical equipment shall be directly connected to the ground grid at two points. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding section (lines 2987, 2989) |
| MV control / protection power | MV breaker control circuits and MV protective relays are UPS-served (120 VAC / 125 VDC). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` UPS services row (line 2939) |
| MV cable basis | 13.8 kV medium-voltage cables: three-conductor copper TECK cable rated 15 kV with 133 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Cable Specifications table (line 3007) |
| Building / location basis | Electrical buildings are prefabricated, modular buildings located in general purpose areas; they may house 13.8 kV main switchgear among other equipment, as required by detailed design. Building 810-1 is identified in the source equipment list as "13.8kV Switchgear Electrical Building", shop-fabricated. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section (line 2973); equipment list row (line 2811) |
| Equipment quantity (source list) | "Medium Voltage Switchgear" appears in the source equipment list with quantity 1 (ELC-QAS-000007-001). Allocation of this exact line to PKG-020 is ASSUMPTION pending confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical equipment list (line 2880) |
| Construction phasing context | One phase, single train, nominal 300 MMSCFD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction phasing row (line 24) |
| Ambient design implication | The -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. ASSUMPTION: applicable to MV switchgear auxiliaries and exposed cabling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (consistent with project-wide ambient basis as recorded in companion construction-work-package deliverables) |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 04-25 West Doe Deepcut expansion (300 MMSCFD), single train, one construction phase. Field construction is assigned to Tourmaline Oil Corporation; construction management, foundations, module setting, mechanical hookups, cabling, terminations, area lighting, fencing, and tie-in works are within Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility section (lines 101-127) |
| Tie-in coordination | Joint planning is required for tie-ins to existing or related facilities; tie-in timing shall be established as the project progresses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 127 |
| Standby-power scope split | Standby-power scope split, incoming-power metering at the facility boundary, and protection coordination remain to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section (line 2927) |
| Removed 13.8 kV emergency generator concept | The previous centralized 13.8 kV emergency-generator concept has been replaced by TOU low-voltage standby generators with transfer switches at the 600 V MCC level. The 13.8 kV switchgear CWP shall not carry a 13.8 kV emergency-generator tie-in scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2080, 2943 |
| Utility supply uncertainty | The main incoming utility voltage is 25 kV (TBC). Utility configuration, metering point, and protection split are TBD-dependent on utility coordination. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2917 |
| Geotechnical / structural status | Final geotechnical inputs and vendor equipment loads are required before closing foundation, anchorage, frost, and structural-support criteria for the switchgear equipment and its electrical building. | TBD - no explicit geotechnical slice in `4-25_Deepcut_DBM.md` accessible source set; ASSUMPTION carried by analogy with companion construction-work-package deliverables. |
| Standards status | Standards, regulatory references, and project electrical specifications are not fully available in the accessible source set; references that cannot be cited to a workspace location shall be treated as `location TBD` and as verification requirements before final issue for construction. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` general standards posture |

## Construction

| Construction data item | Value |
|---|---|
| Work package boundary | Physical installation, construction, inspection, turnover, and tie-in of the 13.8 kV switchgear package to: the BC Hydro utility transformer secondary feed; the downstream 6.9 kV, 4.16 kV, and 600 V step-down transformers serving the radial distribution to facility electrical buildings; the plant ground grid; MV control cabling; communications/network to plant control; structural foundations/supports; and maintenance access. |
| Workface plan minimum contents | Installation sequence, work area limits, equipment offload/setting of MV switchgear lineups and electrical building modules, tie-in/interface checkpoints (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), inspection points, turnover records, and unresolved `TBD` criteria. |
| Interface checklist minimum contents | Electrical Power tie-in checks (utility-side feed and load-side radial step-down transformers); Grounding / Bonding checks (utility-transformer 200 A neutral grounding resistor, plant ground grid two-point connections); I&C / Control Cabling checks (UPS-served 120 VAC / 125 VDC MV breaker control and protective relay wiring); Communications / Network checks (to plant control); Maintenance Access checks (operating clearances, arc-flash boundaries, lineup withdrawal/maintenance space); Structural / Foundations / Supports checks (switchgear lineup and electrical building 810-1 foundations and supports). |
| Detailed switchgear ratings (bus continuous rating, short-circuit interrupting/withstand, BIL, lineup count, breaker count, breaker type, arc-resistant rating, accessories) | TBD - not defined in accessible source slices; depends on vendor engineered equipment package and detailed electrical studies. |
| Foundation, structural support, and seismic detailing for switchgear lineups and Electrical Building 810-1 | TBD - depends on final geotechnical inputs and vendor equipment loads. |
| Protection / coordination / arc-flash study inputs | TBD - to be confirmed by detailed electrical studies; protection coordination and emergency or standby power scope split are explicitly carried as detailed-engineering items. |
| Utility interface scope split (metering, protection, isolation, telemetry) | TBD - utility voltage carried as 25 kV (TBC) and incoming-power metering at the facility boundary is to be confirmed. |
| Inspection and acceptance criteria | TBD - to be confirmed from IFC electrical drawings, project electrical specifications, vendor commissioning procedures, and protection/coordination studies. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
