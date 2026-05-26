# Specification — DEL-069-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, Gas)

## Scope

### Included
- Vendor engineering, design, supply, and fabrication of the process-gas molecular-sieve dehydration package for PKG-069 "Mole Sieve Drier Unit (Gas)" serving the 04-25 Deepcut facility, including adsorbers, internals, instrumentation, piping, regeneration system (compressor, heater, cooler, scrubber), inlet filter/coalescers, dust filters (mole-sieve and MRU), and the Mercury Recovery Unit, sized and arranged consistent with 4-25 Deepcut DBM SEC-06.
- Vendor package design basis and vendor datasheet set as deliverable artifacts (per `_CONTEXT.md`).
- Integration data needed by the EPC Integrator for tie-in to upstream TEG dehydration outlet and downstream UltraTEF cryogenic unit (per SEC-06 process configuration).

### Excluded
- EPC Integrator deliverables: EPC Scope of Work (DEL-069-01), Package Datasheet (DEL-069-02), Construction Work Package (DEL-069-03), Vendor Document Turnover Package (DEL-069-05), and EPC Vendor Package Review and Acceptance (DEL-069-06). Source: GATE-07 deliverable register, PKG-069 entries.
- Upstream amine, TEG dehydration, and downstream UltraTEF cryogenic recovery scopes (covered by other PKGs / sections of SEC-06).
- Sales-gas dry-out header MAWP confirmation (carried as TBC in source basis; resolution is an EPC/Integrator action, not vendor scope, unless agreed otherwise).

## Requirements

### R-1 Adsorbent Selection
3A molecular sieve SHALL be used as the adsorbent. 4A and 5A molecular sieves SHALL NOT be used because larger pore sizes can adsorb H2S and cause sulphur spikes in the regeneration return loop. A silica-gel protective layer SHALL be included to protect the bed against upstream liquid carryover.
Source: 4-25 Deepcut DBM SEC-06 / Bed and Regeneration Basis.

### R-2 Configuration and Operating Mode
The unit SHALL provide three adsorber vessels with two beds in adsorption and one in standby / regeneration / cooling. Gas SHALL enter the adsorption beds in downflow configuration.
Source: 4-25 Deepcut DBM SEC-06.

### R-3 Outlet Water Content
The unit SHALL achieve outlet water content compatible with cryogenic service. Expected outlet < 0.1 ppmv H2O and dewpoint < -90 degC; design maximum < 1 ppmv H2O and dewpoint -75 degC. The cryogenic water dewpoint SHALL be < -75 degC at highest operating pressure. The contractually required outlet value is **TBD** pending owner direction.
Source: 4-25 Deepcut DBM SEC-06.

### R-4 Inlet Conditions (Design Basis)
The package SHALL be designed for: normal inlet pressure 1078 psig (TBC); inlet temperature 40.6 degC summer / 16 degC winter (TBC against final plant inlet estimates); design inlet water content 10 lb H2O/MMSCF at 333 MMSCFD (expected <= 4 lb H2O/MMSCF).
Source: 4-25 Deepcut DBM SEC-06.

### R-5 Bed Sizing and Cycle
Bed sizing basis SHALL be 9.5 ft ID; regeneration tower 8 ft x 20 ft vertical. Preliminary cycle times: adsorption 54 h; heating ramp 0.2 h; regen pre-heat/hold 1 h; heating ramp 0.4 h; heating 3 h; cooling 3 h; standby 38.8 h; total regen cycle 7.6 h. Minimum 12 h standby per tower at 4 lb H2O adsorbed loading SHALL be respected.
Source: 4-25 Deepcut DBM SEC-06.

### R-6 Pressure Drop
Start-of-life bed pressure drop SHALL be < 4 psid. End-of-life pressure drop including vessel nozzles SHALL be < 10 psid.
Source: 4-25 Deepcut DBM SEC-06.

### R-7 BAHX Protection
When a new bed is brought online, outlet gas temperature SHALL NOT exceed 66 degC (downstream BAHX design temperature); exceedance SHALL initiate facility shutdown.
Source: 4-25 Deepcut DBM SEC-06.

### R-8 Inlet Filter/Coalescers
The package SHALL include 2 x 100% inlet filter/coalescers sized for 328 MMSCFD high-pressure dehydrated-gas basis; clean dP < 2 psid; blowdown valves per separator; level dumps to slop tank header. Bulk free liquids at inlet are not assumed; upset carryover from upstream TEG is to be accommodated.
Source: 4-25 Deepcut DBM SEC-06.

### R-9 Regeneration System
Regeneration gas compressor SHALL be a single-stage vertical inline centrifugal machine, 25 MMSCFD basis, 2 x 100% installed standby. Regeneration gas heater SHALL be BEU shell-and-tube using heat medium. Regeneration gas cooler SHALL be an aerial cooler condensing desorbed water, cooled to 110 degF at design conditions while maintaining >= 15 degF above HC dewpoint / hydrate point, with automated warm-air recirculation, intake louvers, and split-header design. Regeneration gas scrubber SHALL be a two-phase vessel with mist pad, indoor installation; separated water gap-level controlled to the produced-water drain system. Assumed compressor design differential is 100 psid; loop-table value is 79.5 psid; final value TBC.
The regeneration heater set-point basis is unresolved between 450 degF (system overview) and 460 degF (heater detail); the vendor SHALL flag and resolve this conflict in the package design basis (see `Guidance.md` Conflict Table).
Source: 4-25 Deepcut DBM SEC-06.

### R-10 Recycle Return
Saturated regeneration gas SHALL normally return upstream of the TEG inlet coalescer. An alternate normally-closed path SHALL be provided to permit return immediately upstream of the molecular-sieve coalescers.
Source: 4-25 Deepcut DBM SEC-06.

### R-11 Blowdown and Reverse-Rotation Protection
Blowdown SHALL be operator-initiated via HMI only and SHALL NOT participate in automatic plant blowdown. Two blowdown valves SHALL be provided (regeneration loop and adsorption loop). Blowdown rate SHALL be limited to 50 psi/min at maximum inlet pressure. A regeneration-compressor bypass SHALL prevent reverse rotation.
Source: 4-25 Deepcut DBM SEC-06.

### R-12 Mercury Recovery Unit
The MRU SHALL be 1 x 100% with provision (reserved space) for one additional future MRU vessel. Media SHALL be sulphur-impregnated activated carbon with guaranteed life >= 6 years. Allowable inlet mercury approximately 100 ug Hg/Nm3; required outlet mercury <= 0.01 ug Hg/Nm3; end-of-life dP < 6 psi.
Source: 4-25 Deepcut DBM SEC-06.

### R-13 Dust Filters
Molecular-sieve dust filter and MRU dust filter SHALL each be 1 x 100%, sized for main + regeneration gas flow, with clean dP 2 psid and manual bypass to permit online filter change-out.
Source: 4-25 Deepcut DBM SEC-06.

### R-14 Flange Class
Mole-sieve system piping and equipment SHALL use 900# flange rating (per DBM note that the molecular sieve system requires 900# flanges while adjacent cryogenic-bound piping is 600# at 200 degF).
Source: 4-25 Deepcut DBM SEC-04/06 line note.

### R-15 Turndown
The adsorption side SHALL accommodate 2:1 turndown, with further turndown achievable via single-bed adsorption. Vendor SHALL identify the operating envelope below which channeling / premature breakthrough risk becomes unacceptable.
Source: 4-25 Deepcut DBM SEC-06.

### R-16 Adsorbent Life
The package SHALL be designed assuming 3-year typical adsorbent life (vendor TBC), with the option to extend to 5 years subject to vendor confirmation and turnaround-cycle alignment review.
Source: 4-25 Deepcut DBM SEC-06.

### R-17 Dry-Out Header Interface
The package SHALL provide a tie-in for a low-pressure dry sales-gas recycle dry-out header (initial assumed operating pressure ~250 psig). Final header MAWP and sales-compressor discharge assumptions remain TBC and are an integration item with the EPC Integrator.
Source: 4-25 Deepcut DBM SEC-06.

### R-18 Documentation
The vendor SHALL deliver: the engineered physical equipment package; the vendor package design basis; and the vendor package datasheet set, as listed in `_CONTEXT.md` Anticipated Artifacts.
Source: `_CONTEXT.md`.

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| ASME BPVC Section VIII Div. 1 (or vendor-equivalent) | Adsorber vessel and scrubber pressure-vessel design | location TBD — not specified in accessible sources (ASSUMPTION: industry default) |
| ASME B16.5 / B16.47 | Flange ratings (900# basis confirmed by source) | 4-25 Deepcut DBM (flange-rating note) |
| ASME B31.3 | Process piping within vendor scope | location TBD (ASSUMPTION: industry default) |
| 4-25 Deepcut Design Basis Memorandum (DBM) — SEC-06 | Process design basis, equipment basis, operating envelope, BAHX-protection rules | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| EPC Package Datasheet (DEL-069-02) | Package data handoff to vendor | location TBD (not yet locally extracted; references decomposition only) |
| EPC Scope of Work (DEL-069-01) | Package scope, tagged equipment, boundaries | location TBD (not yet locally extracted) |
| 26020-Package_Requirements.docx | Project package requirements | location TBD (binary; not extracted for PKG-069) |

## Verification

| Req | Verification Method |
|---|---|
| R-1 Adsorbent | Vendor design basis review; material certificate; bed-fill records |
| R-2 Configuration | P&ID review; vessel count and arrangement check against SEC-06 |
| R-3 Outlet water content | FAT/SAT moisture analyzer demonstration; commissioning dry-out performance test |
| R-4 Inlet conditions | Design-condition review against EPC Package Datasheet (DEL-069-02) when available |
| R-5 Sizing/cycle | Sizing calculation review; control-system cycle table verification |
| R-6 dP | Pre-startup clean-bed dP measurement; lifecycle monitoring plan |
| R-7 BAHX protection | Cause-and-effect / SIS review; new-bed online temperature trip test |
| R-8 Inlet filter/coalescers | Datasheet review; FAT |
| R-9 Regeneration system | Equipment datasheets; performance curves; FAT for compressor/heater/cooler/scrubber |
| R-10 Recycle return | P&ID review; NC alternate-path proof test |
| R-11 Blowdown | Cause-and-effect review; HMI demonstration; rate-limit verification |
| R-12 MRU | Vendor performance guarantee; inlet/outlet mercury sampling regime |
| R-13 Dust filters | Datasheet review; clean-dP measurement; manual bypass functional test |
| R-14 Flange class | Piping/equipment material/flange review |
| R-15 Turndown | Process simulation review; vendor breakthrough envelope statement |
| R-16 Adsorbent life | Vendor guarantee statement; review by EPC Integrator |
| R-17 Dry-out header | Tie-in P&ID review; interface coordination record with EPC Integrator |
| R-18 Documentation | Document-deliverables register acceptance against `_CONTEXT.md` and DEL-069-05 / DEL-069-06 |

## Documentation

The vendor SHALL deliver the artifacts named in `_CONTEXT.md` / Anticipated Artifacts:
- Vendor engineered physical equipment package (hardware)
- Vendor package design basis (document)
- Vendor package datasheet set (documents)

Vendor document register, submittals, source-required vendor documentation, and turnover records are governed by DEL-069-05 (Vendor Document Turnover Package); the vendor SHALL deliver inputs to that package as required.
