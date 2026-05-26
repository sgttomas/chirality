# Procedure — DEL-060-03 Construction Work Package

This Procedure describes the operational steps to **produce** the Construction Work Package artifact set for PKG-060 (Tank Farm Pump Building 4-25) and to **use** it during construction execution and turnover. It is consistent with the Specification (`Specification.md`) and the Datasheet (`Datasheet.md`) of this deliverable.

## Prerequisites

Inputs that must be available before producing or executing the CWP:

- Accepted PKG-060 Scope of Work (`DEL-060-01_scope-of-work`) — package scope, boundaries, and responsibility narrative.
- Accepted PKG-060 Package Datasheet (`DEL-060-02_package-datasheet`) — vendor handoff technical basis and interface requirements matrix.
- Vendor Engineered Equipment Package (`DEL-060-04_vendor-engineered-equipment-package`) issued for construction — confirmed equipment list, foundations interface drawings, electrical loads, instrument list, building drawings.
- Vendor Document Turnover Package (`DEL-060-05_vendor-document-turnover-package`) — relevant submittals required for installation (vendor IOMs, datasheets, certs, P&IDs).
- GATE-07 PROJECT_DECOMP snapshot artifacts: `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `SCOPE_LEDGER.csv`.
- DBM-Deepcut SEC-01 Construction Responsibility and SEC-02.2 Site Data.
- BC Energy Regulator permit amendment and Section 12.4 site alteration permit (location TBD).
- Owner construction safety standards and turnover acceptance criteria (TBD).
- `_DEPENDENCIES.md` (declared upstream/downstream) — currently lists no declared edges; coordinate with `Dependencies.csv` if generated.

## Steps

### Phase A — Produce the CWP artifact set

1. **Confirm package scope and identity.** Read `_CONTEXT.md`, the PKG-060 row in `PACKAGE_REGISTER.csv`, and the DEL-060-03 row in `DELIVERABLE_REGISTER.csv`. Record DeliverableID, package contents, applicable interface types, and supported objectives.
2. **Compile installation basis.** From the Package Datasheet (`DEL-060-02_package-datasheet`) and vendor package, extract foundation loads, electrical loads, instrument I/O, building footprint, and lift weights/dimensions needed for installation planning. Where vendor data is pending, mark `TBD`.
3. **Author the Construction Work Package (ART-F8F13A9988).** Structure to cover: package identity; scope of construction; sequence of work; construction responsibility matrix (echoing DBM SEC-01 and PKG-060 by-others items); cold-weather provisions; permit conditions; safety and environmental controls; QA/QC plan; turnover criteria.
4. **Author the Installation and Tie-In Workface Plan (ART-538DFF5CDE).** For each applicable PKG-060 interface type (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports), produce a workface card with tie-in location, responsible party (confirmed per CWP-CFL-01), prerequisites, sequence, tools/crew, hold points, and acceptance evidence.
5. **Author the Construction Interface and Turnover Checklist (ART-4CE1B9B840).** One checklist row per applicable interface plus rows for: foundations sign-off, module setting sign-off, mechanical hookup sign-off, electrical termination sign-off, cable home-run installation sign-off, area lighting sign-off, DCS integration sign-off coordination, fire & gas integration sign-off, and pre-commissioning loop checks.
6. **Cross-check with sibling deliverables.** Verify that the CWP does not contradict DEL-060-01 scope, DEL-060-02 datasheet values, or DEL-060-04/05 vendor scope. Surface any conflicts in the Conflict Table in `Guidance.md`.
7. **Issue and record.** Issue CWP artifacts to the project document register and record the version/revision in this deliverable folder.

### Phase B — Execute construction using the CWP

8. **Pre-mobilization review.** Confirm permit conditions, environmental controls, and Owner safety standards are in force at site. Confirm cold-weather provisions are in place if ambient is below the cold-weather threshold (TBD; see Guidance).
9. **Foundations and grading.** Tourmaline executes grading, piling, and foundations per DBM SEC-01. EPC Integrator verifies conformance to vendor foundation interface drawings.
10. **Module / equipment receipt and setting.** Off-load, lay-down, inspect for shipping damage, and set modules, pipe racks, and equipment on foundations per Tourmaline field construction scope.
11. **Self-framing building erection.** Erect the site-built pump building per vendor drawings. Apply wind-loading constraints (DBM SEC-02.2) during erection.
12. **Mechanical hookup.** Install interconnecting piping and mechanical hookup of modules, equipment, and shipped-loose components. Verify no aluminium materials are introduced in caustic-service interfaces (REQ-CWP-11).
13. **Electrical hookup.** Install home-run cables, terminate at MCC and motors, install area lighting. Verify 575 V / 3 ph / 60 Hz motor configuration, DOL or VFD start, and local H-O-A or On-Off control (REQ-CWP-08).
14. **I&C and DCS integration.** Coordinate with controls discipline for DCS integration (by-others scope per SOW-0192). Loop-check instrumentation against vendor I/O list.
15. **Interface tie-ins.** For each PKG-060 interface type, execute per the workface card with the confirmed responsible party. Capture sign-off in the turnover checklist (REQ-CWP-06).
16. **Cross-facility metering verification.** For any tie-ins crossing facility boundaries (e.g., shared fuel gas/instrument air with 03-25), verify independent metering integrity (REQ-CWP-10).
17. **Pre-commissioning checks.** Run mechanical completion checks, electrical megger/continuity, instrument loop checks, leak tests, and rotation checks per pump.
18. **Turnover.** Complete the construction interface and turnover checklist with all sign-offs and turn the package over to commissioning/operations. Capture outstanding items as punch list with owners and due dates.

## Verification

| Verification | Method | Records |
|---|---|---|
| CWP artifact set completeness | Document audit of the three artifacts against `ARTIFACT_REGISTER.csv` rows. | Artifact register update. |
| Each PKG-060 interface type has a workface card and a turnover row | Cross-reference workface plan and turnover checklist against `INTERFACE_REGISTER.csv` PKG-060 rows. | Workface card index; checklist register. |
| Responsibility confirmations recorded per tie-in | Inspection of workface cards. | Workface cards. |
| Field configuration matches motor and starter basis | Field inspection during electrical hookup. | Electrical hookup ITRs. |
| No aluminium in caustic-service interfaces | Material conformance check. | Material conformance record. |
| Cold-weather construction provisions applied when required | Site inspection log. | Cold-weather construction log. |
| Independent metering preserved at cross-facility tie-ins | Metering verification. | Metering verification record. |
| Permit conditions respected | Compliance audit against permit amendment and Section 12.4 conditions (when available). | Permit compliance log (TBD). |

## Records

Records that should result from production and execution of this CWP:

- Construction Work Package document (ART-F8F13A9988) with revision history.
- Installation and Tie-In Workface Plan (ART-538DFF5CDE) with workface cards.
- Construction Interface and Turnover Checklist (ART-4CE1B9B840) with sign-offs.
- Per-interface responsibility confirmation records.
- Electrical, mechanical, and I&C ITRs (Inspection and Test Records).
- Material conformance records (caustic service).
- Cold-weather construction log (when applicable).
- Metering verification record (cross-facility tie-ins).
- Punch list at turnover with owners and due dates.
- Permit compliance log (TBD location).
