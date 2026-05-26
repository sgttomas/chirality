# Specification — DEL-077-03 Construction Work Package (Methanol Injection)

## Scope

### In Scope
The EPC Integrator shall produce a Construction Work Package (CWP) that describes how the PKG-077 Methanol Injection package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. Source: `DELIVERABLE_REGISTER.csv` row DEL-077-03 (Description).

The CWP covers:

1. Physical installation of the vendor-supplied Methanol Injection package (foundations, setting, alignment, levelling, anchoring).
2. Construction tie-ins to all applicable facility interfaces (see Requirements §R-INT).
3. Inspection and quality verification of installation and tie-in work.
4. Mechanical completion, system turnover, and handoff to commissioning.
5. Construction interface coordination with adjacent packages and disciplines.

### Out of Scope (boundary with sibling deliverables under PKG-077)
- Package engineering, package design, vendor documentation, and physical equipment supply — owned by Package Vendor under DEL-077-04 and DEL-077-05. Source: `PACKAGE_REGISTER.csv` PKG-077 ResponsibilityModel.
- Scope-of-work narrative and tagged equipment list — DEL-077-01.
- Package datasheet and vendor handoff basis — DEL-077-02.
- EPC vendor-package review and acceptance — DEL-077-06.

### Exclusions
- TBD — no package-specific exclusions are stated in source materials. Source: `PACKAGE_REGISTER.csv` PKG-077 (Exclusions: "TBD; no package-specific exclusions stated in source materials").

## Requirements

> Each requirement is labeled with provenance. ASSUMPTION items are inferences from authority lower in the chain (decomposition narrative or package-discipline convention). Values requiring source data not locally accessible are marked `TBD (location TBD)`.

### R-RESP — Responsibility Discipline
- **R-RESP-1** The CWP shall preserve the vendor/EPC split: vendor package engineering, design, vendor documentation, and equipment supply remain with the Package Vendor; the EPC Integrator owns integration, interfaces, tie-ins, constructability, and construction/turnover. Source: `PACKAGE_REGISTER.csv` PKG-077; `OBJECTIVE_REGISTER.csv` OBJ-004.
- **R-RESP-2** The CWP shall identify the EPC Integrator as the single accountable party for construction execution and turnover of PKG-077. Source: `DELIVERABLE_REGISTER.csv` DEL-077-03 (ResponsibleParty).

### R-SCO — Scope Coverage
- **R-SCO-1** The CWP shall cover SOW-0143 (Methanol Injection as a distinct flat project package, WBS 01). Source: `SCOPE_LEDGER.csv` SOW-0143.
- **R-SCO-2** The CWP shall remain consistent with the package scope, tagged-equipment list, and integration narrative carried in DEL-077-01 and the package datasheet in DEL-077-02. ASSUMPTION: cross-deliverable consistency rule per OBJ-010.

### R-INT — Interface and Tie-In Coverage
- **R-INT-1** The CWP shall plan, execute, and document construction tie-ins for each interface type identified for PKG-077:
  - Process Piping (IFC-32D789AF1B)
  - Utility Piping (IFC-36238DE0E8)
  - Relief / Flare / Vent (IFC-7ECB48113A)
  - Drain / Containment (IFC-4DE6A3A2ED)
  - Electrical Power (IFC-4269247DFA)
  - EHT (IFC-897BE87E57)
  - Grounding / Bonding (IFC-4848032D8D)
  - Area / Exterior Lighting (IFC-739B6603B5)
  - I&C / Control Cabling (IFC-1E031D5EF9)
  - Building HVAC / Services (IFC-F8D351A2A3)
  - Fire & Gas / Safety Systems (IFC-2176B4EB34)
  - Maintenance Access (IFC-AA0A9C42F5)
  - Structural / Foundations / Supports (IFC-A96044F713)
  
  Source: `INTERFACE_REGISTER.csv` (13 PKG-077 rows, all Applicable=YES).

- **R-INT-2** Each interface tie-in shall have an entry in the construction interface and turnover checklist (ART-EC659AD03C) identifying interface owner, tie-in location, installation method, inspection requirement, and turnover sign-off. ASSUMPTION (derived from artifact type "Construction Interface Evidence").

### R-CIV — Civil / Structural Construction Support
- **R-CIV-1** The CWP shall address foundations, supports, grading, containment, and maintenance access required to install and support the Methanol Injection package. Source: `OBJECTIVE_REGISTER.csv` OBJ-008; `INTERFACE_REGISTER.csv` PKG-077 (Structural/Foundations/Supports, Maintenance Access, Drain/Containment).

### R-ELE — Electrical and Controls Tie-In
- **R-ELE-1** The CWP shall include electrical-power, EHT, grounding/bonding, and area-lighting tie-in work consistent with OBJ-005. Source: `OBJECTIVE_REGISTER.csv` OBJ-005.
- **R-ELE-2** The CWP shall include I&C, control-cabling, and fire-and-gas tie-in work consistent with OBJ-006. Source: `OBJECTIVE_REGISTER.csv` OBJ-006.

### R-UTL — Utilities and Support Systems
- **R-UTL-1** The CWP shall include tie-ins to utility piping, relief/flare/vent, drains/containment, and building HVAC/services consistent with OBJ-007. Source: `OBJECTIVE_REGISTER.csv` OBJ-007.

### R-SAF — Sour-Service / Safety / Regulatory
- **R-SAF-1** The CWP shall preserve sour-service, fire/gas, shutdown, drain/containment, environmental, and code/standard requirements through construction execution and turnover evidence consistent with OBJ-009. Source: `OBJECTIVE_REGISTER.csv` OBJ-009. Specific code/standard list and clauses: TBD (location TBD — DBM-Deepcut SEC-15 not deliverable-local).

### R-CMN — Mechanical Completion / Turnover
- **R-CMN-1** The CWP shall define mechanical completion criteria and turnover records sufficient to support commissioning handoff and controlled open-item closure consistent with OBJ-010. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.
- **R-CMN-2** Vendor-documentation prerequisites for construction (installation manuals, vendor inspection records, certified drawings) shall be identified by reference to DEL-077-05 (Vendor Document Turnover Package). ASSUMPTION: cross-deliverable handoff rule per OBJ-010.

### R-ART — Required Artifacts
The CWP shall produce, at minimum:
- **R-ART-1** Construction work package narrative (ART-D62FFA7E43). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-2** Installation and tie-in workface plan (ART-F3B0D2F531). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-3** Construction interface and turnover checklist (ART-EC659AD03C). Source: `ARTIFACT_REGISTER.csv`.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project-defined codes and standards (referenced by OBJ-009) | All construction work | TBD — DBM-Deepcut SEC-15 not deliverable-local |
| 26020-Package_Requirements.docx vendor-documentation tables | Vendor-document prerequisites referenced by R-CMN-2 | TBD — not deliverable-local |
| Provincial / federal sour-service and pressure-equipment codes | Sour-service installation and inspection | location TBD; ASSUMPTION applicable based on OBJ-009 scope |

## Verification

| Req | Verification Approach |
|---|---|
| R-RESP-1, R-RESP-2 | Document review against `PACKAGE_REGISTER.csv` and DEL-077-01 |
| R-SCO-1, R-SCO-2 | Cross-check against SOW-0143, DEL-077-01, DEL-077-02 |
| R-INT-1, R-INT-2 | Inspection of construction interface and turnover checklist (ART-EC659AD03C) against the 13 PKG-077 interface rows |
| R-CIV-1 | Civil/structural inspection records and as-built check |
| R-ELE-1, R-ELE-2 | Electrical and I&C tie-in inspection, continuity/loop tests (specific test list TBD) |
| R-UTL-1 | Utility tie-in pressure / leak / line-walk records (specific tests TBD) |
| R-SAF-1 | Sour-service walkdown, F&G coverage check, regulatory walkdown |
| R-CMN-1, R-CMN-2 | Mechanical completion punch-list closure; turnover package signed by EPC Integrator and accepted by commissioning |
| R-ART-1..3 | Document existence and completeness check |

## Documentation

- Construction work package narrative (ART-D62FFA7E43)
- Installation and tie-in workface plan (ART-F3B0D2F531)
- Construction interface and turnover checklist (ART-EC659AD03C)
- Mechanical completion / turnover package (records, certificates, punch-list closures) — content list TBD
