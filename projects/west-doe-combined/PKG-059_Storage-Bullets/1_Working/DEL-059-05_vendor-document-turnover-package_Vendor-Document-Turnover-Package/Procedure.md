# Procedure — DEL-059-05 Vendor Document Turnover Package (PKG-059)

> Operational. Steps describe how to **produce** the turnover package and how to **operate** the register during execution. Unsupported items are `TBD`. Inferred items are `ASSUMPTION`.

## Purpose

Provide a repeatable operational procedure for the Package Vendor (with EPC Integrator review) to:

1. establish and maintain the vendor document register for PKG-059 (Storage Bullets — eighteen pressure vessels total);
2. produce, submit, review, and accept each source-listed vendor document; and
3. assemble the final Vendor Data Book / Final Supplier Documentation as turnover evidence.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 466.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (basis for the register).
  - Source: `_REFERENCES.md`; `_DEPENDENCIES.md`.
- DEL-059-01 Scope of Work and DEL-059-02 Package Datasheet available for cross-reference.
  - Source: DELIVERABLE_REGISTER.csv rows 462, 463. (Coordination only; not declared as hard upstream in `_DEPENDENCIES.md`.)
- DEL-059-04 Vendor Engineered Equipment Package available as the source of equipment design content that vendor documents describe.
  - Source: DELIVERABLE_REGISTER.csv row 465.
- ARTIFACT_REGISTER.csv DEL-059-05 rows (93 rows) available as the seed list of vendor-document artifact rows.
  - Source: ARTIFACT_REGISTER.csv.
- Source slice `_Sources/26020-Package_Requirements.docx` package heading 14 (Vendor Engineering Deliverables table) — direct `.docx` extraction TBD; current register is the working surface.
- RFQ-level source `Bid Docs/Budgetary/26020-01-PT-RFQ-17-007-_Storage_Bullets.docx` (PACKAGE_REGISTER.csv row 83) — not directly opened in this run.

## Steps

### Step 1 — Initialize the Vendor Document Register

1. Create the register from ARTIFACT_REGISTER.csv DEL-059-05 rows; one row per source-listed vendor document.
2. Group rows under the 10 source categories from the Datasheet.
3. Add per-row fields: planned issue date (`TBD`), responsible reviewer (`TBD`), current submittal status (`PLANNED`), revision counter (`-`), per-bullet vs. fleet-level designation (`TBD` per CONF-004).
4. Verification: register row count matches ARTIFACT_REGISTER.csv DEL-059-05 row count (93).
- Source: ARTIFACT_REGISTER.csv DEL-059-05; Specification REQ-DEL-059-05-001, REQ-DEL-059-05-002.

### Step 2 — Submit and Activate the Document Control Procedure

1. Receive Vendor Document Control Procedure (ART-D4D95E703A) from the Package Vendor.
2. EPC Integrator reviews; on acceptance, activate as the governing procedure for all subsequent submittals.
3. Lock register row for the Document Control Procedure as ACCEPTED.
- Source: ARTIFACT_REGISTER.csv ART-D4D95E703A; Specification REQ-DEL-059-05-010 (sequencing `ASSUMPTION`).

### Step 3 — Submit Quality-Plan Tier

1. Submit Supplier Quality Plan (ART-28175E803C) and Inspection and Test Plan (ITP) (ART-80332A9924).
2. EPC Integrator reviews against package quality expectations (TBD-source criteria).
3. Update register rows with submittal status.
- Source: ARTIFACT_REGISTER.csv DEL-059-05.

### Step 4 — Submit Engineering and Process Tiers

1. Submit Core package engineering documents (Mechanical Design Basis through Mechanical Equipment IOM Manual).
2. Submit Static pressure equipment documents (Static Equipment Specifications; Pressure Vessel Data Sheets; Pressure Equipment Registration Package — per bullet per CONF-004 PROPOSAL).
3. Submit Relief / flare / vent design documents (Relief and Flare Design Basis; PSV / Pressure Relief Sizing Calculations; Relief Valve Data Sheets; Flare Load Summary / Flare System Study; Blowdown / Depressurization Study).
4. Submit Interface-discipline documents (Process piping; Drainage/containment; Electrical / lighting / EHT / grounding; I&C; Structural; Civil grading / spill containment).
5. Confirm P&IDs and Control Narrative document LPG vapour equalization (no pockets) and butane blanket-gas arrangements.
- Source: ARTIFACT_REGISTER.csv DEL-059-05; Specification REQ-DEL-059-05-008, REQ-DEL-059-05-011, REQ-DEL-059-05-012, REQ-DEL-059-05-013.

### Step 5 — Manage Inspection and Manufacturing Records

1. Receive and register Material Test Reports / Certificates, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book as fabrication progresses (per-bullet basis).
2. Reconcile each record back to the ITP requirements.
- Source: ARTIFACT_REGISTER.csv DEL-059-05.

### Step 6 — FAT and Release (per bullet)

1. For each of the eighteen bullets, submit Equipment FAT / Performance Test Procedure (ART-0D1E51ADA7) for EPC Integrator review prior to FAT.
2. Conduct FAT and submit Equipment FAT / Performance Test Report (ART-5098C5E6CC).
3. Issue Inspection Release Certificate before shipment for that bullet.
- Source: ARTIFACT_REGISTER.csv DEL-059-05; Specification REQ-DEL-059-05-006 (sequencing `ASSUMPTION`).

### Step 7 — Shipping and Field Records

1. Submit Logistics / Shipping Plan ahead of shipment of any bullet.
2. Receive Spare Parts Interchangeability Record (SPIR) and Mechanical Spares / Special Tools Requirements.
- Source: ARTIFACT_REGISTER.csv DEL-059-05.

### Step 8 — As-Built and IOM

1. Submit as-built piping and instrument drawing sets.
2. Submit Mechanical Equipment IOM Manual.
- Source: ARTIFACT_REGISTER.csv DEL-059-05.

### Step 9 — Final Vendor Data Book

1. Aggregate accepted submittals into Vendor Data Book / Final Supplier Documentation (ART-FD677DDDB8).
2. Confirm the Vendor Data Book / Mechanical Final Documentation set is consistent and complete across all eighteen bullets.
3. Hand over to EPC Integrator for acceptance under DEL-059-06.
- Source: ARTIFACT_REGISTER.csv DEL-059-05; Specification REQ-DEL-059-05-007; DELIVERABLE_REGISTER.csv row 467.

## Verification

| Check | Method | Source |
|---|---|---|
| Register completeness | Audit register row set vs. ARTIFACT_REGISTER.csv DEL-059-05 rows (93) | Specification V-001 |
| Category coverage | Inspection of register category groupings (10 categories) | Specification V-002 |
| Source citation | Sample-row inspection for source field | Specification V-003 |
| Submittal lifecycle | Review status field consistency | Specification V-004 (ASSUMPTION) |
| Pressure equipment registration | Confirm Pressure Equipment Registration Package row registered/submitted per bullet | Specification V-005 |
| FAT evidence | Confirm Procedure and Report both submitted per bullet | Specification V-006 (sequencing ASSUMPTION) |
| Vendor Data Book aggregation | Confirm aggregated turnover set across the fleet | Specification V-007 |
| Interface document coverage | Cross-check vs. PACKAGE_REGISTER.csv applicable interface list | Specification V-008 |
| Scope boundary | Cross-deliverable audit | Specification V-009 |
| Document control procedure activation | Confirm DCP active before later submittals processed | Specification V-010 (ASSUMPTION) |
| Relief / flare / vent design package | Confirm all five relief/flare/vent documents submitted | Specification V-011 |
| Vapour equalization / blanket gas | Inspect P&IDs and Control Narrative for the features | Specification V-012 |
| Civil grading / containment | Confirm civil documents submitted | Specification V-013 |
| Scope-by-others exclusion | Audit vendor scope claims vs. SOW-0184 by-others list | Specification V-014 |

## Records

- Vendor document register (live working surface for the deliverable).
- Submittal log with per-document revision, review, and acceptance history.
- Material Test Reports / Certificates set (per bullet).
- Inspection Release Certificate (per bullet).
- Manufacturing Record Book / Vendor Data Book (per bullet).
- Pressure Equipment Registration Package set (per bullet).
- FAT Procedure and FAT Report (per bullet).
- Relief / flare / vent design records (Relief and Flare Design Basis; PSV Sizing; Relief Valve Data Sheets; Flare Load Summary; Blowdown Study).
- Logistics / Shipping Plan; SPIR; Mechanical Spares / Special Tools Requirements.
- As-built drawing sets (piping, P&IDs) and IOM.
- Civil grading and containment records (Grading Plan; Drainage Report; Retention Pond / Containment Basin Design; Civil MTO).
- Vendor Data Book / Final Supplier Documentation (the turnover record set).
- Source: ARTIFACT_REGISTER.csv DEL-059-05 rows; DELIVERABLE_REGISTER.csv row 466 (AnticipatedArtifacts).
