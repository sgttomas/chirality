# Package Datasheet Specification — PKG-076 Lube Oil Supply

## Scope

This specification defines the technical content the EPC Integrator must carry in the Package Datasheet for PKG-076 Lube Oil Supply so the package can be engineered, procured, fabricated, and integrated by a vendor or discipline package engineer.

In scope:
- Identification, function, plant/area, and tagged equipment for the lube oil supply package as defined in the source DBM (`4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Package Line-Item Requirements" row 51).
- Storage tank and transfer pump design conditions (specific gravity, capacity, heating, oil grades) to the extent stated or labelled TBC/TBD in source.
- Interfaces to served compressor packages and to utility, drainage, and hazardous-material handling systems.

Out of scope:
- Detailed mechanical design of the storage tanks and pumps (assigned to the Package Vendor under DEL-076-04).
- Construction Work Package content (DEL-076-03).
- Vendor document register and submittals (DEL-076-05).
- EPC vendor package review and acceptance evidence (DEL-076-06).
- Day tanks integral to served compressor packages (carried by those packages).

## Requirements

REQ-076-02-01 — The Package Datasheet shall identify the package as PKG-076 Lube Oil Supply, located at 4-25 Deepcut, with the function of heated compressor cylinder and crank-case lube oil storage and transfer to compressor frame day tanks. (Source: `4-25_Deepcut_DBM.md` §"Utility System Summary" lube oil row; §"Lube Oil Storage and Pump Basis".)

REQ-076-02-02 — The Package Datasheet shall list the lube oil supply pumps P-9240-1 and P-9250-1 as the tagged equipment for this package. (Source: `4-25_Deepcut_DBM.md` §"Package Line-Item Requirements" row 51.)

REQ-076-02-03 — The Package Datasheet shall carry the compressor cylinder lube oil storage as a 400 bbl heated tank and the crank-case lube oil storage as a 200 bbl heated tank, located in the storage tank area. (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis".)

REQ-076-02-04 — The Package Datasheet shall record the design specific gravity for both the cylinder and crank-case lube oil storage tanks as 1.00 (TBC). (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis".)

REQ-076-02-05 — The Package Datasheet shall record that multiple cylinder oil grades may be required across served compressor services (inlet, sales, stabilizer overheads, acid gas, sales booster), driven by sulphur content, rich gas, and H2S, and that manufacturer-recommended cylinder oil types remain TBC during FEED. (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis".)

REQ-076-02-06 — The Package Datasheet shall identify additional storage requirements as TBD and shall preserve the SEC-08 Open Design Development item "Lube oil — Confirm specific gravities, cylinder-oil selections, and added storage requirements." (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; §"Open Design Development Requirements" lube oil row.)

REQ-076-02-07 — The Package Datasheet shall identify the interface to served compressor packages as "transfer pumps fill compressor frame day tanks as needed" and shall not redefine the day tanks as part of this package. (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis".)

REQ-076-02-08 — The Package Datasheet shall reference the project hazardous-material list as the controlling document for lube-oil hazardous-material classification and shall flag that the list was not accessible in the current workspace. (Source: `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers".)

REQ-076-02-09 — The Package Datasheet shall reconcile or surface the conflict between (a) the SEC-08 two-pump basis (P-9240-1 cylinder, P-9250-1 crank-case) and (b) the SEC-09 sparing register entry "Lube Oil Transfer Pump 1 × 100%" before issue. (ASSUMPTION: items refer to the same population; resolution requires human ruling — see Guidance Conflict Table.) (Source: `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis"; SEC-09 sparing register entry "Lube Oil Transfer Pump".)

REQ-076-02-10 — The Package Datasheet shall present interface, scope, and equipment information at a level sufficient for vendor or discipline package engineering handoff (DEL-076-04) and shall not extend into construction execution detail (DEL-076-03). (Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER row DEL-076-02 description.)

REQ-076-02-11 — The Package Datasheet shall maintain consistency of equipment tags, capacities, and design specific gravities with any cross-reference to PKG-076 carried in other deliverables (Scope of Work DEL-076-01, Construction Work Package DEL-076-03, Vendor Engineered Equipment Package DEL-076-04, Vendor Document Turnover DEL-076-05, EPC Vendor Package Review and Acceptance DEL-076-06). (Source: DELIVERABLE_REGISTER rows DEL-076-01…DEL-076-06.)

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| Project hazardous-material list | Controlling list for lube-oil hazardous-material classification and storage | Referenced in `3-25_Comp_and_Liquids_DBM.md` §"Emergency Power, Lube Oil, and Analyzers"; document not accessible in workspace — location TBD |
| 26020-Package_Requirements.docx, package heading 30 | EPC package requirements basis cited by decomposition row for DEL-076-02 | Binary `.docx` under `_Sources/`; clause-level location TBD without text extraction |
| `4-25_Deepcut_DBM.md` SEC-08 §"Lube Oil Storage and Pump Basis" | Design basis for storage and transfer | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2059-2072 |
| `4-25_Deepcut_DBM.md` §2.5 "Atmospheric Tank and General Plant Spacing" | Layout / spacing for lube oil storage tanks | Same source, §2.5 |
| API 650 (atmospheric storage tank standard) | Likely governing fabrication standard for heated atmospheric oil tanks | ASSUMPTION: not explicitly cited for lube oil tanks in accessible source; other 4-25 atmospheric tanks (caustic, condensate, DSO, water) are listed as "API 650" in §"Package Line-Item Requirements" rows for Tanks. |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-076-02-01, 02, 03 | Cross-check Datasheet identification, tagged equipment list, and tank capacities against `4-25_Deepcut_DBM.md` §"Lube Oil Storage and Pump Basis" and §"Package Line-Item Requirements" row 51. |
| REQ-076-02-04, 05, 06 | Confirm that design specific gravities, cylinder oil grade treatment, and added-storage-requirements item are recorded as TBC/TBD with the open-design-development pointer preserved. |
| REQ-076-02-07 | Inspect Datasheet wording and ensure day tanks are attributed to served compressor packages, not to PKG-076. |
| REQ-076-02-08 | Confirm Datasheet flags the hazardous-material list reference and the workspace inaccessibility. |
| REQ-076-02-09 | Confirm Conflict Table entry in Guidance.md is present and includes human-ruling placeholder. |
| REQ-076-02-10, 11 | Cross-deliverable review against DEL-076-01, 03, 04, 05, 06 to confirm no scope leakage and tag/value consistency. |

## Documentation

The following artifacts are produced under DEL-076-02 (from `_CONTEXT.md` Anticipated Artifacts):

- Package technical datasheet (this deliverable's primary artifact; `Datasheet.md`).
- Vendor engineering handoff basis (carried within `Datasheet.md` Interface Summary).
- Package interface requirements matrix (carried within `Datasheet.md` Interface Summary; full matrix elaboration TBD with served-compressor packages confirmed).
- Source-supported equipment and design criteria (carried within `Datasheet.md` Attributes / Conditions sections, with all unsupported values marked TBC/TBD).
