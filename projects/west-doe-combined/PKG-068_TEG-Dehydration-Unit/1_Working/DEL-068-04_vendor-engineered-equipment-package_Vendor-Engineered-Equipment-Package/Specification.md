# Specification — DEL-068-04 Vendor Engineered Equipment Package (TEG Dehydration Unit)

## Scope

### Covers
- Vendor engineering and design of the one-by-100 percent TEG dehydration package described in SEC-05 of `3-25_Comp_and_Liquids_DBM.md`.
- Fabrication/supply of the physical equipment package including the equipment items listed in `Datasheet.md` (contactor, regen train, filtration, pumps, makeup system, exchangers, drums, columns).
- Vendor package design basis and datasheet set (per `_CONTEXT.md` anticipated artifacts).
- Vendor compliance with the EPC Scope of Work (DEL-068-01) and the EPC Package Datasheet (DEL-068-02) which together anchor this vendor production unit.

### Excludes
- EPC Integrator scope of work, package datasheet authorship, construction work package authorship, and EPC integration acceptance (these are DEL-068-01, DEL-068-02, DEL-068-03, DEL-068-06).
- Vendor document turnover register and submittal management (DEL-068-05).
- Upstream inlet compression packages and downstream 04-25 facility scope.
- Final disposition of methanol downstream of inlet separator boot (TBD in source).

## Requirements

### R-068-04-01 — Process duty (FACT)
The TEG package shall be a one-by-100 percent unit that dehydrates compressed sour gas at the design conditions tabulated in `Datasheet.md`. (SEC-05 / TEG Dehydration Basis.)

### R-068-04-02 — Dehydration performance (FACT)
Outlet water content shall not exceed 4 lb H2O/MMSCF. (SEC-05 table.)

### R-068-04-03 — Inlet pressure envelope (FACT)
The contactor shall be designed against the inlet pressures stated in `Datasheet.md` (low 4,502 / normal 5,378 / design 4,502 / maximum 6,205 kPag). (SEC-05 table.)

### R-068-04-04 — Contactor inlet temperature margin (FACT)
The contactor inlet temperature shall be maintained 10 to 15 deg F above the highest operating hydrate/condensation concern. (SEC-05 table.)

### R-068-04-05 — Turndown (FACT)
The contactor shall support 3:1 turndown (TBC) and the regeneration train shall support 2:1 turndown. (SEC-05 table.)

### R-068-04-06 — Contactor internals (FACT)
The contactor shall be structured-packed with at least three theoretical stages, designed at Fs not more than 3.0, and shall include inlet and outlet demisters. (SEC-05 / TEG Dehydration Basis.)

### R-068-04-07 — Contactor blowdown (FACT)
Contactor blowdown shall be automated and routed to HP flare. (SEC-05.)

### R-068-04-08 — Inlet filter coalescer (FACT)
The inlet filter coalescer shall be a one-by-100 percent unit with manual bypass and isolation, with manual blowdown at the coalescer and automated blowdown downstream of the contactor. (SEC-05 / TEG Package Equipment.)

### R-068-04-09 — Flash drum function (FACT)
The flash drum shall separate hydrocarbon vapour, water vapour, and TEG. Hydrocarbon liquids shall drain manually to the produced-water drain. Flash gas shall be pressure-regulated to the 04-25 SOC first-stage suction under the current SCA basis. (SEC-05.)

### R-068-04-10 — Rich TEG filtration (FACT)
Rich TEG filtration shall include full-flow 5 micron solids filtration and a 20 percent slipstream through carbon/particle filtration. (SEC-05.)

### R-068-04-11 — Surge drum sizing (FACT)
The surge drum shall provide 30 minutes retention at 50 psig. (SEC-05.)

### R-068-04-12 — TEG pumps (FACT)
TEG circulation shall use two-by-100 percent rotary gear or positive-displacement pumps with single mechanical seals. (SEC-05.)

### R-068-04-13 — Makeup tank (FACT)
The TEG makeup tank shall be atmospheric, fuel-gas blanketed, heated/insulated, and shall not be connected to the VRU. (SEC-05.)

### R-068-04-14 — Regeneration utility interface (FACT)
The regeneration reboiler shall be sized for LP fuel-gas firing as a listed LP fuel-gas user. Reflux/condenser arrangement shall route regeneration overhead consistent with the LP flare and regen-overhead pump arrangement. (Utility Integration Basis.)

### R-068-04-15 — Relief routing (FACT)
TEG regeneration relief shall route to the LP flare via LP KO drum V-3900-2 consistent with facility flare basis. (SEC-08 flare narrative.)

### R-068-04-16 — Source-aligned process composition (FACT)
The package shall be designed for sour-gas service consistent with the compressor composition basis (approximately 0.296 mol% H2S). Detailed materials/metallurgy selection per applicable sour-service standards is ASSUMPTION pending vendor selection. (SEC-05 / Compression Design Conditions.)

### R-068-04-17 — Integration review (PROPOSAL)
The vendor package design shall be subject to EPC Integrator integration review per `_CONTEXT.md` ResponsibleParty statement, and shall align with DEL-068-01 (EPC Scope of Work) and DEL-068-02 (EPC Package Datasheet) prior to fabrication release.

### R-068-04-18 — Maximum gas flow (TBD)
Maximum gas flow rating: TBC in source; vendor shall propose a value supported by datasheet and operating envelope and submit for EPC acceptance.

## Standards

Governing standards are not explicitly enumerated in the available source slices for this deliverable. The following are ASSUMPTION (likely applicable) pending vendor confirmation:

- ASME BPVC Section VIII Div. 1 — pressure vessels (ASSUMPTION; location TBD)
- NACE MR0175 / ISO 15156 — sour-service materials (ASSUMPTION; location TBD — H2S level cited in source)
- API 12P / 12J / 12K equivalents — equipment-specific (ASSUMPTION; location TBD)
- GPSA Engineering Data Book — TEG dehydration practice (ASSUMPTION; location TBD)
- ASME B31.3 — process piping (ASSUMPTION; location TBD)

Vendor shall confirm and list governing codes/standards in their design basis.

## Verification

| Requirement | Verification Approach |
|---|---|
| R-068-04-01..06, 08..13 | Vendor datasheet review against `Datasheet.md` source-anchored values; mechanical and process design package review by EPC Integrator. |
| R-068-04-02 (water spec) | Performance test/witnessed run with feed-gas representative of source basis; vendor performance guarantee. Specific acceptance protocol TBD. |
| R-068-04-07, 15 | Flare/relief routing review against facility flare system documentation; HAZOP closure. |
| R-068-04-09, 13, 14 | Vendor P&ID and interface drawing review against `_Sources` SEC-05 and Utility Integration Basis. |
| R-068-04-16 | Materials selection review against applicable sour-service standards; mill test reports and PMI per vendor QA plan. |
| R-068-04-17 | EPC Integrator integration review and acceptance evidence (handed to DEL-068-06). |
| R-068-04-18 | Vendor design basis submittal with proposed maximum flow and supporting calculation. |

## Documentation

Vendor shall deliver, at minimum, the following package documentation set (per `_CONTEXT.md` anticipated artifacts; specific list belongs to DEL-068-05):

- Vendor package design basis
- Vendor equipment datasheet set (per item in `Datasheet.md` Construction table)
- P&IDs, GA drawings, isometrics, mechanical/electrical/instrument typicals
- Process simulation summary and performance guarantee documentation
- Materials selection report (with sour-service basis)
- Inspection and Test Plan (ITP)
- Operating and Maintenance manuals
- Spare parts list (commissioning and 2-year operating)
- Turnover records (routed via DEL-068-05)

Full enumeration TBD pending DEL-068-02 Package Datasheet documentation matrix.
