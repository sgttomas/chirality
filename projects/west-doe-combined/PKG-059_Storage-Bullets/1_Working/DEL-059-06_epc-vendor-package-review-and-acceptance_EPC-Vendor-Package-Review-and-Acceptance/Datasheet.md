# Datasheet — DEL-059-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-059-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-059 |
| PackageName | Storage Bullets |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers SOW Items | SOW-0181; SOW-0182; SOW-0183; SOW-0184 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |
| Source Reference | Workbook Packages row 83; 26020-Package_Requirements.docx package heading 14 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance subject | Vendor-engineered NGL storage bullet package (PKG-059) | `_CONTEXT.md`; DELIVERABLE_REGISTER row 467 |
| Acceptance basis documents | EPC Scope of Work (DEL-059-01); Package Datasheet (DEL-059-02); Construction Work Package (DEL-059-03) | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER rows 462-464 |
| Vendor inputs reviewed | Vendor engineered equipment package (DEL-059-04); Vendor document turnover package (DEL-059-05) | DELIVERABLE_REGISTER rows 465-466 |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Storage bullet count and size (acceptance scope) | 16 x 120,000 USG NGL storage bullets at 04-25 | `4-25_Deepcut_DBM.md` line 1629 (NGL Storage Bullets) |
| Bullet service | Processed NGL product storage; replaces retired C3/C4 storage scope | `4-25_Deepcut_DBM.md` line 1629 |
| Governing spacing/siting standard | API 2510 (pressurized bullet spacing table) | `4-25_Deepcut_DBM.md` lines 245-266 (Pressurized Bullet Spacing) |
| Detailed bullet design parameters | TBD — not fully developed in available product-storage basis; flagged as required design-development item | `4-25_Deepcut_DBM.md` line 1629 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Pressurized bullets per cluster (max) | <= 6 | `4-25_Deepcut_DBM.md` line 249 (API 2510) |
| Distance between bullet clusters | 15.24 m (50 ft) | `4-25_Deepcut_DBM.md` line 250 (API 2510) |
| Bullet to property line | 38.1 m (125 ft) | `4-25_Deepcut_DBM.md` line 259 (API 2510 Table 1) |
| Bullet to flare | 30.48 m (100 ft) | `4-25_Deepcut_DBM.md` line 284 (API 2510) |
| Bullet to fired heater | 15.24 m (50 ft) | `4-25_Deepcut_DBM.md` line 299 (API 2510) |
| Bullet to atmospheric tank | 30.48 m (100 ft) | `4-25_Deepcut_DBM.md` line 265 |
| Bullet to spill containment area | 3.05 m (10 ft) | `4-25_Deepcut_DBM.md` line 266 |
| NGL grading requirement | Slope underneath bullets (potentially southbound) to redirect spill away from pipe rack/process areas | `4-25_Deepcut_DBM.md` line 2722 |
| Operating envelope (pressure/temperature/composition) | TBD — bullet-level operating envelope not stated in available source slices | `4-25_Deepcut_DBM.md` line 1629 (design parameters TBD) |

## Construction

| Item | Value | Source |
|---|---|---|
| Shop vs field assembly | TBD | location TBD |
| Materials of construction | TBD | location TBD |
| Code stamp | TBD (ASME / CRN expectations to be confirmed against package datasheet DEL-059-02) | location TBD |
| Inspection and test (ITP) | TBD — to be supplied by vendor and reviewed by EPC | ASSUMPTION (standard EPC acceptance practice) |
| Turnover documentation set | Vendor document register, submittals, source-required vendor documentation, turnover records | DELIVERABLE_REGISTER row 466 (DEL-059-05 scope) |

## References

- `_CONTEXT.md` — deliverable identity and scope.
- `_REFERENCES.md` — reference index.
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) row 467 — this deliverable.
- DELIVERABLE_REGISTER.csv rows 462-466 — sibling PKG-059 deliverables forming the acceptance basis.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — NGL storage bullet basis (line 1627 NGL Storage Bullets; lines 245-266 Pressurized Bullet Spacing; line 2722 NGL grading).
- 26020-Package_Requirements.docx package heading 14 — binary source; source slice not locally extracted (location TBD).
- API 2510 — referenced by DBM for bullet siting (text not locally available).
