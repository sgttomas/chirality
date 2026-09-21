# DEL-03-01 — forward-pass notes (worker B, R0 calibration)

Source state: frozen tree at `00115c719`. Ledger: `DEL-03-01_claims.csv` (65 rows, sealed after validation).

## 1. Census

- **Indexed units:** 28, made up of 26 `CLM` and 2 `REM`. All are covered.
- **Split units:** 9 of 28 (32%). CLM-003 (4), CLM-004 (4), CLM-005 (2), CLM-009 (15, one row per REQ), CLM-012 (2), CLM-013 (2: warning plus AC-001), CLM-018 (4), CLM-019 (2: records plus VER-001), CLM-022 (3). Together they give 38 rows. The other 19 units have one row each.
- **Extra keys:** 8, made up of REGISTER-1..5 and STATE-1..3.

| ClaimType \ Disposition | ALIGNED | STALE_SPEC | PARTIAL | AUTH_CONFLICT | IMPL_DIFF | REM_MISMATCH | NOT_AUDITABLE | Total |
|---|---|---|---|---|---|---|---|---|
| REQUIREMENT | 12 | 5 | 7 | 5 | 1 | – | – | 30 |
| ACCEPTANCE | – | – | 2 | – | – | – | – | 2 |
| EXCLUSION | – | 1 | – | – | – | – | – | 1 |
| CONTEXT_CLAIM | 1 | 5 | 1 | 1 | – | – | 8 | 16 |
| STATE_ASSERTION | – | 9 | – | – | – | – | – | 9 |
| REMAINING_WORK | 1 | – | – | – | – | 1 | – | 2 |
| REGISTER_DEFECT | – | 5 | – | – | – | – | – | 5 |
| **Total** | 14 | 25 | 10 | 6 | 1 | 1 | 8 | 65 |

- **Confidence:** HIGH 20, MEDIUM 42, LOW 3.
- **PostReleaseBasis:** NO on every row. See §5.

## 2. Least-confident rows

- **`CLM-009.5` (REQ-005), IMPLEMENTED_DIFFERENTLY / UNRECORDED_JUDGMENT.**
  - *Finding:* `AgentEngineRunInput` now carries an in-band `signal?: AbortSignal`. REQ-005 and SPEC 10.2 say cancellation is out of band.
  - *Alternative:* ALIGNED. The required fields are present, the signal is additive, and `interrupt()` remains out of band.
- **`CLM-009.13` (REQ-013), AUTHORITY_CONFLICT.**
  - *Alternative:* PARTIALLY_IMPLEMENTED, if `codex.*` HarnessEvent types count as "explicit adapter metadata". On that reading the suite simply lacks a HarnessEvent-type leakage check, because it checks only UI event names and forbidden values.
- **`REM-2` (V3-01), REMAINING_STATE_MISMATCH / CARRIER_PROPAGATION, MechanicallyUnblocked YES.**
  - *Finding:* The gate is "socket API lands on the production path". At `00115c719` the App owns and launches the Runtime service (`frontend/electron/main.ts:860-865`, `runtime-service-host.ts`), and the Codex delegated adapter is registered (`daemon/src/app-owned-composition.ts:214`). The marker therefore looks stale.
  - *Alternative:* "production path" means a released/notarized App. The replatform RUN_LOG records notarization and the native checklist as owner acts still pending. On that reading the gate is unmet, MechanicallyUnblocked is NO and the row is ALIGNED.
  - Depends names DEP-03-01-005/008. Neither is PREREQUISITE.

## 3. Register-defect summary

- **REGISTER-1.** The `_DEPENDENCIES.md` mirror has three faults:
  - It says Declared Upstream/Downstream are "TBD".
  - It lists DEP-006 as ACTIVE PENDING, but the CSV has it RETIRED.
  - Its P45 block says ACTIVE 7 / PENDING 4. The CSV actually has 8 ACTIVE and 5 PENDING, because DEP-009 was added later.
- **REGISTER-2.** In `Dependencies.csv`, rows 001–008 cite `Datasheet.md`, `Specification.md`, `Procedure.md` and `Guidance.md`. None of these exist; their content was consolidated into `ScopeOfWork.md`.
- **REGISTER-3.** DEP-03-01-009 still targets "Root-owned runtime contracts API v2 / event schema v2". D-APP-127 revised V3-01 to the retained socket API, and the contracts now live in `projects/chirality-runtime`. V3-01 also cites decomposition line L303, but the row is at line 317 in the frozen file.
- **REGISTER-4.** `_REFERENCES.md` says MATCH for REF-002, REF-003 and REF-006, but the recomputed hashes of `docs/CONTRACT.md`, `docs/SPEC.md` and `docs/PRD.md` differ. The SoW's REF-007 (`agents/AGENT_SOFTWARE_DECOMP.md`) also differs from `_REFERENCES.md` REF-007 (`workflows/software-decomp/WORKFLOW.md`).
- **REGISTER-5.** Two rows are still PENDING on outdated grounds:
  - DEP-003 waits on the DEL-04-01 SDK probe, a premise retired under Codex sole engine.
  - DEP-008 waits on Section 9 linkage, but `section9.runtime_engine_contract` already exists in `frontend/scripts/harness-section9-manifest.json`.

## 4. Direction and cause

- **CODEX_SOLE_ENGINE (26 rows)** is the main cause.
  - *Direction records:* `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md`:
    - §1: Codex is the only engine; multi-engine abstractions are retired.
    - §3 "Event representation (clarified)": the eight-name set is not retained and upstream method names are preserved.
    - §3: `runtime-conformance-v2.ts` was removed deliberately; the legacy `src/lib/harness` managers are unreachable.
  - *Governing basis:* D-APP-127, which retires the closed event vocabulary, plus SPEC §11 as amended.
  - *Substantive residual:* K-ENGINE-2 still binds. Codex is the production default, but no `runEngineConformance` run exists over the Codex delegated adapter in either test tree. This is the V3-01 work (CLM-003.4, CLM-009.8/.10, AC-001, VER-001).
- **AUTHORITY_CONFLICT cluster (6 rows):** CLM-004.1, CLM-009.2/.7/.13, CLM-018.2 and CLM-022.2.
  - Canonical `HarnessEvent` types now include `codex.notification`, `codex.steer`, `codex.request` and `codex.request.resolved` (`contracts/src/harness/event-schema.ts:44-47`).
  - CONTRACT K-ENGINE-1/4 (unamended) forbids provider-shaped canonical events except as adapter metadata.
  - SPEC §11 (amended under D-GOV-43) requires upstream names to be preserved.
  - No ruling says whether `codex.*` types are adapter metadata. These rows are marked R4.
- **DOC_HYGIENE (9 rows):** stale reference hashes, dependency mirrors, a `blocked-on` line naming ruled decisions (D-APP-47/48), and a CT-001 "resolved" claim.
- **RUNTIME_EXTRACTION (2 rows):**
  - The SoW scope and identification still describe the App defining the port.
  - Decomposition v3.2 line 317 (GOVERNING) and `_CONTEXT.md` describe App-client conformance against runtime-owned contracts.
- **FACADE_DEPRECATION (2 rows):**
  - The accepted-placement text is stale. The `frontend/src/lib/harness/agent-engine-port.ts` shim no longer exists; the package file is a deprecated re-export (D-APP-47/89).
  - `runtime_engine_contract.md` still cites the moved paths.
- **CARRIER_PROPAGATION (2 rows):** the V3-01 gate marker, and the DEP-009 row left un-revised by the D-APP-127 application.
- **PRE_V3_DRIFT (1 row) and UNRECORDED_JUDGMENT (1 row):** the port shape changes (required `interrupt`, `descriptor`, `preflight`, in-band `signal`).
- **Cross-deliverable note:** the runtime contract doc is also cited by DEL-01-02 (reliance register) and by DEL-09-02 (Section 9).

## 5. Method friction (R0 input)

- **PostReleaseBasis.** Workers cannot run git, so they cannot tell whether cited bytes came from the four post-v3.0.1 commits. I defaulted to NO.
  - *Proposal:* the manager supplies a list of files touched by those commits, or the column becomes `UNKNOWN`-capable.
- **Mixed-cause split rows** (CLM-016, CLM-018.4) must carry one CauseTag.
  - *Proposal:* allow a secondary cause in Notes, as I did, or split further.
- **"Judged against the GOVERNING map" versus AUTHORITY_CONFLICT.** It is unclear when two GOVERNING sources disagree because one was amended (SPEC §11) and the other was not (CONTRACT K-ENGINE-4).
  - *Proposal:* state whether the later-amended governing text wins under MR-11 or the row is AUTHORITY_CONFLICT. I chose AUTHORITY_CONFLICT.
- **MechanicallyUnblocked "at the source the gate itself names".** Gates such as V3-01's name a ruling (D-GOV-43) as context, not a verification surface.
  - *Proposal:* allow App code at the frozen SHA as the verification surface for code-landing gates.
- **CONTEXT_CLAIM versus STALE_SPECIFICATION.** Method or guidance sections with checkable but stale content (CLM-017, CLM-023) fit poorly: NOT_AUDITABLE understates them.
  - *Proposal:* confirm that CONTEXT_CLAIM rows may take STALE_SPECIFICATION.
- **AssessmentEvidence substring check.** Free text after the token must avoid the other tokens' phrases.

## 6. Effort

- **Files read:** about 40, most of them as line ranges or greps. They cover:
  - 9 deliverable files;
  - the conventions, basis, gate transcripts and validator;
  - SPEC §10–11 and CONTRACT K-ENGINE;
  - D-APP-127 and the register rows;
  - the replatform HANDOFF and RUN_LOG excerpts;
  - about 15 code and test files.
- **Context budget:** comfortable, not tight. At this size (a 420-line SoW, 28 units) one worker per deliverable is sufficient.
