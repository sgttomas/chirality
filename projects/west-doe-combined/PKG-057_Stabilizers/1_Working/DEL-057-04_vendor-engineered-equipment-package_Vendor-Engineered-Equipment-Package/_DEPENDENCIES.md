# Dependencies: DEL-057-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (ACTIVE). 0 rows RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / Ref | Statement (abbreviated) |
|---|---|---|---|---|---|---|---|
| DEP-057-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-057 | Parent package anchor: DEL-057-04 implements PKG-057 Stabilizers |
| DEP-057-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0177 | Traces to SOW-0177: carry Stabilizers as flat vendor package |
| DEP-057-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0178 | Traces to SOW-0178: supply three (3) Inlet Stabilizer Packages |
| DEP-057-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0179 | Traces to SOW-0179: major included equipment; 1272 m³/d; 3×40% |
| DEP-057-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0180 | Traces to SOW-0180: scope notes; operating and design conditions; by-others boundary |
| DEP-057-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-057-01_scope-of-work | DEL-057-01 SOW must be issued and accepted before vendor engineering commences |
| DEP-057-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-057-02_package-datasheet | DEL-057-02 Package Datasheet must be issued and accepted as technical handoff basis |
| DEP-057-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-050 | Process interface: overhead vapour pressure-controlled to SOC first/second-stage suction |
| DEP-057-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-057-05_vendor-document-turnover-package | Vendor hands off documentation register and turnover records to DEL-057-05 |
| DEP-057-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-057-06_epc-vendor-package-review-and-acceptance | Physical vendor package enables EPC review and acceptance under DEL-057-06 |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Guidance.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`.
- **DECOMPOSITION_PATH:** Provided as `GATE-07_Final_Published_2026-05-24/` (path did not exist as given). Resolved to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed present; used for anchor validation and target resolution.
- **Anchor validation:** PKG-057 confirmed in `PACKAGE_REGISTER.csv`. SOW-0177/0178/0179/0180 confirmed in `SCOPE_LEDGER.csv`. All sibling deliverable IDs (DEL-057-01 through DEL-057-06) confirmed in `DELIVERABLE_REGISTER.csv`. PKG-050 confirmed in `PACKAGE_REGISTER.csv`.
- **Parent anchor:** Single `IMPLEMENTS_NODE` row (DEP-057-04-001) for PKG-057. No `FLOATING_NODE` warning.
- **Objective associations:** OBJ-001, OBJ-003..OBJ-010 carried in source documents as `ASSUMPTION` under `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` (per `_CONTEXT.md`). Not emitted as ANCHOR rows in this extraction because the association is ASSUMPTION, not confirmed at the deliverable-ID level. Noted here for downstream reconciliation.
- **PKG-050 interface (DEP-057-04-008):** Target is package-level (PKG-050 SOC), not a specific deliverable. Specification.md R11 and DBM L678/L704 provide explicit process-basis for the overhead vapour interface. `TargetDeliverableID` left empty; `TargetPackageID=PKG-050`.
- **Binary source exclusion:** `26020-Package_Requirements.docx` package heading 12 and RFQ `26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx` are binary and not directly readable. Clause-level claims are surfaced through SOW extracts (SOW-0177/0178/0179/0180) per Guidance.md CONF-02 and Datasheet.md TBD section.
- **No scheduling edges extracted:** Statements of coordination-only alignment were not extracted as EXECUTION edges per skill policy.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill); MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition path resolved to GATE-07 snapshot; 10 ACTIVE rows written; 0 rows RETIRED; schema v3.1; no warnings.
