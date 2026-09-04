# Node J Review — Round 1

- Review date: 2026-09-03
- Role: fresh read-only ephemeral Agent 2 generalist
- Method: repository-native `software-code-review` used as review guidance; no TASK-compliance claim because `CHIRALITY_INSTRUCTION_ROOT` was unavailable in the delegated runtime
- Basis: `ede175910c67b384332324622b17695f69e6a715`
- Candidate: `9dd4b4ed04f5b99f6aa42a34ecd8ad6545e23089`
- Candidate parent: `ede175910c67b384332324622b17695f69e6a715`
- Worktree: `/private/tmp/chirality-app-v3-slate3-20260903/nodeJ-review-r1` (detached, retained for tranche closure)
- Verdict: **FAIL**
- Findings: 0 BLOCKER, 2 MAJOR, 0 MINOR, 0 NOTE

## Scope reviewed

I reviewed 100% of `git diff ede175910c67b384332324622b17695f69e6a715..9dd4b4ed04f5b99f6aa42a34ecd8ad6545e23089`: 60 paths, 2,020 insertions, 33 deletions, approximately 230 KiB of diff content.

The complete path inventory is:

- Six files at `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation/Evidence/Node_H_Section8_Preservation_2026-09-03/`: `COMPARE_RESULT_revision2.txt`, `EVALUATOR_BYTES_revision2.tsv`, `EVIDENCE.md`, `FRONTEND_TRIGGER_PATHS_CHANGED_e59efa483..ede175910.txt`, `MANIFEST.sha256`, and `rerun-section8-local.sh`.
- The complete 45-path `run-head-ede175910-revision2/` tree: its `MANIFEST.sha256` plus the 44 exact paths enumerated and verified by that manifest (Section 8 API, cleanup, per-check, SSE, summary and stable artifacts, and run logs).
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation/_run_records/AGENT2_RUN_2026-09-03_NODE_J.md`.
- Eight files under `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_J_2026-09-03/`: `COORDINATOR_DECISIONS.md`, `ORCHESTRATION_PLAN.md`, `STEP0_DISCOVERY.md`, `WORK_GRAPH.json`, and `instances/J1_IMPLEMENTER/{BRIEF_AMENDMENT_V2.md,LAUNCH_BRIEF.md,REGISTERED_CHECKS.json,STATUS.json}`.

No product source, frontend source, runtime source, evaluator source, workflow source, deliverable status, loop receipt, Root surface, plan, register, or decision-record byte changed.

## Findings

### J1-F1 — MAJOR — Bare PID reuse can cause teardown to signal a foreign process

File: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation/Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh`

Locations: lines 122–140 and 143–180 in the candidate.

The script records daemon and Next descendants as bare numeric PIDs. Teardown sends TERM, waits for up to 30 seconds, then sends KILL to the original recorded lists without first deriving an identity-verified survivor set. If a recorded process exits during the grace interval and the operating system reuses its PID before the KILL pass, `kill -KILL` can target an unrelated process. A successful retained run does not remove this race; it only shows that the race did not occur in that run.

The Next tree also loses part of its recorded boundary: the initial descendant capture is later overwritten by `NEXT_TREE_PIDS=$(collect_descendants "$NEXT_PID")`, rather than merged as the daemon list is. A child that exits or reparents before teardown can therefore disappear from the bounded set the script attempts to terminate.

This violates the explicit acceptance requirements that KILL apply only to survivors and that the method cannot signal foreign processes.

Required remediation: record and revalidate a stable process identity before every signal (for example PID plus start time and command fingerprint, or an equivalently bounded job/process-group identity), derive an identity-verified survivor-only set after TERM before KILL, and merge the early/current Next-tree captures rather than discarding the early set. Add a deterministic negative test or proof for stale/reused identities.

### J1-F2 — MAJOR — Teardown records cleanup failures but can still return success

File: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation/Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh`

Locations: lines 143–212 and the main success exits at lines 403–405 in the candidate.

The EXIT trap switches to `set +e`, records remaining process counts, socket/port state, disposable-state removal, and manifest generation, but it never converts any failed cleanup condition into a nonzero process status. Shell behavior independently confirmed that a failing command in an EXIT trap does not override an explicit `exit 0` unless the trap explicitly exits nonzero. As written, the proof can report success even when a daemon/Next descendant remains, a socket or listener remains, disposable state removal fails, or evidence-manifest generation fails.

This violates the explicit acceptance requirement that cleanup remain fail-closed.

Required remediation: capture the incoming exit status, accumulate every teardown invariant and cleanup-command failure, finish writing diagnostic evidence where possible, then explicitly exit nonzero when teardown failed and the incoming status was zero while preserving any pre-existing nonzero status. Add a controlled failure-path proof that demonstrates a cleanup invariant failure cannot yield exit zero.

## Acceptance review

### DEL-09-01-V3-02 hardening

- H2-F1 recursive descendant termination: recursive discovery and TERM/KILL phases are present, but foreign-process safety is not established because only bare PIDs are retained and KILL is not survivor/identity gated. **FAIL (J1-F1).**
- H2-F3 port precondition: the precondition executes before build or daemon startup, returns exit 72 for an occupied port, and left an independently created foreign listener alive. **PASS.**
- H2-F4 process selection: no unanchored `pgrep -f` or `pkill -f` remains; socket ownership and recorded roots are used. The later bare-PID reuse race is addressed separately by J1-F1. **PASS for removal of the unanchored search; overall teardown safety FAIL.**
- Cleanup fail-closed: teardown diagnostics are comprehensive, but failures do not propagate to the process exit status. **FAIL (J1-F2).**

### DEL-09-01-V3-01 revision 2 evidence

- The retained revision-2 run is bound to exact head `ede175910c67b384332324622b17695f69e6a715` and records the first-parent merges for PRs #687 through #692. **PASS.**
- Retained premerge results are internally consistent and recomputable: Section 8 passed 8/8; Section 9 report-only passed 16; retained teardown records zero remaining daemon/Next processes, dead roots, absent socket, free port, and successful disposable-state cleanup. **PASS.**
- The stable summary comparator was independently reproduced byte-for-byte and reports equal behavioral projections. **PASS.**
- Revision-1 sources and comparator inputs are preserved unchanged. **PASS.**
- `EVALUATOR_BYTES_revision2.tsv` was independently recomputed: 15 rows, 12 SAME and exactly three CHANGED trigger paths (`renderer-window-policy.ts`, `run-packaged-security-proof.mjs`, and its focused test). **PASS.**
- All per-run and bundle manifests verify and cover their declared path sets. **PASS.**
- No secret, forbidden packaged binary, product/evaluator/frontend/runtime source, status/receipt, Root/plan/register/decision byte was introduced by this candidate. **PASS.**

### Governance and posture

- The A1 re-stage declaration is present in `STEP0_DISCOVERY.md`. **PASS.**
- F-APP-2/no-release posture holds; release-related scan hits are explicit disclaimers or historical descriptions of unsigned development evidence, not readiness/signing/publication claims. **PASS.**
- The TASK stop is truthful: the record reports `STOPPED_ZERO_WRITE` after the missing instruction-root precondition, and the V2 amendment truthfully authorizes subsequent ephemeral-generalist work. **PASS.**

## Independent checks

| Check | Result | Evidence |
|---|---|---|
| `bash -n rerun-section8-local.sh` | PASS | No syntax error. |
| `shellcheck -S warning rerun-section8-local.sh` | PASS | No warning-or-higher diagnostic. |
| Unanchored process-search scan | PASS | No `pgrep -f` or `pkill -f`. |
| Occupied-port negative proof | PASS | On port 51987, method exited 72 before build/daemon startup; foreign listener PID remained unchanged and alive; negative-run manifest verified. A prior sandbox attempt could not create its test listener and was discarded as invalid setup, not counted as a pass. |
| Independent disposable premerge proof | PASS | Distinct port 51988; Section 8 passed 8/8, Section 9 report-only passed 16; teardown recorded zero remaining processes, absent socket, free port, and cleaned state; generated manifest verified; all untracked proof state removed. |
| Bundle and per-run manifests | PASS | All five manifests verified: bundle, base, revision-1 head, revision-1 round 2, and revision-2 head. Manifest membership and lexical ordering also verified. |
| Comparator reproduction | PASS | Recomputed output exactly matched `COMPARE_RESULT_revision2.txt`; behavioral projections equal. |
| Source/evaluator byte verification | PASS | Revision-1 sources unchanged; revision-2 table recomputed with 12 SAME and the exact three declared CHANGED trigger paths. |
| Strict JSON parsing | PASS | All changed JSON parsed successfully. An initial shell helper attempt shadowed zsh's `path` variable and was discarded as invalid check setup before a clean rerun. |
| Exact change-scope validator | PASS | Only the DEL-09-01 evidence/run-record root and Node J coordination run root changed. |
| Scope-of-work validator | PASS | DEL-09-01 validated. |
| `git diff --check` | PASS | No whitespace errors. |
| Loop receipts validator | PASS | Ledger valid; this candidate does not change the ledger. |
| Authority corpus status | PASS | v20; no drift. |
| APP-HOLD reliance | PASS | ALLOW for DEL-09-01. |
| APP-HOLD integrity | PASS | Integrity scan passed. |
| Harness self-check | PASS | Completed with unchanged baseline classifications (INFO 14, N/A 1, REVIEW 4, WARN 43). |
| Harness pytest | PASS | 350 passed. |
| Root runtime install/build | PASS | `npm ci` and `npm run build` completed. |
| Frontend install/typecheck | PASS | Escalated install completed after a sandbox DNS failure; `npm run typecheck` then passed. The pre-install `tsc not found` attempt was invalid setup and is not counted. |
| F-APP-2 scan | PASS | No forbidden release-readiness claim. |
| Secret/redaction scan | PASS | No credential value found; registration evidence is redacted. |
| Changed-file binary/encoding scan | PASS | All 60 changed paths are text/UTF-8 with no NUL byte. |
| Full Vitest suite | SKIPPED | Reviewer brief explicitly allowed reliance on committed evidence because the candidate changes no frontend/product bytes; focused release-path behavior was exercised by the independent premerge proof. |
| Frontend production build | SKIPPED | Reviewer brief explicitly allowed reliance on committed evidence because the candidate changes no frontend/product bytes; runtime build and frontend typecheck were independently rerun. |
| Release-quality/signing/publication | SKIPPED | Outside this evidence-preservation tranche and prohibited by F-APP-2 posture. |

All reviewer-created disposable processes and generated state were removed. The detached review worktree remains intentionally retained until tranche closure.

## Verdict

**FAIL.** The evidence preservation and revision-2 recomputation are strong, and the occupied-port guard works as intended. However, the hardened rerun method does not meet two explicit safety criteria: it can KILL a foreign process after PID reuse, and cleanup failures can still yield a successful exit. Both are MAJOR findings and require remediation plus fresh review before `REVIEW_PASS`.
