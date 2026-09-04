# Orchestration Plan — APPDEV_V3_NODE_H_2026-09-03

- **RunID:** `APPDEV_V3_NODE_H_2026-09-03`
- **Plan version:** 1 (frozen before any product write)
- **Selection authority:** `HUMAN` — the owner's 2026-09-03 development-slate-2 selection (App v3.0.0-rc.1 pathway, node H) transcribed by HELP_HUMAN into the sealed launch brief at `instances/H1_IMPLEMENTER/LAUNCH_BRIEF.md`; selectability conferred by the merged act named in the item's `NOT_SELECTABLE_UNTIL` tag — PR #686 at `e59efa483` (Receipt 212), re-derived under the committed `WORKPLAN_2026-09-03_app_dev_loop.md` Step 1 rule (`STEP0_DISCOVERY.md` §4).
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session.
- **Executor (H1_IMPLEMENTER):** one ephemeral Agent 2 generalist (Claude Fable 5.1, `claude-fable-5-1`) running the `skills/software-bounded-implementation` method under the sealed brief; no delegation.
- **Independent reviewer (H2_REVIEWER):** one fresh, read-only `TASK + software-code-review` child dispatched by HELP_HUMAN over 100% of the frozen diff after H1 freezes; its return is filed under `instances/H2_REVIEWER/` by H1 when supplied. Required verdict to push: `PASS` with no actionable finding (the seated item's `Checks:` line names the independent-review path explicitly, so it applies even though no product source changes).
- **Descriptive posture:** `TERMINAL_FAN_OUT_IN` with one implementer node and one sequential reviewer node; remediation loops H1 → H2 until PASS. Concurrent development nodes (F, G, I) run in disjoint write sets; the only shared surface is the append-only `loop/LOOP_RECEIPTS.md` (siblings share `Parent-Receipt: Receipt-212`, ledger rule 7).
- **Basis:** branch `codex/app-v3-nodeH-section8-preservation-2026-09-03` cut from `origin/main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge) — the required basis exactly.
- **Working root:** `projects/chirality-app-dev`.
- **Item:** DEL-09-01-V3-01 (`SELECTABLE` after the Step 0 flip) — Section 8 preservation and Shared Runtime Gate evidence across the v3 program; revised (not removed) at closeout per its `Removed when` clause.

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| H1_IMPLEMENTER | Produce stable premerge summary bytes proving unchanged Section 8 behaviour on `main` after PRs 683–686, with the RQG §13 rows DEL-09-01 owns, a bounded rerun method, evaluator/fixture byte identities, sorted manifests, and cleanup proof — without changing `validate-harness-*.mjs` behaviour | repo read-only; CI artifacts via `gh run download` | the brief's write locus only: `frontend/scripts/validate-harness-*.mjs` (unchanged in practice), Section 8 fixtures (unchanged), gitignored `frontend/artifacts/harness/**` (exercised, not committed), DEL-09-01 `Evidence/**` and `_run_records/**`, this run record, `loop/LOOP_RECEIPTS.md` (append, closeout) | `RETURN.md`, `CHECKS.json`, evidence bundle under DEL-09-01, local frozen commit | typecheck, full Vitest, build, premerge (pass, or the recorded deferral class with exact statement of what was and was not proven), diff --check, harness self-check + pytest, APP-HOLD scan, corpus status, scope validation all pass; `REVIEW_READY` |
| H2_REVIEWER | Read-only review of 100% of the frozen diff | frozen diff + repo | none | verdict + findings, filed under `instances/H2_REVIEWER/` | `PASS` with no actionable finding |
| Closeout (H1, after `REVIEW_PASS`) | `_STATUS.md` History line + item revision (pointer to the evidence bundle, next revision trigger), `MEMORY.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, receipt, rebase, push, one unmerged PR | as above | deliverable state, this packet, `loop/LOOP_RECEIPTS.md` (append) | PR number + head SHA + receipt ID | receipts validator VALID after append; post-rebase checks pass |

## Human decision points

- Owner merge of the single PR (one branch, one PR, one receipt, owner merge — workplan Step 4).
- Any write-locus extension the implementer surfaces as a scope need (never taken silently).
- The A1 re-stage rule consequence: a newly staged R20 procedure revision and a fresh owner-executed proof before any future proof claim (`STEP0_DISCOVERY.md` §3).
- G5 fan-in acceptance of the preservation evidence (the item's removal point; not this tranche).

## Constraints carried

Sealed write locus; no `runtime/**`, no `package.json` dependency change, no version bump, no `.github/workflows/**` change (DEL-09-05 owns the workflow under the D-APP-56 R4-P37 amendment), no provider/network expansion (F-APP-1), no signing/notarization/release-readiness claim (F-APP-2), no lifecycle change (F-APP-4), no new standing surface (F-APP-5); the disposable evidence daemon never touches the operator's real userData, LaunchAgent, or Keychain; no credential, token, or private account material preserved; never push before `REVIEW_PASS`; never self-merge; truthful attribution.
