# Datasheet: DEL-076-06 — EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-076-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-076` |
| PackageName | Lube Oil Supply |
| WorkbookID | 76 |
| WorkbookRow | 70 |
| WBS | 01 |
| CoATrackingNumber | 26020-01-29-001 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | SOW-0135; SOW-0136; SOW-0137; SOW-0138 |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION; package-grouping heuristic per `_CONTEXT.md`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Reviewed package | PKG-076 Lube Oil Supply (two lube oil transfer pumps for West Doe Deepcut Storage Tank Area serving all compressor packages on site) | PACKAGE_REGISTER.csv row PKG-076 |
| Major equipment under review | P-9240-1 Cylinder Lube Oil Transfer Pump; P-9250-1 Crankcase Lube Oil Transfer Pump; horizontal split storage tank (crankcase + compressor packing); electric-motor-driven pumps; sweet and sour service | ARTIFACT_REGISTER.csv ART-D795C57849 |
| Review baseline | EPC Scope of Work (DEL-076-01); Package Datasheet (DEL-076-02); Construction Work Package (DEL-076-03) | `_CONTEXT.md` Scope |
| Vendor-side counterpart | Vendor Engineered Equipment Package (DEL-076-04); Vendor Document Turnover Package (DEL-076-05) | DELIVERABLE_REGISTER.csv |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sweet and sour lube oil transfer | ART-D795C57849 |
| Drive | Electric motor driven | ART-D795C57849 |
| Process function | Lube oil supply | PACKAGE_REGISTER.csv |
| Detailed process/operating conditions (pressures, temperatures, flow rates) | location TBD (`26020-Package_Requirements.docx` package heading 30 not locally machine-readable; not extracted at PREPARATION) | `_REFERENCES.md` Missing/Deferred |

## Construction

This deliverable is a review and acceptance record set, not a physical construction artifact. The constructed object reviewed is the Lube Oil Supply package.

| Item | Value | Source |
|---|---|---|
| Acceptance review artifacts (per artifact register) | Vendor document review and comment log (ART-CE37DAAF83); Vendor package acceptance and turnover checklist (ART-36208600FC); Factory/shop test and inspection evidence (ART-F44CA74291) | ARTIFACT_REGISTER.csv (DEL-076-06 rows) |
| Anticipated artifacts (`_CONTEXT.md`) | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Interface scope subject to acceptance | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv PKG-076 (IFC-B592C2D9F7, IFC-09EA6BEDB8, IFC-4D53A7E70E, IFC-7117284B73, IFC-986D504634, IFC-8C17CDE23B, IFC-6D43DAF029, IFC-ACA2756AA0) |
| Acceptance pass/fail criteria | TBD (derive from accepted DEL-076-01 Scope of Work, DEL-076-02 Package Datasheet, DEL-076-03 Construction Work Package once those are accepted) | DEPENDENCY (declared none at PREPARATION; semantic upstream from sibling deliverables) |

## References

- `_CONTEXT.md` (this folder)
- `_REFERENCES.md` (this folder)
- DELIVERABLE_REGISTER.csv — Gate 7 snapshot row `DEL-076-06_epc-vendor-package-review-and-acceptance`
- PACKAGE_REGISTER.csv — Gate 7 snapshot row `PKG-076`
- ARTIFACT_REGISTER.csv — Gate 7 snapshot rows ART-CE37DAAF83, ART-36208600FC, ART-F44CA74291, ART-D795C57849
- INTERFACE_REGISTER.csv — Gate 7 snapshot rows for PKG-076 (eight interface rows enumerated above)
- `26020-Package_Requirements.docx` package heading 30 — referenced but `location TBD` (binary `.docx` not extracted at PREPARATION)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Word Source Basis cited for PKG-076 in PACKAGE_REGISTER.csv; specific section relevant to acceptance criteria `location TBD`
