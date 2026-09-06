# Independent complete source review — BLOCK

Reviewed all 25 source/test members of SOURCE_MANIFEST_v4.json (SHA256 `3ca05c1e6187478b345d658e0039ada1eedc0cdba862da9496ca592bd39a0c93`) and the complete diff from `e00238621db7a00b036245962c21e3fc6ed75452`. All 25 hashes match before and after; independently reconstructed unified diff matches the supplied patch exactly. The full input inventories are preserved beside this return. APP-HOLD dispatch preflight is ALLOW for DEL-02-01/03/04. Scope validation passes; semantic review finds every product change inside the sealed author locus. This is derivative review evidence, not accepted decomposition truth or lifecycle acceptance.

## R1 — P2: Keep legacy Working Root changes effective

Location: `frontend/src/components/shell/chat-panel.tsx:330–362`, especially the new session creation argument at line 334 and unconditional conversation binding at line 362. Related draft selection: line 197.

The new enduring conversation binding is applied even when `presentation` is omitted. Existing compatibility callers `loop-shell.tsx:44`, `loop-tertiary-shell.tsx:45`, `portal-loop-shell.tsx:50` and `app-shell.tsx:357` still mount plain `<ChatPanel />`; their ShellFrame leaves Working Root controls enabled and supplies no New chat request. The `/chat?legacy=1` route explicitly selects LoopShell.

After a completed legacy turn in root A, change Working Root to B using its supported header control. The root-change effect invalidates activeSession, but never clears conversationBinding. The next createHarnessSession call therefore receives the old bound root A instead of selected root B. Its returned root also gets checked against the old binding. Meanwhile the header and file picker show B and draftStorageKey stays tied to A. Clearing the root does not reset the binding either. The user cannot start the intended B conversation without reloading the legacy surface.

This is a regression introduced by this diff, not a request to add new legacy capabilities. Before this change, session creation and draft storage both used the current provider projectRoot. It violates the sealed brief's compatibility preservation and DEL-02-01's surviving compatibility obligation.

Keep the woven conversation binding, canonical synchronization and selected-root draft isolation, but scope them to the woven presentation or explicitly reset them on legacy root transitions so plain ChatPanel retains its existing current-root behavior. Add a default-presentation regression: complete a turn in A, select B, verify the next create request uses B and drafts use B's key; include clear then select another root. Keep the existing woven persona-change and canonical-root tests passing. The new binding test fixture always mounts `presentation="woven"`, so it does not cover this compatibility branch.

## Reviewed coverage and limits

The v4 historical-speaker repair captures persona at assistant message creation and renders each retained message's own origin for label and tooltip. The expansion repair removes ancestor input capture, writes the draft before the activated restoration callback, and defers restoration while composing. Its component tests cover two personas, first input, paste and composition ordering. These repairs have no additional actionable source finding; actual browser keyboard/IME proof remains separately required.

Reviewed ShellFrame's single-return callback, reconnect ownership and in-flight guard, settings trigger anchoring, Escape/outside dismissal and theme reachability; the single primary ChatPanel and replay identity; woven canonical synchronization, stale boot/apply checks, first-message binding, pending selector/native/drop guards, persona transitions and explicit local New chat; document/file-tree integration, right-panel keyboard/menu/control behavior, geometry/default and saved-state compatibility, removal of activity height writers, scoped Stone presentation, Activity session-separated projections and local version-based Clear/filter behavior. Existing pure stream list exports and semantic ownership remain unchanged.

Reviewed all native additions and tests: sender checks precede recent registration; canonical directory and instruction-root checks reuse existing policy; the macOS menu retains standard Edit/View/Window roles; GUI open-file retains one bounded intent and validates delivery origin; the renderer still applies folder selection policy; preload exposes only payloads and removes the exact listener. No recent-list startup clearing, runtime authority, provider or file-policy edit was introduced. Native receiver delivery, Dock/Open Recent integration and isolated app identity proof remain execution gates, not claims supplied by this source review.

Affected-check selection lists frontend-test, frontend-typecheck, app-hold-integrity and harness-self-check. The sealed brief additionally preserves final build/premerge, browser and native obligations. No test suite, build, browser, server or native process was run by this reviewer. Prior test passes and previous partial source passes do not establish final validation. T4 weaving, T6 organisation/account, historical per-chat Reveal, no-folder capability and D121 remain explicit residuals. No additional actionable source finding was identified.

## Decision and attribution

OwnerStandingApproval: D-APP-64 §3
AgentJudgment: REJECT_FOR_REMEDIATION
SelectedOutcome: BLOCK full source fan-in until the legacy root regression is repaired and a fresh complete review passes.
JudgedBy: TASK software-code-review /root/shell_pkg02/source_review05
OwnerCaseSelection: NONE
RejectedAlternatives: Accepting a visible root that differs from the next creation request; removing legacy root controls; weakening woven binding to repair a compatibility branch.
RationaleArtifact: RETURN.md R1, INPUT_INVENTORY.json and FINAL_INPUT_VERIFICATION.json.
IndependentVerifier: This fresh read-only source reviewer, independent of the implementation author.
EffectStatus: HELD for implementation acceptance. The review judgment is actual; no source, dependency, lifecycle or publication effect was applied.
PreservedGates: Bounded author remediation, fresh full-diff review, final registered checks, browser/native proof, manager fan-in and CHANGE/publication authority.

Ontology: Woven per-conversation folder binding and the legacy mutable Working Root are distinct interaction contracts.
Epistemology: The finding follows from actual default callers and inspected changed state/creation paths, not inferred runtime execution. All frozen hashes and the full diff were independently verified.
Praxeology: Isolate the new binding semantics from the legacy branch, prove both transitions and refreeze for fresh review.
Axiology: Keep the selected folder, request context and saved draft identity aligned without weakening woven safeguards.

Actual execution: Codex native descendant; Agent2 TASK role instruction-asserted; no delegation. Exact model/provider identifiers and token/context metrics are not exposed and were not inferred; no substitution. Source writes: none. Evidence writes: source-review-05 only. Used direct reads, hashing/diff inventory helpers, and registered validate_change_scope.py/select_affected_checks.py. One glob read and one guessed preflight filename failed without side effects; subsequent exact-path reads succeeded. An unbounded mock-text search included embedded asset text; subsequent extraction omitted assets and bounded individual lines. No executable product proof is claimed.
