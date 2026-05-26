# Guidance — EPC Vendor Package Review and Acceptance (DEL-106-06)

> Directional document. Why this review/acceptance deliverable exists, principles to apply, considerations, trade-offs, and the Conflict Table for human ruling.

## Purpose

This deliverable produces the evidence that the EPC Integrator has reviewed the Yard Lighting vendor package (DEL-106-04), reviewed the vendor's documentation turnover (DEL-106-05), and concluded that the package is acceptable for integration into the West Doe facility against the EPC Scope of Work (DEL-106-01), Package Datasheet (DEL-106-02), and Construction Work Package (DEL-106-03). It is the closing acceptance artifact for PKG-106 from the EPC Integrator's perspective.

## Principles

1. **Acceptance is human authority.** The EPC Integrator (and Owner where required) signs acceptance; this deliverable supplies evidence to support that decision but does not itself certify (K-AUTH-1).
2. **Source-grounded acceptance.** Acceptance statements must trace to the EPC SOW, Package Datasheet, CWP, vendor submittals, and to the DBM lighting basis (DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles") where the design basis is in question.
3. **Area-classification fidelity.** Yard lighting traverses both classified and non-classified areas; fixture-by-fixture suitability per area-classification drawings is a non-negotiable acceptance check.
4. **Code/regulatory alignment.** CEC compliance for wiring methods and area-classification sealing, and jurisdictional light-pollution regulation compliance, are first-class acceptance topics (not engineering preferences).
5. **Explicit deferrals.** Items not resolvable at acceptance are recorded as punchlist items with owner and date — they are not silently closed.
6. **Integration over isolation.** Yard lighting is accepted as part of the wider Electrical Power, Grounding/Bonding, and Area/Exterior Lighting interface set (workbook row 12), not only as a stand-alone fixture supply.

## Considerations

- **LED technology mandate.** DBM `4-25_Deepcut_DBM.md` lines 3027 and 3031 are explicit: all lighting LED; process area and outdoor lighting LED. Vendor deviations require explicit dispositioning.
- **Hazardous-area suitability.** Many yard locations may be classified (process areas near hydrocarbon-handling equipment). The acceptance log must show area-class certification per luminaire/location combination, not a single blanket statement.
- **Cold-climate verification.** -40 deg C ambient (DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04) governs luminaires, drivers, gaskets, lenses, and any heater provisions; acceptance must not silently accept a milder vendor basis.
- **Light-pollution compliance.** DBM line 3035 enumerates downward illumination, no horizontally aimed floodlights, photocell or switch control, selective coverage, and mast-pole placement away from pad edges. These are aiming/layout acceptance items, not only equipment-selection items.
- **Grounding and bonding.** Workbook row 12 lists Grounding/Bonding as a present interface; pole-mounted fixtures, panels, and conduit systems all carry continuity test obligations.
- **Power distribution interface.** General-purpose lighting is fed from "the nearest power distribution centre" per DBM line 3027; the acceptance package should evidence that distribution-panel circuit assignments and breaker coordination are documented.
- **Construction-scope alignment.** DBM `3-25_Comp_and_Liquids_DBM.md` line 75 and `4-25_Deepcut_DBM.md` line 120 place area lighting in the field-construction scope; the acceptance evidence should align vendor-supplied vs field-installed boundaries.

## Trade-offs

- **Conditional vs full acceptance.** Conditional acceptance lets schedule proceed but transfers risk to punchlist closure; full acceptance withholds closure until everything clears but may block downstream turnover.
- **Document-only vs witnessed verification.** Document review (cut sheets, certifications, photometric reports) is cheaper and faster; witnessed field illumination/uniformity measurements and energization checks are more expensive but reduce field surprises after handover.
- **Photocell vs scheduled switch control.** Photocell control follows ambient light reliably; scheduled/switch control offers explicit operator authority. DBM line 3035 permits either; the choice and its evidence must be explicit.
- **Mast-pole vs structure-mounted lighting.** Mast poles deliver uniform coverage but introduce pad-edge clearance and light-pollution concerns; structure-mounted fixtures avoid the pole infrastructure but may produce uneven coverage. DBM line 3035 directs mast-pole placement away from pad edges where masts are used.
- **EPC-led vs Vendor-led closeout.** EPC-led closeout improves integration assurance; Vendor-led closeout can be faster where vendor familiarity dominates. The decomposition assigns lead to the EPC Integrator with Package Vendor input.

## Examples

- *LED verification:* Vendor cut sheet shows LED outdoor floodlight rated -40 deg C, with hazardous-area certification for the installed area class. Recorded under V-1/V-2 against REQ-1, REQ-3, REQ-6.
- *Light-pollution check:* Lighting layout drawing shows downcast aiming, no horizontally aimed fixtures, mast poles inset from pad edge, with photocell-controlled circuits. Recorded under V-4 against REQ-5.
- *Grounding check:* Continuity test record covers each pole, fixture chassis, and panel; ground-resistance values logged. Recorded under V-3 against REQ-8.

(Additional source-specific examples beyond available DBM coverage — e.g., specific illumination-level targets in lux/footcandles — are TBD pending access to the package-requirements document and any photometric design standard adopted by the project.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-1 | Objective association (OBJ-001/004/005/009/010) is asserted by `_CONTEXT.md` but PACKAGE_HEURISTIC was used (no deliverable-level mapping in `OBJECTIVE_DELIVERABLE_MAP.csv` was directly parsed in this run). | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (not directly parsed in this run) | Datasheet §Identification, Specification §Scope | Keep associations as ASSUMPTION until deliverable-level mapping is confirmed. | TBD |
| CFT-2 | Package-level EPC requirements text presumed to exist in `26020-Package_Requirements.docx` for PKG-106, and additional package attributes may exist in the workbook beyond the exported interface row, but neither was text-accessible during this run; package-specific requirements may exist that this draft does not capture. | `_REFERENCES.md` (cited) | Source files (`.docx`/`.xlsx`, not fully text-accessible) | Specification §Requirements, §Standards | Treat referenced package-requirements text as ASSUMPTION present; convert specific requirements to TBD until human extracts text. | TBD |
| CFT-3 | The governing jurisdictional light-pollution regulation is implied by DBM line 3035 but not cited; REQ-15 carries a TBD regulation reference. | DBM `4-25_Deepcut_DBM.md` (line 3035) | Jurisdictional regulation (not in folder) | Specification REQ-15, V-4, Procedure §Steps | Confirm governing BC/federal light-pollution regulatory citation and update REQ-15 with the clause. | TBD |
| CFT-4 | Illumination-level targets (lux/footcandles) for yard areas (process, road, walkway, control point) are not enumerated in available sources; field-verification of illumination uniformity (REQ-11/V-2) lacks a quantitative pass criterion. | (no direct source) | DBM lighting section (qualitative only) | Specification REQ-11, V-2, Procedure §Steps | Adopt IES RP-7 (or equivalent project standard) targets for each area type; require human ruling on adopted standard and target values. | TBD |
| CFT-5 | Area-classification specifics (which yard zones are Class I Div 1 / Div 2 / Zone 1 / Zone 2 / unclassified) are not enumerated for this deliverable; per-fixture suitability check (REQ-3/V-2) depends on the area-classification drawings. | (no direct source in folder) | Project area-classification drawings (not in folder) | Specification REQ-3, V-2, Procedure §Steps | Acceptance log must reference the current area-classification drawing revision; flag any mismatch against vendor certification. | TBD |
| CFT-6 | Construction-scope split between vendor-supplied and field-installed items (per DBM line 75 and line 120 placing area lighting in field-construction scope) needs explicit reconciliation with the PKG-106 vendor package boundary. | DBM `3-25_Comp_and_Liquids_DBM.md` (line 75); DBM `4-25_Deepcut_DBM.md` (line 120) | DEL-106-01 SOW; DEL-106-04 vendor package boundary | Specification §Scope (Excluded), Procedure §Steps 3-5 | Reconcile vendor-vs-field boundary explicitly in the acceptance checklist; carry as a checklist row. | TBD |
