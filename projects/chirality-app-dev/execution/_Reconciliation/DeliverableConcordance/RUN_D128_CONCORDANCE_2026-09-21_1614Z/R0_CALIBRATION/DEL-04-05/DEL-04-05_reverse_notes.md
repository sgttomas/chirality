# DEL-04-05: reverse-pass notes (RUN_D128 R0 calibration, unit F-04)

- Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows).
- Sealed forward ledger: `DEL-04-05_claims.csv`, SHA-256 `30f979c6…fa737`. It was not modified.

## 1. Responses

| Response | Count | Capabilities |
|---|---|---|
| CLAIMED_BY | 2 | CAP-033 (direct Anthropic engine) and CAP-036 (provider credential lookup) |
| PARTIAL | 7 | CAP-015, 016, 027, 028, 031, 035, 038 |
| NOT_MINE | 51 | All others |

Borderline NOT_MINE answers:

- **CAP-034** (Pi/oMLX redirect guards) and **CAP-055** (loopback-only PEC bridge) are network guards. They are not the provider boundary this SoW scopes, so I answered NOT_MINE.
- **CAP-034's** oMLX guard overlaps the finding in §2.

## 2. Forward-row errors exposed

**E-1: an implementation is missing from the forward ledger.** No forward row covers the oMLX work, which should have been a STATE row with disposition IMPLEMENTED_UNDOCUMENTED:

- **What was delivered.** `_STATUS.md` History records that DEL-04-05 delivered D-APP-72 work (2026-07-22):
  - authenticated literal-loopback oMLX validation;
  - exact model discovery;
  - isolated key handoff;
  - typed redacted failures.
- **Where it is in code.**
  - `frontend/src/lib/harness/omlx-provider-config.ts:40-76,132-142` (literal `http://127.0.0.1:<port>/v1`, manual redirect refusal).
  - The `omlx` branch in `frontend/src/lib/harness/api-key-store.ts:39`.
  - The `PROVIDER_*` channels in `frontend/electron/api-key-ipc.ts`.
  - The provider id `'omlx'` in `frontend/electron/api-key-storage.ts:14`.
- **The gap.** The SoW names only the Anthropic provider, and the forward pass did not add a row for this delivered scope. CAP-035 and CAP-036 were answered against the nearest rows (CLM-009.6 and CLM-009.1). This is a coverage gap in the forward ledger, not a wrong disposition on an existing row.
- **Likely disposition.** This code is also outside the App-owned Codex composition (its credential port is null, and it has no Pi/oMLX engine). The row would therefore likely be IMPLEMENTED_UNDOCUMENTED with CauseTag CODEX_SOLE_ENGINE.

**E-2: minor imprecision on CLM-009.1.**

- CLM-009.1 ImplementationEvidence does not cite `frontend/src/lib/harness/api-key-store.ts:39-43`, which is the shared lookup that both managers use.
- The disposition is unaffected.

No other forward row was contradicted by the capability inventory.

## 3. PostReleaseBasis revisit (read-only `git -C <frozen tree> show` of the four commits, as later permitted)

**Files each commit touched:**

| Commit | Files touched |
|---|---|
| `da95ec194` | Runtime `client.ts`, `app-owned-composition.ts`, `codex-supervisor.ts`, `runtime-daemon.ts`, `session-store.ts`, contracts, and new application-tools files and tests |
| `cb08dbe2f` | `codex-supervisor.ts` and `codex-application-tools.test.ts` |
| `9ecbdecdf` | Execution-evidence files only |
| `ccb95e06a` | Export files and `frontend/electron/plan-export-ipc-contract.ts` |

**Overlap with the lines the forward ledger relies on:**

- `app-owned-composition.ts:180,225` (null credential port and `offline`): lines 180 and 225 are outside the added (+) lines of the da95ec194 diff. That diff only adds the application-tools registry and the supervisor and daemon wiring.
- `codex-supervisor.ts:103-108` (`sandboxPolicy`): these lines sit in unchanged context between hunks.
- `runtime-daemon.ts:465-474,515-536`: the only hunks are at new lines 12-19, 54-57, 166-171 and 657-689.
- `client.ts:695-698`: the only hunks are at new lines 47-51 and 360-380.
- None of the cited tests changed. The tests I cited are `codex-supervisor.test.ts`, `codex-effective-home.test.ts` and `codex-app-server-client.test.ts`.

**Result:** 0 rows would change to `PostReleaseBasis = YES`. The forward assumption of `NO` holds.

**Calibration note:** the result was correct by luck. Four cited files were touched by the post-release commits, and only line-level diff inspection showed the relied-on lines predate them.
