# Orchestration Plan — APPDEV_V3_NODE_B_2026-09-03

- **RunID:** `APPDEV_V3_NODE_B_2026-09-03`
- **Plan version:** 1 (frozen before any write outside this directory)
- **Selection authority:** owner-directed dev-slate selection transmitted through HELP_HUMAN (Agent 0; Claude Fable 5.1) on 2026-09-03: development node B = the three `SELECTABLE` DEL-09-05 v3 items (V3-01, V3-02, V3-03), WP-09 preparation only. The seating that made them selectable is A12 (`plans/steers/chirality_app_v3_app_ruling_record_a12_2026-09-03.md`), merged as PR #681 (`0c683fb16`).
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session.
- **Executor (B1):** one ephemeral Agent 2 implementer (Claude Fable 5.1, `claude-fable-5-1`) under the sealed brief in `instances/B1_IMPLEMENTER/LAUNCH_BRIEF.md`; no delegation.
- **Reviewer (B2):** a fresh read-only reviewer dispatched by HELP_HUMAN over 100% of the frozen diff (AGENTS.md independent-review path); its return is saved under `instances/B2_REVIEWER/`.
- **Posture:** `TERMINAL_FAN_OUT_IN` — B1 executes N1..N5 sequentially in one worktree; B2 reviews; HELP_HUMAN fans in.
- **Basis:** `0c683fb1657706316272951e4c3a0f7781b46009` (= `origin/main` at cut; required basis satisfied).
- **Working root:** `projects/chirality-app-dev`; `FRONTEND` = `projects/chirality-app-dev/frontend`.
- **Accepted upstream truth consumed:** DEL-09-05 `ScopeOfWork.md` (OUT-002, REQ-001..004, AC-002, VER-002) at the applied decomposition `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; `_STATUS.md` `## Remaining` item contracts; `_DEPENDENCIES.md` (DEP-09-05-015 G6a constraint); D-APP-97 C1 evidence (PR #583 run `32327128935`); the pinned plan HTML (completion meaning only); App docs `docs/BUILD_AND_RELEASE.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/RELEASE_QUALITY_RUNBOOK.md`, `docs/ISSUE_READINESS_PROFILES.md`.

## Nodes

| Node | Item | Objective | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| N0 | — | Step 0 discovery and record (`STEP0_DISCOVERY.md`, this plan, `WORK_GRAPH.json`, launch brief) | this run-record directory | Step 0 record | preflights ALLOW/VALID/no drift |
| N1 | V3-02 | `frontend/scripts/generate-sbom.mjs` (pinned Syft, CycloneDX JSON, refusal paths) and `frontend/scripts/generate-third-party-notices.mjs` (production closure incl. `@chirality/*` links and the four Pi packages; deterministic); npm scripts `sbom:generate`, `notices:generate`; tests under `src/__tests__/scripts/` | `frontend/scripts/**`, `frontend/package.json` scripts block, `frontend/src/__tests__/scripts/**` | scripts + tests | typecheck, vitest, build |
| N2 | V3-03 | `frontend/scripts/verify-version-identity.mjs` (every identity surface; `--expect`; dry-run report; staged-patch emission), npm script `verify:version-identity`, tests; staged `3.0.0-rc.1` patch bytes + SHA-256 + dry-run reports under `Evidence/VERSION_IDENTITY_3.0.0-rc.1/` — not applied | as N1 plus the DEL-09-05 `Evidence/**` | check + staged patch + reports | `--expect 2.0.0` passes on the tree; `--expect 3.0.0-rc.1` reports mismatch; `git apply --check` of the patch passes; `package.json` version unchanged |
| N3 | V3-02 | Evidence bundle `Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/`: notices output run twice (byte-identical), SBOM `UNAVAILABLE_UNDER_BOUNDS` record (Syft absent; no download), run record with command/cwd/env/versions/exit/hashes, sorted manifest | DEL-09-05 `Evidence/**` | bundle | hashes recomputable; no bulk binary committed (D-APP-99) |
| N4 | V3-01 | `Release_Runbook_CANDIDATE_2026-09-03.md` and `Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` in the DEL-09-05 folder, headed `CANDIDATE — NOT ADOPTED — WP-09 authoring only; performs no release act` | DEL-09-05 folder | candidate bytes | covers every REQ-002 element; each step names gate, decision owner, evidence obligation, and "not performed in preparation" |
| N5 | — | Checks (`CHECKS.json`), `validate_change_scope.py`, `_run_records/**` entry, local commit, `RETURN.md`; freeze for B2 | run record, DEL-09-05 `_run_records/**` | `REVIEW_READY` | all checks pass or are recorded as the deferrable "absent runtime-daemon bindings" class only |
| N6 | — | After `REVIEW_PASS`: reviewer return saved; `_STATUS.md` (remove V3-01/02/03; History line), `MEMORY.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, Receipt 207; rebase; rerun; push; PR | DEL-09-05 `_STATUS.md`/`MEMORY.md`, run record, `loop/LOOP_RECEIPTS.md` append | PR number, head SHA | receipts validator VALID; owner merge is a later human act |

## Human decision points (none crossed here)

- Owner merge of the PR (confers landed status only).
- DEL-09-05-V3-06 owner ruling applying the 3.0.0-rc.1 identity to product.
- G5 REVIEW verdict over the seated runbook; G6a exact-candidate ruling lifting D-APP-97/F-APP-2 for that candidate; G6b/G-KEY/G7/G8 owner acts (WP-11).
- Owner host act for DEL-09-05-V3-04 (self-signed drill).
- SCOPE_AMENDMENT S-6 (repo-root workflow wiring of the SBOM/notices tooling).

## Constraints carried

Sealed write set (`frontend/scripts/**` new files, `frontend/package.json` scripts block only, `frontend/src/__tests__/scripts/**`, the DEL-09-05 folder, this run record, `loop/LOOP_RECEIPTS.md` append at closeout); nothing else may change. F-APP-2 and D-APP-97 active; no signing identity, Apple service call, notarization, distribution, product version change, `.github/workflows/**` change, release-readiness claim, or WP-11 act. A1 re-stage declaration recorded in `STEP0_DISCOVERY.md`.
