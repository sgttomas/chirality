# Procedure: DEL-035-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the EPC Integrator procedure for producing the EPC Vendor Package Review and Acceptance deliverable for `PKG-035`, the 13.8 kV switchgear electrical building (810-1). The procedure turns vendor documentation, factory/shop test records, inspection records, and EPC integration evidence into an auditable acceptance and turnover package.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-035-06_epc-vendor-package-review-and-acceptance`; `PACKAGE_REGISTER.csv` row `PKG-035`; `ARTIFACT_REGISTER.csv` rows `ART-AA841F7CA1`, `ART-72A172E45B`, and `ART-7F4CFC552C`.

## Prerequisites

| Prerequisite | Required input / condition | Source |
|---|---|---|
| Accepted decomposition basis | Gate 7 final published PROJECT_DECOMP snapshot is the accepted package, deliverable, artifact, interface, objective, and scope basis. | `_REFERENCES.md`; Gate 7 registers |
| Vendor package identity | `PKG-035`, workbook ID 35, workbook row 37, WBS 01, CoA tracking number `26020-01-30-026`. | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-035`; `OBJECTIVE_REGISTER.csv` OBJ-004 |
| Upstream acceptance basis | EPC Scope of Work, Package Datasheet, and Construction Work Package for `PKG-035`. | `DELIVERABLE_REGISTER.csv`; `SCOPE_LEDGER.csv` `SOW-0036` |
| Vendor documentation set | Vendor document submissions and vendor-document turnover package for the 13.8 kV switchgear electrical building. Specific vendor-document table rows are `TBD` pending extraction from `_Sources/26020-Package_Requirements.docx`. | `OBJECTIVE_REGISTER.csv` OBJ-004 and OBJ-010; `_REFERENCES.md` |
| Factory/shop evidence | Factory/shop test and inspection records for the shop-built 810-1 building and its 13.8 kV switchgear. Detailed witness/hold-point criteria are `TBD` pending source-slice extraction from `_Sources/26020-Package_Requirements.docx`. | `ARTIFACT_REGISTER.csv` `ART-7F4CFC552C`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table |
| Interface list | Twelve `PKG-035` interface facts covering utility piping, drain/containment, electrical power, grounding/bonding, area/exterior lighting, I&C/control cabling, communications/network, building HVAC/services, fire and gas/safety systems, maintenance access, grading/site drainage/spill containment, and structural/foundations/supports. | `INTERFACE_REGISTER.csv` rows for `PKG-035` |
| Declared deliverable dependencies | None declared during PREPARATION. | `_DEPENDENCIES.md` |

## Steps

1. Confirm the acceptance package identity.
   - Record deliverable ID `DEL-035-06_epc-vendor-package-review-and-acceptance`, package ID `PKG-035`, package name `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, discipline Electrical, and responsible party EPC Integrator with Package Vendor input.
   - Verify the acceptance record is for EPC review and acceptance only; do not recast vendor engineering, vendor design, or vendor documentation authorship as EPC-authored work.

2. Establish the acceptance basis.
   - List the EPC Scope of Work, Package Datasheet, and Construction Work Package items that the vendor package must satisfy.
   - Tie the basis to `SOW-0036`, which carries the vendor-responsible electrical package under WBS 01 with vendor engineering/design/equipment and EPC facility integration.
   - Mark any upstream acceptance-basis item not available in the folder as `TBD` rather than inventing acceptance criteria.

3. Build the vendor document review and comment log.
   - Create or update the vendor document review log identified as `ART-AA841F7CA1`.
   - For each vendor submission, record document number, title, revision, received date, EPC reviewer, review status, comments, vendor response, disposition, and revision that closes the comment.
   - Where the governing vendor document table is not available from `_Sources/26020-Package_Requirements.docx`, flag the table reference as `TBD` and carry the gap into the Conflict Table in `Guidance.md`.

4. Compile factory/shop test and inspection evidence.
   - Collect FAT records, shop inspection reports, witness/hold-point records, nonconformance reports, and vendor test certificates applicable to Building 810-1 and its 13.8 kV switchgear.
   - Confirm the evidence addresses the DBM basis that Building 810-1 is shop-built and that the 13.8 kV switchgear is the plant main power distribution centre sized for the full facility scope.
   - Treat detailed witness/hold-point scope as `TBD` until the applicable vendor specification or package-requirements source slice is extracted.

5. Verify electrical-building configuration evidence.
   - Confirm the vendor evidence addresses prefabricated modular electrical-building construction in a general purpose area.
   - Confirm HVAC is sized as an n+1 system so cooling tolerates failure or maintenance shutdown of one unit without affecting building heating and cooling.
   - Confirm bottom entry for incoming and outgoing power cables and elevated installation on piles with space below the building for cable tray routing.
   - Confirm equipment doors are sized for, or include removable transom sections to allow, removal of the largest equipment.
   - Confirm major electrical equipment is directly connected to the ground grid at two points and that ground wells with bolted test points are provided at the electrical building.

6. Verify code, standards, and inspection-authority conformance.
   - Obtain vendor conformance evidence for CSA C22.1-21 Canadian Electrical Code, applicable BC provincial/local electrical codes and regulations, and the electrical inspection authority designated by Tourmaline Oil Corp.
   - Record applicable CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, and BCER conformance evidence where relevant to the vendor package.
   - Record deviations or exceptions for formal owner approval rather than accepting them silently.

7. Close the twelve declared interface facts.
   - Add an acceptance-checklist line for each `PKG-035` interface fact in `INTERFACE_REGISTER.csv`.
   - For electrical power, verify evidence that the 13.8 kV bus and feeders support downstream electrical buildings.
   - For grounding/bonding, verify two-point ground-grid connections and ground-well test points.
   - For building HVAC/services, verify n+1 HVAC evidence.
   - For maintenance access, verify equipment door/transom and cable-tray/conduit routing do not block maintenance access.
   - For interfaces where only the register row is available, record `TBD` for detailed acceptance criteria and assign the owner for source resolution.

8. Prepare the vendor package acceptance and turnover checklist.
   - Create or update the acceptance and turnover checklist identified as `ART-72A172E45B`.
   - Include checklist sections for vendor documentation, FAT/shop inspection, electrical-building configuration, code/standards conformance, interface closure, open items, and handoff records.
   - Include sign-off lines for EPC Integrator acceptance and Package Vendor input.

9. Record open items and acceptance exceptions.
   - Log every unresolved vendor response, missing document, unclosed interface, source-slice gap, inspection nonconformance, or acceptance exception.
   - Assign owner, required closure evidence, due date, and downstream impact.
   - Do not close an item by narrative assertion; closure requires a source document, test/inspection record, interface evidence entry, or signed acceptance checklist line.

10. Assemble turnover evidence.
   - Collate the vendor document review log, acceptance and turnover checklist, factory/shop test and inspection evidence, open-items closure log, conformance evidence, and handoff record.
   - Preserve references to the Gate 7 package, deliverable, artifact, scope, objective, and interface register rows used as the acceptance basis.

## Verification

| Check | Acceptance criterion | Evidence / record |
|---|---|---|
| Identity check | Deliverable, package, workbook row, WBS, discipline, and responsible party match the Gate 7 registers. | Acceptance package cover sheet; `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv` |
| Responsibility check | Vendor-owned engineering/design/documentation/equipment and EPC-owned integration are separated. | Acceptance checklist responsibility section |
| Document review check | Vendor document review log exists and all available vendor submissions have disposition status. | `ART-AA841F7CA1` |
| Test/inspection check | Factory/shop test and inspection evidence is present or missing evidence is logged as an open item. | `ART-7F4CFC552C`; open-items log |
| Interface check | All twelve `PKG-035` interface facts have checklist entries and closure status. | `INTERFACE_REGISTER.csv`; acceptance checklist |
| Electrical basis check | Main 13.8 kV distribution role, shop-built building, n+1 HVAC, bottom-entry/elevated installation, equipment access, and grounding provisions are verified or carried as open items. | DBM electrical-basis source slices; vendor evidence |
| Standards check | Applicable codes, standards, regulatory bodies, and inspection-authority requirements are addressed or exceptions are formally recorded. | Vendor conformance statement; inspection-authority correspondence |
| Open-item check | Each unresolved item has owner, closure evidence, due date, and downstream impact. | Open-items closure log |
| Turnover check | Turnover file contains review log, checklist, test/inspection evidence, open-items status, and handoff record. | Turnover evidence package |

## Records

- Vendor document review and comment log (`ART-AA841F7CA1`).
- Vendor package acceptance and turnover checklist (`ART-72A172E45B`).
- Factory/shop test and inspection evidence (`ART-7F4CFC552C`).
- Vendor conformance statements and inspection-authority correspondence.
- Twelve-interface closure checklist for `PKG-035`.
- Open-items and exception closure log.
- Turnover evidence file documenting handoff readiness.

## Source Notes

- Gate 7 registers were used as accepted upstream decomposition truth: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 Electrical Basis was used for the 13.8 kV switchgear, electrical-building, grounding, cabling, code, and standards basis.
- `_Sources/26020-Package_Requirements.docx` is referenced by the decomposition for vendor-document and handoff evidence but was not available as an extracted source slice in this pass; detailed table and witness/hold-point requirements remain `TBD`.
