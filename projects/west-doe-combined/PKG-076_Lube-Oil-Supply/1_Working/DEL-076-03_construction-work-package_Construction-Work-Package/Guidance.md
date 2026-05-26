# Guidance — DEL-076-03 Construction Work Package (Lube Oil Supply, PKG-076)

## Purpose

This Construction Work Package exists so the EPC Integrator can take a vendor-supplied lube oil supply package (two pumps and one split horizontal storage tank serving compressor frame day tanks) and physically install, inspect, tie in, and turn it over to commissioning as part of the West Doe Deepcut facility (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER row 386). It is one of the six Gate 5 EPC anchor deliverables for PKG-076 and supports the facility integration objective OBJ-001 and the vendor/EPC responsibility-split objective OBJ-004 (OBJECTIVE_REGISTER rows 2 and 5).

## Principles

1. **Responsibility split is load-bearing.** The Package Vendor supplies the engineered package; the EPC Integrator owns shipping-to-site, pile installation, tie-in piping, electrical connections, mounting platform and stairs (SCOPE_LEDGER SOW-0138; OBJ-004). The construction work package must never silently absorb vendor-side engineering or vice-versa.
2. **All workbook-declared interface types must be addressed.** The eight interface facts for PKG-076 in INTERFACE_REGISTER (Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Maintenance Access, Structural / Foundations / Supports) are each in EPC scope and each must trace to specific construction work and verification.
3. **Sour-service integrity.** "Sweet and sour service" is stated in source (SCOPE_LEDGER SOW-0137). All installation choices for piping, gaskets, bolting, and welding must preserve sour-service materials traceability (OBJ-009).
4. **Source over convention.** Where the package requirements document (heading 30) or the DBM addresses a construction question explicitly, the document wins over generic construction convention. Where the source is silent, the construction work package marks `TBD` rather than inventing values.

## Considerations

- **Heated storage tank.** The horizontal tank is split (~400 bbl + 200 bbl sections, both heated per SCOPE_LEDGER SOW-0137). Construction will need to address heater installation, insulation, EHT (electric heat trace), and instrument tie-ins. Specific heater type, EHT class, and insulation thickness are not in the accessible source slice — `TBD`.
- **Driver exclusion.** "No Toshiba motors" (SCOPE_LEDGER SOW-0138) is a hard exclusion at receipt-inspection time, not just at procurement. The CWP must check.
- **Compressor day-tank consumers.** P-9240-1 and P-9250-1 fill frame day tanks "of various compressor packages." The CWP discharge tie-in routing depends on the compressor package layouts (PKG-001…PKG-075-class compressor packages). Final routing is a workface-plan item; specific compressor receiving points are not enumerated in the accessible source slice — `TBD`.
- **Containment / spill management.** Lube oil release in the Storage Tank Area is a containment risk; site drain / containment basis is referenced (IFC-09EA6BEDB8) but the design detail is in facility civil/structural deliverables, not here.
- **Constructability vs vendor design.** If vendor package design choices create construction-side problems (e.g., lift weights, awkward tie-in nozzles), the EPC Integrator handles them through `DEL-076-06_epc-vendor-package-review-and-acceptance`, not by editing this CWP.

## Trade-offs

- **Field-routed vs pre-fabricated tie-in piping.** Pre-fabrication reduces field weld count (sour-service benefit) but requires earlier vendor nozzle locations. Default ASSUMPTION: prefer pre-fabricated tie-ins for sour-service segments; resolve in workface plan after vendor GA drawings.
- **Stand-alone platform vs shared structure.** Mounting platform and stairs are EPC scope (SCOPE_LEDGER SOW-0138). A stand-alone platform is simpler but consumes more area in the Storage Tank Area; a shared structure with adjacent equipment saves area but couples maintenance access — `TBD` per civil/structural design.

## Examples

No worked examples are available from the accessible source slice. Reference precedent construction work packages from prior compressor-package installations on this site if/when those source artifacts become locally accessible.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | "By others" in SCOPE_LEDGER SOW-0138 reads from vendor perspective and assigns shipping/installation/tie-ins/electrical to EPC; PACKAGE_REGISTER row 70 narrative similarly assigns integration to EPC. No direct conflict identified, but the phrase "By others" is fragile if the CWP is read in isolation. | SCOPE_LEDGER SOW-0138 ("By others") | PACKAGE_REGISTER row 70 (EPC integration narrative) | Specification §Scope; Procedure §Prerequisites | Treat all "By others" items as EPC Integrator scope for this CWP. | TBD |
| CONF-02 | Site/area electrical classification (Class I Div ?? or Zone ??) not in accessible source slice; required for electrical tie-in design. | `_REFERENCES.md` 26020-Package_Requirements.docx heading 30 (location TBD) | DBM-Deepcut 4-25 SEC-12 Electrical Basis (not locally extracted) | Specification REQ-CWP-04, REQ-CWP-06; Datasheet Conditions | Carry as TBD until source slices are extracted to deliverable-local references. | TBD |
| CONF-03 | Sour-service materials standard (NACE MR0175 vs ISO 15156 vs both) not explicitly stated in accessible source slice. | SCOPE_LEDGER SOW-0137 ("sweet and sour service") | OBJ-009 source slices (DBM SEC-15 Regulatory, Codes, and Standards Basis) | Specification §Standards; REQ-CWP-10 | PROPOSAL: NACE MR0175 / ISO 15156 (industry-default for sour-service materials) — confirm against DBM SEC-15. | TBD |
