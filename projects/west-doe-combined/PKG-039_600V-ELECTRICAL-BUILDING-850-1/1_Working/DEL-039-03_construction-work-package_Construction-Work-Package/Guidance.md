# Guidance: DEL-039-03_construction-work-package

## Purpose

The Construction Work Package turns the accepted `PKG-039` package basis for the 600V ELECTRICAL BUILDING (850-1) into construction-facing instructions, tie-in planning, inspection evidence, and turnover records. It is an EPC Integrator deliverable for physical installation and facility integration, not a vendor package design deliverable.

This guidance is grounded in `_CONTEXT.md`, Gate 7 register rows for `DEL-039-03_construction-work-package` and `PKG-039`, Workbook Packages row 41, and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical-building and construction-responsibility sections.

## Principles

- Preserve the responsibility split. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-039`.
- Treat the twelve `PKG-039` interface facts as construction checklist items, not optional context. Source: `INTERFACE_REGISTER.csv` rows for `PKG-039`.
- Keep the electrical-building installation basis source-specific: prefabricated modular building, general-purpose area, elevated on piles, bottom cable entry, TECK/ACIC cabling, EMT between adjacent equipment, exterior GFI receptacle, equipment-door removal allowance, and n + 1 HVAC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings".
- Carry source gaps forward as `TBD`. Coordinate-level layout, drawing-based conflict checks, detailed workface manpower loading, lift studies, scaffolding, sequencing, and package-specific turnover line items are not available from the current source set.
- Use construction records to prove installation readiness, tie-in completion, inspection acceptance, and turnover completeness. The work package should be auditable against `ART-298F584585`, `ART-93DCDB7068`, and `ART-17C0FB26AE`.

## Considerations

### Installation Basis

The building is not an ordinary field-built enclosure in the available DBM basis. The source describes electrical buildings as prefabricated, modular buildings. Construction planning should therefore emphasize receiving, off-loading, setting modules on foundations, field hook-up, shipped-loose items, structural supports, home-run cables, and electrical terminations. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Construction Responsibility".

### Interface Completeness

The twelve interfaces carried for `PKG-039` cover utility piping, drains/containment, electrical power, grounding/bonding, exterior lighting, I&C/control cabling, communications/network, building HVAC/services, fire and gas/safety systems, maintenance access, civil grading/drainage/containment, and structural/foundations/supports. The construction interface and turnover checklist should include an explicit row or evidence item for each interface.

### Electrical Inspection and Certification

Electrical materials and equipment are to be designed, fabricated, installed, tested, and inspected according to applicable codes, regulations, and the inspection authority designated by Tourmaline Oil Corp. Supplied electrical equipment is to be new, current design, and third-party certified by CSA, ULc, FM, ETL, or another acceptable NRTL. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical inspection/certification paragraphs.

### Grounding and Bonding

Grounding is a construction-critical verification topic. The construction package should require two direct ground-grid connections for major electrical equipment, ground wells at electrical buildings, and bolted ground connections at test points. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraph.

### Missing Detail

The current source set does not include plot plan CIV-235633-5002 or a PKG-039 vendor construction extraction. Do not fill those gaps with generic construction detail. Use `TBD` and route them to human/vendor resolution before field release.

## Trade-offs

| Topic | Preferred treatment | Reason |
|---|---|---|
| Vendor package detail vs EPC construction planning | Reference vendor design as an input and keep EPC construction scope focused on site installation, tie-ins, inspection, and turnover | Preserves the Gate 7 responsibility model for vendor-owned electrical packages |
| Interface checklist breadth vs field usability | Include all twelve source-supported interfaces, with `TBD` where line-item detail is unavailable | Avoids dropping source-supported interface facts while preventing invented details |
| Plot-location precision vs source fidelity | Mark coordinate-level layout and drawing-based checks `TBD` until CIV-235633-5002 is available | The DBM identifies the plot plan as an external deliverable gap |
| Generic construction procedure vs package-specific evidence | Use generic workface structure only where source detail is absent, and label unresolved package-specific inputs `TBD` | Keeps the deliverable useful without overstating unavailable vendor/detail design information |

## Examples

Example construction checklist entries supported by the source set:

- Verify the building is set on piles with bottom-entry cable tray space available under the building. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings".
- Verify grounding records show two direct ground-grid connections for major electrical equipment and bolted test connections at ground wells. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraph.
- Verify the turnover checklist addresses communications/network, control cabling, HVAC/services, fire and gas/safety systems, and maintenance access interfaces. Source: `INTERFACE_REGISTER.csv` rows for `PKG-039`.
- Record coordinate-level placement and drawing-based access checks as `TBD` pending plot plan CIV-235633-5002. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plot-plan gap paragraph.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No direct source conflict identified in accessible materials. Remaining issues are source gaps marked `TBD`. | N/A | N/A | N/A | N/A | N/A |
