# Procedure: DEL-061-04 Vendor Engineered Equipment Package — NGL Booster and Transfer Pumps Building

This procedure describes the steps to **produce and deliver** the vendor-engineered equipment package for `PKG-061`. Steps for operating the installed equipment are not in scope (those belong with vendor IOM documentation included in `DEL-061-05`).

## Prerequisites

- EPC Scope of Work (`DEL-061-01`) issued by EPC Integrator.
- EPC Package Datasheet (`DEL-061-02`) issued by EPC Integrator — design inputs (flow, head, NPSHa, suction/discharge pressures, temperatures, NGL composition, MOC class, sparing, driver basis, area classification, site/climate).
- Local reference materials accessible:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Trace Appendix row 58; sister-service design patterns).
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at PREPARATION (functional upstream is `DEL-061-01` and `DEL-061-02` per decomposition; not yet declared in `Dependencies.csv`).
- Resolution of (or `TBD` acceptance of) duty data items currently flagged "location TBD: `26020-Package_Requirements.docx` package heading 17."

## Steps

1. **Receive and log EPC inputs.** Receive `DEL-061-01` (SOW) and `DEL-061-02` (Package Datasheet) from EPC Integrator. Log into vendor document control.
2. **Confirm scope and tag list.** Verify that the vendor scope covers two pumps tagged `P-9570-1` and `P-9580-1` of API 610 multi-stage can configuration (DBM-Deepcut Trace Appendix row 58). Reconcile any deviation with EPC Integrator.
3. **Develop vendor package design basis.** Translate `DEL-061-02` duty data into a vendor design basis covering: design flow, differential head, NPSHa/NPSHr margin, suction/discharge conditions, NGL composition, site/climate envelope (including -40 deg C startup if applicable — DBM-Deepcut line 1679 precedent), area classification, sparing philosophy.
4. **Select pump model and accessories.** Select API 610 multi-stage can pump model meeting the design basis. Select coupling, baseplate, mechanical seal system (API 682 — ASSUMPTION pending `DEL-061-02` confirmation), seal flush plan, driver, motor accessories, and local instrumentation.
5. **Issue vendor datasheet set.** Produce datasheets for: pump, driver/motor, mechanical seal, coupling, baseplate, local instruments. Each datasheet cites `DEL-061-02` and the governing standard.
6. **Issue package interface matrix.** Document mechanical (suction/discharge nozzle list, lube oil, vents/drains), electrical (motor power, control wiring), I&C (signals to DCS), civil/structural (anchor loads, foundation interface), HSE (noise, emissions, fire/gas) interfaces for EPC Integrator review.
7. **Submit for EPC integration review.** Submit design basis, datasheets, interface matrix, and compliance statements to EPC Integrator for `DEL-061-06` review.
8. **Incorporate review comments.** Resolve EPC integration review comments; reissue affected documents.
9. **Manufacture / procure.** Fabricate or procure the engineered package per the issued design.
10. **Inspection and Test Plan execution.** Perform inspections and tests per the project ITP; specific FAT scope `TBD` and to be defined per project requirements.
11. **Factory Acceptance Test (FAT).** Execute FAT for each pump (mechanical run test, performance test per API 610 acceptance grade — grade `TBD`).
12. **Pre-shipment release.** Obtain EPC Integrator release for shipment after FAT and document review.
13. **Ship and deliver.** Ship the engineered equipment package(s) to site per the agreed schedule.
14. **Vendor turnover documentation handoff.** Provide all vendor turnover documents to `DEL-061-05` (Vendor Document Turnover Package).

## Verification

| Verification check | Method | Pass criterion |
|---|---|---|
| Equipment count and tag list correct | Document review against DBM-Deepcut Trace Appendix row 58 and `DEL-061-02` | 2 pumps, tags `P-9570-1`, `P-9580-1` |
| Configuration matches DBM | Vendor datasheet vs. DBM | API 610, multi-stage can |
| Duty matches EPC Datasheet | Cross-reference vendor datasheet vs. `DEL-061-02` | All duty fields traced; no unresolved discrepancies |
| Interface matrix complete | Review with EPC Integrator | All mechanical, electrical, I&C, civil/structural, HSE interfaces listed and agreed |
| Standards compliance | Compliance statements reviewed | API 610 (edition `TBD`), API 682 (ASSUMPTION), motor standard (`TBD`) |
| FAT acceptance | FAT report | API 610 performance tolerances met (acceptance grade `TBD`) |

## Records

- Vendor package design basis document.
- Vendor datasheet set (pump, driver, seal, baseplate, instruments).
- Package interface matrix.
- Standards compliance statements.
- Inspection records and Material Test Reports (MTRs).
- FAT report and signed acceptance.
- Shipping release documentation.
- Vendor turnover documents (handed off to `DEL-061-05`).
