# Guidance — DEL-043-02 Package Datasheet (PKG-043)

> Directional document. Provides rationale and considerations for authoring and using the package datasheet for PKG-043 *Instrumentation (outside of Mechanical Packages only)*.

## Purpose

The Package Datasheet exists to give a third-party vendor or discipline package engineering team the technical handoff data they need to engineer and design PKG-043 within the EPC Integrator's intent (`DELIVERABLE_REGISTER.csv` row 241 `Description`). It is the **mandatory Gate 5 EPC anchor deliverable** and also functions as the **evidence carrier for package interface facts** rather than promoting each interface to a standalone deliverable (`_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row 241 `Notes`).

## Principles

1. **Source-anchored.** Every non-trivial value cites a source slice (`SourcePath + SectionRef`) or carries `TBD` with `location TBD`. Decomposition prose is routing, not authority (`SKILL.md` Authority Hierarchy).
2. **Interface facts travel with the datasheet.** The five Gate 6 interfaces for PKG-043 (Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network) are intentionally carried here as artifact rows, not as independent deliverables (`_CONTEXT.md` Notes).
3. **Plug-n-play package philosophy.** Each PKG-043 interface row carries the Gate 6 disposition that instrumentation field supports, power, and communications are included in each package scope as appropriate (`INTERFACE_REGISTER.csv` PKG-043 Notes). The datasheet inherits this disposition.
4. **No invented responsibility model.** Responsibility is source-dependent; no separate vendor-package ownership model is to be inferred (`PACKAGE_REGISTER.csv` row 45 `ResponsibilityModel`).
5. **Respect package title scope.** PKG-043 explicitly excludes instrumentation that lives inside Mechanical Packages; do not consume mechanical-package-internal instrumentation into this datasheet (`PACKAGE_REGISTER.csv` row 45 `Name`).

## Considerations

- The workbook (`26020-Package_Requirements.docx`) and packages/interfaces export (`26020-Packages_Interfaces_4_export.xlsx`) hold most clause-level data (service conditions, equipment, area classification, signal protocols). They are listed in `_REFERENCES.md` but are binary office documents; until a source slice is extracted, populated datasheet values for these topics MUST be `TBD`.
- DBM context (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) is cited by `PACKAGE_REGISTER.csv` `SourceRefs` and can inform context but is not equivalent to a package datasheet source for design values.
- The objective association (OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010) is recorded under `PACKAGE_HEURISTIC` and labeled ASSUMPTION pending explicit mapping (`SKILL.md` Step 1.3; `_CONTEXT.md` Supports Objectives).
- The package has `OpenIssue = FALSE` (`PACKAGE_REGISTER.csv` row 45), so no register-level dispute blocks Gate 5 readiness; readiness gating now depends on workbook clause-level extraction sufficient for vendor handoff.

## Trade-offs

- **Evidence-carrier vs. discipline cleanliness.** Carrying interface facts inside the datasheet keeps EPC anchor evidence consolidated but adds matrix content that some teams normally split into a separate interface register. The decomposition Note explicitly chose consolidation; this guidance follows that choice.
- **`TBD` vs. plausible defaults.** It is tempting to fill conventional instrumentation defaults (e.g., 4-20 mA loops, NEMA 4X, standard signal counts). The skill's non-negotiable constraints disallow this when source slices are not opened. Prefer `TBD` over plausible defaults.
- **Granularity of the interface requirements matrix.** A matrix at the *interface-type* level is supported by the snapshot (five rows). A matrix at the *tag/loop* level requires workbook extraction and is currently `TBD`.

## Examples

- Identification table in `Datasheet.md` is fully populated from `PACKAGE_REGISTER.csv` row 45 and `DELIVERABLE_REGISTER.csv` row 241 — this is the pattern for source-grounded population.
- Interface inventory in `Datasheet.md` cites `INTERFACE_REGISTER.csv` PKG-043 rows verbatim including `InterfaceID` — this is the pattern for carrying interface facts as datasheet evidence.
- Service / process conditions block is left as `TBD` — this is the pattern for a topic that requires workbook extraction; it is *not* to be filled with convention.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none observed) | No conflicts between accessible sources observed in this pass. | — | — | — | — | TBD |
