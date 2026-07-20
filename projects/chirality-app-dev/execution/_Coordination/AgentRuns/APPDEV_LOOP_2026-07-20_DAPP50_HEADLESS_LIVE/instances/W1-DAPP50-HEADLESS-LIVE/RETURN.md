# RETURN — IMPLEMENTED_AWAITING_COMMIT_BOUND_REPIN

**Verdict:** `BLOCK` for final closeout only. The implementation and applicable
validation are complete; this is a staged-closeout blocker, not an
implementation failure.

## Basis and authority

- Role: `WORKING_ITEMS` (W1 serialized integration owner)
- Basis/HEAD: `bc35e3b0049d990f494dd3610603be285c7aa9ed`
- Branch: `codex/app-dev-dapp50-headless-live-20260720`
- Authority applied: D-APP-50 Option A and riders; the only live capability
  flip is `domain_headless_preview_run` for exact profile
  `open_pipe_stress`.
- Git actions: none. Delegation: none. Waivers: none.

## Result

The frontend now provides a configured-local-process adapter for
`openpipestress-runner solve`. It verifies an explicit absolute executable
realpath and configured SHA-256 immediately before direct, shell-free spawn;
uses an exact `solve` argv, a minimal environment, exact validated request
bytes on stdin, bounded stdout/stderr, timeout/termination/reaping, and stable
sanitized failure codes. DEC-065 exit 0/1/2 semantics remain distinct.

The live read-side tool is gated to exact profile `open_pipe_stress`, uses
`runnerInputRef` with existing project-root read containment, and flows through
the normal permission, event, redaction, evidence, result-budget, and artifact
pipeline. `pec`, unknown, missing, and profile-mismatch cases fail closed. The
descriptor remains read-only, project-root-read, input-dependent, exclusive,
and non-confirming. Generated catalog and runtime documentation describe the
configured local transport and its limitations.

## Implementation path accounting

Tracked modifications (12):

- `frontend/docs/harness/adding_a_tool.md`
- `frontend/docs/harness/runtime_engine_contract.md`
- `frontend/docs/harness/tool_catalog.md`
- `frontend/packages/harness-contract/src/tool-catalog.ts`
- `frontend/packages/harness-contract/src/tool-descriptor.ts`
- `frontend/src/__tests__/lib/domain-profile-registry.test.ts`
- `frontend/src/__tests__/lib/sdk-options-builder.test.ts`
- `frontend/src/__tests__/lib/tool-descriptor.test.ts`
- `frontend/src/lib/harness/mcp/domain-profile-registry.ts`
- `frontend/src/lib/harness/mcp/read-tools.ts`
- `frontend/src/lib/harness/tool-evidence.ts`
- `frontend/src/lib/harness/tool-path-policy.ts`

Untracked implementation files (2):

- `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`
- `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`

Staged implementation paths: 0. The untracked control package is parent-owned
except for this instance's `RETURN.md`, `HANDOFF.md`, and `STATUS.json`.

## Validation evidence

Passed:

- Generated tool catalog plus independently reproduced focused Vitest: 23
  tests passed for the exact frozen test-file SHA-256
  `12ea34a53611bb0a5a2c5010d1d7f0525960c783753e7f4b162b2b2c6116ba94`.
- Adjacent contract/runtime suite: 66 tests passed across 6 files.
- Full frontend Vitest: 751 passed, 4 skipped across 98 passed and 1 skipped
  files.
- Frontend TypeScript typecheck.
- Harness contract dependency validation.
- Agent SDK MCP probe: 1/1 passed.
- Production Next/Electron build.
- Owned-server premerge validation: Section 8, 8/8; Section 9, 16/16
  report-only checks.
- Secret scan: 2,499 files, 0 blocked findings, 20 allowed fixtures.
- D-APP-48 pull-contract validator against the existing reachable pin.
- App-loop receipt validator.
- Authority corpus reconciliation status: v9, 8/8 match, no drift.
- Practitioner harness self-check: exit 0 with the pre-existing 3 REVIEW and
  6 WARN findings.
- `tools/validation` pytest: 123 passed.
- `tools/practitioner_harness` pytest: 311 passed.
- Frontend tracked whitespace/diff check, branch/HEAD check, staged-path check,
  and prohibited-scope diff check.

Not applicable to this no-packaging/no-network tranche:

- Instruction-root integrity reported the expected absent package bundle (43
  instruction files and 4 unpacked SDK entries); packaging is prohibited.
- Network-policy proof is not applicable because this change adds no network
  or provider behavior and its evidence target is outside W1 write scope.
- Packaging was not performed.

## Content hashes (SHA-256)

| Path | SHA-256 |
|---|---|
| `frontend/docs/harness/adding_a_tool.md` | `0aac93acfcefdfdfcb510960ec023654ef463fb3f84f6f3325173fc2ebf6c0f5` |
| `frontend/docs/harness/runtime_engine_contract.md` | `1de58e89704877ed1e19cdd4c60c76899385248c33c85b9c3f8efddb0a91a613` |
| `frontend/docs/harness/tool_catalog.md` | `58d857a9f4a6ea7d41b45bc4584332bbb11e73b39daae970745def65a3a60d07` |
| `frontend/packages/harness-contract/src/tool-catalog.ts` | `27504b2a5a487116a6c7a886d56efdc5f3cf4426779f2a3dca665e184977f83e` |
| `frontend/packages/harness-contract/src/tool-descriptor.ts` | `a121391ec71851e7280db4ebf2731b53db6829cb42d1bf07604cb8a4f76dc6d4` |
| `frontend/src/__tests__/lib/domain-profile-registry.test.ts` | `05d3ade7b76e42149621a238e1b226ab41732c3bd348e219ecf5790ff5b9555b` |
| `frontend/src/__tests__/lib/sdk-options-builder.test.ts` | `6720fc7969adaffc6f7633c9e939f7e7cf3fc8a91f4494b2263b0636994da509` |
| `frontend/src/__tests__/lib/tool-descriptor.test.ts` | `7c9a2fb613ed86b65ce09ad311df69bd8a412795010a4a56cd33399b2d515429` |
| `frontend/src/lib/harness/mcp/domain-profile-registry.ts` | `dc465717becc687fb0a0992c82e5af3fbfac1e7fd87df2ea0d12e50fb53cd30b` |
| `frontend/src/lib/harness/mcp/read-tools.ts` | `99ab4b761026498687b8efd1d93d738755adfd2e71ee53096f7a6c2e7042f4d5` |
| `frontend/src/lib/harness/tool-evidence.ts` | `a06d58f72bf4af5346cdb6c13fe40694c97140f9290ba1e91e583d2c1bebda84` |
| `frontend/src/lib/harness/tool-path-policy.ts` | `222fa95ade200b37887f80300841b2661ca0cfdc81666a51e037bbf45f03ac8e` |
| `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` | `12ea34a53611bb0a5a2c5010d1d7f0525960c783753e7f4b162b2b2c6116ba94` |
| `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` | `eac51da403aa5f91c1bf9fcf0ab5c62efcc46a7e1b526ca097213fdf617dfc57` |

## Preserved boundaries

No diff exists under `projects/chirality-piping/**`, `_DomainEngines/**`, or
`projects/pec/**`. No apply/propose/refresh/accept capability, endpoint/public
transport, provider/network expansion, solver-truth claim, or `pec` proposal
behavior was added.

The staged-closeout authority boundaries remain byte-for-byte unchanged:

- D-APP-48 pull contract:
  `565260f4ef63fe9d408b1354be2d220a5a8fad52cda94c1de93e36b997780748`
- DEL-10-01 `_STATUS.md`:
  `6f38cf1167d8a840d74bd0e50417ea4797489e9bc2e9d3c14441e27ae8d591df`
- `loop/LOOP_RECEIPTS.md`:
  `8eabef4042ee83e44403fffead019748109c76c66013c050f45b431bcfb0b520`
- Decision register:
  `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920`

No DEL-10-01 run record or Receipt-83 was created.

## Blocker and next gate

D-APP-48 binds exported contract bytes to a reachable Git commit. W1's Git
authority is prohibited, so the new contract bytes cannot be truthfully
repinned until a commit exists. Recommended next gate:

1. Narrow G0 CHANGE creates the implementation-content commit only.
2. W2 repins/revalidates D-APP-48 against that reachable commit and performs
   the authorized DEL-10-01 status/run-record/Receipt-83 closeout.
3. Independent EVALUATION, then final CHANGE integration.

Unknowns: none beyond the commit-bound value that cannot exist before G0.
