# Specification — DEL-067-03 Construction Work Package (Tanks, Sour Water (API 650) 4-25)

## Scope

### In Scope
The EPC Integrator shall produce a Construction Work Package (CWP) describing how the PKG-067 Tanks, Sour Water (API 650) 4-25 package (two API 650 modified atmospheric sour-water / produced-water storage tanks, expected tags TK-9010-1 and TK-9020-1) will be physically installed, built, inspected, turned over, and tied into the larger 04-25 Deepcut facility. Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row DEL-067-03; `SCOPE_LEDGER.csv` SOW-0227.

The CWP covers:

1. Physical installation of the two vendor-supplied tanks (TK-9010-1, TK-9020-1) including foundation setting, shell erection method (where vendor delivers shop-fabricated vs. field-erected), levelling, anchoring, and roof installation. Specific erection method: TBD (location TBD — vendor decision in DEL-067-04).
2. Construction tie-ins to all applicable facility interfaces (see Requirements §R-INT).
3. Internal coating application/inspection, external insulation and electric heating (where required), PVRV/EPRV protection, LP fuel-gas blanket, and VRU suction/header tie-in (as applicable). Source: `SCOPE_LEDGER.csv` SOW-0227.
4. Secondary containment construction (berm / liner / drainage) coordination with the facility containment scope.
5. Inspection and quality verification of installation and tie-in work, with sour-service rigor (see §R-SAF).
6. Mechanical completion, system turnover, and handoff to commissioning.

### Out of Scope (boundary with sibling deliverables under PKG-067)
- Package engineering, package design, vendor documentation, and physical equipment supply — owned by Package Vendor under DEL-067-04 (Vendor Engineered Equipment Package) and DEL-067-05 (Vendor Document Turnover Package). Source: `PACKAGE_REGISTER.csv` PKG-067 ResponsibilityModel.
- Scope-of-work narrative — DEL-067-01.
- Package datasheet and vendor handoff basis — DEL-067-02.
- EPC vendor-package review and acceptance — DEL-067-06.

### Out of Scope (resolved at sibling deliverables)
The package source materials (SOW-0226..SOW-0228) describe what the package supplies and lists scope-notes/open-items but do not enumerate explicit "by others" construction items the way some other packages do. Items the CWP shall therefore *coordinate to* but not own include (ASSUMPTION based on EPC/vendor split, OBJ-004, OBJ-005, OBJ-007, OBJ-008): interconnecting piping outside vendor battery limits, DCS integration, foundation engineering, electrical supply, blanket-gas supply piping outside vendor battery limits, and VRU header from the receiving compressor/VRU package.

### Exclusions
- TBD — no package-specific exclusions are stated in source materials. Source: `PACKAGE_REGISTER.csv` PKG-067 Exclusions ("TBD; no package-specific exclusions stated in source materials.").

## Requirements

> Each requirement is labeled with provenance. ASSUMPTION items are inferences from authority lower in the chain (decomposition narrative or package-discipline convention). Values requiring source data not locally accessible are marked `TBD (location TBD)`.

### R-RESP — Responsibility Discipline
- **R-RESP-1** The CWP shall preserve the vendor/EPC split: vendor package engineering, design, vendor documentation, and equipment supply remain with the Package Vendor; the EPC Integrator owns integration, interfaces, tie-ins, constructability, and construction/turnover. Source: `PACKAGE_REGISTER.csv` PKG-067 ResponsibilityModel; `OBJECTIVE_REGISTER.csv` OBJ-004.
- **R-RESP-2** The CWP shall identify the EPC Integrator as the single accountable party for construction execution and turnover of PKG-067. Source: `DELIVERABLE_REGISTER.csv` DEL-067-03 (ResponsibleParty); `_CONTEXT.md`.

### R-SCO — Scope Coverage
- **R-SCO-1** The CWP shall cover SOW-0225, SOW-0226, SOW-0227, and SOW-0228 (the four PKG-067 IN-scope items: distinct flat package carriage; basic scope — two sour-water tanks for 4-25 service; major included equipment with coating/insulation/PVRV/blanket/VRU; scope notes and open items). Source: `SCOPE_LEDGER.csv` rows SOW-0225..SOW-0228.
- **R-SCO-2** The CWP shall remain consistent with the package scope carried in DEL-067-01 and the package datasheet in DEL-067-02. ASSUMPTION: cross-deliverable consistency rule per OBJ-010.
- **R-SCO-3** The CWP shall identify the two API 650 modified atmospheric storage tanks (expected tags TK-9010-1 and TK-9020-1) as the package's tagged equipment scope, and shall flag the explicit open items from SOW-0228 (service naming, tank count, tags, source headers, design SG, heating/insulation extent, VRU/blanket gas applicability, 3-25 design-basis applicability) as construction-readiness prerequisites to be resolved by DEL-067-02 and DEL-067-04. Source: `SCOPE_LEDGER.csv` SOW-0227, SOW-0228.

### R-INT — Interface and Tie-In Coverage
- **R-INT-1** The CWP shall plan, execute, and document construction tie-ins for each interface type identified for PKG-067 (9 interfaces, all Applicable=YES per `INTERFACE_REGISTER.csv`):
  - Process Piping (IFC-1CB18EBD35)
  - Relief / Flare / Vent (IFC-44474541F7)
  - Drain / Containment (IFC-C5A70E8F73)
  - Grounding / Bonding (IFC-A172213C86)
  - Area / Exterior Lighting (IFC-0152A5CE44)
  - Cathodic Protection (IFC-A3C5E09CBC)
  - I&C / Control Cabling (IFC-789528648B)
  - Grading / Site Drainage / Spill Containment (IFC-E6F955CD2C)
  - Structural / Foundations / Supports (IFC-2815BE772E)

  Source: `INTERFACE_REGISTER.csv` (9 PKG-067 rows).

- **R-INT-2** Each interface tie-in shall have an entry in the construction interface and turnover checklist (ART-09F3991C52) identifying interface owner, tie-in location, installation method, inspection requirement, and turnover sign-off. ASSUMPTION (derived from artifact type "Construction Interface Evidence").
- **R-INT-3** Process Piping tie-ins (IFC-1CB18EBD35) shall include the tank fill lines from upstream sour-water / produced-water source header(s) and any pump-out lines to downstream disposition. Specific source-header identity, line list, and tie-in detail: TBD (location TBD — open item per SOW-0228; expected resolution by DEL-067-02 / DEL-067-04).
- **R-INT-4** Relief / Flare / Vent tie-ins (IFC-44474541F7) shall include PVRV/EPRV venting paths and any blanket-gas relief routing. Source: `INTERFACE_REGISTER.csv` PKG-067; `SCOPE_LEDGER.csv` SOW-0227 (PVRV/EPRV protection). Specific relief destination (atmosphere vs. low-pressure flare/vent header): TBD (location TBD).
- **R-INT-5** Drain / Containment tie-ins (IFC-C5A70E8F73) and Grading / Site Drainage / Spill Containment (IFC-E6F955CD2C) shall coordinate with the facility secondary-containment scope. Source: `INTERFACE_REGISTER.csv` PKG-067; `OBJECTIVE_REGISTER.csv` OBJ-007, OBJ-009.

### R-CIV — Civil / Structural Construction Support
- **R-CIV-1** The CWP shall address tank foundations (ring wall or slab as specified by vendor), grading, secondary containment (berm or equivalent), and site drainage required to install and support TK-9010-1 and TK-9020-1. Source: `INTERFACE_REGISTER.csv` PKG-067 (Structural/Foundations/Supports IFC-2815BE772E; Grading/Site Drainage/Spill Containment IFC-E6F955CD2C; Drain/Containment IFC-C5A70E8F73); `OBJECTIVE_REGISTER.csv` OBJ-008.
- **R-CIV-2** Foundation design and secondary-containment design are expected to be produced by the project civil discipline outside this package; the CWP shall coordinate foundation-readiness and containment-readiness with the owning civil scope and verify foundation acceptance prior to tank erection / setting. ASSUMPTION based on OBJ-008 and standard EPC discipline split (foundation engineering not stated as vendor scope).

### R-ELE — Electrical Tie-In
- **R-ELE-1** The CWP shall include grounding/bonding (IFC-A172213C86), area/exterior-lighting (IFC-0152A5CE44), and cathodic-protection (IFC-A3C5E09CBC) tie-in work consistent with OBJ-005. Source: `OBJECTIVE_REGISTER.csv` OBJ-005; `INTERFACE_REGISTER.csv` PKG-067.
- **R-ELE-2** Where electric heating (EHT) is required per SOW-0227 (extent TBD per SOW-0228), the CWP shall include EHT installation, circuit acceptance, and commissioning evidence. Source: `SCOPE_LEDGER.csv` SOW-0227, SOW-0228. Note: `INTERFACE_REGISTER.csv` for PKG-067 does NOT list a discrete "EHT" interface row — the heating scope (where required) is treated as part of the tank vendor package and supplied power feed (assumed via facility electrical scope). ASSUMPTION; see Conflict Table CFT-001.
- **R-ELE-3** Cathodic Protection (IFC-A3C5E09CBC) installation and testing (e.g., anode placement, reference-cell checks, isolation verification) shall be planned and documented; specific CP system type: TBD (location TBD).

### R-INS — Instrumentation and Controls Tie-In
- **R-INS-1** The CWP shall include I&C / control-cabling tie-in work (IFC-789528648B) for tank instrumentation (level, temperature, pressure/vacuum, leak detection as applicable) consistent with OBJ-006 and SOW-0227. Source: `OBJECTIVE_REGISTER.csv` OBJ-006; `INTERFACE_REGISTER.csv` PKG-067; `SCOPE_LEDGER.csv` SOW-0227.
- **R-INS-2** DCS integration is presumed to be coordinated with the facility controls scope; the CWP shall coordinate I/O tie-in and loop verification with the owning controls package. ASSUMPTION (not stated in PKG-067 source slices, inferred from EPC discipline split and OBJ-006).
- **R-INS-3** Note: `INTERFACE_REGISTER.csv` for PKG-067 does NOT list a discrete "Fire & Gas / Safety Systems" interface row; area-wide F&G coverage of the tank pad is presumed to come from the facility F&G package. ASSUMPTION; see Conflict Table CFT-002.

### R-UTL — Utilities and Support Systems
- **R-UTL-1** The CWP shall coordinate the LP fuel-gas blanket supply tie-in and VRU suction/header tie-in (where applicable per SOW-0227 / SOW-0228) with the owning utility/VRU packages. Note: `INTERFACE_REGISTER.csv` for PKG-067 does NOT list a discrete "Utility Piping" interface row — blanket-gas and VRU connections are treated as Process Piping (IFC-1CB18EBD35) and Relief / Flare / Vent (IFC-44474541F7) here. ASSUMPTION; see Conflict Table CFT-002.

### R-SAF — Sour-Service / Safety / Regulatory
- **R-SAF-1** The CWP shall apply sour-service construction rigor — materials traceability (positive material identification at receipt), heat-affected-zone hardness limits, post-weld heat treatment where required, hydrostatic testing per API 650 for the tank shells, and tank inspection / certification — consistent with OBJ-009. Source: `OBJECTIVE_REGISTER.csv` OBJ-009; `SCOPE_LEDGER.csv` SOW-0226 (sour-water service). Specific code/standard clauses (API 650, NACE MR0175/ISO 15156, project sour-service basis): TBD (location TBD — DBM-Deepcut SEC-15 not deliverable-local; API 650 clauses not deliverable-local).
- **R-SAF-2** The CWP shall preserve relief/flare/vent, drain/containment, environmental, and regulatory requirements (including secondary containment and spill response) through construction execution and turnover evidence. Source: `OBJECTIVE_REGISTER.csv` OBJ-009; `INTERFACE_REGISTER.csv` PKG-067 (Relief/Flare/Vent, Drain/Containment, Grading/Site Drainage/Spill Containment).
- **R-SAF-3** Internal-coating application and inspection (holiday test, dry-film thickness, cure verification) for sour-service exposure shall be planned and documented; specific coating-system spec: TBD (location TBD). Source: `SCOPE_LEDGER.csv` SOW-0227 (internal coating).

### R-CMN — Mechanical Completion / Turnover
- **R-CMN-1** The CWP shall define mechanical completion criteria and turnover records sufficient to support commissioning handoff and controlled open-item closure consistent with OBJ-010. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.
- **R-CMN-2** Vendor-documentation prerequisites for construction (API 650 nameplate / tank data report, vendor inspection records, certified drawings, coating QA records, weld maps and NDE reports) shall be identified by reference to DEL-067-05 (Vendor Document Turnover Package). ASSUMPTION: cross-deliverable handoff rule per OBJ-010.
- **R-CMN-3** Operability / maintainability / winterization considerations carried by OBJ-010 shall be visible in turnover evidence (maintenance-access walkdown, EHT-readiness walkdown where heating is required, secondary-containment walkdown). Source: `OBJECTIVE_REGISTER.csv` OBJ-010; `SCOPE_LEDGER.csv` SOW-0227.
- **R-CMN-4** Resolution of the SOW-0228 open items (service naming, tank count, tags, source headers, design SG, heating/insulation extent, VRU/blanket gas applicability, 3-25 design-basis applicability) shall be a documented prerequisite to mechanical completion. Source: `SCOPE_LEDGER.csv` SOW-0228.

### R-ART — Required Artifacts
The CWP shall produce, at minimum:
- **R-ART-1** Construction work package narrative (ART-EE79CD3464). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-2** Installation and tie-in workface plan (ART-FE1E5417F6). Source: `ARTIFACT_REGISTER.csv`.
- **R-ART-3** Construction interface and turnover checklist (ART-09F3991C52). Source: `ARTIFACT_REGISTER.csv`.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650 (modified atmospheric storage tanks) | Tank shell/roof/bottom design, fabrication, erection, inspection, hydrostatic test, nameplate | Applicable per SOW-0227 ("API 650 modified atmospheric"); specific edition/clauses TBD (location TBD) |
| Project-defined codes and standards (referenced by OBJ-009) | All construction work; sour service | TBD — DBM-Deepcut SEC-15 not deliverable-local |
| Sour-service material/welding standards (e.g., NACE MR0175 / ISO 15156 family) | Materials, welding, and hardness limits in sour-water service | ASSUMPTION applicable based on sour-service scope (SOW-0226); specific reference TBD (location TBD) |
| Provincial / federal pressure-equipment, sour-service, environmental, and construction codes | Installation, inspection, containment, and turnover authorization | location TBD; ASSUMPTION applicable based on OBJ-009 |
| 26020-Package_Requirements.docx package heading 22 (vendor-documentation tables) | Vendor-document prerequisites referenced by R-CMN-2 | TBD — clause-level text not deliverable-local (`_Sources/26020-Package_Requirements.docx` is a binary `.docx`) |
| 26020-03-PT-RFQ-19-007 (3-25 sour-water analog RFQ) | Analog basis where 4-25 service is intended to mirror 3-25 (applicability TBD per SOW-0228) | location TBD; not deliverable-local |

## Verification

| Req | Verification Approach |
|---|---|
| R-RESP-1, R-RESP-2 | Document review against `PACKAGE_REGISTER.csv` PKG-067 and DEL-067-01 |
| R-SCO-1..R-SCO-3 | Cross-check against SOW-0225..SOW-0228, DEL-067-01, DEL-067-02 |
| R-INT-1, R-INT-2 | Inspection of construction interface and turnover checklist (ART-09F3991C52) against the 9 PKG-067 interface rows |
| R-INT-3 | P&ID / line-list cross-check (downstream — pending vendor and P&ID availability) |
| R-INT-4 | Relief-path walkdown; PVRV/EPRV set-pressure and discharge-path verification |
| R-INT-5 | Containment / drainage walkdown; coordination log with civil containment scope |
| R-CIV-1, R-CIV-2 | Civil/structural inspection records; foundation-acceptance record; ring-wall/slab survey |
| R-ELE-1..R-ELE-3 | Grounding tests; lighting acceptance; CP installation and reference-cell readings; EHT continuity (where applicable) |
| R-INS-1..R-INS-3 | Loop check / I/O verification log with owning controls package |
| R-UTL-1 | Blanket-gas and VRU tie-in handoff log with owning utility/VRU packages |
| R-SAF-1..R-SAF-3 | PMI records; weld-hardness records; hydrostatic test record per API 650; coating QA records (DFT, holiday, cure); regulatory walkdown |
| R-CMN-1..R-CMN-4 | Mechanical completion punch-list closure; turnover package signed by EPC Integrator and accepted by commissioning; documented closure of SOW-0228 open items |
| R-ART-1..R-ART-3 | Document existence and completeness check |

## Documentation

- Construction work package narrative (ART-EE79CD3464)
- Installation and tie-in workface plan (ART-FE1E5417F6)
- Construction interface and turnover checklist (ART-09F3991C52)
- Mechanical completion / turnover package (records, certificates, punch-list closures, API 650 tank data reports, hydrotest records, coating QA records, CP commissioning records) — content list TBD (location TBD)
