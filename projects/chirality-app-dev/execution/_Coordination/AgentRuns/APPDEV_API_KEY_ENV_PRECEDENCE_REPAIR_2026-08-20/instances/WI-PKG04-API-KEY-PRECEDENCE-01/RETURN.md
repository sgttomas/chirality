# Return — WI-PKG04-API-KEY-PRECEDENCE-01

RUN_STATUS: `SUCCESS`

Node: `N1 / PKG-04 / DEL-04-05`

Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`

Branch: `codex/app-api-key-precedence-20260820`

## Coverage and accepted child returns

- Implementation child
  `TASK-PKG04-API-KEY-PRECEDENCE-IMPLEMENT-01`: accepted `SUCCESS`.
- Review 01: correctly returned `FAIL` on one evidence-coverage omission and
  zero code/test findings.
- Evidence remediation: accepted; no product/test byte changed.
- Fresh Review 02
  `TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-02`: accepted `PASS`, 8/8 frozen v2
  hashes matched, exact diff and both files reviewed 100%, zero actionable
  findings, N1 fan-in valid.

## Accepted product identity

| SHA-256 | Path |
|---|---|
| `72e9cdb9fabb5beb77ba009933dbb8c1375f012ac0162e088d96a460fe5baaab` | `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` |
| `56b36a5ed44885877d692ad6357b6ee209f96edb8844aec2f5781d6c0a5b4fe7` | `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` |

The runtime now resolves persisted safeStorage first, then
`ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. The former
`it.fails` is replaced by positive stored/env/whitespace regression coverage.
oMLX isolation, storage/persistence, error semantics, public interfaces,
dependencies, and lockfiles are unchanged.

## Validation

- Focused API-key storage Vitest: PASS, 1 file / 18 tests.
- Full frontend Vitest: PASS, 150 files passed, 1 skipped; 1,165 tests passed,
  4 skipped.
- Frontend plus Electron typecheck: PASS.
- Frontend build: PASS.
- Practitioner harness: PASS, 350 tests, including post-calibration rerun.
- Repository self-check: exit 0, including post-calibration rerun; unchanged
  4 REVIEW / 31 WARN baseline outside N1.
- APP-HOLD integrity: PASS; register match and zero held deliverables.
- APP-HOLD reliance for DEL-04-05: ALLOW, including post-calibration rerun.
- Final secret scan: PASS, 5,820 files, zero blocked findings.
- Scope validation, JSON parse, tracked/untracked whitespace, and exact
  write-boundary inspection: PASS.
- Fresh Review 02: PASS, zero actionable findings.

## Deliverable effects

- `Evidence_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20.md` proves the RQ-001
  slice and removes the Receipt-180 precedence blocker for downstream
  verification.
- `_STATUS.md` and `MEMORY.md` are truthfully calibrated.
- DEL-04-05 remains `IN_PROGRESS`.
- `## Remaining` remains empty.
- Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- No dependency row or lifecycle transition changed.

## Closure and handoff

- Blockers: none within N1.
- Waivers: none.
- Human rulings needed: none.
- Rerun: none while the two accepted product hashes and frozen v2 subjects
  remain unchanged; any changed subject requires proportional checks/review.
- Derivative status: run controls and normalized check files are derivative
  evidence; DEL-04-05 `_STATUS.md`, `MEMORY.md`, and evidence are the
  package-local handoff truth for this slice.
- Runtime telemetry summary: `NOT_REQUIRED`; this was a serialized
  implementation/review proof loop, not a multi-member batch activation, and
  the runtime exposed no token/context occupancy telemetry.
- Next owner: `HELP_HUMAN` must relay this accepted terminal N1 handoff to
  `WI-PKG02-API-KEY-PRECEDENCE-01` and release N2. Git commit/push/PR work
  remains with CHANGE after graph fan-in.
