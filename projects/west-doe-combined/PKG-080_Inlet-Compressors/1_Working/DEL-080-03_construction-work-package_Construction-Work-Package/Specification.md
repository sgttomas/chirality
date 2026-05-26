# Specification: DEL-080-03 — Construction Work Package (Inlet Compressors)

## Scope

This Construction Work Package (CWP) governs the EPC Integrator's scope to **physically install, build, inspect, tie-in, turn over, and integrate** the PKG-080 Inlet Compressors package into the larger 03-25 facility. (Source: DELIVERABLE_REGISTER.csv row 362; PROJECT_DECOMP.md L127)

**Covers:**
- Receipt, set, alignment, and grouting of the two vendor-supplied modular reciprocating compressor packages (Ariel KBZ/6 basis; equipment tags KM-2150 and KM-2250). (Source: SCOPE_LEDGER.csv SOW-0121; DBM-Comp_and_Liquids §inlet compression / §prime movers)
- Reassembly of modular split pieces (three pieces per package) into self-framing buildings on prepared foundations. (Source: DBM-Comp_and_Liquids §inlet compression)
- Field execution of all package-to-facility tie-ins covering the thirteen declared interface types listed in §Requirements. (Source: INTERFACE_REGISTER.csv rows 512-524)
- Field inspection, mechanical completion, pre-commissioning support, and turnover documentation to facility operations. (Source: DELIVERABLE_REGISTER.csv row 362 anticipated artifacts: "installation and tie-in workface plan; construction interface and turnover checklist")
- Construction-side coordination with DEL-080-04 (Vendor Engineered Equipment Package), DEL-080-05 (Vendor Document Turnover Package), and DEL-080-06 (EPC Vendor Package Review and Acceptance). (Source: DELIVERABLE_REGISTER.csv rows 363-365)

**Excludes:**
- Vendor package engineering, design, and fabrication (those scopes are owned by the Package Vendor under DEL-080-04). (Source: PACKAGE_REGISTER.csv row 66 responsibility narrative)
- Process design of upstream/downstream facility scope outside the package battery limits. (ASSUMPTION: derived from the EPC vs. Package Vendor split in PACKAGE_REGISTER.csv row 66.)
- Vendor document register production (DEL-080-05). (Source: DELIVERABLE_REGISTER.csv row 364)

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-1 | The CWP shall describe receiving, setting, anchoring, and grouting of two Ariel KBZ/6 separable two-stage reciprocating compressor packages, modularized for shop assembly and field re-assembly from three pieces each. | SCOPE_LEDGER.csv SOW-0121; DBM-Comp_and_Liquids §inlet compression |
| R-2 | The CWP shall plan tie-ins for all thirteen declared package interfaces: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv rows 512-524; PACKAGE_REGISTER.csv row 66 |
| R-3 | The CWP shall maintain materials and seal selection consistent with NACE-compliant sour-service requirements stated for the package. | SCOPE_LEDGER.csv SOW-0122 |
| R-4 | Electrical tie-in scope shall accommodate 4,000 V, three-phase, 60 Hz supply to each compressor motor (KM-2150, KM-2250) rated 3,878 kW / 5,200 hp, with starting VFD per SCA-001 VE #34; soft starts shall not be used for these motors. | DBM-Comp_and_Liquids §electrical / §prime movers |
| R-5 | The CWP shall include an installation and tie-in workface plan and a construction interface and turnover checklist as deliverable artifacts. | DELIVERABLE_REGISTER.csv row 362 anticipated artifacts |
| R-6 | The CWP shall provide mechanical completion and turnover evidence supporting EPC Vendor Package Review and Acceptance (DEL-080-06). | DELIVERABLE_REGISTER.csv row 365 |
| R-7 | The CWP shall preserve package configuration of 2 x 50% with no installed spare; field changes that alter unit count or rated capacity are not permitted without scope change. | SCOPE_LEDGER.csv SOW-0122 |
| R-8 | The CWP shall accommodate process tie-in conditions of approximately 1275 kPag suction and 6550 kPag discharge per unit and 80 MMSCFD combined facility throughput. | SCOPE_LEDGER.csv SOW-0122 |
| R-9 | Site civil/foundation, climatic loads, seismic, and permit basis | TBD — location TBD (not stated in accessible source slices) |
| R-10 | Specific welding, NDE, and pressure-test procedures for tie-in piping | TBD — to be derived from vendor package documentation (DEL-080-04/05) and project welding/QA specification (location TBD; ASSUMPTION: separate facility-wide welding & NDE spec exists) |

## Standards

| Standard / Governing Document | Applies To | Location |
|---|---|---|
| NACE materials standards (sour service) | R-3 materials and seals | location TBD (referenced as "NACE-compliant" in SCOPE_LEDGER.csv SOW-0122; specific NACE document not cited in accessible sources) |
| NEMA MG1 (motor enclosure / construction) | R-4 electrical tie-in interface | DBM-Comp_and_Liquids §electrical (NEMA MG1 compliance stated); clause TBD |
| SCA-001 VE #34 (starting VFD requirement) | R-4 | DBM-Comp_and_Liquids §electrical |
| SCA-001 VE #37 (capacitor bank removal where VFDs present) | R-4 electrical tie-in considerations | DBM-Comp_and_Liquids §electrical |
| Project welding, NDE, and pressure-test specifications | R-2 piping tie-ins | location TBD (not present in accessible source slices) |
| Project HSE / construction safety standards | All field execution | location TBD |
| 26020-Package_Requirements.docx (package heading 33) | Package-level requirements basis | `_Sources/26020-Package_Requirements.docx` (binary; clause-level text not extracted this run; location TBD at clause level) |

## Verification

| Req | Verification Method |
|---|---|
| R-1 | Receiving inspection records; foundation survey; alignment and grouting QC records; module reassembly checklist signoff. |
| R-2 | Interface walkdown against the thirteen interface types; tie-in punchlist; per-interface turnover sign-off in the construction interface and turnover checklist. |
| R-3 | Material certification (MTR) review against NACE basis; weld procedure qualification reviews for sour service; ASSUMPTION: project welding spec governs procedure qualification. |
| R-4 | Electrical commissioning checks at MCC-8200 4160 V bus (per DBM §electrical); motor protection and VFD pre-energization checks. (Source: DBM §electrical) |
| R-5 | Document deliverable check at CWP submission. |
| R-6 | Mechanical completion certificate; turnover package handover log to operations; alignment with DEL-080-06 acceptance checklist. |
| R-7 | Configuration audit prior to mechanical completion. |
| R-8 | Pressure-test records on tie-in piping; PSV setpoint check against discharge basis (PSV scope TBD — interfaces with Relief / Flare / Vent). |
| R-9 | TBD — pending site basis. |
| R-10 | TBD — pending project welding/QA specification. |

## Documentation

The CWP shall deliver (anticipated artifacts per DELIVERABLE_REGISTER.csv row 362):

- Construction work package (this document set).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (covering all thirteen interface types per INTERFACE_REGISTER.csv rows 512-524).

Supporting records to be retained (ASSUMPTION: standard EPC construction record set):
- Receiving inspection logs.
- Foundation acceptance records.
- Alignment, grouting, and bolting records.
- Welding procedure logs and NDE reports for tie-in piping.
- Pressure-test certificates.
- Electrical pre-energization and protection-test records.
- Mechanical completion certificate.
- Turnover dossier to operations.
