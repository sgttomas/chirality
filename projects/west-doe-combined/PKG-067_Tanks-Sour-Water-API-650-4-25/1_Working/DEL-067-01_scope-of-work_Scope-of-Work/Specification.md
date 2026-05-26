# Specification — DEL-067-01 Scope of Work

> Normative requirements for the EPC Scope of Work deliverable for PKG-067 "Tanks, Sour Water (API 650) 4-25". Requirements are grounded in `26020-Package_Requirements.docx` (heading "26020-01-PT-19-005 - Tanks, Sour Water"), the GATE-07 PROJECT_DECOMP snapshot, and `DBM-Deepcut/4-25_Deepcut_DBM.md`. Inferred requirements are labeled `ASSUMPTION`. Missing values are `TBD`.

## Scope

### In scope

The Scope of Work shall describe, for PKG-067, all of the following at a level sufficient for EPC integration and downstream vendor handoff:

1. The package identity, tagged equipment list, and package boundary for two API 650 modified atmospheric produced-water / sour-water storage tanks supporting 4-25 service (tags `TK-9010-1`, `TK-9020-1`; source: `26020-Package_Requirements.docx` Major Included Equipment; DBM row 2627).
2. The package function within the 4-25 produced-water system: receive produced water from the inlet separator system and various drain headers; provide buffered storage; allow batched transfer to the 03-25 Liquids Hub via the produced water transfer pumps (PKG-060) and the new produced water pipeline (DBM lines 502–510, 521, 2555).
3. The source basis for the package, including the governing decomposition snapshot, the source heading in `26020-Package_Requirements.docx`, and the DBM Produced Water section.
4. Package boundaries and interfaces (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports — per PACKAGE_REGISTER row 94).
5. Whole-facility integration narrative: how this package fits with the inlet separator system, NGL water wash, mole-sieve regeneration, VRU, drain headers, and the produced water pipeline to 03-25.
6. Responsibility assignment record consistent with the package split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (PACKAGE_REGISTER row 94 governance note).

### Out of scope (for this deliverable)

- Detailed package design (covered by DEL-067-04 Vendor Engineered Equipment Package).
- Vendor document register and turnover records (covered by DEL-067-05).
- Construction tie-in workface plan (covered by DEL-067-03 Construction Work Package).
- Vendor package review and acceptance evidence (covered by DEL-067-06).
- Produced water pipeline beyond the 04-25 facility riser (designed and installed by others — DBM line 506).
- Sour-produced-water with sand/solids handling from the 03-25 Compressor Station stream (explicitly excluded — DBM line 504).

## Requirements

### R-067-01-01 — Tagged equipment list

The Scope of Work SHALL identify the two produced-water / sour-water storage tanks at expected tags `TK-9010-1` and `TK-9020-1`, with package count of two tanks for 4-25 service.
- Source: `26020-Package_Requirements.docx` paragraph 281; DBM row 2627; PACKAGE_REGISTER.csv row 94.

### R-067-01-02 — Governing standard

The Scope of Work SHALL state that the tanks are API 650 modified atmospheric tanks.
- Source: `26020-Package_Requirements.docx` paragraph 281 ("API 650 modified atmospheric"). ASSUMPTION: "modified" qualifier consistent with DBM Condensate tank specification line 1646; sour-water-specific clause text TBD.

### R-067-01-03 — Service definition

The Scope of Work SHALL identify the service as produced water that may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, and mercaptans (non-exhaustive list; TBC), with design specific gravity 1.25 (TBC).
- Source: DBM lines 508.

### R-067-01-04 — Package function and integration narrative

The Scope of Work SHALL include a narrative that describes:
- collection of produced water from the inlet separator system, NGL water-wash recycle, mole-sieve inlet coalescer, regeneration-gas scrubber, compressor stage-1 scrubber, and 300# ANSI produced-water drain header sources (DBM lines 1025, 1558, 1602, 1621, 2013);
- buffered storage of produced water at 04-25 with batch pump-out to the 03-25 Liquids Hub at ~240 m3/d (continuous average 60 m3/d) via produced water transfer pumps housed in Tank Farm Pump Building 2 (PKG-060) and the new produced-water pipeline (DBM lines 502–510, 521, 2555);
- vapour management via LP fuel gas blanket and VRU header connection where applicable (`26020-Package_Requirements.docx` paragraph 281; DBM line 1683).

### R-067-01-05 — Major included equipment and appurtenances

The Scope of Work SHALL list the tank appurtenances required by source:
- internal coating (Devchem 253 on floor, walls, and roof);
- external insulation and electric heating where required;
- PVRV (at least one per tank); EPRV sizing to be reviewed during detailed engineering;
- LP fuel gas blanket;
- VRU suction / header connection as applicable;
- Kennilworth-type hydrocarbon skim float system;
- tank instrumentation and standard tank appurtenances.
- Source: `26020-Package_Requirements.docx` paragraph 281; DBM line 524.

### R-067-01-06 — Package boundary / interface coverage

The Scope of Work SHALL identify, at the package boundary level, each interface type listed in PACKAGE_REGISTER row 94 (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), noting that detailed interface facts are carried in DEL-067-02 Package Datasheet (per DELIVERABLE_REGISTER row 529 narrative).

### R-067-01-07 — Responsibility assignment

The Scope of Work SHALL declare the responsibility split as:
- Package Vendor: package engineering, package design, vendor documentation, physical equipment package;
- EPC Integrator: integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration).
- Source: PACKAGE_REGISTER.csv row 94 governance note.

### R-067-01-08 — Source basis citation

The Scope of Work SHALL cite, at minimum:
- the GATE-07 PROJECT_DECOMP snapshot path;
- `26020-Package_Requirements.docx` heading `26020-01-PT-19-005 - Tanks, Sour Water`;
- `DBM-Deepcut/4-25_Deepcut_DBM.md` Produced Water section;
- the 3-25 analog `26020-03-PT-19-007 - Tanks, Sour Water` as a reference analog (PACKAGE_REGISTER row 94 Word Source Basis note).

### R-067-01-09 — Exclusions explicitly stated

The Scope of Work SHALL state the package-level exclusions identified by source: (a) produced water pipeline beyond the 04-25 facility riser is by others (DBM line 506); (b) sour-produced-water with sand/solids from the 03-25 Compressor Station stream is NOT included in 04-25 produced water (DBM line 504); (c) detailed sizing/specification items reserved for detailed engineering (EPRV sizing, tank isolation philosophy for potential sour vapours, capacity/dimensions) — DBM line 524; line 1714.

## Standards

| Standard | Use | Location reference |
|---|---|---|
| API 650 (modified) | Atmospheric tank governing standard | `26020-Package_Requirements.docx` paragraph 281; clause location `TBD` |
| API 2000 | Blanket gas / vacuum-breaker sizing basis (applied to condensate tanks; ASSUMPTION: applies to produced-water tanks where blanket gas is provided) | DBM line 1663 |
| NFPA 30, Tables 22.4.2.1 and 22.4.1.5 | Atmospheric tank spacing | DBM lines 268–269 |
| CSA C22.1-21 (Canadian Electrical Code) | Electrical installation basis applicable to facility electrical scope, including tank-related electrical | DBM lines 2866, 3410 |
| Facility regulatory authorities (CSA, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER) | Project-level applicable bodies | DBM line 2866 |
| BCER Determination 100120203 | Permitting basis for the 03-25 liquids hub; amendments noted as required for sour water treating | DBM line 133 |

## Verification

| Requirement | Verification method |
|---|---|
| R-067-01-01 (Tags) | Tag list in SOW matches `26020-Package_Requirements.docx` paragraph 281 and DBM row 2627. |
| R-067-01-02 (API 650) | Standard explicitly cited in SOW with `TBD` clause location flagged. |
| R-067-01-03 (Service) | Service text matches DBM line 508 verbatim (non-exhaustive composition; SG 1.25 (TBC)). |
| R-067-01-04 (Integration narrative) | Narrative references inlet separator, NGL water wash, mole-sieve, regeneration gas scrubber, drain headers, VRU, produced-water transfer pumps (PKG-060), produced-water pipeline, 03-25 Liquids Hub. |
| R-067-01-05 (Appurtenances) | Appurtenance list matches `26020-Package_Requirements.docx` paragraph 281 plus DBM line 524 items. |
| R-067-01-06 (Interfaces) | Each interface type from PACKAGE_REGISTER row 94 appears once in the SOW boundary section. |
| R-067-01-07 (Responsibility) | Responsibility paragraph reproduces the PACKAGE_REGISTER row 94 governance note. |
| R-067-01-08 (Sources) | Cited references resolvable to existing local files in `_REFERENCES.md`. |
| R-067-01-09 (Exclusions) | Exclusion bullets present and tagged to source citations. |

## Documentation

The Scope of Work produced under this deliverable shall result in:
- Package scope of work narrative (the principal artifact).
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record.

Source: `DELIVERABLE_REGISTER.csv` row 528 Anticipated Artifacts; `_CONTEXT.md` Anticipated Artifacts.
