# LAUNCH BRIEF — M1 (verbatim sealed brief as received)

RunID: `APPDEV_V3_NODE_M_2026-09-04` · Instance: `M1` · Received 2026-09-04 from HELP_HUMAN. The text below is the dispatch prompt reproduced verbatim; nothing is added or removed.

---

Act as a fresh ephemeral Agent 2 implementer for a RECORD-ONLY App v3 owner-ruling tranche (node M / A15). Do not delegate. Create your own scratch worktree with `git -C /Users/ryan/dev/chirality worktree add /private/tmp/chirality-app-v3-a15-20260904/nodeM -b codex/app-v3-nodeM-a15-owner-rulings-2026-09-04 origin/main`. Never touch `/Users/ryan/dev/chirality`, the HELP_HUMAN worktree `/Users/ryan/.codex/worktrees/85d6/chirality`, or any other worktree/branch. Do not push. Preserve your worktree until told tranche closed.

Basis must be exact current `origin/main` 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f; stop and report if it differs. Read root AGENTS.md, agents/AGENT_TASK.md, projects/chirality-app-dev/AGENTS.md, loop/LOOP_INIT.md, committed standing plan via `git show HEAD:projects/chirality-app-dev/loop/WORKPLAN_2026-09-03_app_dev_loop.md`, A14, Node I/A14 run record and commit 62120130a as precedent, the affected DEL-09-05 and DEL-09-06 `_STATUS.md`/dependencies/memory, and receipt rules. Run and record Step 0 discovery before editing: receipts validator, App authority corpus status from WORKING_ROOT, git status, decision-register scan, APP-HOLD reliance/dispatch for DEL-09-05 and DEL-09-06, pinned completion-reference SHA, and relevant ruling/status verification.

Owner decisions to transcribe verbatim in substance from this HELP_HUMAN chat on 2026-09-04:
1. Asked: `Do you authorize the recommended per-response CSP nonce with dynamic rendering for DEL-09-06-V3-04?` Owner answered: `Yes, so authorized.`
2. Asked: `Do you authorize installing Syft v1.18.1 on the owner host to unblock DEL-09-05-V3-02?` Owner answered: `Yes, so authorized.`
3. Asked: `Do you authorize creation of the disposable self-signed identity and the seated credential-transition drill, without authorizing Developer ID signing, notarization, Apple calls, distribution, or release-readiness claims?` Owner answered: `Yes, so authorized.`
The separate SCOPE_CHANGE authorization is out of this A15 record.

Write only:
- new repo-root `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`;
- DEL-09-06 `_STATUS.md` for V3-04 ruling/gate annotation and one History line;
- DEL-09-05 `_STATUS.md` for V3-02 and V3-04 host-act authorization annotations and one History line;
- a new run record `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/` following Node I shape, including your sealed brief, STEP0_DISCOVERY.md if current convention requires it, CHECKS.json, RETURN.md, HANDOFF_STATE.md if current convention requires it, and MANIFEST.sha256;
- append-only next valid receipt (expected Receipt 220, Parent Receipt 219, re-evaluate at closeout) in LOOP_RECEIPTS.md.
No other path may change.

Required semantics:
- A15 selects per-response nonce with dynamic rendering for the four packaged routes and makes DEL-09-06-V3-04 selectable once A15 lands. It grants the outcome, not an exact code shape; hash/SRI is not selected.
- Host acts are authorized but NOT performed by this tranche. For each, state that A14's dated deferral is lifted prospectively / later performance is now authorized; do not imply A14 was invalid. Syft remains operationally blocked until owner installation is observable. V3-04 remains blocked until the owner-created disposable identity actually exists; DEL-04-05-V3-01 is already landed.
- Use exact term `disposable self-signed A→B credential-transition drill`; explicitly no Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, or production identity act/claim.
- Do not retag or split DEL-09-06-V3-03 in this record-only tranche.
- No frontend/product/host/Root/lifecycle/Checking Approval SHA/register/decomposition/SCOPE_CHANGE change.
- A1: no frontend path touched, so record not applicable/no re-stage declaration needed beyond truthful no-frontend note.

Run proportional closeout checks: git diff --check; receipts validator; authority corpus no drift; APP-HOLD integrity/reliance for DEL-09-05 and DEL-09-06; repo harness self-check and pytest/path checks selected by software-workflow; exact change-scope over the write set; manifest verification; F-APP-2 prohibited-claim scan; confirm no forbidden paths. Commit only the scoped tranche. Freeze and return `REVIEW_READY` with branch, head SHA, basis, changed-file list, diff stat, check summary, and any uncertainty. Do not push or open a PR.
