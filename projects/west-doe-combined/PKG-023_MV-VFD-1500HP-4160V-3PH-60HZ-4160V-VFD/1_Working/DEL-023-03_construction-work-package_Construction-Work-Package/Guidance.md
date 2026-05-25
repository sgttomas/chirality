# Guidance: DEL-023-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-023` into a source-supported plan for physically installing, tying in, inspecting, and turning over the MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package as part of the 04-25 Deepcut facility. It should make the EPC integration boundary visible to the Tourmaline field construction organization while keeping vendor-owned package design distinct from facility integration scope.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat the six workbook interface `X` facts as evidence carried under the Construction Work Package, not as separate deliverables.
- Keep vendor-owned package engineering/design with the Package Vendor and field construction with Tourmaline; reserve facility integration and tie-in planning for the EPC Integrator.
- Use `TBD` for VFD topology, harmonic mitigation, driven motor identity, lift/rigging weights, foundation loads, energization sequence, and detailed commissioning steps until a source-supported package-specific basis is available.
- Use DBM electrical and construction-responsibility basis only at the level it supports: 4.160 kV service basis, cable schedule, grounding/bonding, cable tray/conduit, area classification for VFD-fed motors, electrical-building housing possibilities, and Tourmaline field construction scope items.

## Considerations

The DBM medium-voltage service basis explicitly assigns the 4.160 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded system to facility process AC inverter-drive motors rated 250 hp up to 5,500 hp. A 1,500 hp 4160 V VFD falls within this band, so the construction work package can reasonably rely on the 4.160 kV service basis for feeder and grounding decisions while flagging that the DBM also states "VFD and soft-starter requirements for 4.16 kV motors are TBD."

The DBM Construction Responsibility section is explicit that grading, piling, foundation work, setting modules/equipment on foundations, mechanical hookup, miscellaneous structural support installation, field-installed home-run cables, and electrical terminations are Tourmaline field construction scope. The construction work package should organize its work breakdown around these named activities and identify where vendor-supplied skids or modular sub-assemblies arrive ready-to-set versus requiring field assembly.

Tie-ins to existing or related facilities require joint planning, and tie-in timing is to be established as the project progresses. Interconnecting piping to ISBL/OSBL tie-in points is explicitly flagged as external interface responsibility "to be confirmed for each tie-in." For an electrical VFD package this most naturally maps to feeder tie-in at the 4.16 kV switchgear, control/communication tie-ins to the plant PLC/network, and grounding/bonding tie-in to the facility ground grid; package-specific tie-in points themselves remain `TBD` pending integration design.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The construction work package should require routing and physical placement to preserve withdrawal envelopes for VFD cells, isolation transformers (if present), and the driven motor, but detailed clearance dimensions remain `TBD` until detailed design or vendor data are available.

Area classification language in the DBM only obligates Zone 2 marking and reduced temperature code on VFD-fed motors, not on the VFD lineup itself (which the DBM places in electrical buildings as general-purpose installations). The construction work package should preserve this distinction.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Driven motor identity / load | Mark `TBD` pending package-specific source confirmation. | No accessible source slice identifies which 1,500 hp motor service or process unit the PKG-023 VFD feeds. |
| VFD topology / harmonic mitigation | Treat as vendor-owned design; preserve `TBD` for construction scope. | DBM does not specify topology, isolation transformer, or filter requirements at 4.16 kV. |
| Installation location | Identify "electrical building, location TBD" as the most defensible default. | DBM says electrical buildings may house MV VFDs but does not locate PKG-023. |
| Tie-in to 4.16 kV switchgear bus | Identify as the most plausible feeder tie-in path; keep specific switchgear cell `TBD`. | DBM defines 4.16 kV service for 250-5,500 hp inverter-drive motors but does not assign a specific bus to PKG-023. |
| Standards | List CEC, area classification, project electrical specifications, and `26020-Package_Requirements.docx` as governing bases with locations TBD. | DBM references these bases but detailed clauses and the requirements document slice were not opened for PKG-023 in this run. |

## Examples

- Acceptable construction-work-package entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 25 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "VFD lift weight and rigging plan: TBD. No package-specific source slice available; vendor outline drawing required."
- Acceptable construction-responsibility entry: "Grading, piling, foundation work, setting equipment on foundations, mechanical hookup, electrical terminations, and home-run cables are Tourmaline field construction scope. Source: DBM Construction Responsibility section."
- Not acceptable without new source: "The PKG-023 VFD feeds the inlet/sales compressor motor at 1,500 hp." The accessible source set does not establish that assignment.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-023-03-001 | Package title asserts "MV VFD - 1500HP, 4160V" but no accessible source slice identifies which motor / driven equipment the VFD feeds or confirms the 1,500 hp rating against a process load. | Workbook Packages row 25; `PACKAGE_REGISTER.csv` row `PKG-023` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services / motors paragraphs | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "1500HP, 4160V" as title/identity only and keep the driven-motor assignment, load type, and starting method `TBD` until vendor data or detailed mechanical/electrical source is accepted. | TBD |
| HRR-023-03-002 | DBM states "VFD and soft-starter requirements for 4.16 kV motors are TBD," but PKG-023 is specifically a 4160 V VFD package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph | Workbook Packages row 25 (package exists and is named as a 4160 V VFD) | Specification Requirements; Procedure Steps | Construction Work Package shall not assume topology, isolation transformer, or filtering requirements from the DBM and shall require vendor data plus a project-side requirements confirmation before construction execution. | TBD |
| HRR-023-03-003 | Construction-work-package construction interface and turnover checklist artifact is anticipated, but no source slice defines its content scope for this package. | `_CONTEXT.md` Anticipated Artifacts | `_Sources/26020-Package_Requirements.docx` (not opened for PKG-023 in this run) | Specification Documentation; Procedure Records | Open `26020-Package_Requirements.docx` for a PKG-023 match in a follow-up run, then refine checklist scope; until then, treat the checklist content as `TBD`. | TBD |
