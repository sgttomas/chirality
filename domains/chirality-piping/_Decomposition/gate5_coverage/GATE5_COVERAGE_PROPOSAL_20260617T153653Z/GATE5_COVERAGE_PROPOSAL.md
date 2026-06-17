# Gate 5 — Verify Coverage Proposal (chirality-piping)

**Status:** ACCEPTED (operator, 2026-06-17). All 46 genuine-gap candidates attested RESOLVE_SCAFFOLD_FOR_FILL.
**Package:** GATE5_COVERAGE_PROPOSAL_20260617T153653Z

## Method
Section-coverage attestation over the accepted Gate-4 ledger
(`Domain_Ledger_Gate4_KTY_Draft.csv`, 21,256 IN atoms), built with the reusable
`tools/decomp/build_gate5_coverage.py` (shared tool, unmodified) driven by two
pack-local adapters:
- `_adapter/gate5_make_source_register.py` — derives the
  `Gate2_Source_Unit_Register.csv` the tool expects from
  `Source_Decomp_Prefix_Map.csv` (158 units; all reviewed skeletons resolve).
- `_adapter/gate5_build_coverage.py` — thin wrapper that runs the tool's own
  main() but skips the two not-yet-authored publication/coordination docs
  (control doc + NEXT_INSTANCE_PROMPT, both Gate-6 / coordination artifacts);
  every substantive coverage step runs unchanged.
Then `_adapter/gate5_classify_coverage.py` machine-classifies every cov-empty
in-scope section and auto-attests the structural/boilerplate/OUT-TBD/template
buckets, surfacing only genuine-gap candidates for review. No atom text,
SourceRef, ContentHash, Category, KTY, or Subject mapping is touched.

## Result
- **158 sources, 5,035 sections, all in-scope.** Density distribution:
  cov-high 2,755 / cov-mid 875 / cov-low 3 / **cov-empty 1,402**.
- **3,633 sections carry IN atoms** → ACCEPTED_GATE5_NONZERO.
- **1,402 zero-coverage in-scope sections classified:**
  - **1,356 auto-attested** ACCEPTED_GATE5_SCAFFOLD_FOR_FILL —
    581 STRUCTURAL_COMPONENT_HEADER (grouped-pack boundary headers),
    560 EMPTY_STUB_SCAFFOLD (empty header stubs),
    139 OUT_TBD_ONLY (in-scope, content dispositioned OUT/TBD),
    76 TEMPLATE_SUBSECTION (standard empty KT-doc template slots).
  - **46 GENUINE_GAP_CANDIDATE — surfaced for operator attestation** (0.9% of
    in-scope sections; PENDING_GENUINE_GAP_REVIEW).

## The 46 genuine-gap candidates (operator decision required)
Characterized (see `Gate5_GenuineGap_Shortlist.csv` + `Gate5_ZeroCoverage_Classification.csv`):
- **29 deliverable persona-doc scaffold headers** — Provenance, Identification,
  Documentation (= the boilerplate "required local artifacts" file checklist),
  Prerequisites, Verification, Records to Preserve, Purpose, Open Questions,
  Semantic Lensing Application, TBD/Human-Ruling slots. Empty or boilerplate
  template scaffolding the authors left for fill; same kind as the 76
  auto-attested TEMPLATE_SUBSECTION rows, just titled/spanned outside the
  heuristic. Verified empty/structural on spot-check.
- **16 in SRC-CODE-VALIDATION** — Provenance / Fixture Notes scaffold plus
  **"Invented Stress Section Inputs"** benchmark **data tables**. The data-table
  ones contain real numeric fixture inputs not separately atomized; the validation
  file is represented in the index/ledger at file grain (grouped-code LEDGER_ATOM),
  so the leaf-section zero is an atomization-granularity artifact, not lost source.
- **1 PRD top-level title block** (SRC-DOCS-PRD L1-11) — front-matter title/abstract
  block; the PRD body is atomized in the sections that follow. Structural.

**Recommendation:** attest all 46 as **RESOLVE_SCAFFOLD_FOR_FILL** (template
scaffolding / structural title blocks / grouped-code fixture data already covered
at file grain) — none require Phase-2 re-dispatch. This mirrors the
chirality-app-dev Gate-5 outcome and the bulk-attested template buckets.
Alternatively, route the SRC-CODE-VALIDATION benchmark-input tables to Phase-2
re-dispatch if you want per-table atoms. Awaiting your decision.

## Integrity
`validate_domain_decomposition_integrity.py`: **1 CRITICAL** = the expected-absent
**objectives** annex (Gate-6 publication layer). The coverage annex that Gate 4
reported missing is now **satisfied**. No Gate-5 problem.

## Pack contents
`Section_Coverage_Register.csv` (per-section density + attestation),
`Source_Coverage_Summary.csv`, `Gate5_Coverage_Telemetry.csv/.json`,
`Gate5_ZeroCoverage_Classification.csv`, `Gate5_GenuineGap_Shortlist.csv`,
`GATE5_COVERAGE_REVIEW_PACKET.md`, `HANDOFF_STATE.md`,
`source_atom_slices/`, `Domain_Integrity_Report.md/Findings.csv`.
