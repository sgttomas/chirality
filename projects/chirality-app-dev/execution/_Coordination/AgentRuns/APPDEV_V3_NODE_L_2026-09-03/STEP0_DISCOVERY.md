# Step 0 — Discovery (recorded before any product edit)

Run: `APPDEV_V3_NODE_L_2026-09-03` · Date: 2026-09-03 · Executor: provider `OpenAI`, engine `Codex`, model `GPT-5 family (exact model identifier not exposed to the agent runtime)`; bounded ephemeral Agent 2 under HELP_HUMAN.

## Basis and live state

- Scratch worktree: `/private/tmp/chirality-app-v3-slate3-20260903/nodeL`; branch `codex/app-v3-nodeL-consent-fake-guards-2026-09-03`.
- `HEAD` and `origin/main` at dispatch: `fe0ce926d4475fa41cb91933ad1218b95083889b` (PR #690 merge), exactly the accepted basis.
- The committed-HEAD loader selects `loop/WORKPLAN_2026-09-03_app_dev_loop.md`, mode `100644`, blob `5049fdbd3018a11050b4f8013d73311346b843cc`; read with `git show HEAD:`.
- Receipt validator: PASS; current tail is Receipt 216. Authority corpus: PASS, v20, all eight members match, no drift.
- Pinned completion reference SHA-256: `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, matching the standing-plan pin.
- Practitioner status: PASS via the existing read-only repository Python environment; 53 deliverables are `IN_PROGRESS` and no harness-status finding is emitted.
- Harness self-check: PASS at the unchanged baseline (`INFO=14`, `NOT_APPLICABLE=1`, `REVIEW=4`, `WARN=43`). The first invocation with macOS `/usr/bin/python3` stopped because PyYAML was unavailable; rerunning the same repo command with the existing read-only repository venv interpreter succeeded. No dependency or primary-checkout file was changed.

## APP-HOLD-1 dispatch preflight

`python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-02-05` from the App working root returned exit 0, `verdict: ALLOW`, `hold_status: NOT_HELD`, and `contract_status: CLEAR`. Register SHA-256: `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint: `2e7de2397d081d2c68cff8441232f08e2146759a94f71eb49eb6bcb898e0b8cf`.

## Live item and dependency result

`DEL-02-05-V3-04` is `SELECTABLE`, depends only on landed V3-02, has no owner gate, and confines changes to the fake, optional fixtures, and their tests plus local records. `Dependencies.csv` / `_DEPENDENCIES.md` retain Root-owned `HostedEngineConsentPort` and G3/G-CSP/G4 constraints for the separate live V3-03 item; this fake-backed repair makes no live-account claim and does not consume or decide those interfaces.

## A1 re-stage declaration

This tranche will mutate files under `projects/chirality-app-dev/frontend/`. Under the owner-adopted A1 re-stage rule, **any such mutation invalidates the staged R20 procedure for any future proof claim and requires a newly staged revision and a fresh owner-executed proof** before a future proof claim. The historical R20 evidence remains historical evidence for the bytes against which it ran; it is not evidence for this tranche's post-change bytes.

## Fences and exclusions

F-APP-1 through F-APP-5 remain intact. No provider/network expansion, signing, notarization, publication, distribution, release-readiness or professional claim, issuance, Root write, plan/register/decision record, panel byte, vocabulary byte, or lifecycle act occurs. The Root-owned F1 configuration-digest question and the real-account logout-on-invalidation question remain undecided.

## Decision-latitude rationale

F2 is resolved inside D-APP-60/D-APP-64 latitude by dropping the fake's command-network posture to `off` and clearing pending/session destination state when consent becomes stale. This gives one unambiguous fail-closed snapshot whenever a validated consent field changes. Retaining a selected posture was rejected because it leaves `on` or prior session acceptances visible in fake state despite the stale consent being non-reusable; that path would also need a deliberate stale-plus-on fixture. F3 repairs only fake self-consistency: a fresh post-revocation grant restores the new generation's private home to `present` while leaving the Root-owned logout question open. F4 rejects enqueue requests unless the fake is in `askPerDestination` posture.
