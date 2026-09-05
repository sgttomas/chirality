# D-APP-36 render review — T1 revision2

Reviewer: WORKING_ITEMS pkg02. Parent HELP_HUMAN independently inspected final 1440-light and 960-light replay screenshots and confirmed metadata readable and primary visible beside replay (runtime parent message, 2026-09-05). This is agent visual review, not an owner act or live-account proof.

Final evidence: attempt-4/result.json PASS, 11 observation groups, no browser pageerrors, Chromium148.0.7778.96. Canonical script, input fixture and reviewed source manifest are copied into attempt-4 before execution. COMMANDS.json records executable, arguments, cwd, effective overrides, versions, exit and rerun; CLEANUP.json records browser closure, owned server termination and host port refusal.

All six screenshots were opened and inspected with view_image:

- replay-1440-light.png and replay-1440-dark.png: primary composer visible beside the Session lens. Source identifier wraps into ordinary readable lines, Observed/Disclosure/Currency/counts and Persona are readable stacked blocks. Long source/event text stays in the scrollable panel. No focused Workbench/Pipeline mount or navigation entry.
- replay-960-light.png: narrow panel preserves readable provenance and persona; composer remains visible and focusable. Existing compatibility-footer link clipping is unchanged baseline, outside this T1 repair.
- chat-960.png: primary dialogue and recorded Agents projection visible; no Work projection.
- workbench-960.png: retained URL renders real Workbench context, contract controls and Documents block through the existing legacy shell.
- pipeline-960.png: retained URL renders real DECOMP/PREP/TASK/AUDIT controls and scaffold form through the existing legacy shell.

The browser checks the same DOM composer node, enabled/visible status and document.activeElement through replay selection, theme switching, keyboard resizing, coordination collapse/reopen and return. It checks actual route responses and legacy content, not screenshot existence alone. Intercepted APIs and console messages are retained: 503 console entries correspond to deliberately unavailable unrelated fixture APIs; no page-level JavaScript error occurred. The fixture is recorded-session presentation only and does not execute a runtime turn or validate legacy dispatch execution.

Earlier attempt-3 visual verdict: FAIL. Metadata used full-width two-column styles inside the narrow panel and wrapped source values one character per line. This defect triggered AUTHOR_AMENDMENT_v1.2, fresh source review and rebuild. A separate exact accessible-name mismatch for the collapsed control was repaired in the script using the observed stable region toggle and text assertion (CSS adds a plus pseudo-element). No app behavior was changed to satisfy that locator.

Closure: render requirement satisfied for this frozen T1 revision; repeat after any changed source affecting layout, focus, replay mounting or responsive widths. Parent shared gates and premerge/PR-CI disposition remain separately owned.
