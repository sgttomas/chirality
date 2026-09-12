# R16 direct functional trial

In progress. Actual signed Stage25/R16 App, source 70a02f74f1c1d7246539d689090362021b972055. Lead uses Computer Use and ordinary synthetic output files; no protected live account/session/event files accessed. Existing R15 findings remain historical evidence. No new build requested.

## Observed passes

- Owner completed browser OAuth/2FA. App account menu reports OpenAI signed in / Ready to work. Runtime started automatically after folder selection.
- First HELP_HUMAN chat with gpt-5.6-sol / low completed the requested exact response `R16 ready.` and returned to Idle. Ordinary history excludes hidden boot prompts.
- Explicit native shell request `/bin/cat README.md` completed with reported exit 0 and created `r16-shell-report.md`. Lead independently read the synthetic output: heading plus accurate description of the R6 scratch trial and date. No read fallback requested or reported.
- Collapsed right sidebar, then clicked the inline report link. Sidebar reopened to the rendered report with correct content. One stale accessibility element after collapse was refreshed; that automation error is not a product failure.
- Attach files opened the native picker. Selected actual `trial-diagram.png`, observed removable composer chip, sent a content question, received `A solid red square.` Image reference persists in ordinary transcript. Turn returned Idle.
- Commentary paragraphs and final report/link appear as separate blocks rather than concatenated text.

## Pending

Post-restart owner test FAILED; bounded diagnosis and UI repairs are in progress. Plan, second-chat, interruption and pre-restart history results are recorded below. Native tool-event coverage remains a disclosed limitation. No overall trial acceptance or publishing approval inferred.

## Native Plan Mode

PASS: actual source-grounded native plan revision 1 appeared with read-only status. Revise in chat populated the composer; requested Sources section produced revision 2 and an Earlier revisions (1) control. Synthetic output did not exist before execution. Execute plan populated the exact revision 2 in the composer and switched interaction mode to Chat; sending completed the task and returned Idle. Lead read `r16-plan-report.md` directly: correct project description, consistency finding and Sources section containing both input filenames. Plan remains inspectable after execution.

Limitation observed during execution: agent reported Git status unavailable because developer tools were inaccessible, then verified the synthetic file content directly. This does not establish why Git is inaccessible; no host installation diagnosis or general development-tool qualification is inferred. The requested knowledge-work artifact was completed.

## Second chat, interruption and pre-restart history

PASS: new HELPS_HUMANS chat selected actual catalog gpt-5.6-terra / medium, booted and answered the first user request. UI retained role/model/effort; first chat used gpt-5.6-sol / low. No timeout occurred, so timeout-retry branch remains unexercised natively.

PASS: instructed `/bin/sleep 47`; lead observed actual sleep PID13052/parent12987 before clicking Interrupt. App returned Idle; the same narrowly filtered process check found no matching sleep. A fresh native README-read turn then completed accurately with account still Ready. No account reset, forced signal or fencing change.

Usability finding: interruption leaves the last commentary in transcript with no clear interrupted marker. Turn details exposes instruction basis, not terminal status. Functional recovery passes; visible cancellation status merits source inspection with the rest of the batch.

PASS: reopened first chat through history. Text, image reference, correct HELP_HUMAN/sol/low selections, current native plan revision 2 and expandable unchanged revision 1 all remain. No hidden bootstrap text in ordinary transcript.

Usability finding: selecting a chat replaced the open document sidebar with an Agents/Session breadcrumb and `Select a recorded session to inspect its replay.` empty state. Main chat loaded correctly; inspect whether this sidebar transition is intentional or an obsolete detail route.

## Guarded restart

Normal CmdQ closed GUI10625; existing daemon10666 remained. Same R16 launcher guard PASS. Relaunched only through the guarded launcher (execution session30123); exact GUI13417 and daemon10666 observed. Computer Use attachment to the exact verified App path timed out. No repeated restart or protected live-state read attempted. Owner asked to inspect both chats and send an exact short follow-up. Process existence alone does not establish responsive GUI or successful post-restart execution.

Operational caution: avoid broad Computer Use surface inventory during OAuth follow-up because provider browser URLs can contain authentication parameters. Do not reproduce or persist those URLs. App-only observations are sufficient for this trial.

Bounded App-only author follow-up dispatched under R16_UI_FINDINGS/BRIEF.md for interruption labeling and unintended empty session sidebar. No rebuild; independent source review follows.

## Owner post-restart observation — FAIL

Owner tried the requested actual follow-up and reported:

> Harness Request Failed (ENGINE_UNAVAILABLE)
> ENGINE_UNAVAILABLE: Runtime v2 admission is missing, invalid, stale or no longer live
> Review the request context and retry.

Owner also reported inability to scroll to the other chat’s composer. This establishes a real postrestart execution failure and a long-chat scrolling defect; the earlier Computer Use attachment timeout is no longer the only outstanding restart observation. It does not establish the internal admission reason.

R16_RESTART_ADMISSION/BRIEF.md dispatches bounded source/controlled diagnosis to r13_second_turn_diagnosis (Astra medium). Scrolling is added to r14_ui_cleanup's App-only batch. No further owner retry requested, no live account state access or weakening, no new build. Core pre-restart passes remain valid but overall trial readiness is blocked by restart admission and inaccessible composer.
