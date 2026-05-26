# Specification: DEL-045-01_scope-of-work — Scope of Work

## Scope

This Specification defines the normative requirements for the EPC Integrator's Scope of Work deliverable for PKG-045 "Instrumentation (outside of Mechanical Packages only)" at the West Doe complex (workbook row 47; WBS 03; CoA tracking 26020-01-32-002).

**In scope:**
- Authoring a package-level Scope of Work covering the tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative for instrumentation that is not delivered inside vendor mechanical packages.
- Recording the responsibility assignment for the package.
- Establishing package boundaries against the five active interface counterparts: Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network.

**Out of scope:**
- Detailed instrumentation design, datasheets, loop drawings, cause-and-effect logic, and discipline production deliverables — these are carried under DEL-045-02 (Package Datasheet), DEL-045-03 (Construction Work Package), and DEL-045-04 (EPC/Discipline Production Package).
- Instrumentation that is delivered inside the boundary of a vendor mechanical package (excluded by the package title itself).
- Local 03-25 instrument-air compressor scope (superseded by SCA-006; supplied from 04-25). [Source: 3-25_Comp_and_Liquids_DBM.md]
- Package-specific exclusions beyond the above: TBD; none stated in the source materials available locally. [Source: PACKAGE_REGISTER.csv]

## Requirements

| Req ID | Requirement | Basis / Source |
|---|---|---|
| R-045-01-01 | The Scope of Work shall identify the package by name, workbook ID (45), workbook row (47), CoA tracking number (26020-01-32-002), WBS (03), and discipline (Instrumentation). | PACKAGE_REGISTER.csv |
| R-045-01-02 | The Scope of Work shall enumerate the tagged equipment and package identity list (artifact ART-F40323895F) for instrumentation outside vendor mechanical packages, using source-supported tags only. | ARTIFACT_REGISTER.csv; PACKAGE_REGISTER.csv |
| R-045-01-03 | The Scope of Work shall include a package function and whole-facility integration narrative (artifact ART-F820619A3E) describing what the package does and how it integrates into the process facility. | ARTIFACT_REGISTER.csv |
| R-045-01-04 | The Scope of Work shall include a package responsibility assignment record (artifact ART-34E643FBEB) identifying EPC Integrator responsibility, or discipline-subcontractor responsibility where source-supported. | ARTIFACT_REGISTER.csv; PACKAGE_REGISTER.csv |
| R-045-01-05 | Package boundaries shall be defined against each active interface type: Process Piping (IFC-33F8A9F366), Utility Piping (IFC-AE76B11E50), Electrical Power (IFC-2D030CA850), I&C / Control Cabling (IFC-210F46B073), Communications / Network (IFC-9DAC4D3C4D). | INTERFACE_REGISTER.csv |
| R-045-01-06 | The Scope of Work shall record the Gate 6 disposition that, under the plug-n-play package philosophy, instrumentation field supports, power, and communications are included in each package scope as appropriate. | INTERFACE_REGISTER.csv (Note) |
| R-045-01-07 | Environmental basis: instrumentation, control panels, and field devices addressed by the Scope shall be qualified to a minimum ambient of -40 deg C unless a more severe process or vendor condition applies. | 3-25_Comp_and_Liquids_DBM.md |
| R-045-01-08 | The Scope of Work shall reflect the SCA-006 disposition that instrument air for 03-25 is supplied from 04-25; no local 03-25 instrument-air compressor controls scope shall be added. The 03-25 instrument-air interface (393 SCFM TBC; combined 1,113 SCFM TBC) shall be carried as an interface item to be monitored. | 3-25_Comp_and_Liquids_DBM.md |
| R-045-01-09 | Power-and-control separation shall be carried: power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. | 3-25_Comp_and_Liquids_DBM.md |
| R-045-01-10 | All requirements, design values, and equipment statements in the Scope of Work shall be source-grounded; statements lacking source support shall be marked TBD; inferences shall be labelled ASSUMPTION. | docs/CONTRACT.md K-PROV-1 (ASSUMPTION at the contract-citation level: governs all source-grounded artifacts) |
| R-045-01-11 | The Scope of Work shall cite its accepted upstream decomposition snapshot: GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP. | _REFERENCES.md |
| R-045-01-12 | The Scope of Work shall be authored as an integrator-authored document (ART-E7B3409573 type "EPC Scope of Work"). | ARTIFACT_REGISTER.csv |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| West Doe Compressor Station and Liquids Hub DBM (3-25) | Site/utility/electrical/instrumentation basis for 03-25 scope | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Workbook Packages row 47 | Authoritative package definition and interface marks | location TBD (slice not locally copied) |
| SCA-006 (Scope Change Authorization) | Establishes instrument-air supply allocation between 03-25 and 04-25 | Cited in DBM; full SCA-006 text location TBD |
| Project electrical specification (for power/control separation) | Detailed routing/shielding/grounding rules referenced by DBM | location TBD |
| External instrumentation codes/standards (e.g., ISA, IEC, CSA) | TBD: not enumerated in available source slices for PKG-045 | TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-045-01-01 | Inspection — header fields match PACKAGE_REGISTER.csv row for PKG-045. |
| R-045-01-02 | Inspection — tagged equipment list cross-checked against source rows; non-source-supported tags are not listed. |
| R-045-01-03 | Review — integration narrative explains process role and facility-level role; reviewed against DBM facility narrative. |
| R-045-01-04 | Inspection — responsibility record present and consistent with PACKAGE_REGISTER.csv responsibility note. |
| R-045-01-05 | Inspection — boundary table present for all five active interface IDs. |
| R-045-01-06 | Inspection — Gate 6 disposition recorded with citation. |
| R-045-01-07 | Review — environmental clause present and consistent with DBM site basis. |
| R-045-01-08 | Inspection — SCA-006 instrument-air disposition recorded with cited demand values and "no local compressor controls" statement. |
| R-045-01-09 | Inspection — power/control separation clause present, citing DBM. |
| R-045-01-10 | Audit — every non-trivial claim either cites a source (SourcePath + SectionRef) or is marked TBD/ASSUMPTION. |
| R-045-01-11 | Inspection — accepted upstream snapshot path cited in document references. |
| R-045-01-12 | Inspection — document type marked "EPC Scope of Work". |

## Documentation

The following artifacts shall be produced under this deliverable (per ARTIFACT_REGISTER.csv):

- ART-E7B3409573 — Package scope of work
- ART-F40323895F — Tagged equipment and package identity list
- ART-F820619A3E — Package function and whole-facility integration narrative
- ART-34E643FBEB — Package responsibility assignment record
