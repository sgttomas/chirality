# Guidance — DEL-105-03 Construction Work Package (Platforms)

## Purpose

This Construction Work Package (CWP) provides the EPC Integrator's plan for physically installing, building, inspecting, and turning over the workbook-defined Structural package "Platforms" (PKG-105) and integrating it with adjacent grading / drainage / containment, area / exterior lighting, and structural-foundation systems. The CWP exists because PKG-105 is a Gate 5 EPC anchor deliverable for SOW-0261, supporting `OBJ-001`, `OBJ-005`, `OBJ-008`, and `OBJ-010`.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-105-03; `SCOPE_LEDGER.csv` SOW-0261; `OBJECTIVE_SCOPE_MAP.csv` PKG-105 rows.

## Principles

1. **Source fidelity.** The PKG-105 source slice is intentionally narrow: one workbook row (ID# 105, CoA `26020-01-36-005`) with three marked physical interfaces and an interface review note. The CWP must reflect that scope exactly. Source: Workbook Packages ID# 105; `INTERFACE_REGISTER.csv` PKG-105.
2. **Integrator-owned tie-ins.** Per the Gate 6 disposition, the EPC Integrator owns platform-to-equipment tie-ins through the overall 3D model and integrated P&ID set; the CWP is the operational expression of that ownership. Source: `PACKAGE_REGISTER.csv` PKG-105; `INTERFACE_REGISTER.csv` PKG-105.
3. **Conservative interface scope.** Interfaces not marked in the workbook for PKG-105 are not assumed; the CWP plans only the three marked interfaces. Adding interfaces requires an upstream decomposition update. Source: Workbook Packages ID# 105 (blank columns for PKG-105).
4. **Defer to downstream design.** Specific structural design, anchor patterns, code-clause compliance, and member sizing are owned by DEL-105-04; the CWP plans how the resulting design is installed and accepted, not what the design is. Source: `DELIVERABLE_REGISTER.csv` DEL-105-04.
5. **TBD over invention.** Where source materials do not state a value (platform count, equipment tag list, code/coating spec), the CWP records `TBD (location TBD)` with a resolution route, rather than inventing values. Source: skill `four-documents` constraints.

## Considerations

- **Layout/model dependence.** The interface review note explicitly says platform-to-equipment tie-ins should be confirmed by layout/model. The CWP cannot complete tie-in geometry without the 3D model state; planning text should reference the model snapshot used. Source: `INTERFACE_REGISTER.csv` PKG-105 InterfaceReviewNotes.
- **Foundation sequencing.** Standard practice (ASSUMPTION at the source-slice level) places foundation work and acceptance before platform erection; the workface plan should make this sequence explicit even though sequencing is not stated in PKG-105 sources.
- **Containment continuity.** Where platforms cross or alter grading / drainage / spill-containment features, the CWP must plan for continuity-of-protection during construction (no breach of containment without compensating measures). Source: `INTERFACE_REGISTER.csv` `IFC-07C472C58B`.
- **Lighting sequencing.** Area / exterior lighting at platforms is both a construction-safety prerequisite (work-area lighting) and a turnover deliverable; the CWP should treat these as separable. Source: `INTERFACE_REGISTER.csv` `IFC-26E3DCAD56`.
- **Tag identity carried by siblings.** Tagged equipment associated with each platform is the subject of DEL-105-01 (Scope of Work) and DEL-105-02 (Package Datasheet); the CWP cites these rather than re-deriving identity. Source: `DELIVERABLE_REGISTER.csv` DEL-105-01, DEL-105-02.

## Trade-offs

- **Generic structural plan vs. project-specific plan.** Because PKG-105 source material does not detail member sizes, coating, or anchor patterns, the CWP is necessarily structured around the artifact triplet and the three interfaces; project-specific content arrives only as DEL-105-04 matures. Carrying `TBD` is preferred over importing generic structural-platform conventions as if they were facts. Source: skill `four-documents` constraints; absence of platform-specific content in `26020-Package_Requirements.docx`.
- **Inspection rigor.** Without a code-clause basis on file, the inspection plan should anchor on the EPC Integrator's structural QA program (location TBD) and the eventual DEL-105-04 output; this is recorded as ASSUMPTION rather than a clause-bound requirement.

## Examples

No example structural-platform CWP from PKG-105 source materials is available (no Platforms section in `26020-Package_Requirements.docx`). Sibling Construction Work Package deliverables in the project (e.g., `DEL-067-03_construction-work-package` for Tanks) provide a shape reference for sequencing structure and turnover record layout, but the technical content of those deliverables does not transfer to platforms.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-105-03-001 | Vendor flag for PKG-105 interfaces is "YES" in `INTERFACE_REGISTER.csv`, yet `PACKAGE_REGISTER.csv` PKG-105 says no separate vendor-package ownership model is inferred. | `INTERFACE_REGISTER.csv` PKG-105 rows (Vendor=YES) | `PACKAGE_REGISTER.csv` PKG-105 ResponsibilityModel | Datasheet Conditions; Specification R-RESP / R-INT; Guidance Principle 2 | PROPOSAL: treat "Vendor=YES" as an interface-level flag (tie-in is vendor-coordinated at the counterparty package) rather than a package-ownership statement; CWP retains EPC-Integrator-owned coordination. | TBD |
| CFT-105-03-002 | Platform count, equipment tags, and coating/material spec are not in any deliverable-local source for PKG-105. | Workbook Packages ID# 105 (no equipment list) | `26020-Package_Requirements.docx` (no Platforms section) | Datasheet Quantities; Specification R-STR-1 / R-CMN-2 | PROPOSAL: carry as `TBD (location TBD)` and route resolution through DEL-105-02 and DEL-105-04 before release-for-construction. | TBD |
| CFT-105-03-003 | "Workbook Packages row 106" cited in registers maps to ID# 105 in the spreadsheet (header offset). | `_CONTEXT.md` and registers (row 106) | `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` (ID# 105 is PKG-105) | All sections citing "Workbook Packages row 106" | PROPOSAL: treat the two references as equivalent (decomposition uses excel row index; spreadsheet ID# uses 1-based data row). No content change. | TBD |
