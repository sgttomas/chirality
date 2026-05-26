# Guidance — DEL-044-01 Scope of Work

Directional guidance for drafting and reviewing the EPC Integrator Scope of Work for PKG-044.

## Purpose

The Scope of Work exists to give the EPC Integrator a binding, source-grounded definition of what PKG-044, "Instrumentation (outside of Mechanical Packages only)," includes, what it excludes, how it integrates into the whole facility, and who is responsible for delivering it. It is one of the four mandatory Gate 5 EPC anchor deliverables for this package (`DELIVERABLE_REGISTER.csv` Notes).

## Principles

1. **Workbook row is authoritative.** PKG-044 is defined by Workbook Packages row 46 (`PACKAGE_REGISTER.csv`; `SCOPE_LEDGER.csv` Notes). Do not redefine the package from convention or prior drafts.
2. **Decomposition routes; sources determine content.** The GATE-07 PROJECT_DECOMP snapshot tells the SoW which rows it must reflect; the underlying source rows determine what the SoW actually says.
3. **Plug-n-play package philosophy.** Per the Gate 6 disposition recorded in `INTERFACE_REGISTER.csv`, instrumentation field supports, power, and communications are included in each package scope as appropriate. The SoW MUST be written so the package is buildable as a self-contained, integrable unit.
4. **Boundary discipline.** The package explicitly excludes instrumentation carried inside Mechanical Packages. Cross-package instrumentation MUST NOT be silently absorbed into PKG-044.
5. **Provenance over polish.** Every non-trivial sentence in the SoW should be traceable to a register row, a source row, or an explicit ASSUMPTION/TBD label (K-PROV-1).
6. **Agent proposes, human decides.** EPC Integrator vs. discipline subcontractor allocation is source-dependent and remains a human ruling (`PACKAGE_REGISTER.csv` Notes; ART-42A035696B).

## Considerations

- **Tagged equipment list.** The locally accessible decomposition rows do not enumerate equipment tags for PKG-044. The SoW carries this as TBD pending extraction from Workbook Packages row 46 (Excel). Do not invent tags or quantities from convention.
- **Interface set.** Five interface types are recorded (Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network). The SoW MUST present these as the package's confirmed physical interfaces, with the Gate 6 disposition that field supports, power, and communications are included as appropriate.
- **Boundary caveat language.** Use the recorded caveat verbatim: "Field supports, power, and communications are not marked unless confirmed by package scope." This is the standing project rule for not over-claiming inclusion.
- **Objective linkage.** PKG-044 supports OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 at the package level (`OBJECTIVE_PACKAGE_MAP.csv`). The SoW deliverable supports the same set per `OBJECTIVE_DELIVERABLE_MAP.csv`. Treat package-grouped objective association as directionally relevant context (ASSUMPTION until human-confirmed at the deliverable level), per the OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC default.
- **Sibling deliverables in the same package.** Avoid duplicating content from `DEL-044-02_package-datasheet` (interface fact evidence carried there), `DEL-044-03_construction-work-package`, or `DEL-044-04_epc-instrumentation-discipline-production-package`. The SoW frames; the sibling deliverables fulfill.
- **Whole-facility integration.** ART-0F86ED2722 calls for an integration narrative explaining what the package does and how it integrates into the process facility. Anchor this narrative on the five recorded interface types and the WBS 02 placement.

## Trade-offs

- **Conservative vs. complete.** Locally accessible source rows are thin on equipment-level detail. Preference is conservative ("TBD with cited gap") over fabricated completeness. The cost is more open items at Gate 5 review; the benefit is no rework from inserted-then-removed claims.
- **EPC Integrator vs. discipline subcontractor.** Naming a responsible entity prematurely creates a downstream contractual constraint; leaving it TBD slows commercial close. The current source set does not support a default assignment beyond "EPC Integrator delivers the SoW" — discipline execution responsibility is source-dependent.
- **Inclusion language for field supports / power / comms.** Stating these are included unconditionally over-claims beyond source; stating they are excluded contradicts the Gate 6 disposition. The SoW MUST use the conditional phrasing recorded in source ("as appropriate" / "unless confirmed by package scope").

## Examples

- **Good:** "PKG-044 includes the Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network interfaces recorded in INTERFACE_REGISTER.csv (rows IFC-A0182B4C75, IFC-9E42D79051, IFC-0DD8B45540, IFC-20C7248CDB, IFC-0664000480). Per the Gate 6 disposition, instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play philosophy."
- **Bad:** "PKG-044 includes all field instrumentation, wiring, and network components for the facility." (Over-claims beyond package boundary and source language.)
- **Good (TBD handling):** "Tagged equipment list: TBD — Workbook Packages row 46 (Excel) not extracted in this iteration; carried as open item per ART-764F78E24A."
- **Bad (TBD handling):** Listing inferred transmitter or PLC tags with no source citation.

## Conflict Table (for human ruling)

None identified in this iteration. The accessible decomposition rows are internally consistent for PKG-044 / DEL-044-01.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
