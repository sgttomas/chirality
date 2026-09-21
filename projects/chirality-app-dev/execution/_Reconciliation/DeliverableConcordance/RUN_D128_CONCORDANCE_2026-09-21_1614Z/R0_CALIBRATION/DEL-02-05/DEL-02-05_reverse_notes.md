# DEL-02-05 — reverse-pass notes (unit F-02)

Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows).
Reverse file: `DEL-02-05_reverse.csv`. The validator result is `RESULT PASS errors=0 warnings=0`.
The sealed forward ledger `DEL-02-05_claims.csv` (sha256 `e9239979…ee89`) was not modified.

## Responses

| Response | Rows | Capabilities |
|---|---:|---|
| CLAIMED_BY | 2 | CAP-HARNESS-013 → CLM-010.6; CAP-HARNESS-015 → CLM-010.5 |
| PARTIAL | 7 | CAP-HARNESS-002, 014, 016, 017, 027, 036, 039 |
| NOT_MINE | 51 | All other capabilities |

- **Coverage.** HARNESS is mostly engine, tool, session and Runtime-client behaviour. This
  deliverable's surfaces sit mainly in `components/settings/**` and `electron/api-key-*`, which
  this area file does not list. The low claim count is expected.
- **Rows with an arguable owner.**
  - CAP-HARNESS-016 and 017 are the hosted-bootstrap client and context. They serve both the
    V3-03 account presentation (this deliverable) and project admission and model gating
    (other deliverables). Both were marked PARTIAL to REM-1.

## Forward-row errors exposed

None.

- **REM-1 is mapped to shipped capabilities.** The reverse pass confirms REM-1's reading: the
  Codex login client and context are shipped harness capabilities (CAP-HARNESS-016 and 017).
  This supports the forward REMAINING_STATE_MISMATCH disposition.
- **CLM-010.3 cites a different file than the capability.** The capability file lists a second
  credential lookup at `frontend/src/lib/harness/api-key-store.ts` (CAP-HARNESS-036: Electron
  globals, then environment). The forward row cites the resolver in
  `frontend/electron/api-key-storage.ts:227-251`. Both apply the same order, so the disposition
  is unaffected. The duplicate resolver is a cross-deliverable observation (DEL-04-05).

## PostReleaseBasis revisited (calibration finding)

The forward pass set `PostReleaseBasis = NO` on every row by assumption. I have now inspected
the four post-v3.0.1 commits with read-only `git show --name-only` against the frozen tree:

| Commit | Touched files within the evidence roots |
|---|---|
| `da95ec194` | Runtime `client.ts`, `contracts/application-tools.ts`, `contracts/index.ts`, `contracts/protocol.ts`, `core/session-store.ts`, `daemon/app-owned-composition.ts`, `daemon/application-tools.ts`, `daemon/codex-supervisor.ts`, `daemon/runtime-daemon.ts`, and three application-tools tests |
| `cb08dbe2f` | `daemon/codex-supervisor.ts` and `tests/codex-application-tools.test.ts` |
| `9ecbdecdf` | Runtime `execution/**` only, which is out of bounds and was not read |
| `ccb95e06a` | `frontend/electron/plan-export-ipc-contract.ts` only; all other files are outside the evidence roots |

The forward ledger cites these Runtime files and tests:

- `packages/daemon/src/codex-login.ts`
- `packages/daemon/src/codex-effective-home.ts`
- `packages/contracts/src/harness/types.ts`
- `packages/contracts/src/harness/agent-engine-port.ts`
- `tests/app-owned-composition.test.ts`

None of them is touched by the four commits, and none of the cited frontend files is touched
either.

**Result: 0 rows would change to YES.** The assumption held for this deliverable. It was
unverified at seal time, so it should not be relied on for other units.
