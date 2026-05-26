# Guidance: DEL-100-03_construction-work-package — Construction Work Package

## Purpose

This guidance directs the EPC Integrator in producing the Construction Work Package for PKG-100 (Hydrogen Peroxide Sweetening Unit). The deliverable exists because the H2O2 sweetening package is a vendor-supplied skid that must be physically integrated into the 03-25 facility — foundations, building, piping, electrical, controls, fire/gas, drains, lighting, EHT, grounding, and access must all be planned and executed at the field-construction level even though the package internals are not in EPC scope. (Source: DELIVERABLE_REGISTER.csv row DEL-100-03; PACKAGE_REGISTER.csv row PKG-100.)

## Principles

- **Vendor / Integrator boundary is non-negotiable.** The Package Vendor owns package engineering, package design, vendor documentation, and physical equipment supply. The EPC Integrator owns integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Do not pull vendor design into the Construction Work Package. (Source: PACKAGE_REGISTER.csv PKG-100; OBJECTIVE_REGISTER.csv OBJ-004.)
- **"By others" is EPC-Integrator construction scope, not unowned scope.** SOW-0110 names interconnecting piping, DCS integration, foundations, and electrical supply to MCC as "by others" relative to the vendor package — meaning they are this Construction Work Package's scope. (Source: SCOPE_LEDGER.csv SOW-0110.)
- **Carry every workbook interface fact.** All 13 PKG-100 interfaces in INTERFACE_REGISTER.csv must be visible in the construction interface checklist. Omitting an interface fact is a quality failure. (Source: INTERFACE_REGISTER.csv rows for PKG-100; OBJECTIVE_REGISTER.csv OBJ-005, OBJ-006, OBJ-007, OBJ-008.)
- **Sour-service handling matters.** OBJ-009 carries sour-service, relief/flare, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory requirements into the package. The construction plan, tie-ins, and inspection checklists shall reflect this. (Source: OBJECTIVE_REGISTER.csv OBJ-009.)
- **Source fidelity over convention.** Where the 26020 Word source heading 52 is referenced but only available via decomposition extracts (SOW-0107…SOW-0110), do not invent values; cite the extract and mark precise location TBD when the underlying Word slice is not directly readable.

## Considerations

- **Self-framing building.** SOW-0109 calls for a self-framing building erected at site. Plan the building foundation, anchor design (TBD pending vendor design), lifts, weather closure for winter erection, and turnover separately from the package skid. (Source: SCOPE_LEDGER.csv SOW-0109.)
- **Winterization basis.** Ambient design is -40 °C min / +35 °C max. Building heating, EHT for H2O2 and sour-water lines, insulation, and freeze protection for the 400 BBL H2O2 tank are construction-scope considerations even where the vendor sizes the EHT load. (Source: SCOPE_LEDGER.csv SOW-0110; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-02-area equivalents.)
- **MCC / motor termination convention.** Per DBM-Comp_and_Liquids SEC-12, the field construction contractor hard-wires local control stations (H-O-A or On-Off) adjacent to each motor back to the MCC motor-starter circuit. Plan the termination scope and inspection holdpoints accordingly. (Source: DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12.)
- **DCS integration.** "By others" per SOW-0110, but the field tie-in, terminations at the DCS marshalling cabinets, loop checks, and SAT scope are construction-scope responsibilities; coordinate with the controls/I&C package owner.
- **Sparing, isolation, maintenance access.** OBJ-010 calls for handoff-readiness evidence including sparing, isolation, winterization, vendor documentation, commissioning, turnover, and open-item closure. Construction's turnover package should index these items even if many are vendor-supplied. (Source: OBJECTIVE_REGISTER.csv OBJ-010.)
- **H2O2 material compatibility.** H2O2 is an oxidizer; specific materials, gasketing, contamination control, and spill containment requirements apply. Specific values are TBD because they require vendor data and a sour-service / oxidizer-service materials specification that is not in the locally readable source slices.

## Trade-offs

- **Detail now vs. vendor-driven detail later.** Many parameters (pump capacity, design conditions, materials) are explicitly "Vendor to design" or TBC in SOW-0110. The Construction Work Package should structure placeholders and open-item flags rather than freeze invented values.
- **Field construction by contractor vs. document ownership by EPC Integrator.** Gate 7 assigns deliverable ownership to the EPC Integrator. The 3-25 DBM does not name a separate "construction responsibility" the way the 4-25 (Deepcut) DBM does, but the Construction Scope Summary lists the facility construction scope. (ASSUMPTION: in the absence of a stated contractor in the 3-25 DBM for this package's construction, treat the field-execution contractor as TBD and reflect that in the responsibility matrix.)
- **Building scope partitioning.** The self-framing building could be vendor-erected or contractor-erected. SOW-0109 states the building is to be erected at site but does not explicitly assign erection party; treat as ASSUMPTION (contractor-erected as part of construction scope) unless vendor scope says otherwise.

## Examples

- **Interface checklist row pattern.** "Interface: Drain / Containment. Source fact: IFC-DB6DD6511D (workbook Packages row 63). Action: route package equipment drains and spill containment to facility produced-water / contaminated drain network per facility drain plan (location TBD). Verification: walk-down and turnover form (TBD)."
- **`By others` workface row pattern.** "Item: Electrical supply to MCC. Source: SOW-0110. Scope: pull and terminate 600V feeder from 600V MCC to package skid termination box; coordinate breaker, cable, and lugs against vendor electrical termination drawing. Verification: cable test record; loop check; energization record."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-100-03-01 | Construction-execution responsibility for PKG-100 is unstated. The Deepcut DBM (4-25) explicitly assigns field construction to Tourmaline Oil Corporation; the Comp_and_Liquids DBM (3-25) does not contain an equivalent assignment in the locally accessible slices. PKG-100 is a 3-25 (WBS 03) package. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (Construction Scope Summary lists scope but not contractor) | DBM-Deepcut/4-25_Deepcut_DBM.md (Construction Responsibility — 04-25 only) | Datasheet Construction; Specification CWP-100-004; Guidance Trade-offs | Treat the field-execution contractor as TBD for 03-25 PKG-100; the EPC Integrator owns the deliverable; the responsibility matrix in the Construction Work Package must record contractor as TBD. | TBD |
| CFL-100-03-02 | SOW-0110 names "foundations" and "electrical supply to MCC" as "by others" (i.e., not in the vendor package) but does not explicitly identify a foundation designer or load source. | SCOPE_LEDGER.csv SOW-0110 | PACKAGE_REGISTER.csv PKG-100 (responsibility split silent on foundation engineer) | Specification CWP-100-005; CWP-100-010 | Foundation engineering is EPC-Integrator scope under the package-integration responsibility; vendor must supply equipment loads, anchor bolt patterns, and dynamic data as inputs. Mark vendor-data dependency in the open-item register. | TBD |
| CFL-100-03-03 | Source for clause-level standards (e.g., CSA Z662 sour service, NBC, building code) is not directly readable from the 26020 Word source slice locally; only decomposition extracts and DBM narrative are accessible. | 26020-Package_Requirements.docx package heading 52 (binary, not directly readable) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-15 (referenced but specific clauses not extracted locally) | Specification Standards | Cite the source and mark `location TBD` for clause-level requirements until Word source extracts are made available. | TBD |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Facility Overview; Construction Scope Summary; SEC-04 (Produced water / H2O2); SEC-12 (Electrical Basis / 600V MCC).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, row `PKG-100`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`, rows `SOW-0107`–`SOW-0110`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, rows for `PKG-100`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv`, rows `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`.
