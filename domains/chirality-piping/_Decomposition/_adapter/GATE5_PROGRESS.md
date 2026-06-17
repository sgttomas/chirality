# Gate 5 (Verify Coverage) — progress checkpoint

Persona: **DOMAIN_DECOMP**. Decomposing `projects/chirality-piping/` into
`domains/chirality-piping/`. cwd = monorepo root `/Users/ryan/ai-env/projects/chirality`.
WRITE_SCOPE = repo-metadata only; no content invention; commit/push only when operator asks.

## Method (reuses shared tool; mirrors accepted app-dev Gate 5)
Section-coverage attestation over the accepted Gate-4 ledger via the reusable
`tools/decomp/build_gate5_coverage.py` (UNMODIFIED), driven by pack-local adapters.

## Adapter scripts (pack-local `_adapter/`)
- `gate5_make_source_register.py` → derives `Gate2_Source_Unit_Register.csv` from
  `Source_Decomp_Prefix_Map.csv` (158 units; reviewed skeletons). Prefix-map column
  schema is identical to app-dev.
- `gate5_build_coverage.py` → wrapper around the shared tool. Monkeypatches ONLY
  `update_control_doc` + `update_next_prompt` to skip-if-target-missing (the control
  doc `Chirality_Domain_Decomposition.md` and `_Coordination/NEXT_INSTANCE_PROMPT.md`
  are Gate-6 / coordination artifacts not yet authored; the shared tool's main() tries
  to read them in place and would FileNotFoundError after all substantive artifacts are
  already written). Everything else (registers, summary, telemetry, review packet,
  package dir, atom slices, and the in-place updates to Open_Issues / Validation_Checks /
  Companion_Inventory / Intake_Telemetry which DO exist) runs unchanged. Shared tool untouched.
  Invoke: `python3 _adapter/gate5_build_coverage.py --timestamp <TS> [--skip-render]`.
- `gate5_classify_coverage.py` → classifies every cov-empty in-scope section; auto-attests
  structural/boilerplate/OUT-TBD/template buckets; surfaces genuine-gap candidates. Writes
  AttestationStatus/Note into `Section_Coverage_Register.csv`, emits
  `Gate5_ZeroCoverage_Classification.csv` + `Gate5_GenuineGap_Shortlist.csv`.

## DONE — coverage built + classified (awaiting operator Gate-5 attestation)
- Source register: 158 units, all reviewed skeletons resolve.
- Coverage (skip-render): **158 sources, 5,035 sections (all in-scope)**; density
  cov-high 2,755 / cov-mid 875 / cov-low 3 / cov-empty 1,402. **3,633 sections carry IN atoms.**
- Classification of the 1,402 cov-empty in-scope sections: **1,356 auto-attested**
  ACCEPTED_GATE5_SCAFFOLD_FOR_FILL (581 structural component headers, 560 empty-stub
  scaffolds, 139 OUT/TBD-only, 76 template subsections) + **46 GENUINE_GAP_CANDIDATE**
  PENDING_GENUINE_GAP_REVIEW (0.9% of sections).
- The 46 candidates = 29 deliverable persona-doc scaffold headers + 16 SRC-CODE-VALIDATION
  (Provenance/Fixture scaffold + "Invented Stress Section Inputs" benchmark data tables,
  covered at file grain) + 1 PRD title block. Recommendation: RESOLVE_SCAFFOLD_FOR_FILL
  (none need Phase-2 re-dispatch); operator may instead route the validation input tables
  to Phase 2 for per-table atoms.
- Integrity validator: 1 CRITICAL = expected-absent objectives annex (Gate-6 layer);
  coverage annex now satisfied. No Gate-5 problem.
- Proposal pack: `gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/`
  (Section_Coverage_Register, Source_Coverage_Summary, telemetry csv/json,
  ZeroCoverage_Classification, GenuineGap_Shortlist, review packet, handoff,
  atom slices, integrity report/findings, GATE5_COVERAGE_PROPOSAL.md).

## GATE 5 ACCEPTED (operator, 2026-06-17)
All 46 genuine-gap candidates attested **RESOLVE_SCAFFOLD_FOR_FILL** (none routed to
Phase 2), matching app-dev. Section_Coverage_Register.csv + Gate5_ZeroCoverage_Classification.csv
flipped PENDING_GENUINE_GAP_REVIEW → ACCEPTED_GATE5_SCAFFOLD_FOR_FILL (final tally:
1,402 SCAFFOLD_FOR_FILL + 3,633 NONZERO; 0 pending). Proposal MD = ACCEPTED. Structural
invariants pass (UnassignedINUnits=0, UnitsWithoutKnowledgeTypeMapping=0). Acceptance
snapshot `gate_snapshots/GATE5_COVERAGE_20260617T160317Z/` (GATE5_ACCEPTANCE.md + artifact
SHA-256; Token GATE5_ACCEPT_20260617); `_LATEST_GATE5.md` updated. HTML coverage-review
surfaces skipped (--skip-render); renderable on demand.

**NEXT (do NOT start until operator says so): Gate 6 (Publish)** by adapting
`domains/chirality-app-dev/_Decomposition/_adapter/gate6_*.py`. Objectives annex
handled at publish per persona Deviation A.

## Frozen inputs (Gate 4 accepted baseline)
`Domain_Ledger_Gate4_KTY_Draft.csv` = 21,256 IN atoms; 98 KTYs / 630 subjects.
Acceptance snapshot `gate_snapshots/GATE4_KTY_20260617T153218Z`.
