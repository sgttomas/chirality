# Datasheet — EPC Vendor Package Review and Acceptance (DEL-082-06)

Descriptive datasheet for the EPC-integrator review-and-acceptance evidence covering the Flare KO Drum (Low Pressure) 3-25 vendor package. This deliverable is acceptance evidence; it is not the vendor engineered package itself (DEL-082-04) or the vendor document turnover package (DEL-082-05).

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-082-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-082` |
| PackageName | Flare KO Drum (Low Pressure) 3-25 |
| Workbook Row | 56 |
| Source Heading | 26020-Package_Requirements.docx package heading 35 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | SOW-0079; SOW-0080; SOW-0081; SOW-0082 |
| Supports Objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject system | Low-Pressure Flare Knock-Out Drum and associated transfer pump | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07 (LP flare receives TEG, VRU, seal-pot services; LP relief routes to LP KO drum V-3900-2, pump P-3900-2 to slop) |
| Subject equipment tag — vessel | V-3900-2 | DBM SEC-07 |
| Subject equipment tag — pump | P-3900-2 | DBM SEC-07 |
| Pump configuration basis | LP flare KO drum transfer pump: 1 x 100 percent | DBM SEC-09 equipment list row |
| Acceptance subject | Vendor package against EPC Scope of Work, Package Datasheet, and Construction Work Package | `_CONTEXT.md` Scope |
| Review record class | Document review log; acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Coordination mode | DECLARED; no upstream/downstream dependencies declared at PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| LP flare service classification | Sour hydrocarbon relief service (TEG, VRU, compressor seal-pot routes) | DBM SEC-07 |
| LP relief header size basis | 508 mm / 20 in (carried equal to HP header in current source basis) | DBM SEC-07 |
| LP stack OD | TBD | DBM SEC-07 (explicit TBD) |
| Staggered blowdown requirement | Required to limit maximum relief | DBM SEC-07 |
| Detailed blowdown sequencing source | W242510-PRC-REP-000003-001 (Plant Shutdown and Blowdown Philosophy) | DBM SEC-07 |
| Isolation philosophy for sour service | Double block/bleed or equivalent where required by operations or HAZOP | DBM SEC-09 |
| Vent/drain routing | To correct flare/drain/closed system based on pressure, sour-service, and contamination class | DBM SEC-09 |
| Equipment design margin (vessels) | 10 percent on flow | DBM SEC-09 design-margin table |
| Equipment design margin (process pumps) | 15 percent on flow unless package-specific design requires otherwise | DBM SEC-09 design-margin table |

## Construction

| Item | Value | Source |
|---|---|---|
| Pressure vessel design | Applicable pressure class, sour-service requirements, corrosion allowance, coating, manway access, internals removal, drainage, venting, inspection | DBM SEC-09 Vessel and Exchanger Design |
| Internals removal / access | Required by vessel design philosophy | DBM SEC-09 |
| Skid-edge isolation | Required at package boundaries where required for maintenance | DBM SEC-09 Isolation Philosophy |
| Free-drain / slope basis at flare KO interface | LP flare bypass header shall free-drain or slope toward the flare KO interface as defined by detailed design | DBM SEC-06 (VRU recycle / LP flare bypass paragraph) |
| Project hazardous-material list | Referenced but not available in workspace | DBM SEC-07 (TBD basis) |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-06, SEC-07, SEC-09 (locally accessible)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — package heading 35 (binary `.docx`; not parsed in-band, location `TBD` for clause-level citation)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 56 (binary `.xlsx`; location `TBD` for clause-level citation)
- GATE-07 PROJECT_DECOMP snapshot deliverable register (decomposition basis)
- Peer deliverables (context only): DEL-082-01 SoW, DEL-082-02 Package Datasheet, DEL-082-03 CWP, DEL-082-04 Vendor Engineered Package, DEL-082-05 Vendor Document Turnover Package

ASSUMPTION: Equipment tags V-3900-2 and P-3900-2 from the DBM are taken as the LP Flare KO Drum and its transfer pump referenced by PKG-082. Cross-confirmation against the package vendor datasheet (DEL-082-02) is TBD.
