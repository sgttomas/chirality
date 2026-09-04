# App v3 Node M / A15 — Independent Review Round 4

- Review date: 2026-09-04
- Reviewer: fresh, read-only descendant instructed for ephemeral Agent-2 reviewer mode; no Node M implementation or prior-review participation
- Execution class: `delegated-harness-native`
- Role evidence: Agent-2 role not mechanically enforced; governed-workflow role evidence `instruction-asserted`
- Non-delegation evidence: instruction+config asserted, not mechanism-proven; no descendant was observed
- Method: repository-native `software-code-review` guidance applied to the complete frozen diff
- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)
- Frozen candidate: `c3c3b628203ccc949d3ee3b3573a96b45f472278`
- Candidate commits: `c4decf4023a1f8652f90002ab3016088d7a3c668`, `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`, `4fa170341700e491dff8c72ce1229ba84735f073`, `52998709c5c19bc5c3df3944735593299d60be56`, and `c3c3b628203ccc949d3ee3b3573a96b45f472278`
- Worktree: `/private/tmp/chirality-app-v3-a15-20260904/nodeM-review-r4` (detached and retained until tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 1 MAJOR, 0 MINOR, 0 NOTE

## Reviewed scope

I reviewed 100% of `git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..c3c3b628203ccc949d3ee3b3573a96b45f472278`: 30 paths, 1,751 insertions, and 11 deletions across the complete five-commit range. The scope consists only of the A15 owner-ruling record, the bounded DEL-09-05 and DEL-09-06 status edits, Receipt 220, and the Node M AgentRuns package. Exact change-scope validation passed; no unstated path changed.

## Prior-finding disposition verification

| Finding | Round-4 result | Evidence |
|---|---|---|
| M-R1-F1 | PASS | A15 and Receipt 220 accurately identify three typed plain-text mobile-fallback replies. A15 contains no `[click]` marker; each question matches the sealed owner-source brief and each answer is exactly `Yes, so authorized.` |
| M-R1-F2 | PASS | DEL-09-05-V3-02 is `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable. Syft remains absent; A15 authorization is prospective; A14 remains truthful dated history; the owner re-pin alternative remains explicit. |
| M-R1-F3 | PASS | The filed R1 report is byte-identical to the external immutable report at SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. R1 FAIL and its accepted remediation are represented in the durable record. |
| M-R2-F1 | PASS | DEL-09-06-V3-04's gate, Depends, Return, and Removed-when clauses consistently select a per-response nonce with dynamic rendering, do not permit hash/SRI as the selected result, and leave the exact attachment code shape open. DEL-09-06-V3-03 remains byte-identical to the basis. |
| M-R2-F2 | FAIL at current-record closeout coherence | The orchestration graph and M1–M4 launch/status/return records exist, the three prior reports are immutable and byte-identical, and reconstruction provenance is calibrated. However, three mutable current records retain stale round-state or handoff text, as M-R4-F1 details. |
| M-R3-F1 | PASS for evidence calibration | Current orchestration, work-graph, checks, handoff, receipt, M1–M4 status/return, and reconstructed launch records identify `delegated-harness-native`; Agent-2 roles are labelled `role not mechanically enforced` with `instruction-asserted` evidence; non-delegation is instruction+config asserted, not mechanism-proven; no descendants were observed. Earlier sealed handoffs, the sealed M1 brief, and immutable review reports remain historical direction/output governed by the adjacent calibration. |

The R1, R2, and R3 reports filed in the candidate are byte-identical to their external immutable sources at the required SHA-256 values `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`, `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`, and `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802`. The sealed M1 brief is unchanged from the first reviewed freeze at SHA-256 `65ea1171d38ef3bf58757f34d2329df333401efb5a548db5e886625f2dec4946`.

## Finding

### M-R4-F1 — MAJOR — Mutable current records retain stale round-state and reviewer-handoff claims

Paths and lines:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M1/STATUS.json:14`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/instances/M1/RETURN.md:27-28`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/RETURN.md:49-54`

Evidence: M1's current status is still `review_ready_r3`, although its timeline and both return surfaces correctly say that round 3 failed, its finding was remediated, and the candidate is awaiting round 4. M1's current return says the package includes “both immutable review reports,” but three immutable prior-review reports are present. The top-level return first says the next fresh reviewer consumes `REVIEW_R3_HANDOFF.md`, even though that review has occurred; the same file later correctly points to `REVIEW_R4_HANDOFF.md`.

Impact: the current run record is internally contradictory at the manager fan-in boundary. It can misidentify the live review round and direct a consumer to a spent handoff, while undercounting the immutable review evidence. This violates the required truthful, complete multi-agent record and closeout-pointer consistency even though the A15 ruling and deliverable-state semantics are sound.

Remedy: set M1's current status to `review_ready_r4`; change its return to identify all three immutable prior-review reports; and remove or correct the spent `REVIEW_R3_HANDOFF.md` “next reviewer” statement in the top-level return so the only current next-review pointer is `REVIEW_R4_HANDOFF.md`. File this report immutably, record/disposition this finding, update all dependent manifest/check/handoff/receipt pointers truthfully, and submit the complete remediation freeze to a fresh reviewer. Do not alter A15 ruling substance or deliverable item semantics.

## Semantics verified as correct

- The owner-question/answer transcription and plain-text mobile-fallback provenance are exact.
- A15 authorizes but does not perform the Syft install, disposable identity creation, or credential-transition drill. A14 remains truthful dated history and its deferrals are lifted prospectively only.
- DEL-09-05-V3-02 remains parked until owner-installed Syft `v1.18.1` is observable; DEL-09-05-V3-04 remains parked until the owner-created disposable identity exists.
- DEL-09-06-V3-04 alone becomes selectable when A15 lands. It selects per-response nonce plus dynamic rendering for `/`, `/chat`, `/pipeline`, and `/workbench`, while preserving implementation latitude inside that outcome.
- DEL-09-06-V3-03 is byte-identical to the basis. Current State and Checking Approval SHA fields are unchanged in both edited status files.
- No frontend/product, host, Root, authority-corpus, decision-register, decomposition, SCOPE_CHANGE, lifecycle, dependency, Scope of Work, or memory byte changed.
- F-APP-2 remains intact: no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, production-identity, or other prohibited release act or positive claim occurred.
- Receipt 220 physically follows Receipt 219, names Parent-Receipt 219, uses `EXECUTED`, and its Checks field is pass/fail-only.

## Independent check results

| Check | Result | Evidence |
|---|---|---|
| Basis and ancestry | PASS | Basis `719fe5e34...` is an ancestor of freeze `c3c3b6282...`; complete five-commit range reviewed. |
| Changed-path inventory | PASS | Exactly 30 paths; 1,751 insertions and 11 deletions; no unstated mutation. |
| Software-workflow affected-check selection | PASS | Selected `harness-self-check`, `app-hold-integrity`, and `harness-pytest`; no frontend check selected. |
| Receipt validator | PASS | Ledger validator returned VALID with the versioned receipt contract satisfied. |
| Receipt 220 structure | PASS | One Receipt 220; Parent Receipt 219; Gate-Outcome `EXECUTED`; pass/fail-only Checks posture. |
| Authority-corpus status | PASS | v20; every authority reference matches; no drift. |
| APP-HOLD integrity | PASS | Register matches scan; no held deliverables. |
| APP-HOLD reliance | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| APP-HOLD dispatch | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| Harness self-check | PASS | Exit 0 at the unchanged repository baseline; existing INFO/WARN/REVIEW findings were reported, not introduced by this tranche. |
| Harness pytest | PASS | Complete practitioner-harness suite passed using repository Python 3.13. |
| Exact change scope | PASS | No violation against the sealed write set. |
| Manifest hashes | PASS | All 29 recorded file identities verify. |
| Manifest membership | PASS | Manifest covers every changed path except itself, with no extra member. |
| Strict JSON | PASS | CHECKS and all M1–M4 STATUS files parse. |
| `git diff --check` | PASS | No whitespace errors. |
| Prior report byte identities | PASS | R1, R2, and R3 filed bytes match their external immutable reports and recorded SHA-256 values. |
| Sealed M1 brief identity | PASS | Current bytes match the first reviewed freeze at SHA-256 `65ea1171d38ef3bf58757f34d2329df333401efb5a548db5e886625f2dec4946`. |
| Mobile provenance and owner-answer fidelity | PASS | No A15 `[click]` token; three exact questions and typed answers match the sealed M1 brief. |
| DEL-09-06-V3-04 selected-outcome coherence | PASS | Gate, Depends, Return, and Removed-when are nonce-only and code-shape neutral. |
| DEL-09-06-V3-03 byte fence | PASS | Basis and freeze item-section bytes hash identically. |
| Current State / Checking Approval SHA fence | PASS | Neither field changed in either status file. |
| Native-descendant evidence calibration | PASS | Required execution-class, role-evidence, and non-delegation calibration is present in current mutable role records; no descendant observed. |
| Current round/handoff record coherence | FAIL | M1 status, M1 review-evidence count, and one top-level next-review pointer are stale; M-R4-F1. |
| F-APP-2 and forbidden-path scans | PASS | Release-related additions are authorization questions or explicit no-act/no-claim fences; forbidden paths are absent. |
| A14 identity | PASS | SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact cited match. |
| Pinned completion-reference identity | PASS | SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact cited match. |
| Packaged route inventory | PASS | Exactly `/`, `/chat`, `/pipeline`, and `/workbench` have `page.tsx` route files. |
| Syft observation | PASS | No `syft` executable found; no installation or network act attempted. |
| Disposable identity observation | PASS | `security find-identity -v -p codesigning` reports zero valid identities; no key material read or changed. |
| Detached review worktree status before report write | PASS | Clean detached HEAD. |
| Frontend typecheck/Vitest/build/premerge/render bar | SKIPPED | No `frontend/` path changed and the affected-check selector chose no frontend check; no pass inferred. |
| Signing/notarization/publication/release execution | SKIPPED | Prohibited and outside this record-only tranche under F-APP-2; no pass or readiness inference. |

## Verdict

**FAIL.** A15's owner transcription, ruling semantics, parked/selectable states, prior substantive remediations, host-act boundaries, evidence calibration, F-APP-2 fences, exact scope, immutable-review identities, and deterministic gates are sound. One MAJOR durable-record issue remains: mutable current records disagree on the active review round and next-review handoff. Correct M-R4-F1 and send the complete next freeze to a fresh reviewer before manager fan-in.
