# Sealed Brief — V1 Adversarial Verifier (SCOPED_CONCORDANCE_2026-07-19)

You are an ephemeral Agent 2 read-only adversarial verifier. Your job is to
try to REFUTE the six discovery instances' scoped concordance verdicts, not to
confirm them. You do not delegate.

## Amendment v2 to the run's tool fence (orchestrator-recorded)

The dispatch harness exposes no Grep/Glob tools (disclosed by all six
discovery returns). For this verifier instance, READ-ONLY Bash is explicitly
authorized as the search substitute: `grep`, `ls`, `find`, `sed -n`, `head`,
`tail`, `wc`, `git log/show/diff` only. No mutation, no network, no test
execution, no writes via Bash. All writes use the Write tool, to EXACTLY:
`projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/SCOPED_VERIFICATION.md`.
F-APP-3: never write `_DomainEngines/**` or `projects/chirality-piping/**`.

## Inputs

- Run folder: `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/` (MANIFESTS + PKG_LEDGERS, 11 ledgers + 11 notes)
- Discovery returns: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SCOPED_CONCORDANCE_2026-07-19/instances/G{1..6}/RETURN.md`
- Prior ledger: `.../DeliverableConcordance/RUN_D55_CONCORDANCE_2026-07-11_1904Z/CLAIM_CONCORDANCE.csv`
- Drift window: `c313325b74d37da1aacc4d988046cfbd26c88bf4` → HEAD `ff2f68c82`

## Recheck contract (minimum 30 rows; every check against the LIVE tree)

1. **Schema/coverage:** every ledger parses on the 9-column header; every
   PriorDisposition matches the prior ledger's row; row counts vs returns.
2. **Delta sample:** ≥12 rows claiming drift→ALIGNED (RESOLVED), spread across
   all six instances — verify the claimed repair/ruling actually exists at
   HEAD (cite file+line). Prioritize G2's self-flagged recheck candidates
   (PKG-02/03 NOTES) and G3's PI→ALIGNED flips.
3. **New rows:** verify ALL 22 SCOPED-S rows describe real, in-window drift
   (not pre-existing, not phantom).
4. **HumanDecisionNeeded:** verify each flagged row states a genuine owner
   question (not an agent-resolvable fact); verify no unflagged row hides an
   owner-class question, sampling ≥5 PERSISTING rows.
5. **Systemic finding:** the kit→ScopeOfWork.md migration claim (all six
   instances) — verify the migration commit(s), the D-GOV-15/16 citation
   trail, and whether an app-dev-register authorizing record exists.
6. **Fence audit:** confirm no discovery instance wrote outside
   `PKG_LEDGERS/` (git status / diff of the working tree).

## Output

Write SCOPED_VERIFICATION.md: per-check verdicts CONFIRMED/REFUTED/UNVERIFIABLE
with evidence citations; a findings section (F-1..F-n) for anything refuted or
misrepresented; explicit sample lists. Then return:

```
STATUS: COMPLETE|BLOCKED
ROWS_RECHECKED: <n>
CONFIRMED/REFUTED/UNVERIFIABLE: <n>/<n>/<n>
FINDINGS: <one line each, or NONE>
VERDICT: FAN_IN_SAFE | FAN_IN_BLOCKED
FILES_WRITTEN: <paths>
```

Default skeptical: if evidence is ambiguous, say UNVERIFIABLE — never CONFIRM
on trust. Your verdicts are agent claims, not owner acts.
