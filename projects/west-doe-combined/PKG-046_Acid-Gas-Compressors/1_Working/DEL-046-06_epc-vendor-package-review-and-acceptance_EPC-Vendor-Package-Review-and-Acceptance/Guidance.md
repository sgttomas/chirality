# Guidance — DEL-046-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's auditable evidence that the PKG-046 (Acid Gas Compressors) vendor-engineered package has been reviewed against the binding EPC scope, datasheet, and construction work package and is accepted for handoff to construction/commissioning. It is the gate at which vendor-engineered work is converted into project-binding installed equipment basis.

Source: `_CONTEXT.md` Scope and Notes (Gate 5 EPC-integrator review/acceptance evidence).

## Principles

- **EPC Integrator is the lead.** Package Vendor provides input; the Integrator owns acceptance. Source: `_CONTEXT.md` ResponsibleParty.
- **Acceptance is evidence-based.** Every acceptance decision is traceable to a vendor document review entry, a test/inspection record, or a turnover document index entry. Source: `_CONTEXT.md` Anticipated Artifacts.
- **Package scope boundaries are protected.** Acceptance verifies that the vendor has not extended its scope into facility-owned interfaces (cross-facility utilities, controls integration, civil/structural OSBL) or, conversely, transferred package-internal scope to the field. Source: DBM SEC-09 line 617.
- **Sour-service integrity is non-negotiable.** Given the West Doe sour-gas basis (DBM SEC-05), acceptance of any acid-gas/sour-service equipment without traceable sour-service material certification is not permitted. (ASSUMPTION: applies to PKG-046; clause-level basis `location TBD`.)
- **Ambient envelope is project-governing.** The -40 deg C to +35 deg C envelope governs unless the vendor demonstrates a more severe condition; deviations require Integrator concurrence. Source: DBM SEC-02 (lines 96, 145).
- **Controls integration is a vendor-integration milestone, not a vendor-only deliverable.** Final data maps, permissive logic, trip interfaces, and alarm priorities are resolved jointly. Source: DBM SEC-12 line 810.

## Considerations

- **Package title vs. equipment content.** The package is titled "Acid Gas Compressors" (workbook row 48), but the locally accessible DBM treats acid gas as routed to the NRM disposal well (DBM SEC-01 line 51; SEC-03 line 208) and does not enumerate dedicated acid-gas compression equipment in the readable source slices. The Integrator should resolve whether PKG-046 covers facility-side acid-gas compression equipment, a vendor-supplied acid-gas injection/recompression package, or a misalignment between workbook row 48 and the locally readable DBM. See Conflict Table below.
- **Reference fidelity.** The cited package authority `26020-Package_Requirements.docx` (package heading 1) is present in `_Sources/` but only as a binary `.docx`; downstream drafting should resolve a readable extraction before issuing the final Acceptance Checklist.
- **Cross-deliverable coupling.** Acceptance evidence quality depends on the completeness of DEL-046-01 (SOW), DEL-046-02 (Datasheet), DEL-046-03 (CWP), DEL-046-04 (Vendor Engineered Package), and DEL-046-05 (Vendor Turnover Package). At time of writing, those sibling deliverables also show minimum-viable filesets only.
- **Objective association.** The supports-objectives list (OBJ-001, OBJ-003 through OBJ-010) was associated by the package-heuristic mode (per brief `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`) and should be treated as ASSUMPTION pending human confirmation.

## Trade-offs

- **Strict gate vs. conditional acceptance.** Strict gating prevents construction churn but delays handoff; conditional acceptance with a punch list enables earlier construction at the cost of carried risk. The default posture should be strict acceptance for sour-service mechanical scope and conditional acceptance with documented punch items for non-safety-critical scope. (PROPOSAL — human ruling needed.)
- **Witness vs. surveillance inspection.** Full witness drives schedule and cost; surveillance reduces both but accepts more residual risk. Selection should be risk-tiered (process safety, sour service, rotating equipment) — clause-level basis `location TBD`.

## Examples

Specific worked examples (e.g., model acceptance checklist line items) — TBD pending readable extraction of `26020-Package_Requirements.docx` and initialization of sibling deliverables DEL-046-01 through DEL-046-05.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-046-06-001 | Package title "Acid Gas Compressors" (PKG-046) suggests dedicated acid-gas compression equipment; readable DBM treats acid gas as routed to NRM disposal well and does not enumerate facility-side acid-gas compressors. | `_CONTEXT.md` PackageName; workbook Packages row 48 | DBM 3-25_Comp_and_Liquids_DBM.md SEC-01 line 51; SEC-03 line 208 | Datasheet Identification/Attributes; Specification Scope/Standards (R6); Guidance Considerations | Treat workbook Packages row 48 + `26020-Package_Requirements.docx` package heading 1 as the binding authority for the package equipment list; reconcile DBM after extraction. | TBD |
| CF-046-06-002 | `_REFERENCES.md` cites `26020-Package_Requirements.docx` heading 1 as the source authority, but no readable extraction is locally available. | `_REFERENCES.md` Source Materials Referenced By Decomposition Row | `_REFERENCES.md` Missing/Deferred References | Specification R6, R8; Standards table; Datasheet Construction | Extract and slice `26020-Package_Requirements.docx` heading 1 to markdown under `_Sources/` before final acceptance issue. | TBD |
| CF-046-06-003 | `_DEPENDENCIES.md` declares no upstream/downstream dependencies, but the deliverable scope explicitly requires DEL-046-01, DEL-046-02, DEL-046-03 (and implicitly DEL-046-04, DEL-046-05). | `_CONTEXT.md` Scope | `_DEPENDENCIES.md` Declared Upstream/Downstream | Specification verification approaches; Procedure Prerequisites | Declare DEL-046-01, DEL-046-02, DEL-046-03 as upstream constraints and DEL-046-04, DEL-046-05 as upstream inputs in `_DEPENDENCIES.md` via the dependency-extract task. | TBD |
