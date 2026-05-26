# Datasheet — DEL-084-02 Package Datasheet (PKG-084 Fuel Gas Skid 3-25)

> EPC Integrator technical handoff datasheet capturing the package data required for third-party vendor / discipline package engineering and design of the Low-Pressure Fuel Gas Package (skid-mounted heater + scrubber) serving the West Doe complex.
> All non-trivial values are source-cited or marked `TBD` / `ASSUMPTION` per skill rules.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-084-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-084` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-084 |
| Parent Workbook ID | 84 | `_CONTEXT.md` |
| Package Name | Fuel Gas Skid 3-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-084 |
| Package Tag (workbook) | 26020-02-PT-23-001 — Fuel Gas Skid | `PACKAGE_REGISTER.csv` row PKG-084 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-084-02 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| Workbook Row | 60 | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Source Basis (declared) | Workbook Packages row 60; `26020-Package_Requirements.docx` package heading 37; `Bid Docs/Budgetary/26020-02-PT-RFQ-23-001_FG_Skid_1.docx`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |

## Package Identity and Composition

| Attribute | Value | Source |
|---|---|---|
| Package description (workbook) | One skid-mounted Low Pressure Fuel Gas Package comprising one (1) Low-pressure fuel gas heater and one (1) Low-pressure fuel gas scrubber | `PACKAGE_REGISTER.csv` row PKG-084 (description column) |
| Process function | Skid serves the low-pressure (LP) fuel gas system for the West Doe Deep Cut Facility (cross-facility shared utility; serves 04-25 gas plant, 03-25 liquids hub, and 03-25 compressor station) | `PACKAGE_REGISTER.csv` row PKG-084; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Utility Integration Basis (L452); §Fuel Gas (L454-465) |
| Package vendor responsibility | Package engineering, package design, vendor documentation, and physical equipment package | `PACKAGE_REGISTER.csv` row PKG-084 |
| EPC Integrator responsibility | Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | `PACKAGE_REGISTER.csv` row PKG-084 |
| Reference RFQ | `26020-02-PT-RFQ-23-001_FG_Skid_1.docx` | `PACKAGE_REGISTER.csv` (Word Source Basis) |

> ASSUMPTION: package register description says "serve … West Doe Deep Cut Facility" while the 03-25 Comp_and_Liquids DBM places the fuel-gas building "at or associated with 04-25." Interpreted here as a single shared LP fuel gas package physically associated with 04-25 serving the combined complex. Owner ruling needed before issue (see `Guidance.md` Conflict Table CF-01).

## Equipment List (in package scope)

| Item Tag (source) | Description | Source |
|---|---|---|
| LP Fuel Gas Heater | Electric resistance heater controlled by SCR; sized for maximum sales-compressor discharge pressure and winter ambient buyback gas conditions; skin-temperature thermocouple override and gas-outlet temperature control to prevent overheating under stagnant-gas conditions | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| V-3210-1 (Deepcut basis) / V-3210-2 (03-25 basis) — LP Fuel Gas Scrubber | Two-phase scrubber removing condensed liquids before distribution to LP fuel gas users; downstream of the LP fuel gas heater; routes condensed liquids to TK-9130-1 (4-25 basis) / TK-9130-2 slop (3-25 basis) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |

> ASSUMPTION: V-3210-1 vs V-3210-2 tag duplication across DBMs reflects facility-specific tag numbering for the same single shared package. Treated as one scrubber unless source ruling resolves otherwise (Conflict Table CF-02).

## Service / Process Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | Low-pressure fuel gas (sweet, downstream of molecular sieve dehydration / sales-gas buyback pipeline) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L456 |
| LP fuel gas users (listed) | TEG stripping, caustic treating overhead dilution, maintenance purge, drive gas, blanket gas, building heaters, flare pilots/purge, compressor purge/sweep gas, generator fuel | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L456, L463; `DBM-Deepcut/4-25_Deepcut_DBM.md` L1830 (utility row) |
| Normal total LP fuel gas flow | 1.382 MMSCFD (39.13 e3m3/d) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Design LP fuel gas flow | > 1.5 MMSCFD (42.5 e3m3/d); final design flow TBC | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Fuel-gas inlet source — primary | Enbridge sales-gas pipeline via 04-25 plant sales-gas splitter | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L456 |
| Fuel-gas inlet source — secondary | Alliance pipeline | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L456 |
| Enbridge supply — Normal / Max / MAWP | 5,171 kPag (750 psig) / 5,516 kPag (800 psig) / 9,928 kPag (1,440 psig) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L458-460 |
| Alliance supply — Normal / Max / MAWP | 5,516 kPag (800 psig) / 8,274 kPag (1,200 psig) / 9,928 kPag (1,440 psig) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L458-461 |
| Emergency buyback fuel gas | Sourced from sales pipeline through regulators independent from plant main regulators; no consumption expected during normal operation; buyback MAOP estimate 9,928 kPag, requires detailed-engineering verification | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1878 |
| Emergency buyback inclusion ruling | CONFLICT: W242510 indicates not required; Process_DBM_fixed includes it in 04-25 utility package; awaits human authority ruling before final issue | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L465; see Conflict Table CF-03 |

## Equipment Sizing & Construction Attributes

### LP Fuel Gas Heater

| Attribute | Value | Source |
|---|---|---|
| Type | Electric resistance heater | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Control | SCR (silicon-controlled rectifier) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Sizing basis | Maximum sales-compressor discharge pressure and winter ambient buyback gas conditions | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Duty | TBD | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Required overrides / controls | Skin-temperature thermocouple override; gas-outlet temperature control to prevent overheating under stagnant-gas conditions | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Inlet design pressure | TBD (sized for buyback case up to MAOP 9,928 kPag; final value confirmed by vendor) | ASSUMPTION from `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872, L1878 |
| Inlet design temperature | TBD | TBD |
| Outlet temperature target | TBD | TBD |
| Electrical power supply | TBD (skid is electric-drive consistent with facility electrification basis); coordinate with EPC electrical | ASSUMPTION; cross-ref `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L533 |
| Area classification | TBD — to be confirmed by EPC HAZOC / area-classification deliverable | TBD |

### LP Fuel Gas Scrubber (V-3210-1 / V-3210-2)

| Attribute | Value | Source |
|---|---|---|
| Type | Two-phase vertical scrubber (vane/mesh internals TBC by vendor) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; ASSUMPTION on internal style |
| Position | Downstream of LP fuel gas heater | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Sizing K-factor | Maximum K = 0.35 Imperial with operating-pressure derating | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Flow basis | Fuel gas system design flow (> 1.5 MMSCFD) at design operating pressure | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Hydrocarbon liquid density basis | Inlet-gas-composition liquid density at 150 psig and initial dewpoint | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874 |
| Expected liquid load | Minimal (normal sources downstream of molecular sieve dehydration or from sales-gas buyback pipelines) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874 |
| Liquid disposition | Routes condensed liquids to TK-9130-1 (Deepcut basis) / TK-9130-2 slop (3-25 basis) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| Design pressure | TBD (must envelop Alliance Max 8,274 kPag with upstream protection; envelope MAOP 9,928 kPag pending pressure-protection philosophy) | ASSUMPTION from `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L458-461; L1878 |
| Design temperature | TBD | TBD |
| Material of construction | TBD | TBD |
| Relief / blowdown routing | TBD (coordinate with HP/LP flare basis at 03-25/04-25; see Conflict CF-04) | TBD; cross-ref `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare; `DBM-Deepcut/4-25_Deepcut_DBM.md` L1830 (Fuel gas utility) |

## Site / Environmental Conditions

| Attribute | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15W6, north of Dawson Creek, BC | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L12 (Site table); L85 |
| Site elevation | 673 m above mean sea level | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L85 |
| Climatic / ambient design envelope | TBD (winter ambient basis applies to buyback heater sizing) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| Area classification | TBD | TBD |
| Seismic / wind / snow loads | TBD | TBD |

## Interface Requirements Matrix (package-level)

Per PACKAGE_REGISTER PKG-084 (`Applicable interface types` column) and Comp_and_Liquids DBM, the package shall provide tie-in interfaces for the following interface types. Detailed tag-level interface tags are out of scope for the package datasheet; they will be carried in EPC interface lists and `INTERFACE_REGISTER.csv`.

| Interface Type | Direction (typical) | Notes / Source |
|---|---|---|
| Process Piping | In/out | LP fuel gas distribution to users; condensate to slop tank |
| Utility Piping | In/out | TBD |
| Relief / Flare / Vent | Out | Scrubber / heater PSV routing — TBD (see CF-04) |
| Drain / Containment | Out | TBD; coordinate with `DBM-Deepcut/4-25_Deepcut_DBM.md` L1833 (drains row) |
| Electrical Power | In | Heater electric resistance + SCR; instrument power |
| Grounding / Bonding | In | Standard skid bonding to facility grounding grid (TBD) |
| Area / Exterior Lighting | In | TBD |
| I&C / Control Cabling | In/out | Heater control (SCR), skin-T thermocouple, gas-outlet T control, scrubber LIC, ESD |
| Building HVAC / Services | In | TBD (skid building scope TBC) |
| Fire & Gas / Safety Systems | In/out | TBD; coordinate with facility F&G philosophy |
| Maintenance Access | — | TBD; vendor to provide maintenance envelopes |
| Structural / Foundations / Supports | In | Skid mounting / anchor pattern; foundation loads from vendor |

Source: `PACKAGE_REGISTER.csv` row PKG-084 (`Applicable interface types`); detail attribution `DBM-Deepcut/4-25_Deepcut_DBM.md` L1830 (Fuel gas utility row).

## Anticipated Artifacts (this datasheet rolls up)

- Package technical datasheet (this document)
- Vendor engineering handoff basis
- Package interface requirements matrix (placeholder above; detail in EPC interface deliverables)
- Source-supported equipment and design criteria

Source: `DELIVERABLE_REGISTER.csv` row DEL-084-02 (Anticipated Artifacts column); `_CONTEXT.md`.

## Open Items / TBD Summary

| ID | Open Item | Source |
|---|---|---|
| OI-01 | Heater duty (kW) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1872 |
| OI-02 | Scrubber & heater design pressure / temperature / materials | TBD |
| OI-03 | LP fuel gas final design flow (> 1.5 MMSCFD; precise TBC) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| OI-04 | Emergency buyback fuel gas inclusion (W242510 says no; Process_DBM_fixed says yes) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L465 |
| OI-05 | V-3210-1 vs V-3210-2 tag duplication across DBMs | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 |
| OI-06 | Facility location of the LP fuel gas building (04-25 per Comp_and_Liquids DBM L452; package register says serves Deep Cut Facility) | Comp_and_Liquids L452; `PACKAGE_REGISTER.csv` |
| OI-07 | Relief/blowdown routing (HP vs LP flare allocation) | TBD; cross-ref `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare |
| OI-08 | Area classification, seismic/wind/snow envelopes | TBD |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- `PACKAGE_REGISTER.csv` row `PKG-084` (Gate 7 snapshot)
- `DELIVERABLE_REGISTER.csv` row `DEL-084-02` (Gate 7 snapshot)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (§Utility Integration Basis L450; §Fuel Gas L454-465)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Utility table row "Fuel gas" L1830; §"Fuel Gas Heating and Scrubbing" L1872-1874; §Emergency Buyback L1876-1878)
- `_Sources/26020-Package_Requirements.docx` — package heading 37 (location TBD; not slice-read here)
- `Bid Docs/Budgetary/26020-02-PT-RFQ-23-001_FG_Skid_1.docx` — referenced by `PACKAGE_REGISTER.csv` (location TBD; not slice-read here)
