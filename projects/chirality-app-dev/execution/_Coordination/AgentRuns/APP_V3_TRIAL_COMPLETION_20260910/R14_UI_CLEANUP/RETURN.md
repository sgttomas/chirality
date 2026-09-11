# R14 UI cleanup return

Status: bounded implementation complete; pending parent integration and independent review. Derivative repair evidence, not authoritative decomposition or release acceptance. Upstream basis and context hashes: BRIEF.md / context.json. No pointer updated.

Changes:
- Codex shell disables local-model probes on mount, refresh, and daemon actions, and guards activation. Compatibility controller defaults retain local-model behavior. Hosted Settings excludes API-key component entirely; standalone compatibility panels remain.
- Workflow heading is now Workflows. Library disclosure contains workflow/skill/legacy views; bundled skills remain read-only, legacy methods are absent from ordinary discovery, compatible legacy workflows remain explicitly selectable. Central/category/search/inspection and qualified identity remain. Raw metadata is in Technical details disclosure.
- Footer omits unavailable activity/duration instead of announcing missing telemetry; valid observed counts/duration, running state, reconnect and details are preserved.

Validation: 49 tests passed across six focused files: method-library-view, activity-strip, activity-view-local-state, runtime-settings-reconnect, runtime-settings, settings-view-codex. First five-file run passed 48; new settings-view test passed 1 separately. One initial test-file write used the wrong working-directory prefix and failed without creating a file; corrected before testing.

Frontend npx tsc --noEmit --incremental false was executed and failed only on concurrent owner paths: chat-panel.tsx native-plan.revised union comparison; selected-session-replay-lens.tsx TranscriptItem.attachments and inferred map argument types. Reported to parent. Parent must rerun integrated typecheck after siblings finish. No build, packaged/native/live checks executed per brief.

Turn instruction-basis clutter belongs chat/replay authors; parent notified. Parent approved the sole shell-frame controller option edit; other shell edits are sibling-owned. Final closure requires parent frozen-diff review, integrated deterministic checks and requested next native trial. No commit/push performed.
