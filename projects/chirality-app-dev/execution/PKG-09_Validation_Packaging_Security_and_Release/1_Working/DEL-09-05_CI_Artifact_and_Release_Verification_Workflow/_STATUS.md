# Status: DEL-09-05

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-04
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-09-05-V3-02** (`SELECTABLE` — residual only: the CycloneDX SBOM evidence for one identified artifact; the tooling, tests, and notices evidence landed in node B) — artifact evidence tooling: pinned-Syft CycloneDX SBOM and full-closure third-party notices.
  Trace: OUT-002 (CI workflow and stable artifact evidence; exact-candidate identity and custody checklist), REQ-001, AC-002, VER-002; CLM-034.
  Plan: WP-09; G5 pass evidence (pinned Syft CycloneDX JSON; notices); AT-039 notices/SBOM inputs; AT-001 evidence input. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Landed (node B, 2026-09-03): `frontend/scripts/generate-sbom.mjs` (Syft pinned `v1.18.1`; refuses absent/mismatched Syft; `--closure`/`--artifact`/`--dry-run`), `frontend/scripts/generate-third-party-notices.mjs`, npm scripts `sbom:generate`/`notices:generate`, unit tests, and `Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/` (notices generated twice byte-identical; SBOM recorded `UNAVAILABLE_UNDER_BOUNDS`).
  Blocker: SBOM `UNAVAILABLE_UNDER_BOUNDS` — Syft `v1.18.1` is not installed on the executing host; the exact command is recorded in `Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/sbom/dry-run.closure.json`. A15 prospectively authorizes the owner host install and lifts A14's dated deferral without invalidating it; this record-only tranche did not perform the install, so the SBOM remains operationally blocked until Syft `v1.18.1` is observable on the owner host (no agent download/network act).
  Depends: owner host act installing Syft `v1.18.1` (authorized prospectively by A15, not yet performed or observable), or an owner re-pin of `SYFT_PIN` (a recorded tooling change); the unsigned artifact from the D-APP-97 C1 workflow or an offline `desktop:pack` for the `--artifact` scan. Wiring into repo-root `.github/workflows/**` needs an owner scope grant beyond `projects/chirality-app-dev/**` (SCOPE_AMENDMENT S-6) and is not selectable here.
  Write locus: deliverable-local evidence (`Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/sbom/**` or a dated successor bundle) and state; `frontend/scripts/**` only if the pin is re-ruled; any `frontend/` touch carries the A1 re-stage declaration.
  Checks: `npm run sbom:generate -- --closure` and `-- --artifact <app>` exit 0 with `syft version` = pin; APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, receipts validator; registered frontend gates and the independent-review path only if `frontend/` is touched.
  Return: SBOM JSON for the closure and for one identified artifact with the Syft version, command, cwd, env, exit status, and hashes; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract.
  Removed when: the SBOM JSON for one identified artifact lands under this deliverable's evidence with the Syft version and hashes recorded.
- **DEL-09-05-V3-04** (`NOT_SELECTABLE_UNTIL: the owner-created disposable self-signed identity exists on the host — A15 prospectively authorizes creation and the seated drill and lifts A14's dated deferral; DEL-04-05-V3-01 is landed; this record-only tranche performed no host act`) — disposable self-signed A→B credential-transition drill.
  Trace: OUT-002, REQ-002 (recovery/rollback and custody content), AC-002, VER-002.
  Plan: WP-09; G5 self-signed transition drill; AT-051/AT-057 preparation-identity portions; not G-KEY release evidence. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Owner host act creating the disposable identity (authorized prospectively by A15, not yet performed or observable); DEL-04-05-V3-01 typed states (landed); DEL-09-05-V3-01 procedure. A14's 2026-09-03 deferral remains dated history and is lifted prospectively only.
  Write locus: Deliverable-local evidence; no production identity or Apple call.
  Checks: APP-HOLD-1 dispatch preflight, D-APP-38 authority-corpus `status` (no drift), `git diff --check`, repo-wide harness self-check and pytest, and the receipt validator; frontend gates skipped because no product source changes; drill executed under the AGENTS.md host-capability escalation rule.
  Return: Drill record proving usable state preserved where safe or distinguishable non-destructive reauthentication/decrypt-failure states, with cleanup proof; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the drill evidence lands and is cited by the runbook.
- **DEL-09-05-V3-05** (`NOT_SELECTABLE_UNTIL: owner G6a exact-candidate ruling naming the exact artifact and lifting D-APP-97/F-APP-2 for that candidate`) — WP-11 release operation record.
  Trace: OUT-002 (separately authorized WP-11 owner/CHANGE execution record), REQ-003, AC-002, VER-002.
  Plan: WP-11; G6a, G6b, G-KEY, G7, G8 (owner acts; CHANGE performs only authorized Git/publication work). Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Owner G6a ruling; every G5 input; the reviewed runbook. Never agent-executable: the owner performs signing, notarization, stapling, publication, and backcheck acts.
  Write locus: Deliverable-local execution record only.
  Checks: runbook blocking semantics; exact signed-byte reruns; no agent act.
  Return: Owner/CHANGE execution record bound to exact frozen identities; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the immutable publication snapshot is recorded at G8.
- **DEL-09-05-V3-06** (`NOT_SELECTABLE_UNTIL: G5 fan-in per owner ruling A14 (2026-09-03) — product stays 2.0.0; staged patch SHA-256 311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82 recorded under Evidence/VERSION_IDENTITY_3.0.0-rc.1/`) — apply the staged 3.0.0-rc.1 version-identity patch to product.
  Trace: OUT-002, REQ-002 (version-identity runbook content), AC-002, VER-002; CLM-034.
  Plan: WP-09; AT-043 (UI, bundle metadata, DMG filename, release manifest, updater/publication metadata, and runtime report the same 3.0.0-rc.1 identity); G5 and G7 review the applied result. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: DEL-09-05-V3-03 (the identity-consistency check and staged patch bytes); the owner ruling named in the gate; DEL-09-04-V3-01 consumes the applied identity (dependency-linked, not a gate).
  Write locus: `frontend/package.json`, bundle/DMG/manifest identity surfaces enumerated by the staged patch, and deliverable-local state; any `frontend/` touch carries the A1 re-stage declaration.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: The applied patch identity, the identity-consistency check output over every surface, and the ruling citation; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the identity is applied and the check passes on `main`.

## History
- 2026-09-04 - Owner ruling A15 (`plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`, repo root; record-only node M, run record `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/`) prospectively authorized the Syft `v1.18.1` owner-host install for V3-02 and creation plus performance of the disposable self-signed A→B credential-transition drill for V3-04, lifting A14's dated deferrals without invalidating their historical truth. Neither host act was performed: Syft remains operationally blocked until the required version is observable, and V3-04 remains blocked until the owner-created disposable identity exists. No Developer ID signing, notarization, Apple call, distribution, publication, release-readiness, production identity, product, `frontend/`, lifecycle, Checking Approval SHA, or Root act or claim.
- 2026-09-03 - Owner ruling A14 (`plans/steers/chirality_app_v3_app_ruling_record_a14_2026-09-03.md`, repo root; record-only node I, run record `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_I_2026-09-03/`): **V3-06** deferred to G5 fan-in — product stays `2.0.0`; the staged patch (SHA-256 `311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82`) stays recorded and unapplied under `Evidence/VERSION_IDENTITY_3.0.0-rc.1/`; gate text updated. **V3-02** and **V3-04**: the owner deferred both host acts (Syft `v1.18.1` install; disposable self-signed identity); both stay blocked as tagged. No product, `frontend/`, lifecycle, Checking Approval SHA, host, signing, release, or Root act.
- 2026-09-03 - Development node B (WP-09 preparation; run record `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_B_2026-09-03/`, branch `codex/app-v3-nodeB-wp09-prep-2026-09-03`, basis `0c683fb1657706316272951e4c3a0f7781b46009`, rebased onto `9c99e4bf7972bcde0f639b0a7bf8fc2fb731b8da`; content commits `0e5480299`/`e61e546a7`/`f7dead780` pre-rebase): **V3-01** reviewed candidate recorded — `Release_Runbook_CANDIDATE_2026-09-03.md` SHA-256 `5c452dc1fdaf2be1a89b880b77dbba57e144fb1eaed4ddaddac45c12d8849821` and `Exact_Candidate_Identity_and_Custody_Checklist_CANDIDATE.md` SHA-256 `b3332d5642c0591398058b608dc4398fe851ba82fa245cdc0cf8b1ac042b895d`, three independent read-only review rounds (`instances/B2_REVIEWER/REVIEW_0{1,2,3}_*.md`), round 3 PASS; removed from Remaining (execution stays V3-05, `NOT_SELECTABLE_UNTIL` G6a). **V3-02** tooling, tests, npm scripts, and the notices evidence landed (`Evidence/WP09_ARTIFACT_EVIDENCE_2026-09-03/`, notices SHA-256 `384127cc4fc7f807f089c629160beeac4557ae71260bd1e51318bee032d70f52`); SBOM `UNAVAILABLE_UNDER_BOUNDS` pending an owner host act installing Syft `v1.18.1`; item retained with that blocker named. **V3-03** `frontend/scripts/verify-version-identity.mjs`, npm script, tests, and `Evidence/VERSION_IDENTITY_3.0.0-rc.1/` (dry-run reports; staged patch SHA-256 `311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82`, `git apply --check` exit 0, **not applied**; `package.json` version stays `2.0.0`); removed from Remaining (application stays V3-06, parked on the owner version-identity ruling). Checks: typecheck, full Vitest, build, harness self-check, pytest, hold scan, `git diff --check`, change-scope, corpus no drift, receipts validator pass; premerge deferred to PR CI (absent runtime-daemon bindings). A1 re-stage declaration recorded in `STEP0_DISCOVERY.md` (frontend `scripts/**`, `package.json` scripts, `src/__tests__/scripts/**` touched). No signing, notarization, Apple call, distribution, product version change, workflow change, lifecycle, or Checking Approval SHA change; no release-readiness claim.
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; decomposition-conformant v3 outputs/requirements (OUT-002, REQ-*, AC-002, VER-002) added from the Gate-5 row text only; v3 Remaining items seeded (6, of which 3 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-19 - PR #583 proved the D-APP-97 C1 unsigned CI-artifact path in
  `Desktop Unsigned Artifact Verification` run `32327128935`, job
  `96300526868`; the bounded macOS build, DMG mount/posture verification, and
  CI artifact upload passed. The adjacent G4 manifest remediation then passed
  governance run `32327623630`, job `96301949909`. This closes DEL-09-05's
  applicable R4-P49 unsigned-artifact evidence scope and removes its Remaining
  item. State stays IN_PROGRESS; lifecycle, Checking Approval SHA, signing,
  notarization, publication, distribution, release authority, and
  professional claims are unchanged.
- 2026-08-19 - D-APP-97 C1 implementation reactivated the disabled template as
  a least-privilege PR/manual macOS-only unsigned CI-artifact workflow. It
  verifies staged/DMG-mounted identity, unsigned/adhoc and non-notarized
  posture, packaged-dependency and instruction-root evidence, and uploads only
  bounded CI artifacts. Deterministic checks and fresh review passed; the
  actual macOS workflow run remains PR-CI-owed. State remains IN_PROGRESS;
  lifecycle, Checking Approval SHA, signing, notarization, distribution, and
  release authority are unchanged.
- 2026-08-17 - D-APP-97 converted DEL-09-05's D-APP-56-deferred R4-P49 claim
  family into open unsigned local/CI-only release-preparation engineering,
  including the disabled workflow's reactivation as an unsigned-artifact
  workflow. No workflow/product byte, lifecycle, Checking Approval SHA,
  release, signing, notarization, or distribution act occurred in this
  recording tranche.
- 2026-07-12 - D-APP-56 R5 P05 neutralized the desktop-release template by preserving it byte-for-byte as repo-root `.github/workflows/desktop-release-template.yml.disabled`; it is no longer an active GitHub workflow. State remains IN_PROGRESS.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-075, UPD-078; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P45 applied UPD-146, UPD-147; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
