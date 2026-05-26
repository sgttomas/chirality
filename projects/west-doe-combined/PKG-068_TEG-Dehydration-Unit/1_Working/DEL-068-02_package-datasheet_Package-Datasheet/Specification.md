# Specification — PKG-068 TEG Dehydration Unit (Package Datasheet)

## Scope

### Covered
- Normative requirements applicable to the EPC Integrator's Package Datasheet handoff for `PKG-068` TEG Dehydration Unit.
- Process, mechanical, performance, and interface requirements that the Package Vendor must satisfy in package engineering, design, vendor documentation, and physical equipment supply.
- Interface requirements that the EPC Integrator must execute to integrate `PKG-068` into the 04-25 Deepcut facility.

### Excluded
- Detailed vendor engineering deliverables (covered by `DEL-068-04` Vendor Engineered Equipment Package).
- Vendor document turnover content (covered by `DEL-068-05`).
- Construction work package planning (covered by `DEL-068-03`).
- EPC review and acceptance (covered by `DEL-068-06`).
- Package scope of work narrative (covered by `DEL-068-01`).
- Workbook package responsibility note states "TBD; no package-specific exclusions stated in source materials" (`PACKAGE_REGISTER.csv`). No additional package-specific exclusions are claimed here.

## Requirements

### Process performance requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-068-02-001 | The TEG contactor shall achieve outlet water content <= 4 lb H2O / MMSCF at defined contactor inlet conditions (43 degC summer / 35 degC winter, fully water-saturated). | `4-25_Deepcut_DBM.md` SEC-06 TEG Design Values |
| REQ-068-02-002 | The TEG unit shall accept design inlet flows of 329.2 MMSCFD summer / 335 MMSCFD winter (excluding regen gas) with maximum total contactor flow of 354.2 / 360 MMSCFD respectively when 25 MMSCFD recycled regeneration gas is present. | same |
| REQ-068-02-003 | The TEG unit shall accommodate 3:1 inlet-gas turndown on the contactor (TBC) and 2:1 turndown on TEG regeneration circulation. | same |
| REQ-068-02-004 | Regenerated lean TEG purity shall meet design 99.80 wt% at 45.0 USGPM circulation, 136.4 SCFM stripping gas, 395 degF reboiler, 3.25 psig reboiler pressure, producing <3 lb H2O / MMSCF outlet (alternate expected: 99.74 wt% at 44.3 USGPM, 111.8 SCFM, <4 lb H2O/MMSCF). | same |
| REQ-068-02-005 | Operating pressure basis is 1100 psig / 7584 kPag pending confirmation; the unresolved 1085 psig alternate shall be reconciled in detailed engineering before pressure-containing-equipment design is finalized. | same; TBC |
| REQ-068-02-006 | The package shall deliver dehydrated gas to the downstream Inlet/TEG Dehydration Cross-Exchanger and molecular-sieve dehydration unit consistent with 10 lb H2O / MMSCF mol-sieve tolerance. | same |

### Mechanical and equipment requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-068-02-010 | Equipment scope shall include, at minimum: Inlet Air Cooler, Filter Coalescer, TEG Contactor, Glycol Flash Tank, Glycol Reboiler/Still Column, Glycol Circulation Pumps, Glycol Particulate Filters, Glycol Charcoal Filter, Gas/Glycol Exchanger, Air/Glycol Exchanger, Fuel Gas Scrubber, TEG Make-up Tank, Burner Control Panel. | `PACKAGE_REGISTER.csv` Scope column |
| REQ-068-02-011 | TEG inlet cooler shall include automatic warm-air recirculation, automated side-air and recirculation louvers, electric or heat-medium plenum heater, and 125% total excess surface area (including allowance for amine carryover sensible heat). | `4-25_Deepcut_DBM.md` SEC-06 TEG Equipment |
| REQ-068-02-012 | TEG contactor shall use structured packing providing ≥3 theoretical stages with FS ≤3.0 at design conditions, inlet and outlet mesh/vane vertical-flow demisters, and automated outlet blowdown to HP flare. Contactor sparing configuration (1 x 100% vs 2 x 50%) is TBD and shall be confirmed by the EPC Integrator before vendor design freeze. | same; SEC-06 TEG Open Items |
| REQ-068-02-013 | TEG flash drum shall be a three-phase separator operating at 60 psig with overhead flash-gas pressure such that gas can flow to the stabilizer overheads compressor first-stage suction (~50 psig). Flash gas basis is 1 SCF per USG circulating TEG. | same |
| REQ-068-02-014 | Lean/rich TEG exchanger shall be a bloc-welded plate exchanger (1 x 100%, no polymer gaskets, bolted cover for cleaning). Exchanger type and sparing are TBC during detailed engineering. ASSUMPTION: bloc-welded plate type is preferred-basis only and may be revised. | same |
| REQ-068-02-015 | TEG reboiler shall be heat-medium-fired with 425 degF supply via mixing valves; reboiler operating temperature 395 degF; reboiler pressure 3.25 psig. ASSUMPTION: workbook "Burner Control Panel" line item is interpreted as the reboiler-fired-equipment control system; configuration (direct-fired vs heat-medium fired) shall be confirmed. | `4-25_Deepcut_DBM.md` SEC-06; SEC-09 |
| REQ-068-02-016 | Still overheads shall be cooled, partially condensed, and recovered to the VRU suction header at normal backpressure ~<0.5 psig; still overheads separator shall include a demister with 5 min retention (LAL→LAH) and 2 x 100% bottoms pumps with auto-start on high level. | `4-25_Deepcut_DBM.md` SEC-06 |
| REQ-068-02-017 | TEG circulation pumps shall be 2 x 100% motor-driven positive-displacement rotary-vane pumps with single mechanical seals. | same |
| REQ-068-02-018 | TEG surge tank shall provide 30 min retention at design TEG circulation rate and design pressure 50 psig; TEG make-up shall be via manual operator activity. | same |
| REQ-068-02-019 | TEG filtration shall include a full-flow rich-TEG particle filter at nominal 5 micron and a 20% rich-TEG slipstream through charcoal/carbon plus 5 micron filtration; manual LP fuel-gas purge shall precede opening sour service. | same |
| REQ-068-02-020 | TEG make-up storage shall be an atmospheric heated and insulated storage tank with fuel-gas blanket and no VRU connection; a transfer pump shall feed make-up TEG to the TEG surge tank. | same |
| REQ-068-02-021 | Equipment expected to contain liquid TEG for maintenance draining shall include thermal PSVs where the equipment can be 100% full of TEG; flange rating 300# ANSI for TEG drain service (TBC); thermal PSV outlets shall route by separate line to the produced-water drain header. | `4-25_Deepcut_DBM.md` SEC-06 drainage table |

### Utility and interface requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-068-02-030 | TEG stripping gas shall be LP fuel gas regulated to 5 psig; design supply 0.30 MMSCFD; flow cases per Datasheet conditions. | `4-25_Deepcut_DBM.md` SEC-06; SEC-08 utility table |
| REQ-068-02-031 | Heat-medium supply to the TEG reboiler shall be 425 degF per single-loop heat-medium basis. | `4-25_Deepcut_DBM.md` SEC-09 |
| REQ-068-02-032 | Flare/blowdown routing: TEG contactor automated outlet blowdown shall route to HP flare; TEG flash-drum automated low-pressure blowdown shall route to LP flare. | `4-25_Deepcut_DBM.md` SEC-06 |
| REQ-068-02-033 | Still emissions shall be recovered to VRU suction; the TEG make-up tank shall NOT be connected to VRU. | `4-25_Deepcut_DBM.md` SEC-06; SEC-08 VRU notes |
| REQ-068-02-034 | The package shall expose tie-in points, terminations, and design data sufficient for the EPC Integrator to execute the 13 interfaces enumerated in the Datasheet (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports). | `INTERFACE_REGISTER.csv` PKG-068 rows |
| REQ-068-02-035 | Package and EPC scope split shall follow the responsibility model: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` Responsibility Model; `OBJ-004` |

### Open / TBD requirements

| Req ID | Item | Disposition |
|---|---|---|
| REQ-068-02-090 | Operating pressure (1100 vs 1085 psig basis) | TBC — detailed engineering |
| REQ-068-02-091 | Contactor sparing (1 x 100% vs 2 x 50%) | TBD |
| REQ-068-02-092 | Lean/rich exchanger type and sparing | TBC |
| REQ-068-02-093 | Reboiler fired configuration (direct-fired burner vs heat-medium fired) | TBC — ASSUMPTION currently heat-medium fired per DBM |
| REQ-068-02-094 | Material selection (sour-service grades, methyl mercaptan exposure on TEG carbon filter location) | TBD |
| REQ-068-02-095 | Ambient design conditions specific to TEG package | TBD — location in DBM not cited in this pass |
| REQ-068-02-096 | Flash-drum pneumatic level-controller float SG | TBC |
| REQ-068-02-097 | TEG carbon-filter location for methyl mercaptan risk | TBC |
| REQ-068-02-098 | Regeneration hydraulics, condenser-failure dilution gas, preheat coil details | TBC |
| REQ-068-02-099 | Low total-flow cases and start-up/low-pressure water content | TBC |

## Standards

| Standard / Code Domain | Applicable Item | Location |
|---|---|---|
| Sour-service material and design discipline | Equipment in sour-origin gas service | `4-25_Deepcut_DBM.md` SEC-15 Regulatory, Codes, and Standards Basis (referenced via `OBJ-009`); specific clause TBD — location TBD |
| Flange rating standard | 300# ANSI on TEG drain service | `4-25_Deepcut_DBM.md` SEC-06 drainage table; ANSI standard reference TBD |
| Insulation specification | Hot/cold insulation including glycol tracing | `4-25_Deepcut_DBM.md` insulation reference; specific standard / spec number TBD |
| Vendor document standards | Vendor-document turnover content | `26020-Package_Requirements.docx` vendor-document tables — location TBD (binary source, not text-readable this pass) |
| API / mechanical equipment standards | Pumps, vessels, exchangers | TBD — facility mechanical specifications not enumerated in TEG section of DBM |

ASSUMPTION: Specific code/standard clause citations require the `26020-Package_Requirements.docx` content (binary; not readable in this pass) and SEC-15 of the DBM. These are deferred as `location TBD`.

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-068-02-001, -004 | Vendor performance test data; site performance test against contactor outlet water spec and lean-TEG purity at design circulation/stripping gas rates |
| REQ-068-02-002, -003 | Vendor process datasheet sign-off; turndown demonstration at FAT and during commissioning |
| REQ-068-02-005, -090 | EPC pressure basis reconciliation memo before vendor design freeze; vessel/equipment pressure ratings sized for the confirmed basis |
| REQ-068-02-006 | Outlet gas water-content sample at unit boundary; mol-sieve unit inlet sampling consistency check |
| REQ-068-02-010 through -021 | Vendor package datasheets, GA drawings, P&IDs, equipment lists; EPC review against this Specification |
| REQ-068-02-030 through -033 | Utility tie-in walkdown; flare/blowdown routing P&ID review against HP/LP flare basis; VRU header routing P&ID review |
| REQ-068-02-034 | EPC interface register sign-off per `INTERFACE_REGISTER.csv` rows; interface drawing turnover |
| REQ-068-02-035 | Contract responsibility matrix sign-off (EPC + Vendor); DEL-068-06 EPC review and acceptance |
| REQ-068-02-090 through -099 | Tracked in Conflict Table (Guidance.md); each item closed by human ruling or detailed-engineering deliverable before package issue-for-construction |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`) and corresponding documentation deliverables for this Package Datasheet:

| Artifact | Coverage |
|---|---|
| Package technical datasheet (ART-355EBDBAD7) | This deliverable's `Datasheet.md` and `Specification.md` |
| Vendor engineering handoff basis (ART-CCC3AE418E) | Datasheet identification, attributes, conditions, construction; Specification requirements |
| Package interface requirements matrix (ART-7CE5313EC5) | Datasheet — Package interface requirements table; this Specification REQ-068-02-034 |
| Source-supported equipment and design criteria | Datasheet attributes/conditions/construction tables with source citations |
| Per-interface evidence artifacts (ART-F80D7E8B07 through ART-8FA1EBAE68 etc.) | Carried as Datasheet interface table rows per `_CONTEXT.md` Notes |

Required downstream documentation (not produced here):
- Vendor process datasheet (`DEL-068-04`)
- Vendor document turnover register (`DEL-068-05`)
- Construction work package (`DEL-068-03`)
- EPC vendor package review and acceptance record (`DEL-068-06`)
