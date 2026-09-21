# DEL-09-01 — forward-pass notes (R2, PKG-09 wave 5)

Ledger: `DEL-09-01_claims.csv`, 45 rows, sealed. SHA-256
`f91122a47b0e5ef98e8b96be7c1467eecc9a39f7973abfd1664c89af897ef56d`. Validator: `RESULT PASS errors=0 warnings=0`.
Basis: frozen tree at `00115c719`. The rule notice for Addendum 9 (R4-Q6) arrived **before sealing**. No row turns on R4-Q6: no row concerns the API-key UI, the "Full access" option or the `~/.codex` link. The in-root CI workflow's `ANTHROPIC_API_KEY` env is a CI detail, not the UI.

## 1. Census

By ClaimType: REQUIREMENT 17 · ACCEPTANCE 10 · CONTEXT_CLAIM 9 · STATE_ASSERTION 5 · REGISTER_DEFECT 2 ·
EXCLUSION 1 · REMAINING_WORK 1.

By Disposition (all rows, SEE rows included): STALE_SPECIFICATION 17 · ALIGNED 14 · PARTIALLY_IMPLEMENTED 6 ·
NOT_AUDITABLE 5 · REMAINING_STATE_MISMATCH 2 · STALE_VERIFICATION 1.

SEE rows, counted separately (MR-4): 8. CLM-001, CLM-007, CLM-009.10, CLM-014, CLM-020, CLM-022 and CLM-026 point to `REGISTER-1`, and CLM-018.6 points to `CLM-003`. All 8 are STALE_SPECIFICATION. Without them, STALE_SPECIFICATION is 9.

Split rate: 28 indexed units (27 CLM + REM-1) produced 42 rows, plus 3 run-local rows (REGISTER-1, REGISTER-2, STATE-1).
Two units were split:
- CLM-009, the Requirements table, into `.1`–`.10`, one row per DEL-09-01-REQ-001..010;
- CLM-018, the six-row Verification table, into `.1`–`.6`.

That gives 2 of 28 units split (7%). SubItems: CLM-013 carries AC-001 and CLM-019 carries VER-001, each in one row, named in Notes.

HumanDecisionNeeded: NO 44 · R4-Q1 1 (CLM-009.8). Confidence: HIGH 31 · MEDIUM 14 · LOW 0.
No errata file exists yet.

## 2. Least-confident rows (MEDIUM; alternative readings)

- **CLM-009.8 (REQ-008), PARTIALLY_IMPLEMENTED + R4-Q1.** The validator reaches LIVE routes. The permission check "under current validation markers" depends on `UNAPPROVED_*_TEST` markers, and only the LEGACY_ONLY Agent SDK managers honour them. The live composition is Codex-only, with no stub engine. *Alternative:* read REQ-008 as a module contract ("the script covers eight behaviours"), which gives ALIGNED (recorded as `ALSO_MODULE:ALIGNED`). Under that reading, R4-Q1 would still be cited by rule 3 only if the marker sub-claim counts. The R4-Q1 citation is judgement-sensitive: LIVE code meets most of the claim.
- **CLM-009.7 (REQ-007), PARTIALLY_IMPLEMENTED.** This is judged on the in-root copy `projects/chirality-app-dev/.github/workflows/harness-premerge.yml`, as the manager instructed. That copy starts no Runtime service and sets no binding, so its readiness poll and routes would answer 503 at the frozen basis. It also sits in a directory that GitHub Actions does not load. The workflow that actually operates is the repo-root file, which is out of root. *Alternative:* UNKNOWN, on the ground that the operative workflow cannot be read.
- **CLM-003 / CLM-017 / CLM-018.6 / CLM-023, STALE_SPECIFICATION.** These rely on D-APP-56 P37/P45 (UPD-142) renaming the CI artifact to `harness-validation-summaries`, as recorded in the deliverable's own DEP-09-01-010 and CLM-013. *Alternative:* the in-root copy still uploads `harness-section8-summary`, so a reader who takes the in-root file as the CI surface would call these ALIGNED for the name.
- **CLM-012 / CLM-013 (AC-001), PARTIALLY_IMPLEMENTED; CLM-019 (VER-001), STALE_VERIFICATION.** The evidence exists but stops at revision 3 (2026-09-04), before D-GOV-43. *Alternative:* STALE_ASSESSMENT, if the Evidence bundle is treated as the operative assessment. Its AssessmentEvidence is OVERTAKEN either way.
- **CLM-016, STALE_SPECIFICATION.** The false present fact is the REF-006 MATCH bullet. The missing Runtime-binding prerequisite on its own would read as PARTIALLY_IMPLEMENTED.
- **CLM-009.9 (REQ-009), PARTIALLY_IMPLEMENTED.** This treats stale present-tense facts as a K-INVENT-1 shortfall. *Alternative:* DEFERRED_AGENT_WORKFLOW, since this is document-authoring discipline tied to a skill.
- **CLM-005, CLM-009.2, CLM-010, ALIGNED.** CLM-009.2 notes that CONTRACT K-VALIDATE-1 (`docs/CONTRACT.md:139`) lists `desktop:dist` as a required check, while SPEC §19.1 and PRD §12.2 separate it out as packaging. The SoW follows SPEC and PRD. I did not treat this as AUTHORITY_CONFLICT because the SoW text ("must include" four commands) contradicts neither source.

## 3. Register-defect summary

- **REGISTER-1** (STALE_SPECIFICATION). In `_REFERENCES.md`, REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD are recorded MATCH, but none reproduces (`HASH-RECOMPUTE@00115c719`, REFERENCE_HASHES.csv). REF-001 DIRECTIVE, REF-004 TYPES and REF-005 PLAN recompute equal. I did not recompute REF-007, REF-009 or REF-010: they are Root `workflows/software-decomp/**` paths outside the evidence roots. Eight SoW rows restate the MATCH as current and cite REGISTER-1 through SEE. CLM-027 separately quotes a hash pair (`ac35fba4…`) that matches neither side.
- **REGISTER-2** (REMAINING_STATE_MISMATCH). In `_DEPENDENCIES.md`, "Declared Upstream/Downstream: TBD — no edges extracted" and the Lifecycle Summary "TBD 10" lag behind the file's own P45 block (SATISFIED=1, TBD=9) and Dependencies.csv. DEP-09-01-010 is marked SATISFIED on the strength of the repo-root workflow, which is OUT_OF_ROOT and could not be verified.
- **Also noted, not rowed.** `_STATUS.md` `Last Updated: 2026-09-04` lags behind the trigger merges; this is folded into REM-1. The SoW `decomposition_basis` pin `d6f6cadb2` differs from the decomposition's last change `dbd812a52`, a known basis defect (RUN_BASIS §5).

## 4. Direction and cause

Main CauseTags:
- DOC_HYGIENE 12 (REF-006 restatements, the hash pair, dependency bookkeeping, REQ-009);
- PRE_V3_DRIFT 8 (the provenance summary deleted on 2026-06-15 at `b946950d5`; the in-root workflow, unchanged since `7bee9ae41`, 2026-05-18, and left behind by the Runtime-binding requirement of `99fe2edae`, 2026-07-23; the D-APP-56 artifact rename carried into only part of the kit; the missing-ID fixture);
- A2_TOPOLOGY 4 (REM-1, CLM-012, CLM-013, CLM-019);
- CODEX_SOLE_ENGINE 2 (CLM-009.8, STATE-1).

CAUSE2 secondaries: A2_TOPOLOGY on CLM-009.7, 009.8, 016, 017 and 023. CARRIER_PROPAGATION on CLM-003, 018.6, 019, REM-1 and STATE-1. DOC_HYGIENE on CLM-004. PRE_V3_DRIFT on CLM-013.

Records used:
- GOV: D-APP-56 (P37 CI hand-off to DEL-09-05; P45 UPD-140/141/142).
- GOV: D-APP-127. It preserves daemon-era executed records but supersedes their applicability, and it authorizes no "reliance on the retired daemon path".
- CTX: `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/W3_RETURN.md` §8. It records that the repo-root harness-premerge workflow needs A2 rework, that no project token is minted under A2, and that a CI stub engine "should be an option of the App-owned composition".
- D-APP-38 is cited for the REF-006 history.

NONE_FOUND searches:
- `_DECISIONS/_REGISTER.md` for DEL-09-01, Section 8, premerge and REF-006: only D-APP-56 P37 and the D-APP-88 boundary mention premerge.
- The D-APP-127, D-APP-97 and D-APP-56 ruling records.
- CONTEXT sources: AgentRuns APP_V3_CODEX_HOST_REPLATFORM_20260912 (grep "Section 8|premerge") and `plans/steers`.
- The release plan HTML named in RUN_BASIS §5 is not present at `projects/chirality-app-dev/plans/` in the frozen tree.

No UNRECORDED_JUDGMENT rows.

Key evidence chain for REM-1 and the A2 rows:
1. Running `git log --first-parent e2f8317da..00115c719` over the revision-trigger surfaces returns 13 merges, including `19bca4930` (PR #774, D-GOV-43), so gate condition 1 has occurred.
2. `validate-harness-section8.mjs` itself changed at `9eaddb596`.
3. `39c0bb6ab` removed the `--runtime-daemon` entry that `rerun-section8-local.sh` starts.
4. `runtime-daemon-harness-port.ts:1081-1100` binds only to a `project-*.token` with project id `chirality-app-dev`, while A2 writes `client-token` (`electron/runtime-service-host.ts:38`).

The REM-1 Depends list names DEP-09-01-008, an ACTIVE PREREQUISITE with SatisfactionStatus TBD. MechanicallyUnblocked is therefore NO.

PostReleaseBasis is NO on every row. None of the cited App files is in TOUCHED_PATHS.csv. The one cited touched file, `packages/daemon/src/app-owned-composition.ts:33`, blames to `fca60696d`, which is not one of the four post-release commits.

Done-declaration context: Q-02 (release act and the F-APP-2 fence) does not bear on any DEL-09-01 row. This deliverable makes no signing, notarization or release claim.

## 5. Method friction

- **In-root versus repo-root workflow.** The SoW's `.github/workflows/harness-premerge.yml` is ambiguous. SoW paths are App-relative elsewhere, but CLM-013 and the evidence bundle (`EVALUATOR_BYTES_revision3.tsv`) mean the repo-root file, which is out of bounds. The in-root file is a stale copy in a directory that GitHub Actions does not load. *Proposal:* the brief should say which file is the CI evidence surface, or allow read access to the one repo-root workflow a deliverable names.
- **REACH for build and CI scripts.** The validator's CODE_PATH regex treats `frontend/package.json` and `frontend/.gitignore` as code, so they need REACH tags. I tagged package scripts LIVE, following the manager's note. I left the in-root `.yml` untagged, because it is not a code extension and is not executed.
- **Selectability-tag mismatch on an open Remaining item.** The tie-break (rule 2a) covers "open or done status"; a stale `NOT_SELECTABLE_UNTIL` tag is not quite either. I used REMAINING_STATE_MISMATCH with ALSO:STALE_SPECIFICATION. *Proposal:* name selectability tags explicitly in rule 2a.
- **R4-Q1 when a claim is mixed.** The claim is met mostly by LIVE code, with one sub-behaviour met only by LEGACY_ONLY code (CLM-009.8). Rule 3 and the Addendum 8 reading address LEGACY plus TEST_ONLY, not LIVE plus LEGACY_ONLY. I cited R4-Q1 because the marker sub-claim has no live implementation. *Proposal:* say whether rule 3 applies per sub-claim.

## 6. Effort

About 40 files or ranges read. These were the deliverable kit (SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `_DEPENDENCIES`, Dependencies.csv, MEMORY, the INSP-03 assessment, two run records, EVIDENCE.md and EVALUATOR_BYTES_revision3.tsv), both validation scripts, the release-quality wrapper (grep), the test file, the in-root workflow, package.json, the daemon-harness-port pair, main.ts and runtime-service-host (ranges), selected harness routes, app-owned-composition (grep), SPEC §19, PRD §12 and FR-066/068, CONTRACT K-VALIDATE-1, and the D-APP-127, D-APP-56 and W3 CONTEXT excerpts. Git: 8 read-only log/show/blame calls against the frozen tree. The context budget was comfortable, not tight.

## Coverage gaps

- **Section 8 under the A2 Runtime service.** No deliverable text owns how Section 8 is meant to bind to the App-owned Runtime service. The `project-*.token` / `CHIRALITY_RUNTIME_PROJECT_ID` env contract in `runtime-daemon-harness-port.ts` does not match A2's `client-token`. The ownership question is whether that belongs to DEL-09-01, DEL-09-05 (the CI owner) or a Runtime-integration deliverable. The same goes for whether `frontend/scripts/controlled-ci-runtime.ts` and `build-controlled-ci-runtime.mjs` (still present, and reported broken against the A2 core in W3_RETURN §8) are to be retired.
- **In-root workflow copy.** `projects/chirality-app-dev/.github/workflows/harness-premerge.yml` is a stale, non-executed copy, and no deliverable claims it as its own. A candidate for DEL-09-05 or the extension item 4 audit.
