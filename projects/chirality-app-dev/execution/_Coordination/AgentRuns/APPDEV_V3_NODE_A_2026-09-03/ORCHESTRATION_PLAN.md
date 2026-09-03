# Orchestration Plan — APPDEV_V3_NODE_A_2026-09-03

- **RunID:** `APPDEV_V3_NODE_A_2026-09-03`
- **Plan version:** 1 (frozen before any product write)
- **Selection authority:** `HUMAN` — the owner's 2026-09-03 development-slate selection (App v3.0.0-rc.1 pathway, node A) transcribed by HELP_HUMAN into the sealed launch brief at `instances/A1_IMPLEMENTER/LAUNCH_BRIEF.md`; selectability conferred by the merged seating candidate PR #681 (Receipt 205, A12).
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session.
- **Executor (A1_IMPLEMENTER):** one ephemeral Agent 2 generalist (Claude Fable 5.1, `claude-fable-5-1`) running `skills/software-bounded-implementation` method under the sealed brief; no delegation.
- **Independent reviewer (A2_REVIEWER):** one fresh, read-only `TASK + software-code-review` child dispatched by HELP_HUMAN over 100% of the frozen diff after A1 freezes; its return is filed under `instances/A2_REVIEWER/` by A1 when supplied. Required verdict to publish: `PASS` with no actionable finding (App `AGENTS.md` independent-review path).
- **Descriptive posture:** `TERMINAL_FAN_OUT_IN` with one implementer node and one sequential reviewer node; remediation loops A1 → A2 until PASS. Concurrent development nodes (B…) run in disjoint write sets; the only shared surface is the append-only `loop/LOOP_RECEIPTS.md` (Receipts 206–209 share `Parent-Receipt: Receipt-205`, ledger rule 7).
- **Basis:** branch `codex/app-v3-nodeA-credential-ipc-2026-09-03` cut from `origin/main` at `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge) — the required basis exactly.
- **Working root:** `projects/chirality-app-dev`.
- **Items (all `SELECTABLE` on `main` at basis):** DEL-09-06-V3-01, DEL-04-05-V3-01, DEL-02-05-V3-01 — executed under one integration owner because they share `frontend/electron/api-key-ipc.ts` (each item's `Depends:` line names this serialization).

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| A1_IMPLEMENTER | Sender authorization on the six credential IPC handlers via one shared policy module; typed safeStorage states (`missing`, `storageUnavailable`, `decryptFailed`, `available`) at the store/bridge with non-destructive fixtures; four-state settings panel with remediation copy and react-test-renderer evidence; G-CSP unit-level inventory and pins | repo read-only | the brief's write locus only (see `LAUNCH_BRIEF.md` "Write locus") | `RETURN.md`, `CHECKS.json`, evidence under the three deliverables, local frozen commit | typecheck, full Vitest, build, premerge (or recorded deferral class), diff --check, harness self-check + pytest, APP-HOLD scan, scope validation all pass; `REVIEW_READY` |
| A2_REVIEWER | Read-only review of 100% of the frozen diff | frozen diff + repo | none | verdict + findings, filed under `instances/A2_REVIEWER/` | `PASS` with no actionable finding |
| Closeout (A1, after `REVIEW_PASS`) | `_STATUS.md` Remaining/History updates, `HANDOFF_STATE.md`, `MANIFEST.sha256`, Receipt 206, rebase, push, one unmerged PR | as above | deliverable state, this packet, `loop/LOOP_RECEIPTS.md` (append) | PR number + head SHA | receipts validator VALID after append; post-rebase checks pass |

## Human decision points

- Owner merge of the single PR (one branch, one PR, one receipt, owner merge — workplan Step 4).
- Any write-locus extension the implementer surfaces as a scope need (never taken silently).
- Packaged-proof host execution (`npm run desktop:pack` + `npm run proof:packaged-security`) under the AGENTS.md host-capability rule, or the `artifact-proof` PR label that runs `.github/workflows/desktop-release-template.yml`.
- The A1 re-stage rule consequence: a newly staged R20 procedure revision and a fresh owner-executed proof before any future proof claim.

## Constraints carried

Sealed write locus; no `runtime/**`, no `package.json` dependency change, no version bump, no provider/network expansion (F-APP-1), no signing/notarization/release act (F-APP-2), no lifecycle change (F-APP-4), no new standing surface (F-APP-5); the daemon remains the sole runtime credential owner; no plaintext exposure; no silent ciphertext deletion or overwrite; never push before `REVIEW_PASS`; never self-merge; truthful attribution.
