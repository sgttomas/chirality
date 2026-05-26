# Guidance — DEL-052-03 Construction Work Package (Inlet / TEG Dehy Cross Exchanger)

## Purpose

The Construction Work Package (CWP) exists so the EPC Integrator can physically install the vendor-supplied Inlet / TEG Dehy Cross Exchanger (E-5718-1) into the WBS 01 04-25 Deepcut facility, prove all interfaces are correctly tied in, and hand a mechanically complete, sour-service-rated system to commissioning with controlled open-item evidence. The deliverable is a Gate 5 EPC-anchored production unit. Source: `DELIVERABLE_REGISTER.csv` DEL-052-03 (Description, Notes).

## Principles

1. **Vendor designs; EPC integrates and constructs.** The CWP must not redesign the vendor exchanger. It plans, executes, inspects, and documents the integration and installation of a vendor-engineered package. Source: `PACKAGE_REGISTER.csv` PKG-052 ResponsibilityModel; `OBJECTIVE_REGISTER.csv` OBJ-004.
2. **Interface fidelity over interface convenience.** Every applicable interface in `INTERFACE_REGISTER.csv` for PKG-052 (9 rows) must appear as a planned tie-in with a turnover record, even when the tie-in is small. Source: `INTERFACE_REGISTER.csv` PKG-052.
3. **Source-grounded, not narrative-grounded.** Construction decisions trace to authoritative basis (DBM-Deepcut sections, vendor RFQ/package documents in DEL-052-04 and DEL-052-05, package datasheet in DEL-052-02). Decomposition narrative is routing — not authority. ASSUMPTION elevated from skill authority hierarchy.
4. **Sour-service rigor is mandatory.** The exchanger handles cold sour gas (SOW-0104). Materials traceability (PMI), weld hardness control, hydrotest discipline, and code-stamp verification are not optional and must be visible in the turnover package. Source: `SCOPE_LEDGER.csv` SOW-0104; `OBJECTIVE_REGISTER.csv` OBJ-009.
5. **Closeout discipline.** Open items at mechanical completion are tracked and explicitly dispositioned, not deferred silently. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.

## Considerations

- **"By others" coordination is the headline risk.** SOW-0106 explicitly defers interconnecting piping, DCS integration, foundations, and electrical supply to MCC to other parties. The CWP's value is largely in coordinating those handoffs cleanly; mis-aligned readiness of any of the four will block setting, tie-in, loop-check, or energization respectively. Source: `SCOPE_LEDGER.csv` SOW-0106.
- **Sequencing with foundations and supports** (PKG-052 carries Structural/Foundations/Supports interface IFC-A40EC04E30 and Maintenance Access IFC-0D3B12DEF3) — civil work must precede equipment setting; foundation acceptance record is a hard prerequisite. Source: `INTERFACE_REGISTER.csv`; `SCOPE_LEDGER.csv` SOW-0106 (foundations by others).
- **Sour-side vs. sweet-side tie-in distinction.** The exchanger has two process services: cold sour gas (inlet separator → exchanger → inlet compressors) and sweet gas (amine unit outlet → exchanger). The CWP should treat the two services as separate workface units for hydrotest, material control, and turnover. Source: `SCOPE_LEDGER.csv` SOW-0104.
- **Winterization / heat tracing (EHT)** — ambient design temperatures are -40 °C min / +35 °C max (SOW-0106). EHT interface (IFC-C3CE1B5E7D) is applicable; plan EHT installation, commissioning, and turnover, especially on dead-legs, instrument tubing, and any liquids-bearing lines. Source: `SCOPE_LEDGER.csv` SOW-0106; `INTERFACE_REGISTER.csv` PKG-052.
- **Pressure-equipment scope.** Design pressure 9756 kPag (1415 psig), design temperature 66 °C, TEMA 'R' BEM. The exchanger is provincially registered pressure equipment; coordinate registration/inspection with jurisdictional authority. Specific authority and registration path: TBD (location TBD). Source: `SCOPE_LEDGER.csv` SOW-0105, SOW-0106.
- **Relief / Flare / Vent absence in interface register.** `INTERFACE_REGISTER.csv` does not list a Relief/Flare/Vent row for PKG-052. PSV protection of the exchanger is presumed handled at adjacent equipment per typical exchanger practice; this assumption must be confirmed against P&IDs before construction lock-in. ASSUMPTION; see Conflict Table CFT-001.
- **Electrical Power absence in interface register.** The exchanger has no driver (SOW-0106). The PKG-052 interface register intentionally omits the generic Electrical Power row and carries only EHT, grounding/bonding, and area-lighting electrical interfaces. Confirm this is intentional (i.e., no instrument-power discrete row) before tie-in planning. ASSUMPTION; see Conflict Table CFT-002.
- **Fire & Gas absence in interface register.** No discrete F&G interface row for PKG-052. Area-wide F&G coverage is assumed to come from the facility F&G package; verify exchanger area is within an existing detector coverage envelope. ASSUMPTION; see Conflict Table CFT-002.
- **Vendor-document availability** drives construction readiness. The CWP cannot finalize before DEL-052-05 supplies the required vendor documentation (installation manuals, certified drawings, U-1 / MDR, recommended inspection plans). ASSUMPTION based on OBJ-010 closure conditions.

## Trade-offs

- **Pre-fab vs. stick-build of tie-in piping (sour and sweet sides):** pre-fab improves quality and schedule but locks in dimensions before field reality is known. Pre-fab is generally preferred for sour-service piping because shop-controlled welding improves PMI and hardness compliance — but trade-off rationale beyond this general principle: TBD (source not deliverable-local).
- **Vendor-attended installation vs. EPC-only crew:** vendor presence reduces installation risk and warranty exposure but costs more. Trade-off rationale: TBD.
- **Hydrotest vs. pneumatic / inert-gas tightness test:** hydrotest is the default per pressure-equipment codes; inert-gas testing of sour-service systems carries known release-energy risk. Specific code reference and project-test-plan rationale: TBD (location TBD — pressure-test code reference not deliverable-local).
- **Insulation system selection (cold-service vs. hot-service segments):** sour-side outlet is 28 °C, sweet-side outlet is 16 °C, both close to ambient; cold-service insulation may be unnecessary for the bulk of operating range but freeze/winterization needs may drive EHT + warm insulation locally. Detailed trade-off: TBD.

## Examples

- TBD — example construction work packages from prior Deepcut or 26020 projects not present in deliverable-local references.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-001 | No Relief/Flare/Vent interface row exists for PKG-052; sour-gas equipment normally requires PSV/vent provisions visible in the construction interface set. | `INTERFACE_REGISTER.csv` PKG-052 (no Relief/Flare/Vent row) | General sour-service practice and `OBJECTIVE_REGISTER.csv` OBJ-009 (preserve relief/flare/vent into package scope) | Specification §R-SAF-2; Guidance §Considerations | PROPOSAL: PSV protection is provided at adjacent equipment (inlet separator and/or downstream compressor suction) per typical exchanger practice; PKG-052 carries no discrete relief interface. To be confirmed against P&IDs before tie-in lock-in. | TBD |
| CFT-002 | PKG-052 interface register omits "Electrical Power", "Fire & Gas / Safety Systems", "Relief / Flare / Vent", and "Building HVAC / Services" rows that sibling packages typically carry. | `INTERFACE_REGISTER.csv` PKG-052 (9 rows only) | Sibling packages (e.g., PKG-077 carries 13 interfaces including these types) | Datasheet §Attributes; Specification §R-INT-1, §R-ELE-3, §R-INS-3 | PROPOSAL: omissions are intentional because the exchanger is unfired, has no driver, is a passive heat-exchange device, and likely sits in an open process area. Carry as ASSUMPTION until DEL-052-01/DEL-052-02 confirms. | TBD |
| CFT-003 | SOW-0106 records sour-gas treated-side flow as "4480.28 m6/hr"; "m6/hr" is not a standard volumetric unit. | `SCOPE_LEDGER.csv` SOW-0106 (verbatim transcription) | Engineering convention (expected unit m³/hr) | Datasheet §Conditions | PROPOSAL: treat as transcription artifact and read as m³/hr; confirm against vendor RFQ source 26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx before any flow-dependent construction decision. | TBD |
| CFT-004 | Objective mapping for DEL-052-03 lists 9 objectives via the package-heuristic association; mapping basis is ASSUMPTION rather than explicit deliverable-level mapping. | `DELIVERABLE_REGISTER.csv` DEL-052-03 (RelatedObjectiveIDs) | Skill authority hierarchy (PACKAGE_HEURISTIC = ASSUMPTION) | Datasheet §Identification (Supports Objectives); Specification §R-RESP through §R-CMN | PROPOSAL: retain objective set as directional context (ASSUMPTION) until `OBJECTIVE_DELIVERABLE_MAP.csv` resolves at deliverable-ID level. | TBD |
