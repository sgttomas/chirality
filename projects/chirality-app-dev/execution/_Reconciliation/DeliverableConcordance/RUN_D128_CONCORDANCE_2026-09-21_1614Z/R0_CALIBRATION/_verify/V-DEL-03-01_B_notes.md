# V-DEL-03-01_B — verifier shard notes (R0 calibration, unit V)

- **Shard:** `DEL-03-01_B`, one side of the double-blind pair.
  - `DEL-03-01_A/` was not read.
  - The verifier checked 58 SELECTION items against the frozen tree at `00115c719`.
- **Output:** `_verify/V-DEL-03-01_B.csv`, 58 rows plus `#END`, in the same order as SELECTION.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (non-ALIGNED / LOW / reverse-notes) | 53 | 42 | 2 | 9 |
| b (ALIGNED sample) | 3 | 2 | 0 | 1 |
| c (PARTIAL capability responses) | 2 | 2 | 0 | 0 |
| **Total** | **58** | **46** | **2** | **10** |

- **REFUTED**
  - `CLM-009.13`: the row should be PARTIALLY_IMPLEMENTED / PRE_V3_DRIFT, not AUTHORITY_CONFLICT.
  - `REGISTER-3`: the line-anchor sub-claim is wrong. The disposition itself holds.
- **CONTESTED**
  - The codex.* cluster: `CLM-004.1`, `CLM-009.2`, `CLM-009.7`, `CLM-018.2`, `CLM-022.2`.
  - `CLM-009.5`, `CLM-010`, `CLM-013.1`, `REM-2`, and `CLM-003.1` (class b).

## PostReleaseBasis check

- **Method:** read-only `git show --stat` on `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a`.
- **Files cited by the selected rows that these commits touched:** only `packages/daemon/src/app-owned-composition.ts`, changed by `da95ec194`.
- **The cited line:** `git blame` puts `:214` (registration of the Codex delegated adapter) in `95b3425195` (2026-09-12), which predates those commits.
- **Result:**
  - The reverse-notes revisit is confirmed: `PostReleaseBasis = NO` holds for every selected row.
  - The forward worker's assumed NO happens to be correct here.

## (ii) Systematic patterns

1. **AuthorityTier "highest tier restated" was misapplied to rows that restate SPEC.**
   - Under CONVENTIONS §2, SPEC is a GOVERNANCE_INVARIANT source, but the worker tagged such rows `PRD`.
   - Examples:
     - `CLM-003.2`, `CLM-003.3`, `CLM-005.1`, `CLM-009.5`, `CLM-009.9`, `CLM-009.11`, `CLM-018.4`;
     - class b: `CLM-004.2`, `CLM-018.1`.
   - Only `CLM-009.10`, which cites PRD alone, is correctly `PRD`.
   - Metadata only: no disposition changes.
2. **DirectionEvidence problems.**
   - *GOVERNING sources cited as DirectionEvidence*, breaking the CONTEXT-only rule:
     - decomposition v3.2 (`CLM-002`, `CLM-008`);
     - SPEC 10.2 (`CLM-003.2`);
     - the D-APP-89 ruling (`CLM-005.2`).
     - These belong in NormativeSource or LatestDecision.
   - *A mis-glossed CONTEXT citation.* The conformance-gap rows (`CLM-003.4`, `CLM-009.8/.10`, `CLM-011`, `CLM-012.1`) cite HANDOFF §3 "runtime-conformance-v2.ts removed deliberately".
     - That file was the native-supply/policy compiler check. It was not the engine-conformance evaluator, which is still retained in `contracts/src/harness/engine-conformance.ts`.
     - No CONTEXT record directs skipping K-ENGINE-2 for Codex. The gap is carried as the V3-01 Remaining item instead.
     - The dispositions and CODEX_SOLE_ENGINE still stand; only the direction citation is weak.
3. **The AUTHORITY_CONFLICT cluster and inconsistent splits.**
   - *The conflict itself is reasonable, but not forced.*
     - The worker's conflict pits unamended K-ENGINE-4 against amended SPEC 11 and CONTRACT K-EVENT-1. The worker did not cite K-EVENT-1, which also supersedes the eight-name set.
     - An equally tenable reading exists. Under D-APP-127, the `codex.*` HarnessEvent categories carry upstream names inside explicit metadata fields (`data.codex`, `method`, `params`), which SPEC 10.3 permits. On that reading there is no conflict.
     - This is the MR-11 question the worker raised in friction, so these 5 rows are CONTESTED rather than refuted.
   - *CLM-009.13 does not depend on the conflict.* The evaluator never checks canonical HarnessEvent fields for leakage under either reading, and INSP-03 shows it never did. The row is therefore REFUTED to PARTIALLY_IMPLEMENTED / PRE_V3_DRIFT.
   - *Split inconsistencies:*
     - CLM-003.1 marks the "Contract ownership / SDK APIs do not define public semantics" row ALIGNED, while the identical REQ-002 (CLM-009.2) is AUTHORITY_CONFLICT.
     - CLM-003.2 treats "optional interrupt" as stale, while CLM-005.1 and CLM-018.1 absorb the same wording as ALIGNED.
4. **Minor patterns:**
   - *CONTEXT_CLAIM rows:* checkable CONTEXT_CLAIM rows get STALE_SPECIFICATION (`CLM-002`, `CLM-006`, `CLM-017`, `CLM-023`). One similar row gets NOT_AUDITABLE (`CLM-010`, which contains a false "REF-006 reconciled" assertion). The convention needs a rule for this.
   - *Mixed causes:* rows with two causes carry one CauseTag (`CLM-016`, `CLM-018.4`, `CLM-009.10`).
   - *Line anchors:* they should be checked against the pinned basis. For `REGISTER-3`, L303 is correct at `d6f6cadb2`.
   - *MR-6 on REM-2:* for a gate that names a ruling, MR-6 does not say which source verifies it (`REM-2`).
   - *Missing test case:* `REM-2` VerificationEvidence names a test file without a case.

### Evidence integrity

- Every cited path and line range I opened exists at the frozen tree and says what the row claims. The single exception is the REGISTER-3 anchor interpretation.
- The recomputed reference hashes match the worker's figures.
- All cited test cases exist by name.
- The gate transcripts show both suites passing (App 2,285 passed + 4 skipped; Runtime 407 passed). The transcripts record counts only, not individual case names.

### Additional observation (not a row error)

- GOVERNING SPEC 10.3 (`docs/SPEC.md:681-684`) still states the D-APP-18 Claude key-aware default. This contradicts K-ENGINE-3 as amended.
- It is part of the known deferred corpus drift. It is relevant to CLM-021 and to any reader who treats SPEC 10.3 as current.

## (iii) Effort

- **Files opened:** about 30, mostly as greps and line ranges. They cover:
  - the SoW (in full), `_STATUS`, `_REFERENCES`, `Dependencies.csv`, `_DEPENDENCIES`, MEMORY, `_CONTEXT` and the Assessment;
  - SPEC §10–11 and the CONTRACT K-ENGINE/K-EVENT rows;
  - the D-APP-127 record, the register rows, and HANDOFF §1/§3;
  - the four runtime source files, the frontend route, `http.ts`, the facade, the manifest, the contract doc and the conformance test;
  - the gate transcripts;
  - git log/show/blame for 8 queries.
- **Context:** the ledger (65 rows, about 61 KB) was the largest input. Context was adequate but moderately tight. Around 60 selected items per shard is near the comfortable ceiling for one context.
