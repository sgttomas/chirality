# Specification — DEL-066-02 Package Datasheet (PKG-066 Tanks, Condensate (API 650) 4-25)

ProvenanceNote: Source-grounded against locally accessible DBM source slices. Source `26020-Package_Requirements.docx` heading 21 not locally accessible — content depending solely on it is `TBD (source not accessible)`. Inferences are labeled ASSUMPTION.

## Scope

In scope of this Package Datasheet:
- Definition of the Tanks, Condensate (API 650) package data required for vendor or discipline package engineering and design at the 04-25 Deep Cut Gas Plant (`_CONTEXT.md`).
- Tank inventory, service conditions, governing codes, interface requirements, anticipated artifacts (Datasheet section "Attributes" and "Interface Requirements").
- Carriage of interface facts as evidence per `_CONTEXT.md` Notes (interfaces are not separated as standalone deliverables).

Out of scope:
- Scope of work narrative — owned by DEL-066-01_scope-of-work.
- Construction work package — owned by DEL-066-03.
- Vendor engineering production unit — owned by DEL-066-04.
- Vendor document turnover register — owned by DEL-066-05.

Scope items covered (from `_CONTEXT.md`): SOW-0205, SOW-0206, SOW-0207, SOW-0208.

## Requirements

Each row below is either source-grounded with citation, ASSUMPTION (inferred from related source slices), or TBD (location TBD / source not accessible).

| ReqID | Requirement | Type | Source / Basis |
|---|---|---|---|
| REQ-066-02-01 | Atmospheric storage tanks within PKG-066 shall be designed to API 650 (package name designates API 650). | Code | `_CONTEXT.md`; package name |
| REQ-066-02-02 | Where the produced-water tank analog applies, tanks shall be API-650 Modified, externally insulated and heated, with Devchem 253 internal coating. | Code/Material | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section (ASSUMPTION: directly carried to condensate-service tanks pending vendor datasheet) |
| REQ-066-02-03 | Tank field arrangement shall meet NFPA 30 atmospheric-tank-to-atmospheric-tank spacing of 2.35 m (7.72 ft) minimum. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — NFPA 30 Table 22.4.2.1 |
| REQ-066-02-04 | Atmospheric tanks holding unstable liquids shall be at least 30.5 m (100 ft) from property line or building on same property. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — NFPA 30 Table 22.4.1.5 |
| REQ-066-02-05 | Atmospheric tanks shall be at least 80 m (262.5 ft) from the nearest public road. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — OGAOM Sec. 9.6.15, DPR 48 |
| REQ-066-02-06 | Atmospheric condensate tanks shall be at least 50 m (164 ft) from the flare. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — OGAOM Sec. 9.6.15 |
| REQ-066-02-07 | Atmospheric tanks shall be at least 25 m (82 ft) from any fired heater. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — OGAOM Sec. 9.6.15 |
| REQ-066-02-08 | Pressurized bullets shall be located at least 30.48 m (100 ft) from the nearest atmospheric tank. | Spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 — API 2510 |
| REQ-066-02-09 | Tank vapour collection points shall be tied into the VRU system (post SCA-002, discharge to 04-25 SOC suction). | Process Interface | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Vapour Recovery |
| REQ-066-02-10 | Tank design specific gravity for stabilized C5+ condensate service shall accommodate expected density < 650 kg/m3 at 15 deg C (stabilizer-bottoms basis); design SG TBD pending vendor datasheet. | Process | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` C5+ Condensate section |
| REQ-066-02-11 | Package shall provide tie-ins for stabilized-condensate export (~7,900 bbl/d, 1,256 m3/d to 03-25 sour condensate storage). | Interface | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 380 |
| REQ-066-02-12 | Tank shell/bottom/roof construction details (thickness, plate grades, welding), nozzle schedule, foundation/anchorage, dike/secondary containment, internal coating for non-produced-water service, surface preparation/external coating, and inspection/NDE basis shall be defined per `26020-Package_Requirements.docx` package heading 21. | Construction | TBD (source not accessible) |
| REQ-066-02-13 | Site environmental loading (wind, snow, seismic, temperature extremes) used for tank shell design shall align with the 04-25 site basis. | Civil/Structural | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 site-specific design parameters (location TBD) |
| REQ-066-02-14 | Electrical, instrumentation, and control interfaces (level, temperature, pressure, fire/gas, hi-hi shutdown) shall align with plant DCS/SIS basis. | I&C | TBD (source not accessible: `26020-Package_Requirements.docx` heading 21) |

## Standards

| Standard | Application | Source Citation |
|---|---|---|
| API 650 | Welded tanks for oil storage — governing tank code | Package name (`_CONTEXT.md`); REQ-066-02-01 |
| API 650 Modified (project-specific) | Externally insulated/heated atmospheric tanks with Devchem 253 internal coating (produced-water analog) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section |
| NFPA 30 | Atmospheric tank spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 |
| API 2510 | LP-storage facility spacing (pressurized bullets ↔ atmospheric tanks) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 |
| OGAOM Sec. 9.6.15, DPR 48 | BC regulatory spacing to public roads, flare, fired heaters | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-03 |
| Other tank-specific standards (paint, weld procedures, inspection) | TBD | location TBD (`26020-Package_Requirements.docx` heading 21 not accessible) |

## Verification

| ReqID | Verification Method | Acceptance Evidence |
|---|---|---|
| REQ-066-02-01 | Vendor design review against API 650 latest edition | Stamped vendor calculation set; code-edition declaration |
| REQ-066-02-02 | Vendor datasheet/MOC review | Material certificates; coating system datasheet (Devchem 253 or approved equal) |
| REQ-066-02-03 / -04 / -05 / -06 / -07 / -08 | Plot plan / spacing review | Marked-up plot plan; spacing study |
| REQ-066-02-09 | VRU tie-in P&ID review | Reviewed/approved P&IDs; VRU integration check |
| REQ-066-02-10 | Vendor mechanical calculations | Design SG basis; shell calculations |
| REQ-066-02-11 | Interface tie-in matrix review | Interface register entry; flow/pressure handshake |
| REQ-066-02-12 / -13 / -14 | Package datasheet review against `26020-Package_Requirements.docx` heading 21 (when accessible) | Filled vendor datasheet, gap-closure log |

## Documentation

Anticipated artifacts (per `_CONTEXT.md`):
- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis (this deliverable + DEL-066-04).
- Package interface requirements matrix (carried in this datasheet's Interface Requirements section per `_CONTEXT.md` Notes).
- Source-supported equipment and design criteria (per Attributes/Conditions/Construction sections above).

Required downstream documents (cross-deliverable):
- DEL-066-01 Scope of Work (upstream context).
- DEL-066-03 Construction Work Package.
- DEL-066-04 Vendor Engineered Equipment Package.
- DEL-066-05 Vendor Document Turnover Package.
