# WORKING-P-A Package Checks

Verdict: `PASS`

Basis: D-GOV-16 `7584718aa32b112e415331736d1a8e68c12ac176`;
P3 B1/G3 PASS; `PILOT-VALIDATION-001`; Stage-1 App evidence commit
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; synchronized
`main@0d260eb024d8b8dada0df477b70ac880a6906ffa`.

## Independent verifier fan-in

| Deliverable | Accepted child | Mappings | Source lines | Verdict |
|---|---|---:|---:|---|
| DEL-07-01 | TASK-APP-DEL-07-01-R1 | 31/31 | 370/370 | PASS |
| DEL-07-02 | TASK-APP-DEL-07-02 | 31/31 | 353/353 | PASS |
| DEL-07-03 | TASK-APP-DEL-07-03 | 31/31 | 339/339 | PASS |
| DEL-07-04 | TASK-APP-DEL-07-04 | 34/34 | 383/383 | PASS |
| DEL-07-05 | TASK-APP-DEL-07-05 | 35/35 | 419/419 | PASS |
| DEL-07-06 | TASK-APP-DEL-07-06 | 29/29 | 309/309 | PASS |

Aggregate: six of six terminal PASS returns, 191/191 mappings, and
2,173/2,173 source lines. Every accepted child independently confirmed valid
live `LEGACY_FOUR_DOC`, valid isolated target `SOW_V1`, exact candidate and
source/status hashes, Stage-1 identity, deterministic checklist and safe HTML
render pairs, lifecycle/control containment, and an exact five-path future
replacement manifest.

The original `TASK-APP-DEL-07-01` attempt is preserved as
`FAILED_SUBSTRATE_NONTERMINAL`; no verdict was inferred from its partial
outputs. Fresh R1 evidence alone is accepted for DEL-07-01.

## Package manifest, schema, and containment checks

- Aggregate schema/hash/path script: PASS. Six P3 rows and six candidate hashes
  match; every candidate is byte-identical to its Stage-1 commit blob and
  retains historical D-GOV-15 provenance without a D-GOV-16 marker.
- `PILOT_MANIFEST.tsv`: six rows, P3 source/status/lifecycle identity PASS.
- `REPLACEMENT_MANIFEST.tsv`: 30 rows, exactly one SOW ADD and four legacy
  DELETE actions per deliverable; no status/control action.
- `ROLLBACK_MANIFEST.tsv`: 30 rows and the exact action inverse of the
  replacement manifest at the same paths and hashes.
- Accepted child manifest-to-package manifest equality: PASS for all six.
- Checklist pair byte equality, render pair byte equality, parity issue lists,
  and HTML script/external-resource safety: PASS for all six.
- `git diff --check` over the candidate and manager package: PASS.
- `git status --short -- projects/chirality-app-dev`: empty.
- `HEAD`, `main`, and `origin/main`: all
  `0d260eb024d8b8dada0df477b70ac880a6906ffa`.
- `/tmp` residue matching `TASK-APP-DEL-07*`: none.

## App project checks

The manager ran the launch-brief minimum checks once at the accepted base. The
candidate package is read-only with respect to the App project.

| Check | Result |
|---|---|
| `npm run typecheck` in `projects/chirality-app-dev/frontend` | PASS |
| `npm test` in `projects/chirality-app-dev/frontend` | PASS — 97 files passed, 1 skipped; 713 tests passed, 4 skipped |
| `npm run build` in `projects/chirality-app-dev/frontend` | PASS — Next and Electron TypeScript builds completed |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | PASS — baseline INFO 15, N/A 2, REVIEW 27, WARN 6 |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tools/practitioner_harness` | PASS — 264 passed |

The current `software-workflow.json` path rules select no additional check for
the coordination-only candidate paths. `frontend-premerge` was therefore not
selected; it requires a running harness API and is scoped to runtime-premerge
evidence. Whitespace/format hygiene is covered by `git diff --check`.

Blockers, waivers, repairs, conflicts, and rerun requirements: none at the
recorded hashes and authority. Any accepted-basis, source/status/candidate,
tool, or `PILOT-VALIDATION-001` change invalidates this check record.
