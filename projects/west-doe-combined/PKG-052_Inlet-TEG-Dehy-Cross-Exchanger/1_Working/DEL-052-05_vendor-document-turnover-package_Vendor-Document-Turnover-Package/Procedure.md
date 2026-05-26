# Procedure — DEL-052-05 Vendor Document Turnover Package (PKG-052)

> Operational. Steps describe how to **produce** the turnover package and how to **operate** the register during execution. Unsupported items are `TBD`. Inferred items are `ASSUMPTION`.

## Purpose

Provide a repeatable operational procedure for the Package Vendor (with EPC Integrator review) to:

1. establish and maintain the vendor document register for PKG-052;
2. produce, submit, review, and accept each source-listed vendor document; and
3. assemble the final Vendor Data Book / Final Supplier Documentation as turnover evidence.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 340.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (basis for the register).
  - Source: `_REFERENCES.md`; `_DEPENDENCIES.md`.
- DEL-052-01 Scope of Work and DEL-052-02 Package Datasheet available for cross-reference.
  - Source: DELIVERABLE_REGISTER.csv rows 336, 337. (Coordination only; not declared as hard upstream in `_DEPENDENCIES.md`.)
- DEL-052-04 Vendor Engineered Equipment Package available as the source of equipment design content that vendor documents describe.
  - Source: DELIVERABLE_REGISTER.csv row 339.
- ARTIFACT_REGISTER.csv DEL-052-05 rows available as the seed list of vendor-document artifact rows.
  - Source: ARTIFACT_REGISTER.csv.
- Source slice `_Sources/26020-Package_Requirements.docx` package heading 7 (Vendor Engineering Deliverables table) — direct `.docx` extraction TBD; current register is the working surface.

## Steps

### Step 1 — Initialize the Vendor Document Register

1. Create the register from ARTIFACT_REGISTER.csv DEL-052-05 rows; one row per source-listed vendor document.
2. Group rows under the 9 source categories from the Datasheet.
3. Add per-row fields: planned issue date (`TBD`), responsible reviewer (`TBD`), current submittal status (`PLANNED`), revision counter (`-`).
4. Verification: register row count matches ARTIFACT_REGISTER.csv DEL-052-05 row count.
- Source: ARTIFACT_REGISTER.csv DEL-052-05; Specification REQ-DEL-052-05-001, REQ-DEL-052-05-002.

### Step 2 — Submit and Activate the Document Control Procedure

1. Receive Vendor Document Control Procedure (ART-B9AFEA01D9) from the Package Vendor.
2. EPC Integrator reviews; on acceptance, activate as the governing procedure for all subsequent submittals.
3. Lock register row for the Document Control Procedure as ACCEPTED.
- Source: ARTIFACT_REGISTER.csv DEL-052-05; Specification REQ-DEL-052-05-010 (sequencing `ASSUMPTION`).

### Step 3 — Submit Quality-Plan Tier

1. Submit Supplier Quality Plan (ART-7F6D2A9FFC) and Inspection and Test Plan (ITP) (ART-23F5BF5334).
2. EPC Integrator reviews against package quality expectations (TBD-source criteria).
3. Update register rows with submittal status.
- Source: ARTIFACT_REGISTER.csv DEL-052-05.

### Step 4 — Submit Engineering and Process Tiers

1. Submit Core package engineering documents (Mechanical Design Basis through Mechanical Equipment IOM Manual).
2. Submit Heat transfer equipment documents (Static Equipment Specifications; Heat Exchanger Data Sheets; Pressure Equipment Registration Package).
3. Submit Process package design documents (PFD, H&MB, P&IDs, etc.).
4. Submit Interface-discipline documents (Process piping; Drainage/containment; Electrical; I&C; Structural).
- Source: ARTIFACT_REGISTER.csv DEL-052-05; Specification REQ-DEL-052-05-008.

### Step 5 — Manage Inspection and Manufacturing Records

1. Receive and register Material Test Reports / Certificates, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book as fabrication progresses.
2. Reconcile each record back to the ITP requirements.
- Source: ARTIFACT_REGISTER.csv DEL-052-05.

### Step 6 — FAT and Release

1. Submit Equipment FAT / Performance Test Procedure for EPC Integrator review prior to FAT.
2. Conduct FAT and submit Equipment FAT / Performance Test Report.
3. Issue Inspection Release Certificate before shipment.
- Source: ARTIFACT_REGISTER.csv DEL-052-05; Specification REQ-DEL-052-05-006 (sequencing `ASSUMPTION`).

### Step 7 — Shipping and Field Records

1. Submit Logistics / Shipping Plan ahead of shipment.
2. Receive Spare Parts Interchangeability Record (SPIR) and Mechanical Spares / Special Tools Requirements.
- Source: ARTIFACT_REGISTER.csv DEL-052-05.

### Step 8 — As-Built and IOM

1. Submit as-built piping and instrument drawing sets and as-built PFD/P&ID package.
2. Submit Mechanical Equipment IOM Manual.
- Source: ARTIFACT_REGISTER.csv DEL-052-05.

### Step 9 — Final Vendor Data Book

1. Aggregate accepted submittals into Vendor Data Book / Final Supplier Documentation.
2. Confirm the Vendor Data Book / Mechanical Final Documentation set is consistent and complete.
3. Hand over to EPC Integrator for acceptance under DEL-052-06.
- Source: ARTIFACT_REGISTER.csv DEL-052-05; Specification REQ-DEL-052-05-007; DELIVERABLE_REGISTER.csv row 341.

## Verification

| Check | Method | Source |
|---|---|---|
| Register completeness | Audit register row set vs. ARTIFACT_REGISTER.csv DEL-052-05 rows | Specification V-001 |
| Category coverage | Inspection of register category groupings | Specification V-002 |
| Source citation | Sample-row inspection for source field | Specification V-003 |
| Submittal lifecycle | Review status field consistency | Specification V-004 (ASSUMPTION) |
| Pressure equipment registration | Confirm Pressure Equipment Registration Package row registered/submitted | Specification V-005 |
| FAT evidence | Confirm Procedure and Report both submitted | Specification V-006 (sequencing ASSUMPTION) |
| Vendor Data Book aggregation | Confirm aggregated turnover set | Specification V-007 |
| Interface document coverage | Cross-check vs. PACKAGE_REGISTER.csv applicable interface list | Specification V-008 |
| Scope boundary | Cross-deliverable audit | Specification V-009 |
| Document control procedure activation | Confirm DCP active before later submittals processed | Specification V-010 (ASSUMPTION) |

## Records

- Vendor document register (live working surface for the deliverable).
- Submittal log with per-document revision, review, and acceptance history.
- Material Test Reports / Certificates set.
- Inspection Release Certificate.
- Manufacturing Record Book / Vendor Data Book.
- FAT Procedure and FAT Report.
- Logistics / Shipping Plan; SPIR; Mechanical Spares / Special Tools Requirements.
- As-built drawing sets (piping, P&IDs) and IOM.
- Vendor Data Book / Final Supplier Documentation (the turnover record set).
- Source: ARTIFACT_REGISTER.csv DEL-052-05 rows; DELIVERABLE_REGISTER.csv row 340 (AnticipatedArtifacts).
