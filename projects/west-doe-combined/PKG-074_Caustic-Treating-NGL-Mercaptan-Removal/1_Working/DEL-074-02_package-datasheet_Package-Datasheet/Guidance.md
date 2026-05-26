# Guidance — Package Datasheet (PKG-074 Caustic Treating, NGL Mercaptan Removal)

## Purpose

The Package Datasheet is the mandatory Gate 5 EPC anchor deliverable for PKG-074 (`_CONTEXT.md`). It carries forward, in one place, the design basis, performance targets, equipment configuration, materials restrictions, and interface set required so that:
- a third-party proprietary process provider can engineer and supply the non-regenerative caustic treating package (DBM-Deepcut line 1511), and
- the EPC Integrator can plan and execute facility-level integration (PACKAGE_REGISTER.csv row 51 `IntegratorScope`).

Interface facts for this package are intentionally carried within the datasheet as evidence rather than as standalone deliverables (`_CONTEXT.md` Notes).

## Principles

1. **Source-anchored content.** Numeric design values, sulphur targets, and equipment counts come from the DBM-Deepcut current-scope NGL mercaptan treating section (DBM-Deepcut lines 1509-1572). Decomposition narrative is used only for scope, identity, and interface set.
2. **Non-regenerative basis is the live design basis.** Prior regenerative-basis flow values and regen-column entries (e.g., NGL Regen Vapour, NGL Regen Gas) are legacy and not current design values (DBM-Deepcut lines 760, 1572).
3. **Caustic compatibility governs material selection.** No aluminum in the caustic building; stainless cladding/straps; caustic-compatible (polymer) tank materials (DBM-Deepcut line 1566).
4. **Indoor installation is non-negotiable.** Freezing and crystallization risk drive indoor location of all caustic-containing equipment (DBM-Deepcut line 1552).
5. **Tank venting segregation.** Spent caustic and DSO tanks vent to incinerator; fresh caustic tank is segregated from VRU to avoid contamination (DBM-Deepcut line 1562).
6. **Cross-facility coupling with 3-25.** The incinerator serving this package is at 3-25; shared-facility operational responsibility is TBD and must be coordinated in detailed engineering (DBM-Deepcut lines 1570-1572).

## Considerations

- **Process provider choice (TBD).** Provider selection drives contactor stage count, internals, and detailed caustic chemistry. The datasheet should remain technology-neutral on stage count until selection (DBM-Deepcut line 1548).
- **Sulphur case envelope.** Performance is defined against the 1 mol% H2S inlet gas case; 0.1 mol% startup and untreated cases are reference comparisons only (DBM-Deepcut lines 1541-1546).
- **Drain drum coupling to SOC.** V-6940-1 vapours route to SOC first-stage suction; SOC inlet flow basis for V-6940-1 is TBC (DBM-Deepcut lines 760, 1560). Coordinate SOC sizing and the package drain-drum operating window during detailed engineering.
- **Heating and freeze protection.** All caustic-containing tanks and lines are heated and insulated; EHT must be coordinated with the building HVAC envelope (DBM-Deepcut lines 1560, 1562, 1564).
- **Safety-shower alarm path.** Activation must surface as a discrete control-room alert; this is an I&C interface that should not be deferred (DBM-Deepcut line 1552).
- **DSO disposition optionality.** Pumping DSO into C5+ product is a possible disposal path, but is subject to detailed-engineering review (DBM-Deepcut lines 528, 1564). Default disposition is trucked off site.

## Trade-offs

- **Number of contactor stages vs. caustic make-up rate.** Source (DBM-Deepcut line 1548) leaves stage count TBD; more stages improve heavy-RSH (C3, C4) extraction (line 1536-1537) at the cost of higher capital. Treat as a vendor-driven optimization rather than fixing in this datasheet.
- **Indoor footprint vs. operability.** Indoor installation reduces freeze risk but increases building HVAC and F&G scope. Source mandates indoor (DBM-Deepcut line 1552); no trade-off latitude.
- **VRU segregation vs. emissions capture.** Excluding the fresh caustic tank from the VRU header avoids contamination but means fresh-caustic vent gas is not recovered (DBM-Deepcut line 1562); this is a chemistry constraint, not an emissions optimization choice.

## Examples

- The DBM-Deepcut treated-NGL sulphur table (lines 1541-1546) gives explicit pre/post numbers for the 1 mol% H2S case and demonstrates the magnitude of sulphur reduction the package must deliver (RSH-as-S from 3,240 to 203.7 ppmw; total S from 4,166 to 970 ppmw).
- The pressurized caustic drain drum routing (DBM-Deepcut line 1560) illustrates the package-to-SOC interface that must be carried forward in both this datasheet and the SOC datasheet to avoid drift between packages.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-074-02-01 | Objective-to-deliverable mapping at deliverable level is not explicit; objectives are inferred from the package-level register row. | `_CONTEXT.md` "Supports Objectives" list (OBJ-001, OBJ-003..OBJ-010) | PACKAGE_REGISTER.csv row 51 Objectives column (OBJ-001; OBJ-003..OBJ-010) | Datasheet "Covers Scope Items / Supports Objectives"; Specification framing | Adopt package-heuristic mapping (consistent between `_CONTEXT.md` and PACKAGE_REGISTER row 51). Treat as ASSUMPTION until OBJECTIVE_DELIVERABLE_MAP.csv is consulted at deliverable-ID granularity. | TBD |
| CF-074-02-02 | `_REFERENCES.md` says "No deliverable-specific source slices copied during PREPARATION" but the DBM-Deepcut source contains rich, locally accessible slices used by this draft. | `_REFERENCES.md` Missing/Deferred References | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1509-1572 (locally accessible) | All four documents | Treat the DBM-Deepcut section as the locally accessible source slice; no copy was required because the source is already on the shared source root. | TBD |
| CF-074-02-03 | PACKAGE_REGISTER.csv row 51 lists "No package-specific exclusions stated in source materials" as TBD. | PACKAGE_REGISTER.csv row 51 Exclusions column | DBM-Deepcut current-scope NGL mercaptan treating section (no explicit exclusion list) | Specification Scope (Excluded) | Adopt the exclusions inferred from current-scope boundaries (no on-site regeneration, separate downstream packages, incinerator at 3-25); flag as ASSUMPTION until a source-validated exclusion list exists. | TBD |
