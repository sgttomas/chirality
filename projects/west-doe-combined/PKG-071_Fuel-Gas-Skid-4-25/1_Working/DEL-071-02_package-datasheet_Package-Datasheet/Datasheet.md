# Datasheet — DEL-071-02 Package Datasheet (Fuel Gas Skid 4-25)

EpistemicLabels in use: FACT, ASSUMPTION, TBD.

## Identification

| Field | Value | Provenance |
|---|---|---|
| Deliverable ID | `DEL-071-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 331 |
| Parent Package ID | `PKG-071` | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 61 |
| Workbook ID | 71 | PACKAGE_REGISTER.csv row 61 |
| Workbook Row | 61 | PACKAGE_REGISTER.csv row 61 |
| WBS | 01 | PACKAGE_REGISTER.csv row 61 |
| CoA Tracking Number | 26020-01-23-001 | PACKAGE_REGISTER.csv row 61 |
| Package Name | Fuel Gas Skid 4-25 | PACKAGE_REGISTER.csv row 61 |
| Package Function | Skid will serve the low-pressure fuel gas system for the West Doe Deep Cut Facility. | SCOPE_LEDGER.csv `SOW-0100`; 26020-Package_Requirements.docx package heading 25 (Basic scope) |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row 61 |
| Type | EPC Package Datasheet | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 331 |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Package Vendor Role | Owns package engineering, package design, vendor documentation, and the physical equipment package | PACKAGE_REGISTER.csv row 61 (Responsibility) |
| EPC Integrator Role | Owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv row 61 (Responsibility) |

## Attributes (Package Composition)

| Attribute | Value | Provenance |
|---|---|---|
| Package configuration | 1 skid-mounted Low Pressure Fuel Gas Package | SCOPE_LEDGER.csv `SOW-0100`; 26020-Package_Requirements.docx package heading 25 (Basic scope) |
| Major equipment item | 1 Low-pressure fuel gas heater | SCOPE_LEDGER.csv `SOW-0100`; `SOW-0101` |
| Major equipment item | 1 Low-pressure fuel gas scrubber | SCOPE_LEDGER.csv `SOW-0100`; `SOW-0101` |
| Skid | A skid for the system to be mounted on | SCOPE_LEDGER.csv `SOW-0101` (Major included equipment) |
| Heater capacity | TBD (capacity not stated in source) | SCOPE_LEDGER.csv `SOW-0101` |
| Heater control | Heater controlled by SCR (600 V); heater shall include skin-temperature thermocouple override control | SCOPE_LEDGER.csv `SOW-0101` |
| Scrubber sizing basis | Sized using a k factor of 0.35 (imperial) maximum, plus de-ration factor for operating pressure; Vendor to design | SCOPE_LEDGER.csv `SOW-0101` |

## Conditions (Process / Operating / Design)

| Parameter | Value | Provenance |
|---|---|---|
| Design flow required | > 8.4 MMSCFD (237.5 e3m3/day) | SCOPE_LEDGER.csv `SOW-0102` (Capacity/design throughput) |
| Gas outlet temperature (heated to) | 95 F (35 C) | SCOPE_LEDGER.csv `SOW-0102` |
| Final flow | TBD | SCOPE_LEDGER.csv `SOW-0102` |
| Operating pressure | 150 psig | SCOPE_LEDGER.csv `SOW-0102` (Operating conditions) |
| Ambient temperature range | -19 C to 22.2 C | SCOPE_LEDGER.csv `SOW-0102` |
| Design pressure | 150 psig | SCOPE_LEDGER.csv `SOW-0102` (Design conditions) |
| Design temperature range | -40 C to 35 C | SCOPE_LEDGER.csv `SOW-0102` |
| MAWP | TBD | SCOPE_LEDGER.csv `SOW-0102` |
| Driver / power | SCR heater control panels are 600 V, located in electrical building | SCOPE_LEDGER.csv `SOW-0102` |

## Construction / Battery Limits / Interfaces

Workbook X-column interface facts for `PKG-071` are carried in this datasheet as evidence for vendor handoff (INTERFACE_REGISTER.csv rows 453-464, all `Applicable=YES`, source: Workbook Packages row 61).

| Interface Type | Applicable | Interface ID | Provenance |
|---|---|---|---|
| Process Piping | YES | `IFC-2E4D1DF06E` | INTERFACE_REGISTER.csv row 453 |
| Utility Piping | YES | `IFC-726500493C` | INTERFACE_REGISTER.csv row 454 |
| Relief / Flare / Vent | YES | `IFC-392BE6E532` | INTERFACE_REGISTER.csv row 455 |
| Drain / Containment | YES | `IFC-F69E23A0EA` | INTERFACE_REGISTER.csv row 456 |
| Electrical Power | YES | `IFC-5AB340F539` | INTERFACE_REGISTER.csv row 457 |
| Grounding / Bonding | YES | `IFC-58E35CBB07` | INTERFACE_REGISTER.csv row 458 |
| Area / Exterior Lighting | YES | `IFC-65D375A602` | INTERFACE_REGISTER.csv row 459 |
| I&C / Control Cabling | YES | `IFC-6DFB82A890` | INTERFACE_REGISTER.csv row 460 |
| Building HVAC / Services | YES | `IFC-DAB6B71A54` | INTERFACE_REGISTER.csv row 461 |
| Fire & Gas / Safety Systems | YES | `IFC-7667708987` | INTERFACE_REGISTER.csv row 462 |
| Maintenance Access | YES | `IFC-B1A9FA92D4` | INTERFACE_REGISTER.csv row 463 |
| Structural / Foundations / Supports | YES | `IFC-85BC26C1D5` | INTERFACE_REGISTER.csv row 464 |

By-others / out-of-vendor-scope (carry into EPC integration):
- Shipping packages to site, installation, tie-in piping, electrical tie-in, etc. — `SOW-0102` (Scope notes and open items).

## Open Items / TBD Set

- Heater capacity — TBD (`SOW-0101`).
- Final gas flow — TBD (`SOW-0102`).
- MAWP — TBD (`SOW-0102`).
- Package-specific exclusions beyond the by-others list — TBD; PACKAGE_REGISTER row 61 records "no package-specific exclusions stated in source materials."
- Clause-level Codes & Standards references for sour-service / Mechanical pressure equipment — ASSUMPTION: governed by Deepcut DBM SEC-09, SEC-14, SEC-15 (location TBD; full DBM section text not slice-read in this run).

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row 331
  - `PACKAGE_REGISTER.csv` row 61
  - `SCOPE_LEDGER.csv` rows 100-103 (`SOW-0099`..`SOW-0102`)
  - `INTERFACE_REGISTER.csv` rows 453-464
  - `ARTIFACT_REGISTER.csv` rows 2785-2799 (datasheet-scoped artifacts)
  - `OBJECTIVE_REGISTER.csv` rows for `OBJ-001`, `OBJ-004`..`OBJ-010`
- Source root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/`
  - `26020-Package_Requirements.docx` package heading 25 (extracted into `SOW-0099`..`SOW-0102`; raw .docx not slice-read directly in this run — ASSUMPTION that SCOPE_LEDGER extractions faithfully represent the source heading).
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` (referenced through OBJECTIVE_REGISTER; not slice-read in this run).
