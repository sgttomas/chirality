# DEL-03-01 — R0 calibration notes (worker A, forward pass)

Source state: frozen tree at `00115c719`. Ledger: `DEL-03-01_claims.csv` (60 rows).

## 1. Census

Indexed units: 28 (26 CLM + 2 REM). All covered.

Split rate: 5 of 28 units were split (CLM-003 into 4, CLM-004 into 6, CLM-005 into 3,
CLM-009 into 15, CLM-012 and CLM-013 into 2 each). That gives 50 rows from indexed units,
plus 6 run-local rows (REGISTER-1..5, STATE-1).

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 30 |
| CONTEXT_CLAIM | 12 |
| STATE_ASSERTION | 7 |
| REGISTER_DEFECT | 5 |
| ACCEPTANCE | 4 |
| REMAINING_WORK | 2 |

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 24 |
| ALIGNED | 14 |
| PARTIALLY_IMPLEMENTED | 11 |
| NOT_AUDITABLE | 7 |
| DOCUMENTED_UNIMPLEMENTED | 2 |
| IMPLEMENTED_DIFFERENTLY | 1 |
| REMAINING_STATE_MISMATCH | 1 |

Confidence: 25 HIGH, 33 MEDIUM, 2 LOW.

## 2. Least-confident rows

- **`CLM-009.8` (REQ-008, conformance before production default): LOW.**
  - My reading: `DOCUMENTED_UNIMPLEMENTED`. Codex is the registered production engine
    (`app-owned-composition.ts:214`), but no `runEngineConformance` run exists against the
    delegated Codex adapter. The A2 handoff removed `runtime-conformance-v2.ts` on purpose.
    `HumanDecisionNeeded = R4`: K-ENGINE-2 requires conformance *before* a production
    default, and v3.0.1 shipped without it.
  - Alternative reading: `PARTIALLY_IMPLEMENTED`. This holds if the S-1..S-8 checks named
    in K-ENGINE-3, plus the `native-event-adapter` and `codex-attachment-adapter` Runtime
    tests, count as the Codex-era conformance.
- **`CLM-009.7` (REQ-007, SDK names only as adapter metadata): LOW.**
  - My reading: `PARTIALLY_IMPLEMENTED`, because of the provider-named `claudeSessionId` on
    the public `UIEvent` `session:init` (`contracts/src/harness/types.ts:282`).
  - Alternative reading: `ALIGNED`, if an optional compatibility field counts as explicit
    adapter metadata. INSP-03 accepted it.
- **`REM-2` (MEDIUM, borderline).**
  - `MechanicallyUnblocked = YES`, because the A2 socket API is on the production path in
    code: `runtime-service-host.ts`, the turn route, then `getDaemonHarnessPort`.
  - The gate status comes from code plus a CONTEXT run log, not from an App status surface.
    If the verifier requires an App status surface, this becomes `UNKNOWN`.
- **`CLM-004.2` (route compatibility): ALIGNED, MEDIUM.** I did not diff the route request
  shape across the A2 transition.

## 3. Register-defect summary

- **REGISTER-1.** The `_DEPENDENCIES.md` mirror disagrees with `Dependencies.csv`.
  - DEP-006 shows as ACTIVE/PENDING in the table but is RETIRED in the CSV.
  - The P45 block counts are stale.
  - DEP-008 (Section 9 linkage) is still PENDING, although
    `section9.runtime_engine_contract` exists and is linked to `engine-conformance.test.ts`.
- **REGISTER-2.** `EvidenceFile`/`SourceRef` point to `Datasheet.md`, `Specification.md`,
  `Procedure.md` and `Guidance.md`, none of which exist. DEP-005's `TargetLocation` names a
  DEL-03-03 `Specification.md` that is also absent.
- **REGISTER-3.** DEP-003 is an ACTIVE PREREQUISITE on the DEL-04-01 Claude SDK probe. It is
  obsolete under Codex as sole engine.
- **REGISTER-4.** DEP-009 still targets "API v2 / event schema v2". V3-01 was revised to the
  repaired socket API on 2026-09-12, but this row was not.
- **REGISTER-5.** `_REFERENCES.md` records MATCH for CONTRACT, SPEC and PRD, but their
  SHA-256 at `00115c719` differ (`57411f8d…`, `8b0d805b…`, `17ca3f3c…`). The D-APP-38
  corpus bump has not reached this deliverable.
- **STATE-1.** `_STATUS.md` `blocked-on` lists D-APP-47 and D-APP-48, both RULED. I did not
  check D-T0-09 or D-30.

## 4. Direction and cause

Main CauseTags: CODEX_SOLE_ENGINE (12), DOC_HYGIENE (10), A2_TOPOLOGY (5), PRE_V3_DRIFT (5),
RUNTIME_EXTRACTION (3), CARRIER_PROPAGATION (2), FACADE_DEPRECATION (1),
UNRECORDED_JUDGMENT (1). No OTHER tokens.

CONTEXT and GOVERNING records used:

- **D-APP-127 ruling application** (GOVERNING). It retires the closed event vocabulary.
  - It states that the DEL-03-01 architecture-bound clauses were revised.
  - In fact only the `_STATUS` V3-01 item was revised. The SoW body (REQ-011, CLM-003/004
    SSE rows, CLM-021 "Claude Agent SDK preferred substrate") was not.
  - This partial application is the common root of most stale rows.
- **`AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md` L126-128** (CONTEXT). The
  deliberate removal of the core conformance check explains why the Codex adapter is not a
  conformance subject.
- **`…/RUN_LOG.md`** (CONTEXT). The 2026-09-12 signed build is the basis for REM-2's gate
  appearing satisfied.
- **Decomposition v3.2 L303.** Its App-client verification scope underlies the CLM-008 and
  CLM-002 staleness.

The only `UNRECORDED_JUDGMENT` is `CLM-009.5`. `AgentEngineRunInput` carries
`signal?: AbortSignal` in band, while both the SoW and GOVERNING SPEC 10.2 say cancellation
is out of band.

Cross-deliverable observations:

- GOVERNING SPEC §10.3 still names the Claude key-aware default, against CONTRACT K-ENGINE-3
  and D-GOV-43. Per MR-11 the ruling stands, so I did not raise an AUTHORITY_CONFLICT.
- The App's `frontend/docs/harness/runtime_engine_contract.md` contradicts itself and
  SPEC 10.2:
  - it calls `AgentEnginePort` "historical design naming";
  - it points to the deprecated facade;
  - it names a nonexistent `frontend/src/lib/harness/engine-conformance.ts`.
- The REM-2 text says the "multi-engine port abstractions are retired", but the
  `engine-claude` and `engine-pi-omlx` packages and the descriptor/registry still exist in
  Runtime.

## 5. Method friction

- **PostReleaseBasis** could not be determined without git, which is forbidden to children.
  I set every row to `NO`.
  - Proposal: the manager should supply the file list touched by the four post-release
    commits in the brief.
- **AssessmentEvidence.** When the INSP-03 conclusion still holds but my disposition differs
  on judgment rather than recency (for example REQ-007), the three tokens cannot express
  "current but disputed". I used STILL CURRENT with a note.
- **ClaimType for guidance blocks** (Purpose, Considerations, Examples) that contain stale
  factual assertions: CONTEXT_CLAIM + NOT_AUDITABLE loses the staleness. I used
  CONTEXT_CLAIM + STALE_SPECIFICATION where the text asserts a now-false fact (CLM-023,
  CLM-025) and STATE_ASSERTION for CLM-021.
  - Proposal: allow STALE_SPECIFICATION on CONTEXT_CLAIM explicitly.
- **MechanicallyUnblocked "verified at the source the gate names".** For a gate phrased as
  "X lands on the production path", the source is code, but MR-6 says gate status for
  Runtime-owned work comes only from App surfaces.
  - Proposal: define whether App code counts as an App surface.
- **Duplication.** The SoW restates the same fact in Datasheet, Specification, Procedure and
  Guidance (for example the SSE names in CLM-003.3, CLM-004.3, CLM-009.11 and CLM-017).
  Splitting multiplies identical dispositions.
  - Proposal: allow a `SeeAlso` convention, or count duplicates once in the census.

## 6. Effort

- About 45 files or file ranges read or grepped:
  - the 8 deliverable files plus the Evidence header;
  - the contracts package (port, conformance, types excerpts);
  - frontend route, facade and tests;
  - Runtime delegated adapter, composition and test names;
  - SPEC §10-11 and CONTRACT K-ENGINE;
  - the D-APP-127 excerpt;
  - A2 HANDOFF/RUN_LOG excerpts;
  - the Section 9 manifest.
- Context was moderate, not tight. The `_SEMANTIC*` files were not read.
- A 28-unit, 420-line SoW fits comfortably in one worker.
