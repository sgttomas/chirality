# A2-IMPLEMENT-R2 Return

RUN_STATUS: `SUCCESS`

ControlSurface: `FILE`

TaskProfile: `NONE`

TaskSkill: `NONE`

ScopePath: `/Users/ryan/.codex/worktrees/cc31/chirality`

WriteAuthorization: `ALLOWED_WRITE_TARGETS`

## Result

Implemented the full frozen invocation-local federation survey contract in the
existing Task Management tool and added focused coverage for discovery,
validation, joining, finding classification, presentation, failure semantics,
determinism, CLI compatibility, and zero-register-write behavior.

No H1 expansion was needed. The implementation adds no schema column, central
catalog, automatic invocation, CI/daemon behavior, authority effect, or foreign
write.

## Design traceability

- `federation --register PATH [--out PATH]` coexists with the existing
  `validate` and `scan` commands.
- Discovery uses `git ls-files` and admits only the four frozen sanctioned path
  families. Tracked invalid-shape and untracked register lookalikes are
  explicitly excluded and reported.
- Every discovered register is hashed, read, and passed through the existing
  `validate_register` function before its rows participate in the graph.
- Namespace inference implements `ROOT`, single-ID namespace, header-only path
  fallback, and mixed-namespace ambiguity.
- Typed joins use only exact `ActionItemID` tokens in `SourceRef`, exact
  `ElevatedTo`, semicolon-delimited `NoticeRef`, `Status`, and `Disposition`;
  `Notes` is never inspected for links.
- Notice references resolve independently against the owning working root and
  repository root, with zero/multiple results reported rather than guessed.
- All twelve frozen finding classes are emitted as deterministic observation
  records.
- JSON retains the complete finding set and a separately filtered presented
  subset. Root presents the global set; non-Root presents invoking-register
  relevance plus program integrity findings.
- `COMPLETE`, `PARTIAL`, and operational exit semantics are implemented with
  an explicit PARTIAL warning against global-absence/closure inference.
- Output is deterministic JSON with no timestamp and includes authority,
  identity, inventory, validation, findings, exclusions, ambiguities,
  operational errors, and register before/after hashes.

## Applied changes

- `tools/taskmgmt/taskmgmt.py` — federation implementation and CLI integration.
- `tools/taskmgmt/test_taskmgmt.py` — 13 new focused federation tests (29 total
  tests in the file).
- `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/instances/A2-IMPLEMENT-R2/RETURN.md`
- `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/instances/A2-IMPLEMENT-R2/STATUS.json`

Tool/test diff at closeout: 892 insertions, 3 deletions across the two authorized
tool/test paths.

## Focused test evidence

Command:

```text
python3 -m pytest tools/taskmgmt/test_taskmgmt.py -q
```

Result:

```text
.............................                                            [100%]
29 passed in 0.05s
```

Additional checks:

```text
python3 -m py_compile tools/taskmgmt/taskmgmt.py tools/taskmgmt/test_taskmgmt.py
git diff --check -- tools/taskmgmt/taskmgmt.py tools/taskmgmt/test_taskmgmt.py
git diff --check
```

All passed with no output/errors.

The focused matrix covers all four sanctioned shapes; tracked invalid-shape and
untracked lookalikes; valid, invalid, header-only, and mixed-namespace inputs;
discovery, read, and output operational failures; every finding class;
duplicate IDs and ambiguous targets; exact-token and Notes exclusion; missing,
ambiguous, semicolon-list, quoted/backticked, working-root, and repo-root notice
references; both closure-echo directions; Root/global and non-Root relevance;
deterministic bytes; legacy CLI compatibility; and byte/hash equality.

## Live survey evidence

Temporary output directory:
`/tmp/tm-federation-survey.C00N9w/` (outside the repository).

Root command/result:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out /tmp/tm-federation-survey.C00N9w/root.json

taskmgmt federation COMPLETE: 4 register(s), 48 finding(s), 48 presented
coverage: COMPLETE; register_writes: 0
FOREIGN_LINK_TO_LOCAL: 47
REMOTE_CLOSED_LOCAL_OPEN: 1
```

App command/result:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out /tmp/tm-federation-survey.C00N9w/app.json

taskmgmt federation COMPLETE: 4 register(s), 48 finding(s), 24 presented
coverage: COMPLETE; register_writes: 0
LOCAL_LINK_TO_FOREIGN: 47
REMOTE_CLOSED_LOCAL_OPEN: 1
```

Both projections report four PASS registers with namespaces/rows:
`ROOT`/103, `APP`/24, `PIP`/24, and `PEC`/6. Both report zero operational
errors, zero excluded live lookalikes, and equal before/after hashes for every
register. The Root/non-Root difference is presentation only; both JSON files
retain 48 complete findings.

## Register before/after SHA-256 proof

The hashes before implementation, before live execution, after live execution,
and inside both projections are equal:

| Register | SHA-256 |
|---|---|
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | `584ee4f9eaa4006c37c248077b26d1aadd5e8678833c46991a2d1101b4fac0ac` |
| `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` | `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |
| `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` | `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` |
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | `85b8e0a66975ffa44fec6db8597940ff2d87f61e8bd09316d1ea0e1d874a9c91` |

## Write-containment proof

- Persistent writes by this child are limited to the four paths named under
  **Applied changes**, exactly matching the sealed write scope.
- The only generated survey outputs were explicit temporary files outside the
  repository, as requested by the brief.
- No register, candidate surface, agent instruction, governance record,
  manifest, notice, ignore rule, loop file, CI file, schema, contract, PRD,
  receipt, handoff, commit, push, or merge was edited by this child.
- All four live register hashes equal the accepted baseline after tests and both
  live surveys.

## Tools used

- `python3 tools/taskmgmt/taskmgmt.py`
- `python3 -m pytest`
- `python3 -m py_compile`
- Git read-only status/diff commands
- SHA-256 read-only hashing

ToolPolicyCompliance: `N/A` (no tool allowlist was declared).

## Missing

None.

## Needs human ruling

None. H1 is not required.

## Dependency notes

None.
