# App v3 Node M / A15 — Independent Review Round 3

- Review date: 2026-09-04
- Reviewer: fresh, read-only ephemeral Agent 2 generalist; no implementation or prior-review participation and no delegation
- Method: repository-native `software-code-review` guidance applied to the complete frozen diff
- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)
- Frozen candidate: `52998709c5c19bc5c3df3944735593299d60be56`
- Candidate commits: `c4decf4023a1f8652f90002ab3016088d7a3c668`, `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`, `4fa170341700e491dff8c72ce1229ba84735f073`, and `52998709c5c19bc5c3df3944735593299d60be56`
- Worktree: `/private/tmp/chirality-app-v3-a15-20260904/nodeM-review-r3` (detached and retained until tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 1 MAJOR, 0 MINOR, 0 NOTE

## Reviewed scope

I reviewed 100% of `git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..52998709c5c19bc5c3df3944735593299d60be56`: 25 paths, 1,312 insertions, 11 deletions, across the complete four-commit range. The exact change-scope validator passed and no unstated path changed.

The scope consists of the A15 ruling record, the bounded DEL-09-05 and DEL-09-06 status edits, Receipt 220, and the Node M AgentRuns package including the two immutable prior-review reports and their dispositions.

## Round-1 and round-2 disposition verification

| Finding | Round-3 result | Evidence |
|---|---|---|
| M-R1-F1 | PASS | A15 and Receipt 220 accurately identify typed plain-text mobile-fallback replies. A15 contains no false `[click]` marker; all three sealed questions and each exact answer `Yes, so authorized.` are preserved without changing ruling substance. |
| M-R1-F2 | PASS | DEL-09-05-V3-02 is `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable. Syft remains absent; A15 is prospective; A14 remains truthful dated history; the re-pin alternative remains explicit. |
| M-R1-F3 | PASS | The filed R1 report is byte-identical to the external immutable source at SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. R1 FAIL and the accepted remediation are represented throughout the run record. |
| M-R2-F1 | PASS | DEL-09-06-V3-04's gate, Depends, Return, and Removed-when clauses are nonce-only, select dynamic rendering for the four routes, reject hash/SRI as the selected result, and leave middleware versus packaged-handler attachment and other exact implementation shape open. DEL-09-06-V3-03 is byte-identical to the basis. |
| M-R2-F2 | FAIL | The orchestration plan, work graph, and M1/M2/M3 launch/status/return files now exist and the reconstructed prompt/return provenance is calibrated. However, the records omit the mandatory delegated-harness-native role and non-delegation evidence calibration described below, so the durable multi-agent record remediation is not complete. The filed R2 report itself is byte-identical to the external immutable source at SHA-256 `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`. |

## Finding

### M-R3-F1 — MAJOR — Native-descendant role and non-delegation claims lack the required evidence calibration

Paths and lines:

- `AGENTS.md:83-106` (governing requirement)
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/ORCHESTRATION_PLAN.md:10-16,53-64`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/WORK_GRAPH.md:7-17,23-27`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M1/STATUS.json:5-10`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M2_REVIEWER/STATUS.json:5-12`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M3_REVIEWER/STATUS.json:5-12`

Evidence: root `AGENTS.md` classifies Codex App Server native descendants as `delegated-harness-native`, states that native descent does not assign an Agent 0/1/2 role, requires explicit Agent-2/TASK mode to be labelled `role not mechanically enforced` with governed-workflow evidence marked `instruction-asserted`, and requires K-SUBAGENT non-delegation for this class to be recorded as instruction+config asserted rather than mechanism-proven. Node M was executed through that native descendant facility. The new orchestration records instead call M1/M2/M3 unqualified Agent 2 instances and state `no delegation` / `delegated_descendants: false`; nowhere in the complete run package do `delegated-harness-native`, `role not mechanically enforced`, `instruction-asserted`, or the instruction+config/non-mechanism calibration appear. The separate M2/M3 reconstruction-versus-verbatim labels are correct but do not satisfy this role/mechanism requirement.

Impact: the durable record conflates an instruction-assigned role and observed no-descendant outcome with mechanism-proven role/non-delegation. That is precisely the evidence overclaim the current delegation doctrine prohibits, and it leaves the round-2 multi-agent record-contract remediation materially incomplete. Manager fan-in would accept a governance record whose attribution strength is stronger than the executable mechanism supports.

Remedy: amend the Node M orchestration plan, work graph, and M1/M2/M3 instance status/return or launch records as appropriate to state the actual class and calibration: `delegated-harness-native`; Agent-2 role not mechanically enforced and governed-workflow role evidence `instruction-asserted`; K-SUBAGENT non-delegation instruction+config asserted, not mechanism-proven; no descendants observed. Keep M1's sealed brief and both immutable reviewer reports byte-unchanged. Update the run summary/check/handoff/manifest and Receipt 220 pointers only as needed, then submit the complete new freeze to a fresh reviewer.

## Semantics verified as correct

- The mobile-fallback provenance and all three owner questions/answers are exact.
- A15 authorizes but does not perform the Syft install, disposable identity creation, or credential-transition drill. Host observation still finds Syft absent and zero valid code-signing identities.
- A14 remains truthful dated history; the two host-act deferrals are lifted prospectively only.
- DEL-09-05-V3-02 remains parked until Syft `v1.18.1` is observable; DEL-09-05-V3-04 remains parked until the disposable identity exists.
- DEL-09-06-V3-04 alone becomes selectable when A15 lands. It selects a per-response nonce plus dynamic rendering for `/`, `/chat`, `/pipeline`, and `/workbench`, and prescribes no exact attachment code form.
- DEL-09-06-V3-03 is byte-identical to the basis. Current State and Checking Approval SHA fields are unchanged in both edited status files.
- No frontend, product, host, Root, authority-corpus, decision-register, decomposition, SCOPE_CHANGE, lifecycle, dependency, Scope of Work, or memory byte changed.
- F-APP-2 is preserved: no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, production-identity, or other prohibited release act or positive claim occurred.
- Receipt 220 physically follows Receipt 219, names Parent-Receipt 219, uses `EXECUTED`, and its Checks field remains pass/fail-only.

## Independent check results

| Check | Result | Evidence |
|---|---|---|
| Basis and ancestry | PASS | Basis `719fe5e34...` is an ancestor of freeze `52998709c...`; complete four-commit range reviewed. |
| Changed-path inventory | PASS | Exactly 25 paths; 1,312 insertions and 11 deletions; no unstated mutation. |
| Software-workflow affected-check selection | PASS | Selected `harness-self-check`, `app-hold-integrity`, and `harness-pytest`; no frontend check selected. |
| Receipt validator | PASS | Versioned ledger contract validates with Receipt 220 present. |
| Receipt 220 parent/vocabulary/measurements | PASS | Parent Receipt 219; Gate-Outcome `EXECUTED`; Checks is pass/fail-only. |
| Authority-corpus status | PASS | v20; every authority reference matches; no drift. |
| APP-HOLD integrity | PASS | Register matches scan; no held deliverables. |
| APP-HOLD reliance | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| APP-HOLD dispatch | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| Harness self-check | PASS | Exit 0 using the repository Python 3.13 runtime. |
| Harness pytest | PASS | Complete practitioner-harness suite passed using the repository Python 3.13 runtime. |
| Exact change scope | PASS | No violation against the sealed write set. |
| Manifest hashes | PASS | All 24 recorded file identities verify. |
| Manifest membership | PASS | Manifest covers every changed path except itself, with no extra member. |
| Strict JSON | PASS | CHECKS and all three instance STATUS files parse. |
| `git diff --check` | PASS | No whitespace errors. |
| R1 report byte identity | PASS | Filed and external bytes match SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. |
| R2 report byte identity | PASS | Filed and external bytes match SHA-256 `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`. |
| Mobile provenance and owner-answer fidelity | PASS | No A15 `[click]` token; three exact questions and typed answers match the sealed M1 brief. |
| DEL-09-06-V3-04 selected-outcome coherence | PASS | Gate, Depends, Return, and Removed-when are nonce-only and code-shape neutral. |
| DEL-09-06-V3-03 byte fence | PASS | Basis and freeze item bytes are identical. |
| Current State / Checking Approval SHA fence | PASS | Neither field changed in either status file. |
| F-APP-2 and forbidden-path scans | PASS | Release-related additions are authorization questions or explicit no-act/no-claim fences; forbidden paths are absent. |
| A14 identity | PASS | SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact cited match. |
| Pinned completion-reference identity | PASS | SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact cited match. |
| Packaged route inventory | PASS | Exactly `/`, `/chat`, `/pipeline`, and `/workbench` have `page.tsx` route files. |
| Syft observation | PASS | No `syft` executable found; no install or network act attempted. |
| Disposable identity observation | PASS | `security find-identity -v -p codesigning` reports zero valid identities; no key material read or changed. |
| Multi-agent record presence | PASS | Orchestration plan, work graph, and M1/M2/M3 launch/status/return records exist; M2/M3 reconstruction provenance and immutable report identities are honest. |
| Native-descendant evidence calibration | FAIL | Delegation class, non-mechanical role label, instruction-asserted role evidence, and instruction+config/non-mechanism K-SUBAGENT calibration are absent; M-R3-F1. |
| Detached worktree status | PASS | Clean detached HEAD after repository checks. |
| Frontend typecheck/Vitest/build/premerge/render bar | SKIPPED | No `frontend/` path changed and the affected-check selector chose no frontend check; no pass inferred. |
| Signing/notarization/publication/release execution | SKIPPED | Prohibited and outside this record-only tranche under F-APP-2; no pass or readiness inference. |

## Verdict

**FAIL.** The owner transcription, A15 semantics, prior semantic remediations, host-act boundaries, F-APP-2 fences, exact scope, prior-review identities, and all deterministic checks are sound. One MAJOR governance-evidence issue remains: the newly reconstructed multi-agent record does not apply the mandatory evidence calibration for delegated-harness-native Agent-2 role and K-SUBAGENT non-delegation claims. Correct that record-only issue and send the complete next freeze to a fresh reviewer.
