# Specification: DEL-035-05 — Vendor Document Turnover Package

## Scope

### In scope

- Production by the Package Vendor of a single Vendor Document Turnover Package for `PKG-035` 13.8kV Switchgear Electrical Building (810-1) consisting of:
  - a Vendor Document Register that enumerates every vendor document required for this package, with submittal status and turnover disposition;
  - vendor document submittals (engineering, quality, logistics, and final-documentation deliverables) covering at minimum the Core vendor document set and the discipline-specific Electrical document set;
  - source-required vendor documentation rows carried as evidence/artifacts within the Vendor Document Register, not as separate decomposition deliverables;
  - turnover records (Manufacturing Record Book / Vendor Data Book and Final Supplier Documentation) suitable for EPC Integrator review and project handoff.
  - Source: `_CONTEXT.md` (Scope; Anticipated Artifacts); `_Sources/26020-Package_Requirements.docx` Table 4 (Core vendor documents); `DELIVERABLE_REGISTER.csv` row `DEL-035-05`.
- EPC Integrator interface/integration review of vendor document submittals (not vendor authoring). Source: `_CONTEXT.md` (Responsible Party).

### Out of scope

- Authoring of the EPC Scope of Work (`DEL-035-01`), Package Datasheet (`DEL-035-02`), Construction Work Package (`DEL-035-03`), Vendor Engineered Equipment Package (`DEL-035-04`), or EPC Vendor Package Review and Acceptance (`DEL-035-06`). Source: `DELIVERABLE_REGISTER.csv` (separate deliverable rows).
- Creation of individual vendor document rows as standalone decomposition deliverables; they remain artifacts under this turnover package. Source: `_CONTEXT.md` (Notes).
- Process unit documentation that is not associated with the 13.8kV Switchgear Electrical Building. Source: workbook row 37 (Discipline = Electrical).

## Requirements

### R-035-05-001 — Vendor Document Index (PRQ-009) (MUST)

The Package Vendor MUST produce and maintain a Vendor Document Index that enumerates every vendor document in the turnover package, with status, revision, and submittal/turnover disposition.

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, row 2 (PRQ-009 "Vendor Document Index").

### R-035-05-002 — Vendor Document Control Procedure (DOC-008) (MUST)

The Package Vendor MUST issue a Vendor Document Control Procedure governing numbering, revision, transmittal, review-comment incorporation, and turnover.

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, row 3 (DOC-008 "Vendor Document Control Procedure").

### R-035-05-003 — Core quality and inspection documentation (MUST)

The Package Vendor MUST submit the following core quality and inspection documents for `PKG-035`:

| ID | Document |
|---|---|
| QLT-006 | Supplier Quality Plan |
| QLT-003 | Inspection and Test Plan (ITP) |
| QLT-013 | Material Test Reports / Certificates |
| QLT-020 | Inspection Release Certificate |

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, rows 4–7.

### R-035-05-004 — Manufacturing / Vendor Data Book (QLT-021) and Final Supplier Documentation (PRQ-016) (MUST)

The Package Vendor MUST compile a Manufacturing Record Book / Vendor Data Book (QLT-021) and a Vendor Data Book / Final Supplier Documentation set (PRQ-016) as the principal turnover artifacts.

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, rows 8 and 11.

### R-035-05-005 — Logistics and spare-parts records (MUST)

The Package Vendor MUST submit a Logistics / Shipping Plan (PRQ-013) and a Spare Parts Interchangeability Record (SPIR) (PRQ-015).

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, rows 9–10.

### R-035-05-006 — Electrical discipline document set (MUST; applicable subset confirmed by `DEL-035-01` and `DEL-035-02`)

The Package Vendor MUST submit the Electrical, lighting, EHT, and grounding documents listed in the Datasheet "Discipline-specific vendor document set — Electrical" table, except for items confirmed not-applicable in the EPC Scope of Work (`DEL-035-01`) or Package Datasheet (`DEL-035-02`).

- Source: `_Sources/26020-Package_Requirements.docx` Table 4, rows 64–80 (Electrical, lighting, EHT, grounding family).
- ASSUMPTION: Lighting (ELE-017), Grounding (ELE-012, ELE-019), Cable Schedule (ELE-014), Cable Tray (ELE-015), Layout (ELE-016), Equipment Data Sheets (ELE-020), Installation Details (ELE-027), Interconnection (ELE-028), FAT/SAT (ELE-029), Test/Energization (ELE-030) apply to a 13.8kV switchgear electrical building based on workbook row 37 family flags (`X` for Electrical Power, Grounding/Bonding, Area/Exterior Lighting). EHT marked None at the package row; ELE-018 and PIP-020/PIP-021 are therefore not required for this package.

### R-035-05-007 — Cross-discipline document families per workbook row 37 (MUST submit applicable family documents; SHOULD coordinate non-applicable families with EPC)

For each cross-discipline family flagged `X` on workbook row 37, the Package Vendor MUST submit the vendor documents that fall within the package vendor's scope as defined by `DEL-035-01`/`DEL-035-02`; for each family flagged None, the Package Vendor SHALL NOT submit standalone documents under this turnover package.

| Family | Workbook flag | Action |
|---|---|---|
| Electrical Power | X | Submit applicable Electrical documents |
| Grounding / Bonding | X | Submit ELE-012, ELE-019 |
| Area / Exterior Lighting | X | Submit ELE-017 |
| I&C / Control Cabling | X | Submit applicable INS-* and CTL-026 documents |
| Communications / Network | X | TBD (no dedicated Table 4 family) |
| Building HVAC / Services | X | TBD (no dedicated Table 4 family) |
| Fire & Gas / Safety Systems | X | Submit applicable TSF-* documents |
| Maintenance Access | X | TBD (no dedicated Table 4 family) |
| Grading / Site Drainage / Spill Containment | X | TBD (no dedicated Table 4 family) |
| Structural / Foundations / Supports | X | Submit applicable STR-* documents |
| Utility Piping | X | TBD (no dedicated Table 4 family) |
| Drain / Containment | X | Submit applicable items (e.g., CIV-014 if within vendor scope) |
| Process Piping | None | Not required |
| Relief / Flare / Vent | None | Not required |
| EHT | None | Not required (ELE-018 excluded) |
| Cathodic Protection | None | Not required |
| Product Loading | None | Not required |
| Pipeline / Pigging | None | Not required |

- Source: `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages sheet, row 37; `_Sources/26020-Package_Requirements.docx` Table 4 rows 82–117.

### R-035-05-008 — Submittal status and disposition tracking (MUST)

The Vendor Document Register MUST carry for each row: document ID, document name, vendor doc number/rev, status (e.g., Issued for Review / Approved / Approved with Comments / Final), submittal date, review-cycle disposition, and turnover-acceptance disposition.

- Source: Inferred from DOC-008 "Vendor Document Control Procedure" purpose (Table 4 row 3) and from `DEL-035-06` EPC Vendor Package Review and Acceptance scope ("Vendor document review log; package acceptance checklist; ... turnover evidence" — `DELIVERABLE_REGISTER.csv` row `DEL-035-06`). ASSUMPTION: specific field set above is conventional for vendor document registers; exact field names are `TBD` until project document-control standard is supplied.

### R-035-05-009 — Turnover package compilation (MUST)

The final turnover package MUST be compiled as a self-contained set comprising at minimum (a) the final Vendor Document Index (PRQ-009), (b) Manufacturing Record Book (QLT-021), and (c) Final Supplier Documentation set (PRQ-016), with all individual vendor documents either embedded or unambiguously referenced.

- Source: Inferred from Table 4 rows 2, 8, and 11 (the three "compilation-anchor" vendor documents) and from the deliverable's defined Anticipated Artifacts ("turnover records") in `_CONTEXT.md`. ASSUMPTION: compilation structure (embedded vs referenced) is conventional; specific format is `TBD`.

### R-035-05-010 — EPC Integrator interface/integration review (MUST permit; review itself is `DEL-035-06`) 

The Package Vendor MUST submit each vendor document at a maturity sufficient for EPC Integrator interface/integration review and incorporate review dispositions back into the Vendor Document Register before turnover.

- Source: `_CONTEXT.md` (Responsible Party); `DELIVERABLE_REGISTER.csv` row `DEL-035-06`.

## Standards

| Standard / governing document | Status |
|---|---|
| `_Sources/26020-Package_Requirements.docx` Table 4 ("Core vendor documents" and discipline tables) | Governing for the vendor document set baseline |
| EPC Scope of Work (`DEL-035-01`) and Package Datasheet (`DEL-035-02`) | Will confirm package-specific applicable subsets; not yet drafted at time of this Specification (location TBD) |
| Project Document Control / numbering standard | location TBD; not present in accessible sources |
| Vendor Data Book / turnover format standard | location TBD; not present in accessible sources |
| IEEE / IEC / CSA electrical standards (e.g., MV switchgear test standards) | Not enumerated in the accessible Package Requirements source for `PKG-035`; ASSUMPTION: likely applicable; do not derive clause-level requirements without source access |

## Verification

| Requirement | Verification approach |
|---|---|
| R-035-05-001 | Inspect Vendor Document Index; confirm enumeration of every Core and Electrical-discipline document required for `PKG-035` |
| R-035-05-002 | Inspect Vendor Document Control Procedure; confirm numbering, revision, transmittal, comment incorporation, and turnover sections |
| R-035-05-003 | Confirm presence of QLT-006, QLT-003, QLT-013, QLT-020 in the Index and as submittal entries with final dispositions |
| R-035-05-004 | Confirm QLT-021 and PRQ-016 are compiled and indexed |
| R-035-05-005 | Confirm PRQ-013 and PRQ-015 are submitted |
| R-035-05-006 | Cross-check Electrical-family submittals against the Datasheet table; confirm exclusions match `DEL-035-01`/`DEL-035-02` |
| R-035-05-007 | For each `X`-flagged family, confirm at least the listed family documents are present; for None-flagged families, confirm absence |
| R-035-05-008 | Inspect Vendor Document Register fields against the field list (or project document-control standard once available) |
| R-035-05-009 | Confirm turnover package contains PRQ-009 (final), QLT-021, PRQ-016 and references every other vendor document |
| R-035-05-010 | Confirm review-cycle and turnover-acceptance dispositions are recorded in the Register; cross-reference `DEL-035-06` review log |

## Documentation

Anticipated artifacts produced by this deliverable (from `_CONTEXT.md`):

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records (Manufacturing Record Book / Vendor Data Book and Final Supplier Documentation)
