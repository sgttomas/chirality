# Specification — DEL-096-01 Scope of Work (PKG-096 Tanks, Sour Condendate (API 650))

## Scope

### In Scope

This EPC Scope of Work defines, for PKG-096 (Tanks, Sour Condendate (API 650)):

- Identity of the tagged equipment and the package's function within the 3-25 West Doe Liquids Hub tank farm.
- Package boundaries, source basis, and the whole-facility integration narrative for two (2) 3800 bbl Sour Inlet Condensate Storage Tanks (TK-9110-2, TK-9120-2).
- Responsibility assignment between the EPC Integrator and the Package Vendor.
- Interface applicability matrix linking the package to facility utility, safety, civil, and instrumentation systems.

Source: `_CONTEXT.md` Scope; SOW-0217..SOW-0220.

### Out of Scope (By Others, per source)

- Foundations; mounting tanks at site; electrical/instrumentation work; platforms; staircases — declared as "By others" in the package source (SOW-0220) and therefore owned by the EPC Integrator and/or facility disciplines rather than the Package Vendor.
- Package vendor engineering deliverables (datasheets, calculations, drawings, vendor data book) are tracked by DEL-096-02 (Package Datasheet), DEL-096-04 (Vendor Engineered Equipment Package), and DEL-096-05 (Vendor Document Turnover) — not this deliverable.
- DCS integration with the tank package is a facility-integration scope (EPC Integrator) — ASSUMPTION from analogous package text (PKG-019 Tank Farm Pumps "Scope Notes / Open Items"); the Sour Condensate tank package text itself does not state DCS integration explicitly.

## Requirements

### REQ-1 — Package identity

The Scope of Work SHALL identify PKG-096 by its workbook identity and tagged equipment.

- Source: SOW-0217; SOW-0218; `_CONTEXT.md`.
- Workbook identity: row 92, "Tanks, Sour Condendate (API 650)".
- Tagged equipment: TK-9110-2 and TK-9120-2, each 3800 bbl Sour Inlet Condensate Storage Tank.

### REQ-2 — Package function and source basis

The Scope of Work SHALL state the package function as "Sour C5+ Condensate Storage Tanks" and cite the source basis.

- Source: SOW-0218.
- Source basis (cited by package text): `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` (location TBD — RFQ document not locally accessible).

### REQ-3 — Code, service, and protective design constraints

The package SHALL be designed and fabricated to Modified API 650, with non-insulated construction, a blanket gas system per API 2000, NACE compliance for sour (H2S) service, and Devchem 253 internal coating on floors, walls, and roofs.

- Source: SOW-0219; package text "Major Included Equipment".

### REQ-4 — Pressure, vacuum, emergency, and vapour-recovery provisions

Each tank SHALL include a PVRV (vacuum or modulating pressure relief), an EPRV (emergency relief), and a VRU header connection.

- Source: SOW-0219.

### REQ-5 — Fill protection

Tanks SHALL be configured with a Maximum fill 90% shutdown, and nozzles SHALL be sized so plant design capacity can fill a single tank.

- Source: SOW-0219.

### REQ-6 — Design conditions

The Scope of Work SHALL carry the design pressure (32 oz test pressure), design temperature range (-40 °C / 60 °C), and Item No. 1 design flow (27,606 kg/h / 919 Am3/d) into downstream package deliverables.

- Source: SOW-0220.
- Item No. 2 design values appearing in SOW-0220 are noted as a CONFLICT (see `Guidance.md`).

### REQ-7 — Interface applicability matrix

The Scope of Work SHALL declare the applicability of facility interfaces as listed in the package "Physical Interface Summary". Interface applicability is reproduced in `Datasheet.md` and SHALL govern downstream interface coordination.

- Source: `26020-Package_Requirements.docx` package heading 48, Physical Interface Summary.

### REQ-8 — Responsibility allocation

The Scope of Work SHALL split responsibility:

- Package Vendor: engineering, design, fabrication, and supply of the tank package (per OBJ-004).
- EPC Integrator: facility integration, package boundary definition, and the "By others" scope items (foundations, mounting, electrical/instrumentation, platforms, staircases) per SOW-0220.

- Source: SOW-0217; SOW-0220; OBJ-004.

### REQ-9 — Boundary preservation across companion deliverables

The Scope of Work SHALL be consistent with DEL-096-02 (Package Datasheet), DEL-096-03 (Construction Work Package), DEL-096-04 (Vendor Engineered Equipment Package), DEL-096-05 (Vendor Document Turnover Package), and DEL-096-06 (EPC Vendor Package Review and Acceptance).

- Source: SCOPE_LEDGER.csv rows SOW-0217..SOW-0220 — `Linked Deliverables`.

### REQ-10 — Sour-service/safety, environmental, and code compliance integration

Sour-service safety, relief/flare/vent, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory requirements identified for the package SHALL be carried into downstream package scopes and interfaces.

- Source: OBJ-009; package Interface Summary (Relief/Flare/Vent: Yes; Drain/Containment: Yes; Grading/Site Drainage/Spill Containment: Yes).

## Standards

| Standard | Use | Location (in source) |
|---|---|---|
| API 650 (modified) | Tank design and fabrication | SOW-0219 / Major Included Equipment — location TBD (clause-level text not locally accessible) |
| API 2000 | Tank pressure/vacuum venting (blanket gas system) | SOW-0219 / Major Included Equipment — location TBD |
| NACE (sour-service) | Material compliance for H2S service | SOW-0219 / Major Included Equipment — location TBD (specific NACE document, e.g., MR0175, not stated in source slice — ASSUMPTION) |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-1 | Inspection: identity table in `Datasheet.md` matches workbook row 92 and `_CONTEXT.md`. |
| REQ-2 | Inspection: SoW narrative states package function verbatim from SOW-0218. |
| REQ-3 | Inspection of downstream Package Datasheet (DEL-096-02) and Vendor Engineered Equipment Package (DEL-096-04) for code/service/coating callouts. |
| REQ-4 | Inspection of vendor data sheets (DEL-096-04) for PVRV, EPRV, and VRU header nozzles. |
| REQ-5 | Inspection of instrumentation/SIS package and tank datasheet for 90% fill shutdown and nozzle sizing basis. |
| REQ-6 | Inspection of Package Datasheet (DEL-096-02) carrying design pressure/temperature/flow values; CONFLICT resolution recorded in `Guidance.md`. |
| REQ-7 | Inspection of interface register entries against the Physical Interface Summary in `Datasheet.md`. |
| REQ-8 | Inspection of responsibility statements across DEL-096-01..DEL-096-06 for vendor/EPC consistency. |
| REQ-9 | Cross-reference: `Datasheet.md` and `Specification.md` referenced by companion deliverables. |
| REQ-10 | Trace from this SoW to the relevant safety/regulatory interface artifacts (TBD — produced by other packages). |

## Documentation

Required artifacts associated with this deliverable (per `_CONTEXT.md` Anticipated Artifacts):

- Package Scope of Work narrative (this deliverable).
- Tagged equipment and package identity list (in `Datasheet.md`).
- Package function and integration narrative (in `Guidance.md`).
- Responsibility assignment record (in `Datasheet.md` and `Specification.md` REQ-8).

Companion deliverable documentation produced elsewhere:

- DEL-096-02 Package Datasheet.
- DEL-096-03 Construction Work Package.
- DEL-096-04 Vendor Engineered Equipment Package.
- DEL-096-05 Vendor Document Turnover Package.
- DEL-096-06 EPC Vendor Package Review and Acceptance.
