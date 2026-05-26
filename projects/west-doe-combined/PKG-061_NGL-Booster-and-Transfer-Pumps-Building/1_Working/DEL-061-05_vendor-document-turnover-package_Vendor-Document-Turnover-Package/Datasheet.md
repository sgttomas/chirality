# Datasheet — DEL-061-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-061-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-061` |
| PackageName | NGL Booster and Transfer Pumps Building |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | SOW-0149; SOW-0150; SOW-0151; SOW-0152 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |
| Source Basis | Workbook Packages row 75 (`26020-Packages_Interfaces_4_export.xlsx`, sheet1 row 75); `26020-Package_Requirements.docx` package heading 17 (Tank Pumps / building-scope wrapper) |

## Attributes

| Attribute | Value | SourcePath / SectionRef |
|---|---|---|
| Package CoA Tracking Number | `26020-01-18-002` | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, col C |
| Package WBS | `01` | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, col B |
| ID # | `61` | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, col A |
| Package Discipline | Mechanical | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, col E |
| Building character | Self-framing building erected at site | `_Sources/26020-Package_Requirements.docx` Tank Pumps section, "Self-framing building to be erected at site." (ASSUMPTION: applies to PKG-061 building wrapper; package heading 17 referenced by decomposition is the building wrapper around PT-18-002 et al., location TBD for an explicit building heading) |

## Conditions (vendor document scope)

| Condition | Value | Source |
|---|---|---|
| Interfaces in vendor scope (Applicability = X on row 75) | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas / Safety Systems; Maintenance Access; Structural/Foundations/Supports | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, cols F-U |
| Interfaces explicitly out (no `X`) | Cathodic Protection; Communications/Network; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75, cols N, P, T, V, W |

## Construction (Vendor Document Set — anticipated)

The vendor document set anticipated for turnover is derived from the comparable Mechanical/rotating package listing in `26020-Package_Requirements.docx` (Tank Pumps section, "Vendor Engineering Deliverables" table). Inclusion in the PKG-061 turnover scope is ASSUMPTION based on package-grouping heuristic; final list confirmed at Vendor Document Index (PRQ-009).

| Group | Document IDs | Source |
|---|---|---|
| Core vendor documents | PRQ-009; DOC-008; QLT-006; QLT-003; QLT-013; QLT-020; QLT-021; PRQ-013; PRQ-015; PRQ-016 | `_Sources/26020-Package_Requirements.docx` Tank Pumps "Vendor Engineering Deliverables" |
| Core package engineering | MEC-001; MEC-002; MEC-003; MEC-006; MEC-014; MEC-016; MEC-017; MEC-018; MEC-021; MEC-022; MEC-023; MEC-024; MEC-025 | ibid. |
| Rotating equipment / pumps | MEC-004; MEC-007; MEC-019; PRO-013; ELE-011 | ibid. |
| Relief / flare / vent design | PRO-014; PRO-015; PRO-016; PRO-017; PRO-018 | ibid. |
| Process piping interfaces | PRO-008; PIP-003; PIP-004; PIP-006; PIP-007; PIP-008; PIP-009; PIP-017; PIP-018; PIP-024; PIP-025; PIP-028 | ibid. |
| Utility piping | PRO-011 | ibid. |
| Drainage / containment | PRO-023; CIV-014 | ibid. |
| Electrical / lighting / EHT / grounding | ELE-002; ELE-003; ELE-014; ELE-015; ELE-016; ELE-020; ELE-027; ELE-028; ELE-029; ELE-030; ELE-017; ELE-018; PIP-020; PIP-021; ELE-012; ELE-019 | ibid. |
| I&C | INS-002; INS-003; INS-005; INS-006; INS-008; INS-009; INS-010; INS-011; INS-016; INS-017; INS-018; INS-025; INS-029; CTL-003; CTL-005; CTL-006; CTL-026 | ibid. |
| Building / HVAC / code | PRO-024; TSF-023; REG-021; STR-002; STR-012 | ibid. |
| Fire & gas / technical safety | TSF-002; TSF-003; TSF-004; TSF-009; TSF-011; TSF-013; TSF-028 | ibid. |
| Structural / foundations / access | STR-001; STR-004; STR-005; STR-006; STR-011; STR-013; STR-014; STR-020 | ibid. |

## References

- `_Sources/26020-Package_Requirements.docx` — package basis document (Tank Pumps heading referenced as nearest source slice for vendor document set; building-wrapper heading 17 referenced by decomposition — explicit building section location TBD).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 75 confirms package identity, discipline, and interface applicability.
- Decomposition: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` line 418.
