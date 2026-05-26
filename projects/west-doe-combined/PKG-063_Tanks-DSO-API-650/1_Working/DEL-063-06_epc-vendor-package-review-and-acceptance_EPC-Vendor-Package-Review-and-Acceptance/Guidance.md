# Guidance — DEL-063-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's binding evidence that the Package Vendor's engineered package and turnover documentation for the DSO storage tank (`26020-01-PT-19-001`, atmospheric API-650-modified, 400 bbl nominal) satisfy the EPC anchor deliverables — Scope of Work (`DEL-063-01`), Package Datasheet (`DEL-063-02`), and Construction Work Package (`DEL-063-03`) — and are ready for integration into the 4-25 future LPG mercaptan treating unit's caustic regeneration system.

Source: `26020-Package_Requirements.docx` `26020-01-PT-19-001` ("Location / Status", "Basic Scope"); `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

## Principles

- **Acceptance is integrator-led, not vendor-self-certified.** `_CONTEXT.md` and the decomposition register assign EPC Integrator as the lead responsible party with Package Vendor input. No agent may certify; binding acceptance is human-authored (`K-AUTH-1`).
- **Evidence is anchored to the source's enumerated artifacts.** The source's "Vendor Engineering Deliverables" list for `26020-01-PT-19-001` is the canonical artifact set. Acceptance does not invent new artifact requirements; it confirms presence and adequacy of those artifacts.
- **Interface evidence follows the Physical Interface Summary.** Only interfaces marked `Yes` for `26020-01-PT-19-001` are in scope; `No`-marked interfaces should be explicitly recorded as out-of-scope rather than silently omitted.
- **Numeric design values come from vendor submittals.** Until the vendor's `MEC-011`, `MEC-014`, etc., are accepted, numeric values flagged `TBD`/`TBC` in source remain `TBD` in this evidence pack rather than being asserted from decomposition prose. (ASSUMPTION — typical EPC practice; aligns with source enumeration.)
- **"By others" boundary is preserved.** Source enumerates owner/EPC-scope items (foundations, mounting, electrical/instrumentation tie-ins, platforms, staircase) that are not Package Vendor deliverables. Acceptance must not demand them from the vendor.

## Considerations

- **API 650 — modified.** Source explicitly calls for "Design & fabrication to modified API 650". The acceptance pack must verify that the vendor's calculation package (`MEC-014`) and Storage Tank Data Sheet (`MEC-011`) identify which API 650 modifications apply and that the EPC Integrator has accepted the modifications.
- **Internal coating and insulation.** Source requires internal coating of floor, walls, and roof, and insulation sufficient to maintain DSO above pour point for truck-out and handling. Acceptance must confirm coating system specification, surface preparation, DFT records, and insulation thickness / heat-trace coordination — even though EHT is marked `No` for this package (heat is provided by the integral heater, not by EHT). (ASSUMPTION — EHT-No in interface summary reflects no external pipe heat trace; the integral heater is in scope.)
- **Heater design.** Vendor designs the heater; minimum 32.2 °C (90 °F) per source. Acceptance must verify heater design basis, duty calculation, and electrical power source coordination (electrical "by others" per source — clarify supply boundary).
- **Pressure-equipment registration applicability.** Source lists `REG-022` under "Static pressure equipment". For an atmospheric tank with 32 oz / 1.0 oz vacuum design pressure, jurisdictional registration may or may not apply. Acceptance must reach an explicit ruling (registered or excluded with basis) rather than carry the item indefinitely.
- **Cathodic protection.** Interface "Cathodic Protection" is marked `Yes`. Acceptance must trace `PLN-015` / `PLN-016` and confirm coordination with site-wide CP system (if any) and with the internal coating system (to avoid double-protection conflicts).
- **Spill containment.** Interface "Grading / Site Drainage / Spill Containment" is `Yes`. Acceptance must confirm bund/dike sizing per applicable rules and coordination with `CIV-014` / `CIV-015`.
- **Truck-out provision.** Source notes insulation is needed "to maintain DSO above pour point for truck-out and handling". Acceptance must confirm a truck-out connection, heating retention during loading, and access (even though "Maintenance Access" and "Product Loading" are marked `No` in the interface summary — ASSUMPTION that truck-out is handled as part of process piping rather than as a separate Product Loading interface; record as a conflict candidate if vendor scope disagrees).

## Trade-offs

- **Depth of vendor re-engineering review vs. timeline.** EPC Integrator review must be deep enough to find configuration mismatches against `DEL-063-02` but cannot substitute for vendor engineering. Default disposition for purely vendor-engineering details with consistent source-grounded inputs is "accepted on evidence" rather than re-derivation.
- **Open-items closure vs. carryover.** Items the source flags `TBD` / `TBC` (capacity/design throughput; minimum ambient temperature; flow rate; insulation minimum temperature) should either be closed via vendor submittal or carried with a named owner. Leaving them silent breaks traceability into commissioning.
- **Single acceptance bundle vs. staged acceptance.** A staged approach (engineering acceptance → fabrication acceptance → turnover acceptance) aligns with the artifact maturity progression in source enumeration. (ASSUMPTION — staging not mandated in source.)
- **Coating QA depth.** Internal coating of a fluid-product tank is a high-failure-cost item. Trading off coating inspection depth against schedule should be ruled explicitly by EPC Integrator quality leadership rather than left to default vendor QA.

## Examples

The source's "Vendor Engineering Deliverables" enumeration for `26020-01-PT-19-001` groups vendor artifacts by function: Core vendor documents; Core package engineering; Storage tanks; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Cathodic protection interfaces; Instrumentation and controls interfaces; Structural, foundations, supports, access; Civil grading / spill containment interfaces. The acceptance checklist should mirror this grouping so reviewers can audit one functional area at a time.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| `C-063-06-01` | Source interface summary marks "Product Loading" and "Maintenance Access" as `No`, but source narrative calls for "truck-out and handling" of DSO above pour point — implying a product-loading interface in practice. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Physical Interface Summary" rows "Product Loading", "Maintenance Access" | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" — insulation "for truck-out and handling" | Datasheet Conditions; Specification `R-063-06-03`, `R-063-06-06`; Guidance Considerations (truck-out) | PROPOSAL: Treat truck-out connection as part of Process Piping interface and explicit acceptance test, but raise to human for confirmation. | TBD |
| `C-063-06-02` | Source enumeration lists `REG-022` Pressure Equipment Registration Package under "Static pressure equipment" for an atmospheric tank where registration may not be jurisdictionally required. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Static pressure equipment | Project-wide registration policy (location TBD) | Specification `R-063-06-07`; Guidance Considerations (registration applicability) | PROPOSAL: EPC Integrator issues a registration-applicability memo; if N/A, formally exclude `REG-022` for this package. | TBD |
