# Runtime project — loop entry

Paths are project-relative except commands and explicitly repository-relative references.

## Map

Read shared `../../AGENTS.md` and the actual invoked role. Discover current authority at `execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md`, then `docs/PRD_AUTHORITY.md`, `docs/PRD.md` and `execution/_Decomposition/_AUTHORITY.md`. Use `execution/_Coordination/HANDOFF_STATE.md` and the newest `loop/LOOP_RECEIPTS.md` entry for continuity; historical payload labels do not override later owner acts.

The work surface is the accepted seven-carrier register in `execution/_Decomposition/RUNTIME_DELIVERABLE_REGISTER.csv` and each carrier's `ScopeOfWork.md`, `_STATUS.md` Remaining and `Dependencies.csv`. Discover declared coordination at `execution/_Coordination/_COORDINATION.md` and held gates at `execution/_Decomposition/HOLD_SUCCESSOR_MAP.csv`. No workplan or inferred DAG priority is selected here.

## Limits

Use only the current brief's authorized scope. Read the deliverable's activation requirements before production dispatch. A migration, initialized status or passing test does not activate work or release a hold. Preserve accepted historical evidence, `root-runtime-1` epoch 1 and the separate R16-B disposition. Shared instruction/tool changes route to Root; sibling changes route to their owning sessions. No operational account/state or release act is implied.

## Step 0 and first return

From the checkout, refresh remote references and run discovery:

```sh
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"
git fetch origin
git status --short --branch
git rev-parse HEAD origin/main
git rev-list --left-right --count HEAD...origin/main
python3 tools/practitioner_harness/harness.py status --project runtime
python3 tools/practitioner_harness/harness.py drift --project runtime
rg -n '^#|^##|^###' projects/chirality-runtime/loop/LOOP_RECEIPTS.md
rg -n 'Current State|Remaining|Depends|HELD' projects/chirality-runtime/execution/PKG-*/1_Working/DEL-*/_STATUS.md
```

First return: branch/main divergence and local changes; accepted authority and effective-state evidence; current lifecycle/holds; the exact authorized task and its read/write limits; available checks and unresolved prerequisites; next lawful manager action. If no applicable activation exists, distinguish authorized readiness preparation from blocked production rather than inventing an execution queue.

Record actual checks and a durable project handoff under the governing run's closeout contract, with truthful model and role attribution. Human acceptance and merge remain actual owner acts under shared CHANGE. Receipt prose is evidence; no Runtime receipt validator or automatic receipt-format enforcement is claimed.
