# Specification: DEL-038-05 — Vendor Document Turnover Package

## Scope

This specification establishes the requirements for the Vendor Document Turnover Package for PKG-038 (600V ELECTRICAL BUILDING, 820-1). The deliverable is a single Package-Vendor production unit comprising the vendor document register, vendor document submittals, source-required vendor documentation (carried as artifacts where available), and turnover records, with EPC Integrator interface/integration review. (Source: Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-038-05; `_CONTEXT.md`.)

**Inclusions.** Vendor-originated documentation for the 600V electrical building package: as-built drawings, vendor datasheets, certified test reports, inspection certificates, factory acceptance documentation, installation/commissioning manuals, operation/maintenance manuals, spare-parts lists, and turnover documentation prepared by the Package Vendor for handoff to the EPC Integrator and Operator. (ASSUMPTION: conventional vendor turnover scope; the exact required document classes are not enumerated in the available DBM source slice.)

**Exclusions.** Standalone deliverables produced by other roles for this package (DEL-038-01 SOW, DEL-038-02 Package Datasheet, DEL-038-03 CWP, DEL-038-04 Vendor Engineered Equipment Package, DEL-038-06 EPC Vendor Package Review and Acceptance) are out of scope here; this deliverable supplies the turnover documentation set referenced by them. (Source: Gate 7 `DELIVERABLE_REGISTER.csv`.)

## Requirements

| Req ID | Requirement | Authority |
|---|---|---|
| R-038-05-01 | The Package Vendor shall produce and maintain a Vendor Document Register listing every document required for turnover, with document number, title, revision, submittal status, review status, and due date. | `_CONTEXT.md` anticipated artifacts; Gate 7 `DELIVERABLE_REGISTER.csv` (ASSUMPTION on minimum register columns) |
| R-038-05-02 | The Package Vendor shall submit vendor document submittals through the submittal workflow established by the EPC Integrator and shall track each submittal to disposition. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` (ASSUMPTION on workflow specifics; location TBD) |
| R-038-05-03 | Source-required vendor documentation listed in the governing package-requirements basis shall be carried as artifacts/evidence within this deliverable where the source rows are available. | Gate 7 `DELIVERABLE_REGISTER.csv` notes column |
| R-038-05-04 | The Package Vendor shall produce turnover records demonstrating that vendor-scope work, equipment, and documentation have been completed, tested, and transferred to the EPC Integrator/Operator. | `_CONTEXT.md` anticipated artifacts; Gate 7 `DELIVERABLE_REGISTER.csv` |
| R-038-05-05 | The EPC Integrator shall perform an interface/integration review of the vendor documentation prior to acceptance against the EPC SOW (DEL-038-01), Package Datasheet (DEL-038-02), and CWP (DEL-038-03). | Gate 7 `DELIVERABLE_REGISTER.csv` (ResponsibleParty column) |
| R-038-05-06 | Vendor documentation shall reflect equipment, materials, fabrication, installation, testing, and inspection performed under the governing electrical standards: CSA C22.1-21 Canadian Electrical Code; BC provincial/local electrical codes; applicable CSA, API, IEEE, ISA, NEMA standards; and the authority of WorkSafeBC, Technical Safety BC, and BCER. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866 |
| R-038-05-07 | Vendor documentation shall be consistent with the prefabricated/modular electrical-building construction basis (HVAC n+1, bottom cable entry, equipment-door sizing, TECK/ACIC cable wiring, GFI receptacle, two-point ground-grid connections). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. "Electrical Buildings" (L2971-2999) |
| R-038-05-08 | The complete list of vendor document types, revisions, and acceptance criteria is `TBD` and shall be defined against `26020-Package_Requirements.docx` (workbook package-requirements basis). | `_REFERENCES.md`; ASSUMPTION — package-specific row for PKG-038 not located in accessible source |

## Standards

| Standard / Reference | Use | Location |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Governing electrical code for the package | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866 |
| BC provincial/local electrical codes; Technical Safety BC | Provincial regulatory compliance | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866 |
| Applicable CSA, API, IEEE, ISA, NEMA standards | Discipline standards bracketed by detailed design | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866 |
| `26020-Package_Requirements.docx` | Package-requirements document basis for vendor document scope | `_REFERENCES.md`; location of PKG-038 specific row TBD |
| Project specifications (Propak) | Discipline package specifications | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3360 |

## Verification

| Req ID | Verification approach |
|---|---|
| R-038-05-01 | Register inspection: confirm completeness, schema, and currency against the submittal log. |
| R-038-05-02 | Submittal-log audit: every required document has a submittal record and a disposition. |
| R-038-05-03 | Cross-check: each source-listed vendor document row is represented as an artifact or marked unavailable with rationale. |
| R-038-05-04 | Turnover-record review against acceptance checklist in DEL-038-06. |
| R-038-05-05 | Evidence of EPC Integrator review entries against SOW/Datasheet/CWP. |
| R-038-05-06 | Documentation review confirms cited code/standard compliance statements. |
| R-038-05-07 | Cross-reference vendor documentation against DBM Electrical-Buildings construction basis. |
| R-038-05-08 | Closure of TBD list once the PKG-038 row in `26020-Package_Requirements.docx` is accessible. |

## Documentation

Required artifacts to be produced by this deliverable (from `_CONTEXT.md`):

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records
