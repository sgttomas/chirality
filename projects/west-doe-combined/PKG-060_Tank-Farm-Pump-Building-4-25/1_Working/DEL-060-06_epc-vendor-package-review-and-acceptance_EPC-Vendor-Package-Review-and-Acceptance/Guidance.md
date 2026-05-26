# Guidance — DEL-060-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's auditable evidence that the PKG-060 (Tank Farm Pump Building 4-25) vendor-engineered package has been reviewed against the binding EPC scope, datasheet, and construction work package and is accepted for handoff to construction/commissioning. It is the gate at which vendor-engineered work for the 04-25 facility's tank-farm pump scope is converted into project-binding installed equipment basis.

Source: `_CONTEXT.md` Scope and Notes (Gate 5 EPC-integrator review/acceptance evidence).

## Principles

- **EPC Integrator is the lead.** Package Vendor provides input; the Integrator owns acceptance. Source: `_CONTEXT.md` ResponsibleParty.
- **Acceptance is evidence-based.** Every acceptance decision is traceable to a vendor document review entry, a test/inspection record, or a turnover document index entry. Source: `_CONTEXT.md` Anticipated Artifacts.
- **Package scope boundaries are protected.** Acceptance verifies that the vendor has not extended its scope into facility-owned interfaces (shared 03-25/04-25 utilities, tank-farm electrical building, civil/structural OSBL, dike walls, tankage/bullets) or, conversely, transferred package-internal scope to the field. Source: DBM SEC-01 line 95; DBM lines 2816-2817.
- **Sour-service integrity is non-negotiable.** Given the 04-25 sour-gas basis (DBM SEC-01 line 5; SEC-05 line 396, 1 mol% combined-feed H2S), acceptance of any wetted, pressure-containing component on condensate or sour-water service without traceable sour-service material certification (NACE MR0175 / ISO 15156) is not permitted. (ASSUMPTION: applies to PKG-060 sour-service pump duties; clause-level basis `location TBD`.)
- **Ambient envelope is project-governing.** The -40 deg C to +35 deg C envelope governs unless the vendor demonstrates a more severe condition; deviations require Integrator concurrence. Source: DBM SEC-02 lines 197-198.
- **Tank-farm separation is enforceable.** Bullet-to-pump-skid spacing per API 2510 (3.05 m / 10 ft) is a layout constraint the vendor must respect or the EPC Integrator must reconcile against the plot plan. Source: DBM SEC-02 line 252.
- **Controls integration is a vendor-integration milestone, not a vendor-only deliverable.** Final data maps, permissive logic, trip interfaces, and alarm priorities are resolved jointly. Source: DBM SEC-12 line 810 (applied as precedent).

## Considerations

- **Package title vs. equipment content.** The package is titled "Tank Farm Pump Building 4-25" (workbook Packages row 85). The locally accessible DBM identifies this package as "Tank Farm Pump Building 2" at facility 04-25 (Deepcut) and enumerates the pump duties: condensate transfer (x2), water transfer (x4), sour-water treatment (x2), process water transfer (x2), fresh caustic transfer (x2) — DBM lines 2555, 2618-2622. The Integrator should confirm naming alignment against the binding `26020-Package_Requirements.docx` heading 15 slice (currently binary). See Conflict Table CF-060-06-001.
- **Reference fidelity.** The cited package authority `26020-Package_Requirements.docx` (package heading 15) and the workbook (`26020-Packages_Interfaces_4_export.xlsx`, row 85) are present in `_Sources/` but only as binary files; downstream drafting should resolve readable extractions before issuing the final Acceptance Checklist.
- **Cross-deliverable coupling.** Acceptance evidence quality depends on the completeness of DEL-060-01 (SOW), DEL-060-02 (Datasheet), DEL-060-03 (CWP), DEL-060-04 (Vendor Engineered Package), and DEL-060-05 (Vendor Turnover Package). At time of writing, those sibling deliverables also show minimum-viable filesets only.
- **Multiple service classes inside one package.** The pump building hosts pumps with materially different service classes (sour-water vs. fresh caustic vs. fresh process water vs. condensate). Acceptance review should not apply a single materials-traceability check across the package — material/sour-service evidence must be reviewed per pump duty. Source: DBM lines 2618-2622.
- **Modularization basis.** Tank Farm Pump Module is shop-built (DBM line 2817). Acceptance must include shop FAT/run-in/loop-check evidence; field-only commissioning of items intended for shop test is a non-conformance.
- **Cross-package interfaces.** The pump building interfaces with bullets/tankage (other deliverables), the 860-1 Tank Farm Electrical Building (DBM line 2816), and shared utilities. Interfaces must be reconciled via tie-in lists, not assumed.
- **Objective association.** The supports-objectives list (OBJ-001, OBJ-003 through OBJ-010) was associated by the package-heuristic mode (per brief `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`) and should be treated as ASSUMPTION pending human confirmation.

## Trade-offs

- **Strict gate vs. conditional acceptance.** Strict gating prevents construction churn but delays handoff; conditional acceptance with a punch list enables earlier construction at the cost of carried risk. The default posture should be strict acceptance for sour-service mechanical scope (sour-water and condensate pumps) and conditional acceptance with documented punch items for non-safety-critical scope (e.g., fresh caustic or fresh process water where appropriate). (PROPOSAL — human ruling needed.)
- **Witness vs. surveillance inspection.** Full witness drives schedule and cost; surveillance reduces both but accepts more residual risk. Selection should be risk-tiered (sour service first; rotating equipment second; auxiliary third) — clause-level basis `location TBD`.
- **Single-train acceptance vs. building-level acceptance.** Because the package contains multiple pump trains with independent service classes, the Integrator may accept by train (allowing early handoff of completed trains) or by building (single milestone). Default proposal: by-train acceptance with a building-level rollup. (PROPOSAL — human ruling needed.)

## Examples

Specific worked examples (e.g., model acceptance checklist line items, FAT scopes per pump class) — TBD pending readable extraction of `26020-Package_Requirements.docx` heading 15 and initialization of sibling deliverables DEL-060-01 through DEL-060-05.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-060-06-001 | Package name mismatch: `_CONTEXT.md` and decomposition state "Tank Farm Pump Building 4-25"; DBM source slice labels the same facility object as "Tank Farm Pump Building 2" at 04-25 (Deepcut). | `_CONTEXT.md` PackageName; workbook Packages row 85 | DBM 4-25_Deepcut_DBM.md line 2555 ("Tank Farm Pump Building 2 ... 4-25 (Deepcut)") | Datasheet Identification/Attributes; Specification Scope | Treat workbook Packages row 85 + `26020-Package_Requirements.docx` heading 15 as the binding name authority; reconcile DBM naming after readable extraction. | TBD |
| CF-060-06-002 | `_REFERENCES.md` cites `26020-Package_Requirements.docx` heading 15 and `26020-Packages_Interfaces_4_export.xlsx` row 85 as the source authority, but neither is locally available as readable text. | `_REFERENCES.md` Source Materials Referenced By Decomposition Row | `_REFERENCES.md` Missing/Deferred References | Specification R8, R10; Standards table; Datasheet Construction | Extract and slice `26020-Package_Requirements.docx` heading 15 and the relevant workbook row to markdown under `_Sources/` before final acceptance issue. | TBD |
| CF-060-06-003 | `_DEPENDENCIES.md` declares no upstream/downstream dependencies, but the deliverable scope explicitly requires DEL-060-01, DEL-060-02, DEL-060-03 (and implicitly DEL-060-04, DEL-060-05). | `_CONTEXT.md` Scope | `_DEPENDENCIES.md` Declared Upstream/Downstream | Specification verification approaches; Procedure Prerequisites | Declare DEL-060-01, DEL-060-02, DEL-060-03 as upstream constraints and DEL-060-04, DEL-060-05 as upstream inputs in `_DEPENDENCIES.md` via the dependency-extract task. | TBD |
| CF-060-06-004 | Multiple service classes inside one package (sour-water vs. fresh process water vs. condensate vs. fresh caustic) imply different materials/sour-service review criteria, but `_CONTEXT.md` describes the deliverable as a single acceptance checklist. | DBM 4-25_Deepcut_DBM.md lines 2618-2622 | `_CONTEXT.md` Anticipated Artifacts (single checklist) | Specification R8; Procedure step 7 | Maintain a single acceptance checklist with per-train materials/sour-service sub-sections, not a single global materials judgment. | TBD |
