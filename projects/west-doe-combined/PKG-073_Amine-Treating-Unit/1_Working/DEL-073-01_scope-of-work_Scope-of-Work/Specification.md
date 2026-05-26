# Specification — DEL-073-01 Scope of Work (PKG-073 Amine Treating Unit)

## Scope

### In Scope

The EPC Integrator Scope of Work for PKG-073 covers the full package scope of the Amine Treating Unit (ATU) as a distinct flat project package under WBS 01, including:

- Carrying PKG-073 as a vendor-responsible Mechanical package; Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration. (Source: `SCOPE_LEDGER.csv` SOW-0051; `PACKAGE_REGISTER.csv` PKG-073)
- Defining package function, tagged equipment, source basis, boundaries, and whole-facility integration narrative. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-073-01)
- Process function: removing H₂S and CO₂ from sour natural gas via continuous MDEA absorption-regeneration across two modules (Amine Gas Sweetening; Amine Regeneration). (Source: `SCOPE_LEDGER.csv` SOW-0052)
- All facility interfaces listed in `INTERFACE_REGISTER.csv` for PKG-073 (13 interface types — see Datasheet). (Source: `INTERFACE_REGISTER.csv` PKG-073 rows)

### Excluded (By Others)

- Shipping packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs; process water pumps and tanks. (Source: `SCOPE_LEDGER.csv` SOW-0054)
- No additional package-specific exclusions stated in source materials. (Source: `PACKAGE_REGISTER.csv` PKG-073 — "TBD; no package-specific exclusions stated in source materials.")

## Requirements

### R-073-01-01 — Package Identity and Boundary

The Scope of Work shall identify PKG-073 as the Amine Treating Unit at Workbook Packages row 49, WBS 01, tracking number 26020-01-27-001, with Package Vendor / EPC Integrator responsibility split per the Gate 1 responsibility model. (Source: `PACKAGE_REGISTER.csv` PKG-073; OBJ-004)

### R-073-01-02 — Process Function Narrative

The Scope of Work shall state the package process function: continuous MDEA-based absorption-regeneration removal of H₂S and CO₂ from sour natural gas across the Amine Gas Sweetening module and the Amine Regeneration module. (Source: `SCOPE_LEDGER.csv` SOW-0052)

### R-073-01-03 — Tagged Equipment List

The Scope of Work shall include the tagged equipment and package identity list anticipated by `_CONTEXT.md` (Anticipated Artifacts). At minimum, the source-extracted Amine Inlet Filter Coalescer shall be listed with: 2 × 100% configuration; 0.3 micron @ 99.97% rating; single phase; Bandlock Type QOC closure; clean pressure drop < 2 psid. Additional equipment items reside in 26020-Package_Requirements.docx heading 27 (`location TBD` for clause-level text not locally accessible). (Source: `SCOPE_LEDGER.csv` SOW-0053)

### R-073-01-04 — Facility Integration Interfaces

The Scope of Work shall enumerate all in-scope interface types from `INTERFACE_REGISTER.csv` (13 types: Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) and assign the EPC Integrator role for facility-side integration. (Source: `INTERFACE_REGISTER.csv` PKG-073; `PACKAGE_REGISTER.csv` PKG-073)

### R-073-01-05 — Electrical Motor Requirements

Motor specifications carried by the Scope of Work shall require: motors 1–200 HP rated 600 V / 3-phase / 60 Hz; motors above 200 HP rated 4160 V or 6900 V / 3-phase / 60 Hz; all motors 100 HP and above shall be VFD-ready. (Source: `SCOPE_LEDGER.csv` SOW-0054)

### R-073-01-06 — Scope Exclusions Recorded

The Scope of Work shall record the "By Others" exclusions listed in SOW-0054 (shipping, pile installation, tie-in piping, electrical connections, mounting platform and stairs, separate process water pumps/tanks). (Source: `SCOPE_LEDGER.csv` SOW-0054)

### R-073-01-07 — Capacity and Design Conditions Pointer

The Scope of Work shall cite Appendix A for capacity/design throughput and design conditions. The Appendix A content is not locally accessible — `location TBD` until source slice is provided. (Source: `SCOPE_LEDGER.csv` SOW-0054)

### R-073-01-08 — Objective Traceability

The Scope of Work shall preserve traceability to facility objectives OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 per `_CONTEXT.md` ("Supports Objectives") and `DELIVERABLE_REGISTER.csv`. (Source: `_CONTEXT.md`; `OBJECTIVE_REGISTER.csv`; ASSUMPTION — association recorded via PACKAGE_HEURISTIC per `OBJECTIVE_ASSOCIATION_MODE`.)

### R-073-01-09 — Whole-Facility Integration Narrative

The Scope of Work shall include a whole-facility integration narrative describing how the ATU connects to upstream sour gas conditioning, downstream sweet-gas dehydration/processing, and acid-gas handling (e.g., PKG-046 Acid Gas Compressors as the acid-gas downstream consumer per `PACKAGE_REGISTER.csv` PKG-046). (Source: `PACKAGE_REGISTER.csv` PKG-046; ASSUMPTION — downstream linkage inferred from acid-gas reference, not from a deliverable-specific integration source slice.)

## Standards

| Standard / Code Reference | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx heading 27 | Authoritative source basis for ATU package scope | `_Sources/26020-Package_Requirements.docx` (binary; clause text `location TBD`) |
| 26020-Packages_Interfaces_4_export.xlsx, Packages row 49 | Authoritative companion register for package identity, discipline, interfaces | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; row-level data carried in PROJECT_DECOMP) |
| DBM-Deepcut/4-25_Deepcut_DBM.md | Facility design basis providing process and integration context | `PACKAGE_REGISTER.csv` PKG-073 "Word Source Basis" |
| 26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx | Bid-document basis for ATU RFQ | `PACKAGE_REGISTER.csv` PKG-073 (`location TBD` — file not present in `_Sources`) |
| Specific industry standards (e.g., ASME, API, NACE for sour service) | ASSUMPTION: likely applicable to ATU specification; not enumerated in accessible source slices | `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-073-01-01 | Document review — identity fields traceable to `PACKAGE_REGISTER.csv` PKG-073 row |
| R-073-01-02 | Document review — process function statement traceable to SOW-0052 |
| R-073-01-03 | Document review — tagged equipment list compared to SOW-0053 and (when accessible) 26020-Package_Requirements.docx heading 27 |
| R-073-01-04 | Cross-check against `INTERFACE_REGISTER.csv` PKG-073 — every in-scope interface present |
| R-073-01-05 | Document review — motor specification text compared to SOW-0054 |
| R-073-01-06 | Document review — exclusions list compared to SOW-0054 |
| R-073-01-07 | Document review — Appendix A citation present; flagged TBD until appendix accessible |
| R-073-01-08 | Cross-check against `OBJECTIVE_DELIVERABLE_MAP.csv` and `_CONTEXT.md` "Supports Objectives" |
| R-073-01-09 | Integration narrative review by EPC Integrator against companion packages (e.g., PKG-046) |

## Documentation

Per `_CONTEXT.md` (Anticipated Artifacts), the Scope of Work deliverable produces:

- Package scope of work (this Specification together with the Guidance and Procedure)
- Tagged equipment and package identity list (Datasheet sections "Identification" and "Construction")
- Package function and integration narrative (Specification Scope and R-073-01-09; Guidance Purpose/Principles)
- Responsibility assignment record (Specification R-073-01-01; Guidance Principles)
