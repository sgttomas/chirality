# App v3 Node M / A15 — Independent Review Round 5

- Review date: 2026-09-04
- Reviewer: fresh, read-only descendant instructed for ephemeral Agent-2 reviewer mode; no Node M implementation or prior-review participation
- Execution class: `delegated-harness-native`
- Role evidence: Agent-2 role not mechanically enforced; governed-workflow role evidence `instruction-asserted`
- Non-delegation evidence: instruction+config asserted, not mechanism-proven; no descendant was observed
- Method: repository-native `software-code-review` guidance applied to the complete frozen diff
- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)
- Frozen candidate: `085189ba093ec1705b68dc7f131692e132ff4cf4`
- Candidate commits: `c4decf4023a1f8652f90002ab3016088d7a3c668`, `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`, `4fa170341700e491dff8c72ce1229ba84735f073`, `52998709c5c19bc5c3df3944735593299d60be56`, `c3c3b628203ccc949d3ee3b3573a96b45f472278`, and `085189ba093ec1705b68dc7f131692e132ff4cf4`
- Worktree: `/private/tmp/chirality-app-v3-a15-20260904/nodeM-review-r5` (detached and retained until tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 1 MAJOR, 0 MINOR, 0 NOTE

## Reviewed scope

I reviewed 100% of `git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..085189ba093ec1705b68dc7f131692e132ff4cf4`: 35 paths, 2,199 insertions, and 11 deletions across the complete six-commit range. The scope consists only of the A15 owner-ruling record, the bounded DEL-09-05 and DEL-09-06 status edits, Receipts 220–221, and the Node M AgentRuns package. Exact change-scope validation passed; no unstated path changed.

## Prior-finding disposition verification

| Finding | Round-5 result | Evidence |
|---|---|---|
| M-R1-F1 | PASS | A15 and Receipt 220 accurately identify three typed plain-text mobile-fallback replies. A15 contains no `[click]` marker; each question matches the sealed owner-source brief and each answer is exactly `Yes, so authorized.` |
| M-R1-F2 | PASS | DEL-09-05-V3-02 is `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable. Syft remains absent; A15 authorization is prospective; A14 remains truthful dated history; the owner re-pin alternative remains explicit. |
| M-R1-F3 | PASS | The filed R1 report is byte-identical to the external immutable report at SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`. R1 FAIL and its accepted remediation are represented in the durable record. |
| M-R2-F1 | PASS | DEL-09-06-V3-04's gate, Depends, Return, and Removed-when clauses consistently select a per-response nonce with dynamic rendering, reject hash/SRI as the selected result, and leave the exact attachment code shape open. DEL-09-06-V3-03 remains byte-identical to the basis. |
| M-R2-F2 | PASS for record presence and provenance | The orchestration plan, work graph, M1–M5 launch/status/return records, four prior immutable reports, dispositions, and active R5 handoff exist. Reconstruction versus contemporaneous provenance is explicit, and all four filed reports are byte-identical to their external originals. |
| M-R3-F1 | FAIL at complete mutable-record calibration | The AgentRuns records and Receipts 220–221 carry the required native-descendant calibration. The candidate A15 record is neither an immutable prior report, a spent historical handoff, nor the preserved M1 brief, yet it still calls M1 a “sealed ephemeral Agent 2 generalist” without the required `delegated-harness-native`, non-mechanical-role, and `instruction-asserted` qualifications. This leaves the disposition's “every Agent-2 role statement” claim incomplete, as M-R5-F1 details. |
| M-R4-F1 | PASS | M1's status is `review_ready_r5`; its timeline records R4 FAIL over `c3c3b628203ccc949d3ee3b3573a96b45f472278`; M1 and the top-level return identify all four filed prior reports; every current-state review pointer selects `REVIEW_R5_HANDOFF.md`; and R2/R3/R4 handoffs are clearly spent history. |

The four filed prior reports are byte-identical to their external immutable sources at the required SHA-256 values `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`, `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`, `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802`, and `ceb24881cf877fce9771c2b7dc9c820c8d34aed9d079f42ec6cee0f9392fd47a`. The sealed M1 brief remains byte-identical at SHA-256 `65ea1171d38ef3bf58757f34d2329df333401efb5a548db5e886625f2dec4946`.

## Finding

### M-R5-F1 — MAJOR — The candidate A15 ruling record retains an uncalibrated native-descendant Agent-2 role claim

Path and line:

- `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md:8`

Governing evidence:

- `AGENTS.md:87-106`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/REVIEW_R5_HANDOFF.md:66-74`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/REVIEW_DISPOSITIONS.md:51`

Evidence: A15 says HELP_HUMAN relayed the rulings to “a sealed ephemeral Agent 2 generalist.” Native descent does not mechanically assign Agent-2 status. The governing doctrine and the sealed R5 handoff require every mutable role statement to identify `delegated-harness-native`, label Agent-2 mode `role not mechanically enforced`, mark governed-workflow role evidence `instruction-asserted`, and calibrate K-SUBAGENT/non-delegation as instruction+config asserted rather than mechanism-proven. The R5 handoff exempts only preserved immutable reports, spent historical handoffs, and the contemporaneous sealed M1 brief. A15 is a current candidate record and is not one of those exceptions. All other current mutable role records are calibrated.

Impact: the durable ruling record still presents an instruction-assigned role as an unqualified fact, while the disposition and `CHECKS.json` claim every mutable role statement is calibrated. This is the same governance-evidence overclaim class as M-R3-F1 and leaves that prior MAJOR incompletely disposed at manager fan-in. The owner ruling substance itself is unaffected.

Remedy: change only A15's execution-attribution sentence to state that HELP_HUMAN relayed the rulings to a `delegated-harness-native` descendant instructed to operate in ephemeral Agent-2 generalist mode, with the role not mechanically enforced and governed-workflow role evidence instruction-asserted; state that K-SUBAGENT/non-delegation is instruction+config asserted, not mechanism-proven, and no descendant was observed. Preserve the owner questions, answers, ruling substance, status semantics, and M1 sealed brief. File this report immutably, disposition the finding, update dependent current run-record/manifest/receipt pointers without editing Receipt 220 or Receipt 221, and send the complete remediation freeze to a fresh reviewer.

## Semantics verified as correct

- The owner-question/answer transcription and typed mobile-fallback provenance are exact.
- A15 authorizes but does not perform the Syft install, disposable identity creation, or credential-transition drill. A14 remains truthful dated history and its deferrals are lifted prospectively only.
- DEL-09-05-V3-02 remains parked until owner-installed Syft `v1.18.1` is observable; DEL-09-05-V3-04 remains parked until the owner-created disposable identity exists.
- DEL-09-06-V3-04 alone becomes selectable when A15 lands. It selects per-response nonce plus dynamic rendering for `/`, `/chat`, `/pipeline`, and `/workbench`, with a nonce-only closure contract and implementation latitude inside that outcome.
- DEL-09-06-V3-03 is byte-identical to the basis. Current State and Checking Approval SHA fields are unchanged in both edited status files.
- Receipt 220 was not edited by the latest remediation. Receipt 221 is a pure append after Receipt 220, names Parent-Receipt 220, preserves the Step 0 cursor, uses the admitted `AWAITING_OWNER` outcome, and points to the current R5 surfaces.
- M1's current status/return, the top-level return/handoff, work graph, checks, manifest, and Receipt 221 agree on four filed prior reports, R5 pending, and `REVIEW_R5_HANDOFF.md` as the only active next-review contract. The candidate correctly does not pretend that the future R5 verdict exists.
- No frontend/product, host, Root, authority-corpus, decision-register, decomposition, SCOPE_CHANGE, lifecycle, dependency, Scope of Work, memory, or Checking Approval SHA byte changed.
- F-APP-2 remains intact: no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, production-identity, or other prohibited release act or positive claim occurred.

## Independent check results

| Check | Result | Evidence |
|---|---|---|
| Basis and ancestry | PASS | Basis `719fe5e34...` is an ancestor of freeze `085189ba0...`; complete six-commit range reviewed. |
| Changed-path inventory | PASS | Exactly 35 paths; 2,199 insertions and 11 deletions; no unstated mutation. |
| Software-workflow affected-check selection | PASS | With App-relative paths, selected `harness-self-check`, `app-hold-integrity`, and `harness-pytest`; no frontend check selected. |
| Receipt validator | PASS | Ledger validator returned VALID with the versioned receipt contract satisfied. |
| Receipt 220 preservation | PASS | Latest-remediation diff is a pure 32-line append with zero deletions; normalized Receipt-220 block hashes match before and after at `38c9be8df4246571a259e825a31bbd017ab4a77753da215056d6c111f1405fe9`. |
| Receipt 221 structure | PASS | Physical successor to Receipt 220; Parent Receipt 220; same Step 0 cursor; admitted `AWAITING_OWNER` Gate-Outcome; pass/fail-only Checks posture. |
| Authority-corpus status | PASS | v20; every authority reference matches; no drift. |
| APP-HOLD integrity | PASS | Register matches scan; no held deliverables. |
| APP-HOLD reliance | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| APP-HOLD dispatch | PASS | ALLOW for DEL-09-05 and DEL-09-06. |
| Harness self-check | PASS | Exit 0 at the unchanged repository baseline; existing INFO/WARN/REVIEW findings were reported, not introduced by this tranche. |
| Harness pytest | PASS | Complete practitioner-harness suite passed using repository Python 3.13. |
| Exact change scope | PASS | No violation against the sealed write set. |
| Manifest hashes | PASS | All 34 recorded file identities verify. |
| Manifest membership | PASS | Manifest covers every changed path except itself, with no extra member. |
| Strict JSON | PASS | `CHECKS.json` and all M1–M5 STATUS files parse. |
| `git diff --check` | PASS | No whitespace errors. |
| Prior report byte identities | PASS | Filed R1–R4 bytes match their external immutable reports and recorded SHA-256 values. |
| Sealed M1 brief identity | PASS | Current bytes match SHA-256 `65ea1171d38ef3bf58757f34d2329df333401efb5a548db5e886625f2dec4946`. |
| Current-round and handoff coherence | PASS | Current mutable round pointers identify R5 only; older handoffs are spent historical contracts; no vague prior-report count remains. |
| R5 anti-self-reference | PASS | Candidate contains R1–R4 reports and the R5 handoff, and correctly excludes the not-yet-created R5 verdict/report. |
| Mobile provenance and owner-answer fidelity | PASS | No A15 `[click]` token; three exact questions and typed answers match the sealed M1 brief. |
| DEL-09-06-V3-04 selected-outcome coherence | PASS | Gate, Depends, Return, and Removed-when are nonce-only and code-shape neutral. |
| DEL-09-06-V3-03 byte fence | PASS | Basis and freeze item-section bytes are identical. |
| Current State / Checking Approval SHA fence | PASS | Neither field changed in either status file. |
| Native-descendant evidence calibration | FAIL | All mutable run/receipt records are calibrated, but the current A15 record's Agent-2 attribution is not; M-R5-F1. |
| F-APP-2 and forbidden-path scans | PASS | Release-related additions are authorization questions or explicit no-act/no-claim fences; forbidden paths are absent. |
| A14 identity | PASS | SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact cited match. |
| Pinned completion-reference identity | PASS | SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact cited match. |
| Packaged route inventory | PASS | Exactly `/`, `/chat`, `/pipeline`, and `/workbench` have `page.tsx` route files. |
| Syft observation | PASS | No `syft` executable found; no installation or network act attempted. |
| Disposable identity observation | PASS | `security find-identity -v -p codesigning` reports zero valid identities; no key material read or changed. |
| Detached review worktree before report write | PASS | Clean detached HEAD. |
| Frontend typecheck/Vitest/build/premerge/render bar | SKIPPED | No `frontend/` path changed and the affected-check selector chose no frontend check; no pass inferred. |
| Signing/notarization/publication/release execution | SKIPPED | Prohibited and outside this record-only tranche under F-APP-2; no pass or readiness inference. |

## Superseded check attempts

- A first affected-check selection used repo-root-prefixed paths and therefore returned only the profile's always-checks. The corrected App-relative invocation selected the execution/docs/loop path rule and `harness-pytest`; no pass was inferred from the first shape.
- A first batched external-report comparison relied on zsh word splitting and addressed invalid composite paths. Explicit per-report `cmp` checks were rerun and all four passed; no identity claim was inferred from the rejected batch.
- A raw Receipt-220 prefix comparison retained the new append separator and therefore differed. The corrected normalized Receipt-220 block comparison matched, and the latest-remediation diff independently showed a pure append with zero deletions.
- A first V3-03 fence command used zsh's read-only variable name `status` and did not run. It was rerun with `status_path` and passed; no pass was inferred from the rejected invocation.

## Verdict

**FAIL.** The A15 owner transcription and ruling substance, parked/selectable states, host-act boundaries, A14 history, all prior current-round/handoff repairs, Receipt 220 preservation, corrective Receipt 221, exact scope, immutable inputs, F-APP-2 fences, and deterministic gates are sound. One MAJOR governance-evidence defect remains: A15 itself carries an unqualified native-descendant Agent-2 role claim, contradicting both the R5 handoff and the recorded disposition that every mutable role statement is calibrated. Correct M-R5-F1 and submit the complete next freeze to a fresh reviewer before manager fan-in.

Post-PASS filing may remain narrative-only only after a future fresh review returns zero BLOCKER and zero MAJOR findings. At that point the immutable review report and final closeout records may be filed without changing owner-ruling, deliverable, product, test, or CSS bytes.
