# Guidance — DEL-077-01_scope-of-work (PKG-077 Methanol Injection)

## Purpose

The Scope of Work for PKG-077 Methanol Injection exists to anchor a workbook-defined, vendor-owned Mechanical package as a distinct flat project package on WBS 01, and to record the integrator-side narrative that lets the rest of the project plan around it. It is the mandatory Gate 5 EPC anchor deliverable for this package. Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work`; `SCOPE_LEDGER.csv` row `SOW-0143`.

## Principles

- **Vendor owns the package; integrator owns the integration.** The Package Vendor is accountable for package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator authors this Scope of Work and is accountable for facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-077` ResponsibilityNote.
- **Workbook row 72 is authoritative.** Where this Scope of Work touches package identity, function, responsibility, or applicable interfaces, the workbook row 72 text (carried into `PACKAGE_REGISTER.csv`) is the authority. Do not invent facts; mark `TBD` if source text is not locally accessible. Source: `SCOPE_LEDGER.csv` row `SOW-0143` Notes.
- **Surface every applicable interface, do not collapse them.** All 13 interface types listed for PKG-077 are flagged YES (applicable) and must each be enumerable in the Scope of Work. Source: `INTERFACE_REGISTER.csv`.
- **Carry the Gate 6 disposition.** Methanol Injection scope is included with the Cryogenic Unit package scope per Gate 6; the Scope of Work must record this so downstream EPC integration does not double-count or miss the relationship. Source: `PACKAGE_REGISTER.csv` row `PKG-077` Notes.

## Considerations

- **Objective traceability is broad.** PKG-077 supports eight objectives (OBJ-001, OBJ-004 through OBJ-010), which means the Scope of Work touches facility scope (OBJ-001), vendor-package execution model (OBJ-004), electrical power integration (OBJ-005), controls integration (OBJ-006), shared utilities including fuel gas (OBJ-007), civil (OBJ-008), sour-service safety (OBJ-009), and operability (OBJ-010). Each objective should be visible in the narrative or interface list, not silently absorbed. Source: `OBJECTIVE_REGISTER.csv`.
- **Tagged equipment text is not in registers.** The workbook row 72 detailed major-equipment text is referenced by `PACKAGE_REGISTER.csv` and `ARTIFACT_REGISTER.csv` ART-F30A41723D but is not surfaced in the snapshot registers. Drafting the tagged-equipment list requires opening the workbook source slice before finalization. Until then, mark `TBD`. Source: `ARTIFACT_REGISTER.csv` ART-F30A41723D.
- **Sour-service applicability is asserted via OBJ-009 but design conditions are unsourced locally.** Design pressures, temperatures, methanol grade/quality, injection rate, and any code citations (e.g., NACE MR0175 / ISO 15156) are not present in the locally accessible registers and remain `TBD` or `ASSUMPTION` until vendor data or workbook detail is brought into the deliverable.

## Trade-offs

- **Breadth versus precision.** The Scope of Work is required to cover the full package scope, but the deeper engineering values (sizing, set points, materials) belong to vendor-authored deliverables (e.g., DEL-077-02 datasheet, DEL-077-04 vendor-engineered-equipment package). The integrator-authored Scope of Work should be complete in identity, function, responsibility, interfaces, boundaries, and integration narrative — and deliberately silent (or TBD) on values that vendor deliverables will own.
- **Gate 6 grouping versus distinct-package tracking.** Methanol Injection is dispositioned to ride with the Cryogenic Unit package per Gate 6, while still being tracked as its own flat package (PKG-077). The Scope of Work must hold both true simultaneously rather than choosing one.

## Examples

- TBD — no exemplar Scope of Work for a methanol-injection package is locally available in `_Sources` or the snapshot. Future revisions may incorporate an example once a peer-package SOW is referenced.

## Conflict Table (for human ruling)

None at Pass 1/Pass 2. No source-vs-source conflicts were identified within the locally accessible registers.
