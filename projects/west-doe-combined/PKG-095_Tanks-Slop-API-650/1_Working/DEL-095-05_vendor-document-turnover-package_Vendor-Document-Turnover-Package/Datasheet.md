# Datasheet — DEL-095-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-095-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-095` |
| PackageName | Tanks, Slop (API 650) |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| CoversScopeItems | SOW-0213; SOW-0214; SOW-0215; SOW-0216 |
| SupportsObjectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |
| SourceReference | Workbook Packages row 91; 26020-Package_Requirements.docx package heading 47 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment anchor | API 650 modified atmospheric slop storage tank, likely TK-9130-2, with appurtenances, drain/recycle/truck-out connections, and standard tank instrumentation | SCOPE_LEDGER SOW-0215 (heading 47, Major included equipment) |
| Service class | Slop — off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate | SCOPE_LEDGER SOW-0214; SOW-0216 (heading 47) |
| Vendor responsibility framing | Workbook-defined vendor-responsible Mechanical package; Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration | SCOPE_LEDGER SOW-0213 (Workbook Packages row 91) |
| Required deliverable element — vendor document register | Required for Mechanical packages per DBM Mechanical Package Structure | DBM-Comp_and_Liquids §"Mechanical Package Structure" (line 617) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Receiving review party | EPC Integrator interface/integration review | DELIVERABLE_REGISTER row DEL-095-05 |
| Source list / disposition path / tank design basis | Final list/path/basis require process confirmation | SCOPE_LEDGER SOW-0216 (heading 47, Scope notes and open items) |
| Document-class scope | Vendor document register; vendor document submittals; source-required vendor documentation; turnover records | DELIVERABLE_REGISTER row DEL-095-05 (Anticipated Artifacts) |

## Construction (Document Set Composition)

| Artifact Class | Inclusion | Source |
|---|---|---|
| Vendor Document Register | Required | DBM §Mechanical Package Structure; DELIVERABLE_REGISTER row DEL-095-05 |
| Vendor Document Submittals (issued documents) | Required | DELIVERABLE_REGISTER row DEL-095-05 |
| Source-required vendor documents (rows from source vendor document table) | Required where source table rows are available; carried as artifacts/evidence | DELIVERABLE_REGISTER row DEL-095-05; _CONTEXT Notes |
| Turnover Records (final handover evidence) | Required | DELIVERABLE_REGISTER row DEL-095-05 |
| Individual source vendor document table rows | Artifacts/evidence within this package — NOT separate deliverables | _CONTEXT Notes |

ASSUMPTION: Specific document classes (e.g., GA drawings, IOM manuals, MTRs, NDE reports, pressure test certs, calibration certs, weld maps, coating reports) typical for an API 650 atmospheric tank package are likely required by the source vendor document table at 26020-Package_Requirements.docx heading 47. Exact list TBD — heading-47 source slice not extracted locally beyond SCOPE_LEDGER summary rows.

## References

- `_REFERENCES.md` (this deliverable)
- Gate 7 published PROJECT_DECOMP snapshot
- `DELIVERABLE_REGISTER.csv` row `DEL-095-05`
- `SCOPE_LEDGER.csv` rows `SOW-0213`..`SOW-0216`
- `_Sources/26020-Package_Requirements.docx` heading 47 (binary; not locally extracted as markdown — location TBD for clause-level rows)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Mechanical Package Structure" (line 617)
