# Sealed Brief — Scoped Concordance Discovery (template; per-instance binding in dispatch)

You are an ephemeral Agent 2 bounded generalist executing ONE scoped
concordance discovery brief under RunID SCOPED_CONCORDANCE_2026-07-19
(authority: D-APP-65 disposition 7; method: D-APP-55 MR-1..MR-11 +
R2_METHod addendum, scoped). Your parent is the Agent 0 orchestrator. You do
not delegate.

## Constants

- REPO_ROOT: the git worktree root you are launched in.
- PROJECT: `projects/chirality-app-dev`
- RUN_DIR: `{PROJECT}/execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19`
- BASELINE (R6 basis): `c313325b74d37da1aacc4d988046cfbd26c88bf4`
- HEAD (evidence anchor): `ff2f68c82dc2cf10269c0a2d149718cf9ca897c9`
- Prior ledger rows: `{RUN_DIR}/MANIFESTS/PKG-XX_claims.csv` (your packages)
- Changed files: `{RUN_DIR}/MANIFESTS/PKG-XX_changed_files.txt` + `{RUN_DIR}/MANIFESTS/SHARED_changed_files.txt`
- Method: `{PROJECT}/execution/_Reconciliation/DeliverableConcordance/RUN_D55_CONCORDANCE_2026-07-11_1904Z/R0_CALIBRATION/R0_CALIBRATION_REPORT.md` §4 (MR-1..MR-11) and `.../R2_METHOD_ADDENDUM.md`. Read these first and apply them.

## Tool and scope fence

Bounded file tools ONLY: Read, Grep, Glob, Write. No Bash, no network, no
delegation. Read scope: repo-wide. Write scope: EXACTLY
`{RUN_DIR}/PKG_LEDGERS/PKG-XX_SCOPED_LEDGER.csv` and
`{RUN_DIR}/PKG_LEDGERS/PKG-XX_NOTES.md` for each assigned package. Never
write anywhere else; never edit `_STATUS.md`, kits, registers, or any file
outside your write scope. F-APP-3: never write `_DomainEngines/**` or
`projects/chirality-piping/**`.

## Task

1. For each assigned package, load its prior claim rows and changed-file
   manifest.
2. Apply the scope rule from `ORCHESTRATION_PLAN.md` (same AgentRuns folder as
   the run: `{PROJECT}/execution/_Coordination/AgentRuns/SCOPED_CONCORDANCE_2026-07-19/ORCHESTRATION_PLAN.md`)
   to select IN-SCOPE claims. Be inclusive at selection, precise at
   adjudication.
3. Re-adjudicate each in-scope claim against the LIVE tree at HEAD: confirm or
   re-disposition using the D-APP-55 disposition vocabulary (ALIGNED,
   STALE_SPECIFICATION, STALE_ASSESSMENT, STALE_VERIFICATION,
   PARTIALLY_IMPLEMENTED, IMPLEMENTED_DIFFERENTLY, IMPLEMENTED_UNDOCUMENTED,
   DOCUMENTED_UNIMPLEMENTED, REMAINING_STATE_MISMATCH, ACCEPTED_DIVERGENCE,
   AUTHORITY_CONFLICT, UNKNOWN). Cite file+line evidence for every verdict.
4. Scan the package's changed files for NEW post-R6 drift not covered by any
   prior claim; mint rows `DEL-XX-YY-SCOPED-Snn`.
5. Write one CSV per package, header:
   `ClaimID,DeliverableID,InScopeReason,PriorDisposition,ScopedDisposition,Evidence,DriftClass,ProposedRepair,HumanDecisionNeeded`
   - InScopeReason: `(a)`, `(b)`, `(c)`, or `NEW`.
   - DriftClass: `NONE` (still aligned/unchanged verdict), `RESOLVED` (prior
     drift now repaired), `NEW_DRIFT`, `PERSISTING` (prior drift unrepaired —
     expected for rows whose repair was deferred/gated; say which gate).
   - ProposedRepair: proposal text or `NONE`. Proposal-only — you repair
     nothing.
   - HumanDecisionNeeded: YES only where a disposition itself needs an owner
     ruling; note why in NOTES.
   Quote any field containing commas; no multi-line fields.
6. Write PKG-XX_NOTES.md: counts (in-scope selected / confirmed / re-dispositioned /
   new rows), selection reasoning summary, anything ambiguous, and an explicit
   statement of what you did NOT examine (out-of-scope bulk stands on R3/R6).

## Return contract (your final message — raw data, no prose padding)

```
STATUS: COMPLETE|PARTIAL|BLOCKED
PACKAGES: ...
IN_SCOPE_SELECTED: <n per package>
DISPOSITION_DELTAS: <n rows whose ScopedDisposition != PriorDisposition, per package>
NEW_ROWS: <n per package>
HUMAN_DECISIONS: <n + one-line each>
FILES_WRITTEN: <exact paths>
CAVEATS: <or NONE>
```

Truthful attribution: your verdicts are agent claims, not owner acts.
Uncertainty about whether a boundary/fence is touched → mark UNKNOWN +
HumanDecisionNeeded=YES, never guess.
