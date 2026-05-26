# Datasheet — EPC Vendor Package Review and Acceptance (DEL-099-06)

> Descriptive document. Identification and observable attributes of this review/acceptance deliverable for the Truck Product Loading Unit 3-25 vendor package.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-099-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-099` |
| PackageName | Truck Product Loading Unit 3-25 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | SOW-0241; SOW-0242; SOW-0243; SOW-0244 |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC) |
| Source Reference | Workbook Packages row 98; 26020-Package_Requirements.docx package heading 51 |

## Attributes

Attributes describe the EPC Integrator review/acceptance evidence package against the vendor-supplied Truck Product Loading equipment for Unit 3-25.

| Attribute | Value | Source |
|---|---|---|
| Package subject | Truck Product Loading (condensate product loading stations) for Unit 3-25 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row PKG-099 |
| Number of loading stations | 3 product truck-loading stations | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 (lines 414-415); SEC-06 ("three condensate truck-loading stations") |
| Loading pumps | 3 condensate loading pumps, one per station | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 414); SEC-08 (line 526) |
| Per-station loading capacity | 103 m3/h, 345 kPad differential | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 415) |
| Loading fluid | Product (sweet) condensate from product condensate storage | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 |
| Custody / metering boundary | LACT is third-party NRM scope; facility scope to tie-in flange | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-03 (line 22); SEC-06 (line 417) |
| Site low-temperature basis | -40 deg C minimum ambient governs exposed equipment, package buildings, panels, instrumentation | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04 (line 145) |
| Review lead | EPC Integrator | `_CONTEXT.md` ResponsibleParty |
| Reviewed inputs | Vendor Engineered Equipment Package (DEL-099-04); Vendor Document Turnover Package (DEL-099-05) | DELIVERABLE_REGISTER.csv rows 555-556 |
| Acceptance baseline | EPC Scope of Work (DEL-099-01); Package Datasheet (DEL-099-02); Construction Work Package (DEL-099-03) | DELIVERABLE_REGISTER.csv rows 552-554 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating environment | Outdoor, sour-service-adjacent area; truck movement zone | DBM SEC-13 (line 671, 677, 679) |
| Hazardous area / detection | LEL, H2S, methyl mercaptan, fire detection coverage required for truck loading | DBM SEC-16 (line 838) |
| Shutdown integration | Truck loading shutdowns coordinated between package PLC, BPCS, RIO, ESD | DBM SEC-17 (line 862) |
| Spill control | Truck-loading slabs and spill-control provisions per civil basis | DBM SEC-13 (line 688, 696) |
| Permitting status | Truck rack permit amendment required (BCER 100120203) | DBM SEC-18 (line 872) |
| Acceptance signing authority | Human approver (K-AUTH-1); agent does not certify | Chirality K-AUTH-1 |

## Construction

The "construction" of this deliverable is an evidence package, not a physical object. It is constituted by the following anticipated artifacts:

| Artifact | Description | Form |
|---|---|---|
| Vendor document review log | Per-document review status, comments, dispositions against vendor submittals (from DEL-099-05) | Log (table/CSV or Markdown) |
| Package acceptance checklist | Item-by-item acceptance against EPC SOW, Package Datasheet, and CWP | Checklist |
| Test/inspection evidence | Records of FAT, SAT, hydrotest, NDE, pressure-test, electrical, instrument loop checks, fire/gas, ESD as applicable | Records (vendor + EPC witness) |
| Turnover evidence | Mechanical Completion, Pre-Commissioning, Commissioning, Operational Acceptance records | Turnover certificates and supporting records |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder)
- Decomposition: GATE-07_Final_Published_2026-05-24 — `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-03, SEC-04, SEC-06, SEC-08, SEC-09, SEC-13, SEC-16, SEC-17, SEC-18)
- Workbook Packages row 98 — not locally readable as text (`.xlsx`); content TBD (location TBD)
- 26020-Package_Requirements.docx package heading 51 — not locally readable as text (`.docx`); content TBD (location TBD)
- Sibling PKG-099 deliverables: DEL-099-01 (SOW), DEL-099-02 (Datasheet), DEL-099-03 (CWP), DEL-099-04 (Vendor Eng. Package), DEL-099-05 (Vendor Document Turnover)
