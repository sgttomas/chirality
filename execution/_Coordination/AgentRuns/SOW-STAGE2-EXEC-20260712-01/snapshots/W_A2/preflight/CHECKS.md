# W-A2 Preflight Checks

Status: `PASS — CANDIDATE AWAITING HELP_HUMAN A2-B0 FAN-IN`

| Gate | Result | Evidence |
|---|---|---|
| Refs and ancestry | PASS | `HEAD=main=origin/main=remote main=b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4`; accepted binding `71a5511a7785a4157f3b614e75634ace024caef3`, W-A1 integration evidence `e64ce353597fa9a5ca39dcb4d0a24e0d0cb70d7a`, and D-GOV-16 are ancestors |
| Exact A2 extraction | PASS | 16 P3 ordinary App rows; package distribution 5/5/6 |
| Source/status equality | PASS | 64/64 legacy source hashes and 16/16 `_STATUS.md` hashes equal P3; all source/control paths exist |
| Lifecycle and exclusions | PASS | 16/16 IN_PROGRESS, 16/16 non-pilot, 16/16 non-ISSUED; zero live `ScopeOfWork.md` |
| Live format | PASS | Active validator resolves 16/16 exactly `LEGACY_FOUR_DOC`, valid, zero issues |
| Context/dependency freeze | PASS | 16 context, 16 reference, 16 dependency-summary, and 16 dependency-register hashes frozen; 171 dependency data rows total |
| W-A1 non-absorption | PASS | 15/15 W-A1 members remain exact `SOW_V1`; candidate and status hashes equal the accepted postmerge ledger; zero legacy files |
| Pilot non-absorption | PASS | 10/10 pilots remain exact `SOW_V1`; candidate and status hashes equal the accepted P4 postmerge ledger; zero legacy files |
| Remaining App exclusion | PASS | P3 contains 53 App members: exactly 16 A2 and 37 non-A2; only the 16 A2 live paths are listed in this release basis |
| Method authority | PASS | Active standard, skill, validator, converter, mapper, parity reporter, checklist compiler, and renderer hashes frozen; converter requires isolated migration and exact D-GOV-16 authority |
| Caller prerequisites | PASS | Accepted P2 manifests bind 64/64 root and 9/9 App classified callers; legacy and SOW supported; invalid and unauthorized dual states fail closed |
| Package ownership | PASS | Three manager candidate/evidence scopes are pairwise disjoint; 16 candidate, author, and verifier targets are unique |
| Author/verifier sequencing | PASS | Separate author and verifier per sealed row; verifier runs after author terminal and cannot repair candidate |
| Future integration contract | PASS | Five-path replacement per member, inverse rollback, unchanged status/control hashes, CHANGE-only serial integration |
| Profile/check freeze | PASS | App profile hash and exact registered commands resolved; always and execution-path-selected checks named in package plan |
| Output schema | PASS | A2 manifest has one header plus 16 unique member rows; package plan has one header plus three unique package rows and counts sum to 16 |
| Portable paths | PASS | Snapshot and terminal outputs contain no checkout-absolute or local-file URI paths |
| Output containment | PASS | Writes limited to the sealed preflight snapshot and ORCHESTRATOR-A2-B0 return/status |
| Project-tree read-only | PASS | No tracked, staged, or untracked changes under `projects/chirality-app-dev` |
| Diff hygiene | PASS | `git diff --check` passes for the authorized output scope |

## Tool execution boundary

The live validator was used read-only for format resolution. Converter, mapper,
parity, checklist, and renderer surfaces were inspected and hash-bound but were
not executed to produce candidates. No tool wrote a project path. No build,
conversion, repair, Git mutation, lifecycle act, H1/H2 act, release, or
retirement occurred.

## App command freeze

- `harness-self-check`: repository root,
  `python3 tools/practitioner_harness/harness.py self-check` (always).
- `harness-pytest`: repository root,
  `python3 -m pytest -q tools/practitioner_harness` (selected by execution/doc
  paths).
- `frontend-typecheck`: `projects/chirality-app-dev/frontend`,
  `npm run typecheck`.
- `frontend-test`: same working directory, `npm test`.
- `frontend-build`: same working directory, `npm run build`.
- `frontend-premerge`: same working directory,
  `npm run harness:validate:premerge`.

These commands are frozen as later package fan-in requirements; this read-only
preflight did not run project-writing build steps.

## Drift and exceptions

- Drift: none.
- Blockers: none.
- Unknowns: none material to A2 release basis.
- Waivers: none.
- Declared environmental state outside scope: the pre-existing untracked
  `.claude-worktrees/` container remains present and was neither inspected nor
  modified.
