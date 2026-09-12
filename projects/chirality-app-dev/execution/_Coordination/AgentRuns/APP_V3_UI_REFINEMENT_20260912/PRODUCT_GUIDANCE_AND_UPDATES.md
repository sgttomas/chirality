# Product guidance and public updates

Owner continuation, 2026-09-12: make role instruction delivery work for primary
and delegated agents, implement the saved product AGENTS.md direction, use the
public chirality-app releases repository for updates, and rename the workflow
action to `Turn into workflow`. All instructions are open source. The distinction
between product and repository guidance is applicability, not confidentiality.

## Findings and implementation

The old package copied repository AGENTS.md. Primary role instructions were
supplied at thread start, but native role configuration had no production caller.
Changed guidance was appended as user text. Stock Codex 0.154 ignores developer
instruction overrides on an already loaded subscribed thread.

The product default now lives at `../../../../instructions/AGENTS.md`
(repository path `projects/chirality-app-dev/instructions/AGENTS.md`). Electron
seeds an editable App-owned `instructions/AGENTS.md`, preserves it across
upgrades, and offers Open and Restore default in Settings. Restore preserves a
backup. The packaged source remains inspectable. Native Codex continues to
discover applicable user/project instructions; Chirality does not duplicate
its project AGENTS chain or replace base Codex instructions.

Primary delivery contains common guidance plus the active role. Generated
content-addressed native role files contain common guidance plus one full role.
They preserve their captured bytes for existing work. User model, feature,
depth and permission settings are not changed. Fresh-context role delegation
is explained in product guidance because a full-history fork does not by itself
establish another role at this supplier pin.

Changed guidance requires confirmed idle unload followed by cold resume of the
same provider thread. Active descendants defer it. Actual provider-start
evidence references the resolved basis separately from merely resolved content.
The first native edit test exposed a two-second timing assumption: the supplier
defaults to a 60-second idle unload delay. The App-owned server now sets the
supported `thread_unload_delay_secs=0` process option. Only unsubscribed idle
thread caches are affected. Closure confirmation allows the supplier's shutdown
period and checks complete loaded-thread inventory if the notification is lost.
Failure remains `INSTRUCTION_ADOPTION_PENDING`, with retry-in-this-chat guidance.

After that timing repair, the existing chat still returned old guidance. Its
recorded root hash matched the edited file, so resolution was correct but did
not establish delivery. The stock supplier restores a reference context on
resume and only renders general developer instructions during full initial
context construction. Normal history diffs can therefore omit an edited
general developer message. The repair pairs the cold-resume configuration with
the supported `thread/inject_items` method, supplying an explicit developer
message before admitting the user's next turn. Acknowledged delivery and
resolved content are recorded separately; an uncertain acknowledgment leaves
the user turn unstarted. Native requalification passed as recorded below.

Public updates use an unauthenticated manual GET to
`https://api.github.com/repos/sgttomas/chirality-app/releases/latest`. The checker
rejects redirects and credentials, validates stable release identity and exact
repository destinations, chooses a matching Mac asset, and otherwise offers the
release page. Download remains a user-selected browser handoff. No automatic
installation, restart, or publishing is added.

## Source basis

- [Loaded-thread resume overrides](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L4237).
- [Idle unload, shutdown and closure notification](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/app-server/src/request_processors/thread_lifecycle.rs#L414).
- [Stock idle-delay default](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/config/mod.rs#L3828).
- [Fresh-context role application](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/tools/handlers/multi_agents/spawn.rs#L92).
- [Role developer-instruction replacement](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/agent/role.rs#L183).
- [Restored reference context](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/session/mod.rs#L1599) and [normal context diffs](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/session/mod.rs#L4294).
- [Supported model-visible item injection](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/app-server/src/request_processors/turn_processor.rs#L956) and [rollout flush before acknowledgment](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/codex_thread.rs#L608).
- [GitHub latest release API](https://docs.github.com/en/rest/releases/releases#get-the-latest-release).

## Parent verification so far

Native development instance used the existing approved isolated profile and
derived launcher, with the fresh source checkout and rebuilt Runtime. It did
not access R17 or any identity/auth/Codex-home file. Logs exclude lines with `@`.

- Primary received the temporary `AMBER-LARK-42` probe through product guidance
  and returned it without tools or file reads.
- One fresh TASK child received a brief without that answer and returned the
  same probe. The conversation displayed native task activity and completion.
  The model requested and displayed was gpt-6-astra/medium. Controlled tests
  separately inspect exact role config and primary/child supplied bytes.
- Initial edited-chat check failed after 2.23 seconds, prompting the stock
  unload-delay correction above. A second check after restart completed but
  returned old `AMBER-LARK-42` instead of edited `COPPER-WREN-54`. The recorded
  root SHA matched the controlled edit
  (`2488143634b8edff08664f0ccebdb81e1281e4f5dcd3adf7790ae64d09f4f4ca`).
  This was a failed qualification, leading to the history-delivery repair.
- With the history repair and rebuilt Runtime, the same chat answered
  `COPPER-WREN-54` correctly. A second controlled edit without restart supplied
  a new ALBATROSS-PROBE rule (root SHA
  `fb4d40795fa568763ca06507104bc5507e8aff56ed38e0a79bee685c1402b45a`);
  the primary returned `NAVY-FINCH-88`. One fresh native TASK child, with the
  expected answer excluded from its brief, also returned `NAVY-FINCH-88`.
  Native task activity and Completed were observed. Prior messages remained.
- Native Settings Restore default then removed the temporary rule, retained a
  backup, and disabled Restore. Parent compared only the newly authorized App
  instructions file with the source default and verified identical bytes.
- Native Settings displayed Open AGENTS.md and Restore default. Open returned
  without an App error. Restore required its ordinary confirmation, restored
  exact bundled bytes, disabled the restore button, and retained the test edit
  in a backup. No claim is made about a particular external editor.
- Native Check for Updates completed as up to date. The actual public stable
  release is v2.0.0, older than 3.0.0-rc.1. No download was attempted.
- Native Plan panel displayed `Turn into workflow` with the existing action.
- Owner added Report issue while the instruction repair continued. The link
  appears beside Details in the main footer. Native click opened Chrome at
  GitHub sign-in. After the owner completed sign-in, that same tab displayed
  Create new issue at `https://github.com/sgttomas/chirality-app/issues/new`,
  with empty title and description fields. The return destination worked.
  No report was submitted and no logs, account or conversation data were sent.
  At 760 px the existing stacked layout scrolls to its footer; the link and
  Details remain legible there, and Tab from the link focuses Details. The
  temporary viewport was reset afterward.

First full Runtime run: 331 passed, one old teardown failure. Its fixture used
raw daemon shutdown while claiming to emulate SIGKILL, which actually races
semantic cancellation. The corrected test uses production close ordering,
deliberately constructs stale persisted running state, and tests startup
recovery without claiming actual SIGKILL evidence. Its focused file passed
12 tests; the subsequent CI-worker full suite passed all 332 tests. Competing
raw-daemon cancellation paths are not claimed repaired.

First full frontend run: 2178 passed, four skipped, one exact prose pin failed.
Removed the comment-string requirement rather than restoring meaningless words
to satisfy it. Existing installer/filesystem prohibitions remain, and the
behavioral test now asserts checking never opens a browser until requested.
Those two test files passed all 32 tests. Final complete candidate checks and
independent review follow; historical failed results remain recorded here.

Complete candidate `95b342519`: Runtime 336 tests passed; frontend 2180 passed,
four skipped; both typechecks passed. Independent review of all 98 paths
returned one P2 for ordinary unpackaged launches selecting repository guidance
as the default; the native timing/history limit was separately disclosed.
The parent repaired explicit development, source-override, staged-override and
packaged default resolution. Nine store/wiring tests pass, including initial
seed and Restore default with distinct repository/product fixtures.

After the history repair and Report issue addition: Runtime TypeScript and all
342 Runtime tests pass; frontend/Electron typechecks and all 2185 frontend
tests pass, four skipped. Tests use the existing CI one-worker setting. The
history regressions separately model configuration and restored model-visible
history, acknowledgment ordering, failure/lost acknowledgment, retry, restart,
unchanged reuse and active-work exclusion. Prior failed evidence remains above.

No replacement build, owner install-over acceptance, notarization, or publishing
is established by this record.

## Delegated work and fan-in

All three specialist instances used gpt-6-astra/medium and did not delegate.
`product_instruction_audit` returned the production-path audit and pinned
source findings under `briefs/PRODUCT_INSTRUCTION_AUDIT.md`; its initial timing
recommendation was corrected after the native test, as recorded above.
`public_release_updates` returned its six-file implementation under
`briefs/PUBLIC_RELEASE_UPDATES.md`: 82 focused tests, final update tests 10/10,
and frontend/Electron typechecks passed. `product_instruction_runtime` returned
the implementation under `briefs/PRODUCT_INSTRUCTION_RUNTIME.md`, then the
bounded teardown-fixture correction and native delay repair: initial 51 focused
tests, 332 full tests after the fixture correction, and 42 distinct targeted
tests plus Runtime TypeScript after the delay/error repair. HELP_HUMAN read
the source returns and performed the direct checks above. Fresh independent
whole-diff review remains a separate instance and record.

The Report issue continuation returned three changed files and 158 focused
tests plus frontend/Electron typechecks passing. Parent inspected the complete
delta and performed the native navigation described above. No new IPC or
external-navigation permission was introduced.

The Runtime history repair returned seven files and 50 focused tests plus
TypeScript passing. Parent inspected all seven diffs and ran the complete
connecting suites above. The same read-only source auditor verified the pinned
history omission and supported injection/flush path. No agent tested a mock and
claimed native adoption; the live primary and fresh-child checks are separate.
