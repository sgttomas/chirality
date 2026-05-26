# Procedure — DEL-079-04 Vendor Engineered Equipment Package

## Purpose

Operationalize the production of the Vendor Engineered Equipment Package: from EPC handoff inputs (Scope of Work, Package Datasheet) through vendor engineering, fabrication, FAT, delivery, site receipt, and turnover to DEL-079-06 (EPC Vendor Package Review and Acceptance). The Procedure covers both producing the deliverable (vendor engineering) and using/operating it (site receipt and integration touch points). Operational running of the package after acceptance is out of scope.

## Prerequisites

Inputs required before vendor engineering can start:

- DEL-079-01 Scope of Work — issued and accepted by EPC Integrator.
- DEL-079-02 Package Datasheet — issued and accepted by EPC Integrator (technical handoff basis).
- `_REFERENCES.md` — confirms the authoritative decomposition basis and source materials.
- Locally accessible source slices (this run): `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Instrument Air sections and Skid-Edge isolation section.
- EPC-confirmed instrument count for sizing reconciliation (per Guidance, Principles).

Declared upstream dependencies per `_DEPENDENCIES.md`: none declared during PREPARATION (TBD pending dependency-extract run).

## Steps

### S-1 Confirm inputs
Vendor reviews DEL-079-01 (SOW) and DEL-079-02 (Package Datasheet) against the requirements set in this deliverable's Specification (R-1 through R-12). Flag any gap or contradiction in a clarification log to the EPC Integrator before proceeding.

### S-2 Sizing reconciliation
Reconcile the 1,113 SCFM consolidated demand (TBC per SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: L1923) against the EPC-supplied final instrument count. Apply per-instrument factors (0.5 / 1.0 SCFM) and 20 percent per-facility contingency exactly as the source basis prescribes (SectionRef: L1912). Document any deviation as a PROPOSAL for EPC ruling; do not silently re-roll the contingency.

### S-3 Select compressor and dryer
Select 2 x 100 percent capacity compressors with provision for a future third 100 percent unit (R-1). Rate at 930 kPag (135 psig) capacity condition (R-2). Select dryer to meet -73.3 deg C water dewpoint at 1000 kPag (R-4). Issue compressor and dryer datasheets.

### S-4 Receiver and reserve-volume design
Size dry receiver, wet receiver, and contributing header volume to deliver 15 minutes usable reserve from 120 psig down to 80 psig (R-5). Issue calculation memo with receiver geometry and assumed header volume contribution.

### S-5 PSV, piping, and skid-edge design
Set PSVs at or below 1034 kPag (R-8). Specify piping per ASME Category D where service permits (R-7). Implement skid-edge block valves on all services; OMIT spectacle blinds at instrument air skid-edge connections per explicit source exception (R-9; SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: L2452).

### S-6 Electrical and area-classification coordination
Coordinate driver class and electrical interface with EPC electrical lead (R-12). Validate the assumed General Purpose / Non-Classified building area classification with the EPC (R-11; SectionRef: L1943). Update area classification drawing if the assumption is not confirmed.

### S-7 Control narrative
Issue control narrative covering lead-lag changeover, header pressure regulation to 827 kPag normal supply, compressor shutdown at 1000 kPag, and facility shutdown at 482 kPag (R-3). Specific changeover setpoints are vendor scope; route through EPC controls review.

### S-8 Fabricate as shop-built skid
Fabricate as a shop-built modular package per the Modular Equipment List designation for the 420-1 Instrument Air Package (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: L2785).

### S-9 Factory Acceptance Test (FAT)
Execute FAT covering: lead-lag changeover; capacity at 930 kPag; dryer dewpoint at design and turndown; PSV bench certificate; control logic verification. Issue FAT report.

### S-10 Delivery and site receipt
Deliver to 04-25 (Deepcut) site. EPC Integrator performs receipt inspection per its own procedures; vendor supports and resolves discrepancies.

### S-11 Vendor document submittal
Submit the vendor document set to feed DEL-079-05 (Vendor Document Turnover Package). Detailed register format is governed there.

### S-12 Handoff to DEL-079-06
Transfer the package and documentation to the EPC Integrator for DEL-079-06 review and acceptance.

## Verification

| Step | Verification |
|---|---|
| S-1 | Vendor clarification log closed before kickoff |
| S-2 | Sizing memo reviewed and accepted by EPC Integrator |
| S-3 | Compressor / dryer datasheets approved |
| S-4 | Reserve-volume calculation accepted |
| S-5 | PSV certificates issued; P&IDs / line list approved; skid-edge interface drawing approved |
| S-6 | Electrical one-line approved; area classification drawing approved |
| S-7 | Control narrative and cause-and-effect approved by EPC controls |
| S-8 | Fabrication progress reports and weld/NDE records |
| S-9 | FAT report accepted by EPC Integrator |
| S-10 | Receipt inspection record (EPC) |
| S-11 | Vendor document register entries logged to DEL-079-05 |
| S-12 | Acceptance package transmitted to DEL-079-06 |

## Records

- Vendor clarification log
- Sizing calculation memo
- Equipment datasheets (compressor, dryer, filters, receivers)
- Skid GA, P&IDs, line list, isometrics
- Electrical one-line and area classification drawing
- Control narrative and cause-and-effect
- PSV calculations and certificates
- FAT procedure and FAT report
- Vendor O&M manual and spare parts list
- Shipping and receipt inspection records
- Submittal log feeding DEL-079-05

Final dispositioning of these records into the project document control system is handled by DEL-079-05 (Vendor Document Turnover Package) and DEL-079-06 (EPC Vendor Package Review and Acceptance).
