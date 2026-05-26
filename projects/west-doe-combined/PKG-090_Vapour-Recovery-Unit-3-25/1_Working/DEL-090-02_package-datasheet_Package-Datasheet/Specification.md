# Specification — DEL-090-02 Package Datasheet (Vapour Recovery Unit 3-25)

> Normative requirements for the EPC Package Datasheet to be issued for the 3-25 Vapour Recovery Unit. Requirements derive from the 3-25 Comp_and_Liquids DBM where source slices are locally accessible; inferences are labeled `ASSUMPTION` and unresolved values are `TBD`.

## Scope

### In scope
- Define the EPC Integrator package datasheet content for the 3-25 VRU as the technical handoff basis to a third-party vendor or discipline package engineering.
- Capture package equipment, design conditions, interfaces, and supporting references in a form sufficient for vendor engineering and design under the active SCA-002 / SCA-006 basis.
- Carry interface facts (suction, discharge, utilities, flare) as evidence inside this datasheet rather than as standalone deliverables, per `_CONTEXT.md` "Notes".

### Out of scope
- Vendor-internal design, fabrication, or vendor document submittals (covered by DEL-090-04 and DEL-090-05).
- Construction installation, tie-in, and turnover (covered by DEL-090-03).
- EPC review/acceptance of the vendor package (covered by DEL-090-06).
- Local 03-25 SOC, local 03-25 stabilization, local 03-25 instrument air, or 03-25 heat-medium content (superseded under SCA basis per DBM SEC-01).

## Requirements

### R-1 Equipment basis
- R-1.1 The package shall comprise two 200 hp electric-drive vapour recovery compressor packages arranged 2 x 100 percent. (Source: `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06.)
- R-1.2 The package shall serve as the tank-vapour recovery unit for the 03-25 Liquids Hub, accepting vapours from condensate and produced-water tank systems and selected process vents per the active process basis. (Source: DBM SEC-06.)

### R-2 Discharge routing
- R-2.1 VRU discharge shall be routed to the 04-25 SOC suction, consistent with SCA-002. (Source: DBM SEC-01, SEC-06.)
- R-2.2 The datasheet shall not specify a local 03-25 SOC; local SOC has been removed from the current basis. (Source: DBM SEC-01 "Removed scope items".)

### R-3 Recycle and suction-pressure control
- R-3.1 Each VRU shall include a recycle path returning second-stage discharge to first-stage suction. (Source: DBM SEC-06.)
- R-3.2 The recycle valve shall be sized for 100 percent flow at minimum driver speed and lowest discharge pressure. (Source: DBM SEC-06.)
- R-3.3 A make-up / blanket-gas regulator from LP fuel gas shall maintain minimum suction pressure at maximum turndown. (Source: DBM SEC-06.)
- R-3.4 Recycle-valve final fail action: TBD for VRU (compressor recycle valves elsewhere expected fail-open per DBM SEC-05; VRU-specific value not isolated in source slice). `location TBD`.

### R-4 Suction header and flare interface
- R-4.1 The VRU suction header shall include an LP-flare bypass V-ball valve operated by VRU suction pressure. (Source: DBM SEC-06.)
- R-4.2 The VRU suction header shall free-drain or slope toward the flare KO interface as defined by detailed design. (Source: DBM SEC-06.)
- R-4.3 LP relief paths from the VRU shall route to the LP flare via LP KO drum V-3900-2 with pump P-3900-2 to slop. (Source: DBM SEC-07 "Flare and Blowdown".)

### R-5 Utility interfaces
- R-5.1 Instrument air shall be supplied from 04-25; no local 03-25 instrument-air compressor package shall be specified for the VRU. (Source: DBM SEC-07 "Instrument Air".)
- R-5.2 Fuel-gas blanket / make-up for the VRU shall be drawn from the LP fuel-gas system. (Source: DBM SEC-06, SEC-07.)
- R-5.3 Electrical power shall be supplied from the shared cross-facility utility system. (Source: DBM SEC-07 "Utility Integration Basis".)

### R-6 Service condition basis
- R-6.1 Service shall be classified as sour hydrocarbon vapour, with methyl-mercaptan toxicity context applicable to vent, purge, and analyzer planning. (Source: DBM SEC-07 "Fuel-Gas Sulphur and Purge Hazard Basis".)
- R-6.2 Design suction pressure, design suction temperature, design discharge pressure, design capacity per package, and inlet composition envelope: `TBD` (not stated in accessible DBM slice; `location TBD`).
- R-6.3 Tag list (compressor packages, drivers, KO, recycle valves, regulators) shall be issued with the datasheet: `TBD` — tag list not extracted from accessible source.

### R-7 Datasheet artifact set (this deliverable's outputs)
- R-7.1 The datasheet package shall include: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and source-supported equipment and design criteria. (Source: `_CONTEXT.md` "Anticipated Artifacts".)
- R-7.2 The interface requirements matrix shall enumerate suction sources, discharge interface to 04-25 SOC suction, fuel-gas, instrument air, electrical, flare, and drain interfaces.

### R-8 Source fidelity and traceability
- R-8.1 Every non-trivial value in the datasheet shall cite a source (`SourcePath` + `SectionRef`) or be labeled `TBD` with `location TBD`.
- R-8.2 Inferences shall be labeled `ASSUMPTION`; conflicts shall be entered in the Conflict Table in `Guidance.md`.
- R-8.3 The datasheet shall not reintroduce superseded scope (local 03-25 SOC, local 03-25 stabilization, local 03-25 instrument air, 03-25 heat-medium). (Source: DBM SEC-01 "Removed scope items" and SEC-06 "Current Supersession Controls".)

## Standards

| Standard / Source | Applicability | Source location |
|---|---|---|
| 3-25 Comp_and_Liquids DBM (current governed basis) | Authoritative project design basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| SCA-002 (VRU discharge to 04-25 SOC suction) | Governs discharge routing | Cited in DBM SEC-01, SEC-06 |
| SCA-006 (no local 03-25 instrument air) | Governs IA interface | Cited in DBM SEC-07 |
| 26020-Package_Requirements.docx (heading 43) | Decomposition-cited package requirement source | `_Sources/26020-Package_Requirements.docx` (text slice not locally accessible — `location TBD`) |
| 26020-Packages_Interfaces_4_export.xlsx | Decomposition-cited interface source | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (text slice not locally accessible — `location TBD`) |
| Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 | Required for final blowdown sequencing tied to flare interface | DBM SEC-07 "Flare and Blowdown"; document not accessible locally — `location TBD` |
| Industry codes (ASME, API, CSA, applicable provincial codes) | ASSUMPTION — typical for mechanical compressor packages; clause-level claims withheld pending source access | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 Equipment basis | Cross-check datasheet equipment list against DBM SEC-01 and SEC-06 entries (2 x 200 hp electric-drive, 2 x 100 percent). |
| R-2 Discharge routing | Confirm discharge tie-in tag and pressure align with 04-25 SOC suction interface; reference SCA-002. |
| R-3 Recycle and suction-pressure control | Inspect recycle-line P&ID, valve sizing calculations against minimum driver speed / lowest discharge pressure; verify LP-fuel-gas regulator presence. |
| R-4 Suction header and flare interface | P&ID and isometric review for V-ball bypass, free-drain slope, LP KO routing to V-3900-2 / P-3900-2. |
| R-5 Utility interfaces | Confirm instrument-air, fuel-gas, and electrical sources match cross-facility utility basis. |
| R-6 Service condition basis | Vendor returns design pressures, temperatures, capacities, and composition envelope; values reviewed against DBM-derived envelope when available. |
| R-7 Datasheet artifact set | Datasheet issue check: datasheet, handoff basis, interface matrix, and design-criteria document all present. |
| R-8 Source fidelity | Source-citation review on every non-trivial value; `TBD`/`ASSUMPTION` labels intact; Conflict Table in `Guidance.md` reviewed. |

## Documentation (required artifacts at issue)

- Package technical datasheet (this deliverable's primary artifact)
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria
