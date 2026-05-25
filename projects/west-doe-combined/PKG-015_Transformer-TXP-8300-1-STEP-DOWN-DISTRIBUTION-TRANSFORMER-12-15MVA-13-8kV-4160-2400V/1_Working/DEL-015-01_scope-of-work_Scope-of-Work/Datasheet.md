# Datasheet — DEL-015-01 Scope of Work (PKG-015)

> Type: Descriptive datasheet for the EPC Integrator Scope of Work for PKG-015 Transformer TXP-8300-1.
> Authority: Workbook Packages row 17 (decomposition row); DBM section "Incoming Power and Transformers" (3-25 Comp_and_Liquids DBM L738–L750).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-015-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | DELIVERABLE_REGISTER.csv |
| ParentPackageID | `PKG-015` | PACKAGE_REGISTER.csv |
| Package Name | Transformer TXP-8300-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 12/15MVA 13.8kV/4160/2400V | PACKAGE_REGISTER.csv (Workbook row 17) |
| Tag | TXP-8300-1 | Package name (Workbook row 17) |
| WBS | 02 (26020-02-30-006) | PACKAGE_REGISTER.csv |
| Discipline | Electrical | PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| Covers Scope Items | SOW-0016 | `_CONTEXT.md` |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` |

## Attributes (package identity as carried in source)

| Attribute | Value | Source |
|---|---|---|
| Equipment class | Step-down distribution transformer (oil-filled assumed) | Package name; DBM L2947–L2949 (general transformer basis) — ASSUMPTION: oil-filled per DBM convention for MV transformers |
| Nameplate rating | 12/15 MVA (ONAN/ONAF inferred) | Package name (Workbook row 17). ASSUMPTION: dual rating denotes self-cooled / forced-air-cooled stages; location TBD in vendor scope |
| Primary voltage | 13.8 kV, 3-phase, 60 Hz | Package name; DBM L732, L744 |
| Secondary voltage(s) | 4,160 V and 2,400 V | Package name (Workbook row 17). DBM L744 confirms 4.16 kV; 2,400 V not directly described in accessible DBM text — `location TBD` |
| Grounding | Low-resistance grounded (LRG) on MV per DBM | DBM L732–L733 |
| Service | 4,160 V MCC for 4,000 V class motors (KM-2150, KM-2250 noted) | DBM L744, L754 |
| Sub-fed from | 04-25 13.8 kV Main Switchgear | DBM L740 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility | 03-25 Compressor Station and Liquids Hub | DBM section header |
| Area classification (general) | Class I, Zone 2, Gas Groups IIA/IIB | DBM L722 |
| Standby/emergency power basis | LV standby generators on 600 V MCC with transfer switch (no MV emergency feed to TXP-8300-1) | DBM L505, L762 |
| Cross-facility electrical interface | Primary feed from 04-25; coordination required | DBM L740 |

## Construction (package boundary as EPC scope)

The Scope of Work artifact does not itself construct the transformer. It documents the EPC Integrator's responsibility for integrating the vendor-supplied transformer package into the facility. Construction elements that this artifact must enumerate:

- Tagged equipment list (transformer TXP-8300-1 and any package-bundled auxiliaries — vendor-defined; `location TBD`).
- Package function within the 03-25 power distribution architecture (step-down from 13.8 kV bus to 4,160 V MCC and to 2,400 V loads — 2,400 V load list is `TBD`).
- Boundaries: vendor scope (engineering, design, vendor documentation, physical equipment package) vs. EPC Integrator scope (foundations, grounding, tie-ins, cabling, area lighting, control cabling, communications, maintenance access, structural supports). Source: PACKAGE_REGISTER.csv "Applicable interface types".
- Whole-facility integration narrative covering the seven applicable interface types (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports).

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `PACKAGE_REGISTER.csv` row PKG-015 (Gate 7 snapshot)
- `DELIVERABLE_REGISTER.csv` row DEL-015-01
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC "Incoming Power and Transformers" (L738–L750), System Voltages (L728–L736), Area Classification (L720–L726)
- Workbook Packages row 17 (referenced by decomposition; raw workbook not separately read here)

## TBD / Open Items

- 2,400 V service: load list, grounding basis, and tap arrangement — `location TBD` (not present in accessible DBM slices).
- Cooling class (ONAN/ONAF vs. KNAN, etc.) — `ASSUMPTION`, vendor-defined.
- Impedance, BIL, taps, vector group, NLTC/OLTC selection — `TBD` (vendor scope; not in EPC SoW unless EPC pre-specifies).
- Secondary containment requirements — `TBD` per DBM L2949 reference (general policy).
