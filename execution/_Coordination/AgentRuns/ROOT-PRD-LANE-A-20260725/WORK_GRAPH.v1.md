# Work Graph v1 — ROOT-PRD-LANE-A-20260725

| Node | Executor | Model | Objective | Read scope | Write targets | Depends on | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|---|---|
| N1 | Ephemeral Agent 2 generalist (sealed brief `briefs/PRD-AUTHOR-BRIEF.md`) | opus-5 | Author candidate root PRD | Ratified `docs/` corpus, `AGENTS.md`, `README.md`, D-GOV-21 record + packet + handoff, standing workplan, `_REGISTER.md`, `docs/thesis/` (read-only), `exports/chirality-app/export_public.py` (allowlist facts) | `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md` (new; the only write) | Step 0 preflight (done) | Terminal text: file written, section outline, provenance-label counts, constraint confirmations, unresolved items | V1 (Agent 0) |
| N2 | Agent 0 (parent) | — | Fan-in validation, Receipt 34, run closeout, commit + PR to owner-review gate | run record, loop receipts | `execution/_Coordination/LOOP_RECEIPTS.md`, run-record files | N1 accepted | — | human review of candidate PRD (Lane A terminal gate) |

## Failure handling

N1 failure/invalid return blocks N2; nothing commits; defect returns to the
owner. Partial returns are not accepted at fan-in.
