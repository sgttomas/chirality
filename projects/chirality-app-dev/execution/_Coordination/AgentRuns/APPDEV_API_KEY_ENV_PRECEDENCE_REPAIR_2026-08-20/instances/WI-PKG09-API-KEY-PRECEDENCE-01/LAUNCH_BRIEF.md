# WORKING_ITEMS activation — N3 PKG-09 packaged-security closure

- RequestedBy: `HELP_HUMAN`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- InstanceID: `WI-PKG09-API-KEY-PRECEDENCE-01`
- PackageID: `PKG-09`
- Selected deliverables: `DEL-09-06` primary; `DEL-09-04` dependent
- Branch: `codex/app-api-key-precedence-20260820`
- Accepted basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`
- Graph: v2, serialized N3 after Agent 0-accepted N1 and N2 terminal handoffs

## Accepted predecessor product identity

- `frontend/electron/api-key-storage.ts`:
  `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`
- `frontend/src/__tests__/electron/api-key-storage.test.ts`:
  `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4`
- `frontend/electron/api-key-ipc.ts`:
  `3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb`
- `frontend/src/__tests__/electron/api-key-ipc.test.ts`:
  `818b7424ef1de3f4418486a4a7ae839cb837d84a23af6fdd73621f847d74b1a6`

N1 and N2 checks and fresh reviews pass with zero findings. N2 preserves
DEL-02-05 lifecycle, dependencies, Remaining, and Checking Approval SHA.

## Objective

Build a fresh unsigned macOS arm64 artifact from the exact accepted fixed
bytes, execute the existing fail-closed packaged security proof against it,
retain a D-APP-99 compact identity-bound evidence package, and remove only the
DEL-09-06 D-APP-97 packaged-security Remaining item and DEL-09-04 REQ-009 /
R4-P49 packaged-security Remaining item if all acceptance checks pass.

## Write ownership

N3 owns only:

- a new compact closure-evidence directory under DEL-09-06
  `Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/**`;
- `Assessment_INSP-03_DEL-09-06.md`, `MEMORY.md`, `_STATUS.md`, and a new
  DEL-09-06 TASK run record;
- `Assessment_INSP-03_DEL-09-04.md`, `MEMORY.md`, `_STATUS.md`, and a new
  DEL-09-04 derivative run record;
- N3 and child records below this RunID's instance directory.

All product, test, proof-script, workflow, dependency, lockfile, SOW,
decomposition, decision/register, receipt, completion-log, root-governance,
and foreign-loop paths are read-only. A product/proof-script defect is an
exact blocker returned upward, not an implicit scope expansion.

## Checks and acceptance

1. Revalidate all four accepted predecessor hashes before and after execution.
2. APP-HOLD dispatch and reliance must be `ALLOW` for DEL-09-06 and DEL-09-04.
3. Focused storage/IPC/proof tests, full frontend Vitest, frontend/Electron
   typecheck, frontend build, practitioner harness, root self-check, and
   APP-HOLD integrity pass with normalized evidence.
4. Secret scan passes with zero blocked findings.
5. `npm run desktop:dist` produces a fresh unsigned arm64 app and DMG;
   packaged dependency boundary and instruction-root integrity pass.
6. `npm run proof:packaged-security -- --output-dir <isolated-host-output>`
   passes against the just-built packaged app and records: exact executable,
   app.asar and CLI hashes; safeStorage encrypted store/status/remove; accepted
   UI/canonical-env/compatibility-env source and precedence behavior without
   credential leakage; provider isolation; renderer blocked diagnostic/probe;
   usable GUI/daemon descendant TCP snapshots with zero non-allowlisted
   outbound; confirmed GUI/daemon shutdown, stream closure, and cleanup.
7. Full raw host output stays in an isolated temporary host directory through
   review. The repository retains only compact redacted summaries, hashes,
   exact commands/results, and required failure-attempt calibration.
8. Relevant DEL-09-06 and DEL-09-04 assessment/state claims are calibrated to
   the passing artifact. Lifecycle remains `IN_PROGRESS`; Checking Approval
   SHAs, dependencies, SOW, RunAtLoad, and owner-machine deployment residuals
   remain unchanged.
9. Scope, JSON/NDJSON parse, candidate-wide whitespace, and secret containment
   pass. Fresh integrated 100% read-only review must return PASS with zero
   actionable findings before manager fan-in.

## Host surface

Unsigned packaging and packaged Electron/keychain/process/network execution
require exact host-capability escalation by the child. A sandbox denial or
missing host run is not a pass. CI may supplement registered checks but does
not replace this required in-session host proof.

## Exclusions

No signing, notarization, distribution/publication, release or lifecycle act,
provider expansion, real credential, dependency/lockfile change, RunAtLoad,
owner-machine daemon deployment, receipt/completion-log, commit, push, PR,
merge, or shared/root/foreign-loop governance write.
