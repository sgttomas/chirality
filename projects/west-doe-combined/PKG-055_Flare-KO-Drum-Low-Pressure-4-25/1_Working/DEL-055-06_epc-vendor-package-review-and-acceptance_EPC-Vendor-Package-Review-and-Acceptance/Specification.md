# Specification — DEL-055-06 EPC Vendor Package Review and Acceptance

> Normative specification for the review-and-acceptance evidence package the EPC
> Integrator must produce against the LP Flare KO Drum vendor package (PKG-055).

## Scope

### Covered
- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-055-04).
- EPC Integrator review of the Vendor Document Turnover Package (DEL-055-05).
- Integration acceptance against the EPC Scope of Work (DEL-055-01), Package
  Datasheet (DEL-055-02), and Construction Work Package (DEL-055-03).
- Production of: vendor document review log, package acceptance checklist,
  test/inspection evidence index, and turnover evidence record.

### Excluded
- Vendor-side engineering, design, and fabrication (owned by DEL-055-04).
- Vendor document submittal authorship (owned by DEL-055-05).
- Construction execution work (owned by DEL-055-03).
- Process design basis authorship (owned by upstream DBM and DEL-055-02).

## Requirements

| ID | Requirement | Authority | Verification |
|---|---|---|---|
| REQ-06-01 | The EPC Integrator SHALL maintain a vendor document review log that records each vendor submittal, review status (Approved / Approved-as-Noted / Rejected / Information), reviewer, date, and disposition reference. | `_CONTEXT.md` Anticipated Artifacts; SOW-0083..0086 (decomposition) | Inspect review log; spot-check submittals listed in DEL-055-05 register. |
| REQ-06-02 | The acceptance checklist SHALL verify the vendor package against the EPC Scope of Work (DEL-055-01), Package Datasheet (DEL-055-02), and Construction Work Package (DEL-055-03) item-by-item. | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv | Cross-reference checklist rows to source items in DEL-055-01/02/03. |
| REQ-06-03 | Test and inspection evidence SHALL include vessel pressure test records, NDE records, instrument loop-check records, and FAT/SAT certificates as applicable to the LP Flare KO Drum package. | ASSUMPTION (typical for ASME Sec VIII Div 1 vessel packages); location TBD pending `26020-Package_Requirements.docx` heading 10 | Inspect evidence index; confirm each record matches the vendor's certified inspection plan. |
| REQ-06-04 | Turnover evidence SHALL include mechanical completion certificate, punchlist closure record, vendor data book transmittal, and as-built redlines (when applicable). | ASSUMPTION; location TBD pending source. | Inspect turnover package against CWP turnover checklist (DEL-055-03). |
| REQ-06-05 | Layout and siting acceptance SHALL confirm compliance with flare/KO-drum spacing rules: distance between flare tanks (including KO drums) and vegetation or other fire hazards >= 10 m. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. "Flare and Incinerator Spacing" | Compare as-built plot coordinates to governing plot plan; reconcile to CIV-235633-5002 when issued. |
| REQ-06-06 | Acceptance SHALL not be issued while open items remain on the punchlist that would prevent safe commissioning, fire-safe operation, or code compliance. | ASSUMPTION (standard EPC practice); location TBD | Review punchlist closure record before acceptance signature. |
| REQ-06-07 | All acceptance decisions SHALL be traceable to identified SoW items (SOW-0083, SOW-0084, SOW-0085, SOW-0086) and objectives (OBJ-001, OBJ-004..OBJ-010) for PKG-055. | OBJECTIVE_SCOPE_MAP.csv (GATE-07); `_CONTEXT.md` | Spot-check checklist coverage of each SoW item. |
| REQ-06-08 | Vendor identity, vendor scope split, and detailed acceptance criteria specific to the LP Flare KO Drum SHALL be captured against the EPC Package Datasheet (DEL-055-02) and Package Requirements heading 10. | location TBD pending readable extraction of `26020-Package_Requirements.docx` heading 10 | TBD until source extracted. |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| ASME Section VIII Division 1 | Pressure vessel (LP Flare KO Drum) — ASSUMPTION pending source confirmation | location TBD |
| ASME B31.3 | Process piping tie-ins — ASSUMPTION pending source confirmation | location TBD |
| OGAOM Sec. 9.6.15 | Flare/incinerator spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Thermal radiation flux limits | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| API 521 / API 537 | Flare system / flare equipment design — ASSUMPTION pending source confirmation | location TBD |
| `26020-Package_Requirements.docx` heading 10 | Package requirements for PKG-055 | binary source; location TBD |

## Verification

| Method | Applies To |
|---|---|
| Document review (against SoW, Datasheet, CWP) | REQ-06-01, REQ-06-02, REQ-06-07, REQ-06-08 |
| Records inspection (test, NDE, FAT/SAT, MCC) | REQ-06-03, REQ-06-04 |
| Layout reconciliation against plot plan CIV-235633-5002 (when issued) | REQ-06-05 |
| Punchlist closure inspection | REQ-06-04, REQ-06-06 |

## Documentation

Artifacts produced under this deliverable:

- Vendor Document Review Log (table; one row per submittal)
- Package Acceptance Checklist (SoW / Datasheet / CWP cross-reference)
- Test & Inspection Evidence Index (pointers to vessel hydro, NDE, FAT/SAT)
- Turnover Evidence Record (MCC, punchlist closure, data-book transmittal)

All artifacts SHALL cite their evidence sources (vendor document numbers, test
report numbers, drawing numbers).
