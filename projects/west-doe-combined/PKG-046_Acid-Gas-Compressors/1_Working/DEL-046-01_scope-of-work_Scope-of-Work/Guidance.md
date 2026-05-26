# Guidance: DEL-046-01 — Scope of Work (PKG-046 Acid Gas Compressors)

## Purpose

This guidance document supports the EPC Integrator in producing a defensible, source-grounded Scope of Work for the Acid Gas Compressor package (`26020-01-PT-12-001`). The Scope of Work is the Gate 5 anchor deliverable that downstream package work (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance) builds upon.

Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` PKG-046 rows.

## Principles

1. **Source-anchored definition.** The Scope of Work derives its identity, capacity envelope, configuration, interfaces, and exclusions from the project source materials (PROJECT_DECOMP GATE-07 snapshot + DBM Deepcut §Compression and Acid Gas Handling). Do not introduce equipment, capacities, or interfaces that are not supported by the source. Source: `_REFERENCES.md`; SKILL authority hierarchy.
2. **Responsibility separation.** The Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. The Scope of Work must reflect this separation explicitly and avoid blurring vendor scope into EPC scope. Source: `PACKAGE_REGISTER.csv` Responsibility.
3. **Boundary clarity.** Battery limits at the amine regenerator outlet (suction) and the acid gas injection pipeline tie-in (discharge) are critical to scope clarity. Pipeline and disposal well are explicitly excluded from the package scope. Source: `4-25_Deepcut_DBM.md` lines 84, 1037-1061.
4. **TBD discipline.** Unresolved items (`3x50%` alternative, KBT/6 vs KBK/6, disposal well MAWP, 02-25 modification trigger, dry-out case, 5th-stage design discharge pressure reference) are surfaced as TBD with provenance and are not silently resolved. Source: `4-25_Deepcut_DBM.md` lines 878, 994-1002, 1051-1059.
5. **Derivative-package rule.** This Scope of Work is a derivative package: it cites the GATE-07 PROJECT_DECOMP snapshot and the DBM as upstream truth; it does not substitute for them. Source: SKILL precedence; project convention.

## Considerations

### Configuration ambiguity (2x100% + spare vs 3x50%)

Two configurations remain on the table per the DBM. The Scope of Work should document the 2x100% + 1 spare as the current design basis (DBM §Acid Gas Compressor Design Conditions) and explicitly note the 3x50% alternative as a TBD design decision. Treating the alternative as resolved would overcommit the EPC scope and bias vendor pricing/engineering. Source: `4-25_Deepcut_DBM.md` lines 878, 885, 994.

### Compressor model conflict (Ariel KBT/6 vs KBK/6)

The DBM cites Ariel KBT/6 with a conflicting KBK/6 reference noted as TBD. The Scope of Work should not select a model; it should reference the DBM model basis and defer model confirmation to the Package Datasheet and vendor engineering. Source: `4-25_Deepcut_DBM.md` line 995.

### Disposal well data dependency

The acid gas compressor lifetime operating conditions depend on disposal well pressure characteristics that Tourmaline (or a Tourmaline-contracted third party) must provide. The Scope of Work should flag this as an external responsibility and as a risk to vendor design freezes. Source: `4-25_Deepcut_DBM.md` lines 1049-1055.

### Shared 02-25 interface

The disposal well/reservoir is shared with the existing 02-25 facility. Incremental 04-25 acid gas volume may trigger modifications at 02-25, with both the trigger and extent unresolved. The Scope of Work should not absorb 02-25 scope but should declare the dependency. Source: `4-25_Deepcut_DBM.md` lines 93, 173, 1059.

### Sour service materials and codes

Acid gas service implies sour service materials (NACE MR0175 / ISO 15156) and likely API 618 governance for reciprocating compressor design. These are not cited explicitly in available source slices; the Scope of Work should either incorporate them via the EPC contract spec stack or leave them for the Package Datasheet to call out. Treat as ASSUMPTION until source-confirmed.

### Source-binary access

`26020-Package_Requirements.docx` (package heading 1) and `26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 48) are cited as authoritative source surfaces but are binary files not directly readable in this drafting environment. Detailed clause/row content from those sources is `location TBD` in this draft and should be reconciled in Pass 3 or in a re-run when extracted markdown slices are available.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| 2x100% + spare vs 3x50% | Reliability, footprint, capex, spares strategy; current basis 2x100%+1 spare. Resolution should be documented before vendor engineering freeze. Source: `4-25_Deepcut_DBM.md` lines 878, 885, 994. |
| Recycle-based capacity control without adjustable volume pockets | Reduces acid gas leakage points (sour-service preference) at the cost of capacity-control flexibility. Source: `4-25_Deepcut_DBM.md` line 1033. |
| Acid gas dehydration by recycle vs separate dehydration unit | DBM defers to disposal-system needs (35-60 lb H2O/MMSCF target). Pipeline hydrate prevention is a design driver; mercaptan condensation can shift the basis. Source: `4-25_Deepcut_DBM.md` lines 988, 1031. |
| Disposal metering location (high-pressure Coriolis downstream of compression) | Preferred over low-pressure metering due to lower water content and pressure drop; trades sensor service conditions against accuracy. Source: `4-25_Deepcut_DBM.md` line 1035. |
| Manual recycle-valve isolation excluded | Minimizes leakage points (sour-service); reduces maintenance isolation flexibility. Source: `4-25_Deepcut_DBM.md` line 1031. |

## Examples

- **Example battery-limit statement** (suction side): "The package upstream battery limit is the acid gas pipe inlet from the amine regenerator overhead, water-saturated, at the design conditions defined in DEL-046-02 §1st-stage suction." Source basis: `4-25_Deepcut_DBM.md` lines 988, 1010, 1039.
- **Example battery-limit statement** (discharge side): "The package downstream battery limit is the acid gas injection pipeline tie-in at the package skid edge, assumed 3-inch NPS (final sizing TBD); the injection pipeline and disposal well are excluded from this scope." Source basis: `4-25_Deepcut_DBM.md` lines 84, 1061.
- **Example RAR row**: "Vendor documentation: Package Vendor (owner) / EPC Integrator (review and integration acceptance per DEL-046-06)." Source basis: `PACKAGE_REGISTER.csv` Responsibility; `DELIVERABLE_REGISTER.csv` DEL-046-05, DEL-046-06.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-046-01-01 | Compressor model: Ariel KBT/6 vs KBK/6 | `4-25_Deepcut_DBM.md` line 995 (KBT/6 with KBK/6 conflict noted) | Same line (KBK/6 reference) | Datasheet (Compressor model reference); Specification REQ-03 | PROPOSAL: Adopt KBT/6 as current basis per DBM table; mark KBK/6 as TBD pending vendor confirmation | TBD |
| CFL-046-01-02 | Compressor count/configuration: 2x100% + 1 spare vs 3x50% | `4-25_Deepcut_DBM.md` line 994 (2x100% + spare basis) | `4-25_Deepcut_DBM.md` line 878, 885 (3x50% alternative noted) | Datasheet (package count); Specification REQ-02 | PROPOSAL: Adopt 2x100% + 1 spare as current basis; document 3x50% as unresolved alternative | TBD |
| CFL-046-01-03 | 5th-stage design discharge pressure reference: 1,500 psig unresolved vs 1,200 psig normal | `4-25_Deepcut_DBM.md` line 1002 | Same line | Datasheet (Design Capacity Snapshot); Specification REQ-06; Package Datasheet (DEL-046-02) | PROPOSAL: Carry 1,200 psig as normal operating; carry 1,500 psig design-discharge reference as TBD | TBD |
| CFL-046-01-04 | Disposal well MAWP, min and max pressures | `4-25_Deepcut_DBM.md` lines 1051-1055 (TBC, provided by Tourmaline) | (no second source) | Specification REQ-13; Guidance §Disposal well data dependency | PROPOSAL: Leave TBD; flag as external responsibility | TBD |
| CFL-046-01-05 | 02-25 disposal well/reservoir modification trigger and extent | `4-25_Deepcut_DBM.md` line 93 | `4-25_Deepcut_DBM.md` line 173, 1059 | Specification REQ-10; Guidance §Shared 02-25 interface | PROPOSAL: Leave TBD; flag as shared-interface dependency | TBD |
| CFL-046-01-06 | Package-level exclusions stated in source | `PACKAGE_REGISTER.csv` Exclusions = "TBD; no package-specific exclusions stated in source materials" | (no second source) | Specification §Out of Scope | PROPOSAL: Carry no package-level exclusions beyond the EPC/Vendor split and the pipeline/well exclusion called out in DBM | TBD |
| CFL-046-01-07 | Detailed SOW-0047..0050 row content | `_CONTEXT.md` Source Reference (Workbook Packages row 48 — binary) | Not locally readable | Specification REQ-14 | PROPOSAL: Mark each `SOW-####` as `location TBD` until workbook slice is extracted | TBD |
