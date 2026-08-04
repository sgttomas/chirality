# HELPS_HUMANS return — H1 G4 diff-mode CI wiring

Status: **READY FOR HELP_HUMAN FAN-IN — GITHUB CI RERUN REQUIRED**

Basis: `origin/main@97678a841ef58345c73d3470ed8de57c9b1405d2`

Manager: `HELPS_HUMANS`, managed by `HELP_HUMAN` under run
`ROOT_FOUR_LANES_2026-08-02`, plan v2. This is deterministic validator and CI
wiring; no new agent, skill, product authority, or human decision mechanism is
created. Git integration remains assigned to C1/CHANGE and merge remains the
owner's gate.

## Result

The governed `governance-harness` workflow now runs G4 in candidate-range diff
mode:

- pull requests use `github.event.pull_request.base.sha`; pushes use
  `github.event.before`; checked-out `HEAD` is the candidate;
- the existing `HEAD^` fallback is used only when the event base does not
  resolve;
- every manifest in the live corpus is still schema-validated;
- candidate diff coverage is accepted only from tranche manifests newly added
  between base and head; and
- legacy no-argument CI/schema mode, unqualified all-manifest diff mode, and
  explicit `--tranche` callers retain their existing behavior.

The added-only boundary is material. Historical manifests already declare the
exact G4 workflow and tool paths; unqualified all-manifest coverage therefore
cannot prove that a new tranche carries its own manifest. A modified or renamed
historical manifest also cannot satisfy the new CI selector.

## Changed paths and working-file SHA-256

| Path | SHA-256 / role |
|---|---|
| `.github/workflows/governance-harness.yml` | `1471a1f2b996b564f66e874666715bea3cc77b322dc15965f4586743c9f35265`; invokes G4 with event base, `HEAD`, and `--added-manifests-only` |
| `tools/validation/validate_instruction_tranche_manifest.py` | `9fc01c76585586cbaf51eae103095825b3c0dea64fd642029c2106146ca53c2b`; additive candidate-range selector with whole-corpus schema preservation |
| `tools/validation/test_validate_instruction_tranche_manifest.py` | `e4c5ac3541c2fb6ce3d7e5902eac8603279af3859da3124ab3f82b25cd681f4c`; CLI positive, missing-manifest, historical-reuse, schema-preservation, applicability, and workflow-wiring proofs |
| `docs/governance_harness/tranche_manifests/ROOT-G4-DIFF-CI-20260802.yaml` | `e8f4a4ba533e895afbea7d11dcd8771902efe329438d68b973b4d8c05196bcde`; G4 self-application manifest |
| `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/H1-G4-CI/LAUNCH_BRIEF.md` | Parent launch brief; surplus terminal blank line removed within the H1 evidence scope |
| `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/H1-G4-CI/subagents/H1-A2-G4-VERIFY/LAUNCH_BRIEF.md` | `1d72976c68206a318ea8ab7da9632a732550f25d717883d709e426a092d1806f`; sealed read-only Agent 2 brief |
| `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/H1-G4-CI/subagents/H1-A2-G4-VERIFY/RETURN.md` | `a2624338a9a15c58fd273859d78334db92fceea3cc57471e013bb10230c8cc0f`; independent compatibility/edge review |
| this return | H1 fan-in evidence; intentionally not self-hashed |

No exact-path pin or mirror of the G4 workflow, validator, or tests was found
under `projects/` or `domains/`. The tranche changes no `agents/` file. The G4
manifest therefore records M6 `none-required`; no foreign coordination surface
was written.

## Positive and negative proof

The focused CLI proof ran six candidate-range/wiring cases:

```text
test_candidate_range_diff_blocks_when_only_historical_manifest_covers_change PASSED
test_candidate_range_diff_blocks_modified_historical_manifest_reuse PASSED
test_candidate_range_diff_passes_with_added_manifest PASSED
test_candidate_range_diff_preserves_whole_corpus_schema_validation PASSED
test_candidate_range_diff_ignores_non_instruction_change_without_new_manifest PASSED
test_governance_harness_ci_wires_candidate_range_diff_mode PASSED
```

The primary missing-manifest test first proves that legacy unqualified diff
mode returns PASS when a historical exact-path manifest exists. The exact same
base/head range then invokes the new CLI selector and proves exit `1`,
`G4 BLOCK (diff mode)`, the diagnostic `adds no schema-readable tranche
manifest`, and the uncovered `AGENTS.md` path. A second negative proves that
modifying the historical manifest still exits `1`. The positive creates a new
self-covering candidate manifest and protected `AGENTS.md` change and proves
exit `0`, `G4 PASS (diff mode)`, and `checked against 1 manifest(s)`.

## Commands and results

| Command | Result |
|---|---|
| `python3 -m pytest -vv tools/validation/test_validate_instruction_tranche_manifest.py -k 'candidate_range_diff or governance_harness_ci_wires'` | PASS, 6 selected |
| `python3 -m pytest -q tools/validation/` | PASS, 311 |
| `python3 tools/validation/validate_instruction_tranche_manifest.py` | PASS, 26 schema-valid manifests |
| YAML `safe_load` of `.github/workflows/governance-harness.yml` | PASS |
| `python3 -m pytest -q -n auto --dist loadscope tools/` with localhost service permission matching CI capability | PASS, 1147 passed, 2 skipped, 1 unrelated pytest warning |
| `python3 tools/practitioner_harness/harness.py self-check` | Exit 0; existing INFO/WARN/REVIEW findings remain non-BLOCK and are unrelated to H1 |
| live G0, G1, G2, and G3 validators | PASS |
| H1-scoped `validate_candidate_whitespace.py --base-ref origin/main --paths ...` | PASS |
| H1 tracked `git diff --check` | PASS |

The first sandboxed full-tools run reported two software-workflow temporary
HTTP-service startup failures (`exit_code=125`); the focused suite and the full
tools estate both passed when rerun with localhost binding permitted. This is
environmental evidence, not a G4 code failure.

## Fan-in and CI rerun requirements

1. C1/CHANGE must commit the coherent run tranche without rebasing over or
   overwriting foreign lane products.
2. Before commit, rerun candidate whitespace over the whole tranche. The
   current whole-worktree scan is blocked by whitespace in untracked W1/S1/C0/
   E1 records outside H1's write scope; H1's own scoped scan is clean.
3. On the exact PR head, rerun the required `governance-harness` check. Its G4
   step must log `G4 PASS (diff mode)` using the PR base and checked-out HEAD;
   the newly added Root G4 manifest must be among the candidate coverage
   sources. Candidate whitespace, routed tools tests, self-check, and G0-G3
   must also pass.
4. The `push` run on any accepted `main` merge must pass the same G4 step over
   `github.event.before..HEAD`.
5. CI, commit, push, PR, and owner merge evidence are not yet present and must
   be supplied by C1 and the owner gate. Task Management register closure is
   explicitly outside this run.

## Risks and readiness

- GitHub expression expansion and the synthetic pull-request merge ref can be
  proven only by the required hosted CI run, not by local YAML parsing.
- Added-only selection intentionally rejects amendment or rename of an old
  manifest as proof for a new tranche; a new tranche manifest is required.
- No retroactive manifest is synthesized and no disclosed historical gap is
  reclassified.

Subject to whole-tranche whitespace cleanup and the hosted CI rerun above, H1
is ready for HELP_HUMAN fan-in.
