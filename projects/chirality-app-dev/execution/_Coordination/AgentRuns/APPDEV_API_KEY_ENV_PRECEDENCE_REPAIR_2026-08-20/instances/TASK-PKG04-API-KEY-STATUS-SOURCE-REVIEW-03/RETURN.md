# Return — TASK-PKG04-API-KEY-STATUS-SOURCE-REVIEW-03

RUN_STATUS: SUCCESS

Verdict: **PASS** — zero actionable findings. The frozen v3 amended N1
identity is valid for manager fan-in within this sealed review scope.

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/validate_change_scope.py:*`,
`python3 tools/software_workflow/select_affected_checks.py:*`; repository reads.
Structured comparison and generated-manifest checks were not relevant.

RuntimeOverrides: none

WriteAuthorization: managed instance `STATUS.json` and `RETURN.md` only

## Findings

No blocking or non-blocking actionable findings.

## Identity and coverage

- Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`.
- Frozen manifest: PASS. All 12 of 12 SHA-256 values in
  `FROZEN_DIFF_MANIFEST_V3.md` were independently recomputed and matched.
- Scope validation: PASS, zero violations for the exact two declared
  product/test paths.
- Diff coverage: 100% of the exact two-file basis diff inspected: 143
  insertions and 19 deletions.
- File coverage: 100% of `frontend/electron/api-key-storage.ts` (223 lines)
  and `frontend/src/__tests__/electron/api-key-storage.test.ts` (339 lines).
- Diff hygiene: PASS; the exact two-file basis diff has no whitespace errors.
- No dependency, lockfile, migration, generated-artifact, provider, storage
  path, lifecycle, package-state, or release-surface change appears in the
  frozen product diff.

## Implementation and contract assessment

`frontend/electron/api-key-storage.ts:164-196` uses one provider-isolated
resolver for `get` and `status`. It preserves the accepted resolution order:

- a non-whitespace persisted safeStorage credential wins and reports `ui`;
- Anthropic then resolves trimmed `ANTHROPIC_API_KEY` before trimmed
  `CHIRALITY_ANTHROPIC_API_KEY` and reports `env`;
- oMLX consults only its persisted blob and `CHIRALITY_OMLX_API_KEY`;
- absent and unsupported providers report unconfigured/`none`.

`status` projects only `{ configured, source }`; credential values remain
internal to the resolver and do not cross the status API. `get`, `set`,
`remove`, storage filenames, compatibility globals, corruption handling, and
unsupported-provider mutation errors remain unchanged apart from the already
accepted Anthropic environment-order correction.

The focused test file directly covers persisted UI precedence with simultaneous
environment values, canonical-only and compatibility-only environment keys,
both environment variables, whitespace fallthrough, oMLX UI/environment/none
isolation, unsupported providers, and the retained storage/get/set/remove
behavior.

## Daemon serialization and N2 consumer trace

- `runtime/packages/daemon/src/runtime-daemon.ts:272-279` spreads the store's
  status object into the authenticated credential-status response.
- `runtime/packages/daemon/src/runtime-daemon.ts:515-522` serializes the full
  enumerable response with `JSON.stringify`; it does not filter `source`.
- `runtime/packages/client/src/client.ts:116-135` returns parsed JSON without
  removing extra response properties.
- The root static `CredentialStatusResponse` / `ProviderCredentialPort` types
  still name only `configured`, but this does not erase the runtime `source`
  property. N2 can widen its local consumer shape with an optional validated
  `ui | env | none` discriminator without a root-runtime-contract edit.
- Current `frontend/electron/api-key-ipc.ts:71-86` still re-infers source from
  the Electron environment. That is the known, serialized N2 defect and is
  properly held outside N1; the v2 graph and amendment give N2 sufficient
  non-secret input to remove it.

## Verification completeness

Deterministic affected-check selection requires `frontend-test`,
`frontend-typecheck`, `harness-self-check`, and `app-hold-integrity`. Frozen
evidence records PASS for all four, and additionally records PASS for the
focused 20-test file, full frontend suite (150 passed files, 1 skipped; 1,167
passed tests, 4 skipped), frontend build, 350-test practitioner harness,
APP-HOLD reliance, explicit scope, secret scan, and whitespace checks.

The secret scan reports PASS across 5,833 scanned files with zero blocked
findings and 21 allowed fixtures. The APP-HOLD evidence reports register match,
zero held deliverables, and ALLOW for all four run targets. The self-check's
existing unrelated 4 REVIEW / 31 WARN baseline is disclosed and does not
intersect this N1 scope.

## Risk and fan-in

- Blocking findings: 0.
- Non-blocking findings: 0.
- Residual risk: low. This review consumed hash-bound recorded verification
  evidence rather than rerunning the product suite. The root credential status
  type does not yet advertise `source`, so N2 must validate the runtime field in
  its local consumer contract as its amendment already requires.
- Fan-in validity: **VALID** for the N1 manager to consume this return with the
  frozen v3 package. This is not lifecycle acceptance, release readiness, or
  broader DEL-04-05 closure.

## Exact N2 handoff

After N1 manager acceptance, release N2 with this contract: daemon
`credentialStatus` responses carry non-secret `source: 'ui' | 'env' | 'none'`;
N2 must consume and validate that store-owned field, delete environment-based
source re-inference, preserve structured daemon-unavailable behavior and
store/remove contracts, and prove simultaneous persisted UI plus environment
reports `ui` without exposing credential material.

## Rerun requirements

- None while all 12 frozen v3 subjects remain byte-identical.
- Any product/test or frozen evidence change requires a new manifest,
  appropriate affected checks, and another fresh independent review.

## Tools Used

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`

ToolPolicyCompliance: PASS

Outputs:

- This managed `STATUS.json`.
- This managed `RETURN.md`.

MISSING: none

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES:

- N2 remains intentionally serialized behind accepted amended N1 fan-in.
