# Guidance: DEL-090-06 — EPC Vendor Package Review and Acceptance

> Directional guidance for executing the EPC Integrator's review and acceptance of the PKG-090 VRU 3-25 vendor package. Rationale is grounded in accessible Gate 7 source slices; where rationale is derived from generic engineering judgement, it is labelled `ASSUMPTION`.

## Purpose

Provide the rationale and decision considerations the EPC Integrator uses when reviewing, commenting on, and accepting the Package Vendor's engineered equipment package and turnover documentation for VRU 3-25. The deliverable's outputs (review log, acceptance checklist, test evidence) are the evidence base for objectives OBJ-002 through OBJ-010 (per `OBJECTIVE_DELIVERABLE_MAP.csv`, package-heuristic association).

## Principles

1. **EPC owns integration; Vendor owns the package.** The Package Vendor is responsible for compressor train engineering, design, and equipment; the EPC Integrator is responsible for facility integration acceptance. Source: SOW-0249.
2. **Source-of-truth hierarchy.** EPC review compares vendor submittals against (a) the EPC Scope of Work (DEL-090-01), (b) the EPC Package Datasheet (DEL-090-02), and (c) the EPC Construction Work Package (DEL-090-03). Source: `_CONTEXT.md` Scope.
3. **Acceptance is evidence-driven.** Every accepted item must have a documented basis (review log entry, test record, or checklist line). Source: ART-08602095B0 / ART-2BE816FC33 / ART-63586A61E0 descriptions.
4. **No silent reconciliation.** When vendor documents disagree with the EPC datasheet/SOW/CWP, the disagreement is logged for human ruling; the EPC Integrator does not unilaterally relax a requirement. ASSUMPTION (good-practice principle; not literal in accessible source slices).

## Considerations

- **Sour-service integrity.** With 0.4588 mol% H2S and 0.4314 mol% CO2, NACE compliance is a hard gate for materials, weld procedures, and inspection; missing NACE evidence is a blocker rather than a comment. Source: SOW-0251.
- **Seal system safety.** Plan 53 dual mechanical seal with fuel-gas barrier and primary vent to LP flare implies a tightly coupled seal/utility/flare interface; review should verify alarm setpoints, flare back-pressure, and barrier-gas supply continuity. Source: SOW-0251. Specific setpoints: `TBD`.
- **Capacity and operating margin.** Design capacity (1 MMSCFD) versus expected flow per unit (0.510 MMSCFD) leaves design margin; reviewer should confirm vendor sizing maps to operating points (1st-stage intercooler 48.9 °C, 2nd-stage aftercooler 60.0 °C, dewpoints 45.6 °C / 53.2 °C). Source: SOW-0252.
- **VFD readiness.** All compressor and cooler motors are VFD-ready at 600 V; vendor electrical/VFD interface documents should be reviewed against the facility's 600 V distribution design from DEL-090-03 / DEL-090-02. Source: SOW-0251; SOW-0252.
- **Lead-lag operability.** Two 100% trains in lead-lag housed in one building is the vendor configuration; control philosophy (lead selection, auto-changeover, common alarms) is a review focus. Source: SOW-0250. Detailed control philosophy: `TBD`.
- **"By others" coordination.** Shipping to site, piling/installation, tie-in piping, electrical connections, mounting platform and stairs are EPC-Integrator scope; acceptance cannot precede readiness of these interfaces. Source: SOW-0252.

## Trade-offs

- **Comment vs. reject.** Documents with sufficient information but minor non-conformance are typically accepted-with-comment to preserve schedule, while safety/NACE/seal/relief items are typically rejected pending resolution. ASSUMPTION (industry-standard EPC review practice; not literal in accessible source slices).
- **Witnessed vs. reviewed tests.** Where factory/shop tests have safety or schedule criticality (e.g., compressor mechanical run, motor PI tests), witnessing is preferred; lower-risk tests may be accepted on certified records. ASSUMPTION.
- **Early conditional acceptance vs. full acceptance.** Conditional acceptance can unlock downstream construction work but requires explicit residual-item tracking in ART-2BE816FC33. ASSUMPTION.

## Examples

Examples drawn only from accessible source slices:

- A vendor compressor datasheet citing dual mechanical seal but omitting the fuel-gas barrier source would be logged as a finding against SOW-0251 (seal plan), not accepted.
- A vendor motor datasheet that is not explicitly VFD-rated would be logged as a finding against SOW-0251 / SOW-0252.
- A vendor capacity curve that does not envelope the 0.510 MMSCFD expected flow at the stated operating temperatures would be logged as a finding against SOW-0252.

Further worked examples require access to `26020-Package_Requirements.docx package heading 43` source text and are `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-090-06-001 | Objective mapping at the deliverable-ID level was derived via PACKAGE_HEURISTIC (PKG-090 row in `OBJECTIVE_DELIVERABLE_MAP.csv` lists OBJ-002..OBJ-010), but the explicit deliverable-objective row count for DEL-090-06 was not separately confirmed. | `_CONTEXT.md` "Supports Objectives" list | `OBJECTIVE_DELIVERABLE_MAP.csv` rows mentioning DEL-090-06 | Datasheet > Identification; Guidance > Purpose | Treat as best-effort (ASSUMPTION) until human confirms the deliverable-level objective set. | TBD |
| C-090-06-002 | NACE edition and specific document not stated in accessible source slice. | SOW-0251 "NACE designation applies" | (no second source accessible) | Specification > Standards; Specification > REQ-090-06-004 | Defer NACE edition to Vendor Engineered Equipment Package documentation (DEL-090-04). | TBD |
| C-090-06-003 | API seal-plan edition not stated; SOW-0251 refers to "Plan 53 type" only. | SOW-0251 | (no second source accessible) | Specification > Standards; REQ-090-06-005 | Defer to vendor seal-system documentation; record edition in review log when received. | TBD |
| C-090-06-004 | Acceptance prerequisite (REQ-090-06-012) requiring DEL-090-05 closure and DEL-090-03 readiness is lifecycle-inferred. | (none) | (none) | Specification > REQ-090-06-012 | Adopt as ASSUMPTION until confirmed by package execution plan. | TBD |
