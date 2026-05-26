# Datasheet — DEL-069-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-069-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-069 |
| PackageName | Mole Sieve Drier Unit (Gas) |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | SOW-0144 |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 |
| Source Reference | Workbook Packages row 73 (location TBD — source workbook is a binary `.xlsx`, row text not locally extracted) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable form | Compiled vendor document set covering register, submittals, source document rows as artifacts where available, and turnover records | _CONTEXT.md (Scope, Anticipated Artifacts) |
| Subject equipment | Process-gas molecular sieve dehydration unit (3 driers: 2 adsorption + 1 standby/regeneration/cooling) | DBM-Deepcut/4-25_Deepcut_DBM.md sec. "Molecular-Sieve Bed and Regeneration Basis" |
| Tag scope (per DBM equipment-by-package row 56) | AC-6180-1, K-6190-1, K-6195-1, F-5910-1, F-5920-1, F-6151-1, F-6155-1, E-6170-1, V-6160-1, V-6130-1, V-6140-1, V-6150-1, V-6185-1 | DBM-Deepcut/4-25_Deepcut_DBM.md line 2607 (PKG row 56, Mole Sieve Drier Unit (Gas)) |
| Document classification basis | TBD — Workbook Packages row 73 vendor document list not locally accessible (binary `.xlsx`) | _REFERENCES.md (Missing/Deferred References) |
| Turnover acceptance authority | EPC Integrator (interface/integration review); final acceptance authority TBD pending project document control matrix | _CONTEXT.md (ResponsibleParty); document control matrix not in accessible sources |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Equipment operating envelope context (drives required certification scope) | Normal inlet 1078 psig (TBC); summer inlet 105 degF / winter 61 degF; inlet flow 332.6 MMSCFD adsorption + 25.45 MMSCFD regeneration | DBM-Deepcut/4-25_Deepcut_DBM.md sec. "Molecular-Sieve Equipment, Controls, and Protection" / Bed and Regeneration Basis |
| Vessel flange rating context | Molecular sieve system requires 900# flanges | DBM-Deepcut/4-25_Deepcut_DBM.md line 628 |
| Adsorbent identity (drives vendor material certifications) | 3A molecular sieve mandatory; 4A and 5A not permitted | DBM-Deepcut/4-25_Deepcut_DBM.md line 1269 |
| Protective media | Silica gel layer for upstream liquid carryover protection | DBM-Deepcut/4-25_Deepcut_DBM.md line 1270 |
| Adsorbent life expectation | Typical 3 years TBC by vendor; 5-year extension to be reviewed | DBM-Deepcut/4-25_Deepcut_DBM.md line 1271 |
| Turnover trigger conditions | Vendor document set required at: PO award (initial register), submittal milestones, FAT, shipment, and mechanical completion turnover | ASSUMPTION (standard EPC vendor doc lifecycle; not anchored to project-specific schedule in accessible sources) |

## Construction (Document Set Composition)

| Document Class | Representative Items | Source |
|---|---|---|
| Vendor Document Register | Master list of all vendor documents with revision, status, transmittal/submittal references, and turnover status | _CONTEXT.md (Anticipated Artifacts) |
| Vendor Document Submittals | Issued vendor documents per the register (drawings, datasheets, calculations, manuals, certifications) | _CONTEXT.md (Anticipated Artifacts) |
| Source Vendor Document Table Rows (as artifacts) | Individual rows from the source vendor document table retained as evidence where available | _CONTEXT.md (Anticipated Artifacts; Notes) |
| Turnover Records | Mechanical completion / package turnover packets, As-Built drawings, vendor manuals, spare parts lists, certifications, inspection/test records | _CONTEXT.md (Anticipated Artifacts); ASSUMPTION on specific contents — not enumerated in locally accessible source |
| Equipment-specific certifications | ASME U-Stamp / CRN as applicable for adsorber vessels; vendor process guarantees for adsorbent loading, bed pressure drop (SOL <4 psid; EOL incl. nozzles <10 psid), regeneration thermal efficiency (<40%) | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1268, 1272 (parameters); ASME/CRN applicability ASSUMPTION based on cryogenic-section precedent (line 1324) |

## References

- Decomposition entry: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-069-05)
- DBM source (accessible): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections: Molecular-Sieve Bed and Regeneration Basis; Molecular-Sieve Equipment, Controls, and Protection; Equipment-by-Package table row 56)
- Workbook Packages row 73 — source `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; not text-extracted) — **location TBD**
- Package Requirements — `_Sources/26020-Package_Requirements.docx` (binary; not text-extracted) — **location TBD**
- _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md (deliverable-local)
