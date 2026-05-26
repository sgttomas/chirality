# Datasheet: DEL-100-03_construction-work-package — Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-100-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-100 — Hydrogen Peroxide Sweetening Unit |
| Parent workbook row | Workbook Packages row 63 |
| CoA tracking number | 26020-03-27-001 |
| WBS | 03 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope items | SOW-0107; SOW-0108; SOW-0109; SOW-0110 |
| Supported objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — best-effort PACKAGE_HEURISTIC mapping from `_CONTEXT.md`; package-grouped, not deliverable-level confirmed) |

## Attributes

| Attribute | Current value | Source |
|---|---|---|
| Facility/WBS basis | WBS 03 / 03-25 Compressor Station and Liquids Hub facility basis | PACKAGE_REGISTER.csv row PKG-100; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-01 |
| Package function | Sour water hydrogen peroxide treatment package: sour water is sent to the static mixer and then to the Hydrogen Peroxide Reactors for treatment; hydrogen peroxide is pumped in from the H2O2 tank by the H2O2 pumps; treated water is then sent to produced water storage tanks. | SCOPE_LEDGER.csv SOW-0108; 26020-Package_Requirements.docx package heading 52 (Basic scope) |
| Major included equipment (vendor-supplied) | Hydrogen Peroxide Pumps (chemical injection pumps); Hydrogen Peroxide Reactors; Static Mixer; 400 BBL Hydrogen Peroxide Storage Tank; self-framing building to be erected at site; additional equipment per PFD | SCOPE_LEDGER.csv SOW-0108, SOW-0109; 26020-Package_Requirements.docx package heading 52 (Basic scope; Major included equipment) |
| Package interfaces (facility-side, EPC Integrator) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv rows for PKG-100; PACKAGE_REGISTER.csv row PKG-100 |
| Items "by others" (not within vendor package) | Interconnecting piping; DCS integration; foundations; electrical supply to MCC | SCOPE_LEDGER.csv SOW-0110 (Scope notes and open items) |
| Construction responsibility basis | Construction scope (the field-execution scope for the 03-25 facility) includes construction management, grading, piling, foundations, roads, field buildings, offloading and setting of modules, mechanical hookups, installation of shipped-loose instruments and valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security systems, control room and maintenance systems, potable and septic utilities, non-process building heating and fuel storage, and demolition/removal where required for the project tie-ins. EPC Integrator is the deliverable owner per Gate 7. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Construction Scope Summary; DELIVERABLE_REGISTER.csv row DEL-100-03 |
| Deliverable artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row DEL-100-03; ARTIFACT_REGISTER.csv rows for PKG-100 |
| Vendor / EPC split | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package. EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv row PKG-100; OBJECTIVE_REGISTER.csv OBJ-004 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Treatment package throughput | 24,154 BBL/D (≈ 160 m³/h). | SCOPE_LEDGER.csv SOW-0110; 26020-Package_Requirements.docx package heading 52 (Scope notes and open items) |
| H2O2 storage tank capacity | 400 BBL (one tank). | SCOPE_LEDGER.csv SOW-0109, SOW-0110; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04 (H2O2 storage) |
| H2O2 pump capacity | TBC; Vendor to design. | SCOPE_LEDGER.csv SOW-0110 |
| Sour water operating temperature | 9 °C. | SCOPE_LEDGER.csv SOW-0110 |
| Sour water operating pressure | 340.54 kPag. | SCOPE_LEDGER.csv SOW-0110 |
| Sour water operating flow rate | 160 m³/h (24,154 BBL/D). | SCOPE_LEDGER.csv SOW-0110 |
| Ambient design temperature | -40 °C min, +35 °C max. | SCOPE_LEDGER.csv SOW-0110 |
| Design conditions (process/mechanical) | TBC; Vendor to confirm. | SCOPE_LEDGER.csv SOW-0110 |
| Driver basis | All pumps driven by 575V / 3PH / 60 Hz motors; starting method DOL or VFD; local control via H-O-A or On-Off switch; electric motor fed from 600V MCC. | SCOPE_LEDGER.csv SOW-0110 |
| H2O2 supply source | Hydrogen peroxide supplied from onsite tanks. | SCOPE_LEDGER.csv SOW-0110 |
| Sour-service / safety basis | Carries sour-service, relief/flare, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory requirements per Gate 7 objective basis. | OBJECTIVE_REGISTER.csv OBJ-009 |

## Construction

| Construction topic | Current basis |
|---|---|
| Work package boundary | Covers the PKG-100 Hydrogen Peroxide Sweetening Unit construction work package for physical installation, construction, inspection, turnover, and tie-in to larger facility systems. The vendor-supplied skid/package and self-framing building are installed by the construction contractor; package internal engineering and equipment remain Vendor scope. |
| Included field activities | Foundations for the package and the self-framing building; offloading and setting of the package skid and major equipment (H2O2 pumps, reactors, static mixer, 400 BBL H2O2 tank); erection of the self-framing building at site; ISBL/OSBL interconnecting process and utility piping tie-ins ("by others" relative to the vendor package per SOW-0110); home-run cabling and terminations from 600V MCC to the package motors, and to local control stations (H-O-A / On-Off); grounding/bonding, EHT, area/exterior lighting, building HVAC/services, fire & gas devices, and I&C / control cabling for the listed package interfaces. Source: DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Construction Scope Summary; SCOPE_LEDGER.csv SOW-0110; INTERFACE_REGISTER.csv rows for PKG-100. |
| Interface controls | Must address every PKG-100 interface listed above (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). |
| Local control stations | One local control station adjacent to each motor (H-O-A or On-Off as applicable), hard-wired back to the motor starter circuit in the MCC by the field construction contractor. Source: DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 (600V MCC narrative). |
| DCS integration | "By others" relative to the vendor package per SOW-0110; the construction work package shall plan the tie-ins, terminations, and loop checks required to integrate the vendor package into the 03-25 facility DCS. |
| Quantities and coordinates | TBD; not provided in locally accessible source slices for this deliverable. |
| Inspection and turnover forms | TBD; source set identifies a checklist artifact but does not provide approved form content. |
| Open vendor design items | Pump capacity (TBC); detailed package design conditions (TBC); H2O2 pump, reactor, and static mixer engineering — all Vendor to design. Source: SCOPE_LEDGER.csv SOW-0110. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`, package heading 52 (Basic scope; Major included equipment; Scope notes and open items) — referenced via decomposition extractions (binary not directly readable; location TBD for exact paragraph anchors).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 63 — referenced via decomposition extractions (binary not directly readable).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Facility Overview; Construction Scope Summary; SEC-04 (Produced water / H2O2 storage and treatment); SEC-12 (Electrical Basis / 600V MCC).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row `DEL-100-03_construction-work-package`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, row `PKG-100`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`, rows `SOW-0107` through `SOW-0110`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, rows for `PKG-100`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`, rows for `PKG-100`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv`, rows `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`.
