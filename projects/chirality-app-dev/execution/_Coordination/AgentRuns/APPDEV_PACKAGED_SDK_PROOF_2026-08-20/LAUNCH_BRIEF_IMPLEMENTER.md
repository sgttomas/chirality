# Sealed Agent 2 brief — DEL-09-04 packaged SDK CI proof

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SDK_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-DEL0904-PACKAGED-SDK-01`
- ChildInstanceID: `A2-DEL0904-PACKAGED-SDK-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-04`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: close the bounded D-APP-97 packaged-SDK/R4-P49 engineering gap by invoking the existing `verify-packaged-agent-sdk-runtime.mjs` in `.github/workflows/desktop-release-template.yml` against both (1) the staged packaged app and (2) the read-only mounted unsigned DMG app, preserving its scripted no-live-provider proof and stable parseable JSON evidence, and uploading both evidence outputs with the unsigned CI artifact.
- AcceptedBasis: branch `codex/app-packaged-sdk-proof-20260820` at `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`; D-APP-97 C1; DEL-09-04 live kit/status/dependencies; committed HEAD standing loop plan; frozen activation/work graph; APP-HOLD dispatch preflight `ALLOW`.
- Dependencies: existing unsigned Desktop workflow, `desktop:dist`, packaged Agent SDK verifier, packaged dependency boundary and instruction-root proof. Preserve all pins, manifests, provider/network policy, and stable verifier semantics.
- DeclaredReads: root/project agent and TASK instructions; committed standing loop plan; D-APP-97; DEL-09-04 live SOW/status/memory/dependencies; software workflow profile and validation/build/release gates; `skills/software-bounded-implementation/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; current workflow; verifier, package scripts/config, and relevant tests; G4 validator/schema/manifests when required.
- AllowedTools: repository read/search; `apply_patch`; existing repository/package tests, typecheck/build, YAML/Bash static validation, and registered software-workflow commands; no installs, network/provider proof expansion, release actions, credentials, or destructive commands.
- AllowedWriteTargets: `.github/workflows/desktop-release-template.yml`; `docs/governance_harness/tranche_manifests/APP-DEL0904-PACKAGED-SDK-CI-20260820.yaml` only if required by the committed candidate-range validator; `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`; closely related focused tests only when necessary; `projects/chirality-app-dev/frontend/scripts/verify-packaged-agent-sdk-runtime.mjs` only if a real verifier defect blocks integration; DEL-09-04 `MEMORY.md`, `_STATUS.md`, and `_run_records/**`; this run root's `IMPLEMENTER_RETURN.md` and `STATUS_IMPLEMENTER.json`.
- ExpectedOutputs: meaningful workflow integration; focused regression coverage; stable separate staged/mounted packaged-SDK summaries; unsigned artifact upload coverage; truthful pre-CI DEL-09-04 state/evidence that keeps the R4-P49 Remaining scope open; exact check/containment/PR-CI-owed return.
- AcceptanceCriteria:
  1. Workflow runs the existing verifier once against `dist/mac-arm64/Chirality.app/Contents/Resources` and once against the mounted `Chirality.app/Contents/Resources` while the DMG remains read-only mounted.
  2. Each invocation writes a stable parseable `summary.json` at a distinct retained path, and workflow validation fails unless each summary reports `status: pass` and `proofMode: scripted-no-live-provider`.
  3. Both summary paths are uploaded with the existing unsigned CI artifact/evidence; no live provider, real credential, secret, signing/notarization, release, or publication path is introduced.
  4. The mounted proof cannot silently use the staged app path; tests assert both resource roots/output roots and mounted-before-cleanup ordering.
  5. Existing unsigned artifact identity, dependency boundary, instruction-root, architecture, minimum-version, signing/notarization-posture, and upload checks remain intact.
  6. Focused tests, YAML parse, all run-block Bash syntax, typecheck, full Vitest if feasible, proportional build decision, candidate-range governance validation, self-check, practitioner pytest, corpus status, APP-HOLD integrity, unchanged receipt validation, diff hygiene, and containment are returned precisely.
  7. DEL-09-04 remains `IN_PROGRESS`; do not remove the open packaged-SDK/R4-P49 Remaining item before external PR-CI proof passes.
- EXCLUSIONS: no signing, notarization, distribution/publication, release-readiness/professional claim, provider/network expansion, credential access, dependency/lockfile/package pin change, lifecycle or Checking Approval SHA change, owner-machine LaunchAgent deployment, runtime/root/foreign-loop source change, receipt/completion-log write, commit, push, PR, merge, or additional engineering node.
- Escalation: stop and return a precise blocker before any excluded need or scope/acceptance expansion. Discovered out-of-node work is reported, not implemented.
- ExpectedReturn: concise product-first result; exact paths; commands/results; write containment; external PR-CI proving surface and rerun; derivative state; residual risks; CHANGE-readiness recommendation without acceptance/release claim.
