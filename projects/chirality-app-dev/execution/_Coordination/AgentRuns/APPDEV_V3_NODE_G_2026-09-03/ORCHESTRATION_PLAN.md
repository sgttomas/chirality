# Orchestration Plan — APPDEV_V3_NODE_G_2026-09-03

- **RunID:** `APPDEV_V3_NODE_G_2026-09-03`
- **Plan version:** 1 (frozen before any product write)
- **Selection authority:** `HUMAN` — the owner's 2026-09-03 development-slate-2 selection (App v3.0.0-rc.1 pathway, node G) transcribed by HELP_HUMAN into the sealed launch brief at `instances/G1_IMPLEMENTER/LAUNCH_BRIEF.md` (chat transcription is evidence, not ruling); selectability of DEL-09-06-V3-05 conferred by the merged node A closeout PR #686 (Receipt 212), which seeded the item as `SELECTABLE`.
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session.
- **Executor (G1_IMPLEMENTER):** one ephemeral Agent 2 generalist (Claude Fable 5.1, `claude-fable-5-1`) running the `skills/software-bounded-implementation` method under the sealed brief; no delegation.
- **Independent reviewer (G2_REVIEWER):** one fresh, read-only `TASK + software-code-review` child dispatched by HELP_HUMAN over 100% of the frozen diff after G1 freezes; its return is filed under `instances/G2_REVIEWER/` by G1 when supplied. Required verdict to publish: `PASS` with no actionable finding (App `AGENTS.md` independent-review path — this tranche changes product source under `frontend/electron/**` and `frontend/scripts/**`).
- **Descriptive posture:** `TERMINAL_FAN_OUT_IN` with one implementer node and one sequential reviewer node; remediation loops G1 → G2 until PASS. Concurrent development nodes (F, H, I) run in disjoint write sets; the only shared surface is the append-only `loop/LOOP_RECEIPTS.md` (sibling receipts share `Parent-Receipt: Receipt-212`, ledger rule 7).
- **Basis:** branch `codex/app-v3-nodeG-egress-probe-restriction-2026-09-03` cut from `origin/main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge) — the required basis exactly.
- **Working root:** `projects/chirality-app-dev`.
- **Item (`SELECTABLE` on `main` at basis):** DEL-09-06-V3-05 — restrict the packaged-proof egress-layer probe URL to destinations the REQ-NET-001 egress policy denies, or hard-code the `:8443` probe and drop `CHIRALITY_EGRESS_LAYER_PROBE_URL` (residual R-B of node A).

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| G1_IMPLEMENTER | Make the main-process egress-layer probe structurally unable to request any destination the REQ-NET-001 egress policy would allow (design decision D1 in `COORDINATOR_DECISIONS.md`); prove it at unit level; keep the packaged proof observing `egressLayerDiagnostics > 0`; update the proof script, its test, and contract pins deliberately | repo read-only | the brief's write locus only (see `LAUNCH_BRIEF.md` "RUN RECORD … write locus") | `RETURN.md`, `CHECKS.json`, evidence under DEL-09-06, local frozen commit | typecheck, full Vitest, focused Vitest, build, `desktop:pack`, packaged security proof, premerge (or recorded deferral class), diff --check, harness self-check + pytest, APP-HOLD preflight + scan, corpus status, receipts validator, scope validation all pass; `REVIEW_READY` |
| G2_REVIEWER | Read-only review of 100% of the frozen diff | frozen diff + repo | none | verdict + findings, filed under `instances/G2_REVIEWER/` | `PASS` with no actionable finding |
| Closeout (G1, after `REVIEW_PASS`) | DEL-09-06 `_STATUS.md` Remaining/History update (V3-05 removed; V3-02/03/04 unchanged; lifecycle and Checking Approval SHA untouched), `MEMORY.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, receipt (Parent-Receipt `Receipt-212`; next unused ID at rebase time), rebase, push, one unmerged PR with the `artifact-proof` label | as above | deliverable state, this packet, `loop/LOOP_RECEIPTS.md` (append) | PR URL + head SHA + receipt ID | receipts validator VALID after append; post-rebase checks pass |

## Human decision points

- Owner merge of the single PR (one branch, one PR, one receipt, owner merge — workplan Step 4).
- Any write-locus extension the implementer surfaces as a scope need (never taken silently).
- Packaged-proof host execution under the AGENTS.md host-capability rule (in-sandbox here), and the `artifact-proof` PR label that runs `.github/workflows/desktop-release-template.yml` to bind a proof to the merged SHA.
- The A1 re-stage rule consequence: a newly staged R20 procedure revision and a fresh owner-executed proof before any future proof claim (this tranche mutates `frontend/`).

## Constraints carried

Sealed write locus; no `runtime/**`, no `package.json` dependency change, no version bump, no provider/network expansion (F-APP-1 — the probe destination remains the policy-denied `:8443` form already used; no destination is added to REQ-NET-001), no signing/notarization/release act (F-APP-2), no domain-engine surface (F-APP-3), no lifecycle change (F-APP-4), no new standing surface (F-APP-5); never push before `REVIEW_PASS`; never self-merge; truthful attribution.
