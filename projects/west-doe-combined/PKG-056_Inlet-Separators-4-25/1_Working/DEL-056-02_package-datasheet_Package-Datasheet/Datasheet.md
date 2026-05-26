# Package Datasheet — DEL-056-02 (PKG-056 Inlet Separators 4-25)

> Descriptive document. Values are source-grounded; missing values are marked `TBD`; inferences are labeled `ASSUMPTION`. Source slices cited inline.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-056-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | PKG-056 — Inlet Separators 4-25 | `_CONTEXT.md` |
| Workbook Package Row | 68 | `_CONTEXT.md`; `26020-Packages_Interfaces_4_export.xlsx` (row 68) |
| Source Heading | Package heading 11 (`26020-01-PT-17-004 - Inlet Separators`) | `26020-Package_Requirements.docx` heading 11 (location TBD — exact heading number derived from source extraction; ASSUMPTION: that the "4-25" qualifier maps to the 26020-01-PT-17-004 unit based on the "4-25 West Doe Deepcut" location stamp in the source slice) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |

## Attributes — Equipment Inventory (Package Tagged Equipment)

| Item | Quantity / Sparing | Description | Source |
|---|---|---|---|
| Horizontal three-phase inlet separators | 2 (2 x 50%) | Identical horizontal three-phase separators. Internally coated with Devchem 253 (piping not coated). Manually adjustable weir; vertical (horizontal-flow) high-performance mesh/vane mist eliminator; de-sanding nozzles. | `26020-Package_Requirements.docx`, package heading "26020-01-PT-17-004 - Inlet Separators", section "Major Included Equipment"; corroborated by `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Inlet Separator Design Parameters" |
| Heated self-framing building | 1 (covers instrumentation and one vessel end) | TBD enclosure size / TBD HVAC load | `26020-Package_Requirements.docx` heading 11, "Major Included Equipment" |
| Inlet PCVs | 2 parallel per separator | Balanced globe valve with hardened trim; one for main inlet, one for drive-gas connection. Design dP <= 5 psid at design inlet pressure (DBM). | Package Requirements heading 11; DBM line 646 |
| Outlet manual isolation valve | per separator | For PCV maintenance isolation without blowdown | Package Requirements heading 11; DBM line 646 |
| Skid-edge inlet isolation valve | per separator | Isolates inlet PCVs for maintenance | Package Requirements heading 11; DBM line 646 |
| Liquid outlet heater (HEX) | 2 at 04-25 (one per installed separator) | Heats cold liquid from approximately -26 °C to a temperature sufficient to keep the MPFF level-control-valve feed above hydrate / freeze thresholds. Heat medium: TBD (candidates: warm glycol, process cross-exchange). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 648 |
| Plot space for third separator | reserved (future) | CONFLICT: legacy project references describe four inlet-separator packages; current basis is two installed plus plot reservation for one more. See Conflict Table in `Guidance.md`. | DBM line 589 |

## Conditions — Operating

| Parameter | Value | Notes / Source |
|---|---|---|
| Operating Pressure | 4,502 to 4,998 kPag (653 to 725 psig) | Package Requirements heading 11, "Scope Notes / Open Items" |
| Operating Temperature | 12.5 to 33.2 °C | Package Requirements heading 11 |
| Gas Flow Rate (operating) | 3,184 e3m3/d (112.5 MMSCFD) per train | Package Requirements heading 11 |
| Produced Water Flow Rate (operating) | 10 Am3/d | Package Requirements heading 11 |
| Raw Condensate Flow Rate (operating) | 616 Am3/d | Package Requirements heading 11 |
| Maximum Inlet Operating Pressure (gathering tie) | 1300 psig (basis: 90% of assumed upstream pipeline MAOP 1440 psig — ASSUMPTION pending detailed-engineering validation) | DBM line 628 |
| Inlet condition during start-up / winter cooldown | Two-phase flow possible; methanol injection may be required for hydrate suppression | DBM line 630 |

## Conditions — Design

| Parameter | Value | Notes / Source |
|---|---|---|
| Design Pressure | 9,377 kPag | Package Requirements heading 11, "Design conditions" |
| Design Temperature | 2.8 to 34 °C | Package Requirements heading 11 |
| Design Gas Flow Rate | 6,368 e3m3/d (225 MMSCFD) per train | Package Requirements heading 11 |
| Design Produced Water Flow | 10 m3/d | Package Requirements heading 11 |
| Design Raw Condensate Flow | 616 m3/d | Package Requirements heading 11 |
| Inlet separator total design vapour (facility) | 300 MMSCFD | DBM §"Inlet Separator Design Parameters", line 622 |
| Inlet separator shut ESDV pressure shutdown | 1360 psig | DBM line 809 |
| Downstream design pressure (post-PCV to J-T outlet) | 1360 psig (600# flange at 200 °F); mol sieve requires 900# flanges | DBM line 628 |
| Slug Capacity (per separator) | 33.9 m3 (Package Requirements heading 11). CONFLICT: DBM line 591 reports an unresolved 31.8 vs 33.9 m3 conflict. | Package Requirements heading 11; DBM line 591 |
| Water Retention Time | TBD | Package Requirements heading 11 |
| Condensate Retention Time | TBD | Package Requirements heading 11 |
| Upstream pipeline holdup (slug source basis) | ~67 m3 (ASSUMPTION: slug processing over 6 hours by downstream MPFF, SOC, and stabilizer equipment) | DBM line 591 |

## Construction

| Aspect | Value | Source |
|---|---|---|
| Vessel orientation | Horizontal | Package Requirements heading 11 |
| Vessel function | Three-phase: sour natural gas (vapour), sour raw condensate (light liquid), sour water (heavy liquid) | Package Requirements heading 11, "Basic Scope" |
| Internal coating | Devchem 253 (vessel only; piping excluded) | Package Requirements heading 11 |
| Internals | Manually adjustable weir; vertical high-performance mesh/vane mist eliminator (subject to operations review); de-sanding nozzles | Package Requirements heading 11; DBM line 646 |
| Sour service | Yes (sour gas / sour condensate / sour water service) | Package Requirements heading 11; DBM §upstream context |
| Vessel dimensions | 9 ft ID x 40 ft S/S each (per current installed-separator basis) | DBM line 589 |
| Sparing | 2 x 50% (two identical trains) | Package Requirements heading 11 |
| By-others scope (excluded) | Interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection | Package Requirements heading 11, "Scope Notes / Open Items" |

## Interface Applicability Matrix

Source: `26020-Packages_Interfaces_4_export.xlsx` (row 68); restated in `26020-Package_Requirements.docx` heading 11 "Physical Interface Summary".

| Interface Type | Applicability | PE Notes |
|---|---|---|
| Process Piping | Yes | — |
| Utility Piping | Yes | — |
| Relief / Flare / Vent | Yes | — |
| Drain / Containment | Yes | — |
| Electrical Power | No | — |
| Area / Exterior Lighting | Yes | `26020-Packages_Interfaces.3.xlsx` column M (row 68) — TBD detail |
| EHT (Electrical Heat Tracing) | Yes | — |
| Grounding / Bonding | Yes | — |
| Cathodic Protection | No | — |
| I&C / Control Cabling | Yes | — |
| Communications / Network | No | — |
| Building HVAC / Services | No | — |
| Fire & Gas / Safety Systems | Yes | — |
| Maintenance Access | Yes | — |
| Grading / Site Drainage / Spill Containment | No | — |
| Structural / Foundations / Supports | Yes | — |
| Product Loading | No | — |
| Pipeline / Pigging | No | — |

## Process Interfaces (Adjacent Systems)

- Upstream: facility inlet pig receivers (with ESDV / possible HIPPS) deliver pipeline gas to inlet separators (DBM line 809; Package Requirements heading 11 inlet PCV scope).
- Downstream gas: inlet separator overhead gas to inlet/TEG DEHY cross-exchanger and on to inlet compression (DBM line 606; Package Requirements line 2421).
- Downstream liquids: heated condensate to MPFF (medium-pressure flash feed separator) via inlet-separator liquid outlet heater (DBM lines 668, 834).
- Utilities: low-pressure fuel gas (purge / drive gas alternate); methanol injection (hydrate suppression); HP flare (vents/blowdown); closed hydrocarbon drain; produced-water handling (DBM lines 811, 834).

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — heading `26020-01-PT-17-004 - Inlet Separators` (read via local textutil extraction)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 68 (interface column M referenced; binary spreadsheet not text-extracted — location TBD for cells beyond interface applicability)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Inlet Separator Design Parameters" (lines 589-660, 809-852)
- Accepted decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-056-02)
