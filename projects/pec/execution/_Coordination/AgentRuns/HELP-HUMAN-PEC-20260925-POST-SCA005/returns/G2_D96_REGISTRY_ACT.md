# Return G2: D-PEC-96 option-A registry act (WORKING_ITEMS)

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, graph node G1 (the act). Brief `G2_D96_REGISTRY_ACT.md`, SHA-256 `e9dadc1a5a783d5a87597dc98659d6e1ca495a14d5071363d13e66e828594541`, verified before work began. Date 2026-09-26.

## Publication

- **PR:** #950, https://github.com/sgttomas/chirality/pull/950. It is open and not merged.
- **Branch:** `claude/pec-d96-registry-act`, cut from `origin/main` `f90320c1d110cad75d04c96c91a595b7eb244498`.
- **Head before this return:** `02ae9e2a09bd8497c6de5d786722b803cca3d03a`. This return file is committed on top of it, so the final head is the commit that adds this file.
- **Commits:**

  | Commit | Contents |
  |---|---|
  | `d7c43074` | run root, scripts and dispatch preflight |
  | `c5536209` | act (product writes) |
  | `590066fd` | checks |
  | `dd63560a` | `MEMORY.md` |
  | `a8e6fd95` | run records |
  | `02ae9e2a` | verdict 01 and the N1/N2 repairs |

## Act report

- I ran `apply_d96.py` (`80725b4f…bbf3`, copied byte for byte into the run root) once from the repository root.
  - The output reads 6 UNCHANGED, 11 READ, 11 WRITE, then `OK option=A files=11 mode=written`.
  - It exited 0 with empty stderr.
  - A non-writing `--check-only` run came first.
  - `--repo` was given as the literal absolute worktree path. That path equals `git rev-parse --show-toplevel`. The host's isolation guard refuses a command substitution there.
- All 11 postimages equal the grant table.
  - 10 are modified and 1 is created (`schema_version_1.json`).
  - The path-list hash is `b5db12e5…c73c`.
  - The 6 must-remain files are unchanged.
- PEC's row now reads `shared-dev-loop` v1 live, `loop-receipts-ledger` v1 historical and `agentruns-json` v1 historical, as ruled in question 2.
- `MEMORY.md` was created from the template (`5a9564f4…6a5a`).
  - Its SHA-256 is `035ecb8686d72b18eb680531e1239ab4b2df4f5ae1b70811f6e4d667ccf30a3f`.
  - The only substitution is `{{DEL-ID}}`.
  - It has no run row: node M1 writes that at closeout.

## Written paths

The 11 product paths and their postimage hashes are tabled in `MANIFEST.md`, and they equal the proposal's grant table. The other written paths are:
- DEL-01-06 `MEMORY.md`;
- the run root `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/**` (per-file hashes are in Git);
- this return.

## Checks

The full record is in the run root's `VALIDATION.md`. Every command, with its cwd and exit code, is in `checks/COMMANDS.txt`.

| Check | Result |
|---|---|
| Reliance holds, `dispatch-for-production` (before the act) and `rely-for-production` (before fan-in) | ALLOW on all 13 targets both times |
| Selection | exactly the five registered checks |
| `v2-loop-registry` | Ran 19, OK (12 before) |
| `v2-store-guard` | 13 OK |
| `v2-api-contract` | 6 OK |
| `v2-core-posture` | PASS, 0 findings; core tree `88f590c0…c016` → `dd7e1dda…6e5a` |
| `harness-self-check` | exit 0; output byte-identical before and after (`8856b78f…70fe`; WARN=126, where the prototype had 124 because `main` moved) |
| Enforcement | 28 OK |
| Receipts validator | output identical before and after |
| Mutation | 19/19 CAUGHT, none `NOT_APPLIED`, `RESULT PASS` |
| Byte identity | 11/11 |
| Basis citations | 4/4 present |
| Non-ASCII bytes | 0 |
| `git diff --check` | clean |
| `remaining` in `v2/` | no match |
| Strict register validator | exit 1 with 26 pre-existing `XRG-013` warnings (D-GOV-48); output byte-identical before and after; no new finding |

There was one operator error, which is disclosed. The first selection call used repository-relative paths and selected only the three always-checks. I reran it with project-relative paths, which selected all five. Both outputs are kept.

## Verifier

**Verdict 01** (fresh `pec-reviewer`, Opus 5.5 high, on `a8e6fd959`) is **PASS WITH NOTES**, with no BLOCKING findings.
- It reproduced the act byte-identically on a fresh `git archive` export of `f90320c1d`, the same day.
- It reran every check, including the mutation run, whose output was byte-identical to mine.
- Containment was clean.

Its findings, and what I did with each:

| Finding | Class | Disposition |
|---|---|---|
| N1: time misstated in `MANIFEST.md` | non-blocking | repaired |
| N2: undisclosed `RUN.md` substitution | note | repaired by disclosure |
| N3: adapter stricter than the schema text (bound bytes) | note | carried as `HANDOFF_STATE.md` residual 9 |
| N4: `origin/main` moved to `53145aaeb` (PR #947, disjoint, merges cleanly) | note | carried as residual 11 |
| N5: the brief's hash cannot be checked from inside the repository | note | no action |
| N6: test assertion nit (bound bytes) | note | carried as residual 10 |

**Backcheck (verdict 02)** of the N1/N2 repairs at `02ae9e2a0` was dispatched to the same verifier and was still running at hand-back. It is not yet recorded as `VERIFIER_VERDICT_02.md`.

## Containment

At `dd63560a7` the branch diff was 11 product paths, each with its granted act, 54 run-root files and 1 `MEMORY.md`, with nothing outside. The verifier's check at `a8e6fd959` found 73 paths (11 product, 1 `MEMORY.md`, 61 run-root) with nothing outside. Later commits add only run-root files and this return.

## Unresolved (for HELP_HUMAN)

1. **Verdict 02 is pending.** Collect the backcheck from agent `a79a9fdd7f3abb1ed`, then commit it to the run root as `VERIFIER_VERDICT_02.md`.
2. **CI was pending at hand-back.** `origin/main` has moved to `53145aaeb`. If CI reports "Update the PR base", I have not repaired it.
3. **Merge and owner records.** Merging is HELP_HUMAN's decision under the standing authorization. HELP_HUMAN also owns the work graph, the central receipt, `docs/STATUS.md` and `README.md`, the register-row wording after merge, and the `MEMORY.md` run row (node M1).
4. **Carried residuals, as the ruling directs:**
   - the stale "declares `remaining-loop` now" text goes to S2 and a later scope change;
   - the SOW revision-1.4 lag goes to S2;
   - R-05 and FX-PEC-0 go to X1;
   - the path-normalization residual stays open;
   - verdict 01's N3 and N6 stay open.

## Limits honoured

- No lifecycle change and no Gate 5 act.
- No write to `_STATUS.md`, the SOW, the decomposition, a register, `docs/**`, `projects/pec/AGENTS.md` or `_DECISIONS/**`.
- No CHECKING, ISSUED or acceptance.
- The owner was not asked about CHECKING.
