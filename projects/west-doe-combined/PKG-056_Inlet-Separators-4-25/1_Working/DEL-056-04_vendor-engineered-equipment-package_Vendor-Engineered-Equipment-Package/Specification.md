# Specification — DEL-056-04 Vendor Engineered Equipment Package

**Pass:** P1/P2 | **DECOMP_VARIANT:** PROJECT | **Skill:** four-documents

## Scope

This specification governs the Package Vendor production unit for the Inlet Separators 4-25 package (PKG-056): engineering, design, fabrication/supply, and delivery of the physical equipment package. The vendor scope is anchored to the EPC Scope of Work (DEL-056-01) and Package Datasheet (DEL-056-02) and is reviewed by the EPC Integrator for integration.

**Includes:**
- Vendor engineered physical equipment package for two (current authority) horizontal three-phase inlet separator packages and associated package components.
- Vendor package design basis and datasheet set.

**Excludes:**
- EPC-integrator-owned deliverables (Scope of Work, Package Datasheet, Construction Work Package, EPC vendor review/acceptance).
- Vendor document register and turnover records (DEL-056-05 Vendor Document Turnover Package).
- Cross-package facility design decisions that are not local to the inlet separator package.

## Requirements

Each requirement is grounded in the locally accessible source slices. Inferences are labeled **ASSUMPTION**. Where source location is known to be in the docx/xlsx that has not been extracted to readable slices, **location TBD** is recorded.

### R1 — Configuration

- **R1.1** The package shall comprise horizontal three-phase inlet separators arranged as identical parallel units; current governed basis is two (2) installed packages, each sized for one half of facility capacity. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R1.2** The package shall preserve plot space for a future third separator. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R1.3** Legacy "four inlet separator packages" / "4 x 50%" basis is **CONFLICT** with R1.1; vendor design shall proceed on R1.1 unless EPC ruling overrides. See `Guidance.md` Conflict Table.

### R2 — Vessel design

- **R2.1** Separator vessels shall be designed per applicable pressure class, sour-service requirements, corrosion allowance, internal coating, manway access, internals removal, drainage, venting, and inspection needs. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **R2.2** Internal coating shall be Devchem 253 on the separator vessel; associated piping is not internally coated. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **R2.3** Nominal vessel envelope: 9 ft ID x 40 ft S/S (current Deepcut basis). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R2.4** Sour-service materials selection shall reference SEC-04 of the project design basis memorandum; specific clause set location TBD until SEC-04 is locally accessible. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

### R3 — Internals

- **R3.1** Each separator shall be fitted with a manually adjustable weir. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R3.2** Each separator shall be fitted with a vertical high-performance mesh/vane type mist eliminator, subject to operations review. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R4 — Pressure ratings and process conditions

- **R4.1** Maximum inlet operating pressure: 1300 psig (basis: 90% of assumed upstream gathering pipeline MAOP 1440 psig); shall be validated during detailed engineering. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R4.2** Design pressure from plant gate up to inlet PCV downstream manual isolation shall equal upstream inlet pipeline MAWP. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R4.3** Design pressure downstream of inlet PCV to J-T valve/expander outlet isolation in cryogenic unit shall be 1360 psig (equivalent 600# flanges at 200 deg F). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R4.4** Total design vapour flow across the inlet separator population shall be 300 MMSCFD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R4.5** Per-separator slug capacity: TBD — current source identifies an unresolved range of 31.8-33.9 m3. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R4.6** Peak produced water rate, water retention time, condensate retention time: TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R5 — Inlet pressure control

- **R5.1** Each inlet separator package shall be provided with at least two parallel balanced-globe inlet pressure control valves with hardened trim; design differential pressure shall be <= 5 psid at design inlet pressure. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **R5.2** Skid-edge inlet isolation shall enable isolation of the inlet PCVs for maintenance. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R5.3** Outlet manual isolation shall enable PCV maintenance without blowing down the full separator. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R6 — Level control and produced water

- **R6.1** Each package shall be provided with at least two parallel produced-water level control valves. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **R6.2** Methanol may report to and drain at the inlet separator boot; downstream methanol disposition TBD. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

### R7 — Liquid outlet heater

- **R7.1** One liquid outlet heater shall be installed per inlet separator package to heat cold liquid (~-26 deg C inlet) to a temperature sufficient to keep MPFF LCV feed above hydrate and freeze thresholds. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R7.2** Outlet temperature target, duty, and heating medium: TBD pending process simulation; candidate media include warm glycol and process-stream cross-exchange. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R8 — ESDV and shutdown

- **R8.1** A full-port piggable facility inlet ESDV with position transmitters shall be provided on the pig receiver inlet skid (interface — not vendor scope but governed for fit). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- **R8.2** Inlet separator shut ESDV pressure shutdown is 1360 psig per Deepcut basis; 635 psig appears in Comp_and_Liquids basis. **CONFLICT** — see Conflict Table.
- **R8.3** If inlet pipeline MAOP exceeds facility inlet design pressure, HIPPS may be required to protect inlet separators; HIPPS requirements TBC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R9 — Methanol and drive gas

- **R9.1** Vendor package shall provide injection points for methanol upstream of PCV and upstream of HCL/water dump valves; design capacities TBC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **R9.2** Drive gas (sales gas upstream of sales gas splitter; alternate inlet compressor discharge) shall be separately metered to each inlet separator package because drive gas enters upstream of plant inlet gas meters. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R10 — Package isolation philosophy

- **R10.1** Parallel inlet separator packages shall be isolatable on a unit basis so the entire unit can be removed from service while other units operate. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R11 — Package building

- **R11.1** Each inlet separator package shall be enclosed in a self-framing package building that encloses instrumentation and one end of the vessel. **ASSUMPTION**: this configuration mirrors the MPFF package narrative in the Deepcut DBM, which states "the MPFF package is configured similarly to the inlet separator." Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

### R12 — Interfaces

- **R12.1** Vendor package shall interface with: MPFF via heated hydrocarbon liquid outlet lines; gas processing train via overhead gas; LP fuel gas for purge/drive; HP flare for vents and blowdown; methanol injection; closed hydrocarbon drain; produced-water handling; package controls. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

## Standards

- Project design basis memoranda (DBM-Deepcut and DBM-Comp_and_Liquids), SEC-04 (separator vessel design basis) and SEC-06 (produced-water tank coating where defined). Local clause-level slices for SEC-04/SEC-06 not currently extracted — **location TBD**.
- Sour-service materials, pressure-vessel code, and supporting industry codes referenced through SEC-04: specific code citations **TBD** until SEC-04 slice is accessible.
- `26020-Package_Requirements.docx` (package heading 11) — clause-level slice **location TBD** until docx is extracted to markdown.

## Verification

| Requirement | Verification approach |
|---|---|
| R1 (configuration) | Vendor design review against EPC Package Datasheet (DEL-056-02); EPC integration review (DEL-056-06). |
| R2 (vessel design) | Vendor design calculations; pressure vessel code stamping; coating procedure qualification; sour-service certification. |
| R3 (internals) | Vendor design submittal; operations review of mist eliminator and weir; factory acceptance test. |
| R4 (process conditions) | Process datasheet alignment with EPC Package Datasheet (DEL-056-02); validation during detailed engineering. |
| R5/R6 (PCVs/LCVs) | Valve datasheets; trim selection review; dP confirmation; factory acceptance test. |
| R7 (heater) | Process simulation closure of TBD items; heater datasheet; medium selection ruling; factory acceptance. |
| R8 (ESDV/HIPPS) | Shutdown setpoint ruling; HIPPS study during detailed engineering. |
| R9 (methanol/drive gas) | Injection point and meter configuration review; design capacity ruling. |
| R10 (isolation) | P&ID review; mechanical isolation/blowdown procedure review. |
| R11 (building) | Package building drawings review; vendor proposal cross-check. |
| R12 (interfaces) | Package interface requirements matrix (anchored in DEL-056-02); EPC integration review (DEL-056-06). |

## Documentation

Anticipated vendor-produced artifacts (per `_CONTEXT.md` and DELIVERABLE_REGISTER row 375):
- Vendor engineered physical equipment package (delivered hardware)
- Vendor package design basis
- Vendor datasheet set (vessel, internals, PCV/LCV, heater, instrumentation)
- Process datasheet alignment evidence against EPC Package Datasheet (DEL-056-02)
- Sour-service and coating procedure documentation
- Vendor document submittals (turnover materials are governed by DEL-056-05)
