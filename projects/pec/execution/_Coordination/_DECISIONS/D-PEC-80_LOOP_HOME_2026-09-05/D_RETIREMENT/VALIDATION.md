# D-PEC-80 D — final retirement verification

D supplements the pre-retirement A/B/C evidence without rewriting it.
The 2026-09-05 supplementary owner direction replaces the overlay treatment.
D-APP-114/115 were read from fetched origin/main; PEC acceptance is still
awaiting owner. This is one PR and one continued candidate Receipt 167.

| Check | Evidence / result |
|---|---|
| Six archive moves | RELOCATION_MAP.csv; before/after SHA-256 identical; git mv shows 100% similarity for every file |
| Original migration history | INTEGRITY.json; all 335 historical files still match original A hashes at their final chained homes |
| Intent and receipts | INTEGRITY.json; entire Owner intent section verbatim, exact source SHA; frozen receipt prefix unchanged |
| Remaining gates | REMAINING_AUDIT.json; 64 status files, zero Remaining surfaces; zero marker changes; no scope created |
| Constraint homes | D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md; 11 grouped constraints mapped to surviving sources; none homeless |
| Whole-tree plan references | PLAN_REFERENCE_INVENTORY.csv; 323 original matches classified; live PEC pointers updated, history preserved, unrelated sister-loop references untouched |
| Final legacy references | FINAL_REFERENCE_INVENTORY.csv / SUMMARY.json; no unclassified PEC legacy target; current packet provenance enumerated |
| Full post-commit Step 0 | POST_COMMIT_CHECKS.json; exit 0; step0.stdout includes exactly no committed plan: deliverables alone |
| Validators and tests | CHECKS/CHECKS.json; all ten commands exit 0: entrypoints, receipt validator, both Task Management registers, 89 focused tests, harness self-check, 6 API tests, 12 registry tests, core posture, diff whitespace |
| Post-commit candidate whitespace | POST_COMMIT_CHECKS.json / postcommit-whitespace.stdout; PASS |
| Fresh candidate-only acceptance | DRY_RUN.md and DRY_RUN_INPUT.txt; separate read-only child, no AGENTS/persona/prior report; committed discovery and paper walk |

The original B-only dry runs legitimately report a committed overlay. They
are historical execution evidence; D's input/report supersede their candidate
for final review. Neither an archived plan nor this validation record becomes
a selection surface. Only Remaining items or an exact scoped owner preparation
request can supply the selection basis under the generic init.

No Root/tools/source change was needed for D: PEC launchers already point to
the init, and the shared validator supports absence of plans. The scope grant
is unchanged. The owner-intent text is candidate ruling language under item D,
not an invented RULED act. On owner direction D rules with the other items;
the same row and Receipt 167 will be updated before any explicitly directed
merge. No merge is performed in this tranche.

Rerun from repository root: python3 on this directory's verify_retirement.py;
run the init's complete Step 0 block; run the parent run_check_suite.py with
D_RETIREMENT/CHECKS as its evidence target (or a fresh sibling output label).
The recorded compatible Python 3.13 is required for the existing v2 tests.
Self-check exit 0 retains its warning/review findings; no clean-corpus claim.
