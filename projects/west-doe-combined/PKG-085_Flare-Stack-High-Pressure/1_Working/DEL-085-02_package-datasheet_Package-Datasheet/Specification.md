# Specification — DEL-085-02 Package Datasheet (PKG-085 Flare Stack, High Pressure)

> Normative requirements for the EPC Integrator-issued Package Datasheet deliverable that hands off the HP/Cryo flare stack package to the Package Vendor. This specification governs the *content and form* of the datasheet, not the design of the flare stack itself. Stack design requirements appearing here are those that the datasheet MUST carry forward as binding inputs to the vendor.

## Scope

### In scope
- Defines required content, structure, and source-fidelity rules for the EPC Package Datasheet (this deliverable) for PKG-085 Flare Stack (High Pressure).
- Carries the EPC-Integrator-set technical inputs (design conditions, interface boundaries, equipment basis, spacing/radiation constraints) required by the Package Vendor for engineering, design, fabrication, and supply of the HP/Cryo flare stack package, including the shared HP/Cryo + LP dual stack arrangement at 03-25. Source basis: DBM-Comp_and_Liquids (lines 497-499); PACKAGE_REGISTER.csv (PKG-085).
- Carries package-level interface requirements for the eight interface types declared in PACKAGE_REGISTER.csv (Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports).

### Out of scope
- Vendor's own internal package engineering documents (those are produced under DEL-085-04 Vendor Engineered Equipment Package).
- Construction work package, vendor document turnover register, and EPC vendor package review/acceptance evidence (DEL-085-03, DEL-085-05, DEL-085-06).
- Final flare relief and blowdown studies (called out as required, but the studies themselves are not produced here; DBM-Comp_and_Liquids line 548).

## Requirements

| ID | Requirement | Verification (cross-ref Procedure) | Source |
|---|---|---|---|
| R-01 | The Package Datasheet SHALL identify the deliverable, parent package, workbook row, discipline, type, and responsible party. | Procedure Step P-01 (Identification check) | _CONTEXT.md (mandatory); K-STATUS-1 alignment |
| R-02 | The Package Datasheet SHALL state the HP/Cryo flare stack body geometry as 660 mm OD x 60,957 mm tall, sonic tip; and SHALL flag the companion LP stack OD as TBD pending source confirmation. | Procedure Step P-02 (Geometry cross-check) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| R-03 | The Package Datasheet SHALL state HP and LP relief header sizes as 508 mm (20 in) and SHALL list upstream KO drums and transfer pumps (V-4100-2, V-4150-2, P-4100-2, P-4150-2; LP companion V-3900-2 / P-3900-2). | Procedure Step P-03 (KO/header listing check) | DBM-Comp_and_Liquids (lines 497, 499) |
| R-04 | The Package Datasheet SHALL include the shared-service note that the HP/Cryo + LP dual stack is a shared-interface system between 03-25 and 04-25, with the exact service split and owner interface carried as an open interface item until resolved. | Procedure Step P-04 (Shared-interface note check) | DBM-Comp_and_Liquids (line 56) |
| R-05 | The Package Datasheet SHALL carry, as design inputs to the Vendor, the spacing requirements from DBM-Deepcut Section "Flare and Incinerator Spacing" (lines 276-289), including the cited references (OGAOM Sec. 9.6.15; API 2510; OGPFR Appendix 1 Schedule 1 Sec. 2). | Procedure Step P-05 (Spacing table check) | DBM-Deepcut/4-25_Deepcut_DBM.md (lines 276-289) |
| R-06 | The Package Datasheet SHALL carry thermal-radiation-flux limits 9 kW/m^2 (inside boundary, blackened area) and 5 kW/m^2 (outside boundary) as the current DBM basis, with the explicit qualifier that OGPFR references are external regulatory references not included in the available input package and must be verified against the governing regulation during detailed design. | Procedure Step P-06 (Radiation criteria check) | DBM-Deepcut/4-25_Deepcut_DBM.md (lines 285-289) |
| R-07 | The Package Datasheet SHALL state that the HP/Cryo flare receives cryogenic relief and that the upstream J-T valve includes a mechanical stop or physical stroke limit so that control-failure mass flow to the propane absorber does not exceed cryogenic flare design flow. | Procedure Step P-07 (Cryogenic-flow design note check) | DBM-Deepcut/4-25_Deepcut_DBM.md (line 1321) |
| R-08 | The Package Datasheet SHALL list the eight package-level interface types (Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports) and SHALL flag the tag-to-tag interface matrix as TBD pending extraction of 26020-Packages_Interfaces_4_export.xlsx. | Procedure Step P-08 (Interface-type list check) | PACKAGE_REGISTER.csv (PKG-085, InterfaceTypes column) |
| R-09 | The Package Datasheet SHALL list the scope items it covers (SOW-0087, SOW-0088, SOW-0089, SOW-0090) and SHALL record the objectives association as an ASSUMPTION under the package-grouping heuristic until human-confirmed. | Procedure Step P-09 (Scope/objectives traceability check) | OBJECTIVE_SCOPE_MAP.csv; _CONTEXT.md |
| R-10 | Every non-trivial value in the Package Datasheet SHALL carry a source citation (SourcePath + SectionRef) or be marked TBD with `location TBD`. Decomposition prose SHALL NOT be used as a value source where authoritative source slices exist. | Procedure Step P-10 (Source-citation QA) | SKILL Authority hierarchy; QA_CHECKS.md (source-grounding gate) |
| R-11 | The Package Datasheet SHALL NOT derive clause-level requirements from the binary sources 26020-Package_Requirements.docx or 26020-Packages_Interfaces_4_export.xlsx unless and until their text contents are extracted to a locally accessible artifact; absent that, related values SHALL be marked TBD `location TBD`. | Procedure Step P-11 (Binary-source restraint check) | _REFERENCES.md (Missing/Deferred References); SKILL Step 1 source-fidelity rule |
| R-12 | The Package Datasheet SHALL reference the budgetary bid document only as "go-by for pricing/delivery, not engineering authority" and SHALL NOT use it as a basis for binding design values. | Procedure Step P-12 (Budgetary-document handling check) | PACKAGE_REGISTER.csv (PKG-085, SourcePath field — budgetary marked "go-by only") |
| R-13 | The Package Datasheet SHALL state that final flare relief and blowdown loads, HP/LP service split, and pilot/ignition/purge configuration are TBD pending the final flare studies and detailed engineering. | Procedure Step P-13 (Open-item-disclosure check) | DBM-Comp_and_Liquids (line 548); DBM-Deepcut (line 289) |

## Standards (carried by the Package Datasheet as inputs to the Vendor)

| Standard / Document | Status | Location |
|---|---|---|
| OGAOM Sec. 9.6.15 (Oil and Gas Activities Operations Manual — flare/incinerator spacing) | Cited in DBM | DBM-Deepcut/4-25_Deepcut_DBM.md (lines 280-287); standard text itself `location TBD` |
| API 2510 (pressurized bullets spacing reference) | Cited in DBM | DBM-Deepcut/4-25_Deepcut_DBM.md (line 284); standard text itself `location TBD` |
| OGPFR Appendix 1, Schedule 1, Sec. 2 (thermal radiation flux limits) | Cited in DBM with explicit caveat that text is not in available input package | DBM-Deepcut/4-25_Deepcut_DBM.md (lines 285-289); standard text `location TBD` |
| 26020-Package_Requirements.docx (project package requirements) | Referenced by decomposition; not text-accessible | `_Sources/26020-Package_Requirements.docx` (binary); `location TBD` |
| Applicable provincial/federal flare regulations and ERP/EPRP requirements | TBD | `location TBD` |
| Vendor flare tip / ignition / monitoring standards (e.g., API 521 / API 537 family) | ASSUMPTION — likely applicable; not cited in available DBM slices | `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01..R-09, R-13 | Document-content review by EPC Integrator (Procedure Steps P-01..P-09, P-13) against this Specification and the cited source slices. |
| R-10 | Source-citation audit: every non-`TBD` value must have a SourcePath+SectionRef in the Datasheet table cells or References section. |
| R-11 | Binary-source restraint audit: confirm Datasheet rows that depend on 26020-Package_Requirements.docx or 26020-Packages_Interfaces_4_export.xlsx are marked TBD `location TBD` until extraction is performed. |
| R-12 | Reference-handling audit: confirm budgetary document is labelled go-by/non-authoritative in the Datasheet References section. |
| Cross-document | Specification (this file) and Datasheet must use identical numeric values and terminology (660 mm OD, 60,957 mm, 508 mm/20 in, 9/5 kW/m^2, 25/80/50/30.48/10 m spacings). |

## Documentation (artifacts produced by/around this deliverable)

Per `_CONTEXT.md` Anticipated Artifacts:

- Package technical datasheet (this deliverable, `Datasheet.md`)
- Vendor engineering handoff basis (this deliverable, applied through R-01..R-13)
- Package interface requirements matrix (carried by the Datasheet at interface-type level; tag-to-tag matrix is TBD pending extraction of 26020-Packages_Interfaces_4_export.xlsx)
- Source-supported equipment and design criteria (carried by Datasheet tables with citations)

Companion deliverables (out of scope here): DEL-085-01 Scope of Work; DEL-085-03 Construction Work Package; DEL-085-04 Vendor Engineered Equipment Package; DEL-085-05 Vendor Document Turnover Package; DEL-085-06 EPC Vendor Package Review and Acceptance.
