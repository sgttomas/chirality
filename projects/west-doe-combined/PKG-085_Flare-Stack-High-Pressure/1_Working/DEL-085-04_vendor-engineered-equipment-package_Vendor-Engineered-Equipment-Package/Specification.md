# Specification — DEL-085-04 Vendor Engineered Equipment Package (Flare Stack, High Pressure)

## Scope

This specification governs the Package Vendor production unit for the high-pressure flare stack package at PKG-085, including vendor engineering, design, fabrication/supply, and the physical equipment package developed from the EPC Scope of Work (`DEL-085-01`) and EPC Package Datasheet (`DEL-085-02`) (source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv).

In scope:
- Vendor-developed package engineering and design that satisfies EPC SOW and Package Datasheet requirements for the HP flare stack and its KO/relief receivers as identified in source basis.
- Fabrication, supply, and physical assembly of the engineered vendor package, including bulks, instrumentation/controls, mechanical, structural, and other discipline content within the vendor's defined battery limits.
- Vendor design basis and vendor datasheet set covering the vendor-supplied equipment (source: `_CONTEXT.md` anticipated artifacts).
- EPC Integrator integration review participation by the Package Vendor.

Out of scope (handled by sibling deliverables in PKG-085):
- EPC Scope of Work definition (`DEL-085-01`).
- EPC Package Datasheet (`DEL-085-02`).
- Construction Work Package — install/tie-in/turnover planning (`DEL-085-03`).
- Vendor Document Turnover Package (`DEL-085-05`).
- EPC Vendor Package Review and Acceptance (`DEL-085-06`).

## Requirements

### REQ-085-04-01 — Source-derived design basis
The vendor engineered package SHALL be developed from the EPC SOW (`DEL-085-01`) and EPC Package Datasheet (`DEL-085-02`) inputs (source: `_CONTEXT.md` scope statement; DELIVERABLE_REGISTER.csv).

### REQ-085-04-02 — HP flare service
The vendor package SHALL provide HP relief/blowdown disposal capability consistent with the HP flare service identified in the source basis (source: 3-25 DBM, Flare and Blowdown section; 4-25 Deepcut DBM HP-flare interface statements).

### REQ-085-04-03 — Stack configuration (current source basis, ASSUMPTION pending vendor confirmation)
The HP/Cryo flare stack configuration is currently stated as sonic, 660 mm OD by 60,957 mm tall (source: 3-25 DBM Flare and Blowdown). Final vendor configuration SHALL be reconciled with final flare studies (source: 3-25 DBM Plant Information Summary, "blowdown and relief basis require final flare studies"). Loads, materials, and dimensional confirmation: TBD.

### REQ-085-04-04 — HP relief header interface (current source basis)
The HP relief header at the package interface is currently sized at 508 mm (20 in) (source: 3-25 DBM Flare and Blowdown). Vendor SHALL coordinate connection sizing and orientation against the EPC Package Datasheet.

### REQ-085-04-05 — KO drum and pump arrangement (current source basis)
The HP flare service includes two HP KO drums (V-4100-2 in the compressor area; V-4150-2 in the tank farm) manifolding to the HP flare, each with one 100% transfer pump (P-4100-2; P-4150-2) discharging to truck-out or slop (source: 3-25 DBM Flare and Blowdown; Equipment Count table). Vendor SHALL deliver vendor-scope items consistent with this arrangement; final vendor scope split: TBD against `DEL-085-02`.

### REQ-085-04-06 — Thermal radiation limits
The flare installation SHALL satisfy:
- ≤ 9 kW/m² inside the boundary blackened area, and
- ≤ 5 kW/m² outside the boundary
(source: 4-25 Deepcut DBM Flare and Incinerator Spacing, citing OGPFR Appendix 1, Schedule 1, Sec. 2 — external regulatory reference; clause text not locally accessible (location TBD)).

### REQ-085-04-07 — Spacing limits
The package layout-relevant deliverables SHALL respect the spacing limits stated in 4-25 Deepcut DBM Flare and Incinerator Spacing:
- 25 m flare-to-nearest-plant-equipment;
- 80 m flare-to-public-road/property-line;
- 50 m flare-to-atmospheric condensate tanks;
- 25 m flare-to-separators/atmospheric produced-water tanks;
- 30.48 m flare-to-pressurized bullets (per API 2510 — external reference; location TBD);
- 10 m flare KO tanks-to-vegetation/fire hazards;
- 25 m fired heater-to-flare/incinerator
(source: 4-25 Deepcut DBM Flare and Incinerator Spacing).

### REQ-085-04-08 — Environmental and structural design basis
Vendor mechanical and structural design SHALL satisfy snow, wind, seismic, frost, vibration, settlement, and maintenance access loads consistent with the site civil/structural basis; flare/stack elements are explicitly within scope of the foundation discipline check (source: 3-25 DBM Foundations).

### REQ-085-04-09 — Detection at the package boundary
LEL, H2S, methyl mercaptan, and fire detection at flare/vent interfaces of the vendor package SHALL be coordinated with the project detection design; final counts, tags, set points, voting logic, placement, and calibration are TBD pending detailed design and safety studies (source: 3-25 DBM Detection narrative).

### REQ-085-04-10 — Cross-facility coordination
The HP/Cryo and LP dual flare stack is a shared 03-25 / 04-25 system; vendor package boundaries SHALL be reconciled with the current 03-25/04-25 allocation, and any unresolved service split or owner interface SHALL be carried as an open interface item (source: 3-25 DBM Utilities narrative).

### REQ-085-04-11 — Vendor scope boundaries (TBD)
The exact mechanical/structural/instrument/electrical/insulation/coating supply split between Vendor and EPC scope: TBD — defined by EPC SOW (`DEL-085-01`) and Package Datasheet (`DEL-085-02`).

### REQ-085-04-12 — Anticipated artifacts
The vendor package SHALL produce: (a) vendor engineered physical equipment package, and (b) vendor package design basis and datasheet set (source: `_CONTEXT.md` anticipated artifacts).

## Standards

| Standard / Regulation | Applicability | Location |
|---|---|---|
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Flare thermal radiation flux limits | External regulatory; location TBD (cited by 4-25 Deepcut DBM) |
| OGAOM Sec. 9.6.15 | Flare and incinerator spacing | External regulatory; location TBD (cited by 4-25 Deepcut DBM) |
| API 2510 | Spacing flare-to-pressurized bullets | External industry standard; location TBD (cited by 4-25 Deepcut DBM) |
| Project Design Basis Memoranda | Project-wide design basis (utilities, spacing, foundations, detection) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Vendor-applicable codes for flare stacks (e.g., API 521, API 537) | ASSUMPTION: likely applicable; not explicitly cited in accessible sources | location TBD |

## Verification

| Requirement | Verification Approach | Records |
|---|---|---|
| REQ-085-04-01 | Cross-check of vendor design basis against EPC SOW and Package Datasheet | EPC review log (DEL-085-06) |
| REQ-085-04-02..05 | Vendor datasheet review against 3-25 DBM Flare and Blowdown source values; reconciliation report against final flare studies | Vendor design basis; flare study report (TBD) |
| REQ-085-04-06, REQ-085-04-07 | Layout check of as-built positions against thermal-radiation flux model and spacing table | Thermal radiation model report; layout drawings |
| REQ-085-04-08 | Discipline civil/structural calculations referencing final geotechnical report | Foundation/anchorage calculations |
| REQ-085-04-09 | Detection design review and FAT/SAT records | Detection tag list; FAT/SAT records |
| REQ-085-04-10 | Interface register and open-issues log against 03-25/04-25 shared-system allocation | INTERFACE_REGISTER.csv updates; interface ruling records |
| REQ-085-04-11 | Vendor scope-split confirmation matrix against EPC SOW and Package Datasheet | Scope-split matrix |
| REQ-085-04-12 | Document register check that both anticipated artifacts are issued | Vendor document register (DEL-085-05) |

## Documentation

- Vendor engineered physical equipment package (anticipated artifact).
- Vendor package design basis and vendor datasheet set (anticipated artifact).
- Vendor calculations supporting REQ-085-04-02 through REQ-085-04-08 (TBD against vendor document register).
- Interface and integration evidence to support EPC Vendor Package Review and Acceptance (`DEL-085-06`).
