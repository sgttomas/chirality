# Specification — DEL-052-03 Construction Work Package (Inlet / TEG Dehy Cross Exchanger)

## Scope

### In Scope
The EPC Integrator shall produce a Construction Work Package (CWP) describing how the PKG-052 Inlet / TEG Dehy Cross Exchanger package (tagged equipment E-5718-1) will be physically installed, built, inspected, turned over, and tied into the larger 04-25 Deepcut facility. Source: `DELIVERABLE_REGISTER.csv` row DEL-052-03 (Description).

The CWP covers:

1. Physical installation of the vendor-supplied Inlet / TEG Dehy Cross Exchanger (E-5718-1) including foundations setting, alignment, levelling, and anchoring.
2. Construction tie-ins to all applicable facility interfaces (see Requirements §R-INT).
3. Inspection and quality verification of installation and tie-in work, with sour-service rigor (see §R-SAF).
4. Mechanical completion, system turnover, and handoff to commissioning.
5. Construction interface coordination with adjacent packages and disciplines (notably inlet separation upstream and inlet compression downstream on the sour side; amine sweetening unit on the sweet side).

### Out of Scope (boundary with sibling deliverables under PKG-052)
- Package engineering, package design, vendor documentation, and physical equipment supply — owned by Package Vendor under DEL-052-04 (Vendor Engineered Equipment Package) and DEL-052-05 (Vendor Document Turnover Package). Source: `PACKAGE_REGISTER.csv` PKG-052 ResponsibilityModel.
- Scope-of-work narrative and tagged equipment list — DEL-052-01.
- Package datasheet and vendor handoff basis — DEL-052-02.
- EPC vendor-package review and acceptance — DEL-052-06.

### Out of Scope (by-others, per source)
Per SOW-0106 the following are explicitly "by others" and not within this CWP's executed-scope unless the EPC Integrator separately owns the adjacent package: interconnecting piping, DCS integration, foundations, electrical supply to MCC. The CWP shall plan the tie-ins to these scopes and identify the owning party at each interface.

### Exclusions
- TBD — no package-specific exclusions are stated in source materials. Source: `PACKAGE_REGISTER.csv` PKG-052 Exclusions ("TBD; no package-specific exclusions stated in source materials.").

## Requirements

> Each requirement is labeled with provenance. ASSUMPTION items are inferences from authority lower in the chain (decomposition narrative or package-discipline convention). Values requiring source data not locally accessible are marked `TBD (location TBD)`.

### R-RESP — Responsibility Discipline
- **R-RESP-1** The CWP shall preserve the vendor/EPC split: vendor package engineering, design, vendor documentation, and equipment supply remain with the Package Vendor; the EPC Integrator owns integration, interfaces, tie-ins, constructability, and construction/turnover. Source: `PACKAGE_REGISTER.csv` PKG-052 ResponsibilityModel; `OBJECTIVE_REGISTER.csv` OBJ-004.
- **R-RESP-2** The CWP shall identify the EPC Integrator as the single accountable party for construction execution and turnover of PKG-052. Source: `DELIVERABLE_REGISTER.csv` DEL-052-03 (ResponsibleParty).

### R-SCO — Scope Coverage
- **R-SCO-1** The CWP shall cover SOW-0103, SOW-0104, SOW-0105, and SOW-0106 (the four PKG-052 IN-scope items: distinct flat package carriage; basic scope and process function; major included equipment; scope notes including operating/design conditions and by-others items). Source: `SCOPE_LEDGER.csv` rows SOW-0103..SOW-0106.
- **R-SCO-2** The CWP shall remain consistent with the package scope and tagged-equipment list carried in DEL-052-01 and the package datasheet in DEL-052-02. ASSUMPTION: cross-deliverable consistency rule per OBJ-010.
- **R-SCO-3** The CWP shall identify E-5718-1 (Inlet / TEG DEHY Cross Exchanger, TEMA 'R' BEM, duty 5514.3 kW / 18.82 MMBTU/hr) as the package's tagged equipment scope. Source: `SCOPE_LEDGER.csv` SOW-0105; `PACKAGE_REGISTER.csv` PKG-052 ScopeStatement.

### R-INT — Interface and Tie-In Coverage
- **R-INT-1** The CWP shall plan, execute, and document construction tie-ins for each interface type identified for PKG-052 (9 interfaces, all Applicable=YES per `INTERFACE_REGISTER.csv`):
  - Process Piping (IFC-E97F55B211)
  - Utility Piping (IFC-A891689774)
  - Drain / Containment (IFC-DDB08C1331)
  - EHT (IFC-C3CE1B5E7D)
  - Grounding / Bonding (IFC-398F6BFCE1)
  - Area / Exterior Lighting (IFC-F79647C246)
  - I&C / Control Cabling (IFC-94006D4790)
  - Maintenance Access (IFC-0D3B12DEF3)
  - Structural / Foundations / Supports (IFC-A40EC04E30)
  
  Source: `INTERFACE_REGISTER.csv` (9 PKG-052 rows).

- **R-INT-2** Each interface tie-in shall have an entry in the construction interface and turnover checklist (ART-0E330BEA94) identifying interface owner, tie-in location, installation method, inspection requirement, and turnover sign-off. ASSUMPTION (derived from artifact type "Construction Interface Evidence").
- **R-INT-3** Process Piping tie-ins (IFC-E97F55B211) shall include the sour-gas inlet line from inlet separation, the sour-gas outlet line to the inlet compressors, and the sweet-gas inlet and outlet lines (amine-unit side). Source: `SCOPE_LEDGER.csv` SOW-0104 (process function narrative). Specific pipe-class, line-list, and tie-in point detail: TBD (location TBD — vendor and P&ID data not deliverable-local; expected from DEL-052-02 / DEL-052-04).
- **R-INT-4** Note on "by others" items per SOW-0106 (interconnecting piping, DCS integration, foundations, electrical supply to MCC): the CWP shall identify the owning party at each interface and plan the tie-in handoff, even when the tie-in is executed by another package. Source: `SCOPE_LEDGER.csv` SOW-0106.

### R-CIV — Civil / Structural Construction Support
- **R-CIV-1** The CWP shall address foundations, supports, grading, containment, and maintenance access required to install and support E-5718-1. Source: `OBJECTIVE_REGISTER.csv` OBJ-008; `INTERFACE_REGISTER.csv` PKG-052 (Structural/Foundations/Supports, Maintenance Access, Drain/Containment).
- **R-CIV-2** Foundation design is "by others" per SOW-0106; the CWP shall coordinate foundation-readiness with the owning civil package and verify foundation acceptance prior to equipment setting. Source: `SCOPE_LEDGER.csv` SOW-0106.

### R-ELE — Electrical Tie-In
- **R-ELE-1** The CWP shall include EHT (IFC-C3CE1B5E7D), grounding/bonding (IFC-398F6BFCE1), and area/exterior-lighting (IFC-F79647C246) tie-in work consistent with OBJ-005. Source: `OBJECTIVE_REGISTER.csv` OBJ-005; `INTERFACE_REGISTER.csv` PKG-052.
- **R-ELE-2** Electrical supply to MCC is "by others" per SOW-0106; the CWP shall coordinate the electrical tie-in handoff and verify supply readiness prior to commissioning. Source: `SCOPE_LEDGER.csv` SOW-0106.
- **R-ELE-3** Note: `INTERFACE_REGISTER.csv` for PKG-052 does NOT list a discrete "Electrical Power" interface row — the exchanger is unfired with no driver (SOW-0106: "Driver: No Driver"), so primary electrical loads are limited to EHT, instrumentation, and area lighting. Source: `INTERFACE_REGISTER.csv` PKG-052; `SCOPE_LEDGER.csv` SOW-0106.

### R-INS — Instrumentation and Controls Tie-In
- **R-INS-1** The CWP shall include I&C / control-cabling tie-in work (IFC-94006D4790) consistent with OBJ-006. Source: `OBJECTIVE_REGISTER.csv` OBJ-006; `INTERFACE_REGISTER.csv` PKG-052.
- **R-INS-2** DCS integration is "by others" per SOW-0106; the CWP shall coordinate I/O tie-in and loop verification with the owning controls package. Source: `SCOPE_LEDGER.csv` SOW-0106.
- **R-INS-3** Note: `INTERFACE_REGISTER.csv` for PKG-052 does NOT list a discrete "Fire & Gas / Safety Systems" interface row; the exchanger is a passive heat-exchange device. Fire and gas coverage of the equipment area is presumed to come from the area-wide F&G package, not this CWP. ASSUMPTION based on absence in register and equipment type.

### R-UTL — Utilities and Support Systems
- **R-UTL-1** The CWP shall include tie-ins to utility piping (IFC-A891689774) and drains/containment (IFC-DDB08C1331) consistent with OBJ-007. Source: `OBJECTIVE_REGISTER.csv` OBJ-007; `INTERFACE_REGISTER.csv` PKG-052. Specific utility list (vent, drain, blowdown, instrument air, steam-out if any): TBD (location TBD).

### R-SAF — Sour-Service / Safety / Regulatory
- **R-SAF-1** The CWP shall apply sour-service construction rigor — materials traceability (positive material identification at receipt), heat-affected-zone hardness limits, post-weld heat treatment where required, hydrotest plans, and code-stamp verification — consistent with OBJ-009. Source: `OBJECTIVE_REGISTER.csv` OBJ-009; `SCOPE_LEDGER.csv` SOW-0104 (sour gas service). Specific code/standard list and clauses: TBD (location TBD — DBM-Deepcut SEC-15 not deliverable-local).
- **R-SAF-2** The CWP shall preserve relief/flare/vent, drain/containment, environmental, and regulatory requirements through construction execution and turnover evidence. Source: `OBJECTIVE_REGISTER.csv` OBJ-009. Specific tie-in points to facility relief/vent (if any from this exchanger): TBD (location TBD — INTERFACE_REGISTER.csv PKG-052 does NOT list a Relief/Flare/Vent row; PSV protection is presumed handled at adjacent equipment per typical exchanger practice — ASSUMPTION to be confirmed against P&IDs).

### R-CMN — Mechanical Completion / Turnover
- **R-CMN-1** The CWP shall define mechanical completion criteria and turnover records sufficient to support commissioning handoff and controlled open-item closure consistent with OBJ-010. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.
- **R-CMN-2** Vendor-documentation prerequisites for construction (installation manuals, vendor inspection records, certified drawings, U-1 / MDR for the pressure vessel) shall be identified by reference to DEL-052-05 (Vendor Document Turnover Package). ASSUMPTION: cross-deliverable handoff rule per OBJ-010.
- **R-CMN-3** Operability/maintainability/winterization considerations carried by OBJ-010 shall be visible in turnover evidence (e.g., maintenance-access walkdown, winterization walkdown given -40 °C ambient minimum). Source: `OBJECTIVE_REGISTER.csv` OBJ-010; `SCOPE_LEDGER.csv` SOW-0106 (ambient design temperatures).

### R-ART — Required Artifacts
The CWP shall produce, at minimum:
- **R-ART-1** Construction work package narrative (ART-2444495F85). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-2** Installation and tie-in workface plan (ART-F79E686395). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-3** Construction interface and turnover checklist (ART-0E330BEA94). Source: `ARTIFACT_REGISTER.csv`.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project-defined codes and standards (referenced by OBJ-009) | All construction work; sour service | TBD — DBM-Deepcut SEC-15 not deliverable-local |
| ASME BPVC Section VIII (pressure vessel) / TEMA 'R' (heat exchanger mechanical) | E-5718-1 vessel/exchanger construction, inspection, and code-stamping | ASSUMPTION applicable based on TEMA 'R' designation in SOW-0105 and pressure-equipment service; specific edition/clauses TBD (location TBD) |
| Sour-service material/welding standards (e.g., NACE MR0175 / ISO 15156 family) | Materials, welding, and hardness limits in sour gas service | ASSUMPTION applicable based on sour-service scope (SOW-0104); specific reference TBD (location TBD — DBM-Deepcut SEC-15 not deliverable-local) |
| Provincial / federal pressure-equipment, sour-service, and construction codes | Installation, inspection, and turnover authorization | location TBD; ASSUMPTION applicable based on OBJ-009 |
| 26020-Package_Requirements.docx vendor-documentation tables | Vendor-document prerequisites referenced by R-CMN-2 | TBD — clause-level text not deliverable-local (`_Sources/26020-Package_Requirements.docx` is a binary `.docx`) |

## Verification

| Req | Verification Approach |
|---|---|
| R-RESP-1, R-RESP-2 | Document review against `PACKAGE_REGISTER.csv` and DEL-052-01 |
| R-SCO-1..R-SCO-3 | Cross-check against SOW-0103..SOW-0106, DEL-052-01, DEL-052-02 |
| R-INT-1, R-INT-2 | Inspection of construction interface and turnover checklist (ART-0E330BEA94) against the 9 PKG-052 interface rows |
| R-INT-3 | P&ID / line-list cross-check (downstream — pending vendor and P&ID availability) |
| R-INT-4 | Handoff log/matrix between PKG-052 CWP and owning by-others packages |
| R-CIV-1, R-CIV-2 | Civil/structural inspection records and foundation-acceptance record |
| R-ELE-1..R-ELE-3 | EHT continuity tests, grounding tests, lighting acceptance; supply-readiness handoff log |
| R-INS-1..R-INS-3 | Loop check / I/O verification log with owning controls package |
| R-UTL-1 | Utility tie-in pressure / leak / line-walk records |
| R-SAF-1, R-SAF-2 | PMI records, weld-hardness records, hydrotest records, code-stamp verification; sour-service walkdown; regulatory walkdown |
| R-CMN-1..R-CMN-3 | Mechanical completion punch-list closure; turnover package signed by EPC Integrator and accepted by commissioning; maintenance/winterization walkdown |
| R-ART-1..R-ART-3 | Document existence and completeness check |

## Documentation

- Construction work package narrative (ART-2444495F85)
- Installation and tie-in workface plan (ART-F79E686395)
- Construction interface and turnover checklist (ART-0E330BEA94)
- Mechanical completion / turnover package (records, certificates, punch-list closures, vessel MDR/U-1, hydrotest records) — content list TBD (location TBD)
