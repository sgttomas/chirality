# Status: DEL-07-01

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-04
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-07-01-V3-01** (`SELECTABLE`) — organisation-layer protection: hash pinning, write protection, and separation from the working root (SOW-084).
  Trace: OUT-001, AC-001, VER-001; applied decomposition row L357 (instruction-root write protection for both the bundled base and the client-owned, hash-pinned organisation layer); SOW-084 L254 (K-ROOT-1 applies to both layers; read-only during ordinary project execution; hash-pinned; packaging-checked; never a working root and never a proposal path); DEC-025 L634.
  Plan: T3 prerequisite; SR-25; Q14 ruled 2026-09-04 (G2-CONFIRM). Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` (SHA-256 `e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb`), cited only for what the tranche means when complete, never as a queue; status from current `main`.
  Depends: none for the policy helpers and fixtures; DEL-08-01-V3-01 owns the packaging checks; DEL-04-04-V3-01 consumes the pins.
  Write locus: `frontend/src/lib/harness/instruction-root.ts` and path-policy helpers, organisation-layer pin and protection fixtures, tests; `frontend/electron/daemon-instruction-root.ts` only if protection must be enforced at the daemon boundary (additive; D-APP-98); deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: the organisation-layer path is validated as separate from the working root and refused as a working root or a proposal path; a pin file with a SHA-256 per asset is verified at boot; write protection is proven with fixtures for both layers; durable non-secret bytes sufficient for independent recomputation per the `loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: merged with review PASS.

## History
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-074, UPD-077; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-130; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-09-04 - SCA-APP-010 shell-redesign seating (D-APP-108; owner adopted the seating list as presented): Remaining items seeded DEL-07-01-V3-01 (SELECTABLE: DEL-07-01-V3-01) with gate, dependency, write-locus, check, and return contracts; ruled questions cited by item. `ScopeOfWork.md` re-pinned to the applied decomposition at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` with a SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` aligned (WI-041, WI-042, WI-043, WI-044, WI-045). Run evidence `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-09-05 - D-APP-109 (owner direction 2026-09-05): dependency register re-extracted against the applied decomposition row L357 with the held edge proposals emitted as cycle-participating, non-gating rows (run `execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); `_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change.
