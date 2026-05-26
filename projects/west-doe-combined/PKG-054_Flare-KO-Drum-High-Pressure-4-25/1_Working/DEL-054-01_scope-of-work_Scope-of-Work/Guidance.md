# Guidance — DEL-054-01 Scope of Work (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Purpose

This Scope of Work is the EPC Integrator's anchoring statement of *what the package is and how it integrates into the facility*. It is the upstream deliverable that the Package Datasheet, Construction Work Package, vendor production unit, vendor document turnover, and EPC review/acceptance deliverables all consume (per `DELIVERABLE_REGISTER.csv` for `PKG-054`). Getting identity, function, boundary, responsibility, and interface set correct here prevents downstream rework when the vendor receives the technical handoff.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; package note "Mandatory Gate 5 EPC anchor deliverable defined by user instruction".

## Principles

1. **Vendor owns the package; EPC owns the integration.** Package engineering, design, vendor documentation, and equipment supply belong to the Package Vendor. Interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator. This split is the controlling responsibility model for `PKG-054`. Source: `PACKAGE_REGISTER.csv` ResponsibilityModel.
2. **Source-anchored content; no invention.** Every non-trivial statement should cite Workbook Packages row 55, `26020-Package_Requirements.docx` package heading 9, the 04-25 Deepcut DBM, or another locally accessible source slice. Where a value is not in an accessible slice, mark `TBD` with `location TBD` rather than inferring it. Source: SKILL `four-documents` source-grounding rule.
3. **Interface set is exhaustive at the package boundary.** The ten interface types in `INTERFACE_REGISTER.csv` for `PKG-054` form the integration surface. Omitting any of them in the SOW will create a hidden EPC scope item downstream. Source: `INTERFACE_REGISTER.csv`.
4. **Sour-service flare relief context.** SOW-0078 places this drum upstream of the cryogenic flare header tie-in before the common HP/Cryo flare stack. Treat the package as part of the facility-wide flare/blowdown safety system, not as an isolated mechanical skid. Source: `SCOPE_LEDGER.csv` SOW-0078; `OBJ-007`, `OBJ-009`.

## Considerations

- **Tag preservation.** Carry `V-4100-1` and `P-4100-1` exactly as stated in SOW-0077; downstream P&ID, datasheet, and construction documents will key off these tags.
- **EHT + insulation scope ownership.** SOW-0078 declares outdoor HP flare headers are EHT-traced and insulated, but does not specify which interface (Process Piping vs. EHT vs. Electrical Power vs. Insulation) owns the trace circuit, controller, and power feed. Resolve in Datasheet/Construction Work Package; capture as Conflict ID `CONF-054-01-01` below if it remains unresolved at SOW-level.
- **Liquid handling and truck-out.** SOW-0077 names "liquid handling to condensate slop tank" and "truck-out provision". The interface to the condensate slop tank and the truck-out connection are facility-level integration items; the EPC scope should explicitly identify which side of each interface is vendor- vs. EPC-supplied.
- **Budgetary go-by is informational only.** `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` is identified in `PACKAGE_REGISTER.csv` as a budgetary pricing/delivery go-by. Do not promote any value from it into a requirement without explicit human ruling. Source: `PACKAGE_REGISTER.csv` SourceRefRaw.

## Trade-offs

- **Specificity vs. source coverage.** The locally accessible source slices (workbook row, scope ledger, package register) describe identity, function, equipment list, responsibility, and interface set, but do not provide clause-level design conditions. SOW content should be specific where source supports it and explicitly `TBD` (with `location TBD`) elsewhere. Pushing more detail into the SOW than source supports compromises auditability.
- **EPC-authored vs. vendor-authored content.** This SOW is EPC-authored; technical design content belongs in the Package Datasheet (`DEL-054-02`) and the vendor's engineered equipment package (`DEL-054-04`). Resist drift of vendor design content into this deliverable.
- **Interface enumeration vs. interface design.** Naming the ten applicable interfaces in this SOW satisfies the integration narrative requirement; interface *design* belongs in the Package Datasheet and downstream EPC discipline deliverables.

## Examples

Source-grounded statement (good):
> "The package supplies one HP flare knock-out drum (`V-4100-1`) and one HP flare KO drum transfer pump (`P-4100-1`); liquid is routed to the condensate slop tank with a truck-out provision (SOW-0077; `26020-Package_Requirements.docx` heading 9, Major included equipment)."

Insufficiently grounded statement (avoid):
> "The package vessel is designed for 285 psig at 250 F." — there is no locally accessible source slice for this value; mark `TBD` with `location TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-054-01-01 | EHT trace ownership at HP flare header is not delineated between Process Piping, EHT, and Electrical Power interfaces. | `SCOPE_LEDGER.csv` SOW-0078 (states EHT + insulation as fact) | `INTERFACE_REGISTER.csv` PKG-054 (lists EHT and Electrical Power as separate interfaces, no ownership split) | Specification R06; Datasheet "Construction"; Procedure step 3 | PROPOSAL: assign EHT circuit + power feed ownership to EPC Integrator under the Electrical Power + EHT interfaces; piping insulation under Process Piping. | TBD |
| CONF-054-01-02 | Design conditions (P, T, sizing, materials) are not in locally accessible source slices but are required by downstream Package Datasheet. | `_REFERENCES.md` (no copied slices) | `PACKAGE_REGISTER.csv` SourceRefRaw (`26020-Package_Requirements.docx` heading 9 detail text exists in source but not locally extracted) | Datasheet "Conditions" | PROPOSAL: extract design conditions from `26020-Package_Requirements.docx` package heading 9 into deliverable-local source slice before producing `DEL-054-02_package-datasheet`. | TBD |
