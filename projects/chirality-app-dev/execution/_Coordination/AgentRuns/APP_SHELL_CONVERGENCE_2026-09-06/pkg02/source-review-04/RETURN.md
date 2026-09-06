# Independent complete source review — BLOCK

Reviewed all 25 source/test members of integration-01/SOURCE_MANIFEST_v3.json, SHA256 `9241484bdda05836a5e8163d42fe84b62ff620520cdeeb23b250e64ccb782824`, and the complete candidate diff from `e00238621db7a00b036245962c21e3fc6ed75452`. All source hashes matched before and after. Scope validation passed, and semantic path review found no product edit outside the sealed author locus. The supplied APP-HOLD dispatch preflight allows all three targets. This is a derivative review of candidate implementation, not lifecycle acceptance or authoritative decomposition truth.

## R1 — P2: Preserve each reply's originating persona in its speaker label

Location: frontend/src/components/shell/chat-panel.tsx:624; related message shape at lines 32–37 and assistant message construction at lines 416–420.

Complete a turn as Working Items, then select Research. The intended Agent control stays live and the repaired binding deliberately retains the transcript. However, every existing assistant bubble's visible speaker label and identifier tooltip read the current activePersona rather than the persona that produced that message. Working Items answers therefore immediately become labelled Research, before Research has answered anything. This is a new regression from adding persona speaker labels, and conflicts with the target's persona display-name attribution and the shell's presentation-only provenance boundary.

Capture the originating persona on the local assistant message when the turn is created and render that stable value for both label and tooltip. Give any initial assistant greeting an explicit truthful treatment. This requires no runtime schema or persisted authority change. Add a regression with a completed answer under one persona, an Agent change and a second answer: the first label/title must remain unchanged and the second must name the new persona. The current persona-change tests assert transcript and binding retention but never inspect speaker attribution.

## Separate browser validation failure — diagnosis still required

The manager supplied browser-integration-03/RETURN.md and draft-diagnostic.json during this review. The actual diagnostic records an empty textarea immediately after Playwright fill while expanded, with identical DOM node identity; ordinary non-expanded fill retains its value through switching Files. Keyboard-by-keyboard input was not exercised. This reviewer did not execute that browser procedure and does not classify the fill-only observation as a confirmed ordinary-keyboard product defect.

The source has an ancestor onInputCapture at woven-dialogue-shell.tsx:486–488 calling restoreExpanded before ChatPanel's textarea onChange stores the incoming draft at chat-panel.tsx:756 onward. That is a concrete event-ordering locus to investigate, not a proven cause. Keep browser acceptance blocked pending normal-keyboard reproduction and diagnosis; preserve the failed automation evidence. A correction, if warranted, must preserve the first input and expansion restoration without remounting ChatPanel. This issue is separate from R1 and does not change R1's confirmed source basis.

## Coverage and limits

Reviewed the single-return ShellFrame callback and unchanged default caller behavior, stable ChatPanel composition, reconnect ownership and guard, settings anchoring/dismissal, theme access, context presentation, canonical-root synchronization and selected-root draft identity, stale boot/apply checks, pending folder guards, native intent/drop gates, enduring conversation binding, subsequent-persona root rejection and explicit New chat reset. The prior folder-lock finding is repaired at source level. Settings now anchors above/below its actual trigger and handles Escape/outside dismissal; manager-supplied browser evidence reports those paths passed.

Reviewed main/preload additions and their tests: sender validation precedes registration, existing canonical directory/instruction-root policy is reused, native recent-document menu roles retain Edit/View/Window menus, GUI open-file holds one pending validated intent, the renderer applies selection policy, preload strips privileged event objects and removes the exact listener. No startup recent-list clearing, new runtime capability or file-policy change was introduced. Native delivery and isolated app identity evidence remain required separately.

Reviewed all geometry/default changes, saved-state compatibility, removal of activity height writers and separator, scoped Stone styles, compact composer/IME handling, right-panel tab/keyboard/menu behavior, document/file-tree presentation, existing replay selection guards, per-session Activity derivations, local version-based Clear/filter behavior and every changed test. No other actionable source finding was identified. Activity retains existing projection components rather than changing shared stream semantics.

Affected-check selection requires frontend-test, frontend-typecheck, app-hold-integrity and harness-self-check. The sealed brief also retains build/premerge, browser and native evidence requirements. This reviewer ran no test suite, build, browser, server, native app or public action. Earlier feedback passes do not establish final validation of these bytes. T4 weaving, T6 organisation/account, historical per-chat Reveal, no-folder capability and D121 remain explicit later scope; no closure is claimed.

## Decision and attribution

OwnerStandingApproval: D-APP-64 §3
AgentJudgment: REJECT_FOR_REMEDIATION
SelectedOutcome: BLOCK source fan-in until R1 is repaired and a fresh complete review passes; browser acceptance also remains blocked pending its separately calibrated input diagnosis.
JudgedBy: TASK software-code-review /root/shell_pkg02/source_review04
OwnerCaseSelection: NONE
RejectedAlternatives: Passing transcript labels that falsely reassign prior replies; treating fill-only browser evidence as proven ordinary-keyboard behavior; disabling intended Agent selection as a shortcut.
RationaleArtifact: RETURN.md R1, browser diagnostic references and immutable input inventories.
IndependentVerifier: This fresh read-only source reviewer, independent of the implementation author.
EffectStatus: HELD for implementation acceptance. The review judgment is actual; no product, lifecycle, dependency or publication effect is applied.
PreservedGates: Bounded remediation, fresh full-diff review, final registered checks, browser/native proof, manager fan-in and CHANGE/publication authority.

Ontology: A retained message's author is distinct from the currently selected persona and from the conversation's folder binding.
Epistemology: R1 follows directly from inspected construction/rendering and supported Agent switching; browser evidence is attributed to its executing specialist with its limits retained.
Praxeology: Repair local message attribution, verify the persona transition, diagnose the separate expansion input observation, freeze again and obtain fresh review.
Axiology: Preserve trustworthy authorship and user input while keeping the intended live Agent control.

Actual execution: Codex native descendant; Agent2 TASK role instruction-asserted; no delegation. Exact model/provider identifiers and token/context metrics are unavailable and not inferred. No substitution occurred. Source writes: none. Evidence writes: source-review-04 only. Read commands, hashing/inventory helpers and the registered validate_change_scope.py/select_affected_checks.py review tools were used. One optional scope-section extraction helper failed on a missing heading and made no source change; subsequent targeted reads located the applicable clauses. No runnable product proof is claimed.
