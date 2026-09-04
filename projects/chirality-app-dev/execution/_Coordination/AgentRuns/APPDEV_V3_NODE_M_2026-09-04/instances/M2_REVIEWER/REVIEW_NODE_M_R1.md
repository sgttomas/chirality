# App v3 Node M / A15 — Independent Review Round 1

- Review date: 2026-09-04
- Reviewer: fresh, read-only ephemeral Agent 2 generalist; no implementation participation and no delegation
- Method: repository-native `software-code-review` guidance applied to the complete frozen diff
- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)
- Frozen candidate: `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`
- Candidate commits: `c4decf4023a1f8652f90002ab3016088d7a3c668`, then evidence correction `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`
- Worktree: `/private/tmp/chirality-app-v3-a15-20260904/nodeM-review-r1` (detached and retained until tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 3 MAJOR, 0 MINOR, 0 NOTE

## Reviewed scope

I reviewed 100% of `git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`: 10 paths, 499 insertions, 8 deletions.

1. `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`
2. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/_STATUS.md`
3. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md`
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/CHECKS.json`
5. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/HANDOFF_STATE.md`
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/MANIFEST.sha256`
7. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/RETURN.md`
8. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/STEP0_DISCOVERY.md`
9. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M1/LAUNCH_BRIEF.md`
10. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`

The exact change-scope validator passed. There is no unstated path mutation.

## Findings

### M-R1-F1 — MAJOR — A15 falsely records plain-text mobile replies as clicks

Path and lines: `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md:5-6,29-50`.

Evidence: the owner-source provenance supplied to this independent review states that all three replies were typed as plain-text mobile fallbacks, each exactly `Yes, so authorized.` They were not clicks on a desktop response control. The A15 record instead states that `"[click]" marks each answer selected by the owner` and prefixes all three answers with `[click]`.

Impact: the questions and answer text are substantively faithful, but the interaction provenance is false. Truthful owner attribution is the standing plan's firm K-AUTH-1 limit and a hard review criterion for a ruling transcription. A durable ruling record must not invent the mechanism by which the owner acted.

Remedy: remove the `[click]` explanation and all three `[click]` markers. State accurately that the owner typed each reply in plain text from the mobile fallback, while preserving each question and the exact answer `Yes, so authorized.` Do not alter the ruling substance.

### M-R1-F2 — MAJOR — The SBOM item is labeled `SELECTABLE` despite its unmet Syft prerequisite

Path and lines: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/_STATUS.md:11,15-16`.

Evidence: line 11 retains the explicit `SELECTABLE` tag for `DEL-09-05-V3-02`, while lines 15–16 say the item remains operationally blocked until Syft `v1.18.1` is installed and observable. The A15 record itself says the host install is only prospectively authorized and was not performed. Independent host observation found no `syft` executable. The standing plan requires an owner-act-gated item to remain parked until the act is observable on `main`/the host.

Impact: the deliverable-local discovery surface gives contradictory dispatch instructions. A later loop can select a task that cannot lawfully satisfy its registered checks because the owner-host prerequisite remains absent. A15 authorizes the host act; it does not complete it.

Remedy: change the V3-02 gate annotation to `NOT_SELECTABLE_UNTIL` the owner-installed Syft `v1.18.1` is observable, while preserving the prospective authorization and the alternative owner re-pin language. Make the History/run-record/receipt wording agree with that parked state.

### M-R1-F3 — MAJOR — The independent review cannot remain `not_run` or outside the durable AgentRuns record

Paths and lines:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/CHECKS.json:114-126`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/HANDOFF_STATE.md:29-33`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/MANIFEST.sha256:1-9`

Evidence: `CHECKS.json` records an independent review as `not_run` and says HELP_HUMAN reviews the frozen record directly. HELP_HUMAN has now explicitly dispatched this fresh independent Agent 2 review. The established App per-node process requires every review report to be filed verbatim under the node's durable run record, with the manifest and closeout surfaces updated. The current manifest is complete for the pre-review freeze, but by definition does not cover this report.

Impact: if these bytes survive closeout, the durable record will contradict the actual review path, omit the findings that caused remediation, and leave the reviewer evidence outside the auditable snapshot. `overall: pass` would also be false for this round.

Remedy: file this report verbatim under a reviewer instance directory in `APPDEV_V3_NODE_M_2026-09-04/`; update `CHECKS.json`, `RETURN.md`, `HANDOFF_STATE.md`, and `MANIFEST.sha256` to record round-1 FAIL and its disposition. After remediation, dispatch a fresh round-2 reviewer over the new complete freeze, file that report verbatim, and record PASS only if it has zero BLOCKER/MAJOR findings. Update the receipt's check summary at final closeout so it does not imply an unreviewed direct path.

## Semantics that were correct

- All three owner questions and the owner answer text `Yes, so authorized.` are otherwise exact.
- A15 preserves A14 as truthful dated history and lifts the two host-act deferrals prospectively only.
- No text claims that Syft installation, identity creation, or the drill already occurred. Independent observation found Syft absent and zero valid code-signing identities.
- `DEL-09-06-V3-04` becomes selectable only when A15 lands. It selects a per-response nonce with dynamic rendering for the four actual packaged routes (`/`, `/chat`, `/pipeline`, `/workbench`), chooses no hash/SRI outcome, and prescribes no exact implementation form.
- `DEL-09-05-V3-04` remains parked until the owner-created disposable identity exists. The exact phrase `disposable self-signed A→B credential-transition drill` is used consistently in the applied meaning and affected status/handoff surfaces.
- The complete `DEL-09-06-V3-03` item section is byte-identical to the basis; it was neither retagged nor split.
- Current State and Checking Approval SHA fields are unchanged in both deliverables. No frontend/product/host/Root/register/decomposition/lifecycle byte changed.
- F-APP-2 remains explicit: no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, or production-identity act or claim.
- SCOPE_CHANGE is excluded from this A15 tranche.
- Receipt 220 physically follows and names Parent-Receipt 219; its closed-vocabulary Gate-Outcome and measurement posture validate.

## Independent check results

| Check | Result | Evidence |
|---|---|---|
| Basis and ancestry | PASS | Basis is PR #693 merge `719fe5e34...`; it is an ancestor of freeze `f8522fcfc...`. The complete two-commit range was reviewed. |
| Changed-path inventory | PASS | Exactly the 10 paths listed above; no unstated mutation. |
| Software-workflow affected-check selection | PASS | Selected `harness-self-check`, `app-hold-integrity`, and `harness-pytest`; no frontend gate selected. |
| Receipt validator | PASS | Versioned ledger valid through Receipt 220. |
| Receipt 220 parent/vocabulary/measurements | PASS | Parent is Receipt 219; Gate-Outcome is `EXECUTED`; no forbidden count-like measurement appears in the receipt. |
| Authority-corpus status | PASS | v20; every authority reference matches; no drift. |
| APP-HOLD integrity | PASS | Register matches scan; no held deliverables. |
| APP-HOLD reliance, both targets | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| APP-HOLD dispatch, both targets | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| Harness self-check | PASS | Exit 0 at the unchanged repository baseline. |
| Harness pytest | PASS | 350 passed using the repository Python 3.13 runtime. |
| Exact change-scope | PASS | Validator reports no violations for the declared write set. |
| Manifest hashes | PASS | All nine manifest entries verify. |
| Manifest membership at frozen pre-review head | PASS | The manifest covers every changed path except itself, with no extra member. It must be regenerated after the required review filing/remediation. |
| `git diff --check` | PASS | No whitespace errors. |
| Strict JSON | PASS | `CHECKS.json` parses. |
| Forbidden-path scan | PASS | No frontend, runtime, workflow, authority corpus, decision-register, decomposition, dependency, memory, Scope of Work, or other forbidden path changed. |
| F-APP-2 wording scan | PASS | All signing/notarization/publication/distribution/release-readiness hits are questions or explicit no-act/no-claim fences. |
| DEL-09-06-V3-03 byte fence | PASS | Complete item section unchanged from the basis. |
| Current State / Checking Approval SHA byte fence | PASS | No diff to either field in either status file. |
| A14 identity | PASS | SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact cited match. |
| Pinned completion-reference identity | PASS | SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact cited match. |
| Packaged route inventory | PASS | Exactly the four cited `page.tsx` routes are present. |
| Syft observation | PASS | `command -v syft` found no executable; no installation or network act was attempted. |
| Disposable identity observation | PASS | `security find-identity -v -p codesigning` reported zero valid identities; no key material was read or modified. |
| Detached worktree status | PASS | Clean detached HEAD after all checks. |
| Frontend typecheck/Vitest/build/premerge/render bar | SKIPPED | No `frontend/` path changed and the affected-check selector did not select frontend checks. No pass inferred. |
| Signing/notarization/publication/release execution | SKIPPED | Prohibited and outside this record-only tranche under F-APP-2. No pass or readiness inference. |

## Verdict

**FAIL.** The substantive owner answers, prospective host-act boundaries, A14 preservation, CSP decision, F-APP-2 fences, receipt structure, and deterministic checks are sound. The candidate is not acceptable for manager fan-in because it invents click provenance, leaves a still-blocked SBOM item explicitly tagged `SELECTABLE`, and would omit the now-performed independent review from the durable AgentRuns record. Remediate all three findings and submit a new complete freeze to a fresh reviewer.
