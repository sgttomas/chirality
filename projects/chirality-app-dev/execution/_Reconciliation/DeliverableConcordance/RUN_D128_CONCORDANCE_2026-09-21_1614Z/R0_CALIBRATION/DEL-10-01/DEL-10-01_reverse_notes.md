# DEL-10-01 — Reverse-pass notes

- **Capability file:** `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows, AREA HARNESS).
- **Forward ledger:** sealed at sha256 `9a646f5897ce7abfede33ed12bab48cb343a95deafe89fedb37fea4e6d348599`. It is not modified.

## 1. Responses

- **PARTIAL (1):** CAP-HARNESS-053 → `DEL-10-01#CLM-016.2`.
  - DEL-10-01 owns the registry mechanism and gate.
  - It does not own the completeness and rule-check tools.
- **NOT_MINE (59):** everything else.
  - The other domain capabilities are assigned to PKG-10 siblings:
    - CAP-HARNESS-054: headless preview runner.
    - CAP-HARNESS-055: PEC proposal tools and bridge client.
  - DEL-10-01 only records the boundary status of those two (CLM-004.1, CLM-004.6).
- **CLAIMED_BY (0).** The domain-profile type mirror (`runtime-contracts`) is outside AREA HARNESS (`frontend/src/lib/harness/**`), so no capability row covers it.

## 2. Forward-row errors exposed

**None.** The reverse pass corroborates the forward pass:

- The capability file marks CAP-HARNESS-053/054/055 (and 031, 050, 051) `LEGACY-IN-PROCESS: no production importer outside lib/harness; reachable only from scripts/ or tests`.
- That is the same static-reachability finding recorded independently at CLM-004.1 (STALE_SPECIFICATION / CODEX_SOLE_ENGINE, R4).
- It strengthens CLM-004.1's MEDIUM confidence, but does not change the disposition.

One refinement, not an error:

- Post-release commit `da95ec194` ("Add application-owned dynamic tools to Runtime") adds a Codex-side mechanism for application-owned tools.
- It carries no domain tools. A grep of `packages/{contracts,daemon}/src/application-tools.ts` and `app-owned-composition.ts` found no domain tool registration.
- No App frontend or electron file consumes it.
- So CLM-004.1 stands. That mechanism is a plausible porting path for the R4 decision.

## 3. PostReleaseBasis revisit (calibration finding)

Method: read-only `git -C <frozen tree> show --name-only` on the four post-v3.0.1 commits, plus `git log` on the two domain-profile files. This is within Agent 0's clarified bound.

- **What the post-release commits touch:**
  - `da95ec194` and `cb08dbe2f`: Runtime application-tools, the daemon, the codex-supervisor, and the client.
  - `9ecbdecdf`: Runtime execution-tree probe artifacts only.
  - `ccb95e06a`: public export, and `frontend/electron/plan-export-ipc-contract.ts`.
- **Overlap with forward evidence:** none of these files is cited as evidence in any forward row.
- **The facade relocation (CLM-016.1)** predates the release:
  - `f4d7deb28` (2026-07-04): D-APP-49 type modules created in `@chirality/harness-contract`.
  - `99fe2edae` (2026-07-23): shared-daemon desktop pilot.
  - `df7d62308` (2026-09-05): "Relocate shared runtime into its project".
- **Rows that should have been YES: 0.** The forward `NO` on all 73 rows was correct, including CLM-016.1, which I had flagged as possibly post-release.
- **Corollary for CLM-016.1.** The relocation happened by 2026-09-05. That is after the v3 plan (2026-08-22), so PRE_V3_DRIFT does not apply, and UNRECORDED_JUDGMENT stands.
- **Candidate direction source, not read (out of bounds for this pass):** the `df7d62308` commit message ("prepare authority transfer") hints that a Runtime-extraction record may exist. A verifier could look for it among the CONTEXT sources. If found, the CauseTag would move to RUNTIME_EXTRACTION.

## 4. Calibration note

The forward pass's single `git log` was later brought within bound by Agent 0's clarification. It is recorded here and not repeated beyond the permitted `log`/`show` use.
