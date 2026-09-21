# v3 "done" declaration — candidate

> **CANDIDATE, CONTEXT-class, not authority until the owner confirms at the R0 gate.**
>
> Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128). Prepared by a TASK (Type 2)
> executor from the frozen tree at `00115c719`. This file assembles what the records
> say "done" meant for v3. It is not an owner ruling. Where the records do not say
> something directly, the text marks it **inferred**. Records written by agents,
> such as run logs, handoffs and publication notes, are labelled
> **agent-recorded**. They show what an agent reported about owner direction. They
> are not verbatim owner rulings.

## How to read this candidate

The plan's done-definition changed twice after the owner adopted it:

1. **2026-08-22 → 2026-09-04: the plan with its amendments.** The owner ruled on
   the Revision 3.1 plan at G0. In that plan, v3.0.0-rc.1 was a stable product with
   an opt-in Codex Preview inside a hard outer envelope enforced by Chirality. The
   G0 rulings and the A- and R-series ruling records changed parts of it. R17-C
   adopted the plan as the pinned "completion and acceptance reference".
2. **2026-09-11/12: the Codex re-platform.** D-GOV-43 and its A2 supplement
   replaced most of the architecture and gates. Their "measure of done" is S-1 to
   S-8. The only human acts they keep are the ruling, the owner's native trial and
   explicit publishing approval. D-APP-127 applied this to the App loop.
3. **2026-09-13 → 2026-09-19: the release.** The owner gave the late product
   decisions in session (agent-recorded). v3.0.0 was published as a stable release
   on 2026-09-13. On 2026-09-19 the owner said: "App has already been published as
   `v3.0.0`".

### Citation keys (all paths repo-relative)

| Key | Path |
|---|---|
| PLAN | `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` |
| G0 | `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` |
| A*n* | `plans/steers/chirality_app_v3_app_ruling_record_a<n>_<date>.md` |
| R*n* | `plans/steers/chirality_app_v3_root_ruling_record_r<n>_<date>.md` |
| DIR43 | `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md` |
| DGOV43 | `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` |
| DGOV43P | `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md` (ruling items adopted by DGOV43) |
| D97 / D125 / D126 / D127 | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-{97,125,126,127}_*.md` |
| RP-HANDOFF / RP-PERSP / RP-LOG | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/{HANDOFF,PERSPECTIVE,RUN_LOG}.md` |
| DT-HANDOFF | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_DIRECT_TRIAL_20260910/HANDOFF.md` |
| UI-LOG | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/RUN_LOG.md` |
| UJ-PLAN / UJ-LOG / UJ-PUB / UJ-NOTES | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/{PLAN,RUN_LOG,PUBLIC_RELEASE_20260913,OWNER_TRIAL_NOTES}.md` |
| OD0919 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md` |
| RECEIPTS | `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` |

Each package mapping is **provisional**. It uses App package and deliverable names
from `projects/chirality-app-dev/execution/PKG-*/1_Working/`.

---

## §1 Done criteria

**DONE-01 — The core experience works end to end: plan, execute, save a workflow,
reuse it and iterate, with Codex agents at full capability.**
- Sources: DIR43 "Verbatim owner statements": "I need to have the Codex agents in
  their full glory". RP-PERSP (owner's note, verbatim): "plan your work, execute it,
  save useful methods as workflows, reuse them, and iterate."
- Status: **ADDED BY D-GOV-43** (DIR43; DGOV43P item 12). The plan's success
  criteria had no workflow-experience criterion (inferred from PLAN §3.2).
- Packages (provisional): PKG-02 (DEL-02-01, DEL-02-03), PKG-08 (DEL-08-01,
  DEL-08-03), PKG-05 (DEL-05-04).

**DONE-02 — Chirality hosts a stock, version-pinned OpenAI Codex App Server as the
sole engine. The App starts, owns and stops a Runtime service child process. There
is no patched supplier, admission layer or LaunchAgent.**
- Sources: PLAN §3.1: "Existing Chirality-native engines remain usable; Codex App
  Server becomes an opt-in delegated-harness adapter." G0 A8: "Opt-in Preview".
  DGOV43P item 1: "hosts a stock OpenAI Codex App Server". RP-HANDOFF §1:
  "Codex is the only engine". D127 "Governing facts applied": "Retired: the
  LaunchAgent and installer (DEL-09-07, APP-HOLD-1), hosted admission".
- Status: **SUPERSEDED BY D-GOV-43 items 1 and 7 plus the A2 supplement** (applied
  by D-APP-127). The ORIGINAL criterion (native engines kept, Codex as an opt-in
  Preview) and G0 A8 no longer describe the product (inferred). This candidate did
  not find the record that first set the Codex sole-engine rule (see Q-06).
- Packages (provisional): PKG-03 (DEL-03-01 to DEL-03-04), PKG-04 (DEL-04-01),
  PKG-09 (DEL-09-07 retired).

**DONE-03 — First run: a new user installs the released DMG, passes Gatekeeper,
starts Chirality, signs in with ChatGPT through Codex and completes a turn.**
- Sources: PLAN §3.2 item 1: "A new user can install the released DMG, pass
  Gatekeeper, start Chirality". D127 on D-APP-126: "independent consent for each
  folder" retires with hosted admission.
- Status: **AMENDED BY D-GOV-43 / D-APP-127**. The steps "choose Codex (Preview)"
  and "grant project consent" drop out (inferred from the sole-engine rule and the
  consent retirement). Recorded outcome: UJ-PUB records "Gatekeeper accepted it as
  Notarized Developer ID". A clean install by a new user is not recorded: UJ-PUB
  says agent checks "do not assert the owner's unperformed installation checks."
- Packages (provisional): PKG-09 (DEL-09-04), PKG-02 (DEL-02-05).

**DONE-04 — Codex delegates natively without a Chirality cap. The four roles and
full Agent 0/1/2 functionality are available, and delegated children receive the
intended role instructions.**
- Sources: PLAN §3.2 item 2: "Codex can delegate natively when it judges delegation
  useful". G0 A1: "Required, no Chirality cap". G0 A2: "Not automatically Agent 2".
  G0 A3 (recorded form): "Agent 0/1/2 role entry is always offered for Codex
  sessions (parity requirement)." G0 D1: "SCA-APP-008 authorizes multi-child
  managed execution". DGOV43P item 8: "Upstream base instructions and tool
  behaviour are preserved."
- Status: **AMENDED BY G0 A1–A3 and D1, then by D-GOV-43 items 8 and 10.** S-5 is
  the check for this criterion.
- Packages (provisional): PKG-08 (DEL-08-01, DEL-08-04, DEL-08-05), PKG-04
  (DEL-04-04).

**DONE-05 — The user chooses the approval and sandbox policy per project and can
override it per turn, from Codex's own options. The composer shows the active
policy.**
- Sources: PLAN §3.2 item 3: "No primary or descendant thread can read, write,
  execute, reach the network". G0 A6: "No pre-authorized read-only fallback." G0 A7:
  "each canonical root chooses under consent". DGOV43P item 4: "Approval policy and
  sandbox mode are the user's choice per project". DGOV43P item 10: "hard outer
  envelope" is "re-expressed as the user-chosen policy of item 4".
- Status: **SUPERSEDED BY D-GOV-43 items 4 and 10.** The ORIGINAL hard envelope
  enforced by Chirality (`includePlatformDefaults: false`, command network off) and
  G0 A6/A7 are replaced (inferred).
- Packages (provisional): PKG-06 (DEL-06-01, DEL-06-04, DEL-06-05), PKG-10
  (DEL-10-02).

**DONE-06 — Faithful transport: the App forwards the complete notification stream
and answers every server request. It never leaves a request unanswered and never
implies approval.**
- Sources: DGOV43P item 2: "No request is left unanswered, so Codex never waits
  indefinitely". RP-HANDOFF §3 sets the disconnection rule: a renderer disconnect
  no longer interrupts a turn.
- Status: **ADDED BY D-GOV-43 item 2.** It replaces the plan's closed HarnessEvent
  schema v2 and G-WIRE approach (PLAN §8.5; D127 retires "the closed event
  vocabulary").
- Packages (provisional): PKG-03 (DEL-03-03, DEL-03-04), PKG-05 (DEL-05-02).

**DONE-07 — Sign-in and sign-out use Codex's own account methods, scoped to
Chirality. Codex custodies credentials in a private `auth.json`. Chirality never
copies credentials and leaves other Codex clients' state unchanged (S-8).**
- Sources: PLAN §3.2 item 1 and §7 (managed ChatGPT login). G0 A9: "Root-private
  app-owned home". DGOV43P item 3 keeps "authentication private (`auth.json` and the
  models cache)". DGOV43P item 6: "The App never reads, copies or relays credential
  material."
- Status: **AMENDED BY D-GOV-43 items 3 and 6.** These supersede G0 A9, D-APP-125
  item 3 and all three D-APP-126 boundaries, per D127.
- Packages (provisional): PKG-02 (DEL-02-05), PKG-04 (DEL-04-05).

**DONE-08 — Lifecycle and continuity: quit stops the owned processes deliberately.
Relaunch resumes the same chat through `thread/resume`. Interruption, approval
denial and unexpected termination are shown truthfully. No orphan process
survives.**
- Sources: PLAN §3.2 item 4: "Interrupt, quit, crash, logout, daemon restart, and
  upgrade do not leave an orphan". G0 A4: "active turns terminalize on retirement or
  crash". DGOV43P item 5: "App relaunch resumes threads through `thread/resume`".
  RP-HANDOFF §3, "Shutdown behaviour".
- Status: **AMENDED BY G0 A4, then by D-GOV-43 items 5 and 7.** S-6 and S-7 are the
  checks.
- Packages (provisional): PKG-03 (DEL-03-02, DEL-03-04), PKG-05 (DEL-05-01).

**DONE-09 — Existing v2 user data is preserved and opens without destructive
rewrite. Daemon-era chats are preserved; they may be viewable but are not
imported.**
- Sources: PLAN §3.1 ("preserves v2 user data and fails explicitly when
  incompatible"). A13: "retention is the v3 posture". DGOV43P item 5: "No
  history-import feature is a release prerequisite".
- Status: **AMENDED BY A13 and D-GOV-43 item 5.** No record found verifies v2 to v3
  migration on the shipped build (see Q-09).
- Packages (provisional): PKG-05 (DEL-05-01, DEL-05-04).

**DONE-10 — Evidence: the App records AgentRuns, plan revisions, workflow
selections, actual model attribution, approvals and the active policy from the same
event stream.**
- Sources: DGOV43P item 9: "recorded by the App from the same event stream".
- Status: **ADDED BY D-GOV-43 item 9.** It replaces the plan's redaction and
  closed-schema evidence model (PLAN §8.5, G-WIRE; inferred).
- Packages (provisional): PKG-05 (DEL-05-02, DEL-05-03, DEL-05-05), PKG-08
  (DEL-08-05).

**DONE-11 — Ordinary application security is kept: renderer isolation, validated
IPC, no credential material in the renderer, a per-response CSP nonce, dependency
integrity and code signing.**
- Sources: PLAN §10.1, G-CSP (context isolation and sender checks). A15 clause 1
  (renderer CSP): "Yes, so authorized." DGOV43P item 11 retains "ordinary software
  integrity" and "renderer isolation and validated IPC" (paraphrased from item 11's
  "Retained:" list).
- Status: **AMENDED BY A15 and D-GOV-43 items 2 and 11.**
- Packages (provisional): PKG-09 (DEL-09-06).

**DONE-12 — Measure of done: S-1 to S-8 pass against pinned stock Codex, on the
production path, in one App instance. Every action is visible in Activity, and no
turn is interrupted by transport.**
- Sources: DGOV43P item 12, "Measure of done." S-1 is Plan Mode with a revision.
  S-2 is real tool use beyond 30 seconds of silence. S-3 saves a workflow. S-4
  reuses and iterates it. S-5 is delegation with role instructions. S-6 is quit and
  relaunch with continuation. S-7 is interruption and a denied approval. S-8 is
  sign-in and sign-out scoped to Chirality.
- Status: **ADDED BY D-GOV-43 item 12.** Recorded outcome: RP-LOG 2026-09-12T15:50Z
  says "All of S-1..S-8 and the disconnect check now PASS on the source-run App."
- Packages (provisional): cross-cutting; PKG-09 (DEL-09-01 to DEL-09-03).

**DONE-13 — An independent source review happens before one consolidated signed
build. After the build, S-6, S-8, the bundle signature and the Codex pin are
repeated as the minimum. Any check whose evidence a later change invalidates is
repeated too.**
- Sources: DGOV43P item 12: "only the checks that exercise a distinct packaged or
  native condition are repeated". DGOV43 "Clarification": "the expected minimum,
  not an absolute ceiling".
- Status: **ADDED BY D-GOV-43** (ruling and clarification). Recorded outcomes: the
  RP-LOG review verdict was PASS for `388de6973`. UJ-PUB says PR #781 "Required CI
  and independent source review passed." The outcome of the packaged S-6 and S-8
  checks on the published build is not recorded (see Q-04).
- Packages (provisional): PKG-09 (DEL-09-04, DEL-09-05).

**DONE-14 — Governance simplification is a primary deliverable. Families whose
purpose disappeared are retired, not renamed. These include the daemon,
LaunchAgent, admission, supplier containment, the Stage 9–13 packaging spine and
the held release bindings.**
- Sources: DGOV43P item 11: "Governance simplification is a primary deliverable".
  The same item says "the nine held release bindings are not mapped onto the spike
  checks". D127 lists the superseded parts.
- Status: **ADDED BY D-GOV-43 item 11**, applied by D-APP-127.
- Packages (provisional): PKG-01 (DEL-01-01, DEL-01-04), PKG-00, PKG-09
  (DEL-09-07).

**DONE-15 — The human acts kept are the D-GOV-43 ruling, the owner's native trial,
the system-prompt discussion and explicit publishing approval.**
- Sources: DGOV43P item 11: "the owner's native trial and explicit publishing
  approval". DT-HANDOFF: "Final milestones are usable trial, system-prompt
  discussion, and explicit publishing approval." RP-HANDOFF §5: "Publishing, the
  system-prompt discussion and trial acceptance remain the owner's separate acts."
- Status: **ADDED BY D-GOV-43** (item 11 and closure gate 5). These replace the
  plan's owner gates G0.5–G8 (inferred). Recorded outcomes: publishing approval is
  recorded (agent-recorded, UJ-PUB). No record found closes trial acceptance or the
  system-prompt discussion (see Q-03).
- Packages (provisional): PKG-01 (DEL-01-01).

**DONE-16 — The release identity is Chirality v3.0.0, a stable release for macOS
Apple Silicon only.**
- Sources: PLAN title and §12.3: "Chirality-3.0.0-rc.1-arm64.dmg". G0 B1: "macOS
  arm64 only; 2nd target deferred". A14: "Defer until G5 fan-in (Recommended)"
  (the rc.1 version patch). UJ-PLAN (agent-recorded owner direction): "Target
  release v3.0.0, with publishing still subject to explicit owner direction."
  OD0919 (owner verbatim): "App has already been published as `v3.0.0`".
- Status: **AMENDED BY owner direction recorded in UJ-PLAN** (agent-recorded, not
  verbatim). The architecture-level retirement comes from D-GOV-43. The shift from
  `3.0.0-rc.1` prerelease to `3.0.0` stable has no verbatim owner ruling in the
  records read (see Q-01).
- Packages (provisional): PKG-09 (DEL-09-05), PKG-01 (DEL-01-03).

**DONE-17 — The exact final installer is Developer ID signed, notarized, stapled
and accepted by Gatekeeper. It is published with its checksum as the latest stable
GitHub release, and the public download is re-verified.**
- Sources: PLAN §12.2: "Publish as a GitHub prerelease". G0 A5: "Decline App
  Sandbox". UJ-PUB: "That later direction supersedes the earlier owner-performed
  Apple step." UJ-PUB records publication "as the latest stable release".
- Status: **AMENDED BY owner direction recorded in UJ-PUB and UJ-LOG**
  (agent-recorded). The change is from a prerelease with an owner-performed Apple
  step to a stable release notarized by an agent under owner direction. Recorded
  outcome: published 2026-09-13T05:08:54Z. Anonymous download and checksum were
  verified at 05:10:01Z (UJ-PUB).
- Packages (provisional): PKG-09 (DEL-09-04, DEL-09-05).

**DONE-18 — The public artifact traces to accepted source and release identities,
with third-party notices and an SBOM.**
- Sources: PLAN §3.2 item 5: "include notices and an SBOM, and pass signing,
  notarization, stapling". PLAN §12.3: "Third-party notices and pinned-Syft
  CycloneDX JSON SBOM." A15 clause 2 authorized installing Syft.
- Status: **ORIGINAL.** No superseding record was found. UJ-PUB lists only the DMG
  and checksum as public assets. Source traceability is recorded through PR #781
  and commit `6f41f93e7` (see Q-08).
- Packages (provisional): PKG-09 (DEL-09-05).

**DONE-19 — The App checks for new stable releases at startup and every six hours.
An available update shows a visible indicator, and download and install stay
explicit.**
- Sources: UJ-LOG 2026-09-13T04:10:37Z (agent-recorded): the "owner authorized
  the startup/six-hour fix and stated readiness to publish afterward."
- Status: **ADDED BY owner direction recorded in UJ-LOG** (agent-recorded).
- Packages (provisional): PKG-02 (DEL-02-01), PKG-09 (DEL-09-06, K-NET-1 clause).

**DONE-20 — Late product decisions made in session:**
- Native questions, steering, checklists and observed delegated agents are included.
- The Skills browsing UI is hidden while skills keep working in the background.
- The folder picker starts at home and remembers the last chosen folder.
- Cross-folder chat continuity is included.

- Sources: UJ-PLAN: "The owner approved all four native interaction additions,
  including native steering." UJ-PLAN, owner decisions 2026-09-13T00:15:50Z: "hide
  Skills UI for this release and keep background skill use". UI-LOG
  2026-09-12T19:52Z: "Owner first withdrew cross-folder chat from the MVP", and
  later "the owner directed finishing it".
- Status: **ADDED BY owner direction recorded in UJ-PLAN and UI-LOG**
  (agent-recorded).
- Packages (provisional): PKG-02 (DEL-02-01, DEL-02-03, DEL-02-04), PKG-08
  (DEL-08-01).

---

## §2 Explicitly out of scope for v3

**OOS-01 — Parity across engines, models and providers, and any multi-engine
abstraction.**
- Sources: PLAN §3.1 (not required): "Parity between every engine, model, tool, or
  provider." RP-HANDOFF §1 says the multi-engine abstractions "are retired, not
  generalized".
- Status: **AMENDED BY D-GOV-43** (ORIGINAL exclusion made stronger).
- Packages (provisional): PKG-03 (DEL-03-01), PKG-04.

**OOS-02 — Claude subscription OAuth and custom ownership of ChatGPT tokens. The
Claude engine is also absent from the App MVP (inferred).**
- Sources: PLAN §3.1: "Claude subscription OAuth; custom ownership of ChatGPT
  tokens; multi-platform distribution." DGOV43 "Application boundary" excludes "any
  change to the Codex sole-engine rule".
- Status: **ORIGINAL; AMENDED BY D-GOV-43 (inferred)** for the Claude engine
  itself.
- Packages (provisional): PKG-04 (DEL-04-05).

**OOS-03 — Distribution for more than one platform. A second deployment target is
deferred.**
- Sources: PLAN §3.1 (as above). G0 B1: "macOS arm64 only; 2nd target deferred".
  A11 closed TM-APP-025 as `RESOLVED_BY_DECISION`.
- Status: **ORIGINAL; confirmed by G0 B1.**
- Packages (provisional): PKG-09 (DEL-09-04).

**OOS-04 — A Chirality-authored subagent scheduler, child allowlist, fixed
hierarchy, or automatic classification of descendants as Agent 2.**
- Sources: PLAN §3.1: "A Chirality-authored subagent scheduler, child allowlist,
  fixed hierarchy". G0 A1, G0 A2.
- Status: **ORIGINAL; confirmed by G0 A1 and A2.**
- Packages (provisional): PKG-08 (DEL-08-04).

**OOS-05 — Hosted Apple signing credentials and automatic notarization on ordinary
CI.**
- Sources: PLAN §3.1: "Hosted Apple signing credentials, automatic notarization on
  ordinary CI".
- Status: **ORIGINAL.** The recorded notarization used a local profile, not CI
  (UJ-LOG 2026-09-13T04:47:31Z; inferred to be consistent).
- Packages (provisional): PKG-09 (DEL-09-05).

**OOS-06 — Re-attaching or replaying an in-flight turn across process
retirement.**
- Sources: PLAN §3.1: "Active-turn attachment, replay, or continuity across
  daemon/supervisor/worker retirement." G0 A4 allows `thread/resume` of the stored
  thread and makes "No in-flight re-attach claim".
- Status: **AMENDED BY G0 A4.** Resuming a stored thread is in scope; re-attaching
  a live turn is out.
- Packages (provisional): PKG-03 (DEL-03-04).

**OOS-07 — Apple App Sandbox.**
- Sources: G0 A5: "Decline App Sandbox".
- Status: **ADDED BY G0 A5.**
- Packages (provisional): PKG-09 (DEL-09-04).

**OOS-08 — Local-model integration and the runtime residency requirements.**
- Sources: DGOV43P item 13: "Local-model integration is not part of this ruling."
  RP-HANDOFF §1: "Piping integration and local-model management remain deferred".
- Status: **ADDED BY D-GOV-43 item 13.**
- Packages (provisional): PKG-04, PKG-10.

**OOS-09 — A workflow execution engine or a separate workflow editor.**
- Sources: RP-PERSP: "This tranche does not include a workflow execution engine, a
  separate workflow editor".
- Status: **ADDED BY D-GOV-43** (owner's intent note, RP-PERSP; inferred scope
  effect).
- Packages (provisional): PKG-08 (DEL-08-03).

**OOS-10 — Importing history from daemon-era chats, or promising to continue them.**
- Sources: DGOV43P item 5: "No history-import feature is a release prerequisite".
- Status: **ADDED BY D-GOV-43 item 5.**
- Packages (provisional): PKG-05 (DEL-05-01, DEL-05-04).

**OOS-11 — An option to share authentication with other Codex clients.**
- Sources: DGOV43P item 3: "a direct shared-authentication opt-in is deferred".
- Status: **ADDED BY D-GOV-43 item 3.**
- Packages (provisional): PKG-02 (DEL-02-05).

**OOS-12 — Runtime CLI and PEC compatibility, and Piping integration, as MVP
prerequisites.**
- Sources: D127 on D-APP-100: "the Runtime CLI's compatibility is unverified and not
  an MVP prerequisite". RP-HANDOFF §3, "Consumers".
- Status: **ADDED BY D-GOV-43 A2 supplement / D-APP-127.**
- Packages (provisional): PKG-03 (DEL-03-03).

**OOS-13 — Skills browsing UI in this release.**
- Sources: UJ-PLAN owner decisions: "hide Skills UI for this release and keep
  background skill use".
- Status: **ADDED BY owner direction recorded in UJ-PLAN** (agent-recorded).
- Packages (provisional): PKG-02 (DEL-02-04).

**OOS-14 — Retired machinery:**
- the LaunchAgent and two-job installer (DEL-09-07);
- hosted admission and identity binding;
- supplier containment evidence;
- the Stage 9–13 packaging spine;
- the closed event vocabulary;
- the per-chat model and effort freeze;
- the G-HELPER bundle identity (TM-APP-030).

- Sources: D127, "Governing facts applied", and its D-APP-88 and D-APP-107
  sections.
- Status: **ADDED BY D-APP-127** (application of D-GOV-43). These were in scope
  under the ORIGINAL plan.
- Packages (provisional): PKG-09 (DEL-09-04, DEL-09-07), PKG-03, PKG-05 (DEL-05-02).

**OOS-15 — Claiming the App Server protocol is stable, or silently falling back to
another engine.**
- Sources: PLAN §3.1: "Claiming the App Server protocol itself is stable or silently
  falling back".
- Status: **ORIGINAL.** The fallback half is still consistent with the sole-engine
  rule (inferred).
- Packages (provisional): PKG-03, PKG-01 (DEL-01-03).

**OOS-16 — Synchronizing the framework and library projection to the release
repository as part of the v3.0.0 publication.**
- Sources: UJ-PUB: "This release distributes the installer and checksum". UJ-PUB
  says the exporter's D-GOV-41 adoption hold "was not run or bypassed".
- Status: **ADDED BY agent decision recorded in UJ-PUB** (agent-recorded; no owner
  record found; inferred).
- Packages (provisional): PKG-09 (DEL-09-05).

---

## §3 Gates

"Final recorded outcome" gives only what a record states. "None found" means the
records read contain no outcome. Anything described as retired is **inferred** from
D-GOV-43 item 11 and D-APP-127 unless the record names the gate.

### Plan gates (PLAN §10.1)

| Gate | Pass evidence required | Final recorded outcome |
|---|---|---|
| G0 | Owner records RC scope, native delegation, Agent-2 failure posture, Preview label, sandbox and network posture, and triage (PLAN §10.1) | **Ruled 2026-08-22** (G0, A1–D3). |
| G0.25 | DEL-09-04 staged owner proof completed or deferred | **PASSED**. A1-A: "Rule G0.25 PASSED". |
| G0.5 | Superseding D-GOV, DEL-02-03 M2, SCA-004, SCA-APP-008, K-CONTROL-1/K-ROLE-2, ten bindings routed, implementation act | **Not passed.** R16: "It does not declare G0.5 passed". R17-B: "G0.5 remains incomplete". Later retired by DGOV43P item 11 (inferred). |
| G1 | Accepted snapshots, AT-053, RQG §13, no stale mirror or unresolved Pi/event defect | **Not passed.** R18-B: "It does not pass G1"; TM-ROOT-106 open. No later pass record found; retired (inferred). |
| G2 | Exact App Server supply bytes, schema, signature and license accepted | **Accepted for 0.149.0 with gaps.** R15-A: "Accept at G2 with documented gaps and G5 finding." The shipped pin is 0.154.0 under DGOV43P item 1: "Upstream drift is a dependency update" (RP-LOG; UJ-LOG). |
| G-HELPER / G-SIG / G-DUAL | Two-LaunchAgent process-supervisor proof | **Retired.** D127 on D-APP-88 retires the LaunchAgent and TM-APP-030. |
| G-SBX / G-SENT / G-PROT / G-ENV / G-ROLE / G-APPR | Authority-envelope proofs on the real turn path | **None found.** R17-A rejected the R16 feasibility attempt. The purpose was replaced by user-chosen policy (DGOV43P items 4 and 10; inferred retired). |
| G-WIRE | Closed event schema v2, secret scan across sinks | **Superseded** by faithful transport (DGOV43P item 2; D127 retires the closed vocabulary). |
| G-CSP | Isolation, CSP, sender checks on all credential IPC | **Partial.** A15 authorized a per-response CSP nonce. No gate pass record found. D127 retires G-CSP as a host gate for live-login claims only. |
| G3 / G4 | Owner-authenticated exact-pin account and turn proof; containment and delegation | **Replaced** for live login by S-8 (D127 on D-APP-122). No gate pass record found. |
| G5 | Unsigned preparation package fan-in, SBOM, notices, runbook, self-signed drill | **None found.** A14 deferred the rc.1 identity to "G5 fan-in". Replaced in practice by the consolidated signed build (DGOV43P item 11; inferred). |
| G6a | Owner release act; exact-candidate K-RELEASE-1 amendment and F-APP-2 lift | **No ruled D-APP release record found.** Publishing approval is recorded by an agent only (UJ-PUB; UJ-LOG 04:10:37Z). G0 D2 and D97 required the exact-candidate lift (see Q-02). |
| G6b | Signed, notarized, stapled without rebuild | **Done for the final 3.0.0 DMG.** UJ-PUB: notarization "Accepted"; stapled; Gatekeeper "Notarized Developer ID". |
| G-KEY | Credential transition on real release identities | **None found.** The credential model changed under DGOV43P items 3 and 6 (inferred). |
| G7 | Exact signed-byte regression, clean machine, no open P0 or high findings | **None found.** UJ-PUB: agent checks "do not assert the owner's unperformed installation checks." |
| G8 | Published; public download re-verified; immutable snapshot | **Done** (agent-recorded). UJ-PUB: public page, latest-release API, digests and checksum verified at 2026-09-13T05:10:01Z. |

### D-GOV-43 checks and retained acts (DGOV43P item 12 and closure gates)

| Check / act | Pass evidence required | Final recorded outcome |
|---|---|---|
| S-1 … S-8 from source | DGOV43P item 12 | **PASS** (RP-LOG 2026-09-12T15:50Z). |
| Independent source review | Separate reviewer before the consolidated build (DGOV43, "Application boundary") | **PASS** at `388de6973` (RP-LOG 16:40Z). UJ-PUB records it passed for final source `6f41f93e7`. |
| Post-build S-6, S-8, signature and Codex pin | DGOV43P item 12 and clarification | **Signature and pin PASS** on each build (RP-LOG; UJ-LOG 03:12:28Z). **Packaged S-6 and S-8: none found**; RP-LOG leaves "native checklist" to the owner. |
| Owner's native trial / trial acceptance | DGOV43P item 11; RP-HANDOFF §5 | **None found.** |
| System-prompt discussion | DT-HANDOFF; RP-HANDOFF §5 | **None found.** UJ-LOG 03:51:58Z still lists "final guidance discussion" as outstanding. |
| Explicit publishing approval | DGOV43P item 11 | **Recorded by an agent** (UJ-LOG 04:10:37Z and 04:47:31Z; UJ-PUB). No verbatim owner text is in these files. |

---

## §4 Gaps and conflicts: questions for the owner

**Q-01 (release identity).** The plan, R17-C and A14 all name `3.0.0-rc.1` as a
GitHub prerelease. A14 deferred that version patch "until G5 fan-in". The published
release is `3.0.0` as "the latest stable release" (UJ-PUB). The only record of the
change is agent-written (UJ-PLAN: "Target release v3.0.0"). Do you confirm that
done for v3 means stable `v3.0.0`, and that `3.0.0-rc.1` was intentionally
skipped?

**Q-02 (release act and fence).** G0 D2 and D-APP-97 keep F-APP-2 in force until an
exact-candidate lift at G6a. D97 says "F-APP-2 continues to fence signing,
notarization, and distribution". The records read contain no D-APP ruling that
amends K-RELEASE-1 or lifts F-APP-2. D-GOV-43 item 11 names "explicit publishing
approval" as the retained act, and D-APP-127 says it authorizes no release. Should
the session publishing approval (agent-recorded in UJ-PUB) count as the release act
and fence lift for the exact published DMG? Or should reconciliation record a
retrospective ruling?

**Q-03 (retained human acts).** D-GOV-43 and the handoffs keep three owner acts:
the native trial, the system-prompt discussion and publishing approval. Only
publishing approval has a record. Were trial acceptance and the system-prompt
discussion completed, waived by publishing, or still open after release?

**Q-04 (packaged checks).** D-GOV-43 item 12 requires S-6 and S-8 again on the
consolidated signed build. RP-LOG assigns this to the owner's native checklist.
The records read show no outcome for any packaged build, including the final
published DMG. Were these performed? Were they invalidated by the later rebuilds
for the dependency repair and the update checker?

**Q-05 (loop record gap).** RECEIPTS runs from Receipt 261 (2026-09-07) to
Receipt 262 (2026-09-19). No App loop receipt records the Codex-only trial, D-GOV-43
and D-APP-127, the user-journey campaign or the v3.0.0 publication. Those events
are recorded only in AgentRuns and Git. Should reconciliation treat the AgentRuns
records as sufficient, or add a durable loop record?

**Q-06 (sole-engine decision).** The plan kept the native engines and made Codex an
opt-in Preview (PLAN §3.1; G0 A8). By 2026-09-10 the work was a "Codex-only MVP"
(RP-HANDOFF; DT-HANDOFF). D-GOV-43 treats "the Codex sole-engine rule" as already
in place. This candidate found no record that first ruled it. Where was that
decided? Should it appear in the done declaration as its own owner decision?

**Q-07 (containment conflict).** The plan's success criterion 3 required a hard
envelope enforced by Chirality. G0 A6 said "No pre-authorized read-only fallback".
G0 A7 set three per-root network postures. D-GOV-43 items 4 and 10 replace all of
this with the user's own Codex policy, including `danger-full-access` by explicit
choice. Do you confirm that done means the user-chosen policy, with A6 and A7
superseded?

**Q-08 (SBOM and notices).** The plan's §3.2 and §12.3 require notices and an SBOM
in the publication. A15 authorized the Syft install for this. The published
release carries only the DMG and checksum (UJ-PUB). Were SBOM and notices
deliberately dropped under D-GOV-43's "ordinary software integrity", or are they an
open obligation?

**Q-09 (v2 upgrade path).** AT-035 and A13 require v2 data to open without
destructive rewrite. UJ-NOTES says "The final DMG has not been installed over the
owner's App by this agent." The records read do not show a v2.0.0 to v3.0.0
install-over check on the published build. Is that check part of done, and was it
performed?

**Q-10 (held bindings and deferred rows).** D-GOV-43 item 11 says the nine held
bindings "are not mapped onto the spike checks". TM-ROOT-106 and TM-APP-027, 028
and 032 were expected to "fire at G6a–G7" (A11). This candidate found no record
that closes or retires these rows. Should the done declaration state them as
retired by D-GOV-43, or are they open reconciliation items?

**Q-11 (managed multi-child delegation).** G0 D1 made managed multi-child
execution (DEL-08-04 and DEL-08-05) an App v3 capability. D-GOV-43 routes
delegation through Codex's own `[agents]` configuration and S-5. Is managed
multi-child execution still part of done, or retired with the daemon path?

**Q-12 (accessibility).** The plan's AT-034 (keyboard and VoiceOver for consent,
login, approval, interrupt and logout) has no successor in D-GOV-43, and no outcome
was found. Is accessibility in or out of the v3 done definition?

**Q-13 (who performed the Apple step).** The plan says the human owner performs
release acts (PLAN §9, WP-11). UJ-PUB records that an agent performed notarization
under a later owner direction. Do you confirm this as the accepted release
procedure for v3.0.0?

---

## §5 Sources read

All files were read from the frozen tree at `00115c719`. SHA-256 is over the file
bytes at that tree. "Read depth" states how much of each file this candidate relied
on.

| Path | Read depth | SHA-256 |
|---|---|---|
| `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` | §1–3, §8, §10, §11, §12, §15 (tag-stripped) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` | full | `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b` |
| `plans/steers/chirality_app_v3_app_ruling_record_a10_2026-08-24.md` | full | `0908fee812919291979dd486dd9748fda21b9fb4b20afb13604a1a3e02bd8aa2` |
| `plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md` | full | `6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27` |
| `plans/steers/chirality_app_v3_app_ruling_record_a12_2026-09-03.md` | full | `21b77b378a6511b48ea2e60e676ea1c9b7ee013d8c042769392decf57ceb29ec` |
| `plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md` | full | `557c64aaf765b20b877cd3a5331d0f6a4c73e562c5463eaf5f9c5e122e325271` |
| `plans/steers/chirality_app_v3_app_ruling_record_a14_2026-09-03.md` | full | `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06` |
| `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md` | full | `5b99e308bd0e0affbc72ac7c8a727ca0aa5fa51d0de073f1d5cfeb35807ec817` |
| `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` | full | `f9b02806eeab1a578e6729c41fc367074758a2b95cc0eda9c8d2edbda446f314` |
| `plans/steers/chirality_app_v3_app_ruling_record_a2_2026-08-23.md` | full | `37e6b6d60874ded0727cf65f25aea09cc961bd35b135b5b8eb33c0d20c1f6158` |
| `plans/steers/chirality_app_v3_app_ruling_record_a3_2026-08-23.md` | full | `91d6867286de465f56bb41a6de9e9d8657e6b63ddb009f294d81b3e6dcccded9` |
| `plans/steers/chirality_app_v3_app_ruling_record_a4_2026-08-23.md` | full | `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d` |
| `plans/steers/chirality_app_v3_app_ruling_record_a5_2026-08-23.md` | full | `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b` |
| `plans/steers/chirality_app_v3_app_ruling_record_a6_2026-08-23.md` | ruling lines | `66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63` |
| `plans/steers/chirality_app_v3_app_ruling_record_a7_2026-08-23.md` | ruling lines | `56b9dc8ed8835a3220ccab10416cd9457d2a1d58b62c92582d84c773430e22d2` |
| `plans/steers/chirality_app_v3_app_ruling_record_a8_2026-08-23.md` | ruling lines | `d4018737aa9ae33e5b26f2afd3fbb2ffc1e9c8d3fe0a2494cf64c951224b6c8f` |
| `plans/steers/chirality_app_v3_app_ruling_record_a9_2026-08-24.md` | ruling lines | `6ce5534514b8298ab9cfff3c72ba7f0532a41f58278ef03cc6c4cdadf9b47178` |
| `plans/steers/chirality_app_v3_root_ruling_record_r10_2026-08-24.md` | headers and ruling lines | `68c8524dc2a84d8584b04969d7684fd6124f6a72399d1a80a499df6baaa0ae8f` |
| `plans/steers/chirality_app_v3_root_ruling_record_r11_2026-08-24.md` | headers and ruling lines | `01d9ae6d42d25942ae4991b61385b8d1a70a8d54a82d88d17648c000d6622fbd` |
| `plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md` | headers and ruling lines | `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd` |
| `plans/steers/chirality_app_v3_root_ruling_record_r13_2026-08-24.md` | headers and ruling lines | `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960` |
| `plans/steers/chirality_app_v3_root_ruling_record_r14_2026-08-24.md` | headers and ruling lines | `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9` |
| `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md` | full | `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301` |
| `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md` | full | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| `plans/steers/chirality_app_v3_root_ruling_record_r17_2026-08-27.md` | full | `23532e46893d8bd79f05775b4744f1438bbb29dbc58b6c70b04b3ae912752faf` |
| `plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md` | full | `1f315a482ddcaf253d13d6b219f8534c1ddcf7b9d818a72f94c988534d9b8d69` |
| `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md` | full | `a9879a87faaeb4cd4d5f16b2b4b0364543dff117e1b51c7e17d1efdcb20f377d` |
| `plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md` | headers and ruling lines | `63b174f00860cd31dbdde1f734a9e1ca08c44f7cd2ed51f7716612f3847a6bce` |
| `plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md` | headers and ruling lines | `88608e168aaab64a833e6c1742647969e726f2928ad9b9bc0a40932085d0e0b5` |
| `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md` | headers and ruling lines | `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a` |
| `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md` | headers and ruling lines | `1f0a3358602fdfb4dff70607ad631130db55dcfd62d71a6fe7a3a13e18f0f42a` |
| `plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md` | headers and ruling lines | `4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de` |
| `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md` | headers and ruling lines | `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53` |
| `plans/steers/chirality_app_v3_root_ruling_record_r8_2026-08-23.md` | headers and ruling lines | `b91ee877b6a6c168434e34389309dd2663026baca03c2d900d9df8d182308d0f` |
| `plans/steers/chirality_app_v3_root_ruling_record_r9_2026-08-23.md` | headers and ruling lines | `bc3a3bf414cfd64a5a650d633e942c2bb741a4562622857a79f5101c837e577b` |
| `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md` | full | `1d584c83d685cd78b7279476cb730556063b2351714379e50ae9b6dfae670d0c` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-97_RULING_RELEASE_PREPARATION_2026-08-17.md` | full | `1493bca33fa67e3f89f95904efdf9ac9ba5f7bdb0a856f69f810980b43a453cc` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-125_RULING_APP_V3_CONTRACT_FINALIZATION_2026-09-06.md` | full | `9f2e8dcc5fd7706c8ed56c3c0d86535d52ce4874b28cf9dd9fbc5934b7890327` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-126_RULING_CREDENTIAL_CUSTODY_BOOTSTRAP_AND_LOGOUT_2026-09-06.md` | full | `4480ad2e70bfcac6487980d9a310ae52720cb472c10467897d97aaf184e55a73` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md` | full | `211ce2d25fde94c2c88c7b688a530e697b1b923efffaaaf18f39db414f494c19` |
| `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` | full | `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899` |
| `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md` | ruling items 1–14 and closure gates | `5afadb4ac0d33c26d188abbd86508de31dd08a027bd7858005273a11eab784cc` |
| `docs/governance_harness/_DECISIONS/_REGISTER.md` | keyword search | `7dbe338827fb4988e6b6151b79a97ffdc667ad167b07d69b9df66bb4564b106b` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md` | full | `218c8e326ec78e07c0a8d38f969b78a58ba41b29510d19979c8ff5e8733a4408` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_DIRECT_TRIAL_20260910/HANDOFF.md` | full | `294c28a698bcbafa1bce930c8051e61f0bb723131cd1c55f5b498de2fbde1f22` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_DIRECT_TRIAL_20260910/REBUILD_PLAN.md` | keyword search | `b7a0ccbf53071e775516a3e9ec8138efb48c9537ff6fde22001bc770b51d3389` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md` | full | `084027ebe6ed95a65df7d712126bfd91447b91eff4472ad1acabeec345177e5e` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PERSPECTIVE.md` | full | `488ff935b9e7d3d8d5e9089755d73e1e91c99f4ed2e35b77569897573c043569` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/RUN_LOG.md` | S-check and build entries | `591e6dd8324df4ef68b3b1e515b32f4d0632905d3d6d8ed00ac57b87fde617e5` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/RUN_LOG.md` | keyword search | `05f020f358dda8c3ae809a3a54163d847bfbf3d1b7b0a1e6da68276cc1e31d35` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/BUILD_EVIDENCE_20260912.md` | keyword search | `34678a063ba53f7deeafdc8a6cfd85d25cea1cb1922fc3e842e6c4ebb6604dee` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/OWNER_HANDOFF_20260912.md` | keyword search | `f5951c61cfd842e6e9ccc8cabeca1f884e1972b143ba9745577d7e18dc2a9ea8` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PLAN.md` | full | `5c7fb1de448646fd5bde0350f551b986308817c33c1ad30778c47dc09c81dc81` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/RUN_LOG.md` | owner/release entries | `10ad53df97b4c61ad1cdf5865efb2a53504898cd0926fca1e99ba62033d81869` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md` | full | `b2b0bab9b1af29da9a8eeb6f67fa1c1646a0db7d726a07db5907942846760043` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/OWNER_TRIAL_NOTES.md` | full | `7a318e20040fd17d232b5af0f5f8459c5066cb4f31dcdeae1927bd4751e0df2c` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/NEXT_AGENT_HANDOFF.md` | opening sections | `f3396117583c2d76bb118a4a5efac3f31056b74efef3619dc14ae6bfc51e3890` |
| `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` | Owner-Direction records; receipts 255–263 | `e8b255bf64e644faccf3e618c3056f271f60cf1ad418f4a6850680c64e3a3b36` |
| `plans/steers/chirality_app_v3_g2_acceptance_transcription_steer_root_2026-08-25.md` | scanned (keyword search for plan amendments/owner text) | `a0d14e05b7749c06605bdfce5d978058b4bea999569f94d0a918a5f2bad6eb76` |
| `plans/steers/chirality_app_v3_gate5_steer_app_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `1dfe6492f97d76d7cb57d44f4ba6f37c5011fc56c918149230800883326cf299` |
| `plans/steers/chirality_app_v3_kcontrol1_amendment_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `c0a9b1098fc9e36d1532dc1834424ee94f40b716d37f3c8b8c12dfb26a807c29` |
| `plans/steers/chirality_app_v3_notice_ingestion_steer_root_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `4c9bc1cd6382a47eb5ef1bd56f7aa9d6fa2cce2dda08bd1aded2b2f352a2c2c2` |
| `plans/steers/chirality_app_v3_phase0_steer_app_2026-08-22.md` | scanned (keyword search for plan amendments/owner text) | `0792a9d0c718b9b6ea7f6897570ec440a1dc46a4c539db588aaab123ba1088d4` |
| `plans/steers/chirality_app_v3_phase0_steer_app_reissued_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `fef516fda00a713785dd1cbfa38e4fdcea30ce2edfa0a265b81754fa84e86ab0` |
| `plans/steers/chirality_app_v3_phase0_steer_root_2026-08-22.md` | scanned (keyword search for plan amendments/owner text) | `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3` |
| `plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md` | scanned (keyword search for plan amendments/owner text) | `c4b674327b78434561a42f93b8bb34e50921281459ec00ca6c8afaaa9ebb80e2` |
| `plans/steers/chirality_app_v3_phase0c_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `ef2ffa62949b870671ccd00d2384429a0b1c97bb9d52259034448c6662cd0eca` |
| `plans/steers/chirality_app_v3_phase0d_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `68e6656f6163c13ffcd600473d7ff0a351ea0262feabc1de5e5b1793eaf3d7ed` |
| `plans/steers/chirality_app_v3_phase0e_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `ad97af5e1871a01df87930777717f4325f8dac7019a25731e386261b7ca16eb4` |
| `plans/steers/chirality_app_v3_phase0f_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `3c94f224578ee8187cfd8d6dda6e005d56b711a303994d26c1fef6c56bde7089` |
| `plans/steers/chirality_app_v3_phase0g_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `40f746f2c7534df4b2290349b0fb8a952a8d9153c287d8bf3b725669955b60ba` |
| `plans/steers/chirality_app_v3_phase1_steer_app_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `7d700af0b05c754e468d958a7580fff713f743ad789540d8c4176bf8711ed394` |
| `plans/steers/chirality_app_v3_phase1_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `2bbd449330b25d2ab88cec4097d3e224b95305954d30196e94fbd21c21062452` |
| `plans/steers/chirality_app_v3_phase2_steer_app_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `5cd8e4ac4b6d77a2672f70218e27e18bfd3ac7cf5d1ddc57af608991260d9a5e` |
| `plans/steers/chirality_app_v3_phase2_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `bf58c6224e4649038d6faafc4a5125c20042a741f521e992f26b77b00f41d0c3` |
| `plans/steers/chirality_app_v3_phase2b_steer_app_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `41580e3b2079388873e8bcc56552bc59bc343674c5454915fe383eadc7417fda` |
| `plans/steers/chirality_app_v3_phase3_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `9c8d3884f97733f674269014c1735977c9628be1d929f6859889c79710ae4186` |
| `plans/steers/chirality_app_v3_phase4_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `54595fe5060bed81fb9b871d623d15505ee7ff42b4e7349d238b9c4d0f9cc644` |
| `plans/steers/chirality_app_v3_phase5_steer_root_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `3bb377aa8bb162fb1d596505e908e1c720e4e4a9344d6d53aac5e9eaf44ac1a9` |
| `plans/steers/chirality_app_v3_pointer_act_steer_app_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `ac7920b2adcf2d77835cb4989b956d1be4ae7c97fb70839c4e25fe83ffbcd5c1` |
| `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md` | scanned (keyword search for plan amendments/owner text) | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| `plans/steers/chirality_app_v3_r17_pathway_seating_steer_root_2026-08-27.md` | scanned (keyword search for plan amendments/owner text) | `8e96c8fc37e5ac21d93b846a2f1efce15fe6564ebad6fe07334571f473339de6` |
| `plans/steers/chirality_app_v3_r18_notice_ingestion_steer_root_2026-09-03.md` | scanned (keyword search for plan amendments/owner text) | `757b718a83affd25196f065149bd5a972ec61ad2582ab24c81a6ebe38a71c633` |
| `plans/steers/chirality_app_v3_r9_transcription_steer_root_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `b8683bba0495a199de8b3a7c9d237165685c3d75bd01a8a91b3e4a28ea1ead9b` |
| `plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391` |
| `plans/steers/chirality_app_v3_supply_resume2_steer_root_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164` |
| `plans/steers/chirality_app_v3_supply_resume_steer_root_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701` |
| `plans/steers/chirality_app_v3_tm_triage_steer_app_2026-08-24.md` | scanned (keyword search for plan amendments/owner text) | `8b7319421ddb09568fc02a2e5c0750ac725a81fafb6491951f396509e897373b` |
| `plans/steers/chirality_app_v3_concordance_inputs_2026-08-23.md` | scanned (keyword search for plan amendments/owner text) | `4d16cefae5dc672376a62ae00437c27ff857e7d994206549e888da3409f40c2a` |

The steer files marked "scanned" contain phase and gate instructions. Their plan
amendments reproduce the G0 record, which is cited directly. HELP_HUMAN named the
D-GOV-43 decision record, its proposal ruling items and the decision register
through D-APP-127, so they were consulted beyond the brief's list. The decision
register was used only to look up the D-GOV-20 and D-GOV-36 to D-GOV-43 rows.
