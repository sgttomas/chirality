# Specification: DEL-016-03 — Construction Work Package (Transformer TXP-8200-1)

## Scope

This Construction Work Package (CWP) defines the EPC Integrator's construction-scope requirements for the physical receipt, installation, termination, tie-in, inspection, testing, and turnover of the PKG-016 step-down distribution transformer TXP-8200-1 (3 MVA, 13.8 kV primary / 600 V secondary, 347 V line-to-neutral implied — see Datasheet ASSUMPTION).

**In scope:**
- Receipt, offloading, and setting of the vendor-supplied transformer package onto its designed foundation.
- Foundation installation per the final geotechnical report and equipment-specific anchorage.
- Primary 13.8 kV feeder termination from the 04-25 Main Switchgear cross-facility feed.
- Secondary 600 V termination into the 03-25 600 V MCC lineup (MCC-8200 service).
- Grounding and bonding tie-in to the facility ground grid.
- Cable raceway, cable installation, terminations, and segregation from control/instrument circuits.
- Field inspection, pre-energization checks, and turnover documentation.

**Out of scope:**
- Engineering, design, fabrication, and factory acceptance testing of the transformer itself (Package Vendor scope — see `DEL-016-04_vendor-engineered-equipment-package`).
- Vendor documentation register and submittals (see `DEL-016-05_vendor-document-turnover-package`).
- EPC vendor package acceptance and integration review (see `DEL-016-06`).
- 04-25 13.8 kV switchgear scope and any 04-25-side construction.
- Third-party LACT scope; only facility-side power/tie-in interfaces are within EPC facility integration.

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| R-CWP-01 | The transformer shall be installed at the location consistent with the 03-25 facility electrical building / MCC arrangement defined in detailed design. | DBM SEC-12 "Electrical Buildings…" |
| R-CWP-02 | The foundation shall be designed against the final geotechnical report and equipment loads (weight, anchoring, vibration, settlement, frost protection, snow/wind/seismic). Pre-pour, anchor-bolt placement, and grout activities shall be inspected and documented. | DBM SEC-11 "Foundations and Structural Supports" |
| R-CWP-03 | Primary feeder termination shall connect TXP-8200-1 to the 04-25 13.8 kV Main Switchgear cross-facility feed. Conductor type, size, raceway, and termination accessories per detailed electrical design and project electrical specifications. | DBM SEC-12 "Incoming Power and Transformers" |
| R-CWP-04 | Secondary feeder termination shall connect TXP-8200-1 to the 600 V MCC lineup serving 03-25 LV loads. | DBM SEC-12 |
| R-CWP-05 | Grounding shall conform to project electrical specifications and detailed design. Secondary system grounding shall be coordinated with the 600 V HRG basis (5 A continuous resistor at the 600 V service level). | DBM SEC-12 "System Voltages"; "Electrical Buildings, Raceways…" |
| R-CWP-06 | Power circuits at 13.8 kV and 600 V shall be physically separated from control and instrument circuits by distance, shielding, or routing as required by the project electrical specifications. | DBM SEC-12 |
| R-CWP-07 | Construction activities shall be coordinated with hazardous-area classification (Class I Zone 2, IIA/IIB general basis); final classification drawings shall govern at the installation location. | DBM SEC-11 "Area Classification" |
| R-CWP-08 | All installation activities shall be performed under construction management, with safety, quality, and document control per the project Construction Management Plan. | DBM SEC-01 "Construction Scope Summary" |
| R-CWP-09 | Field tie-ins (primary cable, secondary cable, ground grid, building/HVAC services where applicable, heat tracing/winterization for outdoor terminations) shall be identified, scheduled, and tracked in the construction tie-in register. | DBM SEC-01; SEC-11 "Miscellaneous and Tie-in Facilities" |
| R-CWP-10 | Pre-energization checks shall include continuity, insulation resistance, transformer turns-ratio (TTR), polarity, oil quality (where applicable), protective device coordination verification, and grounding integrity. (ASSUMPTION — typical industry practice; exact test list per project Electrical Construction Specification, location TBD.) | ASSUMPTION |
| R-CWP-11 | Hand-over of the transformer to commissioning shall use a construction turnover package containing the as-built drawings, test records, punch list, and tie-in completion evidence. | Anticipated Artifacts (DEL-016-03 row); Project turnover convention — location TBD |
| R-CWP-12 | The CWP shall reference and remain consistent with the PKG-016 Scope of Work (`DEL-016-01`) and Package Datasheet (`DEL-016-02`). | DELIVERABLE_REGISTER.csv rows for PKG-016 |

## Standards

| Standard | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs facility electrical installation | Cited in DBM SEC-15; clause-level requirements `location TBD` |
| Project Electrical Specifications | Governs cable, raceway, grounding, terminations | Referenced by DBM SEC-12; document not locally accessible — `location TBD` |
| Project Construction Specifications | Governs construction execution, inspection, QA/QC | Referenced; document not locally accessible — `location TBD` |
| API RP 505 | Used for area classification basis | DBM SEC-11 |
| CSA Z662 | Pipeline scope (not directly applicable to this CWP except adjacent tie-in coordination) | DBM SEC-09 |
| IEEE C57 series (transformer) | ASSUMPTION — typical for power transformer installation/test (e.g., IEEE C57.12.91, C57.93). Not cited in DBM. | ASSUMPTION |

## Verification

| Requirement | Verification Method |
|---|---|
| R-CWP-02 (foundation) | Foundation inspection record, geotechnical concurrence, anchor-bolt and grout reports |
| R-CWP-03, R-CWP-04 (terminations) | Cable test records (continuity, hi-pot/megger), termination inspection checklist |
| R-CWP-05 (grounding) | Ground-grid resistance test record; bonding continuity check |
| R-CWP-06 (segregation) | Field walkdown checklist verifying physical separation per detailed design |
| R-CWP-07 (area classification) | Field walkdown against issued classification drawings |
| R-CWP-09 (tie-ins) | Tie-in register sign-offs |
| R-CWP-10 (pre-energization) | Pre-energization test record set (TTR, IR, polarity, oil quality where applicable) |
| R-CWP-11 (turnover) | Signed turnover certificate with attached test/inspection records and punch list |

## Documentation

Required artifacts at completion of this deliverable (anticipated artifacts from `_CONTEXT.md`):

- Construction Work Package document (this deliverable, formalized)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Foundation inspection records
- Cable test and termination records
- Grounding test records
- Pre-energization test record set
- As-built redlines
- Construction punch list and turnover certificate
