# DEL-09-01 concordance notes (R2 Wave-4)

Deliverable: DEL-09-01 Section 8 Harness Validation Preservation (PKG-09).
Source state: frontend/ at `fac46e33f`, byte-identical through HEAD `6f7c06814` (this
worktree). Workflow files (repo-root and project-local `.github/`) are not under
frontend/; inspected at HEAD `6f7c06814` and bound indirectly through the passing
frontend test `harness-premerge-workflow.test.ts` at `fac46e33f`.

## Census

Total rows: 17 (10 REQUIREMENT, 3 EXCLUSION, 1 IMPLEMENTED_UNMAPPED, 1 REMAINING_WORK,
2 REGISTER_DEFECT).

Disposition counts:
- ALIGNED 11 (REQ-001, REQ-002, REQ-004, REQ-006, REQ-008, REQ-009, EXC-001, EXC-002, EXC-003, UNMAPPED-1, REMAINING-1)
- STALE_VERIFICATION 2 (REQ-003, REQ-005)
- IMPLEMENTED_DIFFERENTLY 1 (REQ-007)
- STALE_SPECIFICATION 1 (REQ-010)
- REMAINING_STATE_MISMATCH 2 (REGISTER-1, REGISTER-2)

AssessmentEvidence: STILL CURRENT 7, OVERTAKEN 2 (REQ-007, REQ-010), NOT APPLICABLE 8.

Fan-in revision note: two Wave-4 verifier items were independently re-verified and ACCEPTED
by this agent's own judgment (not treated as a ruling): (1) UNMAPPED-1 revised
IMPLEMENTED_DIFFERENTLY -> ALIGNED after direct confirmation that sibling DEL-09-02-RQ-012
(DEL-09-02 Specification.md line 28; DEL-09-02_claims.csv row RQ-012) claims the same wrapper
lines 165-198 as ALIGNED requirement coverage — an accepted corpus mapping, so a divergence
disposition misfit plan §7; the behavioral finding and cross-deliverable handle are unchanged.
(2) REGISTER-2 added for the stale _DEPENDENCIES.md PRD-hash warning (see below).

## Key findings

1. **CI workflow migrated and reshaped (REQ-007, REGISTER-1).** The kit (Spec REQ-006/007,
   Datasheet CI workflow surface, Procedure) describes `.github/workflows/harness-premerge.yml`
   as a workflow that directly runs `npm run harness:validate:premerge`, polls
   `/api/harness/session/list?projectRoot=/tmp`, uses `secrets.ANTHROPIC_API_KEY`, and uploads
   `harness-section8-summary`. That description matches the **project-local**
   `projects/chirality-app-dev/.github/workflows/harness-premerge.yml`, which dates only to the
   initial-migration commit (`7bee9ae41`) and is **not an executed GitHub Actions workflow**
   (Actions only runs repo-root `.github/workflows`). The **live** CI is the repo-root
   `.github/workflows/harness-premerge.yml` (ORN-01 reshape, commits `b25ed61d6` /
   `48f622c93` / `b001bd247`): provider `stub` env, no provider secret, runs typecheck + full
   Vitest + instruction-root integrity + `npm run validate:release-quality` (which invokes the
   premerge wrapper at `validate-release-quality-evidence.mjs` line 379), verifies section8
   summary status==pass, and uploads it inside `harness-validation-summaries`. CI ownership now
   sits with **DEL-09-05** (Spec REQ-09-05-004; ADQ-14). Hence REQ-007 = IMPLEMENTED_DIFFERENTLY
   and DEP-09-01-010's `harness-section8-summary` target = REGISTER_DEFECT.

2. **PRD hash mismatch resolved (REQ-010) — STALE_SPECIFICATION.** The kit pervasively describes
   `docs/PRD.md` as HASH_MISMATCH (expected `86cb6fb9...`, observed `fb1c73f7...`), warning-only.
   Current `_REFERENCES.md` REF-006 records MATCH (expected=actual `ac35fba40...`) and live
   `shasum -a 256 docs/PRD.md` reproduces `ac35fba40...`. Reconciled under D-APP-35 (refresh
   accepted hash) and D-APP-38 (versioned corpus, subsumes D-APP-35). Same pattern as the R0
   exemplar DEL-02-01 ACC-001.

3. **Section 9 orchestration inside the premerge wrapper (UNMAPPED-1) — ALIGNED with handle.**
   `validate-harness-premerge.mjs` (a DEL-09-01 construction surface) also runs
   `validate-harness-section9.mjs` report-only (lines 82-102, 165-198), with the exit code driven
   by Section 8 only (line 200). Sibling DEL-09-02-RQ-012 claims exactly this behavior as ALIGNED
   requirement coverage (Section 8 preserved while Section 9 IDs land), and Guidance line 15 +
   decomposition v3.2 assign Section 9 to DEL-09-02 — an accepted corpus-wide mapping, so the row
   is ALIGNED with the DEL-09-02-RQ-012 cross-deliverable handle (revised at fan-in from
   IMPLEMENTED_DIFFERENTLY; disposition hygiene only, behavioral finding unchanged).

4. **Real test-absence search performed (REQ-003, REQ-005).** Grep of `src/**/*.test.*` for
   `RUNTIME_SURFACE_MISSING`, `validate-harness-premerge`, `validate-harness-section8`,
   `api_chat_reachability`, `LEGACY_REMOVED_TEST_ID`, `boot_error_taxonomy` and the
   VERIFICATION_INDEX returned only `harness-premerge-workflow.test.ts` (which asserts the
   repo-root workflow YAML, not wrapper behavior). No deterministic test exercises the wrapper's
   missing-script fail path (REQ-003) or legacy-ID rejection (REQ-005); both are implemented but
   verified by inspection only. Spec/Guidance already request these fixtures.

## Least-confident rows (self-flagged; alternative reading that would flip them)

- **REQ-003 / REQ-005 (STALE_VERIFICATION, MEDIUM).** Implementation is present and correct by
  inspection; I called them STALE_VERIFICATION because the Specification Verification column
  explicitly asks for a deterministic missing-ID / legacy-ID fixture test that does not exist.
  Alternative reading → **ALIGNED**: the Spec's Verification clause offers an OR-branch ("or
  wrapper execution proves readable script"), and INSP-03 rated both PASS on implementation; if
  inspection + the readable-path CI execution is accepted as sufficient, the missing fixture is
  merely a recommended enhancement (RemainingWork), not a disposition-changing gap.

- **REQ-007 (IMPLEMENTED_DIFFERENTLY, MEDIUM).** Alternative reading → **STALE_SPECIFICATION**:
  if one treats the requirement's substance (CI runs the wrapper after readiness and uploads the
  stable summary) as fully satisfied by the repo-root workflow and views only the kit's citation
  as wrong, the row is a pure documentation-staleness repair. I chose IMPLEMENTED_DIFFERENTLY
  because the live mechanism differs materially (indirect invocation via `validate:release-quality`,
  provider-stub env, different upload bundle name, added gates) and ownership moved to DEL-09-05.
  A further alternative is **AUTHORITY_CONFLICT** only if DEL-09-01 REQ-007 and DEL-09-05
  REQ-09-05-004 were treated as competing normative owners of the same CI surface — I did not,
  because the decomposition assigns the CI workflow to DEL-09-05 (no unresolved precedence).

- **UNMAPPED-1 (ALIGNED, MEDIUM — revised at fan-in).** Alternative readings: (a) my original
  **IMPLEMENTED_DIFFERENTLY**, if one reads "mapped" strictly as mapped within the owning
  deliverable's own kit rather than corpus-wide — rejected because the Wave-4 rule makes a sibling
  assignment (DEL-09-02-RQ-012) an accepted mapping; (b) **fold into EXC-002 and emit no row** —
  rejected because the orchestration block is material live behavior on DEL-09-01's own
  construction surface and deserves the explicit handle. Row kept as IMPLEMENTED_UNMAPPED
  ClaimType (unmapped within DEL-09-01) with ALIGNED disposition.

- **REGISTER-2 (REMAINING_STATE_MISMATCH, MEDIUM — added at fan-in).** Alternative reading →
  **no defect row**: the SOURCE_HASH_MISMATCH warning sits inside a dated section ("Run Notes:
  2026-05-20 Dependency Extract"), so it could be read as a historical run record rather than a
  current-truth claim, analogous to preserved `## History` lines. I ledgered it because the
  sentence is present-tense about `_REFERENCES.md` ("reports ... hash mismatch"), now contradicts
  that file's MATCH state, carries no superseding annotation, and MR-5 names `_DEPENDENCIES.md`
  internal inconsistency/metadata lag explicitly; DEL-09-02/04 ledgered the same class, and
  class-level harmonization across PKG-09 registers is an R3 item.

- **REQ-006 (ALIGNED, MEDIUM).** Wrapper code creates/updates the stable summary; but no fresh
  `frontend/artifacts/harness/section8/latest/summary.json` exists in the checkout and the
  Datasheet-cited provenance file (`provenance/build-artifacts/frontend__artifacts__harness__section8__latest__summary.json`)
  is also absent at HEAD. Alternative reading → **STALE_VERIFICATION** if the absent provenance
  citation is treated as a broken verification pointer rather than a freshness gap. I followed
  INSP-03 (freshness gap, not missing code).

## Register-defect summary

- REGISTER-1 (REMAINING_STATE_MISMATCH): DEP-09-01-010 names CI upload artifact
  `harness-section8-summary` from `.github/workflows/harness-premerge.yml`; the executed repo-root
  CI uploads `harness-validation-summaries`. The named artifact survives only in the non-executing
  project-local workflow. Metadata lag.
- REGISTER-2 (REMAINING_STATE_MISMATCH): `_DEPENDENCIES.md` line 61 ([WARNING]
  SOURCE_HASH_MISMATCH, repeated in Run History line 66) still asserts present-tense that
  `_REFERENCES.md` reports a `docs/PRD.md` hash mismatch; `_REFERENCES.md` REF-006 now records
  MATCH (`ac35fba40...`, reproduced by live shasum). Unannotated internal inconsistency within
  the register set; same D-APP-35/38 repair family as REQ-010.
- Not flagged as defects: DEP-09-01-001..010 all carry `SatisfactionStatus=TBD` — this is the
  disclosed open-closure state (DepClosure baseline, INSP-03 Dependency Closure Note), not an
  inconsistency. `_DEPENDENCIES.md` Declared Upstream/Downstream are bare TBD by design
  (docs/SPEC.md §5.2 human-owned sections) — no REGISTER_DEFECT per the Wave-4 rule; mentioned here
  only for completeness.

## Method notes / deviations

- No test suites executed, no dependencies installed, no mutating git. Behavioral verification uses
  `GATE-TRANSCRIPT(W1@fac46e33f)` + named test; non-behavioral rows use the MR-10 vocabulary
  (`RUN-INSPECTION@6f7c06814`, `RULING-RECORD(D-APP-35/38)`, `DOC-BASIS`). Workflow files sit outside
  frontend/ so I cite `RUN-INSPECTION@6f7c06814` for their YAML content, anchored to `fac46e33f`
  through the passing frontend workflow test.
- MR-7: REQ-010 and REGISTER-2 cite `D-APP-35; D-APP-38` (governing the PRD hash refresh); REQ-007
  and REGISTER-1 cite `D-APP-53 (context)` (the ORN queue that reshaped the workflow); the rest
  `NONE_FOUND`.
- No secret/key values copied into any cell (the live repo-root workflow deliberately omits
  `secrets.ANTHROPIC_API_KEY`; the legacy project-local one references the secret name only, which
  I describe without reproducing any value).
- No AUTHORITY_CONFLICT, DEFERRED_AGENT_WORKFLOW, or UNKNOWN rows arose.
