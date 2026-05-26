# Datasheet — DEL-091-01 Scope of Work (PKG-091 Tank Farm Pump Building 3-25)

> Descriptive datasheet for the EPC Integrator Scope of Work deliverable for the
> Tank Farm Pump Building 3-25 package (PKG-091). Populated from `_CONTEXT.md`,
> `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and
> `INTERFACE_REGISTER.csv` in the accepted GATE-07 PROJECT_DECOMP snapshot.
>
> Note on source scope: the Word source `_Sources/26020-Package_Requirements.docx`
> (heading 44) and the Packages workbook
> `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 84) are cited by the
> decomposition but are not locally accessible as text slices. Authoritative
> content for this package is carried into the GATE-07 registers
> (SCOPE_LEDGER SOW-0185 through SOW-0188, PACKAGE_REGISTER row PKG-091, and
> INTERFACE_REGISTER rows for PKG-091); those register rows are the locally
> accessible source slices used here. The DBM source slice
> `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` does not contain
> a Tank Farm Pump Building 3-25 section as of the GATE-07 snapshot; no
> DBM-derived claims are introduced.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-091-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-091` | `_CONTEXT.md` |
| Parent Package Name | Tank Farm Pump Building 3-25 | `_CONTEXT.md` |
| Parent Workbook ID | 91 (Workbook Packages row 84) | `PACKAGE_REGISTER.csv` |
| Package Tracking No. | `26020-03-18-001` (Word source: `26020-03-PT-18-002 - Tank Farm Pumps`) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | SOW-0185, SOW-0186, SOW-0187, SOW-0188 | `_CONTEXT.md`, `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`, `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Authoritative decomposition snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |

## Attributes (Package Identity and Function)

| Attribute | Value | Source |
|---|---|---|
| Package function | Houses all pumps for the Tank Farm 3-25: water transfer pumps in parallel pull water from produced-water tanks through a bag filter and out to the produced-water pipeline; sour-condensate booster pumps move sour condensate from the sour-condensate storage tanks to the condensate-sweetening feed pumps; sweet-condensate feed/booster/recycle pumps and a building drain pump are also housed in the building | SCOPE_LEDGER SOW-0186; `PACKAGE_REGISTER.csv` ScopeDescription |
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv` ResponsibilityModel; SCOPE_LEDGER SOW-0185 |
| Configuration | Building enclosure housing the tagged pump set listed under "Major included equipment" (SOW-0187); water-transfer pumps configured in parallel | SCOPE_LEDGER SOW-0186, SOW-0187 |
| Building Drain Pump | 1 × P-9295-2 — Graco 1050A pneumatic diaphragm, 11.34 m³/h @ 689 kPag, pneumatically driven | SCOPE_LEDGER SOW-0187, SOW-0188 |
| Water Transfer Pumps | 2 × P-9290/9293-2 — radial centrifugal; seal plan: single mechanical; 150 kW (200 HP); 575 V / 3 Ph / 60 Hz; rated 218 m³/d @ 172 kPad (40 USGPM @ 25 psid); water-transfer line to include c/w | SCOPE_LEDGER SOW-0187, SOW-0188 |
| Sour Condensate Booster Pumps | 2 × P-9215/9216-2 — vertical inline centrifugal; seal plan: API-682 Plan 14/52; 18.5 kW (25 HP); 575 V / 3 Ph / 60 Hz | SCOPE_LEDGER SOW-0187 |
| Condensate Sweetening Feed Pumps | 2 × P-9210/9220-2 — vertical inline centrifugal; seal plan: API-682 Plan 14/52; 55 kW (75 HP) @ 100%; voltage TBC (`575V/3Ph/60Hz` is implied by sibling pumps but not explicitly stated for this tag — ASSUMPTION) | SCOPE_LEDGER SOW-0187; ASSUMPTION on voltage |
| Condensate Skim Pump | 1 × P-9200-2 — diaphragm positive displacement (Hydracell, sealless); 11 kW (15 HP); 575 V / 3 Ph / 60 Hz; 20 m³/h | SCOPE_LEDGER SOW-0187, SOW-0188 |
| Sour Condensate Recycle Pump | 1 × P-9230-2 — diaphragm positive displacement (Hydracell, sealless); 11 kW (15 HP); 575 V / 3 Ph / 60 Hz; 20 m³/h | SCOPE_LEDGER SOW-0187, SOW-0188 |
| Condensate Booster Pumps | 2 × P-9211/9221-2 — vertical inline centrifugal; seal plan: API-682 Plan 14/52; 18.5 kW (25 HP) | SCOPE_LEDGER SOW-0187 |
| Condensate Product Recycle Pump | 1 × P-9240-2 — diaphragm positive displacement (Hydracell, sealless); 11 kW (15 HP); with inlet basket strainer (size TBC) | SCOPE_LEDGER SOW-0187 |
| Tagged equipment list (consolidated) | See per-pump rows above; full per-tag datasheets and any further tags are to be issued in DEL-091-02 Package Datasheet | SCOPE_LEDGER SOW-0187; ASSUMPTION (handoff scope) |
| Materials | TBD (sour-service materials and NACE applicability not stated in accessible source slices) | TBD |

## Conditions (Process / Driver Design Basis)

| Parameter | Value | Source |
|---|---|---|
| Driver — voltage / phase / frequency | All pumps driven by 575 V / 3 Ph / 60 Hz motors | SCOPE_LEDGER SOW-0188 |
| Driver — starting method | DOL or VFD; local control via H-O-A or On-Off switch; motors fed from 600 V MCC | SCOPE_LEDGER SOW-0188 |
| Driver — sizing basis | Motors sized for inlet stabilizer composition density at -40 °C start-up condition | SCOPE_LEDGER SOW-0188 |
| Building Drain Pump rated point | 11.34 m³/h @ 689 kPag | SCOPE_LEDGER SOW-0187, SOW-0188 |
| Water Transfer Pump rated point | 218 m³/d @ 172 kPad (40 USGPM @ 25 psid) | SCOPE_LEDGER SOW-0188 |
| Sour Condensate Booster Pump rated point | TBC | SCOPE_LEDGER SOW-0188 |
| Sweet Condensate Feed Pump rated point | TBC | SCOPE_LEDGER SOW-0188 |
| Condensate Skim Pump rated point | 20 m³/h | SCOPE_LEDGER SOW-0188 |
| Sour Condensate Recycle Pump rated point | 20 m³/h | SCOPE_LEDGER SOW-0188 |
| Condensate Booster Pump rated point | TBC | SCOPE_LEDGER SOW-0188 |
| Condensate Loading | Mentioned as in-package scope item; rated point TBC | SCOPE_LEDGER SOW-0188 |
| Operating specifications | TBC — see Throughput/Capacity and site conditions | SCOPE_LEDGER SOW-0188 |
| Design conditions | TBC — see Throughput/Capacity and site conditions | SCOPE_LEDGER SOW-0188 |
| Site ambient design conditions | TBD (not stated in accessible source slices for this package) | TBD |
| Sour-service / NACE applicability | TBD (not stated in accessible source slices) | TBD |

## Construction (Package Boundaries and Battery Limits)

| Element | Statement | Source |
|---|---|---|
| Package boundary scope | Vendor-engineered pump-building package supplied as a unit with vendor engineering, design, vendor documentation, and physical equipment package | `PACKAGE_REGISTER.csv` ResponsibilityModel; SCOPE_LEDGER SOW-0185 |
| Facility-level integration | Owned by EPC Integrator: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` ResponsibilityModel; SCOPE_LEDGER SOW-0185 |
| Excluded — by others | DCS integration; foundations; electrical supply to MCC | SCOPE_LEDGER SOW-0188 |
| Applicable interface types (15) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` rows for PKG-091; `PACKAGE_REGISTER.csv` InterfaceTypes |
| Package-level exclusions stated | TBD; no package-specific exclusions stated in source materials beyond the "by others" list above | `PACKAGE_REGISTER.csv` Exclusions |
| Open issues flagged in source | Operating Specs TBC; design conditions TBC; several pump rated points TBC; inlet basket strainer size TBC; sour-service materials TBD | SCOPE_LEDGER SOW-0188; SOW-0187 |

## References

- `_CONTEXT.md` — deliverable identity, scope items, supported objectives, decomposition pointer.
- `_REFERENCES.md` — authoritative decomposition basis and shared source root.
- GATE-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row `DEL-091-01_scope-of-work`).
  - `PACKAGE_REGISTER.csv` (row `PKG-091`).
  - `SCOPE_LEDGER.csv` (rows `SOW-0185`, `SOW-0186`, `SOW-0187`, `SOW-0188`).
  - `INTERFACE_REGISTER.csv` (15 rows for `PKG-091`).
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-091-01 → OBJ-002…OBJ-010).
- `_Sources/26020-Package_Requirements.docx` (heading 44; location TBD — not locally accessible as text).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages row 84; location TBD — not locally accessible as text).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — no PKG-091 / Tank Farm Pump Building 3-25 section located in the GATE-07 snapshot (no claims sourced from this file).
