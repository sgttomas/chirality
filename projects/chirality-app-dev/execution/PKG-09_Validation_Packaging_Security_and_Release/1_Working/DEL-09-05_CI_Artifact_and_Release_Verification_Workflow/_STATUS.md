# Status: DEL-09-05

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-03
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-09-05-V3-01** (`SELECTABLE`) — author the WP-09 preparation/release runbook candidate and custody checklist.
  Trace: OUT-002, REQ-001 through REQ-004, AC-002, VER-002; CLM-034.
  Plan: WP-09; seated reviewed runbook is G5 pass evidence; AT-039 identity-freeze method and AT-043 version-identity method are described, not executed; no WP-11 act (G6a). Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: D-APP-97 C1 unsigned-artifact workflow evidence (PR #583 run `32327128935`); DEP-09-05-015 (G6a); A1 re-stage rule for any later frontend touch; nothing else blocks authoring.
  Write locus: This deliverable folder (runbook candidate, custody checklist, review record, `_STATUS.md`, `MEMORY.md`, `_run_records/**`); no `docs/**`, workflow, product, or Root write.
  Checks: APP-HOLD-1 dispatch preflight, D-APP-38 authority-corpus `status` (no drift), `git diff --check`, repo-wide harness self-check and pytest, and the receipt validator; frontend gates skipped because no product source changes; plus a fresh read-only independent review of the runbook candidate (finding-free PASS required before the candidate is recorded as reviewed).
  Return: Runbook candidate bytes covering signing, nested-signing order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version identity, custody, GitHub prerelease, and download backcheck as later owner/CHANGE acts, plus the exact-candidate identity and custody checklist and the review record; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the reviewed candidate is recorded; execution remains DEL-09-05-V3-05.
- **DEL-09-05-V3-02** (`SELECTABLE`) — artifact evidence tooling: pinned-Syft CycloneDX SBOM and full-closure third-party notices.
  Trace: OUT-002 (CI workflow and stable artifact evidence; exact-candidate identity and custody checklist), REQ-001, AC-002, VER-002; CLM-034.
  Plan: WP-09; G5 pass evidence (pinned Syft CycloneDX JSON; notices); AT-039 notices/SBOM inputs; AT-001 evidence input. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: The unsigned artifact from the D-APP-97 C1 workflow or an offline `desktop:pack`; exact Syft version pin recorded. Wiring into repo-root `.github/workflows/**` needs an owner scope grant beyond `projects/chirality-app-dev/**` and is not selectable here.
  Write locus: `frontend/scripts/**` tooling and tests, deliverable-local evidence and state; any `frontend/` touch carries the A1 re-stage declaration.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: SBOM JSON and notice inventory bytes for one identified artifact with the Syft version, command, and hashes; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the tooling and one evidence bundle land with review PASS.
- **DEL-09-05-V3-03** (`SELECTABLE`) — 3.0.0-rc.1 version-identity check and staged patch, kept unmerged to product until G5 rules.
  Trace: OUT-002, REQ-002 (version-identity runbook content), AC-002, VER-002; CLM-034.
  Plan: WP-09; AT-043 (UI, bundle metadata, DMG filename, release manifest, updater/publication metadata, and runtime report the same 3.0.0-rc.1 identity); G5/G7. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Current `frontend/package.json` version `2.0.0` (Receipt 202 report-only finding); DEL-09-04 packaging outputs. Application of the identity to product is the separate parked item DEL-09-05-V3-06; G5 reviews the applied result and is not a gate on it.
  Write locus: `frontend/scripts/**` identity-consistency check plus deliverable-local evidence holding the staged patch bytes and hash; no product version byte changes under this item.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: The identity-consistency check, the staged patch bytes and SHA-256, and a dry-run report enumerating every identity surface; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the check and staged patch are recorded; application is DEL-09-05-V3-06.
- **DEL-09-05-V3-04** (`NOT_SELECTABLE_UNTIL: owner authorization of the host self-signed identity creation (host act) and DEL-04-05-V3-01 landed`) — disposable self-signed A→B credential-transition drill.
  Trace: OUT-002, REQ-002 (recovery/rollback and custody content), AC-002, VER-002.
  Plan: WP-09; G5 self-signed transition drill; AT-051/AT-057 preparation-identity portions; not G-KEY release evidence. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Owner host act for the disposable identity; DEL-04-05-V3-01 typed states; DEL-09-05-V3-01 procedure.
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
- **DEL-09-05-V3-06** (`NOT_SELECTABLE_UNTIL: owner ruling applying the 3.0.0-rc.1 version identity to product (a recorded A-series ruling)`) — apply the staged 3.0.0-rc.1 version-identity patch to product.
  Trace: OUT-002, REQ-002 (version-identity runbook content), AC-002, VER-002; CLM-034.
  Plan: WP-09; AT-043 (UI, bundle metadata, DMG filename, release manifest, updater/publication metadata, and runtime report the same 3.0.0-rc.1 identity); G5 and G7 review the applied result. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: DEL-09-05-V3-03 (the identity-consistency check and staged patch bytes); the owner ruling named in the gate; DEL-09-04-V3-01 consumes the applied identity (dependency-linked, not a gate).
  Write locus: `frontend/package.json`, bundle/DMG/manifest identity surfaces enumerated by the staged patch, and deliverable-local state; any `frontend/` touch carries the A1 re-stage declaration.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: The applied patch identity, the identity-consistency check output over every surface, and the ruling citation; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the identity is applied and the check passes on `main`.

## History
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
