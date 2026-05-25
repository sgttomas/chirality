# Specification — DEL-026-03 Construction Work Package

Normative requirements that the Construction Work Package (CWP) for PKG-026 Transformer TXP-8300-2 must satisfy.

## Scope

### In scope

- The CWP shall describe how the PKG-026 step-down distribution transformer TXP-8300-2 and its package-scope ancillaries will be physically installed, built, inspected, turned over, and tied into the larger 04-25 facility systems (DELIVERABLE_REGISTER row DEL-026-03).
- The CWP shall cover the EPC Integrator-owned facility-level integration scope for PKG-026, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration (PACKAGE_REGISTER row PKG-026).
- The CWP shall cover, at minimum, the package-declared interface types: Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports (PACKAGE_REGISTER row PKG-026).

### Out of scope

- Package engineering, package design, vendor documentation, and the physical equipment package itself — these are owned by the Package Vendor under DEL-026-04 and DEL-026-05 (PACKAGE_REGISTER row PKG-026; DELIVERABLE_REGISTER rows DEL-026-04, DEL-026-05).
- Production of the package Scope of Work (DEL-026-01) and Package Datasheet (DEL-026-02) — referenced as upstream inputs only.
- Vendor package review and acceptance evidence (DEL-026-06) — covered by a separate deliverable.

## Requirements

| Req ID | Requirement | Basis / Source |
|---|---|---|
| REQ-CWP-026-01 | The CWP shall document the installation and tie-in workface plan for transformer TXP-8300-2 including setting on foundation, mechanical hookup, electrical terminations, and home-run cable installation. | DELIVERABLE_REGISTER row DEL-026-03; DBM-Deepcut §Construction Responsibility |
| REQ-CWP-026-02 | The CWP shall identify field-construction activities assigned to Tourmaline Oil Corporation per the DBM construction responsibility basis (e.g., setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, electrical terminations, field installation of home-run cables, miscellaneous structural supports). | DBM-Deepcut §Construction Responsibility (lines 101–125) |
| REQ-CWP-026-03 | The CWP shall define a construction interface and turnover checklist covering each PKG-026 interface type: Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. | PACKAGE_REGISTER row PKG-026 |
| REQ-CWP-026-04 | CEC spacing requirements shall apply to TXP-8300-2 as a large oil-filled transformer. Transformer secondary containment requirements shall be reviewed during installation planning. | DBM-Deepcut §Transformers |
| REQ-CWP-026-05 | The CWP shall specify that the transformer shall be installed on a structural-steel transformer base unless detailed engineering directs otherwise. (ASSUMPTION pending vendor/detailed-design confirmation.) | DBM-Deepcut §Transformers |
| REQ-CWP-026-06 | The CWP shall specify grounding installation provisions consistent with the DBM grounding basis for medium-voltage step-down transformers: the 6.9 kV transformer secondary shall be grounded via a 100 A, 10 s neutral grounding resistor configured as a tripping system. | DBM-Deepcut §Power System / grounding paragraph |
| REQ-CWP-026-07 | The CWP shall specify grounding installation provisions for the 600 V class (5 A continuous high-resistance grounding resistor) when applied to a 0.4 kV-class winding; applicability to the specific 0.4 kV winding of TXP-8300-2 is TBD. | DBM-Deepcut §Power System; applicability TBD |
| REQ-CWP-026-08 | The CWP shall define the tie-in interface handling for interconnecting piping to ISBL/OSBL tie-in points as an external-interface item, with per-tie-in responsibility confirmed during execution. | DBM-Deepcut §Construction Responsibility (line 117 region) |
| REQ-CWP-026-09 | The CWP shall be aligned with the EPC Scope of Work (DEL-026-01) and Package Datasheet (DEL-026-02) outputs once those deliverables are accepted; conflicting field decisions shall be escalated to EPC Integrator. | DELIVERABLE_REGISTER rows DEL-026-01, DEL-026-02, DEL-026-06 |
| REQ-CWP-026-10 | The CWP shall produce a construction turnover record sufficient to support DEL-026-06 (EPC Vendor Package Review and Acceptance). | DELIVERABLE_REGISTER row DEL-026-06 |

## Standards

| Standard / Code | Applicable scope | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing; grounding conductor sizing | DBM-Deepcut §Transformers; §Power System (grounding paragraph) |
| Tourmaline construction responsibility basis | Field construction activity boundaries | DBM-Deepcut §Construction Responsibility (lines 101–125) |
| Vendor installation manual for TXP-8300-2 | Equipment-specific installation, torque, alignment, oil-fill, energization | TBD — not in accessible sources; obtain via DEL-026-04 vendor turnover (DEL-026-05) |
| Applicable provincial / regulatory inspection standards | Construction inspection, hold points | location TBD |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-CWP-026-01 | Walk-down of foundation, anchorage, terminations, and home-run cable runs against the workface plan |
| REQ-CWP-026-02 | Cross-check field activity assignments against the DBM construction responsibility table |
| REQ-CWP-026-03 | Interface and turnover checklist completion sign-off for each declared interface type |
| REQ-CWP-026-04 | CEC spacing check on as-built equipment layout; secondary-containment review record |
| REQ-CWP-026-05 | Foundation/base installation inspection report |
| REQ-CWP-026-06 | Grounding-system continuity test record; NGR commissioning confirmation |
| REQ-CWP-026-07 | Grounding-system test for 0.4 kV-class winding once applicability is confirmed |
| REQ-CWP-026-08 | Per-tie-in responsibility record signed by EPC Integrator and tie-in counterparty |
| REQ-CWP-026-09 | Document-set alignment review against DEL-026-01 and DEL-026-02 accepted snapshots |
| REQ-CWP-026-10 | Turnover dossier completeness check against DEL-026-06 acceptance checklist |

## Documentation (artifacts required)

- Construction work package document
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Field inspection and test records (grounding, spacing, base, terminations)
- Tie-in responsibility log
- Punch-list and turnover transmittal to DEL-026-06

## Notes

- All quantitative transformer parameters (impedance, BIL, taps, cooling) needed to size foundations, cabling, and clearances are TBD pending vendor datasheet or detailed-design slices.
