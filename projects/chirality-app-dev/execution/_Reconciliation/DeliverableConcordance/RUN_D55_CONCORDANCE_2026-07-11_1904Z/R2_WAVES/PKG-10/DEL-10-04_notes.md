# DEL-10-04 concordance notes — R2 Wave 6 (PKG-10)

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: frontend/ at
`fac46e33f`, byte-identical through HEAD `1976b379d` (orchestrator-verified at
W6 dispatch). Discovery only; no deliverable file, register, or `_STATUS.md`
was modified.

## Census

22 rows total.

By ClaimType:
- REQUIREMENT: 12
- EXCLUSION: 1
- ACCEPTANCE: 2
- IMPLEMENTED_UNMAPPED: 1
- REMAINING_WORK: 4
- REGISTER_DEFECT: 2

By Disposition:
- ALIGNED: 10 (REQ-003, REQ-004, REQ-006, REQ-008, REQ-011, EXC-001, REMAINING-1..4)
- STALE_SPECIFICATION: 5 (REQ-001, REQ-002, REQ-009, ACC-001, ACC-002)
- PARTIALLY_IMPLEMENTED: 4 (REQ-005, REQ-007, REQ-010, REQ-012)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)
- REMAINING_STATE_MISMATCH: 2 (REGISTER-1, REGISTER-2)

AssessmentEvidence tokens: OVERTAKEN 10, STILL CURRENT 4, NOT APPLICABLE 8.

## Central finding (context for the fan-in verifier)

This kit was drafted in the pure future-boundary register (nothing exists;
everything TBD) and INSP-03 (2026-06-21) confirmed that then-true state. The
D-APP-49/50/51/52 staged tranches then landed a ruled live surface squarely on
this deliverable's subject: `DomainEngineProfile`/`OperationProposal` source
types + guards, a closed two-profile registry, four `mcp__chirality__domain_*`
tools (apply excluded outright), the four validation test files, an ADOPTED
OpenPipeStress fixture profile (`_DomainEngines/profiles/open_pipe_stress.yaml`,
D-T0-06 — cited via this project's own `Dependencies.csv` row -004 note), and
committed v1 validation evidence records. This is exactly the W5-flagged
"kit drafted before the tranches lags the ruled surface" class: most non-ALIGNED
rows are kit-lag STALE_SPECIFICATION or bounded PARTIALLY_IMPLEMENTED, not
missing work.

## Least-confident rows (mandatory self-flagging)

- **DEL-10-04-REQ-001 (STALE_SPECIFICATION, MEDIUM).** Alternative reading:
  ACCEPTED_DIVERGENCE — D-APP-49..52 affirmatively permit the staged surface
  and could be read as accepting the transitional state the kit describes.
  I rejected that under the settled W5/W6 rule: rulings permitting the adjacent
  tool surface do not accept the kit-text divergence about it, and the residual
  is repair-shaped (kit rewrite + SPEC §18 / PLAN R7 transcription). If the
  verifier reads the exclusion wording as endpoints-only (no `/api/domain/*`
  exists), the row could even flip toward ALIGNED; the Scope sentence "not
  current core runtime behavior" is what I judged now-false.
- **DEL-10-04-REQ-002 (STALE_SPECIFICATION, MEDIUM).** Alternative:
  IMPLEMENTED_DIFFERENTLY (live snake_case contract vs the spec's camelCase
  field list). I chose STALE_SPECIFICATION because TYPES.md §11.1 (v6) itself
  says the canonical shape is snake_case and camelCase is only a documentation
  view — the spec's field list mis-cites its own source, a wording defect
  rather than a behavior divergence.
- **DEL-10-04-REQ-003 (ALIGNED, MEDIUM).** Alternative:
  PARTIALLY_IMPLEMENTED if "fail before runtime exposure" is read as requiring
  an in-app full-profile validation step at exposure time. Live enforcement is
  adoption-time validator runs (committed v1 reports) plus the registry's
  byte-marker gate and guard library; no runtime full validation is wired.
- **DEL-10-04-REQ-004 (ALIGNED, MEDIUM).** Alternative: the hardcoded
  open_pipe_stress registry literals (path, identity marker, tool-gate markers)
  could be read as OpenPipeStress-specific data inside core runtime, contra
  FR-114. I judged them registration metadata under the D-APP-51 closed-registry
  design (registration IS the gate), not solver assumptions.
- **DEL-10-04-EXC-001 (ALIGNED, MEDIUM).** Alternative: if "domain-engine
  endpoints" includes MCP tools (SPEC §18 says "endpoints and tools"), the
  ruled tool surface makes the exclusion sentence stale → STALE_SPECIFICATION,
  merging into REQ-001's finding. I kept the exclusion ALIGNED on its literal
  item list (endpoints, apply, protected writes, solver integration,
  solver-truth claims), all of which hold.
- **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Alternative: the pec
  fixture surface is deliberately deliverable-less ruled bridge-lane work
  (D-APP-51/52 executed under their own rulings, like DRQ work), so no mapping
  decision is needed. I still coded it because decomposition v3.2 assigns the
  profile-validation/fixture subject to DEL-10-04 with SOW-070 naming only
  OpenPipeStress, and no corpus surface maps the pec fixture to any deliverable.
- **REGISTER-2 (REMAINING_STATE_MISMATCH, MEDIUM).** Alternative: no defect —
  the DEP-10-04-008 note is dated 2026-07-10 history and Remaining item 3
  already records the discharge path. I coded it because the row's
  SatisfactionStatus now lags live evidence (the accepted D53A snapshot exists
  and covers this deliverable), which is MR-5 metadata lag on the register
  surface itself.

## Register-defect summary

- REGISTER-1: `_REFERENCES.md` REF-007 uses a machine-absolute path
  (`/Users/ryan/ai-env/...`); hashes verified correct at both absolute and
  repo-relative paths. Joins the run-wide machine-absolute-REF-path tranche.
- REGISTER-2: `Dependencies.csv` DEP-10-04-008 stays PENDING while its
  discharge evidence (CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z,
  coverage row `DEL-10-04,Y,8,Y,Y`) exists; the dated note also cites the
  superseded SCC_SAFE_MOVES snapshot as `_LATEST`. Tracked by Remaining item 3.
- Not coded as defects: `_DEPENDENCIES.md` Declared Upstream/Downstream "TBD"
  (human-owned by design per docs/SPEC.md §5.2 and the wave brief);
  CSV↔`_DEPENDENCIES.md` counts and lifecycle summary are internally consistent
  (8 rows, SATISFIED 4 / PENDING 4); `validate_dependencies.py` PASS recorded
  2026-07-11 in Evidence_D53A.

## Method notes / deviations

- REQUIREMENT_INDEX.csv listed 12 IDs for DEL-10-04 and matched the re-derived
  set from Specification.md exactly — no parser gap for this deliverable.
- F-APP-3: no other project's execution tree was read. The only cross-project
  material touched is shared root-level surfaces this project's own documents
  cite: `_DomainEngines/profiles/open_pipe_stress.yaml` + `pec.yaml` and their
  `_validation/*.json` reports (cited by `domain-profile-registry.ts` and
  `Dependencies.csv`), `tools/validation/validate_domain_engine_profile.py`
  (cited by `domain-profile.ts` and the profile header), and
  `agents/AGENT_SOFTWARE_DECOMP.md` (REF-007). Piping/pec engine status is not
  judged anywhere; UNMAPPED-1 explicitly fences it. No UNKNOWN cells were
  required — every cross-project-adjacent fact had an own-surface citation.
- "No test exists" claims (REQ-005/REQ-007/REQ-010 overlap and wording-coverage
  gaps) were backed by real searches: grep over `frontend/src/__tests__`,
  `tools/validation/validate_domain_engine_profile.py`, and its pytest for
  overlap/boundary-wording assertions (no hits), plus the VERIFICATION_INDEX
  rows for the four domain test files.
- Hashes in `_REFERENCES.md` were re-verified by direct `shasum -a 256`
  recomputation this run (all seven MATCH) before asserting REQ-009 staleness.
- The python validator's evidence is its committed v1 report files; it is not
  executed by the Vitest gate, and I did not run it (read-only discovery). Rows
  citing it say so explicitly.
- Not row-coded: `MEMORY.md` line 5 still carries the pre-D-APP-37 wording
  "active code implementation is underway" that D-APP-37 ordered repaired in
  `_STATUS.md` history (the `_STATUS.md` repair is done — line 19 now reads
  "future-boundary contract/documentation drafting"). MEMORY.md is neither kit
  nor register, so it fell outside the claim/REGISTER row contracts; flagged
  here for the R5 kit-refresh tranche to sweep.
