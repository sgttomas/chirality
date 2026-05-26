# Guidance: DEL-076-05 — Vendor Document Turnover Package

> Directional guidance for preparing, reviewing, and turning over vendor documentation for PKG-076 Lube Oil Supply. Rationale draws from accessible sources; unsupported considerations marked `TBD` or `ASSUMPTION`.

## Purpose

DEL-076-05 exists so that the operator and the EPC Integrator receive a coherent, traceable, and reviewable set of vendor documents for the Lube Oil Supply package — sufficient to support operation, maintenance, regulatory and turnover obligations, and integration with the broader 03-25 / 04-25 facility scope. The decomposition explicitly classes this as a Vendor Document Turnover production unit anchored by the EPC Scope of Work (DEL-076-01) and Package Datasheet (DEL-076-02).

## Principles

1. **Source-anchored content.** Vendor documents derive content from the EPC Scope of Work, Package Datasheet, and the DBM mechanical-package documentation classes (DBM 3-25 line 617). Vendor content shall not invent project basis values not present in those upstream sources.
2. **Register-first.** The vendor document register is the single index of record for what must be submitted. Every submittal exists as a register row; nothing turns over outside the register.
3. **EPC integration review is a gate, not a courtesy.** EPC Integrator review status must be recorded before turnover acceptance because the broader facility integration depends on document consistency across packages (PKG-076 vs the 04-25 utility-shared lube-oil scope per DBM 4-25 line 1835).
4. **Source documents stay as evidence.** Source-required vendor document table rows remain artifacts under this deliverable; per `_CONTEXT.md` Notes they are explicitly not separated out into independent deliverables.
5. **TBD is allowed; invention is not.** Where document control basis, hazardous-material list, or numbering scheme are not accessible, leave the field `TBD` and surface it for human ruling rather than synthesizing a project standard.

## Considerations

- **Cross-facility utility split.** The DBM assigns lube oil partially to shared cross-facility utility service (DBM 4-25 line 1835: "lube oil storage and pumping" is in the 04-25 shared utility basis). The boundary between PKG-076 documentation and 04-25 utility scope documentation needs explicit confirmation; the register should make scope-edge documents traceable.
- **Hazardous-material classification.** Lube-oil storage is referenced to the project hazardous-material list which the DBM records as not available in the workspace (DBM 3-25 line 507). Vendor documents that depend on this classification should cite the project list when issued and flag `TBD` until then.
- **Document class completeness.** The DBM mechanical-package documentation list (line 617) is the minimum bar for class coverage. Missing any of these classes (e.g., no utility load summary) is a register-completeness defect, not merely a content defect.
- **Lube-oil basis consistency.** DBM 4-25 lines 2059-2068 fix the cylinder lube-oil 400 bbl heated tank, pump P-9240-1, and crank-case basis. Vendor datasheets that disagree must be reconciled before acceptance.
- **Turnover record vs document register confusion.** Turnover records (acceptance, handover, as-built) are distinct from the document register; both are required and should not collapse into one another.

## Trade-offs

- **Strict register discipline vs vendor flexibility.** A strict register reduces audit risk but may slow early-issue submittals. Recommended: enforce register discipline at IFA/IFC issue, allow informal pre-IFA exchange.
- **Document control via EPC vs vendor system.** Routing all vendor documents through the EPC EDMS preserves a single facility document set, but increases EPC document control load. (Project document control basis: `TBD`.)
- **Coverage breadth vs deliverable scope.** Including utility-shared lube-oil documents under PKG-076 increases this package's turnover load but reduces 04-25 utility-package fragmentation. Owner-level ruling required.

## Examples

- A vendor lube-oil tank datasheet (R-076-05-03) should align quantitatively with DBM 4-25 line 2067 (400 bbl heated tank) and reference the cylinder lube-oil pump P-9240-1 from line 2068.
- A vendor cause-and-effect submittal (R-076-05-02) should map to the EPC Package Datasheet (DEL-076-02) shutdown and protection logic interfaces — explicit mapping `TBD` because DEL-076-02 content is not yet drafted.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Scope split for lube-oil storage documentation: PKG-076 (Lube Oil Supply) vs 04-25 shared utility scope. | `_CONTEXT.md` (PKG-076 scope: vendor document turnover for Lube Oil Supply) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1835 ("lube oil storage and pumping" within 04-25 utility shared support) | Datasheet § Construction; Specification R-076-05-01, R-076-05-09; this Guidance § Considerations | PROPOSAL: include lube-oil storage and transfer vendor documents under PKG-076 since `_CONTEXT.md` names "Lube Oil Supply" as the package; route 04-25 distribution-side utility doc rows by reference. | TBD |
| C-02 | Hazardous-material classification for lube-oil storage. | DBM 3-25 line 507 (references project hazardous-material list; list not in workspace) | None — list absent | Datasheet § Conditions; Specification R-076-05-04 | PROPOSAL: hold hazardous-material classification fields as `TBD` until the project hazardous-material list is supplied. | TBD |
| C-03 | Document control basis (numbering, revision codes, EDMS) is not in the accessible source set. | None accessible | None accessible | Specification R-076-05-08 | PROPOSAL: defer document control basis to the EPC project document control procedure when issued; `TBD` until then. | TBD |
