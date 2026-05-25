# Guidance: DEL-015-03_construction-work-package

## Purpose

The Construction Work Package exists to translate the accepted Gate 7 package basis for `PKG-015` into an executable plan for how the Transformer TXP-8300-1 step-down distribution transformer will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It is owned by the EPC Integrator and executed within the DBM Construction Responsibility basis. It should not restate vendor-owned package engineering or design; it should plan facility-side construction and integration around the vendor-supplied physical equipment.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V" because that is the workbook and Gate 7 register spelling.
- Plan construction execution under the DBM Construction Responsibility basis (Tourmaline field construction scope); do not invent alternative execution responsibility.
- Treat the seven workbook interface `X` facts for `PKG-015` as construction-execution scope items, not as separate deliverables.
- Keep vendor-owned package engineering, design, and physical equipment with the Package Vendor (`DEL-015-04`); keep vendor documentation in `DEL-015-05`; keep final acceptance evidence in `DEL-015-06`. This deliverable plans construction execution and integration.
- Use `TBD` for vendor nameplate values, BIL, impedance, cooling class, tap configuration, oil volume, weights, lift plan, oil-filling procedure, energization sequence, and protective-relay settings until source-supported values from vendor outputs are accepted.
- Use the DBM electrical basis only at the level it supports: medium-voltage distribution architecture, cable schedule type, foundation basis for transformers, grounding/bonding basis, cable tray and conduit routing, and maintenance-access constraints.

## Considerations

The DBM electrical section establishes the facility power distribution architecture: BC Hydro utility supplies a 25 kV-to-13.8 kV, 50 MVA utility transformer that feeds the 13.8 kV switchgear bus, and the 13.8 kV switchgear distributes radially through step-down transformers to facility loads. PKG-015 is one such step-down transformer (12/15 MVA, 13.8 kV primary, 4160/2400 V secondary). This places the package's electrical-power interface squarely on the 13.8 kV bus upstream and on a 4160/2400 V distribution system downstream, both of which constrain cable schedule selections and grounding execution.

The DBM Construction Responsibility section is the controlling basis for who does the field work. The construction work package narrative and workface plan should map each Tourmaline field construction activity (grading/piling/foundations, setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, structural supports, home-run cable installation, electrical terminations, area lighting) onto the transformer scope, while leaving package engineering/design and physical equipment supply to the Package Vendor.

Foundation and support content should follow the DBM foundation basis (transformers on precast concrete bearing foundations) and the Transformers paragraph (large oil-filled transformers generally installed on structural steel transformer bases, CEC spacing, secondary-containment review). Specific loads and dimensions depend on vendor data and are `TBD`. Containment requirements should be reviewed and biased toward selections that limit containment where practical, consistent with the DBM Transformers paragraph.

Grounding and bonding content should reflect the DBM grounding basis: two-point ground-grid connection for major electrical equipment, separate CEC-sized copper ground conductor for distribution transformers (separate from the grounding conductor run with power wiring), ground wells with bolted/compression connections, and above-grade green-insulated conductors in PVC conduit where mechanical protection is required. Resistor grounding policy at the 25 kV utility transformer and 6.9 kV transformers is documented in the DBM; PKG-015 is a 13.8 kV/4160-2400 V step-down, and resistor-grounding details specific to its secondary system are `TBD`.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The workface plan should preserve access to oil sampling, the tap changer, bushings, and the cooling system; specific clearance values are `TBD` until vendor footprint and access drawings are accepted.

Tie-in coordination should follow the DBM tie-in basis: joint planning is required for tie-ins to existing or related facilities, and tie-in timing is established as the project progresses. The construction interface and turnover checklist (`ART-43ADD84004`) is the appropriate place to record the tie-in plan and its scheduling.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Transformer rating / nameplate values | Carry as `TBD` pending vendor data; only the package title's 12/15 MVA, 13.8 kV / 4160-2400 V identifiers are used. | Workbook title contains rating identifiers, but no accessible source slice provides BIL, impedance, cooling class, tap configuration, oil volume, or weights. |
| Lift plan / rigging / oil filling / energization sequence | Mark `TBD` for vendor-driven content. | These depend on vendor equipment data not yet available in the source set. |
| Installation location (electrical building vs. outdoor pad) | Identify as `TBD`. | DBM identifies electrical buildings as housing for MV switchgear but does not assign PKG-015 transformer to a building, pad, or outdoor location. |
| Foundation type | State precast concrete bearing foundations generally, with structural steel transformer bases for large oil-filled units per DBM, and `TBD` for package-specific selection. | DBM supports both bases at the general level; package-specific choice requires detailed engineering. |
| Standards | List CEC, project electrical specifications, and area classification standards as governing bases with locations `TBD`. | DBM references these bases, but detailed clauses/specification documents are not available in the deliverable folder. |
| Resistor grounding on 4160/2400 V secondary | Treat as `TBD` for PKG-015 secondary system. | DBM specifies resistor values for 25 kV utility transformer, 6.9 kV transformers, and 600 V transformers, but does not state resistor-grounding values for a 13.8 kV/4160-2400 V step-down. |

## Examples

- Acceptable workface-plan entry: "Off-load the transformer at the laydown area and set on the precast concrete bearing foundation using the rigging plan to be provided by the Package Vendor (lift plan: `TBD` pending vendor data)."
- Acceptable interface-coverage entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 17; `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Energization sequence: TBD. Source-supported basis not available; to be established with vendor and commissioning team prior to energization."
- Not acceptable without new source: "Transformer impedance is 8.5 percent; cooling class is ONAN/ONAF; tap changer is De-energized 5-position +/-2.5 percent." The accessible source set does not establish these values.
- Not acceptable: restating vendor-owned engineering or design content from `DEL-015-04` or `DEL-015-05` inside this construction work package; reference and integrate instead.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-015-03-001 | Package title states "12/15MVA 13.8kV/4160/2400V" but the accessible source set does not provide vendor nameplate values (BIL, impedance, cooling class, tap configuration, oil volume, weights) needed to plan rigging, foundation loading, energization, or protective-relay coordination. | Workbook Packages row 17; `PACKAGE_REGISTER.csv` row `PKG-015` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers and foundation paragraphs | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat the title values as identity/identification only and carry detailed transformer parameters as `TBD` until vendor package outputs (`DEL-015-04`) are accepted; integrate by reference rather than restating. | TBD |
| HRR-015-03-002 | Installation location (specific electrical building, outdoor pad, or other) for PKG-015 is not assigned by an accessible source slice; this affects foundation execution, cable routing, area lighting, and maintenance access planning. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | Workbook Packages row 17; Gate 7 `PACKAGE_REGISTER.csv` | Datasheet Construction; Specification Requirements; Procedure Steps | Do not assign a location until detailed design or vendor coordination produces a source-supported placement; carry as `TBD` and re-validate when assigned. | TBD |
| HRR-015-03-003 | Resistor-grounding policy is specified in the DBM for the 25 kV utility transformer, 6.9 kV transformers, and 600 V transformers, but is not specified for a 13.8 kV/4160-2400 V step-down; PKG-015 secondary-system grounding policy is unclear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, neutral grounding resistor paragraphs | Workbook Packages row 17 | Datasheet Conditions; Specification Requirements (REQ-015-03-006); Procedure Steps | Carry secondary-system grounding policy as `TBD` and request a project-electrical decision before construction execution; do not invent a resistor value. | TBD |
