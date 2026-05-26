# Guidance — DEL-077-03 Construction Work Package (Methanol Injection)

## Purpose

The Construction Work Package (CWP) exists so the EPC Integrator can physically install a vendor-supplied Methanol Injection package into the WBS 01 facility, prove that all interfaces are correctly tied in, and hand a mechanically complete system to commissioning with controlled open-item evidence. The deliverable is a Gate 5 EPC-anchored production unit. Source: `DELIVERABLE_REGISTER.csv` DEL-077-03 (Description, Notes).

## Principles

1. **Vendor designs; EPC integrates and constructs.** The CWP must not redesign the vendor package. It plans, executes, inspects, and documents the integration and installation of a vendor-engineered package. Source: `PACKAGE_REGISTER.csv` PKG-077 ResponsibilityModel; `OBJECTIVE_REGISTER.csv` OBJ-004.
2. **Interface fidelity over interface convenience.** Every applicable interface in `INTERFACE_REGISTER.csv` for PKG-077 must appear as a planned tie-in with a turnover record, even if the interface is small. Source: `INTERFACE_REGISTER.csv` PKG-077.
3. **Source-grounded, not narrative-grounded.** Construction decisions should trace to authoritative basis (DBM-Deepcut sections, vendor package documents in DEL-077-04 and DEL-077-05, package datasheet in DEL-077-02). Decomposition narrative is routing — not authority. ASSUMPTION elevated from skill authority hierarchy.
4. **Sour-service caution.** Treat the system as sour-service-adjacent until DEL-077-01 / DEL-077-02 confirm otherwise; carry sour-service inspection rigor (materials traceability, pressure-test plans, F&G coverage) into construction. ASSUMPTION: based on OBJ-009 scope and Deepcut WBS 01 placement.
5. **Closeout discipline.** Open items at mechanical completion are tracked and explicitly dispositioned, not deferred silently. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.

## Considerations

- **Vendor-document availability** drives construction readiness. The CWP cannot finalize before DEL-077-05 supplies the required vendor documentation (installation manuals, certified drawings, recommended inspection plans). ASSUMPTION based on OBJ-010 closure conditions.
- **Sequencing with foundations and supports** (PKG-077 carries Structural/Foundations/Supports interface; see IFC-A96044F713) — civil work must precede equipment setting; coordinate with site-wide grading and containment packages. Source: `INTERFACE_REGISTER.csv`.
- **Electrical / I&C readiness** — power (IFC-4269247DFA), EHT (IFC-897BE87E57), grounding (IFC-4848032D8D), control cabling (IFC-1E031D5EF9), and F&G (IFC-2176B4EB34) tie-ins require corresponding facility-side packages to be construction-ready. Coordination owner: EPC Integrator. Source: `INTERFACE_REGISTER.csv`.
- **Hazardous area** — methanol service is flammable. Area classification, ignition control during construction, and hot-work permitting deserve explicit attention. Specific classification: TBD (location TBD).
- **Winterization, heat tracing (EHT), insulation** — methanol freezing point is well below ambient, but methanol-water mixtures and dead-leg considerations may still drive EHT requirements; EHT interface (IFC-897BE87E57) is marked applicable, so plan EHT installation, commissioning, and turnover. Source: `INTERFACE_REGISTER.csv`; engineering rationale ASSUMPTION.
- **Gate 6 disposition note** — `PACKAGE_REGISTER.csv` PKG-077 SourceRef contains: "Methanol Injection scope is included with the Cryogenic Unit package scope." This may indicate scope absorption into another package. The CWP should not silently double-count work. NEEDS_HUMAN_RULING: whether PKG-077 remains a standalone construction work package or is rolled into the Cryogenic Unit CWP.

## Trade-offs

- **Pre-fab vs. stick-build of tie-in piping:** pre-fab improves quality and schedule but locks in dimensions before field reality is known. Trade-off rationale: TBD (source not deliverable-local).
- **Vendor-attended installation vs. EPC-only crew:** vendor presence reduces installation risk and warranty exposure but costs more. Trade-off rationale: TBD.
- **Hydrostatic vs. pneumatic tightness test for methanol piping:** rationale and code reference TBD (location TBD — pressure-test code reference not deliverable-local).

## Examples

- TBD — example construction work packages from prior Deepcut projects not present in deliverable-local references.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-001 | PKG-077 may be carried as a distinct package OR absorbed into the Cryogenic Unit package (Gate 6 disposition). | `SCOPE_LEDGER.csv` SOW-0143 (carries PKG-077 as distinct flat package) | `PACKAGE_REGISTER.csv` PKG-077 SourceRef ("Methanol Injection scope is included with the Cryogenic Unit package scope") | Datasheet §Identification; Specification §Scope; Guidance §Considerations | PROPOSAL: SCOPE_LEDGER (distinct package) is the structural authority for register hygiene; Gate 6 disposition is a re-scoping signal that must be ruled by the human before construction execution. | TBD |
| CFT-002 | Objective mapping for DEL-077-03 lists 8 objectives; mapping basis is package-heuristic ASSUMPTION rather than explicit deliverable-level mapping. | `DELIVERABLE_REGISTER.csv` DEL-077-03 (RelatedObjectiveIDs) | Skill authority hierarchy (PACKAGE_HEURISTIC = ASSUMPTION) | Datasheet §Identification (Supports Objectives); Specification §R-RESP through §R-CMN | PROPOSAL: retain objective set as directional context (ASSUMPTION) until OBJECTIVE_DELIVERABLE_MAP.csv resolves at deliverable-ID level. | TBD |
