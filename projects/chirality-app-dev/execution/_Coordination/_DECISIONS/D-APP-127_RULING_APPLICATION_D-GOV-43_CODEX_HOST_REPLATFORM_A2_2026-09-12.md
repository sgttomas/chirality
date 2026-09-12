# D-APP-127: Application of D-GOV-43 (Codex host re-platform, topology A2) to the App loop

Status: `RULING APPLICATION 2026-09-12` under D-GOV-43 item 11. This is not a
new owner ruling and grants no authority beyond the D-GOV-43 record and its A2
supplement. It records which parts of six earlier App decisions are
superseded and what replaces them. None of those records is edited.

Owning ruling: `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`
(ruled 2026-09-11); supplement `D-GOV-43_supplement_topology_A2.md` (recorded
2026-09-12). Publication SHA of both on `main`:
`d2878462be59a43b4afc175a8cce85abca9cf696` (PR #767). Implementation entry:
`execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md`.

## Owner ruling (verbatim, from the D-GOV-43 record)

> I rule D-GOV-43 accepted as revision 3 at commit 3ef2ef524, with the
> post-build minimum-not-ceiling clarification. The three folded choices
> stand.

Topology selection (verbatim, from the A2 supplement):

> We are all in agreement this is the path forward. You will be handing
> this off so a third agent can begin implementation.

## Authority for this record

D-GOV-43 item 11 authorizes, together with the Root amendments, "the Runtime
and App contract, scope, deliverable, hold and notice changes named in
`IMPACT.md`", applied in one coordinated tranche. `IMPACT.md` names the six
App records below for supersession "by one App decision record under this
ruling; never silently drop". This record is that application. Notices record
it; they do not reopen approval.

## Governing facts applied

- Topology A2: the App starts, owns and stops a simplified Runtime service
  child; the service speaks its existing Unix-socket API with client tokens
  private to the application (no TCP) and owns the stock, version-pinned
  `codex app-server` child. The socket API, client, harness port and Next
  routes are retained and repaired: loopback HTTP and SSE through the
  in-process Next server remain the renderer channel; the SSE keepalive,
  timeout and disconnect defects are repaired; a renderer disconnect no
  longer interrupts a turn.
- Retired: the LaunchAgent and installer (DEL-09-07, APP-HOLD-1), hosted
  admission, identity binding, restart admission, the native admission addon,
  the host-account XPC channel, supplier containment evidence,
  packaged-basis hashing, the Stage 9 to 13 packaging spine, the per-chat
  model and effort freeze, and the closed event vocabulary.
- Families (IMPACT.md purpose test): 1 and 2 retire; 3 adapts; 4 retains; 5
  retires as gates; 6 retains.
- Daemon-era trial chats and executed records are preserved unchanged; the
  new procedures supersede applicability.

## Superseded parts and replacements

### D-APP-125 (App v3 contract finalization directions, 2026-09-06), item 3 only

Superseded: item 3, "Select A2 shared-login brokerage DESIGN preserving
isolated homes and per-root consent. Finalize custody/epochs/switch/logout/
revocation/readiness and affected-client contracts". The design label "A2"
in that item is a slate option, unrelated to topology A2 of the supplement.
The isolated per-root homes, per-root consent, brokerage custody epochs,
switch and revocation contracts and the affected-client contracts are
retired with hosted admission (family 3 adapts its purpose).

Replaced by D-GOV-43 items 3 and 6: one Chirality-owned effective Codex home
that shares the user's configuration and resources by reference and keeps
`auth.json` and the models cache private; sign-in through Codex's own
`account/login/start`, `account/login/cancel` and `account/logout`; the
credential backend verified so that Chirality sign-in and sign-out leave
another Codex client's state unchanged (S-8). Item 3's clauses "no token
copying" and no "ambient authority" carry forward unchanged as "Chirality
never copies credentials".

Not superseded: items 1, 2, 4 and 5. Item 2 (a separate whole-turn Stop,
never a per-request Deny substitute) is consistent with the disconnection
rule and stands. Item 4's "isolated app-managed no-folder" design and its
blocked no-folder behaviour stand as owner directions and are read with
D-GOV-43 item 3 where they use the private-home vocabulary. Item 1 and item 5
are unaffected.

### D-APP-126 (credential custody, bootstrap and logout dispositions, 2026-09-06), all three selected boundaries on the App path

Superseded: boundary 1 (the daemon-owned trusted-supplier authentication
process with a configured built-in keyring as an exception to Electron
`safeStorage`, per-root independent acquisition); boundary 2 (the
account-only nonexecuting bootstrap namespace for sign-in before folder
selection); boundary 3 (global account switch or sign-out fencing every
hosted context in the active generation, with the remote-revoke cleanup
order). The routed Root D-GOV-36 custody exception these boundaries rest on
is superseded by D-GOV-43 on the App path, as the D-GOV-43 record states.

Replaced by D-GOV-43 items 3 and 6: credentials are custodied by Codex in the
private `auth.json` of the effective home (`cli_auth_credentials_store=file`,
verified in S-8); the App never reads, copies or relays credential material;
sign-in and sign-out use Codex's own account methods; sign-out scoped to
Chirality leaves other Codex clients unchanged; no bootstrap namespace, no
generation fencing and no remote-revoke ordering are re-created. The product
target "one OpenAI sign-in experience" survives as the S-8 check; "independent
consent for each folder" retires with hosted admission. The exact
qualification and custom-adapter conditions of D-APP-126 no longer apply.

### D-APP-122 (account and Settings host prerequisite, 2026-09-06), the host-gated and daemon-target parts

Superseded: the daemon target of the account row, popover and Settings
actions ("existing actions retain their true daemon target"); the
STATUS_TRUTHFULNESS_ADDENDUM statements about daemon running or residency
and external oMLX server availability (residency retired by D-GOV-43 item
13); the DEL-02-05-V3-03 gate on the Root DEL-02-09 account and consent
contract and the G3, G-CSP and G4 host gates for live-login claims; and the
A1 re-stage rule with its fresh owner proof for future live-login claims.

Replaced by: the account row and Settings act on the application-owned
Runtime service child and Codex's own login flow; live-login evidence is S-8
on the production path and after the consolidated signed build; the affected-
check rule of the D-GOV-43 clarification (repeat a check when a source,
configuration or packaging change invalidates its earlier evidence) replaces
the A1 re-stage rule.

Not superseded: the selection of the DEL-02-01 account-row host and the
right-panel Settings host as presentation loci (merged in PR #745), the
labelled fake and unavailable states with no live-login claim until S-8
evidence exists, no secret exposure in the renderer, and one ChatPanel and
one runtime controller serving the presentation.

### D-APP-100 (packaged daemon instruction-root resolution, 2026-08-17), the packaged-daemon subject

Superseded: the subject "packaged daemon" and the regression that "app, CLI,
and packaged daemon agree on the resolved root", and the packaged-under-
isolation proof. There is no packaged daemon; the Runtime CLI's compatibility
is unverified and not an MVP prerequisite (A2 supplement).

Replaced by: the application-owned Runtime service child resolves the
instruction root the same way the App does, from the bundled instruction
root; a logged fallback to the packaged resources path only when no manifest
root resolves carries forward as engineering guidance; `instruction-root:integrity`
is the relevant check for packaged instruction roots under the new
packaging procedure (`AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`).
The DEL-09-04 Remaining item that D-APP-100 authorized is revised accordingly.

### D-APP-88 (distinct daemon helper bundle identity, 2026-08-02; concluded 2026-08-13), the helper bundle and LaunchAgent target

Superseded: the headless helper `.app` with a distinct `CFBundleIdentifier`
and `LSUIElement` posture, the LaunchAgent pointed at the helper executable,
one Root runtime daemon continuity, CLI binding and login-time `RunAtLoad`
proof obligations, and TM-APP-030 (G-HELPER) as a release consideration.

Replaced by: the Runtime service runs as a child process of the Electron
main process with no LaunchAgent and no separate launchd bundle identity;
process ownership, orphan protection, restart with backoff and a deliberate
stop on quit are engineering responsibilities of the App (HANDOFF section 3).

Not superseded: the concluded engineering finding of 2026-08-13 (no SIGTERM
handler bound in the shipped helper, combined with the retired `before-quit`
veto) and the PR #552 signal binder, bounded teardown and held-connection
regression, which remain history and inform the child's `teardown()` on quit.
D-APP-93's disposition is unaffected.

### D-APP-107 (DEL-09-07 Scope of Work initialization, 2026-09-04), in whole

Superseded: the `SOW_INITIALIZATION` admission for DEL-09-07, the
PROJECT_SETUP Phase 2.2 resumption, and the exact preflight token
`PROJECT_SETUP:SCOPE_OF_WORK:INIT`. DEL-09-07 (two-job runtime-control
installer, migration and rollback) retires with the LaunchAgent under
D-GOV-43 item 7 and IMPACT.md chain 2 (family 1).

Replaced by: nothing is re-created. The live `APP-HOLD-1-INIT-DEL-09-07` row
is retired from `execution/_Coordination/APP_HOLD_REGISTER.csv` by removal,
the loop's existing retirement mechanism (D-APP-107 retired the expired
D-APP-104 row the same way); `app_hold.py` accepts no other terminal state.
Rationale: the hold's subject, the LaunchAgent installer, no longer exists on
the App path. The DEL-09-07 folder, its ScopeOfWork and D-APP-104 remain
immutable history; DEL-09-07 `_STATUS.md` records the retirement. The
D-APP-107 preflight paragraph in `projects/chirality-app-dev/AGENTS.md` is
outside this record's write scope and is flagged for revision in the
tranche return.

## Consequential applications recorded with this decision

- SCA-APP-008 revised before any acceptance (revision note in the packet).
- PKG-09 DEL-09-03 V3-02 re-pointed; DEL-09-04, DEL-09-05, DEL-09-06 revised;
  DEL-09-07 retired.
- PKG-03 DEL-03-01 to DEL-03-04, PKG-05 DEL-05-02 and PKG-02 DEL-02-05
  architecture-bound clauses revised.
- Supersession headers on the notices named in IMPACT.md; new App and PEC
  notices recording the application.
- `PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md` under
  `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/` supersede the
  applicability of the Stage 9 to 13 spine and the R15 to R17 checklists.

## Boundary

No release, publishing, trial acceptance, change to the Codex sole-engine
rule, local-model work or reliance on the retired daemon path is authorized.
Material scope or behaviour changes and consequential findings return to the
owner; routine implementation choices do not. Prepared by a bounded TASK
executor under the App loop's WORKING_ITEMS coordination; the owner has not
personally reviewed this text.
