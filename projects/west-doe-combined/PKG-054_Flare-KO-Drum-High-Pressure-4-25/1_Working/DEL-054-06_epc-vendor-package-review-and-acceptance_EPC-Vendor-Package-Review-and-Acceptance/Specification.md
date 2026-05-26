# Specification — DEL-054-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for the HP Flare KO Drum (HP) package (`26020-01-PT-17-002`, `V-4100-1`, transfer pump `P-4100-1`). It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-054-04` Vendor Engineered Equipment Package and `DEL-054-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-054-01`), Package Datasheet (`DEL-054-02`), and Construction Work Package (`DEL-054-03`).

Sources: `26020-Package_Requirements.docx` Heading 9 (Basic Scope; Major Included Equipment); `DELIVERABLE_REGISTER.csv` row `DEL-054-06`.

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-054-04` / `DEL-054-05` outputs.
- Defining cryogenic flare KO drum (`26020-01-PT-17-001`) or LP flare KO drum (`26020-01-PT-17-003`) acceptance; those are separate packages.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-054-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0075`, `SOW-0076`, `SOW-0077`, `SOW-0078`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| `R-054-06-02` | The vendor document review log MUST enumerate every "Vendor Engineering Deliverable" listed for `26020-01-PT-17-002` and record disposition (accepted / rejected / open). | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" |
| `R-054-06-03` | The package acceptance checklist MUST verify scope inclusions: supply of one HP flare knock-out drum and one HP flare KO drum transfer pump; HP flare KO drum `V-4100-1`; transfer pump `P-4100-1`; liquid handling to condensate slop tank; truck-out provision; package connections. | `26020-Package_Requirements.docx` Heading 9, "Basic Scope" / "Major Included Equipment" |
| `R-054-06-04` | The acceptance evidence MUST confirm that the HP flare header tie-in to the cryogenic flare header downstream of the drum (before the common HP/Cryo flare stack) is reflected in the as-built/turnover P&ID set (`PRO-008`) and piping iso/tie-in list (`PIP-004`, `PIP-008`, `PIP-028`). | `26020-Package_Requirements.docx` Heading 9, "Scope Notes / Open Items"; "Vendor Engineering Deliverables" — Process piping interfaces |
| `R-054-06-05` | The acceptance evidence MUST verify electrical heat tracing and insulation of outdoor HP flare headers via the EHT design package (`ELE-018`), piping heat tracing schedule (`PIP-020`), and piping heat tracing interface package (`PIP-021`). | `26020-Package_Requirements.docx` Heading 9, "Scope Notes / Open Items"; "Vendor Engineering Deliverables" — Electrical, lighting, EHT, grounding |
| `R-054-06-06` | The acceptance evidence MUST cover each physical interface marked `Yes` in the Heading 9 Physical Interface Summary: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Area / Exterior Lighting; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | `26020-Package_Requirements.docx` Heading 9, "Physical Interface Summary" |
| `R-054-06-07` | The acceptance evidence MUST include pressure-vessel registration and pressure-test evidence: Pressure Equipment Registration Package (`REG-022`), Pressure Vessel Data Sheet (`MEC-009`), and Hydrotest / Pressure Test Packages (`PIP-024`). | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" — Static pressure equipment / Process piping interfaces |
| `R-054-06-08` | The acceptance evidence MUST include rotating-equipment FAT and performance evidence for `P-4100-1`: pump data sheet (`MEC-007`), NPSH calcs (`PRO-013`), mechanical seal / lube oil specification (`MEC-019`), motor starting study (`ELE-011`), and Equipment FAT / Performance Test Report (`MEC-022`). | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" — Rotating equipment / pumps |
| `R-054-06-09` | Quality records MUST be assembled: Supplier Quality Plan (`QLT-006`), ITP execution evidence (`QLT-003`), Material Test Reports / Certificates (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" — Core vendor documents |
| `R-054-06-10` | Turnover MUST include the SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), and Mechanical Equipment IOM Manual (`MEC-025`). | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" |
| `R-054-06-11` | Numeric design/operating values used in acceptance (design pressure/temperature, sizing, flare load summary) MUST be traceable to the Package Vendor's submitted `MEC-009`, `PRO-014`, `PRO-017`, `PRO-018`. Specific numeric values are TBD until those vendor submittals are accepted. | `26020-Package_Requirements.docx` Heading 9, "Vendor Engineering Deliverables" — Relief / flare / vent design; Static pressure equipment |
| `R-054-06-12` | Open items called out in the source ("Scope Notes / Open Items") MUST be closed or carried with explicit disposition in the acceptance record. | `26020-Package_Requirements.docx` Heading 9, "Scope Notes / Open Items" |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Provincial pressure equipment registration regime applicable to the project (typically ABSA in Alberta) | Required for `REG-022` Pressure Equipment Registration Package referenced for the HP flare KO drum. | location TBD — not stated in `26020-Package_Requirements.docx` Heading 9; ASSUMPTION based on the presence of `REG-022` in the source's deliverable enumeration. |
| Pressure vessel design code (ASME BPVC Section VIII or CSA B51 as applicable) | Governs `MEC-009` and acceptance of the HP flare KO drum vessel. | location TBD — not stated in source Heading 9; ASSUMPTION typical to scope. |
| API / industry flare system standards (e.g., API STD 521, API STD 537) | Likely governing for flare load summary (`PRO-017`) and blowdown study (`PRO-018`). | location TBD — not stated in source Heading 9; ASSUMPTION. |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-054-06-01` | Traceability matrix mapping each SOW item to acceptance-checklist rows and to evidence artifacts. |
| `R-054-06-02` | Document-by-document review log inspection; every Heading 9 vendor deliverable has a tracked disposition. |
| `R-054-06-03` | Walk-down and as-built/IFC drawing review against the Heading 9 Basic Scope and Major Included Equipment list. |
| `R-054-06-04` | P&ID and tie-in list inspection (`PRO-008`, `PIP-004`); construction work package (`DEL-054-03`) cross-check. |
| `R-054-06-05` | EHT package review (`ELE-018`, `PIP-020`, `PIP-021`); commissioning/heat-trace energization records. |
| `R-054-06-06` | Interface-by-interface checklist against the Heading 9 Physical Interface Summary. |
| `R-054-06-07` | Hydrotest packages (`PIP-024`) signed off; `REG-022` accepted by registration authority; `MEC-009` reconciled with as-built. |
| `R-054-06-08` | FAT witness records (`MEC-022`); NPSH calc review (`PRO-013`); motor starting study (`ELE-011`) accepted. |
| `R-054-06-09` | Quality records audit; Inspection Release Certificate (`QLT-020`) issued; MRB (`QLT-021`) compiled and accepted. |
| `R-054-06-10` | Receipt inspection records; SPIR provided and accepted; IOM in turnover bundle. |
| `R-054-06-11` | Reconciliation table between EPC Package Datasheet (`DEL-054-02`) values and vendor-submitted values; TBD entries flagged. |
| `R-054-06-12` | Open-items log carried into commissioning; explicit closure or carryover noted. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (SOW-, interface-, and artifact-indexed).
- Test / inspection evidence bundle (FAT, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log.

Standards-related and numeric design values that depend on vendor submittals carry `TBD` placeholders until the Package Vendor deliverables are accepted.
