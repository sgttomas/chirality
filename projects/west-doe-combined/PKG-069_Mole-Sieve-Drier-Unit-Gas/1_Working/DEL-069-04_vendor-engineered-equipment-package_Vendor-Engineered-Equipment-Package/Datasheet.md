# Datasheet — DEL-069-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, Gas)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-069-04_vendor-engineered-equipment-package | _CONTEXT.md |
| Name | Vendor Engineered Equipment Package | _CONTEXT.md |
| ParentPackageID | PKG-069 | _CONTEXT.md |
| Package Name | Mole Sieve Drier Unit (Gas) | _CONTEXT.md |
| Discipline | Mechanical | _CONTEXT.md |
| Type | Vendor Package Production Unit | _CONTEXT.md |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | _CONTEXT.md |
| Covers Scope Items | SOW-0144 | _CONTEXT.md |
| Source Reference | Workbook Packages row 73; 4-25 Deepcut DBM, SEC-06 "Molecular-Sieve Dehydration and Mercury Removal Basis" | _CONTEXT.md; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 |

## Attributes (Process-Gas Molecular-Sieve Dehydration Service)

| Attribute | Value | Source |
|---|---|---|
| Service | Final dehydration of high-pressure sweet, TEG-dehydrated process gas upstream of cryogenic recovery | 4-25 Deepcut DBM SEC-06 / Process Description |
| Adsorbent | 3A molecular sieve (mandatory); 4A and 5A prohibited (avoid H2S adsorption / sulphur spikes in regeneration loop). Protective silica gel layer for upstream liquid carryover | 4-25 Deepcut DBM SEC-06 / Bed and Regeneration Basis |
| Configuration | Three driers; two in adsorption, one in standby / regeneration / cooling; downflow adsorption | 4-25 Deepcut DBM SEC-06 / Bed and Regeneration Basis |
| Adsorbent life | Typical 3 years (TBC by vendor); 5-year extension under review for turnaround alignment | 4-25 Deepcut DBM SEC-06 |
| Bed sizing (basis) | 9.5 ft inner diameter bed basis; regeneration tower vertical 8 ft x 20 ft | 4-25 Deepcut DBM SEC-06 |
| Inlet filter/coalescers | 2 x 100% (one operating, one standby); 328 MMSCFD HP dehydrated-gas basis; clean dP < 2 psid; level dumps to slop tank header | 4-25 Deepcut DBM SEC-06 / Equipment, Controls, and Protection |
| Mercury removal unit (MRU) | 1 x 100% (space for one future); sulphur-impregnated activated carbon; guaranteed media life >= 6 years; inlet ~100 ug Hg/Nm3; outlet <= 0.01 ug Hg/Nm3; end-of-life dP < 6 psi | 4-25 Deepcut DBM SEC-06 |
| Dust filters | Molecular-sieve dust filter and MRU dust filter each 1 x 100%; capacity = main + regen gas; clean dP 2 psid; manual bypass for online change-out | 4-25 Deepcut DBM SEC-06 |
| Regeneration gas compressor | Single-stage vertical inline centrifugal; 25 MMSCFD basis; 2 x 100% installed standby; assumed dP 100 psid (loop table 79.5 psid; final TBC) | 4-25 Deepcut DBM SEC-06 |
| Regeneration gas heater | BEU heat-medium/process-gas shell-and-tube; target regen temperature 450-460 degF (basis unresolved between 450 system overview and 460 heater detail) | 4-25 Deepcut DBM SEC-06 |
| Regeneration gas cooler | Aerial cooler to 110 degF; maintain >= 15 degF above HC dewpoint/hydrate point; automated warm-air recirculation, louvers, split header | 4-25 Deepcut DBM SEC-06 |
| Regeneration gas scrubber | Two-phase, mist pad; separated water gap-level to produced-water drain; drain capacity for peak release TBC; installed indoors | 4-25 Deepcut DBM SEC-06 |
| Regeneration recycle return | Normally upstream of TEG inlet coalescer; NC alternate path immediately upstream of mole-sieve coalescers | 4-25 Deepcut DBM SEC-06 |
| Blowdown | Operator-initiated HMI only; not part of plant ESD blowdown; two blowdown valves (regen and adsorption loops); rate limit 50 psi/min at max inlet pressure; regen compressor bypass to prevent reverse rotation | 4-25 Deepcut DBM SEC-06 |
| Dry-out header | LP dry sales-gas recycle for cryogenic dry-out; assumed initial operating pressure ~250 psig (TBC); header MAWP TBC | 4-25 Deepcut DBM SEC-06 |
| Flange rating (mole-sieve system) | 900# (cryogenic basis 600# at 200 degF elsewhere) | 4-25 Deepcut DBM, line note re mole-sieve flange rating |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Installation | Outdoor multilevel mole-sieve module adjacent to cryogenic modules; inlet filter/coalescers on independent module/building | 4-25 Deepcut DBM SEC-06 / Design Values |
| Inlet capacity | Sized from TEG contactor outflow minus TEG water removal; bed capacity table 332.6 MMSCFD adsorption + 25.45 MMSCFD regeneration | 4-25 Deepcut DBM SEC-06 |
| Normal inlet pressure | 1078 psig (TBC during detailed engineering) | 4-25 Deepcut DBM SEC-06 |
| Inlet temperature | Summer 40.6 degC (105 degF); Winter 16 degC (61 degF) — subject to final plant inlet temperature estimates | 4-25 Deepcut DBM SEC-06 |
| Inlet water content | Expected <= 4 lb H2O/MMSCF at 333 MMSCFD; design 10 lb H2O/MMSCF at 333 MMSCFD | 4-25 Deepcut DBM SEC-06 |
| Outlet water content | Expected < 0.1 ppmv H2O and dewpoint < -90 degC; maximum < 1 ppmv H2O and dewpoint -75 degC; required value TBD | 4-25 Deepcut DBM SEC-06 |
| Cryogenic water-dewpoint limit | < -75 degC at highest operating pressure (to prevent continuous freezing) | 4-25 Deepcut DBM SEC-06 |
| Adsorption turndown | 2:1; further turndown via single-bed adsorption (risk of channeling / premature breakthrough at excessive reduction) | 4-25 Deepcut DBM SEC-06 |
| BAHX downstream temperature limit | New-bed online gas temperature must not exceed 66 degC (downstream BAHX design temperature); exceedance trips facility | 4-25 Deepcut DBM SEC-06 |
| Per-bed flow basis | Bed 1 adsorption 166.3 MMSCFD; Bed 2 adsorption 166.3 MMSCFD; Bed 3 regen/cooling 25.45 MMSCFD | 4-25 Deepcut DBM SEC-06 |
| Preliminary cycle times | Adsorption 54 h; heating ramp 0.2 h; regen pre-heat/hold 1 h; heating ramp 0.4 h; heating 3 h; cooling 3 h; standby 38.8 h preliminary; total regen cycle 7.6 h | 4-25 Deepcut DBM SEC-06 |
| Standby constraint | Minimum 12 h standby per tower at 4 lb H2O adsorbed loading | 4-25 Deepcut DBM SEC-06 |
| Bed pressure drop | Start-of-life < 4 psid; end-of-life (incl. nozzles) < 10 psid | 4-25 Deepcut DBM SEC-06 |
| Thermal efficiency target | Mole-sieve regeneration thermal efficiency target < 40% | 4-25 Deepcut DBM SEC-06 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Modularization | Multilevel outdoor module (mole-sieve equipment); independent module/building for inlet filter/coalescers | 4-25 Deepcut DBM SEC-06 |
| Vessel orientation | Vertical adsorbers; downflow adsorption | 4-25 Deepcut DBM SEC-06 |
| Flange class | 900# system (mole-sieve scope) | 4-25 Deepcut DBM (cryogenic/mol-sieve flange-rating note) |
| Regeneration cooler | Aerial cooler with automated warm-air recirculation and intake louvers; split-header design | 4-25 Deepcut DBM SEC-06 |
| Regen scrubber location | Inside building | 4-25 Deepcut DBM SEC-06 |
| Filter housings | Bag-filter / cartridge style, 2 x 100% with manual bypass; specific construction details TBD by vendor | 4-25 Deepcut DBM SEC-06 (general); vendor-defined details TBD |
| Materials of construction | Per vendor selection compatible with sweet dry process gas, regeneration thermal cycling, and mercury-bearing service ahead of MRU | TBD (vendor) |

## Anticipated Artifacts (Vendor Deliverables)

| Artifact | Notes | Source |
|---|---|---|
| Vendor engineered physical equipment package | Adsorbers, internals, valves, piping, instrumentation, skid steel, regeneration heater/cooler/scrubber/compressor, dust filters, MRU as scoped | _CONTEXT.md / decomposition narrative |
| Vendor package design basis | Document set capturing vendor design assumptions, calculations, vendor specifications | _CONTEXT.md |
| Vendor package datasheet set | Equipment-level datasheets for adsorbers, regen package equipment, filters, MRU, instrumentation | _CONTEXT.md |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- Accepted upstream decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-06 Molecular-Sieve Dehydration and Mercury Removal Basis (authoritative source slice)
- Workbook Packages row 73 — location TBD (binary xlsx not extracted for this deliverable)
- 26020-Package_Requirements.docx — location TBD (binary not extracted)
