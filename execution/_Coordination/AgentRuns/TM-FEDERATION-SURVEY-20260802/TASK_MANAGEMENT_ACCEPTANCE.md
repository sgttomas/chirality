# TASK_MANAGEMENT Behavioral Acceptance — Federation Survey

RunID: `TM-FEDERATION-SURVEY-20260802`
Role: `TASK_MANAGEMENT` (Agent 1)
Status: `READY`
Date: 2026-08-02
Mode: read-only behavioral acceptance under implementation-plan §11
H2 publication/merge: `UNSATISFIED`

## Acceptance verdict

The invocation-local federation preflight is usable and faithful to the
aligned intent. A Root invocation and an App invocation both surveyed the
same four canonical tracked registers with `COMPLETE` coverage. Root received
the complete program-wide finding set; App retained the complete set in the
derived JSON while presenting only App-relevant relationships and required
program-integrity findings. No register changed, no foreign row was written,
no receiving row was created, and no human disposition or authority effect
was inferred.

This is behavioral evidence only. It is not semantic approval of any finding,
register row, decision, publication act, or merge.

## Accepted inputs

- `AGENTS.md`
- `agents/AGENT_TASK_MANAGEMENT.md`
- `plans/chirality-task-management/FEDERATION_SURVEY_IMPLEMENTATION_PLAN_2026-08-02.md`
- `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/COMPONENT_DESIGN.md`
- `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/VERIFICATION_FANIN.md`
- `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/HELPS_HUMANS_RETURN.md`
- current `tools/taskmgmt/taskmgmt.py` and
  `tools/taskmgmt/test_taskmgmt.py`

HELPS_HUMANS entered this acceptance boundary as `READY`. Its manager return
records H1 as unnecessary and H2 as unsatisfied.

## Invocation ordering and authority posture

`agents/AGENT_TASK_MANAGEMENT.md` places `Mandatory federation preflight`
before `Modes` and requires the survey after resolving the invoking register
and before entering any requested mode. It explicitly requires coverage to be
reported before normal-mode output, prohibits register writes and inferred
promotion/priority/elevation/closure/disposition, and says the requirement
binds only an already-invoked `TASK_MANAGEMENT` instance. No loop-entry,
schedule, CI, daemon, gate, or obligation to invoke the role is created.

The acceptance run therefore performed the preflight first and did not enter
a row-maintenance or resolution mode. Both JSON projections identify
themselves as `derived, rebuildable, gitignored, never authority`.

## Executed live contexts

Explicit outputs were kept outside the repository:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out /tmp/tm-federation-accept-root.json

python3 tools/taskmgmt/taskmgmt.py federation \
  --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out /tmp/tm-federation-accept-app.json
```

The live Piping context was additionally exercised at
`/tmp/tm-federation-accept-piping.json` to inspect the closure echo from its
local perspective.

| Context | Coverage | Registers | Complete findings | Presented findings | Result |
|---|---:|---:|---:|---:|---|
| Root | COMPLETE | 4 | 48 | 48 | global presentation confirmed |
| App | COMPLETE | 4 | 25 | 24 | App-relevant presentation confirmed |
| Piping | COMPLETE | 4 | 24 | 24 | local closure echo confirmed |

Every context inventoried these exact canonical registers:

1. `_DomainEngines/pec/_TaskManagement/REGISTER.csv` — namespace `PEC`, 6
   rows, validation `PASS`;
2. `execution/_Coordination/_TaskManagement/REGISTER.csv` — namespace `ROOT`,
   103 rows, validation `PASS`;
3. `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`
   — namespace `APP`, 24 rows, validation `PASS`;
4. `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv`
   — namespace `PIP`, 24 rows, validation `PASS`.

Root's 48 presented observations were 47 `FOREIGN_LINK_TO_LOCAL` findings and
one `REMOTE_CLOSED_LOCAL_OPEN` echo. App's 24 presented observations were all
`LOCAL_LINK_TO_FOREIGN`; the unrelated Piping/Root closure echo remained in
App's complete 25-finding JSON set but was not emphasized. This demonstrates
relevance filtering without loss of coverage disclosure or complete evidence.

## Zero-write proof

The four registers were hashed before Root/App execution and after all Root,
App, Piping, validation, and test activity. The hashes were identical:

| Register | SHA-256 before and after |
|---|---|
| Root | `584ee4f9eaa4006c37c248077b26d1aadd5e8678833c46991a2d1101b4fac0ac` |
| App | `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |
| Piping | `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` |
| PEC | `85b8e0a66975ffa44fec6db8597940ff2d87f61e8bd09316d1ea0e1d874a9c91` |

Each live projection independently reported `register_writes: 0`, equal
before/after hashes for every readable register, and no operational error.
The only acceptance outputs were the explicit `/tmp` projections and this
managed acceptance record. Canonical default projection locations for Root,
projects, domains, and Domain Engines are all covered by `.gitignore` rules.

## Disposition and closure-echo behavior

The helper constructs observations from typed fields and writes finding
records containing class, IDs, paths, source field, and evidence. It emits no
proposed or automatic disposition. The persistent agent contract separately
reserves every disposition to the owning human and permits register edits only
after that act.

The single live closure echo is:

```text
LOCAL_CLOSED_REMOTE_OPEN
local:  TM-PIP-023 (Piping, CLOSED)
remote: TM-ROOT-053 (Root, OPEN)
field:  SourceRef
evidence: linked rows have divergent CLOSED status
```

Root reports the same fact as `REMOTE_CLOSED_LOCAL_OPEN`. This run did not
repair, close, reopen, promote, or otherwise disposition either row. The echo
is an observation only.

## PARTIAL and manual fallback usability

The `PARTIAL` contract is usable and fail-closed:

- invalid or mixed-namespace canonical input yields exit 1 and `PARTIAL`;
- discovery or unreadable-input failure yields operational exit 2 while
  retaining `PARTIAL` evidence when possible;
- console output explicitly says not to infer global absence or closure; and
- output-to-register aliases, including symlinks, fail with exit 2 before a
  register can be overwritten.

The manual fallback contract is also actionable. If the helper is unavailable,
the invoked manager must still enumerate sanctioned tracked register shapes,
validate each register, inspect only the six named typed fields, apply the same
Root/non-Root presentation and coverage rules, disclose that fallback was
manual, and classify any limitation as `PARTIAL` or operational. The fallback
grants no projection or write authority. This is sufficient to continue local
non-dependent work while preventing any unsupported global-absence claim.

## Reproduced checks

```text
python3 -m pytest tools/taskmgmt/test_taskmgmt.py -q
33 passed in 0.06s
```

The passing suite includes tracked/untracked discovery, all canonical path
families, COMPLETE and PARTIAL coverage, discovery/read/output operational
failures, direct and symlink register-output collision, every finding class,
Root/non-Root presentation, exact typed-field linking, omission of `Notes`,
notice resolution, deterministic bytes, zero-write hashes, and coexistence of
the existing `validate`, `scan`, and new `federation` CLI surfaces.

All four explicit `taskmgmt validate` invocations also passed at 103/24/24/6
rows respectively.

## Usability findings and downstream posture

No usability defect or acceptance blocker was found. The console is a compact
summary; the complete inventory, exclusions, findings, coverage, errors, and
zero-write evidence remain available in the JSON projection, as designed.

Verdict: `READY` for HELP_HUMAN cross-manager fan-in. H2 publication and merge
remain unsatisfied, and this return does not authorize CHANGE or publication.
