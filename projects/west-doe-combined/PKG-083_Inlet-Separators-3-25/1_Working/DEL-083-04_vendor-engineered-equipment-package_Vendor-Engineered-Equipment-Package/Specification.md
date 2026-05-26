# Specification — DEL-083-04 Vendor Engineered Equipment Package (Inlet Separators 3-25)

## Scope

This specification governs the Package Vendor production unit for engineering, design, fabrication/supply, and physical delivery of the two horizontal three-phase inlet separator packages (V-1600-2 and V-1700-2) for the 03-25 West Doe Compressor Station and Liquids Hub.

**In scope:**
- Vendor engineering and design of separator vessels, internals, controls, and skid layout for V-1600-2 and V-1700-2
- Fabrication or supply of the physical equipment package
- Vendor package design basis and datasheet set
- Vendor heated self-framing building for instrumentation and one end of each package (extent per EPC handoff)
- Integration deliverables required to support EPC Integrator review and acceptance (DEL-083-06)

**Excluded:**
- EPC Scope of Work (`DEL-083-01`) and EPC Package Datasheet (`DEL-083-02`) (EPC Integrator scope)
- Construction Work Package and field tie-ins (`DEL-083-03`)
- Vendor Document Turnover Package (`DEL-083-05`) — separate vendor production unit
- Downstream methanol disposition system; downstream slug handling at 04-25 stabilization

## Requirements

### R1 — Equipment count and capacity
- R1.1 The vendor shall supply two (2) identical horizontal three-phase inlet separator packages, each sized for 50 percent of facility capacity. Source: DBM 3-25 line 244, line 570.
- R1.2 Each package shall handle 40 MMSCFD gas, 556 m3/d condensate (3,494 bbl/d), and 1,800 m3/d produced water (11,322 bbl/d). Source: DBM 3-25 lines 248-250.
- R1.3 **CONFLICT** — Older `2 x 100%` language exists in source; current basis is `2 x 50%` no spare. Detailed design shall reconcile before issuing final vendor datasheets. Source: line 570. See Conflict Table in `Guidance.md`.

### R2 — Vessel design parameters
- R2.1 Vessel diameter: 2,743 mm (9 ft). Source: line 251.
- R2.2 Straight-side length: 12,191 mm (40 ft). Source: line 252.
- R2.3 ANSI 600# pressure class. Source: line 253.
- R2.4 Design pressure: 4,963 kPag. Source: line 254.
- R2.5 Slug handling: approximately 38 m3 per separator. Source: line 255.
- R2.6 Pressure vessels shall meet applicable pressure class, sour-service requirements, corrosion allowance, manway access, internals removal, drainage, venting, and inspection needs. Source: line 611.

### R3 — Coatings and internals
- R3.1 Internal coating: Devchem 253. Source: lines 256, 611.
- R3.2 Piping is not coated under the current separator basis. Source: line 260.
- R3.3 Internals shall include a manually adjustable weir, vertical/horizontal high-performance mesh/vane mist eliminators, and de-sanding provisions. Source: line 260.

### R4 — Operating conditions
- R4.1 Low operating pressure 125 psig; design operating pressure 200 psig; maximum 572 psig. Source: line 258.
- R4.2 Normal high operating pressure: `TBC` — vendor shall confirm during detailed design.
- R4.3 Inlet design temperature 8.3 deg C; **ASSUMPTION** — vendor must reconcile inlet temperature basis with EPC Integrator before issuing final equipment datasheets per source note. Source: line 258.
- R4.4 Inlet separator ESDV shutdown pressure: 635 psig. Source: line 230.

### R5 — Control valves
- R5.1 Each package shall include at least two parallel inlet pressure-control valves using balanced globe hardened trim with ΔP limit ≤ 5 psid. Source: line 266.
- R5.2 Each package shall include at least two parallel produced-water level-control valves. Source: line 266.

### R6 — Drains and ancillaries
- R6.1 Each separator boot shall accommodate infrequent methanol drainage. Downstream methanol disposition is `TBD` and not in vendor scope. Source: line 218.
- R6.2 Drive-gas recycle from downstream of inlet compressor aftercoolers returns to the separators; vendor package piping shall accept this return. Source: line 264.

### R7 — Layout and housing
- R7.1 Instrumentation and one end of each package shall be enclosed in a heated self-framing building. Building extent is `TBD` at this stage. Source: line 260.
- R7.2 Inlet piping symmetry to distribute flow evenly is an EPC Integrator scope item; vendor connections shall match the symmetrical inlet manifold (interface). Source: line 264.

### R8 — Sour service and materials
- R8.1 Sour-service material selection per pressure-vessel section requirements; corrosion allowance and coating selection consistent with R3.1. Source: line 611.

## Standards

| Standard / Reference | Application | Location |
|---|---|---|
| Project sour-service requirements (per DBM SEC-04 / SEC-06) | Vessel materials, coatings | DBM 3-25 line 611 |
| ANSI B16.5 / equivalent for 600# rating | Flange and pressure-class hardware | location TBD (not cited in available source slice) |
| `26020-Package_Requirements.docx` package heading 36 | Package-level vendor requirements | location TBD (binary; not extracted in this run) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.1, R1.2 | Vendor capacity calculations reviewed against DBM 3-25 §Inlet Separation; equipment count witnessed at FAT |
| R2.1–R2.5 | Vendor mechanical drawings and U1A forms; dimensional and hydrotest record |
| R2.6 | Sour-service NACE compliance certificates; manway and clearance check on drawings |
| R3.1, R3.3 | Coating inspection report (Devchem 253); internals inspection at FAT |
| R4.1–R4.4 | Operating envelope table on vendor datasheet; ESDV setpoint records |
| R5.1, R5.2 | Control valve datasheets and FAT instrument-loop checks |
| R6.1 | Boot drain GA review |
| R7.1 | Building GA review and heat-tracing/heating capacity calculation |
| R8.1 | Material test reports (MTRs); NACE MR0175 compliance |

## Documentation

The vendor shall deliver (per `_CONTEXT.md` anticipated artifacts and EPC integration expectations):

- Vendor package design basis (PDB)
- Vendor equipment datasheets for V-1600-2 and V-1700-2
- Mechanical GAs, P&IDs, and PFDs for each separator package
- Internals drawings (weir, mist eliminators, de-sanding)
- Control valve datasheets and instrument index
- Coating specification and inspection plan (Devchem 253)
- Hydrotest, NDE, MTR, and PWHT records
- FAT plan and FAT report
- Building GA and heating-system capacity sheet
- Vendor inputs feeding `DEL-083-05` (Vendor Document Turnover Package) and `DEL-083-06` (EPC Vendor Package Review and Acceptance)
