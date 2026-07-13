# C2F Read-Only Diagnostics

Basis checked: `main@e150c972889d05a8fc270239451a35c7512dc9a9`

## Manifest and containment results

- P0 exact caller rows: `64`; aggregate classified rows: `8`.
- C2R manifest rows: `64`; surface-set delta from P0: `0`.
- P0 disposition totals: `58 ACTIVATE`, `5 RETAIN_LEGACY`,
  `1 DERIVATIVE_REGENERATE`; C2R reproduces the same totals.
- Frozen App rows: `9`; rows absent from P0: `0`.
- C2R changed subject paths: `48`; App changed subject paths: `4`.
- Root/App changed-path intersection: `0`.
- Manifest-versus-live-diff gaps: `0` in both lanes.
- Current post-hash mismatches: `0` for root/C1G rows and `0` for App rows.
- Forbidden deliverable/control/status/lifecycle/receipt/release paths in the
  52 changed subject paths: `0`.
- Regenerated public export rows: `610`, matching the candidate evidence.

The root coordination `WORK_GRAPH.json` change and run/evaluation evidence are
control-plane writes by their owning sessions and are not candidate source
paths. `.claude-worktrees/` was not read or touched.

## Targeted current reruns

| Check | Result |
|---|---|
| root resolver/reporting/semantic focused pytest | PASS, 30 passed |
| agent instruction validator | PASS, 33 files; 0 errors; 0 warnings |
| skill metadata validator | PASS, 44 valid; 0 invalid |
| public export profile | PASS, 1 passed |
| Git diff hygiene | PASS |
| App seven-file focused seam | PASS, 7 files; 70 tests |
| App typecheck | PASS |

Existing current-hash-bound evidence also records root tools `788 passed`, App
full frontend `707 passed / 4 skipped`, build PASS, self-check PASS,
practitioner harness `264 passed`, and the owned-server premerge rerun PASS at
Section 8 `8/8` and Section 9 report-only `16/16`.

## Fail-closed authority diagnostics

The ratified standard, `docs/SPEC.md`, and `docs/TYPES.md` require an exact
accepted migration authority for `MIGRATION_DUAL`. Both implementations only
check syntax plus self-consistency:

- root `tools/scope_of_work/common.py:41,335-339` accepts any
  `D-GOV-16@[0-9a-f]{7,64}` that is repeated in the candidate marker;
- App `frontend/src/lib/workspace/filesystem.ts:177,652-657,704-705,743-745`
  does the same with isolation and path membership;
- root tests intentionally use and accept synthetic
  `D-GOV-16@0123456` (`test_scope_of_work_tools.py:11,63-64,103-112`);
- App tests intentionally use and accept the same synthetic authority
  (`workspace-deliverable-contract-scanner.test.ts:111-145`).

Neither lane proves equality to or provenance from the accepted D-GOV-16
ruling `7584718aa32b112e415331736d1a8e68c12ac176`. A syntactically valid but
unruled self-bound token therefore reaches `MIGRATION_DUAL`, so the mandatory
unauthorized-dual failure case is not closed.

## ISSUED binding diagnostic

The standard and `skills/scope-of-work/{BRIEF_SCHEMA,SKILL}.md` require ISSUED
preparation to bind the accepted basis as well as source commit, four source
hashes, and `_STATUS.md` hash. The converter checks only the latter inputs
(`convert_four_documents_to_scope_of_work.py:52-63`), emits only those markers
(`:153-155`), and exposes no accepted-basis CLI input (`:193-195`). Its ISSUED
test succeeds without an accepted basis (`test_scope_of_work_tools.py:82-91`).

## Evidence-contract diagnostic

The project-local C2A return and status are terminal PASS, but the root
`instances/WORKING-C2A/STATUS.json` remains `READY`, declares
`return: RETURN.md`, and the declared root return pointer is absent. This is a
schema/control evidence inconsistency even though the project-local evidence
is sufficient to assess the source candidate.
