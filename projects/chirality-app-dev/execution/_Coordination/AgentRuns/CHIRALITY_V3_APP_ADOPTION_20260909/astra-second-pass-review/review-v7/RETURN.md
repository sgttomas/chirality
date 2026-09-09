# Independent Astra Section 4 App review — terminal V7

Verdict: **PASS for the exact reviewed App UI/transport scope; zero remaining actionable App findings.** This closes the App findings below. It does not close the separate Runtime enforcement review or establish a qualified native adapter, supplier behavior, a packaged desktop build, or release approval.

## Exact subject and independence

Base commit: `c16812685831a1cae3d44bf478d08b033c605c3a`.

Freeze: `UI_SOURCE_FREEZE_v7.md`, SHA-256 `240a974e9e6a0c9317ea77b9588997adf2d03b613bfd78595ee1a8c3c5405a80`, 8,682 bytes. All 48 listed postimages matched at entry and terminal verification. `SUBJECT.json` contains exact expected/actual hashes; `source/` retains the reviewed postimages and base diffs; `COVERAGE.json` records complete coverage of each postimage and base diff. New untracked files were reviewed in full as additions, hence their Git working-tree base-diff files are empty. Coverage is cumulative across the full V4 review and successive V5–V7 reviews, with unchanged postimages carried only after exact hash verification. The entire shared stylesheet and the retained compatibility code were included, not only added lines.

The reviewer independently inspected the implementation, proxy/RuntimeClient path, tests and saved visual evidence, reproduced defects, and tested their corrections. Prior PASS labels and test totals were not treated as proof of user intent. No product source was written and no delegation was performed. Earlier failed evidence remains separate under the original review directory, `successor-preflight/`, `review-v5/` and `review-v6/`.

## Findings closed against V7

The complete preserved independent counterexample set passes: **10/10**, in `counterexamples.log`.

| Concrete case | V7 result |
|---|---|
| Completion must retain methods selected for the next message while the earlier turn runs | PASS |
| Same-chat role change must retain unsent text, attachments and method references | PASS |
| Actual Methods Refresh must issue another catalog request after failure | PASS |
| Rejected first method-bearing turn must retain retry references | PASS |
| Agent-driven selection revision must become the next local CAS basis | PASS |
| Canonical-root synchronization followed by reopening must recover the session draft | PASS |
| Historical assistant answer must not acquire the latest role's attribution | PASS |
| Successful selection PUT followed by stream failure must retry with the updated revision/basis | PASS |
| Successful first turn must consume the unbound key so New chat cannot resurrect the sent method | PASS |
| Failure must retain an explicit newer removal to an empty next-message method set | PASS |

The original approved-continuity gap is also closed on the App side: compatible direct-entry V3 records expose Continue, preserve their Runtime session ID and canonical root, recover their own draft, restore transcript and recorded instruction history, and send another turn without create/boot. Historical role attribution comes from the turn-linked recorded instruction basis; absent that evidence the assistant label is neutral. Unsupported legacy/untyped/TASK records remain inspectable without being offered as new direct-entry execution.

## Approved intent assessment

The default conversation enters HELP_HUMAN and permits the other two direct roles. Legacy entry routes render the same conversation surface. Visible ladder/progression controls and persona terminology have been removed from this surface; retained metadata and compatibility code do not create a second launch path.

The Methods panel and adjacent composer control support catalog search, central-method ordering, concise applicability descriptions, source-qualified identity, inspection, ordered selection and removal. Instructions and files remain ordinary message inputs. Selected methods do not change the role or launch a manager automatically. Eligible roles and recorded supplied entries are inspectable; resource-load records are not presented as workflow completion.

Invoke/combine/stop/change semantics are coherent across the reviewed App and relevant Runtime service code: composer additions use selectionMode=merge; turn requests omit method overrides; active methods persist through ordinary messages and agent additions. Explicit replacement, including replace with an empty list, is the Runtime stop/change operation at a permitted boundary and may be coordinated by the agent following ordinary human instructions. The UI labels Use next message and Methods for next turn describe draft references. Removing a composer/library reference edits that next-message request; it does not claim to stop an already active method. Section 4 does not require a dedicated active-method stop button or a workflow tracker, so none is invented as a review requirement.

Native Plan execution is separately capability-gated and permission controls remain separate. Unavailable native support still permits ordinary planning in chat. App history components request and display recorded plan revisions without checking current execution capability, and the primary chat supports explicit project-relative export and an overwrite confirmation. Actual adapter admission and durable Runtime plan history/export semantics remain the Runtime review's responsibility.

Project and selection request cancellation/generation guards, permission-session binding, folder mismatch states, failed-send recovery, same-session role transitions and draft identity were inspected. The file-reference path remains contained/clickable with document viewing and the default-app PDF handoff. Basic attachment selection/removal and transport remain intact. No extra requirement that every composer attachment chip itself open a file is imposed.

## Validation and limits

Independent terminal checks: ten counterexamples PASS, plus nine focused product test files / **55 tests PASS**, including the real Unix-socket RuntimeClient/App proxy integration fixture, replay/native-plan presentation, failed-send state, method catalog refresh and revision/merge behavior. The 50 inherited scaffold tests filtered by the counterexample name expression are not product skips. The replay revision fixture was corrected before terminal testing to include the real `chirality.session/v3` discriminator; its scenario and assertion were unchanged.

Manager-reported V7 checks: focused 70/70; full frontend 1,993 PASS with four registered skips; frontend/Electron typecheck PASS; diff check PASS. These are supporting manager evidence, not represented as independently rerun full-suite results.

Saved settled desktop method/composer/inspection and same-session role-transition images were visually inspected. Narrow unavailable-state evidence and responsive/accessibility structure were reviewed. The later parent continuation fixture proved reopen → same session → next turn → four retained transcript items, and actual Refresh generated another GET. Its clipped/stacked IAB screenshot is behavioral evidence only. The earlier demoted fullPage capture is not used for visual acceptance. V5–V7 changed continuation/draft behavior, with no styling/layout changes from the settled V4 presentation. There was no fresh packaged Electron or live-provider visual run.

Controlled fixtures are hand-seeded. They exercise App presentation and production App transport, not the production resolver's authority decisions or supplier execution. No credentials or live supplier were used. The Runtime service's no-registry plan-history return and current-qualification export checks were explicitly routed to Root for Runtime review; this App PASS does not certify the deeper native-history/qualification seam.

## Handoff

This is a derivative review evidence package, not authoritative decomposition truth. App review closure is PASS on V7 exact bytes. Root/UI manager may consume this return alongside the separately accepted Runtime and governance evidence. Any listed source change requires a new exact subject and relevant backcheck; native/supplier qualification requires its own evidence. All reviewer test processes ended normally; no fixture server or provider process was left running by this reviewer.
