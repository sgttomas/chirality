# VALIDATION EVIDENCE — APP_V3_PATHWAY_SEATING_2026-09-03

Basis `8140daec7ab7165f8972451dbdd3a67b8bb2fd38`; all commands run from the
repository root of the candidate worktree unless a `cwd` is stated. Pass/fail
only; detailed outputs live in the named evidence files.

| # | Check | Command (cwd) | Result |
|---|---|---|---|
| 1 | Basis gate | `git merge-base --is-ancestor 1537ddad1 origin/main`; `origin/main` = `8140daec7…` after PR #680 | PASS (branch re-based onto `8140daec7…`) |
| 2 | Pin identities | `shasum -a 256` of the plan HTML (`b0a57a91…`), A11 (`6197bae1…`), `_LATEST.md` (`12c7758b…`); `git log -1 -- <decomposition>` = `d6f6cadb2` | PASS (all exact, re-verified after re-base) |
| 3 | Whitespace | `git diff --check` | PASS |
| 4 | SOW validator | `python3 tools/scope_of_work/validate_scope_of_work.py <carrier>` for all nineteen carriers | PASS (`format=SOW_V1`) |
| 5 | Deliverable consistency scan | `python3 tools/validation/scan_deliverable_consistency.py <carrier>` for all nineteen; baseline comparison for DEL-02-05 and DEL-09-06 against `HEAD` copies | PASS (exit 0; zero identity mismatches; marker counts unchanged versus baseline) |
| 6 | Dependency schema | `python3 tools/validation/validate_dependencies_schema.py <Dependencies.csv>` for the eight changed registers | PASS |
| 7 | Dependency enums | `python3 tools/validation/validate_enum.py <ENUM> <value>` for every enum field of each added row | PASS |
| 8 | Closure audit | `PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir <packet>/Evidence/dep_closure` | PASS (exit 0; parity with the Gate-5 audit — see `DEPENDENCY_REFRESH.md`) |
| 9 | APP-HOLD-1 dispatch preflight | `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target <each of the nineteen carriers>` (cwd `projects/chirality-app-dev`) | PASS (`ALLOW`; no held target) |
| 10 | APP-HOLD-1 register match | `python3 execution/_Scripts/app_hold.py scan --require-register-match` (cwd `projects/chirality-app-dev`) | PASS |
| 11 | D-APP-38 authority corpus | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (cwd `projects/chirality-app-dev`) | PASS (v20; no drift; no corpus member or `_REFERENCES.md` touched) |
| 12 | Practitioner harness self-check | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | PASS (exit 0; unchanged baseline INFO 14 / NOT_APPLICABLE 1 / REVIEW 4 / WARN 43) |
| 13 | Practitioner harness pytest | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tools/practitioner_harness` | PASS |
| 14 | Receipt validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` before use of the cursor and after appending Receipt 205 | PASS (`VALID`) |
| 15 | Lifecycle invariance | for each carrier, the `Current State`, `Checking Approval SHA`, `Authorization Basis`, `Directive`, `blocked-on`, and `P06 Record` lines of `_STATUS.md` hashed against `HEAD` | PASS (identical for all nineteen) |
| 16 | Write-set containment | `git status --porcelain` enumerates only: the nineteen carriers' `ScopeOfWork.md`/`_STATUS.md` (all) and `_DEPENDENCIES.md`/`Dependencies.csv` (eight), `loop/WORKPLAN_2026-09-03_app_dev_loop.md` (new), `loop/LOOP_RECEIPTS.md` (append), `plans/steers/chirality_app_v3_app_ruling_record_a12_2026-09-03.md` (new), and this packet | PASS (no `docs/**`, `_REFERENCES.md`, corpus, `frontend/**`, register, decision, prior receipt, plan HTML, prior steer, Root, or SCA snapshot byte) |
| 17 | Workplan selector | after commit: `git ls-tree HEAD:projects/chirality-app-dev/loop/ \| grep WORKPLAN_ \| LC_ALL=C sort \| tail -1` | recorded in the PR body and tranche return (expected `WORKPLAN_2026-09-03_app_dev_loop.md`) |
| 18 | Frontend gates | typecheck / Vitest / build-premerge / D-APP-36 | SKIPPED — no product or runtime source changed |

Deviations recorded: the receipt `Gate-Outcome` uses the validator's admissible
token `AWAITING_OWNER` (the brief's `AWAITING_OWNER_BYTE_REVIEW` is not an
admissible token under the D-APP-57 grammar); the count-table reconciliation
in `_DEPENDENCIES.md` corrected pre-existing drift in six files (listed in
`DEPENDENCY_REFRESH.md`).
