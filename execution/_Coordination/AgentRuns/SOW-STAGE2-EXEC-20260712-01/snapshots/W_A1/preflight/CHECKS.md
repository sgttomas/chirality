# W-A1 Preflight Checks

Status: `PASS — CANDIDATE AWAITING HELP_HUMAN A1-B0 FAN-IN`

| Gate | Result | Evidence |
|---|---|---|
| Refs and ancestry | PASS | `HEAD=main=origin/main=remote main=0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; `HEAD^=b4efb8e554354399aadf1f624c107f63ede3230d` |
| Exact A1 extraction | PASS | 15 P3 ordinary App rows; package distribution 2/4/5/4 |
| Source/status equality | PASS | 60/60 legacy source hashes and 15/15 `_STATUS.md` hashes equal P3; all source/control paths exist |
| Lifecycle and exclusions | PASS | 15/15 IN_PROGRESS, 15/15 non-pilot, 15/15 non-ISSUED; zero live `ScopeOfWork.md` |
| Live format | PASS | Active validator resolves 15/15 exactly `LEGACY_FOUR_DOC`, valid, zero issues |
| Context/dependency freeze | PASS | 15 context, 15 reference, 15 dependency-summary hashes; 13 dependency registers plus two intentional PKG-00 absences |
| Pilot non-absorption | PASS | 10/10 pilots remain exact `SOW_V1`; App=6, Piping=4; 10/10 candidate bytes and status hashes match accepted postmerge evidence; zero legacy files |
| Method authority | PASS | Active standard, skill, validator, converter, mapper, parity, checklist, and render hashes frozen; converter requires isolated migration and exact D-GOV-16 authority |
| Caller prerequisites | PASS | Accepted P2 manifests bind 64/64 root and 9/9 App classified callers; legacy and SOW supported; invalid and unauthorized dual states fail closed |
| Package ownership | PASS | Four manager candidate/evidence scopes are pairwise disjoint; 15 candidate, author, and verifier targets are unique |
| Author/verifier sequencing | PASS | Separate author and verifier per sealed row; verifier runs after author terminal and cannot repair candidate |
| Future integration contract | PASS | Five-path replacement per member, inverse rollback, unchanged status/control hashes, CHANGE-only serial integration |
| Profile/check freeze | PASS | App profile hash and exact commands resolved; always and execution-path-selected checks named in package plan |
| Output schema | PASS | A1 manifest has one header + 15 unique member rows; package plan has one header + four unique package rows and counts sum to 15 |
| Portable paths | PASS | Snapshot and terminal outputs contain no checkout-absolute or local-file URI paths |
| Output containment | PASS | Writes limited to the sealed preflight snapshot and ORCHESTRATOR-A1-B0 return/status |
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
- Unknowns: none material to A1 release basis.
- Waivers: none.
- Declared environmental state outside scope: the pre-existing untracked
  `.claude-worktrees/` container remains present and was neither inspected nor
  modified.
