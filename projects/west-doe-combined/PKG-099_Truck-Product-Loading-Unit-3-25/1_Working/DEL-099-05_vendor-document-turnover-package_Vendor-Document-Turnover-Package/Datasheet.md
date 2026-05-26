# Datasheet: DEL-099-05 — Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-099-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-099` |
| PackageName | Truck Product Loading Unit 3-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Decomposition snapshot | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` |

Source: `_CONTEXT.md` (FACT).

## Attributes

| Attribute | Value | Source / Status |
|---|---|---|
| Parent process unit | 3-25 Comp_and_Liquids (Liquids Hub, product truck loading stations) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 22), SEC-06 (lines 413-416) (FACT) |
| Number of truck loading stations served | 3 product truck loading stations | DBM SEC-06 (lines 414-415) (FACT) |
| Per-station loading capacity | 103 m3/h per station, 345 kPad differential | DBM SEC-06 (line 415) (FACT) |
| Condensate loading pumps | Three pumps, one per truck loading station | DBM SEC-06 (line 414) (FACT) |
| Required package deliverable content (per DBM SEC-09) | datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, **vendor document registers** | DBM SEC-09 "Mechanical Package Structure" (line 617) (FACT) |
| Vendor document register contents (line items) | TBD — source `26020-Package_Requirements.docx` heading 51 not locally parseable | location TBD |
| Submittal list / required vendor document classes | TBD — same source not parseable (ASSUMPTION: typical classes include datasheets, GA drawings, P&IDs, electrical schematics, control narrative/cause-and-effect, IOM manuals, QA/QC dossiers, MTRs, FAT/SAT records, spare parts list, training material, warranty) | location TBD; ASSUMPTION |
| Turnover record set | TBD — source not parseable (ASSUMPTION: typical scope includes as-built drawings, completed punch list, signed FAT/SAT reports, calibration certificates, system handover certificate) | location TBD; ASSUMPTION |
| Coordination mode | DECLARED; no declared upstream/downstream dependencies at PREPARATION | `_DEPENDENCIES.md` (FACT) |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Ambient minimum (site) | -40 deg C | DBM SEC-02 / SEC-09 (line 145) (FACT) |
| Service class | Stabilized product condensate (truck loading service) | DBM SEC-06 (lines 22, 34) (FACT) |
| Sour-service applicability for this turnover package | TBD (product loading is stabilized product side; sour considerations apply to other condensate services) | DBM SEC-06 (line 22) (ASSUMPTION) |

## Construction

This deliverable is a documentation package, not a physical construction item. Construction-related attributes describe the vendor-supplied truck loading equipment whose documentation is collected:

| Item | Value | Source |
|---|---|---|
| Equipment class | Mechanical package — product truck loading stations and condensate loading pumps | DBM SEC-06 (lines 414-415) (FACT) |
| Driver basis | Electric motor driven | DBM SEC-08 (line 526) (FACT) |
| Vendor scope boundary discipline | Clear scope boundaries among process vendors, electrical/controls, field construction, cross-facility utility interfaces | DBM SEC-09 (line 617) (FACT) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally accessible; SEC-06, SEC-08, SEC-09 consulted)
- `_Sources/26020-Package_Requirements.docx` (NOT locally parseable — heading 51 cited in `_CONTEXT.md`; content marked TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 98 (NOT locally parseable — marked TBD)
- GATE-07 decomposition snapshot registers (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`)
