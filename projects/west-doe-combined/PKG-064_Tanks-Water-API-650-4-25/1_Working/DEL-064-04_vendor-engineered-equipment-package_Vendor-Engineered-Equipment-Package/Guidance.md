# Guidance: DEL-064-04 — Vendor Engineered Equipment Package (Tanks, Water (API 650) 4-25)

> Directional rationale for the Package Vendor's engineering, design, fabrication/supply scope, and for EPC Integrator interface stewardship. Substantive claims source-grounded; inferences labeled `ASSUMPTION`; gaps marked `TBD`.

## Purpose

This deliverable produces the physical equipment package (process water storage tanks `TK-5317-1` and `TK-5318-1`) plus the supporting engineering/design package needed for the EPC Integrator to install, tie in, and accept the equipment as part of the 4-25 Deepcut facility. The vendor package is the operational realization of the EPC Package Datasheet (`DEL-064-02`) and EPC Scope of Work (`DEL-064-01`); it is the upstream of the Vendor Document Turnover Package (`DEL-064-05`) and the EPC Vendor Package Review and Acceptance (`DEL-064-06`). (`_CONTEXT.md` Scope; PROJECT_DECOMP register rows 540–545.)

## Principles

1. **EPC Package Datasheet is the binding handoff.** The Package Datasheet (`DEL-064-02`) is the technical handoff document for vendor engineering and design (PROJECT_DECOMP register row 541). The vendor package must remain traceable to the datasheet at the line-item level.
2. **Source authority is the West Doe Deepcut DBM (4-25).** Where the Package Datasheet inherits values from the DBM, the DBM text is the authoritative source. Vendor design choices that deviate from the DBM must be flagged for EPC Integrator review.
3. **Atmospheric tank discipline (API 650 modified).** Other 4-25 atmospheric storage tanks (produced water, condensate) are designed as "Modified API 650" with 16 oz/in² test pressure and 90% maximum-fill criteria (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518–519, 1646–1648). The process water tanks should follow the same modified-API-650 discipline unless explicitly excepted.
4. **Cold-climate freeze protection.** "Water tanks shall be insulated to prevent winter freezing" is a stated 4-25 DBM requirement (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2509). Insulation and heat tracing decisions are not optional value-engineering items.
5. **Vendor interface clarity for integration review.** All nozzle loads, instrument I/O, electrical, utilities, and operating cases needed by `DEL-064-06` must be produced as first-class vendor outputs, not extracted later from drawings.

## Considerations

- **Service definition.** Process water in the 4-25 facility serves at least the amine treating unit Module 530 make-up duty (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1556 — "Make-up water, if required during upset operation, is supplied from the process water storage tank") and Module 530 includes process-water storage and transfer in its scope (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1132). Vendor should confirm with the EPC Integrator whether other users (e.g., NGL mercaptan caustic treating water wash make-up) draw from the same tank set.
- **VRU connectivity.** The VRU gas-source table (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~1714) lists produced water tanks, C5+ slop/storage tanks, and amine slop/surge tanks — **not** process water tanks. ASSUMPTION: process water tanks are not VRU-connected. Vendor should confirm vent disposition (atmosphere vs. closed vent) with EPC Integrator before finalizing PVRV/EPRV sizing.
- **Specific gravity / capacity.** Accessible DBM slices do not provide explicit process water tank design SG or capacity. Vendor must obtain these from the Package Datasheet; if absent, raise a `TBD`/Conflict entry rather than assume.
- **Material/coating selection.** Produced water tanks use Devchem 253 internal coating because produced water carries trace hydrocarbons, TEG, amine, H2S, caustic, and mercaptans (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 508, 524). Process water is a cleaner service; coating selection should be made by the vendor against actual fluid composition supplied by the Package Datasheet — not by analogue to produced water by default.
- **Spacing and plot layout.** The vendor's general arrangement must be consistent with the 4-25 Atmospheric Tank and General Plant Spacing rules and the OGAOM 25 m (82 ft) flare-to-atmospheric-tank distance (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~261, 283). Coordinate with EPC Integrator plot plan.
- **Boundary with Tank Farm Pump Building 2.** The PROCESS WATER TRANSFER PUMPS (x2) are listed under "Tank Farm Pump Building 2" (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Tank Farm Pump Building row). The vendor scope ends at the tank-side flanges unless the Package Datasheet integrates the pumps into this package.
- **Objective association is a heuristic.** Supports-objectives field for this deliverable was set by PACKAGE_HEURISTIC at PKG-064 level (`_CONTEXT.md` Supports Objectives). Treat the OBJ mapping as directionally relevant context, not as hard requirement allocation.

## Trade-offs

- **Modified-API-650 vs. straight API 650.** "Modified" allows the cold-climate atmospheric-tank pattern in use at 4-25 (16 oz/in² test pressure rather than the strict API 650 envelope). Trade-off: simpler atmospheric tank cost/schedule against API-650-purist auditability. Decision basis already established by other 4-25 tanks; carry through unless Package Datasheet says otherwise.
- **PVRV-only vs. PVRV + EPRV.** Produced water tanks at 4-25 use "at least one PVRV" with EPRV sizing deferred to detailed engineering (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524). For process water (cleaner service, no expected sour vapours), PVRV-only may suffice; vendor should request EPC Integrator ruling rather than decide unilaterally.
- **Coating vs. uncoated carbon steel.** Coating adds cost and inspection burden but extends life if any contamination is possible. Trade-off requires confirmed fluid spec from Package Datasheet.

## Examples

- **Analogue — Produced water tanks (PROJECT_DECOMP / DBM-Deepcut row 2559).** "Modified API-650 atmospheric tank; 16 oz test pressure", 90% max fill, blanket gas per API 2000, externally insulated and heated, Devchem 253 internal coating, Kennilworth hydrocarbon skim float, at least one PVRV per tank, EPRV sizing deferred (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518–524). This is the closest in-DBM template; deviations should be intentional, not accidental.
- **Analogue — Condensate storage tanks (DBM Sec. line 1646).** "Modified API 650", atmospheric with 16 oz/in² test pressure, 90% max-fill shutdown, blanket gas per API 2000, VRU-connected. Useful for the modified-API-650 design pattern; **not** an analogue for service/coating/VRU connectivity.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFT-064-04-01 | Package Datasheet (`DEL-064-02`) is not yet drafted; many vendor-package values (tank SG, capacity, material, coating, nozzle list) cannot be source-grounded from accessible material. | `_CONTEXT.md` Anticipated Artifacts (Package Datasheet expected) | `_REFERENCES.md` Missing/Deferred — no deliverable-specific source slices copied | Datasheet — Attributes/Conditions/Construction; Specification — R-064-04-08, R-064-04-09 | Defer concrete values to `TBD` until `DEL-064-02` is drafted; this deliverable cannot resolve those values unilaterally | TBD |
| CFT-064-04-02 | "Modified API 650" basis is documented for 4-25 produced water and condensate tanks but not explicitly extracted from the 26020 package-requirements heading 19 (binary source not directly accessible this run). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1646 | `_Sources/26020-Package_Requirements.docx` heading 19 (binary; `location TBD`) | Specification R-064-04-02 | Adopt Modified API 650 as the working basis; confirm against 26020 once source slice is extracted | TBD |
| CFT-064-04-03 | VRU connectivity for process water tanks is not explicitly stated in the VRU gas-source table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~1714 (table lists produced water, C5+, amine — not process water) | none locally | Datasheet — VRU connection; Guidance — VRU connectivity bullet | Assume no VRU connection; vendor PVRV vents to atmosphere unless EPC Integrator instructs otherwise | TBD |
