# Guidance — DEL-089-01 EPC Scope of Work, Pig Receivers (Inlet) 3-25

## Purpose

This Scope of Work exists so the EPC Integrator can carry a single, source-grounded statement of the Pig Receivers (Inlet) PKG-089 package scope into vendor procurement, package integration, construction, and acceptance. It is the Gate 5 EPC anchor deliverable that frames the downstream Package Datasheet (DEL-089-02), Construction Work Package (DEL-089-03), and EPC Vendor Package Review and Acceptance (DEL-089-06). SOURCE: _CONTEXT.md; DELIVERABLE_REGISTER.csv DEL-089-01..DEL-089-06.

## Principles

- **Vendor / EPC split is preserved.** The Package Vendor owns package engineering, design, vendor documentation, and physical equipment. The EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance. The Scope of Work shall never silently assign vendor engineering content to the EPC Integrator. SOURCE: PACKAGE_REGISTER.csv PKG-089 responsibility model; OBJ-004.
- **Source authority over decomposition prose.** When DBM 3-25 SEC-04 and PACKAGE_REGISTER scope statement disagree on count or size, the disagreement is preserved as a conflict for human ruling, not silently reconciled in either direction. SOURCE: skill four-documents Authority Hierarchy; K-PROV-1.
- **Interfaces are first-class.** The package shows up in facility interface registers across ten interface types. The Scope of Work shall list those types explicitly so downstream interface deliverables can land cleanly. SOURCE: PACKAGE_REGISTER.csv PKG-089; OBJ-003; OBJ-006.
- **Sour service drives code and material selection.** The 03-25 facility processes Doe field sour wellstream; CSA Z662 governs pipeline-tie design. Detailed standards table is left TBD until the Word source basis is accessible. SOURCE: DBM 3-25 SEC-04; DBM 3-25 SEC-15 (ASSUMPTION on full citation).

## Considerations

- **Plant inlet boundary is a contract surface.** The first aboveground flange within the lease boundary is where the Doe field pipeline contractor hands off to the facility scope. The EPC Scope of Work should flag this as a construction-handoff line and a constructability risk for the inlet ESDV and pig receiver. SOURCE: DBM 3-25 SEC-04.
- **Frac flowback governs over pigging slug.** The downstream separator slug handling (approx 38 m3) and 04-25 stabilization (approx six-hour processing window) bound how aggressively operations may pig. The pig-receiver scope should be readable against this transient case, not against pigging slug volume alone. SOURCE: DBM 3-25 SEC-04 Slug and Flowback Basis.
- **Delivery-point ESDV shutdown pressure is TBC.** Detailed design must resolve this before issuing equipment datasheets. SOURCE: DBM 3-25 SEC-04.
- **Objective association is package-heuristic.** OBJ-002 through OBJ-010 are recorded as supported by this deliverable via package-grouping heuristic. Treat the OBJ-006 (I&C, fire/gas, shutdown) and OBJ-009 (safety, relief, sour service, codes) linkages as directionally relevant rather than narrowed in source. SOURCE: OBJECTIVE_REGISTER.csv; skill four-documents Step 1.

## Trade-offs

- **Single vs. multi-receiver configuration (see Conflict C-001).** Source materials disagree. A single combined three-phase receiver (DBM SEC-04) simplifies inlet piping but couples isolation, purge, and flare-vent provisions to a single skid; a 2-receiver configuration (PACKAGE_REGISTER) supports redundancy / capacity sharing matched to the two separator trains but increases interface counts (process piping, ESDV count, I&C cabling, supports). The Scope of Work shall not pre-select; the EPC Integrator must obtain a human ruling and update both the Scope of Work and the Package Datasheet (DEL-089-02). SOURCE: DBM 3-25 SEC-04; PACKAGE_REGISTER.csv PKG-089.
- **Non-enclosed structural steel skid.** Both sources agree the skid is structural-steel, non-enclosed. This trades enclosure cost / freeze protection (mitigated by EHT interface, see PACKAGE_REGISTER interface types) against weight and footprint. SOURCE: DBM 3-25 SEC-04; PACKAGE_REGISTER.csv PKG-089.

## Examples

- *Function statement example:* "Plant inlet pipeline gas enters the facility through PKG-089 (26020-02-PT-35-001 Pig Receivers (Inlet)) and proceeds to inlet separators V-1600-2 and V-1700-2 for three-phase separation." SOURCE: PACKAGE_REGISTER.csv PKG-089; DBM 3-25 SEC-04 Inlet Separation.
- *Boundary statement example:* "The plant inlet boundary is the first aboveground flange within the lease boundary; offsite Doe field inlet pipeline scope is excluded." SOURCE: DBM 3-25 SEC-04.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-001 | Pig receiver count and size disagree. | PACKAGE_REGISTER.csv PKG-089 scope statement: "2 identical 610 mm (24") OD Pig receivers on dedicated structural steel non-enclosed skids" | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04 Inlet Pipeline Interface and Pigging: "A single combined three-phase pig receiver ... pig receiver size is TBD" | Datasheet Attributes/Construction; Specification R-3, R-5, R-8 | PROPOSAL: PACKAGE_REGISTER is the authoritative companion register row (CompanionRegisterRow=TRUE) and is later in the decomposition; treat it as authoritative unless the human rules otherwise. The DBM SEC-04 entry may pre-date the package register or refer to a different design state. | TBD |
| C-002 | Delivery-point ESDV shutdown pressure is unresolved. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04: delivery-point ESDV shutdown TBC | (no second source) | Datasheet Conditions; Specification R-6 | PROPOSAL: leave TBD; resolve at detailed design. | TBD |
| C-003 | Word source basis (26020-Package_Requirements.docx package heading 42; 26020-02-PT-RFQ-35-001-Pig_Recv_1.docx) is not readable as text. | _REFERENCES.md; PACKAGE_REGISTER.csv PKG-089 source-basis column | (file format) | Specification R-9 standards table; R-10 SOW item mapping | PROPOSAL: convert binary sources to readable form (pdf2md or equivalent) before final Scope of Work issue; until then, leave standards detail and SOW item mapping TBD. | TBD |
