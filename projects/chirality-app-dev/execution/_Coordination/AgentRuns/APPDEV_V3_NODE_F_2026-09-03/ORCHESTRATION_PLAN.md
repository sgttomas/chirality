# Orchestration Plan — APPDEV_V3_NODE_F_2026-09-03

- **RunID:** `APPDEV_V3_NODE_F_2026-09-03`
- **Plan version:** 1 (frozen before any product write)
- **Selection authority:** `HUMAN` — the owner's 2026-09-03 development-slate selection (App v3.0.0-rc.1 pathway, dev slate 2, node F) transcribed by HELP_HUMAN into the sealed launch brief at `instances/F1_IMPLEMENTER/LAUNCH_BRIEF.md`; the chat transcription is evidence, not ruling. Selectability conferred by the merged seating candidate PR #681 (Receipt 205, A12) and the item's `SELECTABLE` marker on `main` at basis.
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session.
- **Executor (F1_IMPLEMENTER):** one ephemeral Agent 2 generalist (Claude Fable 5.1, `claude-fable-5-1`) running the `skills/software-bounded-implementation` method under the sealed brief; no delegation.
- **Independent reviewer (F2_REVIEWER):** one fresh, read-only `TASK + software-code-review` child dispatched by HELP_HUMAN over 100% of the frozen diff after F1 freezes; its return is filed under `instances/F2_REVIEWER/` by F1 when supplied. Required verdict to publish: `PASS` with no actionable finding (App `AGENTS.md` independent-review path).
- **Descriptive posture:** `TERMINAL_FAN_OUT_IN` with one implementer node and one sequential reviewer node; remediation loops F1 → F2 until PASS. Concurrent development nodes (G, H, I) run in disjoint write sets; the only shared surface is the append-only `loop/LOOP_RECEIPTS.md` (siblings share `Parent-Receipt: Receipt-212`, ledger rule 7).
- **Basis:** branch `codex/app-v3-nodeF-consent-ux-fixtures-2026-09-03` cut from `origin/main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge) — the required basis exactly.
- **Working root:** `projects/chirality-app-dev`.
- **Item (`SELECTABLE` on `main` at basis):** DEL-02-05-V3-02 — static WP-07 account/consent UX fixtures behind a fake consent port. The live `HostedEngineConsentPort` consumption is DEL-02-05-V3-03 and is not touched.

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| F1_IMPLEMENTER | UI-facing `HostedEngineConsentPort` vocabulary shaped by K-CONSENT-1 / K-NET-1; a fake in-memory adapter and named fixtures; the account/consent settings panel (per-root login explanation, root-private app-owned `CODEX_HOME` copy, login/logout/account and consent/revocation states, the three command-network postures, rate-limit/approval status, `Opt-in Preview`, role entry with `role not mechanically enforced`); react-test-renderer (D-APP-36) and static-markup tests; durable evidence per the workplan Evidence contract | repo read-only | the brief's write locus only (see `LAUNCH_BRIEF.md` "Write locus") | `RETURN.md`, `CHECKS.json`, evidence under DEL-02-05, local frozen commit | typecheck, full Vitest, focused Vitest, build, premerge (or recorded deferral class), diff --check, harness self-check + pytest, APP-HOLD scan, corpus status, receipts validator, scope validation all pass; `REVIEW_READY` |
| F2_REVIEWER | Read-only review of 100% of the frozen diff | frozen diff + repo | none | verdict + findings, filed under `instances/F2_REVIEWER/` | `PASS` with no actionable finding |
| Closeout (F1, after `REVIEW_PASS`) | `_STATUS.md` Remaining/History update (V3-02 removed; V3-03 unchanged), `MEMORY.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, receipt append, rebase, push, one unmerged PR | as above | deliverable state, this packet, `loop/LOOP_RECEIPTS.md` (append) | PR URL + head SHA + receipt ID | receipts validator VALID after append; post-rebase checks pass |

## Human decision points

- Owner merge of the single PR (one branch, one PR, one receipt, owner merge — workplan Step 4).
- Any write-locus extension the implementer surfaces as a scope need (never taken silently).
- The A1 re-stage rule consequence: a newly staged R20 procedure revision and a fresh owner-executed proof before any future proof claim.
- Live account/consent flows remain gated (Root DEL-02-09 routed notice; G3/G-CSP/G4) — DEL-02-05-V3-03; nothing in this node claims them.

## Constraints carried

Sealed write locus; no `runtime/**`, no `docs/**`, no `package.json` dependency change, no version bump, no provider/network expansion or new network destination (F-APP-1), no signing/notarization/release act (F-APP-2), no lifecycle change (F-APP-4), no new standing surface (F-APP-5); no live account claim; no secret persistence; no ambient `~/.codex` read; the fake port is never mounted in the product shell (nothing for the live DEL-02-05-V3-03 wiring to undo); never push before `REVIEW_PASS`; never self-merge; truthful attribution.
