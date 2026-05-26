# Specification — DEL-063-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for the DSO storage tank package (`26020-01-PT-19-001`, atmospheric API-650-modified DSO storage tank, 400 bbl nominal). It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-063-04` Vendor Engineered Equipment Package and `DEL-063-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-063-01`), Package Datasheet (`DEL-063-02`), and Construction Work Package (`DEL-063-03`).

Sources: `26020-Package_Requirements.docx` `26020-01-PT-19-001` (Basic Scope; Major Included Equipment); `DELIVERABLE_REGISTER.csv` row `DEL-063-06`.

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-063-04` / `DEL-063-05` outputs.
- Acceptance of other tanks in the source enumeration (`26020-01-PT-19-002` Water; `26020-01-PT-19-003` Caustic; `26020-01-PT-19-004` Condensate; `26020-01-PT-19-005` Sour Water; or 3-25 plant tank packages); those are separate packages.
- Owner-scope "By others" items called out in the source ("Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc.") which are not Package Vendor deliverables.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-063-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| `R-063-06-02` | The vendor document review log MUST enumerate every "Vendor Engineering Deliverable" listed under `26020-01-PT-19-001` and record disposition (accepted / rejected / open). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" |
| `R-063-06-03` | The package acceptance checklist MUST verify scope inclusions: supply of one (1) atmospheric DSO storage tank designed and fabricated to modified API 650, 400 bbl nominal capacity, with heater (vendor-designed, 32.2 °C / 90 °F minimum), internal coating (floor, walls, roof), and insulation to maintain DSO above pour point for truck-out and handling. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Basic Scope" / "Major Included Equipment" |
| `R-063-06-04` | The acceptance evidence MUST confirm tank/process tie-ins to the DSO separator and the caustic regeneration system are reflected in the as-built/turnover P&ID set (`PRO-008`) and piping iso/tie-in list (`PIP-004`, `PIP-008`, `PIP-028`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Basic Scope"; "Vendor Engineering Deliverables" — Process piping interfaces |
| `R-063-06-05` | The acceptance evidence MUST verify storage-tank data sheet (`MEC-011`) and Static Equipment Specifications (`MEC-005`) reflect modified-API-650 design, 400 bbl capacity, 32 oz / 1.0 oz vacuum design pressure, internal coating, insulation, and heater configuration. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Storage tanks |
| `R-063-06-06` | The acceptance evidence MUST cover each physical interface marked `Yes` for `26020-01-PT-19-001`: Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Interfaces marked `No` MUST be confirmed not in scope. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Physical Interface Summary" |
| `R-063-06-07` | The acceptance evidence MUST include pressure-equipment registration evidence where applicable: Pressure Equipment Registration Package (`REG-022`) as listed in the source. Applicability for an atmospheric tank is to be confirmed against jurisdictional rules; ASSUMPTION — may be limited or N/A for atmospheric tanks; status to be ruled by the EPC Integrator. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Static pressure equipment |
| `R-063-06-08` | The acceptance evidence MUST include cathodic protection and grounding evidence: Corrosion Protection Design Basis (`PLN-015`), Cathodic Protection Design Package (`PLN-016`), Grounding / Earthing Study (`ELE-012`), and Earthing / Bonding Layout Drawings (`ELE-019`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Cathodic protection interfaces; Electrical, lighting, EHT, grounding |
| `R-063-06-09` | The acceptance evidence MUST include containment and drainage evidence: Process Sewer / Closed Drain Design Basis (`PRO-023`), Bund / Dike / Secondary Containment Drawings (`CIV-014`), Grading Plan (`CIV-003`), Drainage / Stormwater Management Report (`CIV-004`), and Retention Pond / Containment Basin Design (`CIV-015`) where applicable to this tank's site footprint. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Drainage / containment interfaces; Civil grading / spill containment interfaces |
| `R-063-06-10` | Quality records MUST be assembled: Supplier Quality Plan (`QLT-006`), ITP execution evidence (`QLT-003`), Material Test Reports / Certificates (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Core vendor documents |
| `R-063-06-11` | Turnover MUST include the SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), Mechanical Equipment IOM Manual (`MEC-025`), and Hydrotest / Pressure Test Packages (`PIP-024`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" |
| `R-063-06-12` | Numeric design/operating values used in acceptance (minimum ambient temperature, flow rate, design throughput, insulation minimum temperature, heater duty) MUST be traceable to the Package Vendor's submitted `MEC-011`, `MEC-014`, and related artifacts. Specific numeric values are TBD until those vendor submittals are accepted (source marks these `TBD`/`TBC`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| `R-063-06-13` | Open items called out in the source ("Scope Notes / Open Items") MUST be closed or carried with explicit disposition in the acceptance record. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| `R-063-06-14` | The acceptance evidence MUST confirm "By others" items (foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc.) are handled by other EPC scopes (notably `DEL-063-03` Construction Work Package and discipline production packages) and are not expected from the Package Vendor. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API STD 650 (modified, per source) | Governs design and fabrication of the DSO storage tank vessel. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" — "Design & fabrication to modified API 650" |
| Provincial pressure equipment registration regime (typically ABSA in Alberta) | Applicability for an atmospheric tank is jurisdiction-dependent. Listed via `REG-022` in source enumeration. | location TBD — not stated in `26020-Package_Requirements.docx` `26020-01-PT-19-001`; ASSUMPTION based on listing of `REG-022` |
| API STD 653 (in-service inspection / future maintenance reference) | Likely future-life reference for atmospheric storage tanks; not directly invoked by source. | location TBD — not stated in source; ASSUMPTION (industry typical) |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-063-06-01` | Traceability matrix mapping each SOW item to acceptance-checklist rows and to evidence artifacts. |
| `R-063-06-02` | Document-by-document review log inspection; every source-listed vendor deliverable has a tracked disposition. |
| `R-063-06-03` | Walk-down and as-built/IFC drawing review against the source's Basic Scope and Major Included Equipment list; verification of API-650-modified compliance, capacity, heater, coating, insulation. |
| `R-063-06-04` | P&ID and tie-in list inspection (`PRO-008`, `PIP-004`); construction work package (`DEL-063-03`) cross-check for DSO-separator and caustic-regeneration tie-ins. |
| `R-063-06-05` | Storage Tank Data Sheet (`MEC-011`) and Static Equipment Specifications (`MEC-005`) review against source values; reconciliation table with Package Datasheet (`DEL-063-02`). |
| `R-063-06-06` | Interface-by-interface checklist against the source's Physical Interface Summary. |
| `R-063-06-07` | `REG-022` jurisdictional determination memo; if applicable, registration acceptance evidence; if N/A, recorded basis for exclusion. |
| `R-063-06-08` | Cathodic protection and grounding package review; field tie-in to existing CP system (if any) verified. |
| `R-063-06-09` | Containment/drainage package review; site grading and bund drawings cross-checked against tank footprint. |
| `R-063-06-10` | Quality records audit; Inspection Release Certificate (`QLT-020`) issued; MRB (`QLT-021`) compiled and accepted. |
| `R-063-06-11` | Hydrotest packages (`PIP-024`) signed off; receipt inspection records; SPIR provided and accepted; IOM in turnover bundle. |
| `R-063-06-12` | Reconciliation table between EPC Package Datasheet (`DEL-063-02`) values and vendor-submitted values; TBD/TBC entries flagged with named owners. |
| `R-063-06-13` | Open-items log carried into commissioning; explicit closure or carryover noted. |
| `R-063-06-14` | "By others" scope confirmation memo cross-referencing the Construction Work Package and discipline production packages. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (SOW-, interface-, and artifact-indexed).
- Test / inspection evidence bundle (FAT, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, SPIR, IOM; `REG-022` if applicable).
- Open-items disposition log.

Standards-related applicability calls (notably pressure-equipment registration for an atmospheric tank) and numeric design values that depend on vendor submittals carry `TBD` placeholders until the Package Vendor deliverables are accepted.
