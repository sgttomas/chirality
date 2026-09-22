---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-04
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-030, SOW-072, SOW-073, SOW-078]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-04

## Codex MVP packaging basis

Codex is the sole MVP engine. Under D-GOV-43 topology A2 and D-APP-127, the App owns its Runtime service child and Runtime owns the stock Codex App Server child. Hosted supplier admission, per-root account consent, the LaunchAgent, packaged-basis hashing and supplier-containment evidence are retired subjects; they are not present-day qualification gates.

The App must preserve Codex-held credential custody and separation from other Codex clients, user-selected approval and sandbox policy, truthful event/approval presentation, and applicable renderer, attachment, secret-protection and package-executability controls. Historical Anthropic/Claude/Pi descriptions remain compatibility evidence and do not qualify the live Codex path.

Artifact identity must bind the selected candidate package version, App Info.plist and actual `Chirality-<candidate-version>-arm64.dmg`. Packaged executable behavior and instruction-root integrity require actual package evidence. Signing, notarization, minimum-OS and architecture inspection results must be recorded against that candidate; no result is inferred from a missing record.

Verification hooks: `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md` in the same folder, plus `frontend/package.json` registered packaging/security commands. These procedures supersede the retired Stage 9–13 spine; repeat affected checks when source, configuration or packaging changes invalidate earlier evidence. No publication or product acceptance follows from this text repair.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-04` in service of project scope [SOW-030, SOW-072, SOW-073, SOW-078] and package objectives [OBJ-008].

- **OUT-001** — A macOS 15+ Apple Silicon arm64 package and instruction-root integrity evidence bundle for the consolidated candidate, including bundled pinned Codex execution through App-owned Runtime, accepted K-NET-1 transports and user-selected policy, required signing/notarization result and explicit blockers. Unsigned/adhoc local-builder outputs remain labelled development evidence.

**D-APP-80 concordance note (2026-07-28):** SOW-078 is recorded as an OUT
boundary-only trace. Windows and Linux packaging remain outside the current
release target unless a later accepted scope amendment says otherwise.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Datasheet: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-04 |
> | DeliverableName | macOS DMG Packaging and Instruction Root Integrity |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | CI_CD_CHANGE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | L |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Release target | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` Section 1.9; `docs/SPEC.md` Section 19.4 |
> | Packaging command | `npm run desktop:dist` from `frontend/` | `docs/SPEC.md` Section 19.1; `docs/PLAN.md` release validation commands |
> | Required packaging outputs | `frontend/dist/Chirality-<candidate-version>-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 |
> | Instruction-root integrity command | `npm run instruction-root:integrity` | `docs/SPEC.md` Section 19.1; `docs/TYPES.md` Section 12 |
> | Instruction-root packaged resource requirement | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` Section 1.3; `docs/SPEC.md` Section 1.1 |
> | SDK subprocess packaging posture | Verify the bundled pinned stock codex app-server can execute as a child of the App-owned Runtime service. Retired SDK supplier/layout proof is historical. | `docs/PRD.md` NFR-030 and Section 12.8; `docs/SPEC.md` Section 19.4 |
> | Source-completeness state | Required instruction-root assets may be incomplete in the current source or packaging state; this remains a P0 readiness gate. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OI-004; `docs/PRD.md` Section 10.1 |
> | PRD source status | historical D-APP-38 source state; verify current candidate bytes treated as source status for this run. | `_REFERENCES.md` REF-006; assignment override — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Build platform prerequisites | Node.js >=22.19.0 and installed frontend dependencies; prepare instruction resources and Runtime/frontend builds before pack/dist. | `docs/PRD.md` Section 6.2 and CI sequence near Section 12.2 |
> | Release scope exclusions | Windows/Linux packaging is out of current release scope unless amended. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-078; `docs/PRD.md` KG-014 |
> | Signing posture | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. | `docs/PRD.md` Sections 6.2 and 7.12; `docs/SPEC.md` Section 19.4 |
> | Network/security posture during packaged validation | Record current K-NET-1 transports and the user-selected Codex policy, renderer restrictions, secret protection and actual packaged outcomes; retired supplier containment is not a gate. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
>

### CLM-005 — Construction

> ##### Construction
>
> The deliverable consists of packaging changes and evidence artifacts sufficient to:
>
> - run the local validation sequence from `frontend/`;
> - build the macOS arm64 DMG with `desktop:dist`;
> - prove the app bundle includes required instruction-root assets;
> - preserve or emit the latest instruction-root integrity summary;
> - verify bundled pinned Codex executable executability from the package layout; and
> - record any residual blockers, especially source-completeness or SDK packaging issues.
>

### CLM-006 — References

> ##### References
>
> - `docs/CONTRACT.md` Sections 1.3 and 1.9.
> - `docs/SPEC.md` Sections 1.1, 19.1, and 19.4.
> - `docs/TYPES.md` Section 12.
> - `docs/PLAN.md` release validation commands and risk table.
> - `docs/PRD.md` Sections 6.2, 7.12, 8.11, 10.1, 12.2, 12.8, NFR-030, KG-014, KG-025.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` entries for DEL-09-04, SOW-030, SOW-072, SOW-073, SOW-078, OI-003, OI-004.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Specification: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable covers macOS arm64 packaging and instruction-root integrity for the current consolidated App candidate. Local unsigned/adhoc DMG and app-directory builds remain development evidence; release qualification requires source-bound signing/notarization and a bundled pinned Codex executable through App-owned Runtime, with actual native outcomes recorded.
>
> In scope:
>
> - `frontend/` local packaging command `npm run desktop:dist`.
> - `frontend/` app-directory packaging command `npm run desktop:pack`, which is
>   the layout exercised by the packaged probes and D-APP-18 live proof.
> - DMG output verification for macOS 15+ Apple Silicon.
> - App bundle instruction-root asset inclusion and integrity verification.
> - bundled pinned Codex executable package-layout probe.
> - Integrity summary evidence.
>
> Out of scope:
>
> - Windows/Linux packaging, unless a governed amendment reopens it.
> - Feature implementation unrelated to packaging glue, integrity checks, or package-layout probes.
> - No signing/notarization result is inferred from an unsigned/adhoc local build. The governed release candidate still requires the accepted signing/notarization checks.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-09-04-REQ-001 | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 | Inspect app bundle architecture, `LSMinimumSystemVersion`, and signing posture. |
> | DEL-09-04-REQ-002 | The desktop distribution build must be produced through `npm run desktop:dist` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` FR-067 | Run or review build evidence for `npm run desktop:dist`. |
> | DEL-09-04-REQ-003 | The expected DMG output must include `frontend/dist/Chirality-<candidate-version>-arm64.dmg`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 7.12 | Confirm file exists after packaging. |
> | DEL-09-04-REQ-004 | The expected app bundle output must include `frontend/dist/mac-arm64/Chirality.app`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm app bundle exists after packaging. |
> | DEL-09-04-REQ-005 | The build/integrity flow must produce or preserve `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`, and packaging evidence must state either a passing integrity verdict or enumerated blockers. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm summary JSON exists and records a passing integrity result, or record blocker. |
> | DEL-09-04-REQ-006 | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` K-PACKAGE-1; `docs/SPEC.md` Section 1.1 | Run/review `npm run instruction-root:integrity` and bundle resource inspection. |
> | DEL-09-04-REQ-007 | Missing required instruction-root assets are a P0 packaging and runtime-readiness blocker. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1; decomposition OI-004 | Fail packaging readiness if required assets are absent, or document accepted amendment. |
> | DEL-09-04-REQ-008 | Package evidence must verify bundled pinned Codex execution through the App-owned Runtime child, recording candidate, executable path, command, expected/observed result and secret/network assertions or the exact blocker. | `docs/PRD.md` NFR-030; `docs/PRD.md` KG-025; `docs/SPEC.md` Section 19.4 | Execute packaged Codex execution probe in packaged layout; record command, package path, expected result, observed result, and blocker state. |
> | DEL-09-04-REQ-009 | Packaged validation must verify the current K-NET-1 transport scope and actual user-selected Codex policy, with renderer restrictions and secret protection. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 | Run/review network guardrail checks or document blocker. |
> | DEL-09-04-REQ-010 | Windows/Linux packaging must not be introduced by this deliverable without explicit scope amendment. | Decomposition SOW-078; `docs/PRD.md` KG-014 | Review package scripts/config changes for target creep. |
> | DEL-09-04-REQ-011 | App-directory packaging used by packaged probes must be produced through `npm run desktop:pack` from `frontend/`. | D-APP-18; D-APP-56 R4-P03; `docs/BUILD_AND_RELEASE.md` | Run or review the app-directory packaging proof. |
>

### CLM-010 — Standards

> ##### Standards
>
> - `docs/CONTRACT.md` K-ROOT-1, K-ROOT-2, K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1.
> - `docs/SPEC.md` Section 1.1 instruction-root requirements and Sections 19.1/19.4 release validation requirements.
> - `docs/PRD.md` FR-067, NFR-030, KG-014, KG-025.
> - `docs/TYPES.md` release and validation vocabulary for `instruction-root:integrity` and `desktop:dist`.
>

### CLM-011 — Verification

> ##### Verification
>
> The verification package should include:
>
> | Verification Item | Expected Evidence | Requirement Coverage |
> |---|---|---|
> | Local build command evidence | command transcript or CI/local run record for `npm run desktop:dist` | DEL-09-04-REQ-002 |
> | DMG artifact check | file listing or checksum for `frontend/dist/Chirality-<candidate-version>-arm64.dmg` | DEL-09-04-REQ-001, DEL-09-04-REQ-003 |
> | App bundle check | file listing for `frontend/dist/mac-arm64/Chirality.app` | DEL-09-04-REQ-004 |
> | Minimum macOS version check | inspected `LSMinimumSystemVersion` value `15.0.0` or later | DEL-09-04-REQ-001 |
> | Architecture check | inspected arm64 binary architecture | DEL-09-04-REQ-001 |
> | Signing posture check | local unsigned/adhoc status labelled development evidence; release-candidate signature/notarization verified separately | DEL-09-04-REQ-001 |
> | Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` with explicit pass verdict or enumerated blockers | DEL-09-04-REQ-005, DEL-09-04-REQ-006, DEL-09-04-REQ-007 |
> | packaged Codex execution probe | package-layout probe command, package path, expected result, observed result, and failure/blocker recording rule for bundled pinned Codex executable | DEL-09-04-REQ-008 |
> | Network guardrail check | evidence accepted Codex supplier network policy remains active | DEL-09-04-REQ-009 |
>
> Current candidate evidence is incomplete when instruction-root assets are absent, integrity fails, the bundled pinned Codex cannot execute through App-owned Runtime, or required signing/notarization proof is missing. Local unsigned/adhoc build results remain development evidence and do not satisfy the release gate.
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - `desktop:dist` command transcript or equivalent run record.
> - DMG and app bundle artifact listing plus checksum or deterministic artifact identifier for the DMG.
> - Instruction-root integrity summary with pass/blocker verdict.
> - packaged Codex execution probe command and result.
> - Audit-ready evidence bundle pointers to command transcript, artifact listing/checksum, summary JSON, packaged Codex execution probe output, network guardrail evidence, and residual blockers.
> - `TBD` residual-blocker list for incomplete instruction-root assets, bundled pinned Codex/App-owned Runtime execution failures, signing/notarization gaps, or unresolved packaged-app guardrail scope.
> - `ASSUMPTION` or `PROPOSAL` entries for any packaging config interpretation not directly supported by source evidence.

- **AC-001** — The desktop distribution and app-directory packaging evidence identifies the expected DMG and app bundle, verifies arm64 architecture, minimum macOS 15.0.0, required instruction-root assets and passing integrity summary, bundled pinned Codex execution through App-owned Runtime, current K-NET-1 transports and user-selected Codex policy, and the required signature/notarization result for the consolidated release candidate. Unsigned/adhoc local builds are labelled development evidence; missing or failed candidate proof remains an explicit blocker.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-014 — Purpose

> ##### Purpose
>
> Define operational steps for local unsigned/adhoc development builds and for the consolidated signed/notarized macOS arm64 candidate. Bind instruction-root resources and bundled pinned Codex execution through App-owned Runtime to the actual package; record missing native results as blockers.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> - ResponsibleParty: TBD.
> - Work from `frontend/` for local validation and packaging commands.
> - Node.js `>=22.19.0` is available.
> - Dependencies have been installed with `npm ci`.
> - Required instruction-root assets are present or missing assets are tracked as blockers.
> - Dependency state: `Dependencies.csv` v3.1 currently contains 9 ACTIVE rows; six rows remain `SatisfactionStatus=TBD`, so dependency closure remains open until accepted evidence resolves them.
> - Evidence bundle custody: ResponsibleParty remains TBD; until assigned, route release evidence bundle ownership through the package owner or human-appointed release reviewer.
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.
>

### CLM-016 — Steps

> Use the current procedure in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`. Stop the development server before packaging. Prepare instruction-root resources, build Runtime and frontend (the desktop:prepare chain), then produce the App/DMG through desktop:pack/desktop:dist as applicable. Packaging alone does not perform those prerequisite builds.
>
> Bind the App/DMG identities, instruction-root integrity summary, inspected architecture and minimum macOS, signature/notarization posture and bundled Codex lockfile pin to the actual candidate. Run instruction-root:integrity against the packaged bundle. Verify Codex execution through the application-owned Runtime service and applicable packaged S-6/S-8 checks; record real outcomes or HOST_RERUN_REQUIRED/blockers. Preserve secret and network evidence. Reuse earlier evidence only while its source/configuration/package basis remains valid under D-APP-127.
>
> Ordinary local builds may be unsigned/adhoc. The consolidated candidate signing/notarization requirement is already settled by D-GOV-43; release/publication is separately authorized for an exact candidate. This procedure creates neither a release act nor an unobserved native result.

### CLM-017 — Verification

> ##### Verification
>
> | Check | Pass Criteria | Requirement Link |
> |---|---|---|
> | Local checks | Required commands exit zero or accepted evidence explains non-run state. | DEL-09-04-REQ-002, DEL-09-04-REQ-006 |
> | DMG artifact | `frontend/dist/Chirality-<candidate-version>-arm64.dmg` exists after `desktop:dist`. | DEL-09-04-REQ-003 |
> | App bundle artifact | `frontend/dist/mac-arm64/Chirality.app` exists after `desktop:dist`. | DEL-09-04-REQ-004 |
> | Integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists and states a pass verdict, or all failed/missing assets are enumerated as blockers. | DEL-09-04-REQ-005, DEL-09-04-REQ-007 |
> | macOS target | Binary architecture is arm64 and minimum macOS target is `15.0.0` or later. | DEL-09-04-REQ-001 |
> | Signing posture | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. | DEL-09-04-REQ-001 |
> | SDK subprocess | Packaged bundled pinned Codex executable probe records command, package path, expected result, observed result, and shows the binary is locatable and executable from app bundle/package layout. | DEL-09-04-REQ-008 |
> | Network guardrails | Packaged validation preserves accepted Codex supplier network policy. | DEL-09-04-REQ-009 |
>

### CLM-018 — Records

> ##### Records
>
> Required records:
>
> | Record | Required content |
> |---|---|
> | Pre-packaging command transcript | Command, cwd, timestamp/version, exit status, and accepted non-run evidence basis if substituted. |
> | `desktop:dist` evidence | Command transcript or build run record plus output paths. |
> | DMG artifact identity | `frontend/dist/Chirality-<candidate-version>-arm64.dmg` listing plus checksum or deterministic artifact identifier. |
> | App bundle artifact identity | `frontend/dist/mac-arm64/Chirality.app` listing and inspected release posture. |
> | Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` with pass verdict or blocker list. |
> | packaged Codex execution probe | Probe command, package path, expected result, observed result, output path, and blocker state if failed. |
> | Manual package verification notes | Architecture, minimum OS, signing posture, resource inclusion, working-root selector, network policy, and SDK packaged execution scope. |
> | Evidence bundle custody | ResponsibleParty or routing placeholder; currently `TBD` until human assignment. |
> | Blocker list | REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes. |

- **VER-001** — Run or review pre-packaging checks and local/candidate package evidence; inspect DMG and app-bundle identities, architecture, minimum OS, required candidate signature/notarization, packaged resources, integrity summary, bundled pinned Codex execution through App-owned Runtime, network guardrails and residual blockers. Label unsigned/adhoc results as development evidence.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Guidance: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-020 — Purpose

> ##### Purpose
>
> This deliverable makes release packaging explicit and repeatable for the current macOS-only target. Its job is not just to produce a DMG, but to prove that packaged Chirality preserves the instruction-root resource boundary and can execute the bundled pinned Codex executable from the packaged layout.
>

### CLM-021 — Principles

> ##### Principles
>
> - Treat `desktop:dist` as release-significant. `docs/CONTRACT.md` K-VALIDATE-1 includes `desktop:dist` among checks required before release-significant changes are accepted.
> - Keep the release target narrow. `docs/PRD.md` KG-014 and decomposition SOW-078 make Windows/Linux packaging out of scope without amendment.
> - Treat instruction-root resources as package blockers. `docs/SPEC.md` Section 1.1 says missing required instruction-root assets are a P0 packaging and runtime-readiness blocker.
> - Preserve Chirality-owned boundaries in packaged form. Packaged validation should still exercise instruction-root integrity, working-root availability, current K-NET-1 transports and user-selected Codex policy, and SDK package execution.
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.
>

### CLM-022 — Considerations

> D-GOV-43 settles the two-tier packaging/signing posture recorded in CLM-003/009. Earlier 3.0.0/3.0.1 releases and OC-01 exact-candidate testimony remain historical acts; lagging unsigned-only wording does not make them newly unauthorized. No further release is inferred.
>
> Instruction-root completeness remains a real gate. `frontend/scripts/prepare-packaged-instruction-root.mjs` is the concrete manifest evidence; differences from SPEC §1.1 concerning docs/PLAN.md, WHAT-IS-AN-AGENT.md and PROFESSIONAL_ENGINEERING.md require source-completeness reconciliation by the owner. A boot hash cannot substitute for ordinary instruction-root write protection. Native candidate outcomes, architecture/minimum-OS inspection and S-6/S-8 remain unknown unless their actual records are recovered or checks run. Owner testimony is retained as testimony, not fabricated output.

### CLM-023 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Strict asset completeness vs. build progress | Prefer failing readiness with a documented blocker when required instruction-root assets are absent. Do not weaken integrity requirements without a governed amendment. |
> | `app.asar` packing convenience vs. SDK executable access | Prefer package layout that allows the bundled pinned Codex executable to be found and executed. If `asar` trapping prevents execution, record the packaging probe failure and adjust packaging under this deliverable. |
> | Local unsigned DMG vs. notarized distribution | Keep unsigned/adhoc builds as development evidence; the consolidated candidate requires verified signing/notarization under D-GOV-43. No result is inferred without native proof. |
> | General release checklist vs. DEL-09-04 scope | Keep CI artifact upload and broader release workflow details in DEL-09-05 unless directly needed to prove the DMG/instruction-root/SDK packaging result. |
>

### CLM-024 — Examples

> A package example must cite an actual A2 record under `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/` and identify the source/package it checked. No accepted example is asserted for missing minimum-OS/architecture, packaged network, Codex execution or S-6/S-8 outputs. Owner testimony stays labelled as testimony. Do not turn a build script or version bump into a native result.

### CLM-025 — Conflict Table (for human ruling)

> CONF-001 is historical source currentness under D-APP-38; verify current bytes. CONF-002/003 retain the concrete required-asset mismatch against `frontend/scripts/prepare-packaged-instruction-root.mjs` (including PLAN.md and the two named explanatory/professional assets); resolve by satisfying the accepted set or its owning scope amendment. CONF-004’s SDK probe question is superseded by D-GOV-43/D-APP-127: packaged Codex execution and applicable S-6/S-8 are the current subjects. Missing actual result artifacts remain delivery work, not a new signing-posture vote.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-030 SOW-072 SOW-073 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
