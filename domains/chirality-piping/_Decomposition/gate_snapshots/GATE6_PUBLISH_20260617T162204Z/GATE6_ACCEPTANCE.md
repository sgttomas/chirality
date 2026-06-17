# GATE 6 — PUBLICATION & FINAL ACCEPTANCE (chirality-piping)

Status: ACCEPTED
Accepted UTC: 20260617T162204Z
Token: GATE6_ACCEPT_20260617
Human confirmation: "Accepted." (operator terminal acceptance of the published basis)

## DOMAIN_DECOMP COMPLETE
All six gates CLOSED and ACCEPTED (Intake -> Normalize -> Categories -> Knowledge Types -> Coverage -> Publish).

## Published basis
- 158 source units; 21,912 atoms (IN 21,256 / OUT 147 / TBD 509); 1,812 vocabulary terms.
- 30 Categories (18 PKG 1:1 + 12 cross-cutting); 30/30 CLUSTER_COHERENT.
- 98 Knowledge Types + 630 Subjects; 98/98 CLUSTER_COHERENT; every IN atom carries CategoryID + primary KTY + Subject.
- Section coverage attested: 5,035 sections; 3,633 with IN atoms; 1,402 cov-empty all attested scaffold-for-fill (OI-024). Structural invariants pass (UnassignedINUnits=0, UnitsWithoutKnowledgeTypeMapping=0).
- Integrity validator: PASS (0 CRITICAL / 0 MAJOR / 0 MINOR); all six annexes resolve.
- Objectives layer omitted by design (Deviation A); annex_objectives.csv header-only.

## Documented deferred caveats (accepted basis; future scope-change amendments, not blockers)
- OI-025 — 509 TBD-scope atoms uncategorized (IN decomposition complete).
- 147 OUT atoms — out of scope by author disposition.

## Artifacts
- Control surface: Chirality_Piping_Domain_Decomposition.md (status ACCEPTED).
- Publication manifest: Gate6_Publication_Manifest.csv (per-artifact SHA-256; 18 artifacts).
- Readiness packet: Gate6_Publication_Readiness.md. Integrity: Domain_Integrity_Report.md / Findings.csv.
- Companion inventory: Companion_Inventory.csv (2,468 rows).

## Scope
This is the accepted basis for downstream work. Any amendment (OI-025 TBD disposition,
new-file admission, re-atomization) requires an explicit scope-change cycle.
