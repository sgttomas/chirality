# Specification — DEL-098-06 EPC Vendor Package Review and Acceptance

## Scope

This deliverable is the EPC Integrator's review, integration acceptance, and handoff-readiness evidence package for the PKG-098 Tanks, Sour Water (API 650) — 3-25 vendor scope. It evaluates the vendor's engineered package against:

- the EPC Scope of Work (DEL-098-01),
- the Package Datasheet (DEL-098-02),
- the Construction Work Package (DEL-098-03),
- the Vendor Engineered Equipment Package (DEL-098-04), and
- the Vendor Document Turnover Package (DEL-098-05).

It covers scope items `SOW-0221`, `SOW-0222`, `SOW-0223`, `SOW-0224` [`_CONTEXT.md`].

**Excluded** (by others, per `_Sources/26020-Package_Requirements.docx` heading 50): foundations, on-site mounting of tanks, electrical/instrumentation installation, platforms, staircases. Confirming the as-supplied vendor package respects these by-others boundaries is part of acceptance; performing the by-others work is not.

This is a review-and-acceptance deliverable; it does not modify the underlying vendor scope or produce vendor-engineered artifacts.

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-098-06-01 | The acceptance package shall demonstrate that every "Vendor Engineering Deliverable" listed in `_Sources/26020-Package_Requirements.docx` heading 50 has been received, reviewed, and dispositioned (Accepted / Accepted with comments / Rejected). | `_Sources/26020-Package_Requirements.docx` heading 50, "Vendor Engineering Deliverables" (PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016, MEC-001..MEC-025, MEC-005, MEC-011, PRO-014..PRO-018, PIP-003..PIP-009) |
| REQ-098-06-02 | The acceptance evidence shall confirm conformance of the as-supplied package to the EPC Package Datasheet (DEL-098-02) and any controlling design conditions therein. | DEL-098-02 (sibling in PKG-098); ASSUMPTION — concrete datasheet values not in scope of this read |
| REQ-098-06-03 | The Inspection and Test Plan (ITP, QLT-003) and Inspection Release Certificate (QLT-020) shall be present, signed, and reconciled against the Manufacturing Record Book / Vendor Data Book (QLT-021 / PRQ-016 / MEC-023). | `_Sources/26020-Package_Requirements.docx` heading 50, vendor deliverables list |
| REQ-098-06-04 | Material Test Reports / Certificates (QLT-013) shall be traceable to each tank shell, bottom, and roof course for the seven tanks in scope (TK-9010-1, TK-9020-1, TK-9010-2, TK-9020-2, TK-9030-2, TK-9040-2, TK-9050-2). | `_Sources/26020-Package_Requirements.docx` heading 50, Item Nos. 1-3 |
| REQ-098-06-05 | The acceptance shall verify that the supplied tanks meet the stated process function (sour produced water and produced water atmospheric storage at ~10 °C operating temperature, atmospheric operating pressure) and that any TBD operating conditions (other temperatures, throughput) have been resolved in the vendor data book before acceptance. | `_Sources/26020-Package_Requirements.docx` heading 50, "Scope Notes / Open Items" |
| REQ-098-06-06 | The acceptance shall verify physical-interface conformance against the Package Interfaces row 93: process piping, relief/flare/vent, drain/containment, area/exterior lighting, grounding/bonding, cathodic protection, I&C/control cabling, grading/site drainage/spill containment, and structural/foundations/supports tie-points. Interfaces marked "No" shall not appear in the supplied vendor scope. | `_Sources/26020-Package_Requirements.docx` heading 50, "Physical Interface Summary"; `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 93 |
| REQ-098-06-07 | The acceptance shall verify that the Equipment FAT / Performance Test Procedure (MEC-021) was executed and that the resulting FAT Report (MEC-022) has been accepted before turnover. | `_Sources/26020-Package_Requirements.docx` heading 50, vendor deliverables list |
| REQ-098-06-08 | The acceptance shall confirm receipt of the Logistics / Shipping Plan (PRQ-013), Spare Parts Interchangeability Record (PRQ-015), Mechanical Spares / Special Tools Requirements (MEC-024), and Equipment IOM Manual (MEC-025) prior to turnover. | Same source |
| REQ-098-06-09 | The acceptance shall confirm that PSV / pressure-relief sizing (PRO-015), relief valve data sheets (PRO-016), flare load summary (PRO-017), and blowdown / depressurization study (PRO-018) — to the extent the vendor's scope produced them — are consistent with the EPC Relief and Flare Design Basis (PRO-014). | `_Sources/26020-Package_Requirements.docx` heading 50, "Relief / flare / vent design" subgroup |
| REQ-098-06-10 | The acceptance shall record outstanding open items (TBDs, conditional acceptances, deferred punch-list items) and route them through the EPC change-management process before final close-out. | ASSUMPTION — EPC acceptance convention; not stated in heading-50 slice. location TBD for governing EPC change-management procedure. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650 (Welded Tanks for Oil Storage) | Governs the tank design for the seven 3800 bbl tanks in scope. | ASSUMPTION — implied by package name and analog 4-25 heading; clause-level basis location TBD in heading-50 slice. |
| EPC Scope of Work (DEL-098-01) | Governs the EPC integrator's scope boundary against which the vendor package is accepted. | Sibling deliverable folder `DEL-098-01_scope-of-work_Scope-of-Work/` |
| EPC Package Datasheet (DEL-098-02) | Governs design conditions to which the vendor package must conform. | Sibling deliverable folder `DEL-098-02_package-datasheet_Package-Datasheet/` |
| EPC Construction Work Package (DEL-098-03) | Governs construction-handoff acceptance criteria. | Sibling deliverable folder `DEL-098-03_construction-work-package_Construction-Work-Package/` |
| Project-level acceptance / change-management procedure | Governs disposition routing for open items at acceptance. | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-098-06-01 | Document-by-document review log: each Vendor Engineering Deliverable entry from the heading-50 list is checked off in the vendor document review log with rev, date received, reviewer, and disposition. |
| REQ-098-06-02 | Side-by-side comparison of vendor data sheets vs. DEL-098-02 Package Datasheet values; deltas recorded in the acceptance checklist. |
| REQ-098-06-03 | ITP/IRC reconciliation worksheet: every ITP hold/witness point cross-referenced to an IRC line; gaps flagged. |
| REQ-098-06-04 | MTR traceability matrix: tank-tag × component (shell course / bottom / roof) × heat number × MTR document ID. |
| REQ-098-06-05 | Operating-conditions reconciliation table extracted from vendor data book versus heading-50 source values; any remaining TBD is escalated. |
| REQ-098-06-06 | Interface-by-interface walkdown checklist against Package Interfaces row 93; "No" interfaces verified absent in supplied scope. |
| REQ-098-06-07 | FAT report review with witness signatures and disposition. |
| REQ-098-06-08 | Receipt-of-document checklist with rev/date confirmations. |
| REQ-098-06-09 | Cross-reference table: vendor PRO-015..PRO-018 outputs vs. EPC PRO-014 inputs. |
| REQ-098-06-10 | Open-items log appended to acceptance package, with disposition route per EPC change-management procedure (TBD). |

## Documentation

Per `_CONTEXT.md` ("Anticipated Artifacts") the acceptance deliverable shall produce:

1. **Vendor Document Review Log** — table of every received vendor document with rev, reviewer, date, disposition, comment-resolution status.
2. **Package Acceptance Checklist** — itemized checklist mirroring REQ-098-06-01 through REQ-098-06-10 with pass/fail/TBD entries and evidence pointers.
3. **Test / Inspection Evidence** — assembled set of MTRs, ITP records, IRC, FAT report, and any third-party inspection records (links or attached copies).
4. **Turnover Evidence** — final transmittal record (Vendor Data Book PRQ-016 / MEC-023 receipts, shipping/logistics confirmation per PRQ-013, spares acceptance per PRQ-015 / MEC-024, IOM manuals per MEC-025).

All artifacts shall cite the heading-50 source where requirements derive from it.
