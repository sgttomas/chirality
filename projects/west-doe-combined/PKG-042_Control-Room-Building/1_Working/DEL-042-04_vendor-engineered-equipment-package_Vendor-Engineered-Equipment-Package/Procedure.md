# Procedure — DEL-042-04 Vendor Engineered Equipment Package

Operational procedure for producing, verifying, and turning over the vendor-engineered Control Room Building equipment package under PKG-042.

## Purpose

Define the steps by which the Package Vendor produces the engineered Control Room Building package — engineering, design, fabrication/supply, and the physical equipment — from the EPC anchor inputs (`DEL-042-01_scope-of-work`, `DEL-042-02_package-datasheet`), and the verification and record steps required to support downstream EPC review and acceptance (`DEL-042-06`).

## Prerequisites

- Accepted EPC Scope of Work for PKG-042 (`DEL-042-01_scope-of-work`).
- Accepted EPC Package Datasheet for PKG-042 (`DEL-042-02_package-datasheet`).
- Available design-basis sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections cited in `Datasheet.md` References).
- Resolution of Conflict-Table items HRR-042-04-001 (cross-DBM applicability) and HRR-042-04-003 (interior area classification) before vendor design freeze; HRR-042-04-002 (building configuration) and HRR-042-04-004 (existing-building reuse) should be resolved before final design issuance.
- Confirmed building function: hosts the operations control-room environment, primary control-system server, operator/engineering workstations, and core network switches (DBM 3-25 §796; DBM 4-25 §3119, §3141).
- Final geotechnical report and project structural design criteria available for foundation design (DBM 3-25 §700).
- Declared upstream/downstream dependencies: none declared at deliverable scope (see `_DEPENDENCIES.md`). Effective upstream inputs are the EPC anchor deliverables above and the DBMs; downstream consumers are `DEL-042-03`, `DEL-042-05`, and `DEL-042-06`.

## Steps

1. **Confirm inputs and basis.**
   - Verify the EPC Scope of Work and Package Datasheet are accepted and current.
   - Verify building function and hosting basis (control room hosts operator/engineering workstations, primary control-system server, core network switches) against DBM 3-25 §796 and DBM 4-25 §3119, §3141.
   - Confirm resolution of HRR-042-04-001 and HRR-042-04-003.
2. **Develop vendor package design basis.**
   - Translate EPC inputs into the vendor package design basis document.
   - Capture coordination obligations against DBM 3-25 §704 (area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, maintenance access).
   - Capture plot-plan separation criteria (DBM 4-25 §254, §298) and the foundation basis (DBM 3-25 §700).
   - Capture the eleven PKG-042 InterfaceTypes as design inputs.
3. **Define building configuration.**
   - Record whether the building is shop-assembled module or site-built (HRR-042-04-002); if undecided, default to shop-assembled module and flag for EPC confirmation.
   - Record interior partitioning (operator room / server-network room / electrical-HVAC plant) and HVAC zoning approach.
   - Confirm interior area-classification basis (HRR-042-04-003 disposition) and select wiring method per DBM 4-25 §3025.
4. **Produce vendor datasheet set.**
   - Issue vendor package datasheet(s) covering structure, envelope, interior fit-out, building HVAC, building electrical, fire & gas, communications/network infrastructure, and operator-room furnishings.
   - Cross-reference each datasheet entry to the EPC Package Datasheet line items.
5. **Engineer and design the physical equipment package.**
   - Develop structural, architectural, mechanical (HVAC), electrical, fire & gas, and communications/network design for the building.
   - Provide engineering provisions for each of the eleven PKG-042 InterfaceTypes.
   - Where shop pre-assembly applies, specify rigid conduit for building lighting, exhaust fans, receptacles, and switches per DBM 4-25 §3025.
6. **Fabricate / supply the physical equipment package.**
   - Procure components and fabricate/assemble the vendor-supplied building per the accepted design.
   - Maintain production records suitable for vendor document turnover (handed off to `DEL-042-05`).
7. **Vendor verification / FAT.**
   - Execute vendor factory verification appropriate to a control-room building (envelope integrity, HVAC commissioning where shop-tested, building electrical, fire & gas device functional checks, network infrastructure continuity).
   - Record FAT evidence for inclusion in the turnover package.
8. **Handoff to construction, vendor document turnover, and EPC review.**
   - Coordinate site delivery and module setting with `DEL-042-03_construction-work-package`.
   - Provide the vendor package design basis, datasheet set, and FAT records to `DEL-042-05_vendor-document-turnover-package`.
   - Provide the engineered building and supporting documentation to `DEL-042-06_epc-vendor-package-review-and-acceptance` for EPC review and integration acceptance.

## Verification

- **Design verification.** Confirm vendor design satisfies REQ-042-04-01 through REQ-042-04-12 (`Specification.md`).
- **Interface verification.** Confirm engineering provisions for each of the eleven PKG-042 InterfaceTypes are present in the vendor design (REQ-042-04-04).
- **Coordination verification.** Confirm cross-discipline coordination per DBM 3-25 §704 (area classification, ventilation, heating, egress, F&G, ESD, RIO, power distribution, maintenance access) (REQ-042-04-05).
- **Siting verification.** Confirm plot-plan separations against API 2510 (bullets, ≥ 15.24 m) and OGAOM §9.6.15 (fired heaters, ≥ 25 m) (REQ-042-04-07).
- **Foundation verification.** Confirm foundation design against final geotechnical report and loading basis (REQ-042-04-06).
- **Wiring verification.** Confirm interior conduit and wiring method comply with CEC and the resolved interior area classification (REQ-042-04-08, REQ-042-04-09).
- **Conflict-Table verification.** Confirm HRR-042-04-001 and HRR-042-04-003 have human rulings, and that HRR-042-04-002 and HRR-042-04-004 have dispositions before final design issuance (REQ-042-04-11).
- **Boundary verification.** Confirm vendor design respects the EPC-owned facility-integration boundary (REQ-042-04-12).

## Records

- Vendor package design basis document.
- Vendor package datasheet set.
- Building structural / foundation calculations and geotechnical input record.
- HVAC sizing and zoning calculations.
- Fire & gas device list and area-classification confirmation (from `DEL-042-02`).
- Network infrastructure (passive) layout, rack list, structured-cabling records.
- Factory acceptance test (FAT) records.
- Bill of materials and as-built records for the physical building package.
- Interface compliance evidence for the eleven PKG-042 InterfaceTypes.
- Reference: Conflict Table dispositions captured in `Guidance.md`.
