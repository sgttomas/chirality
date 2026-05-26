# Specification — DEL-083-05 Vendor Document Turnover Package

## Scope

This specification governs the composition, completeness, identity, and acceptance of the **Vendor Document Turnover Package** for `PKG-083 Inlet Separators 3-25` (vendor tag `26020-02-PT-17-003`). It covers:

- the vendor document register (index of all vendor-produced documents);
- vendor document submittals (each individual document instance, with revision control);
- source-required vendor documentation rows (the engineering deliverable rows enumerated by the 26020 package source);
- turnover records (transmittals, acceptance records, final Vendor Data Book closeout).

Excluded:

- physical equipment supply, fabrication, and FAT execution itself (those belong to other PKG-083 deliverables; this package is the documentary turnover only);
- EPC-Integrator-produced facility integration documents (e.g., facility P&IDs, plant-wide IFC drawings); the Package Vendor produces the package-scope documents and the EPC Integrator reviews them at the interface.

Responsibility:

- **Authoring:** Package Vendor.
- **Interface / integration review:** EPC Integrator.
- **Approval:** Per K-AUTH-1, only humans (vendor and integrator authorities) author binding approval records.

## Requirements

### REQ-VDT-01 — Mandatory vendor deliverable rows

The turnover package SHALL contain a submittal slot, with revision history, for every vendor engineering deliverable row listed in `26020-Package_Requirements.docx` heading 36 (Vendor Engineering Deliverables table) for PKG-083. The mandatory rows are reproduced in `Datasheet.md` Construction section and include all of the following families:

- Core vendor documents (PRQ, DOC, QLT) — 10 rows
- Core package engineering (MEC) — 14 rows
- Static pressure equipment (MEC-005, MEC-009, REG-022) — 3 rows
- Relief / flare / vent (PRO-014 through PRO-018) — 5 rows
- Process piping interfaces (PRO-008, PIP-003 through PIP-028) — 12 rows
- Utility piping (PRO-011)
- Drainage / containment (PRO-023, CIV-014)
- Electrical, lighting, EHT, grounding (ELE-017, ELE-018, PIP-020, PIP-021, ELE-012, ELE-019)
- Instrumentation and controls (INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-016, INS-017, INS-018, INS-025, INS-029, CTL-003, CTL-005, CTL-006, CTL-026)
- Building / HVAC / code (PRO-024, TSF-023, REG-021, STR-002, STR-012)
- Fire and gas / technical safety (TSF-002, TSF-003, TSF-004, TSF-009, TSF-011, TSF-013, TSF-028)
- Structural, foundations, supports, access (STR-001, STR-004, STR-005, STR-006, STR-011, STR-013, STR-014, STR-020)

Source: `26020-Package_Requirements.docx` heading 36 — "26020-02-PT-17-003 - Inlet Separators", Vendor Engineering Deliverables table. `location TBD` for clause-level numbering inside the Word document.

### REQ-VDT-02 — Vendor document register (PRQ-009)

A current `PRQ-009 Vendor Document Index` SHALL be the controlled register-of-record. Every other document in this turnover package SHALL appear as a row in PRQ-009. Conflict between PRQ-009 and the standalone documents SHALL be resolved in favour of the latest accepted vendor submittal and reconciled in PRQ-009.

### REQ-VDT-03 — Document control

A current `DOC-008 Vendor Document Control Procedure` SHALL define numbering, revision codes, transmittal mechanics, hold/IFR/IFA/IFC states, and acceptance routing. All submittals SHALL follow that procedure.

### REQ-VDT-04 — Identity preservation

Each submittal SHALL preserve the source deliverable ID (e.g., `MEC-009 Pressure Vessel Data Sheets`) in its filename or transmittal metadata so that the turnover package can be traced row-by-row against the source vendor engineering deliverable table.

### REQ-VDT-05 — Acceptance and turnover state

The turnover package is COMPLETE when:

1. Every row in REQ-VDT-01 has at least one accepted submittal recorded in PRQ-009; AND
2. `QLT-021 Manufacturing Record Book / Vendor Data Book` and `PRQ-016 Vendor Data Book / Final Supplier Documentation` are at IFC / Final-Issued status; AND
3. `MEC-022 Equipment FAT / Performance Test Report`, `QLT-020 Inspection Release Certificate`, and `MEC-023 Vendor Data Book / Mechanical Final Documentation` have been transmitted and accepted; AND
4. The EPC Integrator interface/integration review has been recorded for the integration-relevant rows (interfaces enumerated in `Datasheet.md` Attributes — Applicable interface types).

Item 4 acceptance criteria detail: `TBD` pending the integrator's review checklist.

### REQ-VDT-06 — Standards and codes

Standards governing individual vendor documents (pressure vessel code, ABSA registration for `REG-022`, ASME B31.3 for piping, etc.) are inherited from the underlying equipment specification deliverables and from the project specification basis. This turnover package does not redefine those standards; it only requires that each submittal cite the standard it satisfies.

- ASSUMPTION: Pressure vessel registration is via ABSA (Alberta jurisdiction for West Doe). `location TBD` — source text identifies `REG-022 Pressure Equipment Registration Package` but does not specify jurisdiction in the slice read.

### REQ-VDT-07 — Source-row artifact handling

Where individual source vendor document table rows are available as raw artifacts (per `_CONTEXT.md` anticipated artifacts list), they SHALL be carried in this turnover package as evidence supporting the corresponding PRQ-009 register row. They do not become separate deliverables (per the Gate 5 ruling captured in the decomposition note: "individual source document rows remain artifacts/evidence, not separate deliverables").

## Standards

| Standard / Authority | Applies to | Local source access |
|---|---|---|
| Vendor engineering deliverable list, 26020 issuance | Composition of the turnover package | Available: `_Sources/26020-Package_Requirements.docx` heading 36 |
| RFQ basis | Vendor scope definition | `Bid Docs/Budgetary/26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx` — `location TBD` (referenced but not opened during this draft) |
| ABSA / pressure equipment registration regime | `REG-022` submittal | `location TBD` — ASSUMPTION (Alberta jurisdiction) |
| ASME pressure vessel and piping codes | `MEC-005`, `MEC-009`, piping-family submittals | Not opened locally; cited by inherited equipment-spec deliverables (`location TBD`) |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-VDT-01 | Audit PRQ-009 against the source vendor engineering deliverables table; one row per source row required. |
| REQ-VDT-02 | Confirm PRQ-009 is the latest revision; cross-check entries against the directory of submitted files. |
| REQ-VDT-03 | Confirm DOC-008 is issued and that submittals carry rev codes/transmittals consistent with that procedure. |
| REQ-VDT-04 | Spot-check that filenames or transmittal metadata carry the deliverable ID from the source table. |
| REQ-VDT-05 | Acceptance gate review: tick each sub-condition; produce the turnover acceptance record (see `Procedure.md`). |
| REQ-VDT-06 | Spot-check each submittal for its cited standard; flag gaps. |
| REQ-VDT-07 | Confirm raw artifacts (when present) are attached to the correct PRQ-009 register row, not registered as deliverables. |

## Documentation (Required Output Artifacts)

- `Vendor_Document_Register.xlsx` (or equivalent) — instance of PRQ-009 for this package.
- Individual vendor submittal files, named per DOC-008.
- Transmittal records / acceptance records (per DOC-008).
- Final Vendor Data Book (PRQ-016 / QLT-021 / MEC-023) at turnover.
- Turnover Acceptance Record (covers REQ-VDT-05 conditions; signature authority per K-AUTH-1).

`location TBD` for the final filenames and storage location inside this deliverable folder; those are set by the executing project at submittal time, not by this specification.
