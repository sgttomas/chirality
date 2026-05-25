# Guidance: DEL-014-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-014` into a source-supported description of how the contactor panels (lighting and exhaust-fan, low-voltage) will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It should make the EPC field-construction scope explicit and keep it separated from vendor-owned package engineering and design.

## Principles

- Preserve source spelling and identity. The package name is carried as "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as construction tie-in scope, not as separate deliverables.
- Keep vendor-owned panel engineering and fabrication with the Package Vendor; keep field installation, terminations, and integration with the EPC Integrator/field construction.
- Use `TBD` for panel count, contactor ratings, enclosure construction/ratings, lighting circuit schedule, exhaust-fan circuit schedule, and assigned installation location until a source-supported package-specific basis is available.
- Use DBM only at the level it supports: construction responsibility scope, voltage/service basis, Remote I/O coordination for exhaust fan/heater controls, electrical-building housing possibilities, grounding/bonding basis, cable tray/conduit constraints, and site environmental envelope.

## Considerations

The DBM Construction Responsibility table assigns field construction broadly to Tourmaline, including off-loading and setting equipment, mechanical hookups, installation of shipped-loose components, miscellaneous structural supports, home-run cabling, electrical terminations, and area lighting. These activities are directly applicable to a contactor panel package that supports lighting and exhaust-fan loads, and they frame the scope of this construction work package.

The DBM electrical voltage table establishes a clear two-level service basis: 120/208 V for lighting/receptacles/heat trace/small motors/UPS ≤10 kVA, and 600 V (HRG, 5 A continuous resistor) for larger motors, lighting transformers, building heaters, and UPS >10 kVA. The PKG-014 package title explicitly notes "LOW VOLTAGE," consistent with the 600 V service basis for upstream feeds and the 120/208 V system for downstream lighting loads. Voltage values cited in this construction work package should follow that table only and not be extrapolated to ratings the source does not support.

The DBM Remote I/O paragraph states that RIO nodes may also support building exhaust fan and heater controls and that safety/process devices should be wired to the nearest RIO panel where practical. For a contactor panel package that includes exhaust-fan contactors, this means controls integration is expected to coordinate with the Remote I/O architecture; specific signal lists, wiring assignments, and termination details remain vendor and detailed-design work.

Grounding and bonding are applicable interface topics. The DBM contains facility grounding basis, including two-point grounding for major electrical equipment and separate copper ground conductors per CEC sizing for certain electrical equipment. The construction work package should require coordination with this basis while avoiding unsupported package-specific conductor sizing or termination details.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The construction work package should require panel placement and cable/conduit routing to preserve maintenance access, but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

The site basis (-40 deg C minimum ambient governing exposed equipment, package buildings, control panels, instrumentation, and field devices) is a hard environmental constraint for any exposed contactor panel or field-mounted component within this package.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Panel quantity / contactor rating | Mark `TBD` pending vendor data or package-specific source confirmation. | No accessible source slice defines panel count or contactor ratings for PKG-014. |
| "LOW VOLTAGE" interpretation | Treat as nominal classification consistent with the DBM 600 V LV service for upstream feeds and 120/208 V for lighting service; do not infer specific equipment ratings from the title alone. | The DBM defines LV as 600 V class; the title does not specify equipment rating. |
| Installation location (electrical building vs. field) | Identify both as candidate locations; mark final location `TBD`. | DBM allows electrical-building housing of MCCs/switchgear/distribution; it does not specifically locate PKG-014 contactor panels. |
| Home-run cabling vs. vendor pre-wired cabling | Treat home-run cabling as field-construction scope per DBM; treat panel-internal wiring as vendor scope. | DBM Construction Responsibility assigns home-run cabling and terminations to field construction; vendor scope owns panel internals. |
| Exhaust-fan control integration | Coordinate with Remote I/O architecture; do not specify a fixed I/O list. | DBM identifies RIO as a possible control path but does not specify the exhaust-fan signal list for this package. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations TBD. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable construction-scope entry: "Applicable tie-in interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 16 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Panel quantity and contactor ratings: TBD. No package-specific source slice available."
- Not acceptable without new source: "Provide three NEMA 4X free-standing lighting/exhaust-fan contactor panels in Electrical Building 02 with 100 A contactors." The accessible source set does not establish any of these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-014-03-001 | The accessible source set does not define panel count, contactor ratings, enclosure construction/rating, lighting/exhaust-fan circuit schedule, or assigned installation location for PKG-014. | Workbook Packages row 16; `PACKAGE_REGISTER.csv` row `PKG-014` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (no package-specific PKG-014 slice) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Carry these values as `TBD` until vendor data or package-specific requirements source (e.g., `26020-Package_Requirements.docx` parsed for a PKG-014 match) is accepted; do not infer construction details from generic DBM convention. | TBD |
| HRR-014-03-002 | The DBM identifies Remote I/O as a possible control path for building exhaust fan/heater controls but does not specify the PKG-014 exhaust-fan control signal list, wiring assignments, or whether contactor control is local (panel-resident) or remote (via RIO/PLC). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Remote I/O paragraph (line ~804) | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-C715E9AA3E` (I&C / Control Cabling) | Datasheet Attributes/Conditions; Specification Requirements; Procedure Steps | Coordinate construction tie-in with the Remote I/O architecture per DBM but do not specify a fixed signal list or control topology until detailed design and vendor data are accepted. | TBD |
| HRR-014-03-003 | DBM Construction Responsibility scope is facility-wide, not package-specific. Allocation of each listed activity (e.g., home-run cabling, terminations, area lighting installation) to PKG-014 construction execution is by analogy/applicability rather than by an accessible package-specific source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section | `PACKAGE_REGISTER.csv` row `PKG-014` (responsibility model is facility-level) | Specification Requirements REQ-014-03-006; Procedure Steps | Carry facility-level construction activities as applicable to PKG-014 by analogy where they touch the listed interface facts; treat package-specific allocation as `ASSUMPTION` until confirmed by detailed construction execution planning. | TBD |
