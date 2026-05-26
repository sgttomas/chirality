# Procedure — DEL-106-04 Vendor Engineered Equipment Package (Yard Lighting)

## Purpose

Operational procedure to produce the Vendor Engineered Equipment Package for `PKG-106` Yard Lighting (engineering, design, fabrication/supply of the physical equipment package plus the vendor package design basis and datasheet set), so that downstream `DEL-106-05` turnover and `DEL-106-06` EPC acceptance can proceed.

## Prerequisites

- **Declared upstream dependencies:** None declared in `_DEPENDENCIES.md`. (Logical inputs noted below are not declared blockers.)
- **Logical inputs (ASSUMPTION, not declared edges):**
  - EPC Scope of Work (`DEL-106-01`) — issued.
  - EPC Package Datasheet (`DEL-106-02`) — issued.
  - Accepted facility hazardous area drawings (location TBD).
  - Accepted geotechnical basis for pole foundations (location TBD).
  - Accepted electrical distribution layout identifying nearest RDC(s) (location TBD).
- **Required references read for this deliverable:**
  - DBM-Deepcut `4-25_Deepcut_DBM.md`, sections `## Lighting and Receptacles`, Electrical Services table, and the conduit/cable paragraphs preceding `## Lighting and Receptacles`.
  - Gate 7 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row DEL-106-04; `PACKAGE_REGISTER.csv` row PKG-106; `INTERFACE_REGISTER.csv` rows IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087.
- **Required project metadata read:** `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- **Source slices not yet available:** PKG-106 slice of `26020-Package_Requirements.docx` (HRR-106-04-004).

## Steps

1. **Confirm vendor scope boundary.** Resolve HRR-106-04-001 with the project to fix the outdoor/area subset boundary of `PKG-106`. Record the agreed boundary in the vendor design basis.
2. **Acquire source basis.** Read the DBM lighting basis (DBM-Deepcut `## Lighting and Receptacles`), the EPC Scope of Work (`DEL-106-01`) and Package Datasheet (`DEL-106-02`) once issued, and the PKG-106 slice of `26020-Package_Requirements.docx` once extracted. (TBD where not yet available.)
3. **Establish photometric and layout basis.** Define yard-area lux levels, uniformity ratios, mounting heights, mast pole layout, and fixture coverage zones. (Quantitative criteria TBD; vendor produces against EPC SOW/Datasheet.) Apply light-pollution rules (downcast only, no horizontal floodlights, photocell/switch control, mast pole offset from pad edge).
4. **Select fixtures and poles.** Use LED fixtures only. Confirm each fixture's area-classification suitability against facility hazardous area drawings. Select pole and mast-pole hardware qualified for the site cold-weather envelope (ambient TBD).
5. **Define electrical interface.** Design vendor-side terminations consistent with 120/208 V, 3 phase, 4 wire, 60 Hz, solidly grounded, fed from the nearest RDC. Coordinate branch-circuit conductor sizing assumptions (#10 AWG goal) with EPC Integrator. Do not mix receptacle and lighting circuits in vendor-supplied panels.
6. **Define grounding/bonding interface.** Provide ground lugs and bonding details supporting the declared package interface IFC-DA0D60681B. Do not assume facility cathodic-protection integration (excluded from facility design scope).
7. **Define controls.** Specify photocell or switch control per area, with rationale, supporting working-area minimization.
8. **Foundations and structural interface.** Specify mast pole base loads, anchor patterns, and any foundation interface data needed by EPC civil. (Geotechnical basis TBD.)
9. **Produce vendor package design basis and datasheet set.** Compile: photometric design basis and calculations; fixture datasheets and certifications; pole datasheets with mounting/foundation interface; wiring/termination schedules; grounding/bonding interface details; control schedule; standards-compliance declarations (CEC; light-pollution controls; building code where applicable); BOM. Mark unresolved items TBD with the basis for resolution.
10. **Fabricate / supply the physical equipment package.** Manufacture/procure fixtures, poles/mast poles, vendor-scope wiring, and mounting hardware per the design basis. Apply CEC-compliant rigid conduit and seals where the vendor scope includes shop-built buildings/assemblies containing lighting.
11. **Internal vendor verification.** Confirm vendor design satisfies each requirement (VEEP-REQ-001..015 in `Specification.md`). Record evidence in the vendor design basis.
12. **Hand to turnover and EPC acceptance.** Submit the vendor engineered physical equipment package and the vendor package design basis and datasheet set via `DEL-106-05` (Vendor Document Turnover Package), to be reviewed and accepted in `DEL-106-06` (EPC Vendor Package Review and Acceptance).

## Verification

| Check | Method | Evidence |
|---|---|---|
| All supplied lighting is LED (VEEP-REQ-003, REQ-004) | Inspect vendor fixture schedule | Vendor datasheet set |
| Fixtures suitable for area classification (VEEP-REQ-006) | Cross-check fixture certifications against hazardous area drawings | Vendor fixture schedule + facility area drawings |
| 120/208 V supply origin and feeder coordination (VEEP-REQ-005, REQ-008) | Review vendor electrical schedule with EPC | Vendor schedule + EPC integration note |
| Light-pollution controls implemented (VEEP-REQ-007) | Review photometric and layout drawings | Vendor photometric / layout drawings |
| Conduit method and seals where applicable (VEEP-REQ-009) | Review vendor wiring drawings | Vendor wiring drawings |
| No mixed receptacle/lighting circuits (VEEP-REQ-010) | Review vendor panel schedules | Vendor panel schedules |
| Interface provisions present and clean (VEEP-REQ-011, REQ-012, REQ-013) | Review vendor interface drawings against `INTERFACE_REGISTER` rows IFC-6FCF1B30D6 / IFC-DA0D60681B / IFC-ED86F51087 | Vendor interface drawings + interface register cross-reference |
| Both anticipated artifacts delivered (VEEP-REQ-001, REQ-014) | Confirm artifacts in `DEL-106-05` register | `DEL-106-05` document register |
| Vendor sourced design from EPC SOW + Datasheet (VEEP-REQ-002) | Verify cross-reference matrix | Vendor design basis cross-reference matrix |
| Quantitative basis (lux, pole, foundation) recorded (VEEP-REQ-015) | Verify vendor calculations are present | Vendor datasheet set |

## Records

- Vendor engineered physical equipment package (equipment itself with identification/BOM).
- Vendor package design basis (text + calculations).
- Vendor datasheet set (fixtures, poles, controls, grounding, interfaces).
- Cross-reference matrix to `DEL-106-01` SOW and `DEL-106-02` Package Datasheet.
- Standards-compliance declarations (CEC; light-pollution controls; building code where applicable).
- TBD/HRR resolutions log (HRR-106-04-001..004), retained until each is human-ruled.
- Submission record to `DEL-106-05` (Vendor Document Turnover Package).
- Acceptance evidence captured in `DEL-106-06` (EPC Vendor Package Review and Acceptance).
