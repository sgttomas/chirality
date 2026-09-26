# Receipt — APP-TRANSITION-FORMS-2026-09-26

Derivative account. The [work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md)
(rows FU3 and FU4) carries execution, and the sources below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-26, Claude Code
conversation, on the parent session's D1–D4 recommendations and work plan:

> D1 and D2 as recommended, D3 (a), and D4 yes proceed that way. Your work plan is approved.

As the parent session relayed it, this run is item 3d of the approved plan:

- **FU3.** The Workbench and Pipeline transition forms gain inputs for the
  human-ruled `CHECKING -> IN_PROGRESS` reversal (`ruling` plus `approvalSha`),
  the `ISSUED -> IN_PROGRESS` reopening under an accepted amendment (`amendment`
  plus `approvalSha`) and the optional ruling on the forward gates, with
  D-APP-36 render evidence.
- **FU4.** The DEL-07-04 `ScopeOfWork.md` verification sentences (CLM-003,
  CLM-008) describe the implemented reversal and reopening gates.

During the run the parent session added review follow-ups for the 3a candidate
(`f33291f90`, run `APP-AMENDMENT-REOPEN-2026-09-26`) and for the Runtime
descriptor change (FU2, PR #978). They are listed under Result.

## Result

- **Forms (FU3).** `frontend/src/lib/workspace/deliverable-api.ts` gains
  `lifecycleTransitionTargets` (forward targets, then the reversal from CHECKING
  or the reopening from ISSUED), `lifecycleTransitionEvidence` (which of the
  approval SHA, `ruling` and `amendment` a transition requires or accepts, per
  App SPEC §4.3), option labels (`IN_PROGRESS (ruled reversal)`,
  `IN_PROGRESS (amendment reopening)`) and `lifecycleTransitionErrorMessage`.
  The new `frontend/src/components/pipeline/lifecycle-gate-fields.tsx` renders the
  inputs and the help note, and both forms use it:
  - `Ruling record (required)` on the reversal; `Ruling record (optional)` on the
    gates into CHECKING and ISSUED; hidden elsewhere.
  - `Accepted amendment (required)` on the reopening; hidden elsewhere.
  - Human gates lock the actor to HUMAN, as before. Submission stays disabled
    until the approval SHA and any required ruling or amendment are present.
  - Only the inputs shown are sent, since the API refuses a ruling or amendment
    on other transitions. Both fields are cleared after a successful transition.
  - The help note, linked to the inputs by `aria-describedby`, says the actor is
    asserted by the caller, that the App checks format, location and content,
    not that a human acted, and that `tools/scaffolding/write_status.sh` is the
    anchored check. The reversal and reopening each add one sentence on what
    they need.
  - Refusals are shown in a `role="alert"` paragraph as `CODE: message`. For
    `AMENDMENT_NOT_ADMITTED` the text names the checker code from the API
    details (`AMENDMENT_NOT_ADMITTED (checker code REGISTER_SCHEMA): …`). Known
    refusal codes (the mapped `RULING_*` and `AMENDMENT_*` codes,
    `INVALID_AMENDMENT_REFERENCE`, `HISTORY_NOT_PRESERVED`,
    `INVALID_STATUS_FORMAT`, approval-SHA and backward codes) add a short hint
    and "_STATUS.md was not changed."; each is raised before the file is
    written. The ruling-resolution codes `RULING_NOT_FOUND`,
    `RULING_OUTSIDE_PROJECT_ROOT`, `RULING_IS_STATUS_FILE` and `RULING_EMPTY`
    have no hint and show as the plain code and message.
- **Post-write check (3a review item 1).** `applyLifecycleTransition` re-parses
  the written content and refuses the transition (`INVALID_STATUS_FORMAT`,
  new in `TransitionErrorCode`) unless it reads as the target state, with the
  transition date as `Last Updated` and exactly one more history entry. The
  writer splits lines only at LF and CRLF; the parser's `^`/`$` also match at a
  lone CR, U+2028 and U+2029. A header line such as `note\r**Current State:** …`,
  with a second Current State line in a trailing section, made the writer edit
  the trailing line while the parsed state stayed unchanged. Tests cover the CR,
  U+2028 and U+2029 cases and check that the file is left unchanged. App SPEC
  §4.3 states the check.
- **History safety-net tests (3a review item 2).** New tests refuse
  (`HISTORY_NOT_PRESERVED`) metadata that would overwrite a field line carrying a
  reopening marker, and a reversal whose removal of `Checking Approval SHA` would
  drop one. A test covers replacing the lone `-` history placeholder.
- **3a record nits (items 3 and 4).** The 3a receipt now counts 698 tracked files
  ending in `_STATUS.md`, of which 689 are named exactly `_STATUS.md`. Its Limits
  add the three in-place writer limits (content below `## History` is not
  managed; table rows go after a trailing paragraph; a fenced `## ` line counts
  as a heading). The 3a manifest's "Known limit. The status file" is capitalized.
- **FU2 review item 1.** `tool-descriptor.test.ts` gains a separate test that the
  `dependency_read` (`deps_read`) descriptor description equals the live MCP
  `deps_read` description from `buildChiralityMcpTools`. On this base
  (`f33291f90`) the two differ ("Dependencies.csv." against
  "Dependencies.csv file."), so the test fails here by design. At the integrated
  tip `26fdb18d6`, after #972 and FU2, both strings are identical. A positive
  control, with the live text temporarily set to the base descriptor text,
  passed and was reverted.
- **FU2 review item 2.** Runtime Receipt 4 does not exist on this base, so the
  corrected evidence line was applied by the parent session at integration
  (PR #980).
- **FU4.** DEL-07-04 CLM-003 and CLM-008 name the verification hooks
  (`lifecycle-status.test.ts`, `amendment-reopen-parity.test.ts`,
  `deliverable-contracts.test.ts`, and for the forms
  `lifecycle-transition-gates.test.tsx`). They describe the implemented App SPEC
  §4.3 reversal and reopening gates. Actor identity and accepted schema fixtures
  stay open, and `write_status.sh` stays the anchored check. No requirement text
  changed.
- DEL-07-04 MEMORY, work-graph FU3 and FU4, `loop/LOOP_RECEIPTS.md` Receipt-268
  and the tranche manifest
  `docs/governance_harness/tranche_manifests/APP-TRANSITION-FORMS-20260926.yaml`.

## D-APP-36 render evidence

D-APP-36 (`execution/_Coordination/_DECISIONS/D-APP-36_RULING_2026-06-21.md`;
`docs/ISSUE_READINESS_PROFILES.md` §4) requires component render tests of
user-facing controls, state and disabled/active behaviour. It requires browser
or screenshot checks only where layout, viewport, overlap or interaction risk is
high. Prior receipts met it with `renderToStaticMarkup` tests
(`DEL-02-02/_run_records/TASK_RUN_2026-07-19_DAPP56_R4_P28_pipeline_transition_render.md`).

Produced:

1. **Component render tests.** `workbench-surface.test.ts` and
   `pipeline-surface.test.ts` (static markup) cover:
   - the reversal: option label, required ruling input, no amendment input,
     actor lock, disabled submit, and the help note linked by
     `aria-describedby`;
   - the reopening: required amendment input, no ruling input;
   - the optional ruling on both forward gates, with submit active;
   - an ordinary transition with no gate inputs and no note;
   - a refusal rendered as `role="alert"`.
2. **Interaction tests.** `lifecycle-transition-gates.test.tsx`
   (react-test-renderer) mounts the full `WorkbenchSurface` and `PipelineSurface`
   with a mocked status API. For each surface it:
   - selects the reversal and checks that submission waits for the ruling;
   - submits, and checks the exact API payload (HUMAN actor, trimmed ruling, no
     amendment);
   - sends the optional ruling on the gate into ISSUED;
   - submits the reopening and shows `AMENDMENT_NOT_ADMITTED` with its checker
     code as an alert;
   - shows `HISTORY_NOT_PRESERVED` as an alert.
3. **Browser layout check.** `render/render_forms.tsx` renders four form states
   to static HTML with the App's `globals.css`: the reversal filled, the
   reopening refused, the reversal empty and the forward gate into ISSUED.
   Headless Chromium 141 screenshotted each state at 1000 px (two-column grid)
   and at 500 px (single column). The commands, input hashes, HTML hashes and
   PNG hashes are in `render/MANIFEST.json`, and the PNGs are in `render/png/`.
   The input hashes were taken at the pre-integration commit `cebb0da1b`; at
   the integrated candidate the three inputs differ only by #972's dependency
   summary code, and an independent review re-bundled the renderer at the
   candidate and reproduced all four HTML hashes and all eight PNG hashes.
   An agent inspected all eight and found no overlap, no clipping of labels or
   controls, and no hidden required control. Long values scroll inside their
   inputs. One finding was fixed: the first option labels
   (`IN_PROGRESS (reversal under a human ruling)`) were cut off in the
   two-column select, so they were shortened.

Missing, and why:

- **No render in the running App.** The forms are not mounted in the live App.
  Every route renders `WovenDialogueRoute`, which discards its `legacy` prop, so
  `LoopTertiaryShell` and its Pipeline and Workbench tabs never render. The
  `RUN_D128_CONCORDANCE_2026-09-21_1614Z` DEL-01-01 errata record the Workbench
  form as retired-unmounted (`REACH=LEGACY_ONLY`).
  So the changed forms cannot be exercised in the Next.js App or in the
  packaged desktop App, and no native evidence exists. The packaged App is also
  not available in this container.
- **No human visual check.** The screenshots had an agent's inspection only.
  The IBM Plex fonts that `next/font/local` supplies were not loaded, and system
  fallback fonts rendered.
- **Headless width floor.** Headless Chromium lays out at least 500 CSS px wide.
  A first 420 px capture clipped a 500 px layout; it was discarded, and the
  narrow captures use 500 px.

The FU3 D-APP-36 item is left **open** for the App loop, which decides whether
the component and static browser evidence suffice while the forms stay
unmounted, or whether mounting them is required first.

## Checks (worktree candidate)

Recorded in the hand-off to the parent session, with exit codes: typecheck;
focused and full Vitest; the Root validators G0–G3, receipt, tranche-manifest,
conflict-marker, run-record-leak and whitespace checks; export regeneration; the
APP-HOLD dispatch check for DEL-07-04. The full Vitest run has two expected
failures. One is the known uid-0 `harness-attachment-resolver` failure. The
other is the new `deps_read` description test, described above.

## Limits

- The forms are unmounted legacy surfaces in the live App (see above). This run
  neither mounts them nor changes the woven shell.
- The actor is caller-asserted. The forms force HUMAN on human gates, but that
  is a UI default, not identity (DEL-07-04 REQ-005, P-07/P-14). The App's
  reopening check is unanchored; `write_status.sh` is the anchored check.
- The post-write check refuses a file the writer would edit differently from the
  parser's reading. It does not make such a file transitionable; the human
  repairs its line breaks. It also refuses a table-format history whose new row
  cannot be written as a table row (a `|` in a cell, such as in a ruling path);
  a test covers it. The list-line fallback there would have hidden the table
  history from the parser.
- The new `deps_read` description test fails on this base until FU2 and #972
  are integrated; at the integrated candidate (PR #980) it passes, and the only
  full-suite failure is the known uid-0 `harness-attachment-resolver` case.
- Work-graph FU2 and FU3 rows are adjacent, so integrating this commit after the
  FU2 commit (`8b4a0dd6e`/`c94ab79a7`) may need a trivial merge of those two
  table lines. The same applies to `exports/chirality-app/*`, which is
  regenerated after integration.
- No lifecycle transition, approval-SHA refresh, authority-corpus repin, Runtime
  change, release or issuance.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at the
dispatching session's instruction; the commit's session trailer identifies the
run.
