# GATE 5 — COVERAGE ACCEPTANCE (chirality-app-dev)

Status: ACCEPTED
Accepted UTC: 20260616T163302Z
Token: GATE5_ACCEPT_20260616
Human confirmation: "Gate 5 accepted. Proceed to publishing (Gate 6)."

## Result
- Structural invariants pass: UnassignedINUnits=0, UnitsWithoutKnowledgeTypeMapping=0 (every IN atom -> 1 Category + >=1 KTY).
- Telemetry: UnitCount 11809 (IN 11140 / OUT 107 / TBD 562); SourceCount 92; SectionCount 3046; density {'cov-empty': 987, 'cov-low': 2, 'cov-mid': 381, 'cov-high': 1676}; Categories 16, KTYs 59, Subjects 279.
- 987 cov-empty in-scope sections attested SCAFFOLD-FOR-FILL: 376 component-headers, 368 empty stubs, 124 OUT/TBD-only, 60 template subsections, 59 genuine-gap candidates (code/navigation/structured-data) — all accepted, none routed to Phase-2 re-dispatch (OI-014).
- Coverage tooling reused as-is (build_gate5_coverage.py + render_source_html.py); pack-local shim + classifier only.
- Objectives annex omitted per persona Deviation A (DOMAIN_DECOMP has no Objectives layer) — to be handled at Gate 6 publish.

## Accepted artifact SHA-256
- Gate5_Coverage_Telemetry.csv: 56535a8d306cf58b96a516dc2fd8db87ca68d4986d4316410c8fc4597337387e
- Gate5_GenuineGap_Shortlist.csv: 39e39379717ebb33240c7040eb0777a06565aeec6f3917a39c3d49741d002718
- Gate5_ZeroCoverage_Classification.csv: ce81d110f705ca22bc78c3dd36633cc537227fcd4471dbd6bac59e8f20ebfdc9
- Section_Coverage_Register.csv: 13f8ee0ea63ae17e0090ddd1da91879cce3186d357e90783489903c2263c8b5f
- Source_Coverage_Summary.csv: 88f92860ad51de0053ee51f837cabadaf45fc0a81878a7082daa4bdd091bcee3
- Gate5_Coverage_Telemetry.json: ca4da901f3afe3724242b9a45109877573182fabde04f943a6364bc4f1f04a51

## Scope of this acceptance
Accepts section-coverage attestation + Coverage & Telemetry as the basis for Gate 6 (Publish). Does not create publication truth.
