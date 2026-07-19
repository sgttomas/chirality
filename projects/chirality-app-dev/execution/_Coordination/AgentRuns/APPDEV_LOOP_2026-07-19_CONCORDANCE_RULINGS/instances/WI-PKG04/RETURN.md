# WI-PKG04 Terminal Return

- **Outcome:** ACCEPT
- **Role:** WORKING_ITEMS (Agent 1)
- **Package:** PKG-04 only
- **Deliverable:** DEL-04-01
- **Basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`
- **Authority:** D-APP-68 recommendation 8
- **Manifest slice:** 7 paths;
  `27cab26e3b84d1971c6ba7541010c9849b4add9493d415b332a5165dc74e0cb0`
- **Blockers:** none

## Accepted Package Candidate

DEL-04-01 now carries the owner-rendered
`ADOPT_WITH_RESIDUAL_RISK` verdict for the repository demonstrator, pinned to
`@anthropic-ai/claude-agent-sdk@0.3.150` and observed Claude Code `2.1.150`.
The new decision records the D-APP-52 live observations and limits, assesses
all twelve D-APP-68/DEL-04-01-REQ-015 residual categories, and defines explicit
custom-runtime/hold fallback triggers.

The decision is demonstrator-scoped. It is not release approval, issuance,
certification, professional acceptance, signing, notarization, publication,
or external distribution. It does not claim Windows, Linux, non-arm64,
signed, notarized, or distributed-package proof.

## Exact Paths

1. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Decision_Version_Pinned_SDK_Adoption_2026-07-19.md`
2. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/ScopeOfWork.md`
3. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Evidence_CODEV-001_SDK_Probe_Record.md`
4. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_CONTEXT.md`
5. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/MEMORY.md`
6. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_STATUS.md`
7. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_run_records/TASK_RUN_2026-07-19_DAPP68_adoption_verdict.md`

## Before/After Disposition

- The adoption verdict and approving act changed from live `TBD`/future-act
  wording to the D-APP-68 owner verdict; D-APP-65's pre-ruling assignment is
  retained as dated history.
- The decision-file path, package/version pins, transcript treatment,
  packaged result, and demonstrator boundary are now explicit in the SOW.
- CODEV-001's historical `BLOCKED_TBD` subprocess-version and interrupt cells
  remain byte-preserved and receive an append-only supersession note pointing
  to D-APP-52 live evidence.
- `_CONTEXT.md` and `MEMORY.md` received append-only current notes.
- `_STATUS.md` received exactly one History line. `Current State:
  IN_PROGRESS`, `Checking Approval SHA`, and the complete `Remaining` section
  are byte-identical to the basis.

## Twelve-Row Coverage

The decision contains exactly one numbered assessment row for each required
area: SDK API drift; settings leakage; allowed-tools misconception;
transcript location; Electron packaging; SDK security boundary; subagent
inherited permissions; session-mirror reliability; product-identity drift;
platform dependency; reliance-boundary ambiguity; and engine-adapter lock-in.

## Validation

- SOW-v1 validator: PASS.
- Exact SDK/Claude Code pins, 12-row census, fallback section, and explicit
  scope fences: PASS.
- Authority/evidence citation existence: PASS.
- Read-only D-APP-52 evidence SHA-256 bindings: PASS.
- Existing-file append constraints for CODEV-001, Context, and Memory: PASS.
- Status state/SHA/Remaining byte preservation and one-History-line rule:
  PASS.
- Seven-path allowlist, exact new paths, and manifest slice SHA: PASS.
- Authority corpus v9: no drift.
- App-dev receipt contract: PASS.
- `git diff --check`: PASS.

## Exclusions and Handoff

No frontend source/test, dependency row, other package, shared register,
receipt, completion log, prior concordance ledger, decomposition truth,
domain-engine surface, or hard fence was changed. No lifecycle transition or
Approval SHA mutation occurred.

Requested parent action: accept this return into package fan-in and release V1
only after all other package returns are independently accepted.
