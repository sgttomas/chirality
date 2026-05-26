# Procedure — DEL-077-05 Vendor Document Turnover Package (PKG-077)

## Purpose

Operational steps to produce, submit, and turn over the vendor documentation set for the PKG-077 Methanol Injection package. This procedure addresses both production of the deliverable artifact (the document set) and the controlled submittal cycle that delivers it to the EPC Integrator for acceptance via `DEL-077-06`.

## Prerequisites

- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (PREPARATION did not declare upstream edges for this deliverable). Practical upstream context: the EPC Scope of Work (`DEL-077-01`) and Package Datasheet (`DEL-077-02`) define what the Package Vendor is engineering; the engineered package (`DEL-077-04`) produces the physical basis the turnover records document.
- Accessible source set:
  - `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables list — generic template; no methanol-injection-specific section is present in the accessible source set, per `ART-CF38039426`).
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (methanol injection scope and equipment basis).
  - Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv` row 72; `DELIVERABLE_REGISTER.csv` `DEL-077-05` row; `SCOPE_LEDGER.csv` `SOW-0143`; `ARTIFACT_REGISTER.csv` `ART-CF38039426`).
- Vendor Document Control Procedure (`DOC-008`) and Vendor Document Index (`PRQ-009`) baselined before any document is submitted.
- EPC Integrator named reviewer assigned for `DEL-077-06`.
- TBD/TBC items from DBM (capacities, rates, tank SG, acid-gas-compressor injection details, required injection points) registered with named closure owners.

## Steps

### Step 1 — Baseline the Vendor Document Index
1. Instantiate `PRQ-009` for PKG-077 using `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" as the template.
2. Mark each line APPLICABLE / N/A with a short rationale (see Guidance principle 2 and Specification R-4 through R-13).
3. Add open-item rows for the DBM TBD/TBC parameters identified in Specification R-20 (HRR-077-05-004).
4. Reflect the per-discipline applicability call in the Index revision baseline.

### Step 2 — Baseline the Document Control Procedure
1. Issue `DOC-008` describing document numbering, revisioning convention, transmittal mechanics, submittal milestones, and review-cycle handling.
2. Reflect the named milestones (e.g., preliminary, certified-for-construction, as-built) consistent with the package PO.
3. State whether vendor turnover will be physically co-issued with `PKG-076` Cryogenic Unit turnover (HRR-077-05-001) at the EPC Integrator's election.

### Step 3 — Produce Core vendor documents
1. Produce and submit `QLT-006` Supplier Quality Plan, `QLT-003` ITP, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` SPIR, and supporting quality documents as design and manufacturing milestones permit.
2. Track each submittal on the Vendor Document Index (Step 1).

### Step 4 — Produce discipline engineering documents
1. Mechanical (primary): produce `MEC-001`, `MEC-002`, `MEC-003` (data sheets for `TK-6395-1` and `P-6396-1`), `MEC-006`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-024`, `MEC-025`. For the tank, produce `MEC-005` and the secondary-containment basis (`CIV-014`). Confirm `MEC-009` / `REG-022` disposition per Specification R-5.
2. Process package design: produce `PRO-007` (operating philosophy reflecting transient hydrate management), `PRO-008` (P&IDs covering tank, pump, distribution headers, and all DBM-line-1328 injection points), `PRO-010`, `PRO-011`, `PRO-012`, `PRO-020`, `PRO-025`, `PRO-026`, `PRO-027`.
3. Relief / overpressure: produce `PRO-014`, `PRO-015`, `PRO-016` for the pump-discharge protection (R-7). Confirm `PRO-017` / `PRO-018` disposition.
4. Process piping: produce `PIP-003`, `PIP-004` (tie-in list against DBM line 1328 injection points), `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`. For cold climate, include `PIP-020` and `PIP-021`.
5. Drainage / containment: produce `CIV-014` (consistent with the DBM-line-1329 double-walled tank basis). Confirm `PRO-023` disposition.
6. Electrical / EHT: produce `ELE-002`, `ELE-003` (where applicable), `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020` (pump motor), `ELE-027`, `ELE-028`, `ELE-029`. Include `ELE-018` EHT design package and `ELE-012` / `ELE-019` grounding/bonding. Confirm `ELE-017` disposition.
7. I&C: produce `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, `INS-010`, `INS-011`, `INS-016` (control valves for single-point selection per DBM line 1328), `INS-018`, `INS-025`, `CTL-003` (single-point selection narrative), `CTL-005`, `CTL-006`, `CTL-026`. Confirm `INS-017` disposition.
8. Fire and gas: produce `TSF-002`, `TSF-003`, `TSF-004`, `TSF-028`. Confirm `TSF-009` / `TSF-011` / `TSF-013` disposition.
9. Structural: produce `STR-001`, `STR-002`, `STR-004`, `STR-005`, `STR-006`, `STR-011` (tank-access platform for sampling), `STR-013`, `STR-014`, `STR-020`. Confirm `STR-012` disposition.
10. Each document cites its governing standards (see Specification R-18). Where standards are not yet known (per HRR-077-05-003), mark `location TBD`.

### Step 5 — Execute and document FAT
1. Execute the pump and tank FAT per `MEC-021`.
2. Issue `MEC-022` Equipment FAT / Performance Test Report.
3. Issue `ELE-029` / `ELE-030` Electrical Test Records / Energization Package for the pump motor and EHT circuits.
4. Issue `QLT-020` Inspection Release Certificate prior to shipment.
5. Issue `QLT-013` Material Test Reports / Certificates as they are accumulated through fabrication (methanol-service material traceability per HRR-077-05-003 ASSUMPTION).
6. Compile `QLT-021` Manufacturing Record Book / Vendor Data Book.

### Step 6 — Ship and turn over
1. Execute the Logistics / Shipping Plan (`PRQ-013`).
2. Issue final turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation.
3. Issue as-built piping (`PIP-028`), electrical, I&C, and process (`PRO-028`) drawings as final revisions reflecting closed TBD/TBC items (HRR-077-05-004 closure).
4. Submit the final Vendor Document Index (`PRQ-009`) reflecting all closed transmittals.
5. Hand off to EPC Integrator for `DEL-077-06` review (coordinate co-issue with PKG-076 if elected per Step 2).

### Step 7 — Close-out
1. Address EPC Integrator review comments raised in `DEL-077-06`.
2. Re-issue revisions and update the Index.
3. Confirm all lines on the Index are either CLOSED or N/A with rationale.
4. Confirm all DBM-flagged TBD/TBC items have closed dispositions captured on as-built documents.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Index completeness | Compare `PRQ-009` against `_Sources/26020-Package_Requirements.docx` Core vendor documents list and applicable discipline lines. | Reviewed `PRQ-009` revision |
| Document Control Procedure in place | Confirm `DOC-008` issued before any document submittal. | `DOC-008` rev baseline |
| Quality records present | Confirm `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021` issued. | Document register entries |
| Logistics / spares present | Confirm `PRQ-013`, `PRQ-015` issued. | Document register entries |
| Pump-discharge relief | `PRO-015` calculation reviewed; `PRO-016` data sheet reviewed; PSV install verified on `PRO-028` as-built P&ID. | PSV review record |
| Tie-in scope | `PIP-004` tie-in list cross-referenced against DBM line 1328 injection points (BAHX, J-T inlet, inlet separators, acid-gas-compressor). | Reviewed `PIP-004` |
| Containment | `CIV-014` and tank specification confirm double-walled basis per DBM line 1329. | Reviewed `CIV-014`, `MEC-005` |
| Cold-climate freeze protection | `ELE-018`, `PIP-020`, `PIP-021` cover all methanol-service piping. | Reviewed EHT / insulation deliverables |
| FAT/SAT records present | Confirm `MEC-021`/`MEC-022` and `ELE-029`/`ELE-030` issued. | Signed FAT/SAT records |
| Single-point selection control | `CTL-003` narrative and `CTL-005` C&E matrix reflect DBM line 1328 single-point injection constraint. | Reviewed `CTL-003`, `CTL-005` |
| Standards traceability | Each engineered document cites governing standards (or marks `location TBD` per HRR-077-05-003). | Document QA review |
| TBD/TBC closure | DBM-flagged open items (HRR-077-05-004) have closed dispositions on as-built documents. | Closure log |
| Acceptance | EPC Integrator acceptance via `DEL-077-06`. | `DEL-077-06` acceptance evidence |
| Status hygiene | All Index lines CLOSED or marked N/A with rationale. | Final `PRQ-009` rev |

## Records

- Vendor Document Index `PRQ-009` — final revision
- Vendor Document Control Procedure `DOC-008` — final revision
- Supplier Quality Plan `QLT-006`
- Inspection and Test Plan `QLT-003`
- Material Test Reports / Certificates `QLT-013`
- Inspection Release Certificate `QLT-020`
- Manufacturing Record Book / Vendor Data Book `QLT-021`
- Logistics / Shipping Plan `PRQ-013`
- SPIR `PRQ-015`
- Vendor Data Book / Final Supplier Documentation `PRQ-016`
- Mechanical Final Documentation `MEC-023`
- Mechanical FAT / Performance Test Procedure / Report `MEC-021` / `MEC-022`
- Electrical FAT/SAT Procedure / Test Records `ELE-029` / `ELE-030`
- Process As-Built P&ID Package `PRO-028`
- Piping As-Built Drawings `PIP-028`
- Pump-discharge PSV sizing and data sheet `PRO-015` / `PRO-016`
- Secondary containment drawings `CIV-014`
- EHT design package `ELE-018`
- Single-point injection control narrative and C&E matrix `CTL-003` / `CTL-005`
- Transmittal log and review-cycle disposition records
- TBD/TBC closure log (HRR-077-05-004 items)
