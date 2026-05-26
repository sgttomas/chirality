# Guidance: DEL-080-03 — Construction Work Package (Inlet Compressors)

## Purpose

This Construction Work Package (CWP) exists because Gate 5 makes the EPC Integrator anchor set — Scope of Work, Package Datasheet, and Construction Work Package — mandatory for every approved package. (Source: PROJECT_DECOMP.md L118, L124; DEC-013 in PROJECT_DECOMP.md L205) The CWP is the EPC anchor that translates package scope and design data into how the package is physically built, tied into the facility, inspected, and turned over to operations. (Source: PROJECT_DECOMP.md L127; DELIVERABLE_REGISTER.csv row 362)

## Principles

1. **EPC vs. Package Vendor split.** The Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv row 66 responsibility narrative)
2. **Mandatory anchor.** This CWP is one of three mandatory EPC anchors; it is not optional, and additional package deliverables (vendor production unit, vendor document turnover, EPC acceptance) depend on the anchor being in place. (Source: PROJECT_DECOMP.md L118, DEC-013)
3. **Interface-first.** The Inlet Compressors package has thirteen declared interface types — every one of them must appear in the construction interface and turnover checklist. (Source: INTERFACE_REGISTER.csv rows 512-524)
4. **Source fidelity over convention.** Construction sequencing, methods, and materials shall reflect the accessible source basis (workbook, package requirements document, DBM) rather than generic EPC convention. NACE sour-service treatment and the no-installed-spare configuration are explicit source facts and must drive method selection. (Source: SCOPE_LEDGER.csv SOW-0121, SOW-0122)
5. **Mark unknowns.** Where source slices do not support a value (e.g., site climatic loads, foundation reactions, specific welding procedures), mark `TBD` rather than inventing a value.

## Considerations

- **Modularization.** Each compressor package is modularized into three pieces for transport and field re-assembly into self-framing buildings. Plan crane access, lift sequencing, and module-to-module fit-up early. (Source: DBM-Comp_and_Liquids §inlet compression)
- **Sour service.** H2S basis is approximately 0.296 mol% in the compressor composition table; tie-in piping and seal materials must be NACE-compliant. Confirm vendor-supplied weld filler compatibility for tie-in welds. (Source: DBM §inlet compressor process basis; SCOPE_LEDGER.csv SOW-0122)
- **Electrical interface.** 4,000 V (4160 V class) supply with starting VFDs per SCA-001 VE #34; soft starts are not permitted. Coordinate with MCC-8200 scope and harmonic/reactive-power mitigation studies. (Source: DBM §electrical)
- **2 x 50% configuration with no spare.** Construction sequencing should consider risk of single-unit non-availability during commissioning windows; staged turnover should be planned. (Source: SCOPE_LEDGER.csv SOW-0122)
- **Process operating window.** Suction approximately 1275 kPag, discharge approximately 6550 kPag, combined 80 MMSCFD — tie-in piping pressure design and PSV interfaces must be coordinated with the Relief / Flare / Vent interface. (Source: SCOPE_LEDGER.csv SOW-0122; INTERFACE_REGISTER.csv row 514)
- **Heat tracing (EHT) and HVAC** are declared interfaces and require winterization and building services coordination for the modular buildings. (Source: INTERFACE_REGISTER.csv rows 517, 522)

## Trade-offs

- **Field re-assembly vs. shop pre-fit.** More shop pre-fit reduces field risk but constrains transport; the source basis already commits to three-piece module split. Constructability review should validate that split. (Source: DBM §inlet compression; ASSUMPTION: trade-off framing — not explicit in source.)
- **Sequencing the two units.** Building both in parallel shortens schedule but stresses lay-down and trades. Sequencing them reduces peak resource demand but extends mechanical completion. (ASSUMPTION: trade-off framing — not explicit in source.)
- **Pressure test boundaries.** Wider test boundaries reduce test count but increase isolation and reinstatement scope on vendor-package fittings. (ASSUMPTION: trade-off framing — not explicit in source.)

## Examples

- The Inlet Compressors package interface set (Process Piping, Utility Piping, Relief / Flare / Vent, Drain / Containment, Electrical Power, EHT, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Structural / Foundations / Supports) is the worked example of "interface-first" — each row is a tie-in lane in the workface plan. (Source: INTERFACE_REGISTER.csv rows 512-524)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Equipment make/model named differently across sources: SCOPE_LEDGER.csv SOW-0121 says "Two Ariel KBZ/6 separable reciprocating compressor packages"; the DBM uses generic "electric-drive separable reciprocating compressor packages" with motor tags KM-2150 and KM-2250 (no compressor make/model). | SCOPE_LEDGER.csv row 122 (SOW-0121) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §inlet compression and §prime movers | Datasheet attributes; Specification R-1 | Treat the workbook/package-requirements source (Ariel KBZ/6) as authoritative for make/model and the DBM tags (KM-2150, KM-2250) as authoritative for motor tagging | TBD |
| C-2 | Permit, site civil, and welding/NDE specifications referenced indirectly but not present in accessible source slices. | DELIVERABLE_REGISTER.csv row 362 (implied scope) | (no source available) | Specification R-9, R-10; Procedure Prerequisites | Add the project welding/QA specification and site civil basis as explicit upstream references before CWP execution | TBD |
