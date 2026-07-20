# G0-DAPP50-IMPLEMENTATION-COMMIT — CHANGE Brief

## Identity

- **Role:** CHANGE (Agent 1)
- **Parent:** HELP_HUMAN; released by ORCHESTRATOR fan-in v2
- **Branch:** `codex/app-dev-dapp50-headless-live-20260720`
- **Required HEAD:** `bc35e3b0049d990f494dd3610603be285c7aa9ed`
- **Objective:** create one reachable implementation-content commit so W2 can
  truthfully repin D-APP-48.

Read full `AGENTS.md`, `agents/AGENT_CHANGE.md`, this brief, `updates/v2.md`,
and W1 terminal records. Reproduce exact branch/HEAD, zero staged paths, all 14
hashes, and absence of any other tracked/non-ignored content change before
acting. Any mismatch returns `BLOCK` without cleanup or repair.

## Exact commit population

Stage and commit exactly these 14 paths at these SHA-256 values:

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/docs/harness/adding_a_tool.md` | `0aac93acfcefdfdfcb510960ec023654ef463fb3f84f6f3325173fc2ebf6c0f5` |
| `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` | `1de58e89704877ed1e19cdd4c60c76899385248c33c85b9c3f8efddb0a91a613` |
| `projects/chirality-app-dev/frontend/docs/harness/tool_catalog.md` | `58d857a9f4a6ea7d41b45bc4584332bbb11e73b39daae970745def65a3a60d07` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-catalog.ts` | `27504b2a5a487116a6c7a886d56efdc5f3cf4426779f2a3dca665e184977f83e` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts` | `a121391ec71851e7280db4ebf2731b53db6829cb42d1bf07604cb8a4f76dc6d4` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-profile-registry.test.ts` | `05d3ade7b76e42149621a238e1b226ab41732c3bd348e219ecf5790ff5b9555b` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts` | `6720fc7969adaffc6f7633c9e939f7e7cf3fc8a91f4494b2263b0636994da509` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-descriptor.test.ts` | `7c9a2fb613ed86b65ce09ad311df69bd8a412795010a4a56cd33399b2d515429` |
| `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-profile-registry.ts` | `dc465717becc687fb0a0992c82e5af3fbfac1e7fd87df2ea0d12e50fb53cd30b` |
| `projects/chirality-app-dev/frontend/src/lib/harness/mcp/read-tools.ts` | `99ab4b761026498687b8efd1d93d738755adfd2e71ee53096f7a6c2e7042f4d5` |
| `projects/chirality-app-dev/frontend/src/lib/harness/tool-evidence.ts` | `a06d58f72bf4af5346cdb6c13fe40694c97140f9290ba1e91e583d2c1bebda84` |
| `projects/chirality-app-dev/frontend/src/lib/harness/tool-path-policy.ts` | `222fa95ade200b37887f80300841b2661ca0cfdc81666a51e037bbf45f03ac8e` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` | `12ea34a53611bb0a5a2c5010d1d7f0525960c783753e7f4b162b2b2c6116ba94` |
| `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` | `eac51da403aa5f91c1bf9fcf0ab5c62efcc46a7e1b526ca097213fdf617dfc57` |

Run `git diff --check` and cached diff/path/hash checks. Use commit message:
`feat(app-dev): activate headless preview runner transport`.

## Prohibitions and return

Do not stage or commit the AgentRuns control root, D-APP-48 contract,
DEL-10-01 state/run records, loop receipt, generated/ignored artifacts, or any
other path. Do not push, open a PR, merge, repin, edit content, append a
receipt, clean, reset, stash, amend, or delete anything.

After the commit, verify its single parent is the required base and its tree
delta contains exactly the 14 paths. Write terminal `RETURN.md`, `HANDOFF.md`,
and `STATUS.json` in this instance subtree without staging them. Return
`ACCEPT` with the full commit SHA, parent, exact commit path population, and
remaining untracked control state, or `BLOCK` with the mismatch. W2 remains
held.
