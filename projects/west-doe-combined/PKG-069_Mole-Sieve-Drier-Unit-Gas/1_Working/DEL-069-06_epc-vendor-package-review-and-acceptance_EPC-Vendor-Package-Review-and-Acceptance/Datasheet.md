# Datasheet — DEL-069-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-069-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-069` |
| PackageName | Mole Sieve Drier Unit (Gas) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| ParentObjectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic) |
| Covers Scope Items | SOW-0144 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Final dehydration of process gas upstream of cryogenic recovery (mole-sieve adsorption + regeneration + dust filtration + mercury removal protective dust filter) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-06 "Molecular-Sieve Dehydration and Mercury Removal Basis" |
| Adsorber configuration | Three driers: two in adsorption, one in standby/regeneration/cooling; downflow on adsorption | DBM-Deepcut SEC-06 "Molecular-Sieve Bed and Regeneration Basis" |
| Adsorbent | 3A molecular sieve mandatory; 4A and 5A not permitted (H2S adsorption risk → sulphur spikes in regen loop) | DBM-Deepcut SEC-06 |
| Inlet capacity basis | Bed table totals 332.6 MMSCFD adsorption + 25.45 MMSCFD regeneration flow | DBM-Deepcut SEC-06 |
| Per-bed flow | Bed 1 adsorption 166.3 MMSCFD; Bed 2 adsorption 166.3 MMSCFD; Bed 3 regen/cool 25.45 MMSCFD | DBM-Deepcut SEC-06 |
| Preliminary cycle times | Adsorption 54 h; total regeneration cycle 7.6 h (heating ramp 0.2 h; preheat/hold 1 h; heating ramp 0.4 h; heating 3 h; cooling 3 h; standby 38.8 h preliminary) | DBM-Deepcut SEC-06 |
| Bed sizing | 9.5 ft ID adsorber bed basis; regeneration tower vertical 8 ft x 20 ft | DBM-Deepcut SEC-06 |
| Inlet filter coalescers | Two 100% filter/coalescers on independent module with building; basis assumes no bulk free liquids at inlet | DBM-Deepcut SEC-06 |
| Regeneration gas compressor | Single-stage vertical inline centrifugal; 25 MMSCFD basis; 2 x 100% with installed standby; assumed design differential 100 psid (detailed loop totals 79.5 psid) | DBM-Deepcut SEC-06 |
| Regeneration gas heater | BEU heat-medium/process-gas S&T exchanger; regen temperature 450 degF (system overview) / 460 degF (heater detail) — UNRESOLVED | DBM-Deepcut SEC-06 |
| Regeneration gas scrubber | Two-phase scrubber with mist pad; separated water gap-level controlled to produced-water drain; installed inside building | DBM-Deepcut SEC-06 |
| Dust filters | Mol-sieve dust filter and MRU dust filter each 1 x 100%; capacity main + regen gas; 2 psid clean dP; manual bypass for online change-out | DBM-Deepcut SEC-06 |
| Mercury Recovery Unit (downstream) | Protects BAHX from elemental mercury; protected by dust filters | DBM-Deepcut SEC-06 Process Controls |
| Flange class | 900# flanges required for molecular-sieve system | DBM-Deepcut SEC-04 §"Inlet Pipeline Pressure and Flow" |
| Sales-gas water spec downstream | < 0.1 ppmv (achieved via upstream molecular sieve dehydration) | DBM-Deepcut SEC-05 "Sales Gas Booster Design Conditions" |
| Thermal efficiency target | Molecular-sieve regeneration thermal efficiency target < 40% | DBM-Deepcut SEC-06 |
| Recycle return path | Saturated regeneration gas normally returns upstream of TEG inlet coalescer; alternate normally-closed path returns immediately upstream of mole-sieve coalescers | DBM-Deepcut SEC-06 |
| Blowdown | Operator-initiated HMI blowdown only; two blowdown valves (regen + adsorption loops); 50 psi/min max; regen compressor bypass prevents reverse rotation | DBM-Deepcut SEC-06 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Upstream inlet gas | Sweet, TEG-dehydrated process gas; <=10 lb H2O/MMSCF acceptable to mole-sieve unit | DBM-Deepcut SEC-06 "TEG Design Values" |
| Required outlet water content | Cryogenic-service quality (sub-ppmv basis; <0.1 ppmv reflected in downstream sales-gas spec) | DBM-Deepcut SEC-05 / SEC-06 |
| Mol-sieve inlet pressure | TBD (open item) | DBM-Deepcut SEC-06 "Molecular-Sieve Open Items and Assumptions" |
| Mol-sieve inlet temperature | TBD (final estimates open) | DBM-Deepcut SEC-06 open items |
| Adsorbent life | TBD | DBM-Deepcut SEC-06 open items |
| Dry-out header operating pressure / MAWP | TBD | DBM-Deepcut SEC-06 open items |

## Construction (Acceptance Artifacts)

Per `_CONTEXT.md` anticipated artifacts list:

- Vendor document review log
- Package acceptance checklist
- Test and inspection evidence
- Turnover evidence

Acceptance is performed by the EPC Integrator against the EPC Scope of Work (DEL-069-01), the EPC Package Datasheet (DEL-069-02), and the Construction Work Package (DEL-069-03). Vendor inputs are the Vendor Engineered Equipment Package (DEL-069-04) and the Vendor Document Turnover Package (DEL-069-05). Configuration baseline values for review use are the Attributes/Conditions tables above.

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-04 §Inlet Pipeline Pressure and Flow; SEC-05 §Sales Gas Booster Design Conditions; SEC-06 §Molecular-Sieve Dehydration and Mercury Removal Basis (Process Description, Design Values, Bed and Regeneration Basis, Equipment Controls and Protection, Open Items, Process Controls and Protective Functions).
- Gate 7 Final Published PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Sibling deliverables in PKG-069: DEL-069-01..05 (acceptance basis and vendor inputs).
- TBD: `26020-Package_Requirements.docx` package heading for PKG-069 (binary source; location TBD — not text-accessible during this run).
