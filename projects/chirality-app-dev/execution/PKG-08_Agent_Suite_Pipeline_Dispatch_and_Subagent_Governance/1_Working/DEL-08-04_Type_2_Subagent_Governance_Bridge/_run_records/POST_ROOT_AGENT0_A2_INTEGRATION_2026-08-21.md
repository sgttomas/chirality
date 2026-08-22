# Post-Root Agent 0 / Agent 2 Integration Check — 2026-08-21

- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- ManagerInstance: `WI-PKG08-POST-ROOT-INTEGRATION-01`
- Deliverable: `DEL-08-04`
- Accepted basis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- App implementation basis: `ac2cd801a06a0679bc86830c627218ccca78b658`
  (Receipt 172)
- Outcome: `PASS`
- Lifecycle effect: none; state remains `IN_PROGRESS` and Checking Approval SHA
  remains `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

## Basis and source identity

- `HEAD` and `origin/main` were both the accepted basis; PR #602 merge commit
  `adf805e0d9ac55787e8ac815c3018467babb7f50` is its ancestor.
- `agents/AGENT_HELP_HUMAN.md` matched Git blob
  `a9e538c0d9603e18d9884e9f60489be6df8ba1ff` and SHA-256
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`.
  Its live frontmatter allowlists canonical `TASK` and declares
  `allow_generalist_agent2: true`.
- The App implementation commit is an ancestor of the accepted basis. A diff
  from that commit through `HEAD` over the two harness sources and two focused
  tests was empty, so this check exercised the Receipt 172 implementation
  without later four-file drift.
- The routed TM125 notice SHA-256 was
  `eb765dc3bebbf9dd84842643fb22aa989539513843647b562098c96468547864`.
- APP-HOLD dispatch preflight returned `ALLOW`; DEL-08-04 was `CLEAR` and
  `NOT_HELD`, with scan fingerprint
  `7f9cc294f286f7b91ee972d615ee9ec59430575c65c200ece57dfe6042476daa`.

## Admission and fail-closed matrix

| Route | Result | Evidence |
|---|---|---|
| Configured Agent 0 -> allowlisted canonical TASK Agent 2 | ADMIT | Root hierarchy positive fixture and live metadata pin; App managed-launch canonical TASK test; App governance enumeration manager-plus-TASK test |
| Configured Agent 0 -> explicitly enabled ephemeral generalist Agent 2 | ADMIT only with opt-in | Root Agent 0/1 opt-in type fence and live HELP_HUMAN pin; App managed launch denies before `allow_generalist_agent2: true` and admits after it |
| Unsupported named Agent 2 under Agent 0 | FAIL CLOSED | Root `AGENT0_CHILD_TYPE`; App named-candidate launch denial and enumeration filter |
| Unresolved child role/instruction | FAIL CLOSED | Root `SUBAGENT_ROLE_UNRESOLVED`; App missing-instruction launch denial and enumeration skip |
| Generalist without opt-in | FAIL CLOSED | App before/after opt-in test and managed-launch runtime guard |
| Agent 2 as parent | FAIL CLOSED | Root `TYPE2_DELEGATION_DECLARED` / `GENERALIST_PARENT_TYPE`; App `Agent 2 may not delegate` test/runtime guard |
| Missing or non-TASK canonical class | FAIL CLOSED | Root `TYPE2_CLASS`; App missing/`PERSONA` rejection followed by canonical `AGENT_CLASS=TASK` admission |

The governance-enumeration gate does not synthesize TASK eligibility when TASK
is absent from the Agent 0 allowlist. Ephemeral generalist admission is a
managed-launch route, not a synthetic instruction-enumeration candidate.

## Exact checks

| Check | Command / working directory | Result |
|---|---|---|
| Root validator | `python3 tools/validation/validate_agent_instructions.py` from repo root | PASS — 34 files, 0 errors, 0 warnings |
| Root validator tests | `python3 tools/validation/test_validate_agent_instructions.py` from repo root | PASS — 19/19 |
| App managed delegation | `npm test -- src/__tests__/lib/managed-delegation.test.ts` from App `frontend/` | PASS — 19/19 |
| App subagent governance | `npm test -- src/__tests__/lib/harness-subagent-governance.test.ts` from App `frontend/` | PASS — 11/11 |
| Combined App backcheck | `npm test -- src/__tests__/lib/managed-delegation.test.ts src/__tests__/lib/harness-subagent-governance.test.ts` from App `frontend/` | PASS — 2 files / 30 tests |

The WORKING_ITEMS manager independently repeated the Root validator, its 19
tests, and the combined two-file App backcheck: all passed with the same
34/0/0, 19/19, and 30/30 results.

## Managed execution and review posture

The first executor attempt was interrupted before a return and rejected from
fan-in because APP-HOLD preflight had not preceded its dispatch. It produced no
accepted output. After the exact preflight returned `ALLOW`, a fresh sealed
read-only Agent 2 executed the matrix and returned `PASS`. The full attempt
history, briefs, status files, exact route citations, checks, hashes, and
telemetry are under:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/instances/WI-PKG08-POST-ROOT-INTEGRATION-01/`

Fresh independent review is required before manager fan-in and is recorded in
that instance directory.

## TM125 notice acknowledgment

Disposition: `INCORPORATED`.

The App-loop owner direction adopted the Root notice for this iteration. This
deliverable run record, `_STATUS.md` history, and `MEMORY.md` acknowledge it
through App-owned instruments. The requested reciprocal validation is complete;
the notice did not authorize or require an App-to-Root write, duplicate App
implementation, lifecycle advance, or broader acceptance claim.

## Closure and derivative disposition

- Only the satisfied post-Root Remaining item was removed. The D-APP-103
  decision-packet item remains and is now DEL-08-04's sole Remaining item.
- No Root file, App product/test source, dependency register, decision register,
  shared receipt, completion log, lifecycle field, or Checking Approval SHA was
  changed by this node.
- This run record and the manager/child instance tree are derivative validation
  evidence over accepted Root/App inputs; they do not replace Root instruction
  truth, App product truth, Receipt 172, or deliverable lifecycle truth.
- Blockers: none.
- Reruns: none on this unchanged basis. Rerun the same matrix if the Root
  validator/instructions or either affected App harness source/test changes.
- No release, reliance, issuance, signing, notarization, distribution,
  publication, provider expansion, Git closeout, or merge claim follows.

