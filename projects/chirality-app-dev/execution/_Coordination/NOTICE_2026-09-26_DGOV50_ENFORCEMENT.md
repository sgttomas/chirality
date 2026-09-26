# D-GOV-50 tool enforcement and the ScopeChanging register column

Owner-authorized Root tranche `ROOT-DGOV50-ENFORCEMENT-20260926` enforces D-GOV-50 (reopening an `ISSUED` deliverable under an accepted amendment) in the Root tool and adds a `ScopeChanging` column to the scope-change action register (D-GOV-51, `docs/SPEC.md` §3.3). On 2026-09-26 the owner directed: "D1 and D2 as recommended, D3 (a), and D4 yes proceed that way. Your work plan is approved."

- `ScopeChanging` column. The accepted action register (`Amendment_Actions.csv`, or the name the group-2 `ACCEPTED_MANIFEST.csv` binds) gains `ScopeChanging`, `YES` or `NO`. Checkpoint-group-2 preparation fills it on every row, and the human accepts it with the register. `Intake_Actions.csv` may leave it blank. For a deliverable `RECLASSIFY`, `YES` records that the reclassification changes the deliverable's scope; only a `YES` row authorizes reopening.
- New checker `tools/validation/check_amendment_reopen.py` (CLI and importable `check_reopen()`). It admits a reopening only when all three checks pass:
  - a `checkpoint_snapshots/{AMENDMENT_ID}_GROUP-3_*/` folder holds `ACCEPTED_MANIFEST.csv` and a `DECISION.md` whose first heading reads `# {AMENDMENT_ID} checkpoint group 3 — accepted …`;
  - the register is bound by SHA-256 in the amendment's group-2 `ACCEPTED_MANIFEST.csv`, and its bytes are unchanged;
  - a register row has `EntityType` `DELIVERABLE`, the deliverable's ID, and `MODIFY`, or `RECLASSIFY` with `ScopeChanging` `YES`.

  It reads only inside the scope-change root and refuses paths and symlinks that leave it. Group-1 and group-2 decisions, candidate snapshots and other actions are refused.
- Legacy registers. In a register accepted without `ScopeChanging`, the checker admits `MODIFY` but refuses `RECLASSIFY`. It also refuses a run without a group-3 decision snapshot or a hash-bound group-2 register. In those cases the human records a lawful reopening directly, citing the accepted snapshot, as under D-GOV-50.
- `tools/scaffolding/write_status.sh` now admits `ISSUED → IN_PROGRESS` only with all of these:
  - a `HUMAN` actor and a git repository;
  - `--approval-sha` on every root: well formed, reachable, and a commit containing the group-3 `DECISION.md`;
  - a new `--amendment <id-or-path>` that passes the checker.

  None of these refusals can be overridden. Without `--amendment` the transition stays `BACKWARD_TRANSITION`. The history line records the amendment, the group-3 snapshot, the register row and the approval SHA. Every other refusal is unchanged.
- `scope-change` records group 3 as a decision folder with that heading when the amendment authorizes reopening an `ISSUED` deliverable. PEC's SCA-005 and SCA-006 records already match. `project-setup` `INCREMENTAL` Phase 5.5 presents the `write_status.sh --amendment` command to the human.

Accepted registers, SCA snapshots and `_STATUS.md` records are not rewritten. `docs/SPEC.md` changed in §3.3, so a loop that pins SPEC will see drift.

This loop's lifecycle validator, `frontend/src/lib/lifecycle/transition.ts`, is unchanged by this tranche and still refuses `ISSUED → IN_PROGRESS`. A following App pull request will mirror the checker there: the same three checks, the same refusal codes and legacy rule, and a human actor with an approval SHA and amendment reference. That answers DEL-07-04 REQ-004 in the validator, not only in prose. The refusal codes are `AMENDMENT_UNRESOLVED`, `SCOPE_CHANGE_ROOT_NOT_FOUND`, `PATH_ESCAPE`, `AMENDMENT_OUTSIDE_DELIVERABLE_ROOT`, `GROUP3_NOT_ACCEPTED`, `GROUP2_MANIFEST_MISSING`, `MANIFEST_SCHEMA`, `REGISTER_NOT_BOUND`, `REGISTER_AMBIGUOUS`, `REGISTER_MISSING`, `REGISTER_HASH_MISMATCH`, `REGISTER_SCHEMA`, `NO_DELIVERABLE_ACTION`, `RECLASSIFY_LEGACY_REGISTER`, `RECLASSIFY_NOT_SCOPE_CHANGING` and `ACTION_NOT_AUTHORIZING`. This loop holds accepted `SCA-APP-*` amendments, whose registers are legacy; their `MODIFY` rows would be admitted once each has a group-3 decision snapshot and a hash-bound group-2 register. This loop decides its own adoption; this source tranche grants no release.
