# Execution Scripts

Standalone validation and integrity tooling for the execution workspace.

## `references_hash_tool.py` (DEL-08-01)

Computes and verifies `ContentHash` fields for out-of-folder references in `_REFERENCES.md`.

### Commands

```bash
python3 execution/_Scripts/references_hash_tool.py compute <deliverable_or_references_path>
python3 execution/_Scripts/references_hash_tool.py verify <deliverable_or_references_path>
python3 execution/_Scripts/references_hash_tool.py recompute <deliverable_or_references_path>
```

### Output and Exit Codes

- `compute` / `recompute`
  - `0`: completed (file may or may not have changed)
  - `2`: invalid path or runtime error
- `verify`
  - `0`: verification passed (or bypass recorded with `--allow-bypass`)
  - `1`: verification failed
  - `2`: invalid path, missing bypass metadata, or runtime error

### Bypass Recording

Use only with explicit human approval:

```bash
python3 execution/_Scripts/references_hash_tool.py verify <path> \
  --allow-bypass --actor "<actor>" --reason "<reason>"
```

By default, bypass records append to deliverable-local `HASH_VERIFICATION_BYPASS.jsonl`.

## `validate_dependencies.py` (DEL-08-02)

Lints `Dependencies.csv` files against the v3.1 schema from `docs/SPEC.md` Section 6.

### Commands

```bash
python3 execution/_Scripts/validate_dependencies.py <path/to/Dependencies.csv>
python3 execution/_Scripts/validate_dependencies.py --scan execution/
```

### Output and Exit Codes

- `0`: all files pass (warnings allowed)
- `1`: one or more schema validation failures
- `2`: unreadable/missing inputs or tool failure

### JSON Output

Add `--format json` for machine-readable CI consumption.

## `app_hold.py` (APP-HOLD-1)

Read-only, idempotent scan-authoritative reliance gate for App ScopeOfWork
contracts. `scan` verifies every declared decomposition basis and exact hold
register parity. Register records are typed as `HOLD`,
`STRUCTURAL_BOOTSTRAP`, or `SOW_INITIALIZATION`; a hold always wins. `check` evaluates one of
`reliance`, `dispatch`, `checking-promotion`, or
`accepted-dependency-consumption` for explicit deliverable targets and entry
path. Exit 0 permits, 2 rejects invalid input or authority evidence, 3 blocks
a hold or failed admission condition, and 4 blocks register drift.

There is no generic runtime exception input. D-APP-104's historical structural row
admits unknown `DEL-09-07` only for `dispatch` through the exact
`SCA-APP-009:GATE5:PREPARATION:CANDIDATE_MIRROR` or
`SCA-APP-009:GATE5:PREPARATION:ACTUAL_WORKTREE` token, and only while its two
approved authority-postimage hashes, old pointer preimage, absent
`ScopeOfWork.md`, and five-file-only folder-shape checks all pass. The result
is labelled `admission_kind=STRUCTURAL_BOOTSTRAP`; pointer movement, contract
appearance, authority drift, or folder-shape drift expires it. This does not
authorize PREPARATION, repinning, scope change, or an audit waiver. Any other
override requires a separately accepted and applied App-loop amendment before
the act.

D-APP-107 replaces the expired live bootstrap row with one initialization row.
PROJECT_SETUP calls from the App root before its scope-of-work INIT dispatch:

```bash
python3 execution/_Scripts/app_hold.py check --operation dispatch \
  --entry-path PROJECT_SETUP:SCOPE_OF_WORK:INIT --target DEL-09-07
```

The tool pins the exact target/package/folder, accepted decomposition and
companion, post-SCA-009 pointer, and all five scaffold inputs. The production
ScopeOfWork must be absent. Only a regular `_run_records/` subtree may coexist
with those inputs; symlinks at any ancestor or descendant, special files,
missing inputs, and unexpected folder entries block. The result is
`admission_kind=SOW_INITIALIZATION`, with `BLOCK_SOW_INITIALIZATION` for an
ineligible dispatch. This is read-only, stateless eligibility checking; a
reported ALLOW is not a durable reservation or role authentication.

After the exact target/package contract appears, the row is reported
`CONSUMED` and ordinary scan/register checks govern every operation. A CLEAR
basis permits ordinary preflight, including the verifier, but does not grant
semantic acceptance. Malformed contracts, a HELD basis, mismatched identity,
or symlinked contract paths block. The skill and sealed brief retain their
write boundaries and lifecycle restrictions. D-APP-104 compatibility remains
fixture-tested; its immutable ruling/proposal bytes are unchanged.

## Suggested CI Snippets

```bash
# Workspace-wide dependency schema lint
python3 execution/_Scripts/validate_dependencies.py --scan execution/ --format json

# Pre-run reference integrity check for a target deliverable
python3 execution/_Scripts/references_hash_tool.py verify \
  execution/PKG-08_Optional_Integrity_Hardening/1_Working/DEL-08-01_References_Content_Hashes \
  --format json
```
