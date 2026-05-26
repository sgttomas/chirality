# Specification: DEL-082-04 — Vendor Engineered Equipment Package (Flare KO Drum, Low Pressure, 3-25)

## Scope

This specification governs the Package Vendor production unit for the engineering, design, fabrication/supply, and the physical equipment package for the 03-25 LP flare knock-out drum (V-3900-2) and its in-package accessories, developed from the EPC package Scope of Work (DEL-082-01) and the EPC Package Datasheet (DEL-082-02).

Included:
- Vendor engineering and design of V-3900-2 LP flare KO drum.
- Vendor design and supply of the integral LP flare KO drum transfer pump P-3900-2 (1 x 100 percent) routing accumulated liquids to slop. (Source: DBM line 499, 584.)
- Package-internal instrumentation, valving, drains, and tie-in flanges sized to the LP relief and slop services.
- Vendor package design basis and datasheet set as the vendor handoff back to the EPC Integrator. (Source: `_CONTEXT.md` Anticipated Artifacts.)

Excluded:
- External LP relief header design upstream of the package tie-in flange (EPC scope; header carried as 508 mm / 20 inch in source basis — DBM line 499).
- LP flare stack and shared HP/Cryo+LP dual flare stack scope (separate package interface — DBM line 497, 499).
- EPC review and acceptance scope (covered by DEL-082-06).
- Vendor documentation turnover (covered by DEL-082-05).

## Requirements

### R1 — Service definition (FACT, source-anchored)
The package shall provide LP flare knock-out service for the LP relief loads from TEG regeneration, VRU, and compressor seal-pot services. (Source: DBM line 499.)

### R2 — Tag identity (FACT)
The KO drum shall be tagged V-3900-2 and the transfer pump shall be tagged P-3900-2, consistent with the accepted 03-25 DBM tag basis. (Source: DBM line 499.)

### R3 — Pump sparing (FACT)
The LP flare KO drum transfer pump shall be supplied as 1 x 100 percent. (Source: DBM line 584.)

### R4 — Liquid disposition (FACT)
Accumulated liquids shall be pumped to slop. (Source: DBM line 499.)

### R5 — Relief sizing basis (PROPOSAL, location TBD)
Drum sizing (diameter, length, holdup, vapor space, demister) shall be established by the vendor against the LP relief load case set by the accepted blowdown philosophy. The governing document is the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001, which is referenced but not locally accessible. (Source: DBM line 501; location TBD for the final relief load.)

### R6 — Staggered blowdown coordination (FACT, applies to system)
The blowdown sequence is required to be staggered to limit maximum relief. The vendor design shall accept the staggered-blowdown LP relief profile as defined by the EPC Package Datasheet and accepted blowdown philosophy. (Source: DBM line 501.)

### R7 — Sour-service review (ASSUMPTION)
The vendor shall perform a sour-service material review for all wetted components. The facility is sour per DBM isolation philosophy (DBM line 607, sour-hydrocarbon service guidance). Specific NACE / MR0175 applicability is TBD pending EPC datasheet (DEL-082-02) issue.

### R8 — Code basis (TBD)
Governing pressure vessel and relief code(s) shall be confirmed by the EPC Integrator on the EPC Package Datasheet (DEL-082-02). The vendor shall design to those codes. (Location TBD.)

### R9 — Interface tie-ins (FACT for routing; sizes TBD at the drum)
Package tie-in flanges shall be provided for: LP relief inlet from 508 mm / 20 inch LP relief header (header basis per DBM line 499; drum nozzle sizing TBD); vapor outlet to LP flare stack; liquid outlet to P-3900-2 to slop; required drains, vents, instrument, and PSV connections.

### R10 — Anticipated artifacts (FACT)
The vendor shall deliver the vendor engineered physical equipment package together with a vendor package design basis and datasheet set. (Source: `_CONTEXT.md` Anticipated Artifacts.)

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 | Governs LP relief sequencing and load case | Referenced in DBM line 501; not locally accessible — location TBD |
| EPC Scope of Work (DEL-082-01) | Defines vendor scope handoff | Peer deliverable; not yet accepted — TBD |
| EPC Package Datasheet (DEL-082-02) | Defines vendor design inputs (pressures, temperatures, sour-service, codes) | Peer deliverable; not yet accepted — TBD |
| 26020-Package_Requirements.docx, heading 35 | Decomposition-cited requirements source | Referenced by DELIVERABLE_REGISTER.csv row for DEL-082-04; sliced text not locally accessible — location TBD |
| Pressure vessel code (ASME BPVC Section VIII Div 1 or equivalent jurisdictional code) | ASSUMPTION pending DEL-082-02 confirmation | TBD |
| Pressure-relief code basis (API STD 521 / API STD 520) | ASSUMPTION pending DEL-082-02 confirmation | TBD |
| NACE MR0175 / ISO 15156 | ASSUMPTION pending sour-service confirmation on DEL-082-02 | TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 — Service definition | Review vendor design basis against DBM line 499 service list |
| R2 — Tag identity | Vendor drawing and nameplate review against tag register |
| R3 — Pump sparing | Vendor mechanical scope review (single pump, 100 percent capacity) |
| R4 — Liquid disposition | P&ID and tie-in review confirming P-3900-2 routes to slop |
| R5 — Relief sizing | Vendor sizing calculations reviewed against the blowdown philosophy LP relief load (location TBD until W242510-PRC-REP-000003-001 is sliced) |
| R6 — Staggered blowdown | EPC integration review confirms vendor accepted profile matches accepted philosophy |
| R7 — Sour-service review | Vendor material certification and MR0175 compliance documentation (when sour-service is confirmed) |
| R8 — Code basis | Vendor U-stamp / equivalent certification plus relief sizing per cited codes |
| R9 — Tie-ins | Interface-flange dimensional review and P&ID alignment with EPC datasheet |
| R10 — Anticipated artifacts | Document register check confirming vendor design basis and datasheet set delivered |

## Documentation

Vendor shall deliver the following artifact set (Source: `_CONTEXT.md` Anticipated Artifacts; supplemented by typical vendor package deliverables — ASSUMPTION):

- Vendor engineered physical equipment package (the supplied drum + pump skid/assembly).
- Vendor package design basis (operating, design, and load-case basis statement).
- Vendor package datasheet set (drum datasheet, pump datasheet, instrument datasheet list, valve list).
- General arrangement and outline drawings — ASSUMPTION (typical vendor package).
- P&ID for the supplied package scope — ASSUMPTION.
- Inspection and test plan (ITP) and code certification — ASSUMPTION.
- Operation and maintenance documentation supporting DEL-082-05 (Vendor Document Turnover Package) — TBD final list governed by DEL-082-05.
