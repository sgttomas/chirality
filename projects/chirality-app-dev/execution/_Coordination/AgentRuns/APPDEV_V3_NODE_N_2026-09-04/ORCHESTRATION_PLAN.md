# Orchestration Plan — APPDEV_V3_NODE_N_2026-09-04

- **RunID:** `APPDEV_V3_NODE_N_2026-09-04`
- **Plan version:** 1, frozen before product edits.
- **Selection authority:** `HUMAN` — owner Ryan Tufts authorized the A15 recommended per-response CSP nonce with dynamic rendering; PR #694 merged the durable A15 record at basis `307addfc259b046aeb2ed07d47086cd5686c35b8` and made `DEL-09-06-V3-04` selectable.
- **Execution class:** `delegated-harness-native`. HELP_HUMAN directly dispatched one descendant instructed to operate as a bounded ephemeral Agent-2 generalist. The Agent-2 role is not mechanically enforced; governed-workflow role evidence is `instruction-asserted`; K-SUBAGENT/non-delegation is instruction+config asserted, not mechanism-proven. No descendant of this implementer has been observed.
- **Implementer:** N1_IMPLEMENTER, OpenAI Codex, GPT-5 family (exact model identifier is not exposed to this agent runtime).
- **Independent reviewer:** a fresh read-only descendant will review 100% of the frozen basis-to-head diff. Its verdict does not exist at this stage and will not be invented here.
- **Posture:** sequential implementer → independent reviewer → remediation loop if needed → separately authorized narrative closeout after `REVIEW_PASS`.
- **Basis/branch:** `307addfc259b046aeb2ed07d47086cd5686c35b8`; `codex/app-v3-nodeN-csp-nonce-2026-09-04`.
- **Parent receipt:** Receipt 223; no Node N receipt is appended before post-review closeout.
- **Selected item:** only `DEL-09-06-V3-04`.

## Objective

Implement the A15-selected per-response cryptographically strong nonce for the packaged renderer CSP. Packaged `script-src` must contain a request-specific nonce and exclude `'unsafe-inline'`; Next framework scripts and the app-owned theme bootstrap must receive the same nonce; the four packaged routes must render under the policy without own-resource CSP violations. Development policy and behavior remain unchanged.

The implementer selects the bounded design shape under the ruling: generate a nonce for every packaged renderer request, attach the same CSP to the incoming request before Next handles it and to the response, expose the request nonce to the root layout for the app-owned inline bootstrap, and keep Electron's response hook as a development-only fallback. This uses the framework's pinned request-CSP nonce extraction instead of post-build HTML rewriting. Rejected alternatives are recorded in `RETURN.md`.

## Write ownership

- Product/assurance locus: `frontend/electron/renderer-window-policy.ts`, `frontend/electron/main.ts`, `frontend/src/app/**`, `frontend/scripts/run-packaged-security-proof.mjs`, directly relevant `frontend/src/__tests__/**`, and `frontend/src/__tests__/contract-pins.manifest.ts`.
- Evidence/state locus before review: DEL-09-06 `Evidence/Node_N_CSP_Nonce_2026-09-04/**`, DEL-09-06 `_run_records/**`, and this AgentRuns directory.
- Explicitly withheld until `REVIEW_PASS`: DEL-09-06 `_STATUS.md`, DEL-09-06 `MEMORY.md`, and `loop/LOOP_RECEIPTS.md`.
- Prohibited: package/version/lockfile change unless mechanically unavoidable, any other deliverable state, plans, decisions/registers, decomposition/SCOPE_CHANGE, Root or `.github` surfaces, host identity/Syft state, signing/notarization/publication/distribution, or release-readiness claims.

## Fan-in gates

The first product freeze requires the registered frontend checks, focused and full Vitest, build, release-quality/premerge surfaces, packaged build/proof, route/nonce/CSP assurance, D-APP-36 risk-calibrated render evidence, repo checks, exact scope, manifests, cleanup evidence, and a clean committed worktree. Publication requires a later fresh independent `PASS` with no BLOCKER or MAJOR finding and a separately authorized narrative closeout. Owner merge remains the gate.

## A1 consequence

Every `frontend/` mutation in this tranche invalidates the staged R20 procedure for future proof reliance. Historical R20 remains historical only. A newly staged revision and fresh owner-executed proof are required before a future proof claim. This CSP merge will trigger a separate `DEL-09-01-V3-01` revision 3 after landing; this branch neither performs nor claims that revision.
