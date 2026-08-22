# H1 HELPS_HUMANS Return — TM-ROOT-125

Verdict: `PASS_WITH_RECORDED_RESIDUALS`

Applied basis: Root `AGENTS.md` Delegation and Entry Rules as amended
2026-08-02, the owner direction of 2026-08-21, `TM-ROOT-125`, and the sealed
H1 launch brief. This is structural implementation and validation evidence,
not semantic acceptance, lifecycle action, release, reliance, or merge.

## Changed paths

| Path | Disposition | SHA-256 |
|---|---|---|
| `agents/AGENT_HELP_HUMAN.md` | Added canonical `TASK` to `subagents`, added explicit `allow_generalist_agent2: true`, removed the now-stale validator/App-harness blocker sentence; WRITE_SCOPE and authority clauses unchanged | `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` |
| `tools/validation/validate_agent_instructions.py` | Narrow Agent 0 `TASK` exception and Agent 0/1 generalist-parent rule | `c99e913ab67ebcbc53cb3487baf0d79fe4d05466ff32bc834124e952157dded1` |
| `tools/validation/test_validate_agent_instructions.py` | Replaced superseded negative and added positive/fail-closed/live-metadata policy coverage | `e244a10f5b4558946baf3fad265903c4aa871b80eb5f6adbec0e9e7113a614f7` |
| `docs/governance_harness/tranche_manifests/ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821.yaml` | New G4 manifest; includes the full single-tranche closeout envelope requested by parent fan-in | `83b678a2f98897aeb7e3e678e9f7c19b7910fc00222ee0666e5b1885df80d402` |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md` | Reciprocal App notice and DEL-08-04 post-Root check route | `eb765dc3bebbf9dd84842643fb22aa989539513843647b562098c96468547864` |
| `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md` | Piping agent-index change notice | `858ead7d3a013b2aa9ea7b49dab1a6408030d24a9befb0cb383a5c23a86f9c72` |
| `_DomainEngines/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md` | Tier-0/domain-engine agent-index change notice | `60f37ec3a92b7e6e6918c34b142361bb77598b0df561da3937d1fc1c81c48019` |

This instance also writes this `RETURN.md` and `STATUS.json`. It did not
modify registers, receipts, handoff state, App harness/product source, runtime
product code, lifecycle state, release surfaces, Git history, or remote state.

## Behavioral matrix

| Parent / route | Result | Guard |
|---|---|---|
| Agent 0 → named Agent 1 | allowed, unchanged | child declares type 1 |
| Agent 0 → exact role `TASK` | allowed | child declares type 2; the ordinary type-2 class validator still requires `AGENT_CLASS: TASK` |
| Agent 0 → any other named Agent 2 | rejected | `AGENT0_CHILD_TYPE` |
| Agent 0 → unresolved role | rejected | `SUBAGENT_ROLE_UNRESOLVED` |
| Agent 0 → ephemeral generalist | opt-in allowed | parent frontmatter must carry `allow_generalist_agent2: true`; runtime sealed-brief/tool/scope gates remain |
| Agent 1 → Agent 2 / generalist opt-in | allowed, unchanged | existing type and opt-in rules |
| Agent 1 → Agent 1 | rejected, unchanged | `AGENT1_CHILD_TYPE` |
| Agent 2 declaring subagents | rejected, unchanged | `TYPE2_DELEGATION_DECLARED` |
| Agent 2 generalist opt-in | rejected, unchanged | `GENERALIST_PARENT_TYPE` |

The validator exception does not synthesize eligibility: `TASK` must be in
the Agent 0 allowlist, resolve to the exact live role, declare type 2, and pass
the existing `AGENT_CLASS: TASK` check. Ephemeral generalists still require
explicit opt-in plus the runtime's sealed brief, declared context, tools,
permissions, write targets/containment, and durable return evidence. Agent 2
still cannot delegate.

## Pin and mirror census

- App live authority corpus:
  `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json`
  does not pin or list `agents/AGENT_HELP_HUMAN.md`.
- App derivative evidence does SHA-pin the prior file SHA-256
  `f0640b092c12f0f847e0d8df2786ca46bdf916f33e3330bdc54e202c788cbde3`:
  both DEL-09-06 packaged-security `instruction-root/manifest.json` and
  `summary.json` pairs (original and `Remediation_01`), plus the D-APP-86
  parity baseline `SOURCE_MANIFEST.sha256` and `PACKAGE_MANIFEST.sha256`.
- Those immutable packages remain historical run evidence and were not
  overwritten. They become stale only as proof of current Root instruction
  bytes; App decides regeneration through its own instruments.
- No Piping or domain-engine authority snapshot or SHA-pinned mirror was
  found. Piping's `init/dev-loop-init-prompt.md` reads the live Root file.
- App, Piping, and domain-engine notices were therefore routed under the
  `AGENTS.md` agent-index change-notice rule. All say coordination, not
  authority.

## Checks and exact results

1. `python3 tools/validation/test_validate_agent_instructions.py -v` —
   `PASS`, 19 tests.
2. `python3 tools/validation/validate_agent_instructions.py --json` —
   `PASS`, 34 files, 0 errors, 0 warnings.
3. `python3 -m py_compile tools/validation/validate_agent_instructions.py tools/validation/test_validate_agent_instructions.py`
   — `PASS`.
4. `python3 tools/validation/validate_instruction_tranche_manifest.py` —
   `G4 PASS`, 40 schema-valid manifests including this tranche.
5. `python3 -m pytest tools/validation/test_validate_instruction_tranche_manifest.py -q`
   — `PASS`, 46 tests.
6. `python3 tools/validation/validate_instruction_entrypoints.py` — `PASS`.
7. `python3 -m pytest tools/validation/test_validate_instruction_entrypoints.py -q`
   — `PASS`, 22 tests.
8. App focused cross-surface-support tests — `PASS`, 3 files / 32 tests, by
   `npm test -- src/__tests__/lib/managed-delegation.test.ts src/__tests__/lib/harness-subagent-governance.test.ts src/__tests__/lib/coordination-tools.test.ts`
   in dependency-hydrated worktree `ef5e`. SHA-256 comparison proved all five
   harness source/test inputs byte-identical to this checkout. The first
   attempt in this checkout was operationally unavailable (`vitest` and local
   package links absent), not a test failure.
9. `git diff --check` — `PASS`.

The pre-commit command
`python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --tranche ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821`
cannot validate this uncommitted H1 work. It correctly reported four
pre-existing branch instruction paths outside this tranche while `HEAD` did
not yet contain the new manifest or H1 edits. Parent/CHANGE must rerun the
governed candidate-range form after the dependency-ordered commit exists:
`--base origin/main --head HEAD --added-manifests-only`.

## Residuals and derivative disposition

1. `docs/TYPES.md` section 4.3,
   `docs/WORKFLOW_COMPONENT_STANDARD.md` section 4.1, and
   `docs/DBM_Agent_Instruction_Architecture.md` section 2 retain older
   Agent-1-only prose. They conflict textually with the applied Root
   `AGENTS.md` 2026-08-02 runtime doctrine. They were outside the sealed H1
   writable scope and remain a separate Root-owned concordance follow-on;
   this residual is recorded in all three notices and must be preserved in
   fan-in/validation.
2. App's DEL-08-04 post-Root integration check remains App-owned and runs
   only after this Root tranche lands. The App notice names commit
   `ac2cd801a06a0679bc86830c627218ccca78b658`, Receipt 172, and the exact
   positive/negative checks.
3. Existing App instruction bundles/parity manifests and public exports are
   derivative packages. Regeneration is deferred to their owning App/release
   workflows; no current immutable evidence is rewritten and no release or
   reliance effect is claimed.

No blocker remains for the bounded TM-ROOT-125 engineering product. The
cross-surface prose conflict prevents claiming complete repository-wide
doctrinal concordance, which this brief did not authorize.

## Next owner

`HELP_HUMAN` performs fan-in, preserves both residuals, and hands the validated
engineering product to the owner-directed Root closeout path. After the
engineering commit exists, Root TASK_MANAGEMENT may close `TM-ROOT-125` as
`RESOLVED_WITH_CHANGE` under its register rules and route the already-written
notices. CHANGE then performs the post-commit G4 candidate-range rerun and
ordinary non-merging PR closeout. App owns its later DEL-08-04 adoption and
cross-surface integration evidence.
