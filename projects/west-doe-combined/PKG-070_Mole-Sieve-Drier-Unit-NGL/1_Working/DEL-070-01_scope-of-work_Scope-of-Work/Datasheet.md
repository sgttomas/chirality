# Datasheet — DEL-070-01 Scope of Work (PKG-070 Mole Sieve Drier Unit (NGL))

> Descriptive datasheet for the EPC Integrator Scope of Work deliverable for the
> NGL Mole Sieve Drier Unit package (PKG-070). Populated from `_CONTEXT.md`,
> `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`,
> `INTERFACE_REGISTER.csv`, and the locally accessible DBM source slice
> `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06).
>
> Note on source scope: the NGL-specific RFQ
> `Bid Docs/Budgetary/26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx` and the
> Word file `_Sources/26020-Package_Requirements.docx` (heading 24) are cited
> by the decomposition but are not locally accessible as text slices. The DBM
> SEC-06 source slice describes the *process-gas* molecular-sieve system, not
> the NGL liquid-phase package; it is used only where directly relevant.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-070-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-070` | `_CONTEXT.md` |
| Parent Package Name | Mole Sieve Drier Unit (NGL) | `_CONTEXT.md` |
| Parent Workbook ID | 70 (Workbook Packages row 74) | `PACKAGE_REGISTER.csv` |
| Package Tracking No. | `26020-01-PT-22-003` (Mole Sieve Drier Unit (NGL)) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | SOW-0145, SOW-0146, SOW-0147, SOW-0148 | `_CONTEXT.md`, `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (PACKAGE_HEURISTIC; ASSUMPTION) |
| Authoritative decomposition snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |

## Attributes (Package Identity and Function)

| Attribute | Value | Source |
|---|---|---|
| Package function | NGL molecular sieve dehydration package — dries water-saturated C3+ NGL to cryogenic/storage specification prior to downstream NGL handling | `PACKAGE_REGISTER.csv` ScopeDescription; SCOPE_LEDGER SOW-0146 |
| Configuration | Three-tower: one tower in adsorption, one in regeneration, one on standby | `PACKAGE_REGISTER.csv`; SCOPE_LEDGER SOW-0146 |
| Total package capacity | 2,385 m³/d (15,000 bbl/d) | `PACKAGE_REGISTER.csv`; SCOPE_LEDGER SOW-0146 |
| Service phase | Liquid-phase C3+ NGL (saturated with water at design inlet) | SCOPE_LEDGER SOW-0146, SOW-0148 |
| Outlet specification | <7 ppmw water in dry NGL | SCOPE_LEDGER SOW-0146 |
| Adsorbent type | 3A molecular sieve with silica gel protective layer for liquid carryover | SCOPE_LEDGER SOW-0147 |
| Inlet conditioning | Liquid/liquid coalescer(s) with coalesced water level control to produced water | SCOPE_LEDGER SOW-0147 |
| Regeneration gas system | Regeneration-gas heating; aerial cooler with automated warm-air recirculation louvers, automated intake louvers, and plenum heating bundle for winterization (split-header design); three-phase scrubber with mist pad; pressure relief provisions | SCOPE_LEDGER SOW-0147 |
| Outlet filtration | Particulate filtration on dry NGL leaving the dehydrator | SCOPE_LEDGER SOW-0147 |
| Analyzers | Moisture analyzer with vaporizing regulator for C3+ sampling system (one) | SCOPE_LEDGER SOW-0147 |
| Enclosure | Heated building/enclosure housing inlet gas coalescer, inline mixers, settling vessel, and regeneration gas scrubber as required by final heater/scrubber location and area classification | SCOPE_LEDGER SOW-0147 |
| Modularization | TBD (not stated in accessible source slices) | TBD |
| Tagged equipment list | TBD — per-vessel tags not stated in accessible source slices; to be issued in DEL-070-02 Package Datasheet | TBD; ASSUMPTION (handoff scope) |
| Materials | TBD (sour-service NACE and NGL-service materials not stated in accessible source slices) | TBD |

## Conditions (Process Design Basis)

| Parameter | Value | Source |
|---|---|---|
| Service | Water-saturated C3+ NGL (liquid phase) | SCOPE_LEDGER SOW-0146, SOW-0148 |
| Adsorption inlet design pressure | 1,978 kPag (low/high TBC) | SCOPE_LEDGER SOW-0148 (per latest DBM SEC-07) |
| Adsorption outlet design pressure | 1,943 kPag (low/high TBC) | SCOPE_LEDGER SOW-0148 |
| Adsorption inlet temperature (low / design / high) | 29.7 / 46.3 / 51.8 °C | SCOPE_LEDGER SOW-0148 |
| Adsorption inlet water content | Saturated at design inlet conditions and flow | SCOPE_LEDGER SOW-0148 |
| Bed pressure drop, start-of-life | < 4 psid (27.6 kPad) | SCOPE_LEDGER SOW-0148 |
| Bed pressure drop, end-of-life (incl. vessel nozzles) | < 10 psid | SCOPE_LEDGER SOW-0148 |
| Cycle basis — adsorption | 24 hours (preliminary) | SCOPE_LEDGER SOW-0148 |
| Cycle basis — draining, heating ramp, regeneration pre-heat/hold, heating, cooling, filling, standby, total regeneration cycle | TBC by vendor | SCOPE_LEDGER SOW-0148 |
| Regeneration-side conditions | TBD (not enumerated in accessible source slice; source text truncated at "Regeneration side. Design conditions:") | TBD |
| Adsorbent life | TBD (not stated in accessible source slice for NGL service) | TBD |

## Construction (Package Boundaries and Battery Limits)

| Element | Statement | Source |
|---|---|---|
| Package boundary scope | Vendor-engineered NGL molecular sieve dehydration package supplied as a unit with vendor engineering, design, vendor documentation, and physical equipment | `PACKAGE_REGISTER.csv` ResponsibilityModel; OBJ-004 |
| Tie-in provisions at battery limits | Package utility, electrical, flare, drain, and control-system tie-in provisions to package battery limits | SCOPE_LEDGER SOW-0147 |
| Facility-level integration | Owned by EPC Integrator: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Applicable interface types (12) | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` rows for PKG-070; `PACKAGE_REGISTER.csv` InterfaceTypes |
| Excluded by others (upstream) | NGL mercaptan treating process package and caustic process-provider design | SCOPE_LEDGER SOW-0148 |
| Excluded by others (downstream) | NGL storage bullets, NGL loading, LACT, and product export systems; Sales gas compressors and stabilizer overheads compressor package | SCOPE_LEDGER SOW-0148 |
| Excluded by others (utility) | Produced-water tank, produced-water drain header, and facility drain infrastructure beyond package nozzles/tie-ins; Flare header | SCOPE_LEDGER SOW-0148 |
| Package-level exclusions stated | No package-specific exclusions stated in source materials beyond the "by others" list above | `PACKAGE_REGISTER.csv` Exclusions ("TBD; no package-specific exclusions stated in source materials") |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative decomposition basis and source root
- `_DEPENDENCIES.md` — declared upstream/downstream (none declared at PREPARATION)
- `DELIVERABLE_REGISTER.csv` (GATE-07) — row `DEL-070-01_scope-of-work`
- `PACKAGE_REGISTER.csv` (GATE-07) — row `PKG-070`
- `SCOPE_LEDGER.csv` (GATE-07) — rows `SOW-0145`, `SOW-0146`, `SOW-0147`, `SOW-0148`
- `INTERFACE_REGISTER.csv` (GATE-07) — 12 PKG-070 interface rows
- `OBJECTIVE_REGISTER.csv` (GATE-07) — OBJ-001, OBJ-003..OBJ-010
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 — process-gas molecular sieve basis (analogous design, NOT direct authority for the NGL package)
- `_Sources/26020-Package_Requirements.docx` package heading 24 — cited but **not locally accessible as text slice** (location TBD)
- `Bid Docs/Budgetary/26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx` — NGL-specific RFQ; **not present in `_Sources/`** (location TBD)
