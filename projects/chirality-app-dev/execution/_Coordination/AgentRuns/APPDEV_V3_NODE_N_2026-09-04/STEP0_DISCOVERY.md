# Step 0 discovery — APPDEV_V3_NODE_N_2026-09-04

Recorded before product edits on 2026-09-04 by N1_IMPLEMENTER. Execution is `delegated-harness-native`; Agent-2 role not mechanically enforced; governed-workflow role evidence `instruction-asserted`; K-SUBAGENT/non-delegation instruction+config asserted, not mechanism-proven; no descendants observed.

## Basis and live state

| Observation | Command / source | Result |
|---|---|---|
| Root and clean branch | `git rev-parse --show-toplevel`; `git status --short --branch` | isolated root `/private/tmp/chirality-app-v3-csp-20260904/nodeN`; branch `codex/app-v3-nodeN-csp-nonce-2026-09-04`; clean |
| Exact basis | `git rev-parse HEAD`; `git rev-parse origin/main` | both `307addfc259b046aeb2ed07d47086cd5686c35b8` (PR #694 merge) |
| Standing plan loader | bytewise-last committed `loop/WORKPLAN_*.md`; `git ls-tree`; `git show HEAD:<path>` | one mode `100644` blob selected: `loop/WORKPLAN_2026-09-03_app_dev_loop.md` |
| Receipt structure | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` from repo root | PASS/VALID; newest physical cursor Receipt 223 |
| Decision/ruling scan | decision register plus A15 and live DEL-09-06 status | no later conflicting ruling; A15 has landed and `DEL-09-06-V3-04` is `SELECTABLE` |
| Corpus | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` from App root | PASS; v20, all accepted sources match, no drift |
| APP-HOLD dispatch | `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-09-06` from App root | PASS/ALLOW; no active or scanned holds; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f` |
| Completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` from repo root | PASS; `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| Work discovery | `grep -l '^## Remaining' execution/PKG-*/1_Working/DEL-*/_STATUS.md` | all deliverable status surfaces are discoverable; live DEL-09-06 entry, not the standing plan, supplies the selected item |
| Practitioner status | Python 3.13 `tools/practitioner_harness/harness.py status --project app-dev` | PASS/exit 0; App status generated view, clean branch |
| Harness self-check | Python 3.13 `tools/practitioner_harness/harness.py self-check` | PASS/exit 0; only known repo-wide INFO/NOT_APPLICABLE/REVIEW/WARN findings outside this tranche |

The first practitioner-harness attempt used `/usr/bin/python3` and exited 2 because PyYAML is absent. No pass was inferred. The repository host runtime `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` (Python 3.13.14, PyYAML 6.0.3) was then used and passed both commands.

Dependency preparation was also evidence-calibrated: `runtime/npm ci && npm run build` passed. The first sandboxed `frontend/npm ci` attempt failed with `ENOTFOUND registry.npmjs.org`; no pass was inferred. The exact command was rerun with approved network access and passed without lockfile edits.

## Selected live obligation

`DEL-09-06-V3-04` requires a nonce-based packaged `script-src` replacing `'unsafe-inline'`, with A15 selecting a per-response nonce and dynamic rendering for `/`, `/chat`, `/pipeline`, and `/workbench`. The live item requires registered frontend gates, build/premerge, D-APP-36 risk-calibrated render evidence, packaged proof tightened to reject `'unsafe-inline'`, APP-HOLD, repo checks, durable evidence, and fresh independent review. Its only named item dependency, V3-01, is recorded landed. No Root-owned dependency gates this item.

## A1 re-stage declaration

This tranche will mutate `projects/chirality-app-dev/frontend/`. Under A1, **any such mutation invalidates the staged R20 procedure for any future proof reliance and requires a newly staged revision and a fresh owner-executed proof**. Historical R20 remains historical evidence only. The CSP merge will trigger a separate `DEL-09-01-V3-01` revision 3 after landing. Node N does not perform or claim that later revision.

## Product discovery and chosen shape

- The packaged custom server in `electron/main.ts` currently applies one static packaged CSP only to the response before invoking Next.
- Pinned Next 15.5.21 reads a nonce from the incoming `content-security-policy` header (`node_modules/next/dist/server/app-render/app-render.js` and `get-script-nonce-from-header.js`) and applies it to framework scripts.
- The app owns another inline theme-bootstrap script in `src/app/layout.tsx`; it needs the same request nonce explicitly.
- Electron's `onHeadersReceived` hook currently supplies a CSP only when the renderer-origin response lacks one. A packaged fallback without the request nonce would be inconsistent; development still needs its existing static fallback.
- The selected bounded design therefore creates a cryptographically strong nonce for each packaged request, builds one policy from it, sets that exact policy on the request before Next handles it and on the response, passes the nonce through a non-secret request header to the dynamic root layout, and disables static CSP fallback in packaged mode while preserving development mode unchanged.

Rejected without owner referral: post-build HTML hashing/rewriting (A15 did not select hash/SRI and it would introduce a separate build transformation); a process-wide/static nonce (fails per-response uniqueness); response-only nonce insertion (Next and the app-owned inline script would not receive the nonce); independent request/response nonce generation (violates the same-policy invariant).

Implementation refinement after this Step 0 snapshot: the initially considered companion nonce header was removed before the final proof. The root layout now parses the nonce from the same request CSP that Next consumes and the response enforces. The implementation therefore has one nonce-bearing header rather than two; rationale and proof are in the DEL evidence and N1 return.

## Sealed write locus and fences

The locus is exactly the product/test/evidence/run-record set listed in `ORCHESTRATION_PLAN.md`. No version, lockfile, other deliverable state, authority corpus, plan, decision/register, decomposition/SCOPE_CHANGE, Root, `.github`, host, signing, notarization, Apple, distribution, publication, or release-readiness surface is authorized. `_STATUS.md`, `MEMORY.md`, and the receipt ledger remain untouched before review PASS.
