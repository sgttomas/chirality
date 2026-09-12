# Root return: D-GOV-43 application tranche (topology A2)

Executor: bounded Type 2 (TASK), Fable 5.1, 2026-09-12. Branch
`claude/chirality-codex-replatform-3999f1`, basis
`e83cb1f47cce55a49aebfc3c84eabc744a32ffad`. Uncommitted working-tree changes;
no Git write operations beyond `git apply`.

## Files changed

- `AGENTS.md` (via `git apply` of `AGENTS.proposed.patch`; applied cleanly, text as-is)
- `docs/CONTRACT.md` (§1.13 K-RUNTIME-1, K-CONTROL-1, K-RESIDENCY-1 retired row, closing paragraph; index row; enforcement-map row re-titled; §3 Retired Invariants now lists K-RESIDENCY-1)
- `docs/SPEC.md` (§14 intro, §14.1 replaced, §14.2 sessions re-expressed, §14.3 and §14.4 replaced by short retired notes pointing to git history)
- `docs/DIRECTIVE.md` (§5 row "No external server requirement"; §7 rewritten with the cross-product constraint verbatim)
- `docs/TYPES.md` (§12: `RuntimeClientCredential` re-expressed as the per-launch token; `RuntimeDaemonStatus`, `RuntimeBackend`, residency types retired; `RuntimeServiceStatus`, `PolicySelection`, `ApprovalRecord`, `ThreadIndexEntry` added; `Agent1RunRequest` and `AgentRunEvidence` freed of residency wording)
- `docs/AGENT_WORKFLOW_RUNTIME.md` (skills table row, skills paragraph, context sentence, `permissionMode` sentence)
- `docs/PLAN.md` (§6 note), `docs/PRD_ROOT.md` (annex note citing D-GOV-43 at `d2878462be59a43b4afc175a8cce85abca9cf696`)
- `tools/validation/validate_candidate_whitespace.py` (docstring: advisory under D-GOV-43 item 11)
- `docs/governance_harness/_DECISIONS/_REGISTER.md` (two D-GOV-43 rows: publication SHA; branch note on the ruled row)
- `docs/governance_harness/tranche_manifests/ROOT-DGOV43-APPLICATION-20260912.yaml` (new)
- this file

## instruction_surface_paths (as declared in the manifest)

AGENTS.md; docs/CONTRACT.md; docs/SPEC.md; docs/DIRECTIVE.md; docs/TYPES.md;
docs/AGENT_WORKFLOW_RUNTIME.md; docs/PLAN.md; docs/PRD_ROOT.md;
docs/governance_harness/_DECISIONS/_REGISTER.md;
tools/validation/validate_candidate_whitespace.py;
docs/governance_harness/tranche_manifests/ROOT-DGOV43-APPLICATION-20260912.yaml

`.github/workflows/harness-premerge.yml` is not listed: no workflow under
`.github/workflows/` invokes the whitespace guard (grep confirmed), so the
workflow is unchanged and the validator carries the advisory note only.

## Validator results

- `validate_agent_instructions.py --json`: files_checked 4, errors 0, warnings 0.
- `validate_instruction_entrypoints.py`: PASS: root instruction entrypoints are canonical.
- `validate_instruction_tranche_manifest.py` (plain): G4 BLOCK, three findings, all
  "routed notice ... does not exist" for the Runtime, App and PEC notice paths.
  Those notices are being written concurrently by other agents; nothing else
  is flagged for the new manifest (INFO: self-merge under the standing grant).
- `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`:
  same three BLOCK findings; the diff portion sees 0 changed paths because the
  work is uncommitted.
- Scratch check: the same manifest validated against a scratch tree containing
  placeholder notice files returns G4 PASS, exit 0.
- `pytest -q` (whitespace + manifest tests): 63 passed, 1 failed:
  `test_live_repo_lane_b_manifest_exists_and_passes` runs `check()` on the live
  checkout and fails only on the three missing notices above. It passes once
  the notices exist. pyyaml 6.0.3 and pytest 9.1.1 present.

## Judgment calls and open questions

1. `merge_gate: owner-authorized-pr` per the brief; HANDOFF §2 says
   `human-gated-pr`. The validator accepts both; the brief's value matches the
   standing grant. `owner_direction` includes a `note` key alongside the three
   required keys; the validator accepts it.
2. `RuntimeClientCredential` was re-expressed rather than retired (per-launch
   tokens still exist). `CodexHostStatus` from "Surfaces touched" was expressed
   as `RuntimeServiceStatus` to match the A2 child model; `CodexThreadIndexEntry`
   became `ThreadIndexEntry` per the brief's wording.
3. SPEC §14.3/§14.4 use the short retired-note option (git history pointer),
   the shorter faithful choice. §14.4 cites items 7 and 13 since the CLI
   retirement follows the daemon retirement.
4. K-STORE-2 in CONTRACT §1.13 still says "Central runtime sessions remain
   JSON/JSONL and import legacy project-local sessions lazily"; it was outside
   the named write scope and is left for the lead to decide.
5. DIRECTIVE §7 keeps a one-sentence pointer to the retired D-GOV-20 pilot text
   rather than a "historical" block, matching the brief's "history" instruction
   at minimal length.
6. `basis` and `approved_source_sha` both equal `e83cb1f47...`; the lead updates
   `approved_source_sha` to the candidate HEAD before merge as planned.
