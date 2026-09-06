# Independent source review — BLOCK

Reviewed all 24 source and test members of `integration-01/SOURCE_MANIFEST_v2.json` (SHA-256 `e0db67285c8ee327ba981069f49e33986a687d9efb14c6a086c75f54ef9de8e1`) and the complete `SOURCE_DIFF_v2.patch` from committed baseline `e00238621db7a00b036245962c21e3fc6ed75452`. Before and after hashes match every member. `scope-check.json` passes against the declared source paths; semantic scope inspection found no out-of-locus source edit. APP-HOLD reliance passed for DEL-02-01, DEL-02-03, and DEL-02-04.

## R1 — P1: Preserve the conversation folder lock across an agent change

Location: `frontend/src/components/shell/chat-panel.tsx:799` (also lines 202–213, 263–265, and 286–296).

After a completed first turn, the Agent selector intentionally remains enabled (line 800). Selecting another agent updates the route through `PersonaPicker` (`persona-picker.tsx:80`), and the existing context effect clears `activeSession` because its persona no longer matches. The new folder selector, parent binding notification, and native intent guard all use that runtime-session object as the sole completed-chat lock. They consequently return to the unlocked state even though `messages` still contains the populated conversation. The user can now select another folder through the composer, Files picker, or a native open/drop intent without choosing New chat. This violates the accepted folder-fixed-after-first-message obligation and can send the next turn under a different root while the previous conversation is still displayed.

Keep the conversation's bound folder and locked state independently of the persona-specific runtime session cache. Reset that conversation binding through the explicit New chat path (or another separately authorized complete conversation reset), while preserving the existing rule that a changed persona may require a different session. All folder entry points must consult the enduring conversation binding; its label must retain the actual returned canonical root, including when provider synchronization failed. Do not fix this by disabling the agent selector permanently, since the accepted target keeps it live after a turn.

Required regression: finish a turn, change the route's Agent, and assert that the transcript and recorded folder remain stable, the composer still renders a fixed folder label, the parent reports locked, and both native intents and Files/chooser requests cannot change the root. Assert that explicit New chat releases the lock. Repeat with a selected subfolder whose boot returns a different canonical root and with a failed provider synchronization. The current binding tests hard-code `useSearchParams()` to an empty query, so they cannot exercise this transition.

## Review coverage and limits

- Traced the single-return ShellFrame seam and stable ChatPanel mount, reconnect handler ownership, settings/theme reachability, pending selector guards, canonical-root synchronization, draft storage identity, stale-result handling, new-chat reset, persona routing and permission submission.
- Reviewed all native additions: registration uses the existing sender policy and canonical directory validator; Open Recent uses native menu roles without startup clearing; preload removes privileged event objects, exposes bounded file extraction and subscription cleanup; open-file queues one validated intent. Actual Electron execution and isolated app identity proof remain separate mandatory evidence.
- Reviewed geometry writers and defaults, compatible saved-state readers, the fixed 32 px strip and removed activity-height writer, document presentation and menu handoffs, primary/replay identity, local Activity filtering/clear and session-qualified projection keys, accessibility names and keyboard handling, and all changed tests.
- No additional actionable source finding. Browser evidence, final registered suite, build/premerge and required native proof were pending at dispatch and were not run or claimed by this reviewer. Historical six-file PASS and prior host feedback are not final validation of these bytes. Scope closure for T6, T4, no-folder capability and D121 is not claimed.

## Decision and attribution

OwnerStandingApproval: D-APP-64 §3
AgentJudgment: REJECT_FOR_REMEDIATION
SelectedOutcome: BLOCK source fan-in until R1 is repaired and the complete revised frozen diff receives a fresh independent review.
JudgedBy: TASK software-code-review /root/shell_pkg02/source_review03
OwnerCaseSelection: NONE
RejectedAlternatives: Passing a folder lock that can be bypassed through the intended Agent control; removing the intended live Agent control as a shortcut.
RationaleArtifact: RETURN.md R1 and immutable input inventories.
IndependentVerifier: This fresh independent source reviewer; not the implementation author.
EffectStatus: HELD for implementation acceptance; this report records an actual review judgment and does not apply source, lifecycle, dependency, or publication changes.
PreservedGates: Remediation, fresh full-diff review, final registered checks, browser/native proof, manager fan-in and CHANGE/publication authority remain required.

Ontology: a conversation's folder binding is distinct from a persona-specific runtime session cache. Epistemology: the finding follows the inspected caller/state chain and accepted fixed-folder contract; no browser reproduction is claimed. Praxeology: a bounded author repair and regression precede another fresh review. Axiology: preserve predictable folder authority and the user's visible conversation without blocking supported agent selection.

Actual execution: Codex native descendant, Agent 2 role instruction-asserted, no delegation. Exact model and provider identifiers and token/context metrics are not exposed in this session and are recorded as unavailable. No substitution occurred. Source writes: none. Evidence writes: this directory only. Execution finished at 2026-09-06T04:04:41.642881+00:00.
