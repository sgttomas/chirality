# Datasheet — DEL-026-01 Scope of Work (PKG-026)

> Type: Descriptive datasheet for the EPC Integrator Scope of Work for PKG-026 Transformer TXP-8300-2.
> Authority: Workbook Packages row 28 (decomposition row); Gate 7 PROJECT_DECOMP snapshot registers; 3-25 Comp_and_Liquids DBM (general facility electrical basis only — does not directly enumerate this package's rating; see Guidance Conflict Table).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-026-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | DELIVERABLE_REGISTER.csv (DEL-026-01) |
| ParentPackageID | `PKG-026` | PACKAGE_REGISTER.csv |
| Package Name | Transformer TXP-8300-2 — STEP DOWN DISTRIBUTION TRANSFORMER — 20/26MVA 13.8kV/6.9kV/0.4kV | PACKAGE_REGISTER.csv (Workbook row 28) |
| Tag | TXP-8300-2 | Package name (Workbook row 28) |
| WBS | 02 (26020-02-30-017) | PACKAGE_REGISTER.csv |
| Discipline | Electrical | PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| Covers Scope Items | SOW-0027 | `_CONTEXT.md` |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` |

## Attributes (package identity as carried in source)

| Attribute | Value | Source |
|---|---|---|
| Equipment class | Step-down distribution transformer (oil-filled assumed) | Package name; DBM general transformer convention — ASSUMPTION: oil-filled per MV transformer convention; vendor to confirm |
| Nameplate rating | 20/26 MVA (ONAN/ONAF inferred) | Package name (Workbook row 28). ASSUMPTION: dual rating denotes self-cooled / forced-air-cooled stages; vendor to confirm |
| Primary voltage | 13.8 kV, 3-phase, 60 Hz | Package name; DBM L728–L736 (general 03-25 13.8 kV system) |
| Secondary voltage(s) | 6.9 kV and 0.4 kV (400 V) | Package name (Workbook row 28). Neither 6.9 kV nor 0.4 kV service is directly described in the accessible 3-25 DBM slices — `location TBD` |
| Grounding (MV) | Low-resistance grounded on 13.8 kV primary system | DBM L732 (general 03-25 MV grounding basis); secondary grounding `TBD` |
| Service | Sub-distribution transformer feeding 6.9 kV and 0.4 kV loads (specific load list `TBD`) | Workbook row 28 (package title only). Accessible DBM does not enumerate 6.9 kV or 0.4 kV bus loads for 03-25. |
| Sub-fed from | 03-25 13.8 kV system (sub-fed from 04-25 13.8 kV Main Switchgear per facility convention) | DBM L740 (facility incoming-power basis); package-specific feed not separately confirmed in accessible source set |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility | 03-25 Compressor Station and Liquids Hub | PACKAGE_REGISTER.csv (DBM-Comp_and_Liquids/3-25 reference) |
| Area classification (general facility) | Class I, Zone 2, Gas Groups IIA/IIB | DBM L720–L726 |
| Standby/emergency power basis (facility) | LV standby generators on 600 V MCC with transfer switch (no MV emergency feed identified for TXP-8300-2 in accessible sources) | DBM L505, L762 |
| Cross-facility electrical interface | Sub-fed via 03-25 13.8 kV system from 04-25 Main Switchgear (general facility basis) | DBM L740 |

## Construction (package boundary as EPC scope)

The Scope of Work artifact does not itself construct the transformer. It documents the EPC Integrator's responsibility for integrating the vendor-supplied transformer package into the facility. Construction elements that this artifact must enumerate:

- Tagged equipment list (transformer TXP-8300-2 and any package-bundled auxiliaries — vendor-defined; `location TBD`).
- Package function within the 03-25 power distribution architecture (step-down from 13.8 kV bus to 6.9 kV and 0.4 kV services per package title — load assignments are `TBD` in accessible sources).
- Boundaries: vendor scope (engineering, design, vendor documentation, physical equipment package) vs. EPC Integrator scope (foundations, grounding, tie-ins, cabling, area lighting, control cabling, communications, maintenance access, structural supports). Source: PACKAGE_REGISTER.csv `Vendor_EPC_Boundary` for PKG-026.
- Whole-facility integration narrative covering the seven applicable interface types (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports).

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `PACKAGE_REGISTER.csv` row PKG-026 (Gate 7 snapshot)
- `DELIVERABLE_REGISTER.csv` row DEL-026-01
- `ARTIFACT_REGISTER.csv` rows for DEL-026-01 (ART-F154B8A581, ART-AA91097B6C, ART-CDB03DA424, ART-CCD4B8B930)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC System Voltages (L728–L736), Incoming Power and Transformers (L738–L750), Area Classification (L720–L726), Standby Power (L505, L762)
- Workbook Packages row 28 (referenced by decomposition; raw workbook not separately read here)

## TBD / Open Items

- 6.9 kV service: load list, grounding basis, switchgear assignment — `location TBD` (not present in accessible DBM slices).
- 0.4 kV (400 V) service: load list, panelboard/MCC assignment, grounding — `location TBD`.
- Cooling class (ONAN/ONAF vs. KNAN, etc.) — `ASSUMPTION`, vendor-defined.
- Impedance, BIL, taps, vector group, NLTC/OLTC selection — `TBD` (vendor scope; not in EPC SoW unless EPC pre-specifies).
- Secondary containment requirements — `TBD` per DBM general policy (clause-level not in accessible 3-25 source set).
- Reconciliation of 20/26 MVA / 13.8/6.9/0.4 kV identity (Workbook row 28) against the accessible DBM which describes only a 12 MVA 13.8/4.16 kV unit at 3-25 — see Guidance Conflict Table.
