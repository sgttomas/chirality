# Guidance — DEL-044-02 Package Datasheet (PKG-044 Instrumentation)

## Purpose

This guidance supports drafters and reviewers of the EPC Package Datasheet for PKG-044, "Instrumentation (outside of Mechanical Packages only)." The datasheet is a Gate-5 EPC anchor deliverable; it is the technical handoff that lets a third-party vendor or discipline team engineer the package without inventing facts that should have come from the EPC Integrator. Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-044-02).

## Principles

1. **Source-grounded, not narrative-grounded.** Identity, interfaces, and design conditions in the datasheet must trace back to PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv, the workbook row 46 entry, or the governing DBM (DBM-Comp_and_Liquids). Decomposition prose is route, not authority. (See `_REFERENCES.md`; PACKAGE_REGISTER.csv `SourceRefs` field for PKG-044.)
2. **Interface facts live here.** Per `_CONTEXT.md` notes: "interface facts are intentionally carried here as evidence rather than standalone deliverables." The five interface rows (Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network) must appear verbatim in type and count.
3. **Plug-n-play scope philosophy.** Gate 6 disposition (INTERFACE_REGISTER.csv) clarifies that instrumentation field supports, power, and communications belong inside the owning package scope as appropriate. Drafters should not silently push these to a different package without source warrant.
4. **Conservative inference.** Where the workbook row or referenced DBM does not state a value, mark `TBD` (with location TBD where the source pointer is known but the slice is unread) rather than invent. ASSUMPTION labels are required for any best-effort inference.

## Considerations

- **Mechanical-package-internal instrumentation is excluded.** The package name itself ("outside of Mechanical Packages only") scopes out instrumentation embedded in vendor mechanical packages. Field instrumentation that supports those mechanical packages but is installed by the EPC Integrator may still fall in scope; resolve by reading the specific mechanical package's scope-of-work before assigning a tag here. (ASSUMPTION on edge cases; needs human ruling for borderline tags.)
- **Analyzer scope is partly open.** Final analyzer technology, placement, and tag list remain TBD per the governing DBM (DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 509). The datasheet should record the analyzer-quality air conditions but should not pre-commit to specific analyzer models.
- **Standards register is provisional.** The DBM directs that "the final standards register shall be verified against the latest project specification index" (DBM-Comp_and_Liquids, line 888). Treat the project instrumentation specs (ELC-QAS-000014-001, -000015-001, -000018-001) as the working set and flag any later revision as a register change.
- **Cross-package utilities.** Power and utilities (fuel gas, instrument air) are shared between 03-25 and 04-25 (DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 716; DBM-Deepcut/4-25_Deepcut_DBM.md, lines 75, 95). The datasheet must not redefine these allocations; it consumes them.

## Trade-offs

| Trade-off | Lean toward | Source / rationale |
|---|---|---|
| List specific tag identities vs. mark TBD | Mark TBD with location pointer when row 46 has not been read in the current run | Source-fidelity invariant; workbook row binary not directly readable here |
| Replicate vs. reference the package interface matrix | Replicate the matrix in the datasheet (interface facts are evidence here) | `_CONTEXT.md` Notes |
| Embed DBM design-condition values vs. reference DBM only | Embed value with citation in Conditions table | Vendor handoff quality |
| Add a custom standards subset for this package vs. cite project register | Cite project register; subset is TBD until confirmed | DBM-Comp_and_Liquids, line 888 |

## Examples

Source-grounded condition row (illustrating the citation pattern used in `Datasheet.md`):

> Minimum design ambient temperature: -40 deg C governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. Source: DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 145).

TBD example (correct form):

> Equipment tag list for PKG-044: TBD (location TBD; expected in Workbook Packages row 46, file `_Sources/26020-Package_Requirements.docx` and/or `_Sources/26020-Packages_Interfaces_4_export.xlsx`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| C-044-02-01 | None observed in current pass between drafted documents and accessible sources. | n/a | n/a | n/a | n/a | n/a |

(No cross-document or cross-source conflicts surfaced in Pass 1 / Pass 2 of this run. Future passes — particularly after reading workbook row 46 directly — may need to populate this table.)
