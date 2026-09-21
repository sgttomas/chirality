# DEL-02-05 — R0 calibration notes (forward pass, unit F-02)

Basis: frozen tree at `00115c719`. Ledger: `DEL-02-05_claims.csv` (66 rows, `#END`).
Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

**Rows by ClaimType:**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 29 |
| CONTEXT_CLAIM | 16 |
| ACCEPTANCE | 10 |
| STATE_ASSERTION | 6 |
| REGISTER_DEFECT | 3 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |

**Rows by Disposition:**

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 27 |
| ALIGNED | 16 |
| NOT_AUDITABLE | 10 |
| IMPLEMENTED_DIFFERENTLY | 9 |
| PARTIALLY_IMPLEMENTED | 3 |
| REMAINING_STATE_MISMATCH | 1 |

**Split rate:** 8 of 32 indexed units were split: SEC-1 into 5, SEC-2 into 5, CLM-009 into 2,
CLM-010 into 10 (R01–R10), CLM-013 into 8 (the TBD list, REQ-001–005, AC-001, AC-002), CLM-017
into 2, CLM-020 into 3 (the binding table, VER-001, VER-002) and CLM-023 into 2. That is 25% of
units, giving 61 rows from indexed units. There are also 5 run-local rows: REGISTER-1..3 and
STATE-1..2.

## 2. Least-confident rows

- **SEC-1.4, SEC-2.5, CLM-013.5 (role entry and posture labels).** Role entry exists
  (`frontend/src/components/shell/persona-picker.tsx`). The verbatim labels
  `role not mechanically enforced` and `Opt-in Preview` live only in the consent module, and
  the hosted production shell does not render it. Scored as PARTIALLY_IMPLEMENTED /
  UNRECORDED_JUDGMENT.
  - *Alternative reading:* the labels retired with the consent module under D-APP-127
    (STALE_SPECIFICATION / A2_TOPOLOGY).
  - *Against the alternative:* CONTRACT K-ROLE-2 is still governing and still requires the
    label. D-APP-127 names only the port, per-root consent and the postures.
  - I could not establish whether G-ROLE fails.
- **SEC-2.2 (account row shows only local model status, Q7).** In hosted mode the row shows
  Codex sign-in and readiness (`account-row.tsx:57-68`), not local model status. Scored as
  IMPLEMENTED_DIFFERENTLY / CODEX_SOLE_ENGINE.
  - *Alternative reading:* STALE_SPECIFICATION under D-APP-127. The account row now acts on
    Codex login, so sign-in state is the intended content, and a sign-in summary is arguably
    not an "OpenAI status indicator".
- **Medium-confidence judgment to note: REM-1 (V3-03).** The Codex login flow appears to have
  landed in source on the production path: `hosted-bootstrap-controller` is mounted from
  `shell-frame.tsx`, and Runtime `codex-login.ts` calls `account/login/start`, `cancel` and
  `logout`, with the Runtime test green. Only S-8 owner evidence is outstanding, so I used
  REMAINING_STATE_MISMATCH.
  - *Alternative reading:* the gate means "production path including the signed build", so
    the item is correctly gated. The Remaining text would then be stale only in its
    write-locus and checks lines (STATE-2).

## 3. Register-defect summary

- **REGISTER-1.** `Dependencies.csv` DEP-02-05-008 (HostedEngineConsentPort), -009 (Root/App
  consent contract with G3/G-CSP/G4) and -013 (Root DEL-02-09) remain ACTIVE/PENDING although
  D-APP-127 retired or superseded each target.
- **REGISTER-2.** `_REFERENCES.md` assigns RefIDs REF-009 and REF-010 twice: once to the
  software-decomp resources and once to the SCA-APP-010 files.
- **REGISTER-3.** OUT-002 cites decomposition line 297 at `d6f6cadb2`, but the front matter pins
  `dbd812a52`, where the row is L311. This is an instance of the known decomposition_basis pin
  defect.
- **Related state rows:**
  - STATE-1: `_CONTEXT.md` still carries the consent-port, per-folder consent and posture
    scope.
  - STATE-2: the `_STATUS.md` V3-03 write locus still names the consent-port adapter, and its
    checks still require the APP-HOLD-1 preflight and the A1 re-stage declaration. D-APP-127
    superseded both.
- **Observed and not a defect:** the 2026-06-20 assessment's "DEL-02-06 comment" gap is fixed.
  The key-storage files no longer carry it.

## 4. Direction and cause

- **A2_TOPOLOGY (13 rows).** This is the dominant cause. D-APP-127 (GOVERNING; the application
  of D-GOV-43) retired HostedEngineConsentPort, per-root consent and homes, the three
  command-network postures, identity binding and the HOST-P1 / Root DEL-02-09 / G3 / G-CSP / G4
  live-login gates.
  - The D-APP-127 tranche revised only DEL-02-05 `_STATUS.md`. The CONTEXT record is
    `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md:46`.
  - The SoW SCA-APP-010 Current Contract, REQ-001/003/005, AC-002, VER-002, `_CONTEXT.md` and
    `Dependencies.csv` are therefore stale against a ruling. Repair is transcription, with
    HumanDecisionNeeded set to D-APP-127.
- **CODEX_SOLE_ENGINE (8 rows).** The API-key panel, its typed storage states and the
  Anthropic precedence resolver are implemented and tested at component and IPC level. The
  production Settings omits them for hosted Codex (`settings-view.tsx:31-35`; `hosted` is always
  supplied by `shell-frame.tsx`; covered by the test in `settings-view-codex.test.tsx`).
  - CONTEXT: `execution/_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/R14_FUNCTIONAL_FINDINGS.md:28`.
  - PRD FR-030 and 7.7 still carry the Anthropic requirement, so these rows are R4 rather than
    a ruled repair.
- **PRE_V3_DRIFT (5 rows).** The original TBD wording (component paths, evidence bindings,
  dependency extraction) was overtaken by June–August implementation and assessment.
- **CARRIER_PROPAGATION (4 rows).** Partial propagation of D-APP-108/109/127 into SoW seating,
  `_CONTEXT.md` and the V3-03 lines.
- **FACADE_DEPRECATION (1 row).** R10 names `@chirality/harness-contract`; code imports
  `@chirality/runtime-contracts/types`. The direction is the D118 obsolete-facade retirement in
  `APP_V3_INTEGRATION_2026-09-06/OWNER_DECISION_SLATE_v2.md:28`.
- **Cross-deliverable observation.** DEL-04-05-V3-02 (a REM-1 Depends item) is still gated on
  the retired Root/App consent contract and K-NET-1 postures. It looks unpropagated from
  D-APP-127.

## 5. Method friction

- **PostReleaseBasis cannot be determined.** Attributing evidence to `da95ec194` and the other
  post-v3.0.1 commits needs git history, and the brief forbids git. All rows say `NO`.
  - *Proposed revision:* the manager supplies a per-file commit-attribution list for the four
    commits, or the column accepts `UNDETERMINED`.
- **DirectionEvidence is defined as a CONTEXT record, but the explaining source is often a
  GOVERNING ruling (D-APP-127).** I cited the CONTEXT tranche return and put the ruling in
  LatestDecision.
  - *Proposed revision:* allow a GOVERNING citation in DirectionEvidence when a ruling itself
    explains the divergence.
- **Code that exists but is unreachable in the production shell does not fit the vocabulary
  cleanly** (IMPLEMENTED_DIFFERENTLY vs PARTIALLY_IMPLEMENTED). I used IMPLEMENTED_DIFFERENTLY.
  - *Proposed revision:* add a note convention `UNMOUNTED_IN_PRODUCTION` so these rows can be
    aggregated.
- **REQ/AC/VER bullets are not indexed units.** They sit under CLM-013 and CLM-020 by line
  range, so I had to split them.
  - *Proposed revision:* the indexer should emit REQ-/AC-/VER- bullets as their own units.
- **VER-001 (document-verification method) has no code surface.** I recorded it as
  NOT_AUDITABLE under ClaimType CONTEXT_CLAIM even though it is a verification statement.

## 6. Effort

- **Files read:** about 40 across the deliverable kit (8 files), the D-APP-127 ruling, CONTRACT
  and PRD greps, and about 25 frontend and runtime source and test files, mostly by grep and
  line range.
- **Context budget:** moderately tight but not constraining. The 35 KB SoW plus the 18 KB
  `_STATUS.md` were the largest reads. `_SEMANTIC*.md` and `_run_records/` were not read.
- **Oversize threshold:** a deliverable of this size (484-line SoW, 32 units) is near the
  comfortable upper limit for one worker when both code roots are needed.
