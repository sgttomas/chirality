# Evidence Record: CI and Test-Estate Optimization (2026-07-31)

Status: evidence record per `docs/evidence/README.md`. Non-normative.
Not agent runtime context.

Engagement: one interactive session (owner + one orchestrating model
instance + ~10 subordinate agent instances), conducted in the Agent
0/1/2 idiom — profiling fan-out, sealed execution tranches with
disjoint write scopes, independent verification at every fan-in, all
merges human-ordered.

## 1. Session facts

### Delivered changes

| PR | Merge | Content |
|---|---|---|
| #427 | a7371ed-era main | CI workflows: governance-harness ~2 min to ~80s; harness-premerge ~4.5 min to ~2.5 min |
| #431 | ba0e89f54 | Test-estate optimization: 4 execution tranches (pec, tools, piping, frontend) + CI coverage wiring |
| #432 | 0b26c518d | Path routing for the tools/ estate (profile + runner + drift guards) |
| #437 | 4c1cad5be | Two pre-existing defects: typed manifest-path errors; tool-catalog generator import |
| #438 | 07c7565bd | Routed tools/taskmgmt after the drift guard failed main (first live catch) |

### Measurements (local, before -> after)

| Suite | Before | After |
|---|---|---|
| frontend vitest (1098 tests) | 11.3s | 2.1s |
| tools/ python | 15 invocations, ~11.7s, 159 tests uncollectable | 1 invocation, ~7s, 1078 tests |
| chirality-piping (548 -> 556 tests) | 15.7s serial; 2 fail / 15 error | 4.6s xdist; 556/556 pass |
| pec (356 tests) | 10.9s | 8.4s |
| CI: governance-harness | ~2 min | ~80s (PR), full estate ~30s of that on main |
| CI: harness-premerge | ~4.5 min | ~2.5 min |

Dominant costs, as measured (never "too many tests"; always per-unit
fixed overhead times repetition): one test file was ~95% of frontend
wall time (macOS per-inode first-exec scan of freshly written scripts);
nine identical full-repo self-checks were ~70% of the harness suite;
one repeated scrypt derivation was ~12.5s of pec CPU; two directories
were ~90% of checkout payload.

### Correctness defects found and fixed (all pre-existing)

- 8 files in `projects/chirality-piping/tests/` collected zero tests
  (assertions reachable only via `main()`); revived, all pass live.
- `tools/pdf2md` died at collection without openpyxl (0 of 159 ran).
- `validate_architecture_basis.py` pinned `revision: 0.9` against an
  accepted 0.11 — failing for every contributor.
- `run_evidence_sweep.py` raised raw FileNotFoundError on a missing
  wasm-bindgen (16 downstream test errors).
- Runtime registration surfaced missing manifest paths as
  INTERNAL_FAILURE (raw ENOENT); now typed PROJECT_MANIFEST_INVALID.
- `generate-tool-catalog.mjs` could not run (CJS require of an
  ESM-only subpath); regenerated doc proved byte-identical — no drift
  had accumulated while the tool was broken.
- ~950 passing tests ran on no machine automatically (pec 356; ~590
  under tools/); now CI-gated.

## 2. Rulings and outcomes

Five decision points were routed to the owner before execution. Two
resolved contrary to the orchestrator's recommendation once agents
verified premises; the ruling conditions are what made that safe.

| Ruling | Condition given | Outcome |
|---|---|---|
| A: contract-pin consolidation | "same approach as before" (relocate mechanism, preserve coverage) | 106 pins relocated to one manifest; inventory proof 106 = 106; validated by the gate it modified |
| B: piping loop double-run | dedupe ONLY if results retained as verifiable evidence; else keep both | KEPT BOTH: evidence-sweep is the DEC-025 gate, contract-pinned to re-execute; xdist made both runs cheaper than one had been |
| C: 8 dead test files | revive; deal with consequences | all 8 pass live; zero xfails; anticipated failures did not exist |
| D: coverage | add CI coverage | full tools/ tree + pec workflow added |
| E: claims-language redundancy | reduce; repo-wide single run acceptable | ZERO inline checks removed: per-check verification showed all 45 cover surfaces the repo-wide validator does not scan; consolidation reduced to in-process invocation |

## 3. Boundary-failure log

Every CI failure during the engagement was an interface artifact
between declared scopes, never interior to one:

1. Sparse checkout omitted `runtime/` -> pec's `file:` dependency on
   `runtime/packages/client` unresolvable (PR #431 first pec run).
2. Runner lacked numpy -> `tools/retrieval` import error; local
   machines had it (PR #431 governance run; dependency scan had covered
   test files' imports but not their imports' imports).
3. Removing a duplicate vitest step exposed that daemon registration
   depended on a test side effect creating `.chirality/sessions`
   (PR #427 first premerge run; dependency made explicit).
4. `tools/taskmgmt` landed via an unrelated PR after the routing
   profile was authored -> drift guard failed the full-estate main
   run with a remediating message; routed within hours (PR #438).

## 4. Derived observations (dated induction — see supersession note)

Derived 2026-07-31 by the orchestrating model from Sections 1–3.
Supersession: a reader needing patterns should re-derive from the
facts above with a current model; that derivation supersedes this
list. These are recorded to date-stamp what was believed, not to
direct future work.

1. Claims decay across delegation hops (~1/3 of confident upstream
   claims inverted under verification); verify per hop.
2. Failures concentrate at declared-scope boundaries, not inside
   scopes; invest in dependency declaration.
3. Redundancy hides dependencies; every dedup is a dependency probe.
4. Test-estate cost is power-law distributed; measure before design.
5. Rot occurs on unexecuted paths; execution frequency preserves;
   routing must never take a suite's frequency to zero.
6. Checking systems split into tree-wide invariants (always run) and
   local checks (routable); the split is semantic and stays human.
7. Conditional rulings (criteria, not decisions) compose with agent
   verification; both premise-inversions were absorbed safely because
   the rulings carried conditions.
8. Failure messages are an instruction surface; encode remediation
   where the (increasingly non-human) reader will meet it.

## 5. Promotion trail

Observations that reached executable form during the engagement, via
the normal path (evidence -> human ruling -> enforcement):

- Observation 5 -> the routing drift guards
  (`tools/software_workflow/test_tools_test_routing.py`) and the
  full-estate main-push rule in `.github/workflows/governance-harness.yml`.
- Observation 6 -> `always_checks` vs `path_rules` in
  `tools/tools-test-routing.json`.
- Observation 8 -> typed manifest errors in
  `runtime/packages/core/src/project-registry.ts`; missing-dependency
  reporting in the piping evidence sweep; the drift guard's
  self-describing failure text.

No other observation is promoted. Promotion of any remaining item
requires its own ruling and lands as a guard, gate, profile, or brief
clause — not as guidance prose.
