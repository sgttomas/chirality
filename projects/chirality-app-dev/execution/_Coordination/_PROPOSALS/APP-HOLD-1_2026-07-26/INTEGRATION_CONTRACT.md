# APP-HOLD-1 Exact Integration Contract

Status: `CANDIDATE_NOT_APPLIED`  
Basis: `918bb48b8fcee66c031d0d6d4040a46089f96067`

This file states the exact operational obligations proposed for later
application. It does not itself activate the hold.

## 1. Live placement

On exact owner acceptance:

1. copy `APP_HOLD_REGISTER.csv` to
   `projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv`;
2. copy `tools/app_hold.py` to
   `projects/chirality-app-dev/execution/_Scripts/app_hold.py`;
3. copy `tests/test_app_hold.py` and `tests/fixtures/` to
   `projects/chirality-app-dev/execution/_Scripts/tests/`; and
4. add the instruction and workflow-profile clauses below;
5. add the exact tool row in §7 to root `tools/REGISTRY.md`; and
6. add the exact project-local catalog block in §7 to
   `projects/chirality-app-dev/execution/_Scripts/README.md`;
7. materialize `D-APP-75_RULING_TEMPLATE.md` as
   `execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md`,
   transcribing the exact owner application ruling and final accepted
   candidate hash; and
8. add the exact D-APP-75 row below to
   `execution/_Coordination/_DECISIONS/_REGISTER.md`.

Before application, deterministically confirm `D-APP-75` is still unallocated.
A collision blocks and returns for reminting and refreshed candidate approval.

Proposed decision-register row:

```markdown
| D-APP-75 | Whether to accept and apply the exact APP-HOLD-1 scan-authoritative no-repin reliance hold | Reliance, dispatch, CHECKING promotion, and accepted-dependency consumption for App SOW contracts whose decomposition basis is unresolvable; exact application surfaces only | RULED (exact APP-HOLD-1 candidate accepted) | — | `execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md`; exact owner text and accepted candidate hash recorded there; no repin, product architecture, lifecycle issuance, Root/App SCOPE_CHANGE, release, or professional-reliance authority |
```

## 2. Exact App `AGENTS.md` clause

Add the following subsection after **Project-Wide Execution Discipline** and
before **Closeout And Git Discipline**:

```markdown
## APP-HOLD-1 Reliance Preflight

Before relying on, dispatching, promoting to `CHECKING`, or consuming an
accepted dependency for any App deliverable, every session, agent, and
workflow must run:

`python3 execution/_Scripts/app_hold.py check --operation <operation> --entry-path <declared-entry-path> --target <DEL-ID> [--target <DEL-ID> ...]`

from the App working root. `operation` is exactly one of `reliance`,
`dispatch`, `checking-promotion`, or `accepted-dependency-consumption`.
The execution-time scan and `execution/_Coordination/APP_HOLD_REGISTER.csv`
must agree. A held target always fails closed. APP-HOLD-1 has no
runtime-consulted exception registry and does not infer exceptions from owner
prose. An owner override requires a separately accepted and applied App-loop
amendment to the hold's live register, tool, and instruction surfaces before
the prohibited act begins.

The prohibition binds held contracts regardless of entry path. WORKING_ITEMS
preflight is the primary enforcement mechanism, not the source or limit of
the prohibition. Direct entry, resumed sessions, API paths, other agents, and
other workflows remain bound. A fan-in that observes work or dependency use
without a passing preflight must reject the return and keep dependants held.

APP-HOLD-1 never authorizes repinning. A register/scan mismatch, malformed
contract basis, missing preflight, or held target is blocking and returns to
the human through the active manager.
```

## 3. WORKING_ITEMS pre-dispatch contract

Every App package activation must place the following fields in its frozen
activation record before constructing or dispatching any child node:

```yaml
app_hold_preflight:
  operation: dispatch
  entry_path: <stable run or invocation identifier>
  selected_deliverables: [<DEL-ID>, ...]
  command:
    - python3
    - execution/_Scripts/app_hold.py
    - check
    - --operation
    - dispatch
    - --entry-path
    - <stable run or invocation identifier>
    - --target
    - <DEL-ID>
  result_path: <run-root>/APP_HOLD_PREFLIGHT.json
  result_sha256: <sha256>
  verdict: ALLOW
```

Repeat `--target <DEL-ID>` for every selected deliverable. `WORKING_ITEMS`
must not dispatch when the result is absent, malformed, stale against the
current scan/register hashes, or not `ALLOW`.

## 4. Lifecycle and dependency contracts

Before a proposed `CHECKING` transition, run `check` with
`--operation checking-promotion`. Before declaring or consuming an accepted
dependency, run it with `--operation accepted-dependency-consumption` for
every dependency deliverable. Before any other accepted-basis use, run it with
`--operation reliance`.

The caller persists the JSON result and its SHA-256 with the lifecycle,
dependency, or reliance record.

## 5. Fan-in contract

At fan-in, `WORKING_ITEMS` must:

1. rerun the execution-time scan and require exact register agreement;
2. enumerate all selected deliverables and all claimed accepted dependencies;
3. require a passing preflight for each applicable target and operation;
4. verify the preflight's `scan_fingerprint_sha256` and register SHA-256
   values against a current rerun and current register bytes;
5. reject any return that used a held target, regardless of entry path; and
6. hold only declared dependants while unaffected work remains eligible.

The fan-in result records `ACCEPT | REJECT_APP_HOLD | BLOCK_REGISTER_DRIFT`.

## 6. Registered integrity check

Add this check to `software-workflow.json`:

```json
"app-hold-integrity": {
  "cwd": ".",
  "command": [
    "python3",
    "execution/_Scripts/app_hold.py",
    "scan",
    "--require-register-match"
  ]
}
```

Add `"app-hold-integrity"` to `always_checks`. This registered check confirms
the live corpus and register remain aligned. Targeted preflight remains a
separate required act because registered checks have no selected-target or
entry-path context.

## 7. Tool contract and catalog entries

Classification: deterministic, read-only validator and evidence renderer.

Inputs:

- canonical repository top level;
- exact App execution root;
- exact live hold register, or a scan-only register fixture under declared
  contained fixture mode;
- operation, entry path, and deliverable targets for `check`; and
- optional JSON output confined to the candidate directory or App
  `execution/_Coordination/AgentRuns/` / `execution/_Evaluation/`.

Outputs: JSON to stdout or one contained `.json` evidence file.

Exit codes:

- `0`: scan/register parity passed or all targets allowed;
- `2`: invalid input, malformed contract/register, containment
  failure, or operational failure;
- `3`: one or more targets blocked by APP-HOLD-1; and
- `4`: scan/register drift.

Error posture: fail closed before any `ALLOW`.  
Idempotence: read-only and byte-stable for unchanged Git/corpus/register
inputs, except explicit evidence-output replacement at the same contained
path.

Every live hold-register row must record `authority_basis=D-APP-75`; the tool
fails closed on any other value.

Add this row to root `tools/REGISTRY.md` under **Validation**:

```markdown
| `projects/chirality-app-dev/execution/_Scripts/app_hold.py` | Python 3 | APP-HOLD-1 scan-authoritative SOW-basis hold validator and target/operation preflight; held targets always block and corpus/register drift fails closed | canonical repo/App execution roots, live hold register, `scan` or `check`, operation, entry path, targets, optional contained JSON output | JSON PASS/ALLOW/BLOCK evidence; exit 0 pass/allow, 2 invalid/operational, 3 held target, 4 register drift |
```

Append this block to App `execution/_Scripts/README.md`:

```markdown
## `app_hold.py` (APP-HOLD-1)

Read-only, idempotent scan-authoritative reliance gate for App ScopeOfWork
contracts. `scan` verifies every declared decomposition basis and exact hold
register parity. `check` evaluates one of `reliance`, `dispatch`,
`checking-promotion`, or `accepted-dependency-consumption` for explicit
deliverable targets and entry path. Exit 0 permits, 2 rejects invalid input or
authority evidence, 3 blocks a held target, and 4 blocks register drift.
There is no runtime exception input. Human override requires a separately
accepted and applied App-loop amendment to APP-HOLD-1 before the act.
```

## 8. Enforcement limitation

APP-HOLD-1 is universally binding but is not represented as universal
product-code interception. WORKING_ITEMS receives the primary mechanical
pre-act target gate. Direct/API/resumed/other-workflow entry is
instruction-bound and retrospectively rejected at governed fan-in if it
violates the hold. The registered workflow check detects corpus/register
drift only.

## 9. Closure tests

Application is not complete until:

- live scan equals the six-row expected set, or a mismatch returns for owner
  judgment;
- a held target fails for each prohibited operation through at least three
  distinct declared entry paths;
- an unaffected target passes;
- the CLI exposes no runtime owner-exception input and unrelated decision prose
  cannot release a target;
- register drift fails;
- candidate-layout and proposed-live-layout path resolution both pass;
- D-APP-75 remains unallocated before application, the ruling transcribes the
  exact owner approval and final candidate hash, the decision register is
  updated, and every live hold row cites `D-APP-75`;
- a fan-in fixture using a held accepted dependency returns
  `REJECT_APP_HOLD`; and
- no `ScopeOfWork.md` `decomposition_basis` value changes.
