# GATE 5 — COVERAGE ACCEPTANCE (chirality-piping)

Status: ACCEPTED
Accepted UTC: 20260617T160317Z
Token: GATE5_ACCEPT_20260617
Human confirmation: "attest all 46 as RESOLVE_SCAFFOLD_FOR_FILL in manner that app-dev handled it. Gate 5 is then accepted."

## Result
- Structural invariants pass: UnassignedINUnits=0, UnitsWithoutKnowledgeTypeMapping=0 (every IN atom -> 1 Category + >=1 KTY).
- Telemetry: UnitCount 21,912 (IN 21,256 / OUT 147 / TBD 509); SourceCount 158; SectionCount 5,035 (all in-scope); density {cov-empty 1,402, cov-low 3, cov-mid 875, cov-high 2,755}; Categories 30, KTYs 98, Subjects 630.
- 3,633 sections carry IN atoms (ACCEPTED_GATE5_NONZERO).
- 1,402 cov-empty in-scope sections attested SCAFFOLD-FOR-FILL: 581 component headers, 560 empty stubs, 139 OUT/TBD-only, 76 template subsections, 46 genuine-gap candidates (deliverable persona-doc scaffold headers, SRC-CODE-VALIDATION fixture data tables covered at file grain, 1 PRD title block) — all attested RESOLVE_SCAFFOLD_FOR_FILL, none routed to Phase-2 re-dispatch.
- Coverage tooling reused as-is (build_gate5_coverage.py); pack-local source-register shim + skip-missing-doc wrapper + classifier only. HTML coverage-review surfaces skipped (--skip-render); renderable on demand.
- Objectives annex omitted per persona Deviation A (DOMAIN_DECOMP has no Objectives layer) — handled at Gate 6 publish.

## Accepted artifact SHA-256
- Section_Coverage_Register.csv: 8255a99702075bceec9573364d47ebb617890606d6ab76897dcc2dba06f34481
- Source_Coverage_Summary.csv: 1c1545c3930e74bc909bbfbb2dbd8525490f37d04cfb5b455d048db6e8d09411
- Gate5_Coverage_Telemetry.csv: 3b44db21c7f0818e01b0690230510939a361abc0cf6c496f657866c29b8829af
- Gate5_Coverage_Telemetry.json: 438d2f2b40233a49650ecdfb88c62b23517c8326586dd8087d319c166cac6dd4
- Gate5_ZeroCoverage_Classification.csv: c58c4de184535ebc2772d2d346388d289fce5475d690024daeaf81ea6ebe3cca
- Gate5_GenuineGap_Shortlist.csv: c8f6efd765f2450926111f0561af48239dd6e62cb314a4b2be6b63910e5ce89d

## Scope of this acceptance
Accepts section-coverage attestation + Coverage & Telemetry as the basis for Gate 6 (Publish). Does not create publication truth.
