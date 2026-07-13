# P3_MANIFEST B1 Checks

Verdict: `PASS — CANDIDATE AWAITING RECON-B1`

| Check | Result |
|---|---|
| refs | local main = origin/main = remote main = `9349594530dc19e55baf9c2ef0b7eb4716f48a17`; divergence `0/0` |
| tracked census | 154 members (App 53, Piping 101); exact P0 membership |
| companions / SOW | zero missing legacy/status files; zero `ScopeOfWork.md` |
| lifecycle | 153 `IN_PROGRESS`; sole `ISSUED` is Piping `DEL-01-01` |
| partition | ten pilots; 144 remaining; exact accepted identities |
| path digest | `b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31` |
| manifest comparison | 154/154 rows MATCH; all twelve fields MATCH; zero delta |
| P2 manifest | manifest hash exact; 15/15 bound path hashes exact |
| root callers | 64/64 current and disposed; 60 direct hashes plus four accepted App overlays |
| App callers | 9/9 current and disposed; seven direct hashes plus two accepted C2A-R1 repairs |
| caller search | broad and targeted commit-bound searches refreshed; zero active unclassified |
| C2 containment | 236 changed paths; zero governed project deliverable-population path |
| authority gates | H1 and H2 unapproved; no conversion/release/retirement action |

Commands were read-only `git rev-parse`, `git ls-remote`, `git rev-list`,
`git ls-files`, `git grep`, `git diff --name-only`, SHA-256 computation, TSV
parsing, and status-field extraction. Final structure, JSON, TSV, scope, and
`git diff --check` results are recorded after package assembly.

## Assembly validation

- Exact P3 file set: seven required files, PASS.
- `EXECUTION_MANIFEST.tsv`: 154 data rows / twelve fields, PASS.
- `ROW_COMPARISON.tsv`: 154 data rows / zero delta rows, PASS.
- `MANIFEST.tsv`: six bound artifacts / six exact hashes, PASS before the
  expected CHECKS hash refresh caused by this terminal note.
- JSON parse of the instance status surface: PASS.
- `git diff --check` on the declared P3 and instance write scope: PASS.
- Declared-output status enumeration: only the P3 package and B1 instance
  directory are untracked; parent-owned `WORK_GRAPH.json` and pre-existing
  `.claude-worktrees/` remain outside this instance and untouched.
