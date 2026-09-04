# App v3 Node M / A15 — Independent Review Round 2

- Review date: 2026-09-04
- Reviewer: fresh, read-only ephemeral Agent 2 generalist; no implementation participation and no delegation
- Method: repository-native `software-code-review` guidance applied to the complete frozen diff
- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)
- Frozen candidate: `4fa170341700e491dff8c72ce1229ba84735f073`
- Candidate commits: `c4decf4023a1f8652f90002ab3016088d7a3c668`, evidence correction `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`, then remediation `4fa170341700e491dff8c72ce1229ba84735f073`
- Worktree: `/private/tmp/chirality-app-v3-a15-20260904/nodeM-review-r2` (detached and retained until tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 2 MAJOR, 0 MINOR, 0 NOTE

## Reviewed scope

I reviewed 100% of `git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..4fa170341700e491dff8c72ce1229ba84735f073`: 13 paths, 736 insertions, 9 deletions. The live range contains three commits; this complete range, rather than the dispatch's stale two-commit shorthand, governs.

1. `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`
2. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/_STATUS.md`
3. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md`
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/CHECKS.json`
5. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/HANDOFF_STATE.md`
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/MANIFEST.sha256`
7. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/RETURN.md`
8. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/REVIEW_DISPOSITIONS.md`
9. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/REVIEW_R2_HANDOFF.md`
10. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/STEP0_DISCOVERY.md`
11. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M1/LAUNCH_BRIEF.md`
12. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M2_REVIEWER/REVIEW_NODE_M_R1.md`
13. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`

The exact change-scope validator passed. There is no unstated path mutation.

## Round-1 disposition verification

| Finding | Round-2 result | Evidence |
|---|---|---|
| M-R1-F1 | PASS | A15 contains no `[click]` token. It accurately states that the owner typed plain-text mobile-fallback replies, and preserves all three sealed questions plus the exact answer `Yes, so authorized.` for each. No ruling substance changed. |
| M-R1-F2 | PASS | DEL-09-05-V3-02 is now `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable. A15 authorization is prospective, A14 remains valid dated history, the owner re-pin alternative remains explicit, unrelated items are unchanged, and host observation still finds no Syft executable. |
| M-R1-F3 | PASS for the exact round-1 disposition | The filed R1 report is byte-identical to the external immutable report and has SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. `CHECKS.json`, `RETURN.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, Receipt 220, `REVIEW_DISPOSITIONS.md`, and `REVIEW_R2_HANDOFF.md` consistently record R1 FAIL, accepted remediation, and R2 pending. Receipt identity, parent, and cursor are unchanged. The broader missing multi-agent record contract is a new finding below. |

## Findings

### M-R2-F1 — MAJOR — V3-04's return and removal contract still permits the hash result A15 did not select

Path and lines: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md:16,22-23`.

Evidence: the item's gate annotation correctly says A15 selected a per-response nonce with dynamic rendering and that hash/SRI was not selected. A15 repeats that bounded outcome. But the same live item still says its return may use `(nonce or hash)` and that it is removed when `the nonce (or hash) pipeline` lands.

Impact: the deliverable-local discovery and acceptance surface is internally contradictory. A future implementer or reviewer could close the item with the hash alternative even though the owner selected nonce/dynamic rendering. This undermines the exact ruling the tranche exists to record.

Remedy: make the V3-04 Return and Removed-when lines nonce-only while preserving implementation latitude inside the selected nonce outcome. Do not prescribe middleware versus packaged-handler header attachment or any other exact code form. Update the History/run-record/manifest/receipt only as needed to reflect the corrected candidate, file this review immutably, and submit the complete new freeze to a fresh reviewer.

### M-R2-F2 — MAJOR — The dispatched multi-agent tranche lacks the mandatory work graph and per-child records

Paths and lines: `projects/chirality-app-dev/AGENTS.md:64-68,93-99`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/` (complete directory inventory).

Evidence: project instructions require a recorded work graph for every multi-agent tranche and, whenever children are dispatched, require an activation/plan, work graph, one sealed launch brief per child, each child's return and status, manager return, and handoff state. Node M dispatched an M1 implementer and independent reviewers. The candidate has no `ORCHESTRATION_PLAN.md` or `WORK_GRAPH.json`; M1 has only `instances/M1/LAUNCH_BRIEF.md` and no instance status/return; M2 has only the filed R1 report and no sealed launch/status/return; the generic `REVIEW_R2_HANDOFF.md` is not the actual per-child sealed launch/status/return record for this reviewer. The neighbouring established node-J record demonstrates the same required shape.

Impact: the durable record cannot reconstruct selection authority, execution edges, child boundaries, or complete child returns for the actual multi-agent work. This violates the App record contract and prevents validated manager fan-in even though the substantive ruling and deterministic checks are otherwise sound.

Remedy: add truthful, non-retroactive-fiction control-plane records for the actual tranche: the orchestration plan and work graph, the exact sealed launch brief and status/return for each dispatched child, and any versioned remediation/update records needed to preserve the review sequence. File this R2 report verbatim with its disposition, update `CHECKS.json`, `RETURN.md`, `HANDOFF_STATE.md`, Receipt 220 pointers/check posture, and `MANIFEST.sha256`, then dispatch a fresh reviewer over the complete new freeze. Do not claim facts or exact prompts that cannot be recovered from the runtime record; escalate any unavailable sealed input rather than reconstructing it inaccurately.

## Semantics verified as correct

- The typed mobile-fallback provenance is accurate, all three questions match the sealed owner-source brief, and all three answers are exactly `Yes, so authorized.`
- A15 authorizes but does not perform the Syft install, disposable identity creation, or credential-transition drill. Host observation found Syft absent and zero valid code-signing identities.
- A14 remains truthful dated history. Its two host-act deferrals are lifted prospectively only; A15 does not purport to invalidate or rewrite A14.
- DEL-09-05-V3-02 is parked until owner-installed Syft `v1.18.1` is observable. DEL-09-05-V3-04 is parked until the owner-created disposable identity exists.
- DEL-09-06-V3-04 alone among the three affected owner-gated items becomes selectable when A15 lands. It selects per-response nonce plus dynamic rendering for `/`, `/chat`, `/pipeline`, and `/workbench`, while leaving exact nonce attachment code shape open.
- The complete DEL-09-06-V3-03 item section is byte-identical to the basis; it was neither retagged nor split.
- Current State and Checking Approval SHA fields are unchanged in both deliverables. No frontend, product, host, Root, register, decomposition, lifecycle, or SCOPE_CHANGE byte changed.
- F-APP-2 remains explicit: no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, production-identity, or other release act or claim.
- Receipt 220 physically follows Receipt 219, names Parent-Receipt 219, uses the closed Gate-Outcome vocabulary, and contains no forbidden count-like measurement in its Checks field.

## Independent check results

| Check | Result | Evidence |
|---|---|---|
| Basis and ancestry | PASS | Basis `719fe5e34...` is an ancestor of freeze `4fa170341...`. |
| Candidate commit inventory | PASS | Complete three-commit range reviewed: initial record, evidence correction, and R1 remediation. |
| Changed-path inventory | PASS | Exactly the 13 paths listed above; no unstated mutation. |
| Software-workflow affected checks | PASS | From the App root, selection returned `harness-self-check`, `app-hold-integrity`, and `harness-pytest`; no frontend gate selected. |
| Receipt validator | PASS | Versioned ledger valid through Receipt 220. |
| Receipt 220 parent/vocabulary/measurements | PASS | Parent is Receipt 219; Gate-Outcome is `EXECUTED`; Checks is pass/fail-only. |
| Authority-corpus status | PASS | v20; every authority reference matches; no drift. |
| APP-HOLD integrity | PASS | Register matches scan; verdict PASS. |
| APP-HOLD reliance | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| APP-HOLD dispatch | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| Harness self-check | PASS | Exit 0 using the repository Python 3.13 runtime. |
| Harness pytest | PASS | Full practitioner-harness suite passed using the repository Python 3.13 runtime. |
| Exact change-scope | PASS | No violation against the declared write set. |
| Manifest hashes | PASS | All 12 recorded file identities verify. |
| Manifest membership | PASS | Manifest covers every changed path except itself, with no extra member. |
| R1 report byte identity | PASS | Filed and external reports are byte-identical at SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. |
| Strict JSON | PASS | `CHECKS.json` parses. |
| `git diff --check` | PASS | No whitespace errors. |
| F-APP-2 wording scan | PASS | Release-related additions are owner questions or explicit no-act/no-claim fences; no prohibited positive claim. |
| Forbidden-path scan | PASS | No frontend, authority-corpus, decision-register, decomposition, Root, domain-engine, piping, PEC, or other forbidden path changed. |
| DEL-09-06-V3-03 byte fence | PASS | Basis and freeze section SHA-256 both equal `4cb9efad20d87b1f7ac6b395b701d34da3f40feb5ae559e2fc51ed8ea0828676`. |
| Current State / Checking Approval SHA fence | PASS | Neither field changed in either status file. |
| A14 identity | PASS | SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact cited match. |
| Pinned completion-reference identity | PASS | SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact cited match. |
| Packaged route inventory | PASS | Exactly the four cited `page.tsx` routes are present. |
| Syft observation | PASS | `command -v syft` found no executable and `syft version` was unavailable; no installation or network act attempted. |
| Disposable identity observation | PASS | `security find-identity -v -p codesigning` reported zero valid identities; no key material read or modified. |
| R1 disposition verification | PASS | All three R1 findings are accepted and substantively remediated as shown above. |
| V3-04 selected-outcome coherence | FAIL | Return and removal clauses still permit hash despite A15's nonce selection; M-R2-F1. |
| Multi-agent record contract | FAIL | Required plan/work graph and per-child launch/status/return records are incomplete; M-R2-F2. |
| Detached worktree status | PASS | Clean detached HEAD after all checks. |
| Frontend typecheck/Vitest/build/premerge/render bar | SKIPPED | No `frontend/` path changed and the affected-check selector chose no frontend check; no pass inferred. |
| Signing/notarization/publication/release execution | SKIPPED | Prohibited and outside this record-only tranche under F-APP-2; no pass or readiness inference. |

## Verdict

**FAIL.** All three round-1 findings are remediated, the owner transcription and host-act boundaries are truthful, the deterministic gates pass, and no product or host mutation occurred. The candidate is not valid for manager fan-in because its live V3-04 acceptance text still permits the owner-rejected hash outcome and its actual multi-agent execution is not represented by the mandatory work graph and per-child records. File this report immutably, remediate both findings, and use a fresh reviewer over the next complete freeze.
