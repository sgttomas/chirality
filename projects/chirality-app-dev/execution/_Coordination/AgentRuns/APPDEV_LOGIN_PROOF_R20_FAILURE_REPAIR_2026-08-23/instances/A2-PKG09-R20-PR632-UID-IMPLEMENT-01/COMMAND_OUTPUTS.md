# Complete command outputs — PR #632 UID portability implementation

All executable validations below were invoked exactly once. Read-only hash/diff postchecks are separately permitted by the sealed brief.

## APP-HOLD dispatch

Command from the App root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-UID-IMPLEMENT-01.md --target DEL-09-04
```

Exit `0`; complete output:

```json
{
  "active_hold_deliverables": [],
  "entry_path": "execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-UID-IMPLEMENT-01.md",
  "operation": "dispatch",
  "register_sha256": "e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f",
  "repo_head": "4a48aeaede2d050631006f8ff23fb11736752bef",
  "results": [
    {
      "contract_status": "CLEAR",
      "deliverable_id": "DEL-09-04",
      "entry_path": "execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-UID-IMPLEMENT-01.md",
      "hold_status": "NOT_HELD",
      "operation": "dispatch",
      "verdict": "ALLOW"
    }
  ],
  "scan_fingerprint_sha256": "8a090f0982e99fee1f13a974c2ee341043c22216c43311190fd895258546059f",
  "scan_held_deliverables": [],
  "schema": "chirality-app-hold-check/v1",
  "targets": [
    "DEL-09-04"
  ],
  "verdict": "ALLOW"
}
```

## Ordinary focused suite

Command from `frontend`:

```text
./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
```

Exit `0`; complete substantive output:

```text
RUN  v4.1.10 /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend

Test Files  1 passed (1)
Tests  72 passed (72)
Start at  14:05:48
Duration  3.30s (transform 66ms, setup 0ms, import 78ms, tests 3.16s, environment 0ms)
```

## `umask 0002` focused suite

Command from `frontend`, in one shell:

```text
umask 0002
./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
```

Exit `0`; complete substantive output:

```text
RUN  v4.1.10 /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend

Test Files  1 passed (1)
Tests  72 passed (72)
Start at  14:06:10
Duration  3.25s (transform 45ms, setup 0ms, import 57ms, tests 3.15s, environment 0ms)
```

## Full local-socket suite

Exact elevated command from `frontend`: `npm test`. Permission was limited by the brief and request to local Unix-domain and loopback test sockets; external network was forbidden. No ordinary-sandbox diagnostic was run.

Exit `0`; complete substantive output:

```text
> chirality-frontend@2.0.0 test
> vitest run

RUN  v4.1.10 /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend

{"status":"FAIL","summaryPath":"/var/folders/96/1_3ww0012pv5ptwwsd1990yw0000gn/T/chirality-daemon-proof-test-BqIxpa/evidence/summary.json"}

Test Files  155 passed | 1 skipped (156)
Tests  1282 passed | 4 skipped (1286)
Start at  14:06:26
Duration  3.97s (transform 4.18s, setup 0ms, import 7.20s, tests 21.99s, environment 7ms)
```

The JSON `status: FAIL` line is an expected stdout fixture emitted by a passing test; the Vitest process and aggregate suite both passed.

## Typecheck

Command from `frontend`: `npm run typecheck`.

Exit `0`; complete output:

```text
> chirality-frontend@2.0.0 typecheck
> tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false
```

## Proof-script syntax

Command from `frontend`: `node --check scripts/run-packaged-launchagent-login-proof.mjs`.

Exit `0`; output was empty.

## Static inventory and immutable controls

One POSIX-shell assertion checked the exact count and retained-literal conditions in `IMPLEMENTATION_INVENTORY.md` plus both immutable hashes and sizes. Exit `0`; complete output:

```text
STATIC_UID_INVENTORY_AND_IMMUTABLE_CONTROLS=PASS
```
