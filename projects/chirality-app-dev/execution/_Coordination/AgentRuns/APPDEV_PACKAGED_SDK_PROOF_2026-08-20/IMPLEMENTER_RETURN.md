# Implementer return — A2-DEL0904-PACKAGED-SDK-IMPLEMENT-01

- RunID: `APPDEV_PACKAGED_SDK_PROOF_2026-08-20`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- TaskSkill: `software-bounded-implementation` v1
- Model attribution: OpenAI Codex agent; exact build not exposed by the runtime
- Status: `IMPLEMENTED_PRE_CI — REVIEW AND REQUIRED PR-CI PROOF REMAIN`

## Product result

The existing unsigned Desktop workflow now runs
`verify-packaged-agent-sdk-runtime.mjs` twice after `desktop:dist`:

1. against `dist/mac-arm64/Chirality.app/Contents/Resources`, writing
   `artifacts/release-verification/packaged-agent-sdk/staged/summary.json`;
2. against `${mount_root}/Chirality.app/Contents/Resources` after
   `hdiutil attach -nobrowse -readonly` and before cleanup/detach, writing
   `artifacts/release-verification/packaged-agent-sdk/mounted/summary.json`.

Each invocation uses the verifier's existing scripted SDK subprocess, no-live-
provider semantics. The workflow fails closed if either summary is absent, is
not parseable JSON, does not report `status: pass`, or does not report
`proofMode: scripted-no-live-provider`. Both outputs sit beneath the existing
`artifacts/release-verification/**` upload path and are also named in the
unsigned artifact summary. Existing dependency-boundary, instruction-root,
architecture, minimum-version, signature, notarization-ticket, DMG integrity,
mounted identity, and no-publication checks are preserved.

## Changed paths

- `.github/workflows/desktop-release-template.yml`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`
- `docs/governance_harness/tranche_manifests/APP-DEL0904-PACKAGED-SDK-CI-20260820.yaml`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/MEMORY.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
- DEL-09-04 `_run_records/TASK_RUN_2026-08-20_0404.md`
- DEL-09-04 `_run_records/TASK_RUN_2026-08-20_0404_CHECKS.json`
- this return and `STATUS_IMPLEMENTER.json`

## Checks and evidence

- Per-child APP-HOLD dispatch preflight: `ALLOW`; DEL-09-04 `NOT_HELD`;
  register SHA-256
  `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`.
- `npm test -- src/__tests__/scripts/desktop-release-workflow.test.ts`:
  `PASS`, 1 file / 5 tests.
- YAML parse plus `bash -n` over every YAML `run:` block: `PASS`, 6 blocks.
- Escalated normalized registered checks:
  `PATH="/Users/ryan/.local/share/mise/installs/python/3.13/bin:$PATH" python3 tools/software_workflow/run_registered_checks.py projects/chirality-app-dev/software-workflow.json --check frontend-typecheck --check frontend-test --check harness-self-check --check app-hold-integrity --check harness-pytest --output projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/TASK_RUN_2026-08-20_0404_CHECKS.json --timeout-seconds 600`
  — `PASS`: typecheck; 148 Vitest files passed / 1 skipped, 1144 tests
  passed / 4 skipped; self-check exit 0; APP-HOLD scan register-match
  `PASS`, 0 held; practitioner pytest 350 passed. Escalation was required for
  loopback/Unix-socket tests blocked by sandbox `EPERM`; the configured Python
  3.13 environment supplied PyYAML 6.0.3 and pytest 9.1.1.
- G4 CI/schema mode with the configured Python 3.13 interpreter: `PASS`, all
  35 manifests schema-valid, including this tranche's newly added manifest.
- App receipt validator: `PASS`, frozen through Receipt-52.
- Authority corpus status: `MATCH` for all six authority documents and both
  pinned agent contracts; no drift.
- `git diff --check`: `PASS`.
- Build/premerge decision: not run locally. This tranche changes workflow
  orchestration and its static contract test, not product/build source; a local
  frontend build or harness premerge cannot prove the Actions runner's staged
  app, read-only DMG mount ordering, or retained upload. The authoritative
  proportional package proof is the required PR workflow below.

## Required external proof and rerun

The actual macOS staged-app and read-only-mounted-DMG executions are
`REQUIRED / PR-CI-OWED` and are not inferred here. Run the PR-triggered
`.github/workflows/desktop-release-template.yml` job `verify-unsigned-macos`
on `macos-15`. Acceptance fan-in must inspect the successful run and uploaded
`chirality-desktop-macos-arm64-unsigned` artifact, confirming both summary
files parse with `status: pass` and
`proofMode: scripted-no-live-provider`, their `bundleRoot` values name the
distinct staged and mounted resources, and the mounted proof completed before
detach.

Candidate-range G4 also requires a committed candidate range. After CHANGE
creates the node commit, run:

`python3 tools/validation/validate_instruction_tranche_manifest.py --base <PR_BASE_SHA> --head HEAD --added-manifests-only`

The added manifest is present and passes corpus schema validation; no
candidate-range pass is inferred from the uncommitted worktree.

## Containment and derivative state

All child writes are within the sealed targets. The verifier itself,
dependencies, package/lock pins, runtime source, provider/network policy,
credentials, foreign loops, lifecycle, Checking Approval SHA, shared receipt,
and completion log are unchanged. No commit, push, PR, merge, signing,
notarization, publication, distribution, release, or owner-machine deployment
was performed.

The workflow, test, G4 manifest, DEL-09-04 pre-CI state, normalized check JSON,
TASK run record, and this return are derivative implementation/evidence state
over accepted D-APP-97 C1 and basis
`d8c47d9fbc459b32c053c844be0fa789fd1ffab2`; they do not replace
authoritative decomposition truth. DEL-09-04 remains `IN_PROGRESS`, and the
packaged-SDK/R4-P49 Remaining item remains open until the external proof is
accepted by the owning fan-in.

## Residual risks and recommendation

- Required fresh read-only review over 100% of the frozen diff remains the
  manager's next gate.
- PR CI is the only proving surface for the actual staged and mounted app
  invocations and upload.
- CHANGE-readiness recommendation: proceed to frozen-diff review; if review is
  clean, CHANGE may commit and open the PR so candidate-range G4 and macOS
  package proof can run. This is not an acceptance or release-readiness claim.

## TASK return shape

- `RUN_STATUS:` `SUCCESS`
- `ControlSurface:` `FILE`
- `TaskProfile:` `NONE`
- `TaskSkill:` `software-bounded-implementation`
- `ScopePath:` DEL-09-04 working folder
- `ResolvedSkillPath:` `skills/software-bounded-implementation`
- `ResolvedSkillVersion:` `1`
- `ResolvedTaskProfileRequirement:` `NONE`
- `CompanionFiles:` `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`
- `AllowedTools:` skill frontmatter allowlist plus brief-authorized repository reads, edits, static checks, tests, and registered checks
- `RuntimeOverrides:` none
- `WriteAuthorization:` `ALLOWED_WRITE_TARGETS`
- `ToolPolicyCompliance:` `PASS`
- `MISSING:` required PR-CI staged/mounted proof; committed candidate-range G4; fresh independent review
- `NEEDS_HUMAN_RULING:` none
- `DEPENDENCY_NOTES:` none
