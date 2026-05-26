# Datasheet: DEL-084-04 — Vendor Engineered Equipment Package (Fuel Gas Skid)

> Pass 1/2 source-grounded draft. Substantive numeric values cite the locally accessible
> Design Basis Memorandum (DBM) source slices. Items not resolvable from local sources
> are marked `TBD`. Inferences are labeled `ASSUMPTION`. See `Guidance.md` Conflict Table
> for the package-naming reconciliation issue (CONFLICT C-01).

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-084-04_vendor-engineered-equipment-package` |
| Deliverable Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-084` |
| Package Name (as decomposed) | Fuel Gas Skid 3-25 |
| Anchor Equipment Tags (per source) | `H-3275-1` (LP Fuel Gas Heater), `V-3210-1` (LP Fuel Gas Scrubber); `V-3210-2` is the 03-25 LP Fuel Gas Scrubber tag in the 03-25 DBM. See CONFLICT C-01 in `Guidance.md`. |
| Discipline | Mechanical (with Process / Electrical / Instrumentation interfaces) |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering/design/equipment supply), with EPC Integrator integration review |
| Anticipated Artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set |
| Covers Scope Items | `SOW-0095`, `SOW-0096`, `SOW-0097`, `SOW-0098` |
| Supports Objectives (PACKAGE_HEURISTIC; ASSUMPTION) | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Decomposition Source | Workbook Packages row 60; `26020-Package_Requirements.docx` package heading 37 (heading text not locally re-read; `.docx` not parsed in this run) |
| Authoritative DBM Source (accessible) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Attributes

The fuel-gas system attributes below are drawn from accessible DBM source slices. Where the source explicitly carries `TBC`/`TBD`, that disposition is preserved.

### Service Function (from `4-25_Deepcut_DBM.md`, section "Fuel Gas Basis" and "Fuel Gas Equipment and Controls")

| Attribute | Value | Source |
|---|---|---|
| System service | Low-pressure fuel gas distribution to plant users | 4-25 DBM, "Fuel Gas Basis" |
| Primary users | TEG stripping, blanketing, purge, dilution/enrichment gas, building heaters, generator fuel, flare pilots/purge, compressor purge/sweep | 4-25 DBM "Utilities Overview" table; 3-25 DBM "Fuel Gas" |
| Normal fuel-gas source | Plant fuel gas upstream of the expander-compressor; no normal bulk filtration required | 4-25 DBM "Fuel Gas Design Values" |
| Secondary / buyback source | Emergency buyback from sales-gas pipelines (Enbridge / Alliance / TCPL) | 4-25 DBM "Emergency Buyback and Purge"; 3-25 DBM "Fuel Gas" |

### Pressure/Flow Basis (from `3-25_Comp_and_Liquids_DBM.md`, "Fuel Gas")

| Source | Normal Pressure | Maximum Pressure | MAWP |
|---|---:|---:|---:|
| Enbridge | 5,171 kPag (750 psig) | 5,516 kPag (800 psig) | 9,928 kPag (1,440 psig) |
| Alliance | 5,516 kPag (800 psig) | 8,274 kPag (1,200 psig) | 9,928 kPag (1,440 psig) |

| Flow Parameter | Value | Source |
|---|---|---|
| LP fuel-gas normal total flow | 1.382 MMSCFD (39.13 e3m3/d) | 3-25 DBM "Fuel Gas" |
| LP fuel-gas design flow | > 1.5 MMSCFD (> 42.5 e3m3/d) — design value `TBC` | 3-25 DBM "Fuel Gas" |
| Emergency-generator fuel design flow | 0.468 MMSCFD (13.2 e3m3/d) — `TBC` in detailed engineering | 4-25 DBM "Fuel Gas Equipment and Controls" |
| Emergency-generator start-gas flow | 3.6 MMSCFD for 30 s — `TBC` | 4-25 DBM "Fuel Gas Equipment and Controls" |
| Emergency-generator supply pressure ceiling | < 66 psig (general-purpose classification) | 4-25 DBM "Fuel Gas Equipment and Controls" |
| Buyback gas MAOP estimate | 9,928 kPag — requires detailed-engineering verification | 4-25 DBM "Emergency Buyback and Purge" |

### Conditions

| Attribute | Value | Source |
|---|---|---|
| Design ambient temperature envelope | -40 deg C to +35 deg C (governs exposed equipment, package buildings, control panels, instrumentation, field devices unless a stricter package basis applies) | 3-25 DBM site basis |
| Water content (J-T mode) | Less than 0.1 ppmv H2O | 4-25 DBM "Fuel Gas Design Values" |
| Heater duty | `TBD` | 4-25 DBM "Fuel Gas Equipment and Controls" |
| Scrubber K factor (max) | 0.35 Imperial, with operating-pressure derating | 4-25 DBM "Fuel Gas Equipment and Controls"; consistent with 3-25 DBM V-3210-2 (K = 0.35) |
| Sulphur / mercaptan hazard basis | Sweet-gas purge from fuel-gas system; methyl-mercaptan toxicity and odour relevant to purge/analyzer/operations; formal hazard review required before finalizing | 3-25 DBM "Fuel-Gas Sulphur and Purge Hazard Basis" |

## Construction

| Attribute | Value | Source |
|---|---|---|
| LP fuel-gas heater | Electric resistance heater, SCR-controlled; sized for max sales-compressor discharge pressure and winter ambient buyback gas conditions; includes skin-temperature thermocouple override and gas outlet temperature control to prevent overheating under stagnant-gas conditions | 4-25 DBM "Fuel Gas Equipment and Controls" |
| LP fuel-gas scrubber | Removes condensed liquids before distribution; condensate routes to slop tank (`TK-9130-1` per 4-25; `TK-9130-2` per 3-25); designed for fuel-gas system design flow at design operating pressure | 4-25 and 3-25 DBM "Fuel Gas" sections |
| Regulator philosophy | Minimum 2 x 100% regulator sparing; individually isolatable for maintenance; outlet pressure-test connection; pilot isolation where pilots are external; start-gas regulators are quick-acting, internally sensing (not pilot type) | 4-25 DBM "Fuel Gas Equipment and Controls" |
| Generator fuel filtration | Local fuel-gas particulate filter at the emergency generator | 4-25 DBM "Fuel Gas Design Values" |
| Material classes | `TBD` (vendor selection; must comply with H2S/sour-service governance per project DBM general material requirements — `location TBD` in this run) |
| Module / building / heat-tracing | Package shall comply with the project winterization basis (-40 deg C minimum ambient governs package buildings, panels, instrumentation, and field devices unless a more severe package basis applies) | 3-25 DBM site basis |
| Skid layout, footprint, weights | `TBD` — vendor scope |
| Painting / coating | `TBD` — vendor scope per project coating spec (`location TBD`) |

## References

- `_REFERENCES.md` (deliverable-local pointer file)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — sections "Fuel Gas", "Fuel-Gas Sulphur and Purge Hazard Basis", "Instrument Air"
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — sections "Fuel Gas Basis", "Fuel Gas Design Values", "Fuel Gas Equipment and Controls", "Emergency Buyback and Purge", "Utilities Overview"
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — heading 37 cited by `_CONTEXT.md`; `.docx` not parsed in this run (`location TBD` for clause-level requirements)
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
