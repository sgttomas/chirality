# Guidance — DEL-014-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's authoritative record that the PKG-014 vendor-engineered Contactor Panels (Lighting / Exhaust Fan) Low-Voltage package has been reviewed for facility integration fitness and accepted for handoff. It is the closing-loop evidence between EPC-side basis documents (SOW, Package Datasheet, Construction Work Package) and Vendor-side production (Vendor Engineered Equipment Package, Vendor Document Turnover Package). [Source: DELIVERABLE_REGISTER.csv row DEL-014-06; `_CONTEXT.md`]

## Principles

- **EPC Integrator is the acceptance owner.** Vendor input is sought, but the acceptance decision and evidence belong to the EPC Integrator. [PACKAGE_REGISTER.csv row PKG-014]
- **Acceptance is integration-focused.** The Package Vendor owns package engineering correctness within their scope; the EPC Integrator's acceptance focuses on facility-level integration: interfaces, tie-ins, constructability, and procurement/construction coordination. [PACKAGE_REGISTER.csv row PKG-014]
- **Basis documents must be stable before acceptance.** The acceptance is issued against DEL-014-01 (SOW), DEL-014-02 (Package Datasheet), and DEL-014-03 (Construction Work Package). Acceptance against an unstable basis is meaningless.
- **Evidence over assertion.** Each acceptance line is backed by a vendor document, a test/inspection record, or an interface verification record.

## Considerations

- The PKG-014 interface set (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) defines the integration aspects most likely to require explicit acceptance evidence. [PACKAGE_REGISTER.csv row PKG-014]
- The LV electrical basis is well-defined in source (DBM 3-25 lines 734-735); contactor-panel voltage class verification should be straightforward.
- The exhaust-fan/heater controls integration touches the RIO architecture (Allen-Bradley Flex5000); coordination with the controls discipline is expected. [DBM 3-25 line 804]
- Standby/emergency power for accepted loads relies on LV standby generators at the LV MCC with transfer switch; generator count and rating remain TBD at the project basis level. [DBM 3-25 lines 505, 762]
- The site low-temperature design floor (-40 deg C) is a recurring acceptance check for any exposed vendor enclosures. [DBM 3-25 line 145]
- No deliverable-specific source slices were copied during PREPARATION; package-specific `26020-Package_Requirements.docx` content for PKG-014 was not extracted into a local source slice. Clause-level vendor acceptance criteria therefore remain TBD until that source is sliced or the vendor package itself defines acceptance criteria.

## Trade-offs

- **Acceptance breadth vs. effort.** A heavier checklist gives a stronger record but more reviewer load. The minimum is the four artifacts in `_CONTEXT.md`; a heavier list is acceptable when integration risk is non-trivial. ASSUMPTION: project does not currently mandate a specific checklist depth.
- **Early conditional acceptance vs. fully conditional acceptance at turnover.** Conditional acceptance can unlock construction sequencing but creates open-item carryover; full acceptance at turnover delays construction-readiness but reduces residual risk. The choice is project-management driven; no source mandate.
- **Vendor-supplied test evidence vs. EPC-witnessed test evidence.** Vendor evidence is faster; witnessed tests strengthen acceptance but require schedule coordination.

## Examples

- *Acceptance line for LV electrical class*: "Contactor panel rated 600 V, 3 phase, 3 wire, 60 Hz, HRG-compatible per vendor datasheet rev X, verified against DBM 3-25 LV service basis." [DBM 3-25 line 734]
- *Acceptance line for exhaust-fan control interface*: "Exhaust-fan control interface terminated at nearest RIO node, vendor wiring diagram rev Y, verified against project RIO architecture." [DBM 3-25 line 804]
- *Acceptance line for environmental*: "Vendor enclosure rated to -40 deg C minimum ambient per datasheet rev Z." [DBM 3-25 line 145]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-014-06-001 | Acceptance maturity gate for upstream basis deliverables (DEL-014-01/02/03) is not specified in any accessible source; `_DEPENDENCIES.md` default maturity threshold is `INITIALIZED`, but acceptance evidence may require a higher state (e.g., ISSUED). | `_DEPENDENCIES.md` (default `INITIALIZED`) | No source-level mandate found | Specification REQ-014-06-10; Procedure prerequisites | PROPOSAL: require upstream deliverables at ISSUED before acceptance is issued. | TBD |
| HRR-014-06-002 | Clause-level vendor acceptance criteria are not in any locally accessible source slice for PKG-014 (no package-specific 26020-Package_Requirements.docx slice copied). | `_REFERENCES.md` (notes deferred slices) | DBM 3-25 (project-level only) | Specification REQ-014-06-02 and Standards table; Procedure steps | PROPOSAL: defer clause-level criteria until the package requirements source is sliced or vendor package self-defines acceptance criteria. | TBD |
| HRR-014-06-003 | "Contactor Panels" in the package name refers to electrical contactor switching panels for lighting/exhaust-fan loads. DBM 3-25 uses "contactor" extensively in a process (TEG/sweetening) sense (e.g., line 354 "structured packed contactor"). These are unrelated meanings; the package name's "contactor" is the electrical sense. | Package title; PACKAGE_REGISTER.csv | DBM 3-25 process-contactor sections | Datasheet/Specification terminology | PROPOSAL: confirm "contactor panels" means electrical lighting/exhaust-fan switching panels and document the disambiguation. | TBD |
