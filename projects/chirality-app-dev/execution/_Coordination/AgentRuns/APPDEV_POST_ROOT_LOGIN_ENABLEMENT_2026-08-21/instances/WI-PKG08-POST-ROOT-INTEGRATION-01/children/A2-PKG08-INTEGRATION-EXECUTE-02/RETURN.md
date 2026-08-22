# Return — post-Root DEL-08-04 integration executor, attempt 2

Verdict: `PASS`

The accepted post-PR-#602 Root basis and the already-landed App Receipt 172
harness implementation satisfy the owner-enumerated positive and fail-closed
route matrix. All four required check groups exited zero, and the two App files
also passed in one combined run (2 files / 30 tests). No implementation,
product truth, deliverable state, Root surface, or Git state was changed.

## Basis evidence

| Fact | Observed evidence | Result |
|---|---|---|
| Repository / branch basis | repository root `/Users/ryan/.codex/worktrees/ef5e/chirality`; branch `codex/app-post-root-login-proof`; `HEAD` and `origin/main` both `1b375af4f1219ecfc00fc2755854aa7fd4220901` | PASS |
| Required Root integration | `git merge-base --is-ancestor adf805e0d9ac55787e8ac815c3018467babb7f50 HEAD` exited 0 | PASS |
| App Receipt 172 implementation | `git merge-base --is-ancestor ac2cd801a06a0679bc86830c627218ccca78b658 HEAD` exited 0 | PASS |
| Live HELP_HUMAN bytes | Git blob `a9e538c0d9603e18d9884e9f60489be6df8ba1ff`; SHA-256 `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` | PASS, exact pinned values |
| Live HELP_HUMAN route metadata | `agents/AGENT_HELP_HUMAN.md:3-4` includes canonical `TASK` in `subagents` and `allow_generalist_agent2: true` | PASS |
| TM125 routed notice | SHA-256 `eb765dc3bebbf9dd84842643fb22aa989539513843647b562098c96468547864`; notice requests this exact DEL-08-04 matrix and no Root write | PASS |
| APP-HOLD preflight | parent `APP_HOLD_PREFLIGHT.json`: `DEL-08-04` = `CLEAR` / `NOT_HELD`, fingerprint `7f9cc294f286f7b91ee972d615ee9ec59430575c65c200ece57dfe6042476daa`, verdict `ALLOW` | PASS |
| Receipt-172 four-file implementation identity | `git diff --stat ac2cd801a06a0679bc86830c627218ccca78b658..HEAD -- <the two harness sources and two focused tests>` and the equivalent `--name-only` command were empty | PASS; no later drift in the four App files |

Current SHA-256 values used for this evidence packet:

- Root validator: `c99e913ab67ebcbc53cb3487baf0d79fe4d05466ff32bc834124e952157dded1`
- Root validator tests: `e244a10f5b4558946baf3fad265903c4aa871b80eb5f6adbec0e9e7113a614f7`
- App managed-delegation source / test: `0a3dec1309bde70548daee39a48b280ece6886f837d8c4d4b40b85f4f6a6d180` / `2488a5b5f9f960dd9a5467fc1e94317541bbce71d232aedda9eb823376230b63`
- App subagent-governance source / test: `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c` / `8c8609f770ead99ed8b063cd3609513096d7f633cb4821225ab46fe82dce5f01`

## Exact command results

Commands 1-2 ran from the repository root. Commands 3-5 ran from
`projects/chirality-app-dev/frontend`.

| Group | Exact command | Exit | Result |
|---|---|---:|---|
| Root validator | `python3 tools/validation/validate_agent_instructions.py` | 0 | `34 files, 0 errors, 0 warnings` |
| Root validator dedicated tests | `python3 tools/validation/test_validate_agent_instructions.py` | 0 | `Ran 19 tests`; `OK` |
| App managed-delegation focused test | `npm test -- src/__tests__/lib/managed-delegation.test.ts` | 0 | 1 file passed; 19 tests passed |
| App harness-subagent-governance focused test | `npm test -- src/__tests__/lib/harness-subagent-governance.test.ts` | 0 | 1 file passed; 11 tests passed |
| Combined App backcheck | `npm test -- src/__tests__/lib/managed-delegation.test.ts src/__tests__/lib/harness-subagent-governance.test.ts` | 0 | 2 files passed; 30 tests passed |

## Route matrix

| Route / gate | Root validator evidence | App harness evidence | Verdict |
|---|---|---|---|
| Agent 0 -> allowlisted canonical TASK Agent 2 | `test_hierarchy_accepts_help_human_to_manager_and_canonical_task` (`tools/validation/test_validate_agent_instructions.py:139-164`); live metadata pin (`:287-294`); validator admission condition (`validate_agent_instructions.py:271-280`) | Managed launch test `allows configured Agent 0->TASK...` (`managed-delegation.test.ts:127-146`) and canonical-class test (`:166-200`); governance enumeration test (`harness-subagent-governance.test.ts:269-338`) | ADMIT |
| Agent 0 -> explicitly enabled ephemeral generalist | Agent 0 and Agent 1 generalist opt-in is admitted by the type fence (`validate_agent_instructions.py:283-295`); the positive hierarchy fixture carries the opt-in on both parent levels (`test_validate_agent_instructions.py:139-164`); live HELP_HUMAN pin is asserted at `:287-294` | `allows an Agent 0 ephemeral generalist only with explicit frontmatter opt-in` first denies, then admits after setting the flag (`managed-delegation.test.ts:202-226`); runtime branch is `managed-delegation.ts:274-278` | ADMIT only with explicit opt-in |
| Unsupported named Agent 2 under Agent 0 | `test_hierarchy_rejects_agent0_to_non_task_agent2` asserts `AGENT0_CHILD_TYPE` (`test_validate_agent_instructions.py:166-185`) | Managed launch denies Agent 0 named `CANDIDATE` (`managed-delegation.test.ts:229-251`); governance enumeration filters `SPECIALIST` while retaining manager + TASK (`harness-subagent-governance.test.ts:269-338`) | FAIL CLOSED |
| Unresolved child role / instruction | `test_hierarchy_rejects_unresolved_agent0_child` asserts `SUBAGENT_ROLE_UNRESOLVED` (`test_validate_agent_instructions.py:187-203`) | Managed launch's missing-instruction case rejects (`managed-delegation.test.ts:402-419`); enumeration skips an unreadable child instruction (`subagent-governance.ts:150-156`) | FAIL CLOSED |
| Generalist without parent opt-in | Root treats the opt-in as explicit parent metadata and rejects it on any Agent 2 parent (`validate_agent_instructions.py:283-295`; `test_validate_agent_instructions.py:205-226`) | The Agent 0 generalist test rejects before the frontmatter flag is written and admits only afterward (`managed-delegation.test.ts:202-226`); runtime denial is `managed-delegation.ts:274-277` | FAIL CLOSED |
| Any Agent 2 parent route | `test_hierarchy_keeps_agent2_delegation_rejected` asserts `TYPE2_DELEGATION_DECLARED` (`test_validate_agent_instructions.py:261-281`); `test_hierarchy_rejects_generalist_opt_in_on_agent2` asserts `GENERALIST_PARENT_TYPE` (`:205-226`) | `allows Agent 1->TASK and denies every delegation attempt from Agent 2` rejects with `Agent 2 may not delegate` (`managed-delegation.test.ts:280-304`); runtime guard is `managed-delegation.ts:265-270` | FAIL CLOSED |
| TASK missing or carrying non-TASK class | `test_canonical_task_still_requires_task_class` asserts `TYPE2_CLASS` (`test_validate_agent_instructions.py:283-285`) | Managed test rejects missing and `PERSONA` class, then admits `AGENT_CLASS=TASK` (`managed-delegation.test.ts:166-200`); enumeration requires TASK name, Type 2, and TASK class (`subagent-governance.ts:161-172`) | FAIL CLOSED until canonical |

The enumeration gate does not synthesize TASK eligibility: its dedicated test
keeps TASK absent when it is not in the Agent 0 allowlist
(`harness-subagent-governance.test.ts:341-388`). Generalist admission is a
managed-launch route, not an instruction-file enumeration candidate, and is
therefore evidenced by the explicit managed-delegation test and Root metadata
validator rather than by a synthetic governance-enumeration entry.

## Containment and disposition

- Baseline shared worktree changes before this executor wrote its return were
  the active App tranche's TM-APP-032 edits and the untracked run root. No Root
  file, App harness source/test, DEL-08-04 truth, package source, staging area,
  commit, or branch reference was changed by this executor.
- This executor's only intended file additions are this `RETURN.md` and its
  sibling `STATUS.json`, within the sealed child instance directory.
- The evidence here is a derivative run record over accepted Root/App inputs.
  It cites those inputs and does not replace Root instruction truth, App
  product truth, Receipt 172, or DEL-08-04 lifecycle/state truth.
- Blockers: none.
- Required reruns: none on this unchanged basis. Rerun the same four groups if
  the Root validator/instructions or either App harness source/test changes.
- Claim boundary: validation only. This return makes no lifecycle, completion,
  release, reliance, issuance, signing, notarization, distribution, or merge
  claim.

