# DEL-03-01 — reverse-pass notes (worker B)

- **Inputs:**
  - Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows, AREA HARNESS).
  - Sealed forward ledger: sha256 `90dd4ce1…0478d`. It was not modified.
- **Responses:** 1 CLAIMED_BY, 8 PARTIAL and 51 NOT_MINE.
  - The HARNESS area is almost entirely App-client or legacy in-process runtime behaviour.
  - DEL-03-01 owns the engine port and its conformance. It touches this area only where the port, stub, SDK/Pi conformance subjects, SSE compatibility and redaction checks appear.

## PostReleaseBasis revisit (calibration finding)

- **Method:** read-only `git show --stat` on the four post-v3.0.1 commits in the frozen tree.
- **What the commits touched:**
  - `da95ec194` changed `packages/daemon/src/app-owned-composition.ts`, `core/src/session-store.ts`, `codex-supervisor.ts` and the contracts `index.ts` and `protocol.ts`.
  - `cb08dbe2f` changed `codex-supervisor.ts` and one test.
  - `9ecbdecdf` added evidence files only.
  - `ccb95e06a` touched export files and `plan-export-ipc-contract.ts`.
- **Forward citations checked:**
  - The only cited file these commits touched is `app-owned-composition.ts:214`. `git blame` attributes that line (registration of the Codex delegated adapter) to a 2026-09-12 commit, which predates the release.
  - No other cited file or line (`agent-engine-port.ts`, `engine-conformance.ts`, `event-schema.ts`, `delegated-engine-adapter.ts`, `turn-coordinator.ts`, the frontend routes and tests, electron `main.ts` and `runtime-service-host.ts`) was touched.
- **Result:** 0 rows would change. `PostReleaseBasis = NO` holds for all 65 forward rows.

## Forward-row observations exposed by the reverse pass

No forward row is shown to be wrong. Two refinements for the verifier:

1. **`CLM-005.1` and `CLM-009.9`** (stub and SDK-backed adapter, ALIGNED).
   - The capability rows mark the whole frontend `lib/harness` in-process stack as legacy, with no production importer. This covers the engine registry, the stub, the Claude SDK and Anthropic managers, and the Pi adapter; CAP-HARNESS-028..034 describe them as reachable only from the controlled CI Runtime fixture and tests.
   - The forward notes already say this. A stricter verifier could read CLM-005.1's "SDK-backed adapter exists" as satisfied only by the Runtime Codex adapter, which carries no conformance run. That reading would move CLM-005.1 to PARTIALLY_IMPLEMENTED (CODEX_SOLE_ENGINE).
2. **Pi second-engine conformance** (CAP-HARNESS-034).
   - The `_STATUS.md` history records that SCA-APP-002 once placed a bounded second-engine contract and conformance tranche in DEL-03-01. The forward ledger has no row for that historical tranche; only CLM-009.10 covers it, and only partially.
   - Pi work is retired under Codex sole engine (HANDOFF §1), so no state claim is missed. This is a coverage note, not an error.
