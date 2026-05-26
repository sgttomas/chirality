# Specification — DEL-073-06 EPC Vendor Package Review and Acceptance (PKG-073 Amine Treating Unit)

## Scope

### In Scope

- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-073-04) and vendor document turnover package (DEL-073-05) for PKG-073 Amine Treating Unit.
- Integration acceptance of the vendor package against the EPC Scope of Work (DEL-073-01), Package Datasheet (DEL-073-02), and Construction Work Package (DEL-073-03).
- Handoff readiness verification for facility integration, construction, commissioning, and turnover.
- Production of vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence (source: `_CONTEXT.md`).

### Out of Scope

- Vendor package engineering, design, fabrication, vendor documentation production (owned by Package Vendor; see `PACKAGE_REGISTER.csv` row PKG-073; OBJ-004).
- Re-authoring of the EPC Scope of Work, Package Datasheet, or Construction Work Package (those are the upstream baseline deliverables).
- Cross-package facility design changes outside PKG-073 boundary.

## Requirements

| Req ID | Requirement | Source | Notes |
|---|---|---|---|
| REQ-073-06-01 | The EPC Integrator shall perform documented review of the Package Vendor scope (DEL-073-04, DEL-073-05) against the EPC Scope of Work (DEL-073-01), Package Datasheet (DEL-073-02), and Construction Work Package (DEL-073-03). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-073-06 | Acceptance baseline is the three upstream EPC deliverables. |
| REQ-073-06-02 | The EPC Integrator shall produce a vendor document review and comment log capturing each vendor document, review status, comments, vendor response, and disposition. | `ARTIFACT_REGISTER.csv` ART-B556C47357 | Disposition lifecycle conventions: ASSUMPTION (e.g., approved / approved-with-comments / rejected / re-submit) — confirm against EPC procedure. |
| REQ-073-06-03 | The EPC Integrator shall produce a vendor package acceptance and turnover checklist covering documentation completeness, physical package completeness, and integration readiness. | `ARTIFACT_REGISTER.csv` ART-0C77AD875E | Checklist line items beyond completeness are `TBD` — source clause text not locally accessible. |
| REQ-073-06-04 | The EPC Integrator shall collect and review factory/shop test and inspection evidence required by the SOW, Datasheet, and applicable codes/standards. | `ARTIFACT_REGISTER.csv` ART-C9A6D6903F; `SCOPE_LEDGER.csv` SOW-0053 | Specific test/inspection list is `TBD` — source enumeration (Word heading 27) `location TBD`. |
| REQ-073-06-05 | The EPC Integrator shall verify that vendor package interface deliverables address all in-scope PKG-073 interface types. | `INTERFACE_REGISTER.csv` PKG-073 rows (13 interface types) | Interface acceptance criteria per interface type are `TBD` pending interface specifications. |
| REQ-073-06-06 | The EPC Integrator shall verify that operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure evidence is present and acceptable for facility handoff. | OBJ-010 | Thresholds for sufficiency are `TBD`; ASSUMPTION: closure evidence per upstream open-issue register. |
| REQ-073-06-07 | The EPC Integrator shall preserve the vendor/EPC responsibility split: review does not re-engineer or substitute for vendor work product. | `PACKAGE_REGISTER.csv` row PKG-073 (responsibility text); OBJ-004 | Review may surface non-conformances; vendor remains responsible for design content. |
| REQ-073-06-08 | The EPC Integrator shall track unresolved open items through documented dispositions (accepted, accepted-with-condition, deferred to commissioning, escalated to human ruling). | OBJ-010 | Disposition vocabulary is ASSUMPTION — confirm against project conventions. |
| REQ-073-06-09 | The EPC Integrator shall confirm that vendor documentation supports facility-level objectives OBJ-005 (electrical), OBJ-006 (controls/instrumentation/F&G/shutdown), OBJ-007 (utilities), OBJ-008 (civil/structural/site), and OBJ-009 (safety/regulatory) at the package boundary. | `OBJECTIVE_REGISTER.csv` rows OBJ-005..OBJ-009; `_CONTEXT.md` | Per-objective acceptance criteria are `TBD` — derive from interface-specific specifications when produced. |
| REQ-073-06-10 | Acceptance shall not be issued by an agent; final acceptance is a human-authored decision (K-AUTH-1). | Root `docs/CONTRACT.md` K-AUTH-1 (governance) | EPC Integrator role here is to assemble evidence; acceptance signature is human. |

## Standards

| Standard / Code Source | Applies To | Source | Status |
|---|---|---|---|
| 26020-Package_Requirements.docx package heading 27 — vendor-document tables and package requirements | Vendor document review scope; package acceptance criteria | `_REFERENCES.md`; `_CONTEXT.md` | `location TBD` — binary `.docx` not extracted to markdown |
| Applicable sour-service, fire/gas, environmental, regulatory codes per OBJ-009 | Acceptance of safety/regulatory evidence | OBJ-009 | Code list `TBD` at the package level; defer to vendor-supplied compliance certificates |
| Project commissioning/turnover conventions | Acceptance and turnover checklist | OBJ-010; project convention | `TBD` — convention document not referenced in this deliverable's `_REFERENCES.md` |

## Verification

| Req ID | Verification Approach | Verification Evidence |
|---|---|---|
| REQ-073-06-01 | Documented review records cross-referenced to SOW/Datasheet/CWP clauses | Vendor document review and comment log (ART-B556C47357) |
| REQ-073-06-02 | Inspection of review log completeness against vendor document register | Vendor document review and comment log (ART-B556C47357) |
| REQ-073-06-03 | Inspection of acceptance checklist completion | Vendor package acceptance and turnover checklist (ART-0C77AD875E) |
| REQ-073-06-04 | Inspection of test/inspection evidence pack | Factory/shop test and inspection evidence (ART-C9A6D6903F) |
| REQ-073-06-05 | Cross-check vendor interface deliverables against `INTERFACE_REGISTER.csv` PKG-073 rows | Acceptance checklist interface section |
| REQ-073-06-06 | Inspection of operability/turnover evidence completeness | Acceptance checklist closure section; open-item register |
| REQ-073-06-07 | Audit trail demonstrating reviewer did not re-author vendor scope | Review log change history |
| REQ-073-06-08 | Open-item disposition log review | Open-item closure record (part of turnover evidence) |
| REQ-073-06-09 | Trace of objective-by-objective evidence at package boundary | Acceptance checklist objective-mapping section |
| REQ-073-06-10 | Human signature on final acceptance record | Human-authored acceptance decision artifact |

## Documentation

Required deliverable artifacts (from `_CONTEXT.md` and `ARTIFACT_REGISTER.csv`):

- Vendor document review and comment log (ART-B556C47357)
- Vendor package acceptance and turnover checklist (ART-0C77AD875E)
- Factory/shop test and inspection evidence (ART-C9A6D6903F)
- Turnover evidence (compiled handoff record; specific contents `TBD`)
- Open-item closure / disposition record (ASSUMPTION: part of turnover evidence)
