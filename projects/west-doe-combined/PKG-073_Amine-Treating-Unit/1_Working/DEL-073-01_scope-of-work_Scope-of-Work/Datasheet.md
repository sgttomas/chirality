# Datasheet — DEL-073-01 Scope of Work (PKG-073 Amine Treating Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-073-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | PKG-073 Amine Treating Unit | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-073 |
| Workbook Row | 49 | `PACKAGE_REGISTER.csv` row PKG-073 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Tracking Number | 26020-01-27-001 | `PACKAGE_REGISTER.csv` |
| CoA Tracking | 26020-01-PT-27-001 — Amine Treating Unit | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Source Basis (Word) | 26020-Package_Requirements.docx package heading 27 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Source Basis (Workbook) | 26020-Packages_Interfaces_4_export.xlsx, Packages row 49 | `PACKAGE_REGISTER.csv` |
| Source Basis (Bid Docs) | Bid Docs/Budgetary/26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx | `PACKAGE_REGISTER.csv` (location TBD — file not in `_Sources`) |
| Design Basis Reference | DBM-Deepcut/4-25_Deepcut_DBM.md | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Removes H₂S and CO₂ from sour natural gas using a continuous MDEA absorption-regeneration cycle, operating across two modules | `SCOPE_LEDGER.csv` SOW-0052; `PACKAGE_REGISTER.csv` |
| Module 1 | Amine Gas Sweetening — conditions sour inlet gas and contacts it with lean MDEA solvent to produce pipeline-quality sweet gas | `SCOPE_LEDGER.csv` SOW-0052 |
| Module 2 | Amine Regeneration — thermally regenerates the rich amine, returning lean solvent | `SCOPE_LEDGER.csv` SOW-0052 |
| Vendor Scope of Supply | Complete Amine Treating Unit (ATU) | `SCOPE_LEDGER.csv` SOW-0052 |
| Vendor Ownership | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv`; OBJ-004 |
| EPC Integrator Ownership | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv`; OBJ-004 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour natural gas (H₂S, CO₂) | `SCOPE_LEDGER.csv` SOW-0052 |
| Solvent | MDEA (continuous absorption-regeneration cycle) | `SCOPE_LEDGER.csv` SOW-0052 |
| Capacity / Design Throughput | See Appendix A (source-referenced; appendix not locally accessible) — `location TBD` | `SCOPE_LEDGER.csv` SOW-0054 |
| Operating Conditions | TBD (source SOW-0054 records "Operating conditions: -") | `SCOPE_LEDGER.csv` SOW-0054 |
| Design Conditions | See Appendix A (source-referenced; appendix not locally accessible) — `location TBD` | `SCOPE_LEDGER.csv` SOW-0054 |
| Motor Voltage (1–200 HP) | 600 V / 3-phase / 60 Hz | `SCOPE_LEDGER.csv` SOW-0054 |
| Motor Voltage (>200 HP) | 4160 V or 6900 V / 3-phase / 60 Hz | `SCOPE_LEDGER.csv` SOW-0054 |
| VFD-Ready Threshold | All motors 100 HP and above | `SCOPE_LEDGER.csv` SOW-0054 |

## Construction

### Tagged / Major Included Equipment (source-extracted; non-exhaustive)

| Tag / Item | Description | Source |
|---|---|---|
| Amine Inlet Filter Coalescer | 2 × 100% (piping configured so one filter is always operational); 0.3 micron @ 99.97%; single phase; c/w Bandlock Type QOC; pressure drop < 2 psid clean | `SCOPE_LEDGER.csv` SOW-0053 |
| Additional Amine Gas Sweetening Module equipment | TBD — source enumeration in 26020-Package_Requirements.docx heading 27 not fully extracted into accessible registers | `SCOPE_LEDGER.csv` SOW-0053; `location TBD` |
| Amine Regeneration Module equipment | TBD — source enumeration in 26020-Package_Requirements.docx heading 27 not fully extracted into accessible registers | `SCOPE_LEDGER.csv` SOW-0052; `location TBD` |

### Package Interfaces (in scope per `INTERFACE_REGISTER.csv`)

| Interface Type | Source |
|---|---|
| Process Piping | IFC-9FC19F5C81 |
| Utility Piping | IFC-683A71BA21 |
| Relief / Flare / Vent | IFC-F60A89A405 |
| Drain / Containment | IFC-145D8BEE6D |
| Electrical Power | IFC-55F378C7A7 |
| EHT | IFC-EFD6ABDF06 |
| Grounding / Bonding | IFC-97216F9B13 |
| Area / Exterior Lighting | IFC-A4EE590144 |
| I&C / Control Cabling | IFC-99C905DDB2 |
| Building HVAC / Services | IFC-A22A16E064 |
| Fire & Gas / Safety Systems | IFC-255520DB5E |
| Maintenance Access | IFC-1CE433E603 |
| Structural / Foundations / Supports | IFC-507460CABF |

### By Others (excluded from package vendor scope)

| Item | Source |
|---|---|
| Shipping packages to site | `SCOPE_LEDGER.csv` SOW-0054 |
| Installation on piles | `SCOPE_LEDGER.csv` SOW-0054 |
| Tie-in piping | `SCOPE_LEDGER.csv` SOW-0054 |
| Electrical connections | `SCOPE_LEDGER.csv` SOW-0054 |
| Mounting platform and stairs etc. | `SCOPE_LEDGER.csv` SOW-0054 |
| Process water pumps and tanks (handled separately) | `SCOPE_LEDGER.csv` SOW-0054 |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- GATE-07 PROJECT_DECOMP snapshot:
  - `PACKAGE_REGISTER.csv` row PKG-073
  - `DELIVERABLE_REGISTER.csv` row DEL-073-01_scope-of-work
  - `SCOPE_LEDGER.csv` rows SOW-0051..SOW-0054
  - `INTERFACE_REGISTER.csv` PKG-073 rows
  - `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-003..OBJ-010
- Source workbook: `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; consumed via decomposition extract)
- Source Word doc: `_Sources/26020-Package_Requirements.docx` package heading 27 (binary; consumed via decomposition extract — full clause-level text not locally accessible in markdown form, `location TBD` for direct quotations)
