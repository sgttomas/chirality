# Specification — DEL-098-03 Construction Work Package

> Pass: P1_P2 (initial draft + cross-reference). Normative content for the EPC Integrator's Construction Work Package covering PKG-098 (Tanks, Sour Water, API 650, 3-25).

## Scope

### Covered

- Field receipt, off-loading, and storage of vendor-supplied tank components for PKG-098 (TK-9030-2, TK-9040-2, TK-9050-2: three 3,800 bbl Sour Produced Water Storage Tanks).
- EPC Integrator scope explicitly listed as "By others" in vendor scope (i.e., owned by EPC Integrator for execution):
  - Tank foundations
  - Site mounting / erection of tanks
  - Electrical and instrumentation field installation
  - Platforms, staircases, ladders
  - Source: `26020-Package_Requirements.docx` heading 50, Scope Notes / Open Items.
- Field interface execution for: Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports. Source: `26020-Package_Requirements.docx` heading 50, Physical Interface Summary; `PACKAGE_REGISTER.csv` PKG-098.
- Field hydrotest, flushing/cleaning/drying execution per vendor procedures.
- Construction interface management with adjacent packages and the produced-water transfer / H2O2 treatment systems.
- Turnover documentation: punchlist, mechanical completion, system completion, ready-for-commissioning.

### Excluded

- Tank package engineering, design, fabrication, FAT, vendor data book — owned by Package Vendor. Source: `PACKAGE_REGISTER.csv` PKG-098 PackageScopeNarrative.
- Commissioning and start-up operations beyond ready-for-commissioning handover (ASSUMPTION; CWP scope per common EPC practice).
- Operate/maintain procedures for in-service operation (vendor IOM `MEC-025`).
- Downstream pipeline construction beyond facility tie-in / riser. Source: DBM `3-25_Comp_and_Liquids_DBM.md` §Produced-Water Storage.

## Requirements

R-01. The Construction Work Package SHALL provide a workface plan covering foundations, tank erection/setting, platforms/staircases, and E&I installation for TK-9030-2, TK-9040-2, TK-9050-2. Source: `26020-Package_Requirements.docx` heading 50, Scope Notes (By-others list).

R-02. Tank erection SHALL be performed in accordance with vendor's Equipment Installation / Setting Drawings (`MEC-017`), Anchor Bolt / Embedment Drawings (`STR-013`), Foundation Drawings (`STR-006`), and Lifting / Handling Study (`MEC-018`) / Lifting Lug / Transport Analysis (`STR-014`). Source: Vendor Engineering Deliverables list, `26020-Package_Requirements.docx` heading 50.

R-03. Tank construction shall conform to modified API 650 (atmospheric) per vendor design basis. Source: `26020-Package_Requirements.docx` heading 50 Major Included Equipment; DBM §Produced-Water Storage. (CWP does not redesign; it constructs to the vendor-supplied basis.)

R-04. Internal coating (Devchem 253) on floor, walls, and roof SHALL be inspected for damage at receipt and after erection; field touch-up requirements per coating manufacturer / vendor procedure. Source: `26020-Package_Requirements.docx` heading 50 (coating spec); coating-application standard reference — location TBD.

R-05. External insulation and electric heat tracing SHALL be installed after hydrotest and integrity confirmation. Heat-tracing design serves freeze protection / winterization. Source: `26020-Package_Requirements.docx` heading 50 (external insulation, electric heating); DBM §Site Basis (winterization, electric heat tracing, tank heating governed by -40 °C ambient).

R-06. Field hydrotest SHALL be performed per vendor Hydrotest / Pressure Test Packages (`PIP-024`). Test medium, fill level, hold duration, acceptance criteria — TBD (per vendor procedure / API 650). Source: Vendor Engineering Deliverables list; API 650 procedural detail — location TBD.

R-07. Flushing / cleaning / drying SHALL be executed per vendor procedure (`PIP-025`) prior to system turnover. Source: Vendor Engineering Deliverables list.

R-08. Cathodic protection SHALL be installed per vendor's Cathodic Protection Design Package (`PLN-016`) and Corrosion Protection Design Basis (`PLN-015`). Source: Vendor Engineering Deliverables list; package interface row Cathodic Protection = Yes.

R-09. Bunded / secondary containment SHALL be constructed per vendor's Bund / Dike / Secondary Containment Drawings (`CIV-014`), tied to site grading (`CIV-003`), drainage (`CIV-004`), and retention pond (`CIV-015`). Source: Vendor Engineering Deliverables list; interface row Grading / Site Drainage / Spill Containment = Yes.

R-10. Grounding / bonding SHALL be installed per Grounding / Earthing Study (`ELE-012`) and Earthing / Bonding Layout Drawings (`ELE-019`). Source: Vendor Engineering Deliverables list; interface row Grounding/Bonding = Yes.

R-11. Area / exterior lighting SHALL be installed per Lighting Layout Drawings (`ELE-017`). Source: Vendor Engineering Deliverables list; interface row Area/Exterior Lighting = Yes (note in interface table cites `26020-Packages_Interfaces.3.xlsx` column M row 93).

R-12. I&C field installation (instrument cabling, hook-up, JB/marshalling, loop checks) SHALL follow vendor Instrument Index (`INS-002`), Hook-Up Drawings (`INS-006`), Cable Schedule (`INS-011`), I/O List (`INS-018`), Loop Diagrams (`INS-008`), and Control Narrative (`CTL-003`). Source: Vendor Engineering Deliverables list.

R-13. Process piping tie-ins SHALL be constructed per Tie-In List / Tie-In Scope Sheets (`PIP-004`), with fabrication per `PIP-009` and isometric drawings `PIP-008`. Source: Vendor Engineering Deliverables list; interface row Process Piping = Yes.

R-14. Relief / flare / vent tie-ins SHALL be constructed in accordance with Relief and Flare Design Basis (`PRO-014`) and PSV/Pressure Relief Sizing (`PRO-015`); set-pressures and tag list TBD per RFQ output. Source: Vendor Engineering Deliverables list; interface row Relief/Flare/Vent = Yes.

R-15. Drain / closed-containment tie-ins SHALL be constructed per Process Sewer / Closed Drain Design Basis (`PRO-023`); minimum drain header rating 300# ANSI. Source: Vendor Engineering Deliverables list; DBM §Drain systems (line 493): "Minimum drain-header rating is 300# ANSI."

R-16. Structural steel, platforms, access, anchor bolts, and module supports SHALL be installed per `STR-001` through `STR-020` series. Source: Vendor Engineering Deliverables list.

R-17. The Construction Work Package SHALL produce and maintain a construction interface and turnover checklist covering: weld inspection records, NDE results, coating-touch-up records, hydrotest packages, ITP sign-offs (`QLT-003`), MTRs (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / VDB (`QLT-021`). Source: Vendor Engineering Deliverables list, core vendor documents block.

R-18. Construction shall accommodate the -40 °C minimum ambient site basis (winterization, EHT, freeze protection). Source: DBM §Site Basis (line 145).

R-19. SOW items covered (SOW-0221, SOW-0222, SOW-0223, SOW-0224) shall each be mapped to one or more CWP work packs and turnover boundaries. Source: `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` row DEL-098-03. (Detailed SOW text — location TBD; ARTIFACT_REGISTER mapping not yet read.)

## Standards

| Standard | Applicability | Local availability |
|---|---|---|
| API 650 (Modified) | Tank design/construction basis (vendor-supplied; CWP constructs to drawings) | Not locally accessible — location TBD |
| CSA / provincial pressure equipment construction code | Likely applicable to pressure-test execution in Alberta context | ASSUMPTION; location TBD |
| Devchem 253 coating-application procedure | Internal-coating field touch-up | Location TBD |
| Site safety / hot-work / confined-space (project HSE plan) | Applies to all field construction | Location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01 | Workface-plan document exists and is approved by EPC PM and Construction Manager. |
| R-02, R-16 | Survey checks against `STR-013` anchor-bolt drawings; verified anchor torque records; foundation-as-built confirmation. |
| R-03, R-04 | Visual + dimensional QA against vendor drawings; coating inspection (DFT, holiday test per coating spec — TBD). |
| R-05 | Insulation/EHT installation inspection; continuity check on heat-tracing circuits; commissioning hand-over signed. |
| R-06 | Signed hydrotest report; chart record; punchlist closure. |
| R-07 | Signed flushing/cleaning record per `PIP-025`. |
| R-08 | CP system test certificate; rectifier commissioning record. |
| R-09 | Containment volume verification vs `CIV-014`; grading as-built. |
| R-10 | Earthing continuity / resistance test report. |
| R-11 | Lighting illumination level survey at commissioning. |
| R-12 | Loop check certificates; cable continuity / megger records. |
| R-13 | Piping ITP sign-off; weld map; NDE reports; tie-in walkdown sign-off. |
| R-14 | PSV install certificate; set-pressure verification. |
| R-15 | Drain hydrotest and slope verification. |
| R-17 | Turnover binder review and acceptance by Commissioning Lead. |
| R-18 | Cold-weather construction methods reviewed; winter work procedures attached when applicable. |
| R-19 | Traceability matrix CWP-pack → SOW item; signed by EPC PM. |

## Documentation

Required artifacts produced by this deliverable:

- Construction Work Package (master CWP document, indexed by SOW items SOW-0221..SOW-0224)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Hydrotest, flushing, NDE, coating, EHT, CP, loop-check, earthing, and lighting test records
- Mechanical completion / system completion / ready-for-commissioning sign-off package
- Construction red-line / as-built mark-ups feeding vendor `PIP-028` and structural as-builts

Source: `_CONTEXT.md` Anticipated Artifacts; vendor deliverable list categories.
