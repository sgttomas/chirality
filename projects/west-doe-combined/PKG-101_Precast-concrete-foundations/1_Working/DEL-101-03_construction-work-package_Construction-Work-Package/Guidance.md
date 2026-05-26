# Guidance — DEL-101-03 Construction Work Package (PKG-101 Precast Concrete Foundations)

## Purpose

Provide directional guidance to the EPC Integrator's team authoring the Construction Work Package (CWP) for PKG-101 precast concrete foundations. The CWP is one of three mandatory EPC anchor deliverables for the package (alongside DEL-101-01 Scope of Work and DEL-101-02 Package Datasheet) and is the construction-side counterpart to the engineering handoff embodied by the datasheet (`_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-101-03).

## Principles

- **Construction follows accepted engineering.** Foundation installation criteria, anchor schedules, and concrete mix designs are not set by the CWP; they are received from issued engineering and the accepted geotechnical report (DBM-Comp_and_Liquids line 141; DBM-Deepcut SEC-11 §External Dependencies). The CWP routes and sequences work; it does not establish design values.
- **Default support basis is driven steel piles.** Treat precast concrete elements as the exception, not the rule: transformers on precast concrete bearing foundations and compressors on precast concrete blocks supported on driven steel piles are the only named precast-concrete elements in the locally accessible sources (DBM-Deepcut SEC-11 §Piles and Foundations).
- **Workbook-declared interfaces are scope anchors.** PKG-101 declares YES on two workbook interfaces — Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports — and the workface plan must address both (INTERFACE_REGISTER.csv lines 905-906).
- **Site basis governs construction methods.** A -40 deg C design minimum ambient is the construction reality for exposed work; concrete placement, curing, and material handling shall be planned accordingly (DBM-Comp_and_Liquids line 145).
- **TBDs are surfaced, not invented.** Per-tag installation sequences, lift weights, embed schedules, and ITP acceptance criteria are not in the current sources for PKG-101; surface them as TBD rather than fabricating values.

## Considerations

- **Compressor dynamic-analysis dependency.** Where compressor packages are supported on precast concrete blocks on driven steel piles, the dynamic analysis is an explicit open requirement (DBM-Deepcut SEC-11 §Piles and Foundations; §Assumptions). The CWP should treat installation release for compressor foundations as a hold-point until that analysis is accepted.
- **Skid-to-pile alternate.** Propak's evaluation of welding the compressor steel skid directly to piles (eliminating concrete) is recorded as TBD and considered unlikely for this compressor size (DBM-Deepcut SEC-11 §Piles and Foundations; §External Dependencies). The CWP should not commit to the precast-block path in a way that precludes adopting this alternate if engineering closes the other way.
- **Oil-leak containment at compressor foundations.** Containment and management of on-skid oil leaks is a stated foundation/skid design consideration (DBM-Deepcut SEC-11 §Piles and Foundations) and should be reflected in inspection acceptance criteria for the foundation arrangement.
- **Geotechnical gate.** Multiple parameters (bearing capacity, lateral pile design, LPILE curves, pavement design) depend on the geotechnical report (DBM-Deepcut SEC-11 §External Dependencies). The CWP should organize hold-points around acceptance of that report rather than guess values.
- **Tie-in coordination with PKG-101 interface owners.** The two workbook interfaces are signaled as YES at row 102 but the counterparty discipline owners are not enumerated in the locally accessible sources for PKG-101; this is a coordination action item rather than a source-derived requirement.

## Trade-offs

- **Pre-purchase versus sequence flexibility.** Precast concrete elements (transformer bearing foundations; compressor blocks) imply lead-time and lift-plan commitments that reduce field flexibility once cast. The CWP should weigh early casting against the cost of late engineering changes, especially given the open compressor dynamic analysis.
- **Cold-weather placement versus schedule.** The -40 deg C site basis means cold-weather concrete methods (heated enclosures, accelerators, extended curing) are expected to be required at some point in the construction window; the trade between waiting for weather and using cold-weather methods affects both cost and quality. Specific method statement is TBD.
- **Specific guidance literature on precast-foundation construction methodology is not present in the locally accessible sources** beyond the items above. Additional rationale and worked examples are **TBD**.

## Examples

No worked examples of precast-foundation construction sequences, lift plans, or turnover checklists are present in the locally accessible sources for PKG-101. **TBD** pending issue of discipline engineering and/or addition of method-statement references to `_REFERENCES.md`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-101-03-01 | Decomposition's `Anticipated Artifacts` lists three items (CWP; workface plan; turnover checklist), all attributed to ResponsibleParty "EPC Integrator". DBM-Comp_and_Liquids §Excluded notes some construction-scope items (e.g., "Installation of interconnecting piping to ISBL/OSBL tie-in points") as "External interface responsibility; responsibility is to be confirmed for each tie-in" (line 117). For PKG-101 (foundations) this likely does not apply, but the workface plan must address tie-ins to adjacent disciplines whose construction responsibility is conditional. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row DEL-101-03 (ResponsibleParty = EPC Integrator) | DBM-Comp_and_Liquids §Excluded line 117 | Specification R-101-03-03, R-101-03-05; Procedure tie-in steps | EPC Integrator authors the CWP; tie-in responsibility per discipline interface is confirmed during workface planning rather than assumed | TBD |
| CT-101-03-02 | Default support basis (driven steel piles) versus package name "Precast concrete foundations": the package label implies precast as the primary basis, but the sources name precast only for transformers and compressor blocks. | `_CONTEXT.md` PackageName | DBM-Deepcut SEC-11 §Piles and Foundations | Datasheet Construction table; Specification R-101-03-06; Guidance Principles | Treat precast as the named-element exception (transformers, compressor blocks); rely on the package datasheet (DEL-101-02) to enumerate the tagged precast inventory rather than inferring from the package name | TBD |
| CT-101-03-03 | Compressor foundation construction-release readiness: source states "Dynamic analysis results are TBD" and "Compressor foundation dynamic analysis results are TBD" (DBM-Deepcut SEC-11) but does not explicitly call out a construction hold-point. R-101-03-07 introduces a hold-point as ASSUMPTION. | DBM-Deepcut SEC-11 §Piles and Foundations; §Assumptions | Specification R-101-03-07 (ASSUMPTION) | Specification Verification; Procedure Steps | Hold installation release for compressor foundations until dynamic analysis is accepted; confirm with engineering | TBD |
