# Datasheet — DEL-085-02 Package Datasheet (PKG-085 Flare Stack, High Pressure)

> Descriptive datasheet for the EPC Integrator technical handoff to the Package Vendor for the common high-pressure (HP/Cryo) flare stack at facility 03-25. Values that are not supported by locally accessible source slices are marked `TBD` with `location TBD` where applicable. Decomposition prose is used for scope only, not as a value source.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-085-02_package-datasheet | _CONTEXT.md |
| Deliverable Name | Package Datasheet | _CONTEXT.md |
| Parent Package ID | PKG-085 | _CONTEXT.md |
| Parent Package Name | Flare Stack (High Pressure) | _CONTEXT.md |
| Workbook ID | 85 (Workbook Packages row 58) | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Discipline | Mechanical | _CONTEXT.md |
| Deliverable Type | EPC Package Datasheet | _CONTEXT.md |
| Responsible Party | EPC Integrator | _CONTEXT.md |
| Package Vendor Tag (per package register) | 26020-02-PT-25-001 — Flare Stack (High Pressure) | PACKAGE_REGISTER.csv (PKG-085) |
| Facility Location | 03-25 (HP/Cryo + LP dual flare stack at or associated with 03-25, shared with 04-25) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Flare and Blowdown section (lines 497-499) |
| Service | High-pressure (HP) and cryogenic (Cryo) flare relief and blowdown disposal | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 497) |
| Configuration | Common HP/Cryo + LP dual flare stack; this package addresses the HP/Cryo stack | DBM-Comp_and_Liquids (lines 497-499); PACKAGE_REGISTER.csv |

## Attributes

| Attribute | Value | Units | Source |
|---|---|---|---|
| HP/Cryo flare stack outside diameter | 660 | mm OD | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| HP/Cryo flare stack height | 60,957 | mm | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| Flare tip type | Sonic (HP/Cryo) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| Companion LP stack OD | TBD (carried as TBD in source) | mm | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| HP relief header size | 508 (20 in) | mm | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| LP relief header size | 508 (20 in) | mm | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| Upstream HP KO drums | V-4100-2 (compressor area), V-4150-2 (tank farm) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 497) |
| HP KO drum transfer pumps | P-4100-2, P-4150-2 (truck-out or transfer to slop) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 497) |
| Companion LP KO drum | V-3900-2 (transfer pump P-3900-2 to slop) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499) |
| HP relief / blowdown load (kg/s and composition) | TBD (final flare studies required) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 548) — `location TBD` |
| LP relief / blowdown load | TBD (final flare studies required) | — | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 548) — `location TBD` |
| Vendor budgetary basis | 24292-02-PT-ENR-25-201_R1 (go-by only; not authoritative engineering) | — | PACKAGE_REGISTER.csv (PKG-085); ASSUMPTION — document not present in `_Sources` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Sour service | Yes — package serves sour HP relief (HP KO drums in compressor area and tank farm; routes shared with 04-25) | DBM-Comp_and_Liquids (line 497); DBM-Deepcut (lines 834-842) |
| Cryogenic relief service | Yes — sonic HP/Cryo flare also receives cryogenic flare flow; J-T valve mechanical stop sized so that control-failure mass flow does not exceed cryogenic flare design flow | DBM-Deepcut/4-25_Deepcut_DBM.md (line 1321) |
| Shared service split (03-25 / 04-25) | Stack and incinerator are shared-interface systems; exact service split and owner interface remain open interface items pending source resolution | DBM-Comp_and_Liquids (line 56) |
| Site location reference (03-25) | TBD — site coordinates / plot reference `location TBD` (decomposition routes scope; site coordinates not in available DBM slices) | TBD |
| Flare-to-equipment spacing | 25 m (82 ft) min between flare/incinerator and nearest plant equipment | DBM-Deepcut/4-25_Deepcut_DBM.md (line 280) [OGAOM Sec. 9.6.15] |
| Flare-to-property-line spacing | 80 m (262.5 ft) min between flare and nearest public road or property line | DBM-Deepcut/4-25_Deepcut_DBM.md (line 281) [OGAOM Sec. 9.6.15] |
| Flare-to-atmospheric-condensate-tank spacing | 50 m (164 ft) | DBM-Deepcut/4-25_Deepcut_DBM.md (line 282) [OGAOM Sec. 9.6.15] |
| Flare-to-separator / atmospheric-PW-tank spacing | 25 m (82 ft) | DBM-Deepcut/4-25_Deepcut_DBM.md (line 283) [OGAOM Sec. 9.6.15] |
| Flare-to-pressurized-bullets spacing | 30.48 m (100 ft) | DBM-Deepcut/4-25_Deepcut_DBM.md (line 284) [API 2510] |
| Flare-to-vegetation/fire-hazard spacing (incl. KO drums) | 10 m (32 ft) | DBM-Deepcut/4-25_Deepcut_DBM.md (line 287) [OGAOM Sec. 9.6.15] |
| Thermal radiation flux — inside boundary, blackened area | <=9 kW/m^2 | DBM-Deepcut/4-25_Deepcut_DBM.md (line 285) [OGPFR App.1 Sch.1 Sec.2 — external regulatory ref not in available input package; verify in detailed design (DBM line 289)] |
| Thermal radiation flux — outside boundary | <=5 kW/m^2 | DBM-Deepcut/4-25_Deepcut_DBM.md (line 286) [OGPFR App.1 Sch.1 Sec.2 — verify per DBM line 289] |
| Site climatic / wind / seismic basis | TBD (`location TBD` — refer to 03-25 facility civil/geotech basis; not available in deliverable-local source slices) | TBD |

## Construction

| Item | Description | Source |
|---|---|---|
| Stack support | Self-supported dual flare stack (per package vendor budgetary go-by) | ASSUMPTION — based on PACKAGE_REGISTER.csv reference to "24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf" (budgetary go-by only) |
| Stack tip | Sonic flare tip on HP/Cryo stack | DBM-Comp_and_Liquids (line 499) |
| Stack body materials | TBD (`location TBD` — vendor to confirm against final relief loads and metallurgy review) | TBD |
| Foundations / anchorage | EPC-Integrator scope; equipment-specific foundation and anchorage checks required per DBM general civil basis | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 700) |
| Knock-out drums upstream of stack | V-4100-2, V-4150-2 (HP); V-3900-2 (LP companion) — supplied by EPC-Integrator scope, interface to stack | DBM-Comp_and_Liquids (lines 497, 499) |
| KO drum pumps | P-4100-2, P-4150-2 (HP); P-3900-2 (LP) — to slop / truck-out | DBM-Comp_and_Liquids (lines 497, 499) |
| Headers (HP / LP relief) | 508 mm (20 in) NPS, materials and rating TBD | DBM-Comp_and_Liquids (line 499) |
| Pilot / ignition / purge gas | TBD (`location TBD` — vendor scope; pilot/ignition/molecular-seal configuration to be confirmed) | TBD |
| Flame detection / monitoring | TBD (`location TBD` — vendor scope; pilot-monitoring strategy to be confirmed) | TBD |
| Tie-ins to incinerator | Incinerator physically located at 3-25 facility near the flare stacks; services 4-25 NGL mercaptan treating | DBM-Deepcut/4-25_Deepcut_DBM.md (line 1570) |

## Major Interfaces (Package-Level)

Interface types declared at the package level (PACKAGE_REGISTER.csv, PKG-085 InterfaceTypes column):

- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- Grounding / Bonding
- I&C / Control Cabling
- Fire & Gas / Safety Systems
- Structural / Foundations / Supports

Detailed interface matrix (tag-to-tag, line-to-line) is to be developed from 26020-Packages_Interfaces_4_export.xlsx; that source is a binary spreadsheet and is not text-accessible in this run. Marked `TBD — extraction pending`.

## Scope Coverage and Objectives (context)

- Covers Scope Items: SOW-0087, SOW-0088, SOW-0089, SOW-0090 (_CONTEXT.md; OBJECTIVE_SCOPE_MAP.csv).
- Supports Objectives (ASSUMPTION — package-grouping heuristic per skill default): OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (_CONTEXT.md). Heuristic association; not a hard requirement until human-confirmed.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot), row DEL-085-02
- PACKAGE_REGISTER.csv (GATE-07 snapshot), row PKG-085
- OBJECTIVE_SCOPE_MAP.csv (GATE-07 snapshot), rows for PKG-085
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Flare and Blowdown section
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Flare and Incinerator Spacing section
- 26020-Package_Requirements.docx (package heading 38) — referenced by decomposition; binary .docx, text not accessible in this run (`location TBD`)
- 26020-Packages_Interfaces_4_export.xlsx — referenced by decomposition; binary .xlsx, text not accessible in this run (`location TBD`)
- 24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf — budgetary go-by only, not present in `_Sources` (`location TBD`)
