# D-APP-92 — Native Signal Trace and Sealed Replay Authorization

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-04 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Predecessor:** D-APP-88 Option B ruling SHA-256
`858a0d4be9adfca1adf5b990df672fa69000e41a0d840894164d99b382e196c6`.

## 1. Decision requested

Whether and how to grant the next causal proof step for the still-open
D-APP-88 distinct-helper implementation after the verified R3 blocker.

This is owner-class because interactive native tracing introduces a new
tool/privilege/entitlement exposure beyond the currently approved D-APP-88
item. The packet does not select a product remedy or weaken the mandatory
post-GUI first-signal gate.

## 2. Exact evidence basis

Complete R3 derivative proof root:
`execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/`.

| Evidence | SHA-256 | Material result |
|---|---|---|
| D-APP-88 packet | `853d9ef60a91d461d6477842dd51fccdde4204fafbe978f7d915b821d6257f95` | selected helper identity/package/live-proof contract |
| Root TM-ROOT-112 notice | `1029648d039edd3c0449d0bea867853b033cc457a4b1f477c458dd4e127a6ed3` | coordination releases App evaluation; no App causality or acceptance |
| R3 `ROOT_EVIDENCE_FITNESS.md` | `1c80b8b5739404fa6d37797304f57109d0c390b16f296186e95c4118c569910b` | accepted Root repair satisfies the earlier rerun prerequisite only |
| implementer-02 `RETURN.md` | `df18333874028dddf8e1b08218fb5d6751e30bbd4a20167f11bdd0f2d453143a` | uninstrumented first-signal failure; product rollback |
| `evidence/FIRST_SIGNAL_PROOF.md` | `a81cdd7f03db0d2982aff5034864f3395b07a12f5560dcf05ea7df87ed20f9ec` | authenticated GUI contact; 80 polls; helper/socket/owner unchanged; no teardown |
| exact-matrix `RETURN.md` | `4101c5c3688de1ab4d8bc56bc675b4d7d9a69396fffb2aaaf45061928acd3b4e` | SINGLE and STANDARD instrumented controls passed identically |
| exact `CAUSAL_MATRIX.md` | `e5635b6f38e7d67f8ced73e8f392cf5881bf07aab5852aa3e0fc9af916cf67be` | switch deletion unsupported; synchronous logger may perturb absolute behavior |
| verifier-02 `RETURN.md` | `ef3e26b61965adbf2e0c3e39710f6a099286c1173eb7be6207fcfe2b3ef9605c` | PASS for calibrated blocker/handoff only; repaired identity |
| R3 `VALIDATION.md` | `32e99f44e93482d901282665f996f0bc7624ded466088ebf1e8141342547af85` | blocked handoff validated; implementation not accepted |
| R3 `MANAGER_RETURN.md` | `7f7d7db25f3f6b59f16f045271cd167804644cda10d99be6f89d75e4abda426e` | exact owner-authority prerequisite |
| R3 `HANDOFF_STATE.md` | `2cffbefa20dfc930f393036d50c4787bd592ab3a1854abded1bf681bb6782e9c` | rerun held pending native trace plus sealed replay |

These R3 artifacts are derivative evidence, not product or decomposition
truth. Their fresh verifier PASS accepts the blocker/handoff only.

## 3. Current finding and mandatory gate

The exact uninstrumented helper failed the authenticated post-GUI first
`SIGTERM`: helper and GUI remained alive after 80 0.1-second polls, the socket
and owner inodes were unchanged, no App shutdown-start entry existed, and Root
stop was not entered.

Later exact instrumented SINGLE and STANDARD packages both passed pre-GUI and
post-GUI first-signal controls identically. That comparison excludes removal
of `single-process` as a supported cause or remedy. Its common synchronous
logger may perturb absolute signal/lifecycle timing, so it does not explain or
erase the earlier uninstrumented failure.

The D-APP-88 acceptance conjunction remains unchanged: the first ordinary
authenticated post-GUI signal must enter App teardown and bounded Root stop,
exit the helper, and remove socket/owner state. Repetition, instrumentation,
or owner selection cannot waive that gate.

## 4. Options

### Option A — Bounded interactive native signal trace and sealed uninstrumented replay (recommended)

Authorize one diagnostic-only tranche that:

1. runs in an interactive macOS GUI session against an isolated HOME/userData;
2. reconstructs the exact source-aligned uninstrumented helper candidate and
   binds source, package, identity, topology, and dependency hashes before use;
3. seals a replay transcript fixing stale-owner recovery, helper launch,
   helper-to-GUI delay, authenticated contact, contact-to-signal delay,
   snapshot sequence, exact first signal, bounded polls, and cleanup;
4. uses out-of-process native/Electron signal tracing without changing App
   product bytes or adding callback logging;
5. binds trace records to exact PIDs and time and distinguishes, where the
   selected tracing capability can do so, OS signal delivery, libuv/JS
   callback entry, Electron `before-quit`, teardown entry, and Root-stop
   call/settlement; and
6. freezes raw evidence, returns limitations, removes generated/runtime
   residue, and restores every product/config/test byte.

Every tracing command and tool must be individually enumerated in the sealed
execution brief. No generic shell/tracing grant follows. Any command requiring
elevation, privilege, or entitlement must receive separate command-level
approval before invocation; no persistent entitlement change, SIP/security
posture change, signing identity, or broad administrative grant is authorized.

Credential access is prohibited. The replay may exercise the existing
authenticated registration path without reading, printing, exporting, or
recording any token, keychain item, API key, secret, or credential value.
Only public identifiers, paths, result codes, and redacted state evidence may
be retained.

Effect if ruled: authorizes this causal diagnostic only. A supported cause is
returned as evidence for a later governed remedy/implementation step. No
source remedy, D-APP-88 acceptance, or deliverable closure is automatic.

### Option B — Sealed uninstrumented repetition without native tracing

Authorize the same exact uninstrumented reconstruction, sealed replay inputs,
ordinary process/socket/owner snapshots, first signal, bounded polls, evidence
freeze, cleanup, and rollback, but authorize no new native tracing tool,
privilege, or entitlement.

This can show whether the prior outcome repeats and can calibrate observed
frequency/timing. It cannot by itself distinguish OS delivery, libuv/JS
callback entry, Electron lifecycle entry, teardown, or Root-stop entry.
Therefore an Option B pass or failure is lower-value, non-causal evidence and
cannot by itself support a product remedy, D-APP-88 acceptance, or DEL-09-04
closure.

Effect if ruled: authorizes repetition evidence only. The mandatory
first-signal gate and owner-authority prerequisite for any later native tracing
remain open.

### Option C — Defer and park the trace/replay step

Authorize no new trace or replay. Keep D-APP-88 implementation open and
DEL-09-04 `IN_PROGRESS`. The rolled-back D-APP-89 source baseline and current
shared-identity recovery behavior remain operative; neither is accepted as a
permanent D-APP-88 remedy.

Effect if ruled: park until the owner names a concrete trigger. No closure or
acceptance follows from elapsed time.

## 5. Non-binding recommendation

Recommend **Option A**.

R3 exhausted the source-instrumented relative comparison that remained within
existing authority. The exact uninstrumented failure and the both-pass
instrumented controls are simultaneously valid, and synchronous callback
logging may itself change timing. A bounded out-of-process native trace paired
with a sealed exact uninstrumented replay directly addresses the remaining
causal gap. Option B can add recurrence evidence but cannot locate the seam;
Option C is coherent if the owner declines the new exposure now.

This recommendation is agent-authored and non-binding. It selects no option.

## 6. Preserved authority and limitations

- Root TM-ROOT-112 remains accepted upstream graceful-stop evidence. Its App
  notice is coordination, not App authority, and proves no R2/R3 causality,
  Electron signal behavior, App acceptance, or parity result.
- D-APP-89 remains the product/source baseline. No R3 candidate byte remains
  authoritative product state.
- D-APP-91 remains a planning baseline only. Its TM-PIP-025 rider remains an
  operative condition on the first-domain exact-requirements packet, including
  reverification if the bound Piping runtime-surface basis is materially
  amended.
- The six D-APP-81 rows remain literal `HISTORICAL_RELATION_UNKNOWN` at ledger
  SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`.
- Node 22.19 remains unexecuted. safeStorage was not rerun on the owner
  keychain. Managed-service premerge, overall release-quality, and
  practitioner-environment failures retain no PASS or release credit.
- D-APP-88 implementation remains open; DEL-09-04 remains `IN_PROGRESS`; the
  mandatory first-signal residual remains; TM-APP-036 does not fire.
- No option authorizes a wrapper, supervisor, extra singleton/daemon, generic
  Root change, first-signal-gate weakening, product remedy, credential access,
  release, signing, notarization, publication, distribution, or reliance.

## 7. Validation and affected surfaces

If Option A or B is later ruled, its executing manager must return:

- the exact owner ruling and sealed brief;
- enumerated tools/commands and, for A, every privilege/entitlement decision;
- source/package/dependency/identity manifests;
- the sealed replay transcript and exact deviations;
- process/socket/owner/descriptor/timing and first-signal evidence;
- for A, raw trace evidence and a supported-versus-unknown causal matrix;
- cleanup/rollback manifests and source-state reproduction;
- Node/safeStorage/premerge/release-quality/practitioner limitations; and
- a genuinely fresh adversarial verdict before any acceptance or next-step
  claim.

Affected surfaces are limited to a fresh run/evidence root and temporary
reconstruction/runtime state explicitly granted by the later ruling and brief.
No standing tracing configuration or permanent product change is proposed.

## 8. No-effect boundary

This proposal and its register row create no tracing permission, privilege,
entitlement, replay dispatch, product/source/config/test change, remedy,
D-APP-88 or DEL-09-04 closure, TM-APP-036 firing, Root/Piping/PEC authority,
PRD/decomposition/SCOPE_CHANGE, packaging identity adoption, generic-runtime
semantic, lifecycle, release, reliance, receipt, Git, or professional-
acceptance effect.

## 9. Owner return tokens

- `APPROVE D-APP-92 OPTION A — BOUNDED INTERACTIVE NATIVE SIGNAL TRACE AND SEALED UNINSTRUMENTED REPLAY`
- `APPROVE D-APP-92 OPTION B — SEALED UNINSTRUMENTED REPETITION WITHOUT NATIVE TRACING`
- `DEFER D-APP-92 OPTION C — TRIGGER: <exact trigger>`
