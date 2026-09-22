# App production source review — R5/R6

Date: 2026-09-22. Verdict: **CHANGES REQUIRED — two P2 findings**.

## Findings

### ASR-01 [P2] Do not attribute a delegation-policy storage assignment to D-APP-127

File: `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking/ScopeOfWork.md`, lines 33 and 43 (initial reviewed bytes).

The new current responsibility says “D-APP-127 assigns the App thread index the bound policy”, and the acceptance clause repeats that assignment. D-APP-127 contains no such field assignment. Its incorporated D-GOV-43 proposal/IMPACT retires Root DEL-02-11 and retains an App index keyed by thread identity; the re-platform HANDOFF describes that index and upstream `[agents]` configuration, but does not assign the surviving managed-delegation policy field to it. This is stronger than the cited authority and can incorrectly turn an unresolved storage/ownership design into an already accepted requirement. The manifest itself records absent per-chat policy implementation, so it is especially important not to manufacture an earlier assignment.

Preserve the accepted default/binding/narrowing obligation and the retirement of Root DEL-02-11. Remove the unsupported attribution and leave the replacement storage/interface allocation as source-grounded follow-through, or cite an actual accepted source that settles it. This does not require repeating a previously settled human decision.

### ASR-02 [P2] Resolve the two incompatible current account-admission instructions

File: `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/ScopeOfWork.md`, new lines 39–41 versus unchanged lines 51–54 (initial reviewed bytes).

The repaired Current responsibility correctly says per-root account consent and hosted admission are retired live-login prerequisites. Immediately following it, Current acceptance obligations 1, 3 and 4 still declare root-private per-folder login semantics unchanged and require supplier qualification, Root DEL-02-09 and G3/G-CSP/G4. Both subsections sit in the same explicitly Controlling contract section. A downstream reader cannot apply both; the generic residual pointer does not identify which instruction controls. D-APP-127 expressly retires these particular account/admission prerequisites, so retaining them as current acceptance conditions defeats the repair.

Apply the exact D-APP-127 supersession to the affected acceptance purposes, or clearly mark their retired portions as superseded while retaining surviving guarantees. Keep the separately unresolved Q7 account-indicator and role/posture questions visible; no blanket removal of account, renderer, attachment or secret-protection obligations is warranted. Update the changed-key/evidence manifest for any affected block.

## Reviewed scope and basis

Fresh native TASK child `/root/app_source_review`, parent `/root` HELP_HUMAN; actual mechanism `collaboration.spawn_agent`. No implementation authorship, descendant delegation, source edits, Git mutation or lifecycle action. Engine Codex; same parent-inherited GPT-6 model family, precise provider/model identifier not separately observable. This is independent authorship/context review, not model diversity or personal owner review. Host filesystem access is unrestricted; the read-only production boundary is instruction-enforced.

Base: `379df923927d157be3ebb51d8a1dcf783d970112`. Read Root `AGENTS.md`, `agents/AGENT_TASK.md`, App `AGENTS.md`, parent BRIEF and AGENT0_DISPOSITIONS. No other full role or skill was activated. The reviewer used the bounded assignment directly; cited method/evidence records were inspected as review evidence, not selected as an executing workflow.

The frozen scope is the **183 files** recorded in `APP_SOURCE_REVIEW_HASHES.json`: all 19 changed SoWs (35 physical blocks, 56 original claim keys), all 54 statuses, 54 memories (53 additive changes and a new DEL-09-07 memory), 54 new deliverable run records, D-APP-131 and the decision register. The review covered the complete production diff against the base, all introduced record content (with exact repeated-template comparison), current controlling contract context, relevant adjacent requirements and cited prior-authority sources. It does not certify every unchanged historical clause in the 54-deliverable corpus.

Parent later authorized a separate PKG-06/07 SoW tranche outside these frozen paths. Those new paths require their own review and are excluded here. Any subsequent modification to one of these 183 files requires an affected backcheck.

## Verification and evidence

- Before deliverable reliance, App-local APP-HOLD command ran for every one of the 54 targets with operation `reliance` and entry path `execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-CROSS-PROJECT-R5R6/reviews/APP_SOURCE_REVIEW.md`: exit 0, all ALLOW/CLEAR/NOT_HELD; no active/scan holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `7bd56dd823f28427dd4bfb8ca65017b4fe9c0b8165fb32a702f896e49f8ba6ec`.
- Independently verified all initial 56 manifest keys and before/after block hashes against the actual files. Reversing the 35 unique replacements reconstructed all 19 base SoWs exactly. No undeclared source deletion or mutation was found in that scope.
- All 54 statuses preserve Current State, Checking Approval SHA and Authorization Basis. Every pre-existing History body remains intact; Remaining changes were read across all files and checked for the exact shared-template and affected-check substitutions.
- All 53 prior memories preserve their complete previous content; the DEL-09-07 memory is newly created and records no new production activation. All 54 run records match their deliverable identity and exact changed-key population and disclaim new qualification/lifecycle/acceptance results.
- All 36 explicit full-path verification/source references extracted from repaired blocks resolve. Named checks remain hooks, not claimed new test outcomes.
- Read the R5 verification script and author PKG04/PKG08 reports. Its output-writing backcheck was not executed by this read-only reviewer; independent in-memory reconstruction and field checks above supplied source-integrity evidence. Full R6 accounting/script execution is covered by the separate accounting reviewer/parent.
- Inspected D-GOV-43, its A2 supplement, D-APP-127 and the incorporated impact/handoff provisions. No additional invented human/Root acceptance, D-APP-116–119/P-01 hold discharge, legacy/live qualification equivalence, lifecycle/approval-SHA drift, or unsupported new test result was found in this frozen production diff beyond ASR-01/02.
- The new carrier text preserves redaction, typed failure, attachment, event/terminal, role/scope and delegation-record guarantees while moving retired implementation details to evidence. Shorter blocks or removed function/shape snapshots alone were not treated as defects.
- Conversion and conformance narratives correctly distinguish historical execution from current parity, actual intended-role receipt and exact packaged/native results. An ancillary conversion raw-JSON count inconsistency was reported to its author; the author identified and bound the overlooked DEL-01-03 VALIDATION_DUAL.json and corrected the table/CSV. This is separate evidence scope, not a production acceptance finding.
- Initial 183-file hashes remained unchanged at the completion of source checks. File and instruction hashes plus machine-check results are recorded in the paired JSON.

## Limits and return

No product code changed in this scope; no product/native test run, human inspection, release authorization, new hold discharge or whole-project completion is asserted. Existing unmodified legacy/authority conflicts remain residuals where explicitly preserved. R6 derivative files were being finalized and are outside this source-review verdict. Repair ASR-01/02, regenerate affected binding/accounting evidence, then request the bounded backcheck on the actual candidate.


## Affected backcheck — final integrated source candidate

Date: 2026-09-22. **Current verdict: PASS. ASR-01 and ASR-02 are resolved; no remaining actionable finding in the original 183-file review scope.** The initial review and its findings above remain historical evidence.

The parent resumed this reviewer after the App manager confirmed final source fan-in. Of the original 183 paths, 23 changed since the first snapshot: two SoWs, eight statuses and thirteen local run records. The other 160 files—including all 54 memories, D-APP-131 and the decision register—remain identical to their initial reviewed hashes. Current bytes for every original path are bound by `APP_SOURCE_REVIEW_CURRENT_HASHES.json`; the first snapshot remains in `APP_SOURCE_REVIEW_HASHES.json`.

**ASR-01 resolution.** DEL-03-02 Current responsibility and acceptance obligation 3 no longer attribute a policy field to D-APP-127 or to the App thread index. They retain the accepted none-default, request binding and managed-delegation narrowing purpose, identify the retirement of Root DEL-02-11, and expressly leave replacement storage/interface ownership and verification open. The live Remaining item and its dependency paragraph now make the same distinction. Historical wording remains dated evidence rather than a newly asserted assignment.

**ASR-02 resolution.** DEL-02-05 Current acceptance obligations now agree with Current responsibility: Codex custody, private authentication/shared configuration, truthful account and Settings presentation, user-selected permission policy, credential separation and surviving attachment/renderer/secret protections remain; retired hosted consent, root-private per-folder login, supplier gates and Root DEL-02-09 are not awaited live-login prerequisites. S-8 is named without inventing its native result. Q7's exact indicator conflict and the inherited Agent 0/1/2 entry and role/posture-label conflict remain explicitly identified for source-faithful reconciliation, including the distinction between current instructions and authority-corpus acceptance. All five SEC-2 source subkeys, including unresolved portions, are included in the updated manifest.

**Final fan-in checks.** Read the affected source paragraphs, complete changed status lines and regenerated run-record content. Rechecked all 19 original-scope SoWs against the base and final manifest: 36 physical blocks and 61 source keys now inverse-reconstruct all 19 complete base files exactly. Verified all 54 statuses still preserve Current State, Checking Approval SHA, Authorization Basis and every pre-existing History byte. Every one of the 53 non-retired deliverable residual category summaries matches its final keyed accounting population; DEL-09-07 remains retired. All 54 local run records match their identity and complete final manifest key lists, including the PKG-06/07 expansion, while retaining the no-new-qualification/lifecycle/acceptance boundary.

The separate `APP_EXPANSION_REVIEW.md` supplies independent PASS coverage of the twelve added PKG-06/07 SoWs (25 blocks/30 keys). Its source review was read for coordination and not duplicated. Together, source coverage is 31 SoWs, 61 physical blocks and 91 source keys; the original 183-file population plus twelve additional SoWs is 195 production/control files. Full R6 derivative accounting, global receipt/manifest checks and registered shared checks remain parent/integration-reviewer work; this source PASS does not pre-judge those separate checks.

APP-HOLD reliance was rerun for all 54 targets: exit 0, ALLOW, no active or scanned holds, the same register/scan fingerprints as the first review. Exact preflight output is preserved in the current hash manifest. A final comparison found no drift in any of the 183 captured current files. No product/native tests, production writes, Git mutations, new human acts, release/acceptance claims or further delegation occurred in this backcheck. Any later change to a bound source requires affected review.
