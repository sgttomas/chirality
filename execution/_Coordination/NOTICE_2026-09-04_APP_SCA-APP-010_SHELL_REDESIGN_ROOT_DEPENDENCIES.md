# NOTICE TO ROOT — SCA-APP-010 Shell Redesign: Root-Owned Dependencies

**Status:** `ROUTED`
**Notice class:** cross-loop coordination, not authority
**Routing state:** `ROUTED_TO_ROOT_SURFACE_2026-09-04` (owner-authorized; App ruling record D-APP-108, Q8)
**Supersedes for routing:** the frozen draft `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/DRAFT_NOTICE_TO_ROOT.md`, SHA-256 `f197b31e80ec71e46858bc84bb5d00941c01882e66e16c18115bffc14eaa5c5d` (immutable snapshot evidence; not itself routed)
**Write ID:** SCA-APP-010 `FUTURE_WRITE_SET.csv` N-001; `OWNER_ACTION_MATRIX.csv` step 21; `DOWNSTREAM_HANDOFFS.csv` row 7

## Routing authorization

The App owner authorized routing on 2026-09-04 by selecting, for question Q8
of `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` §6, the option
"Raise now via the SCA-APP-010 Root notice (Recommended)", presented with the
description: "The drafted notice already names Root DEL-02-09's login home as
an OI-008 dependency. Choosing this also authorizes routing that notice into
execution/_Coordination/ in this pass. Root's cadence is the slow path; starting
it now is principle (b), discharging a gate early." The selection is transcribed
verbatim in the App ruling record
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md`.
The same owner granted HELP_HUMAN Root write scope for this work on 2026-09-04
(SCA-APP-010 `Decision_Log.md` G1-CONFIRM). This file is the only Root-surface
write of the routing act.

## Coordination notice

The App-dev loop's owner-approved SCA-APP-010 amends the App decomposition so
that the centre dialogue is the invariant primary surface, Workbench and
Pipeline presentation are retired from the active shell (code, routes, and
tests retained), and the prompted specification ladder (folder, agent,
permissions, delegation, optional governed workflow) is seated on existing App
carriers. Applied identities:

- SOFTWARE_DECOMP post-image SHA-256
  `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content
  commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged to `main` as PR #708
  merge `7795b0972cac147869607d994173753e4a2fc232`; Scope Ledger 80 → 84 rows
  (SOW-081 to SOW-084); topology unchanged (10 packages, 52 deliverables);
- companion invariant-coverage register post-image SHA-256
  `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`;
- active App scope-change pointer `execution/_ScopeChange/_LATEST.md` SHA-256
  `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`, moved to
  SCA-APP-010 as PR #711 merge `311a2f0b811d55315d6eb623130cad0be1417565`;
- App authority corpus v20 unchanged, no drift (the decomposition is not a
  corpus member).

Three App presentations depend on Root-owned semantics the App does not
define. The App records them as `OI-008` (`SHELL_LADDER_BOUNDARY`) and asks
Root only to note them as cross-loop coordination; acceptance, amendment, or
decline is a Root-loop act under Root's own instruments and cadence:

1. **App-wide account presentation over a root-private login home (SR-19).**
   App `DEL-02-05` presents one OpenAI account for the app and consent,
   network posture, and role per folder. `K-CONSENT-1` semantics and the
   port's per-root login semantics are unchanged. The root-private login home
   (`K-KEY-1`) and any shared-login contract remain Root `DEL-02-09`'s. App
   `DEL-02-05-V3-03` stays gated on that contract; App `DEL-02-05-V3-05`
   (seated 2026-09-04) ships the presentation on the fake consent port. The
   App owner has ruled (Q7, D-APP-108) that the account row shows only the
   local model server status and no OpenAI or API status indicator; that is
   an App presentation ruling and asks nothing of Root.
2. **Additive `proposal.*` event types.** App `SOW-082` consumes
   `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and
   `proposal.declined` in the session record. These are candidates against
   the closed `HarnessEvent` schema v2 (`K-EVENT-3`) owned by Root
   `DEL-02-10`. App `DEL-05-02-V3-02` (seated 2026-09-04) consumes them only
   after Root acceptance is routed back as a `NOTICE_*` on the App
   coordination surface; until then App `DEL-02-02-V3-04` renders the proposal
   card over fixtures and makes no live-event claim.
3. **Per-chat delegation policy on the session record.** App `SOW-083` binds
   a delegation policy (`none` by default; ask before each brief; approve each
   brief's writes; bounded briefs) in the boot request (App `DEL-03-02-V3-01`)
   and honours it in the App-managed delegation bridge (App `DEL-08-04-V3-02`)
   as a narrowing input that adds no delegation class. The stored field on the
   daemon-owned session record is Root `DEL-02-11`'s; the App carries the
   policy in App-side session state until Root accepts a stored field.

No Root action is requested beyond recording these dependencies. The App adds
no delegation class, no tool outside its in-process deterministic boundary, no
provider or network change, no signing, notarization, distribution, or release
act, and no change to any Root register, contract, decomposition, or pointer.

## Requested Root handling after routing

The Root loop may record the App identities and the three dependencies as
cross-loop coordination and surface any exact Root/App contract drift. When
Root accepts, amends, or declines any of the three, the App asks only that the
result be routed back as a notice on
`projects/chirality-app-dev/execution/_Coordination/`, which is how the App
items' `NOT_SELECTABLE_UNTIL` states resolve. The Root loop adopts, amends, or
declines under its own instruments and cadence; this notice is not Root
authority and does not request a Root contract, schedule-basis, lifecycle,
implementation, or release change.

## Exclusions

This notice is not App or Root authority; it does not activate
implementation, alter either loop's contract or scope ledger, move any
pointer, close SCA-APP-010's derivative packages, or claim release readiness.

## Attribution

Routed by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) in an untyped Claude
Code session acting as HELP_HUMAN (Agent 0) on the owner's authorization;
role not mechanically enforced. App run evidence:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`.
