# Guidance — DEL-090-01 Scope of Work (PKG-090 Vapour Recovery Unit 3-25)

> Directional document. Rationale drawn from sources; otherwise `TBD`. Inferences labelled `ASSUMPTION`.

## Purpose

PKG-090 is the 03-25 vapour recovery service: two electric-drive, lead-lag rotary-vane compressor packages that collect vapours from condensate and produced-water tank systems and selected process vents, and route them to 04-25 SOC suction under SCA-002. The Scope of Work deliverable exists to give the EPC Integrator and Package Vendor a single anchored statement of what the package is, what it does, where its boundary sits inside the 03-25 facility, and who owns what. It is the Gate 5 EPC anchor for the package and the upstream basis for the Package Datasheet (DEL-090-02), Construction Work Package (DEL-090-03), Vendor Engineered Equipment Package (DEL-090-04), Vendor Document Turnover (DEL-090-05), and Vendor Package Review and Acceptance (DEL-090-06).
Source: DBM SEC-06 §Vapour Recovery; PACKAGE_REGISTER.csv row 100; DELIVERABLE_REGISTER.csv rows 564–569.

## Principles

- **Source authority.** PKG-090 scope is anchored in the project DBM (SEC-06 §Vapour Recovery) and PACKAGE_REGISTER row 100. Wording in the Scope of Work that goes beyond these sources must be labelled `ASSUMPTION` or marked `TBD` until the corresponding vendor RFQ source slice is accessible. (Source: deliverable-local authority hierarchy; `_REFERENCES.md`.)
- **SCA-002 governs discharge routing.** No local 03-25 SOC. VRU discharges to 04-25 SOC suction. (Source: DBM SEC-01 supersession; SEC-06.)
- **2 x 100% lead-lag, single building.** Redundancy by parallel trains, not standby spares. (Source: PACKAGE_REGISTER row 100; DBM SEC-06.)
- **Sour service governs material/equipment selection.** Detailed materials selection sits in DEL-090-04; the Scope of Work flags the service category. (Source: PACKAGE_REGISTER row 100; DBM SEC-06.)
- **Ownership split is not negotiable inside this Scope of Work.** Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and facility-level coordination. (Source: PACKAGE_REGISTER row 100 §Ownership.)

## Considerations

- **Capacity basis is not yet source-grounded locally.** The bid-docs file `Bid Docs/Budgetary/26020-03-PT-RFQ-12-001_VRU_1_R0.docx` referenced by the package register row was not located under `_Sources/`. Capacity, suction/discharge pressures, and turndown values are `TBD` pending source access. Avoid populating these with values drawn from convention or sibling packages. (Source: `_REFERENCES.md`; PACKAGE_REGISTER row 100.)
- **Package heading 43 in `26020-Package_Requirements.docx` is not locally extracted as text.** Specific tagged equipment numbers and any package-level documentation requirements stated there are `TBD` until the heading is extracted or the docx is converted. (Source: `_REFERENCES.md`; PACKAGE_REGISTER row 100.)
- **Interface coordination spans many disciplines.** Thirteen interface types apply (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). Each interface must trace from the Scope of Work narrative into the INTERFACE_REGISTER entries for PKG-090 to keep facility-side integration auditable. (Source: PACKAGE_REGISTER row 100.)
- **Objective association is heuristic.** OBJ-002…OBJ-010 are inherited via the package-grouping heuristic from the decomposition; treat as `ASSUMPTION` until a deliverable-level objective map confirms. (Source: OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC; DELIVERABLE_REGISTER.csv row 564.)
- **VRU suction interacts with both LP flare and LP fuel gas.** The header has an LP-flare bypass V-ball valve and an LP fuel-gas blanket regulator; both behaviours must be reflected in interface scope and P&ID basis. (Source: DBM SEC-06 §Vapour Recovery; SEC-07 §Fuel Gas.)

## Trade-offs

- **2 x 100% versus a single train with spare.** The accepted basis is 2 x 100% lead-lag in one building. Rationale beyond the source statement: `TBD`. (Source: DBM SEC-06 §Vapour Recovery; PACKAGE_REGISTER row 100.)
- **Discharge to 04-25 SOC versus retaining local 03-25 SOC.** SCA-002 removed the local 03-25 SOC; the Scope of Work must align with that decision and not reintroduce local SOC scope. (Source: DBM SEC-01 supersession.)
- **Vendor-package autonomy versus EPC integration.** Detail engineering and equipment-package design rest with the Package Vendor; pulling that scope back into EPC integration would conflict with the ownership statement in PACKAGE_REGISTER row 100. (Source: PACKAGE_REGISTER row 100 §Ownership.)

## Examples

- **Example interface call-out (Process Piping):** Package-side VRU suction header tie-in to facility LP flare bypass and tank/vent collection headers; tie-in location and rating defined by detailed design. Source: DBM SEC-06 §Vapour Recovery.
- **Example responsibility statement:** "The Package Vendor shall supply two (2) complete 100% capacity VRU compressor packages in lead-lag configuration for sour service, both housed in one building. The EPC Integrator shall integrate these packages into the 03-25 facility, including all listed interface types." Source: PACKAGE_REGISTER row 100.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-090-01 | Capacity / sizing values not source-grounded locally. | `_REFERENCES.md` (notes bid docs not copied locally) | PACKAGE_REGISTER.csv row 100 (references `26020-03-PT-RFQ-12-001_VRU_1_R0.docx`) | Datasheet §Conditions; Specification R-090-11 | PROPOSAL: leave values as `TBD` until vendor RFQ slice accessible | TBD |
| C-090-02 | Detailed scope items SOW-0249..0252 referenced by `_CONTEXT.md` but the source text was not located in accessible sources. | `_CONTEXT.md` §Covers Scope Items | `_Sources/` (no scope-item table located) | Specification R-090-09 | PROPOSAL: hold mapping in deliverable; require source access before expanding text | TBD |
| C-090-03 | Objective association OBJ-002…OBJ-010 derived via package heuristic, not by explicit deliverable-level mapping. | DELIVERABLE_REGISTER.csv row 564 | OBJECTIVE_DELIVERABLE_MAP.csv (not inspected for explicit row) | Datasheet §Identification | PROPOSAL: retain as ASSUMPTION until objective map confirms a per-deliverable row | TBD |
