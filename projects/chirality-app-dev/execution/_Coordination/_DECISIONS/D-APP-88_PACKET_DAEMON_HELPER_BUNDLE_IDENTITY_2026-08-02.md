# D-APP-88 — Daemon/Helper Bundle Identity

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-02 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Task Management link:** `TM-APP-030`

## 1. Decision requested

Choose the App packaging posture for the headless daemon while the Desktop GUI
and daemon currently execute from one Electron app bundle and therefore share
one macOS bundle identity.

## 2. Current evidence

| Evidence | SHA-256 | Current fact used |
|---|---|---|
| DEL-09-04 `_STATUS.md` | `cd859e53e4c43ffb45706b3234b5d33a7d88ee91f4dc923d9a4c70cebfdf4207` | LaunchServices may resolve an ordinary app launch to the running headless daemon. Current handling opens the GUI, retires the daemon, and self-heals through the LaunchAgent throttle interval. |
| OD6 `FINDINGS.csv`, `OD6-017` | `dcfd8289ec78e31c933993e460deaca00ad3a69e536a3646479ed7c334da7ed8` | Recovery is evidenced; separate helper identity remains an App owner-choice residual. |
| OD6 `returns/A2-RUNTIME-CONSUMERS/RETURN.md` | basis-bound derivative evidence | The App is both daemon packager and client; shared identity is a packaging/lifecycle residual, not evidence of a second runtime. |
| DEL-09-04 `_run_records/R6_DAEMON_SERVICE_2026-07-25.md` | accepted deliverable-local evidence | Isolated packaged drills established daemon startup, recovery, safeStorage, CLI, and one scripted turn; no distinct helper bundle was created. |

The causal fix already identified by DEL-09-04 is a helper `.app` with its own
`CFBundleIdentifier` and `LSUIElement`, with the LaunchAgent invoking that
helper. This packet neither assumes that fix nor converts recovery evidence
into owner acceptance of the current behavior.

## 3. Options

### Option A — Retain the shared identity as accepted bounded behavior

Rule that the present self-healing bounce is acceptable for this product
generation. Keep one app bundle and the current `--runtime-daemon` posture.
Close only the helper-identity decision residual; retain all unrelated
DEL-09-04 items, including stale-socket, premerge, deployment, instruction-root,
login-time, packaging, and release-preparation residuals.

Implementation effect after the ruling is documentation/state closeout only.
No claim may say that GUI and daemon identities are distinct.

### Option B — Require a distinct headless helper bundle (recommended)

Select a bounded App packaging tranche that:

- builds a helper `.app` inside the unsigned local Desktop package;
- assigns it a distinct `CFBundleIdentifier` and `LSUIElement` posture;
- points the LaunchAgent at the helper executable rather than the GUI bundle;
- preserves one Root runtime daemon, the existing socket/auth/session stores,
  project registration, CLI behavior, and graceful/recover-on-start semantics;
  and
- keeps the ordinary Chirality app identity and GUI launch behavior separate.

The implementation must return exact proposed bundle identifiers, output
paths, plist changes, rollback bytes, and package evidence before closeout.
Selection does not authorize release or a Root generic-runtime change.

### Option C — Defer

Keep the present self-healing shared identity and keep the residual open.
Name a trigger such as the next packaging-identity tranche or release
preparation. Existing recovery remains evidence of bounded behavior, not a
decision that the behavior is acceptable indefinitely.

## 4. Evidence and validation for Option B

The execution package must include:

1. an exact source/commit and package manifest;
2. GUI and helper `Info.plist` extracts showing distinct identifiers and the
   helper's UI-element posture;
3. the installed LaunchAgent plist showing the helper executable path;
4. isolated packaged drills proving:
   - login/job launch starts only the helper/daemon posture;
   - opening Chirality from Finder or the Dock opens the GUI without retiring
     or replacing a healthy daemon;
   - GUI and CLI bind to the same daemon-owned session/auth stores;
   - graceful restart and SIGKILL recover-on-start behavior remain bounded;
   - no TCP listener, token disclosure, extra runtime singleton, or global
     Node dependency is introduced; and
5. artifact hashes, cleanup results, known limitations, rollback steps, and a
   deliverable-local run-record pointer.

Minimum command family, from `frontend/`:

- focused Vitest for `desktop-daemon-posture`, runtime-control IPC,
  CLI-launcher, and Desktop/CLI shared-daemon integration;
- `npm run typecheck`;
- `npm run build`;
- `npm run desktop:pack`;
- `npm run instruction-root:integrity`;
- `npm run harness:validate:premerge` against the isolated package; and
- `npm run validate:release-quality` plus the standing loop closeout checks.

DMG evidence is not required unless a separately ruled packaging tranche puts
DMG behavior in scope. Signing, notarization, publication, and distribution
remain prohibited.

## 5. Dependencies, risks, and non-effects

- Option B changes App packaging identity and launch topology, not Root runtime
  semantics. Any discovered need to alter the generic daemon contract returns
  to Root rather than being absorbed here.
- A distinct helper increases build/packaging complexity and requires explicit
  safeStorage/resource-root verification for the helper process.
- Option A preserves a visible launch bounce and therefore trades simplicity
  for a bounded but user-observable lifecycle discontinuity.
- No option changes the SIGKILL residual, satisfies the release-quality
  premerge row, deploys to the owner's machine, changes instruction-root
  semantics, or grants release authority.
- No option grants Agent-2 Bash, provider/network expansion, lifecycle
  advancement, or professional reliance.
- The six D-APP-81 unknown historical relations remain untouched.

## 6. Non-binding recommendation

Select **Option B**. The live deliverable identifies the shared identity as
the cause, while current recovery only bounds the consequence. A distinct
helper identity removes the GUI/daemon LaunchServices ambiguity without
changing the one-daemon runtime architecture.

## 7. Owner return tokens

- `APPROVE D-APP-88 OPTION A`
- `APPROVE D-APP-88 OPTION B`
- `APPROVE D-APP-88 OPTION C — TRIGGER: <trigger>`
