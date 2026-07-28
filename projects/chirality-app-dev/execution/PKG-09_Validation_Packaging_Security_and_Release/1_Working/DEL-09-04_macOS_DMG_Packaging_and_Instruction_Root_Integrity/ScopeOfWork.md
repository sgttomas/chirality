---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-04
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-030, SOW-072, SOW-073, SOW-078]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-04` in service of project scope [SOW-030, SOW-072, SOW-073, SOW-078] and package objectives [OBJ-008].

- **OUT-001** — A macOS 15+ Apple Silicon arm64 unsigned or adhoc local-builder DMG and app-bundle packaging evidence bundle that identifies the required artifacts, proves instruction-root resource integrity and SDK subprocess package-layout executability, preserves current shipped Anthropic network guardrails, and records residual blockers.

**D-APP-80 concordance note (2026-07-28):** SOW-078 is recorded as an OUT
boundary-only trace. Windows and Linux packaging remain outside the current
release target unless a later accepted scope amendment says otherwise.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Datasheet: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
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
> | Release target | macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` Section 1.9; `docs/SPEC.md` Section 19.4 |
> | Packaging command | `npm run desktop:dist` from `frontend/` | `docs/SPEC.md` Section 19.1; `docs/PLAN.md` release validation commands |
> | Required packaging outputs | `frontend/dist/Chirality-0.1.0-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 |
> | Instruction-root integrity command | `npm run instruction-root:integrity` | `docs/SPEC.md` Section 19.1; `docs/TYPES.md` Section 12 |
> | Instruction-root packaged resource requirement | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` Section 1.3; `docs/SPEC.md` Section 1.1 |
> | SDK subprocess packaging posture | Packaged Electron builds must verify that the SDK subprocess/binary can be found and executed from the app bundle. | `docs/PRD.md` NFR-030 and Section 12.8; `docs/SPEC.md` Section 19.4 |
> | Source-completeness state | Required instruction-root assets may be incomplete in the current source or packaging state; this remains a P0 readiness gate. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OI-004; `docs/PRD.md` Section 10.1 |
> | PRD source status | `MATCH` treated as source status for this run. | `_REFERENCES.md` REF-006; assignment override — reconciled under D-APP-38 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Build platform prerequisites | Node.js `>=20`; dependencies installed in `frontend/` with `npm ci` before validation/package sequence. | `docs/PRD.md` Section 6.2 and CI sequence near Section 12.2 |
> | Release scope exclusions | Windows/Linux packaging is out of current release scope unless amended. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-078; `docs/PRD.md` KG-014 |
> | Signing posture | Unsigned/adhoc as scoped; no notarization requirement in current target. | `docs/PRD.md` Sections 6.2 and 7.12; `docs/SPEC.md` Section 19.4 |
> | Network/security posture during packaged validation | current shipped Anthropic network guardrails remain in force. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
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
> - verify SDK subprocess/binary executability from the package layout; and
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
> This deliverable covers the macOS arm64 unsigned DMG packaging path and the packaging evidence needed to prove instruction-root asset integrity and SDK subprocess package executability for Chirality App vNext.
>
> In scope:
>
> - `frontend/` local packaging command `npm run desktop:dist`.
> - `frontend/` app-directory packaging command `npm run desktop:pack`, which is
>   the layout exercised by the packaged probes and D-APP-18 live proof.
> - DMG output verification for macOS 15+ Apple Silicon.
> - App bundle instruction-root asset inclusion and integrity verification.
> - SDK subprocess/binary package-layout probe.
> - Integrity summary evidence.
>
> Out of scope:
>
> - Windows/Linux packaging, unless a governed amendment reopens it.
> - Feature implementation unrelated to packaging glue, integrity checks, or package-layout probes.
> - Signing/notarization beyond the current unsigned/adhoc local-builder posture.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-09-04-REQ-001 | The release target must remain macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG unless amended. | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 | Inspect app bundle architecture, `LSMinimumSystemVersion`, and signing posture. |
> | DEL-09-04-REQ-002 | The desktop distribution build must be produced through `npm run desktop:dist` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` FR-067 | Run or review build evidence for `npm run desktop:dist`. |
> | DEL-09-04-REQ-003 | The expected DMG output must include `frontend/dist/Chirality-0.1.0-arm64.dmg`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 7.12 | Confirm file exists after packaging. |
> | DEL-09-04-REQ-004 | The expected app bundle output must include `frontend/dist/mac-arm64/Chirality.app`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm app bundle exists after packaging. |
> | DEL-09-04-REQ-005 | The build/integrity flow must produce or preserve `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`, and packaging evidence must state either a passing integrity verdict or enumerated blockers. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 | Confirm summary JSON exists and records a passing integrity result, or record blocker. |
> | DEL-09-04-REQ-006 | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` K-PACKAGE-1; `docs/SPEC.md` Section 1.1 | Run/review `npm run instruction-root:integrity` and bundle resource inspection. |
> | DEL-09-04-REQ-007 | Missing required instruction-root assets are a P0 packaging and runtime-readiness blocker. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1; decomposition OI-004 | Fail packaging readiness if required assets are absent, or document accepted amendment. |
> | DEL-09-04-REQ-008 | The package-layout evidence must verify that the SDK subprocess/binary can be found and executed from the app bundle/package layout without secret leakage or broader network policy. | `docs/PRD.md` NFR-030; `docs/PRD.md` KG-025; `docs/SPEC.md` Section 19.4 | Execute SDK subprocess packaging probe in packaged layout; record command, package path, expected result, observed result, and blocker state. |
> | DEL-09-04-REQ-009 | The packaged validation must preserve current shipped Anthropic network guardrails. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 | Run/review network guardrail checks or document blocker. |
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
> | DMG artifact check | file listing or checksum for `frontend/dist/Chirality-0.1.0-arm64.dmg` | DEL-09-04-REQ-001, DEL-09-04-REQ-003 |
> | App bundle check | file listing for `frontend/dist/mac-arm64/Chirality.app` | DEL-09-04-REQ-004 |
> | Minimum macOS version check | inspected `LSMinimumSystemVersion` value `15.0.0` or later | DEL-09-04-REQ-001 |
> | Architecture check | inspected arm64 binary architecture | DEL-09-04-REQ-001 |
> | Signing posture check | evidence that signing is unsigned/adhoc as scoped | DEL-09-04-REQ-001 |
> | Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` with explicit pass verdict or enumerated blockers | DEL-09-04-REQ-005, DEL-09-04-REQ-006, DEL-09-04-REQ-007 |
> | SDK subprocess packaging probe | package-layout probe command, package path, expected result, observed result, and failure/blocker recording rule for SDK subprocess/binary | DEL-09-04-REQ-008 |
> | Network guardrail check | evidence current shipped Anthropic network policy remains active | DEL-09-04-REQ-009 |
>
> Packaging evidence is not acceptable when instruction-root assets are absent, the integrity summary reports failure, or the SDK subprocess package-layout probe fails. Those cases remain blockers unless a governed amendment accepts a different release target or integrity policy.
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - `desktop:dist` command transcript or equivalent run record.
> - DMG and app bundle artifact listing plus checksum or deterministic artifact identifier for the DMG.
> - Instruction-root integrity summary with pass/blocker verdict.
> - SDK subprocess packaging probe command and result.
> - Audit-ready evidence bundle pointers to command transcript, artifact listing/checksum, summary JSON, first-adapter probe output, network guardrail evidence, and residual blockers.
> - `TBD` residual-blocker list for incomplete instruction-root assets, SDK package-layout failures, or unresolved packaged-app runtime guardrail scope.
> - `ASSUMPTION` or `PROPOSAL` entries for any packaging config interpretation not directly supported by source evidence.

- **AC-001** — The desktop distribution and app-directory packaging evidence identifies the expected DMG and app bundle, verifies arm64 architecture, minimum macOS 15.0.0, unsigned or adhoc posture, required instruction-root assets and passing integrity summary, an executable SDK subprocess in package layout, and preserved current shipped Anthropic network guardrails; missing assets, failed integrity, failed subprocess execution, or unresolved required evidence remain explicit blockers.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-014 — Purpose

> ##### Purpose
>
> Define the operational steps to produce the macOS arm64 unsigned DMG and assemble evidence that instruction-root resources and SDK subprocess packaging posture are valid for the packaged app.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> - ResponsibleParty: TBD.
> - Work from `frontend/` for local validation and packaging commands.
> - Node.js `>=20` is available.
> - Dependencies have been installed with `npm ci`.
> - Required instruction-root assets are present or missing assets are tracked as blockers.
> - Dependency state: `Dependencies.csv` v3.1 currently contains 9 ACTIVE rows; six rows remain `SatisfactionStatus=TBD`, so dependency closure remains open until accepted evidence resolves them.
> - Evidence bundle custody: ResponsibleParty remains TBD; until assigned, route release evidence bundle ownership through the package owner or human-appointed release reviewer.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Confirm release target remains macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG.
> 2. From `frontend/`, run required pre-packaging checks or confirm accepted evidence already exists. Non-run evidence is acceptable only when it identifies the command, source run or artifact, timestamp/version, pass verdict, and any blockers:
>    - `npm run test`
>    - `npm run typecheck`
>    - `npm run harness:validate:premerge`
>    - `npm run instruction-root:integrity`
> 3. If `instruction-root:integrity` reports missing required assets, stop packaging-evidence acceptance and record the missing assets as P0 blockers.
> 4. From `frontend/`, run `npm run desktop:dist`.
> 5. Confirm expected packaging outputs:
>    - `frontend/dist/Chirality-0.1.0-arm64.dmg`
>    - `frontend/dist/mac-arm64/Chirality.app`
>    - `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`
> 6. Inspect the packaged app for macOS release posture:
>    - binary is `arm64`;
>    - `LSMinimumSystemVersion` is `15.0.0` or later;
>    - signing posture is unsigned/adhoc as scoped.
> 7. Inspect packaged resources for required instruction-root assets.
> 8. Run or review the SDK subprocess packaging probe:
>    - record the probe command, package path, expected result, observed result, and evidence path;
>    - verify the SDK subprocess/bundled binary can be found from package layout;
>    - verify it is not trapped inside `app.asar` without execution access;
>    - verify execution does not require secret leakage or broader network policy.
> 9. Confirm packaged app preserves packaging-relevant runtime guardrails:
>    - working-root selector is available;
>    - current shipped Anthropic network guardrails remain in force;
>    - `TBD`: human/source ruling must decide whether SDK-backed turn start after R1 blocks DEL-09-04 closure or is deferred to a broader packaged-app validation workflow.
> 10. Record all command outputs, artifact paths, summary JSON, probe output, checksums or deterministic artifact identifiers, and residual blockers in the integrity/package evidence bundle.
>

### CLM-017 — Verification

> ##### Verification
>
> | Check | Pass Criteria | Requirement Link |
> |---|---|---|
> | Local checks | Required commands exit zero or accepted evidence explains non-run state. | DEL-09-04-REQ-002, DEL-09-04-REQ-006 |
> | DMG artifact | `frontend/dist/Chirality-0.1.0-arm64.dmg` exists after `desktop:dist`. | DEL-09-04-REQ-003 |
> | App bundle artifact | `frontend/dist/mac-arm64/Chirality.app` exists after `desktop:dist`. | DEL-09-04-REQ-004 |
> | Integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists and states a pass verdict, or all failed/missing assets are enumerated as blockers. | DEL-09-04-REQ-005, DEL-09-04-REQ-007 |
> | macOS target | Binary architecture is arm64 and minimum macOS target is `15.0.0` or later. | DEL-09-04-REQ-001 |
> | Signing posture | Codesign evidence matches unsigned/adhoc local-builder scope. | DEL-09-04-REQ-001 |
> | SDK subprocess | Packaged SDK subprocess/binary probe records command, package path, expected result, observed result, and shows the binary is locatable and executable from app bundle/package layout. | DEL-09-04-REQ-008 |
> | Network guardrails | Packaged validation preserves current shipped Anthropic network policy. | DEL-09-04-REQ-009 |
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
> | DMG artifact identity | `frontend/dist/Chirality-0.1.0-arm64.dmg` listing plus checksum or deterministic artifact identifier. |
> | App bundle artifact identity | `frontend/dist/mac-arm64/Chirality.app` listing and inspected release posture. |
> | Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` with pass verdict or blocker list. |
> | SDK subprocess packaging probe | Probe command, package path, expected result, observed result, output path, and blocker state if failed. |
> | Manual package verification notes | Architecture, minimum OS, signing posture, resource inclusion, working-root selector, network policy, and SDK packaged execution scope. |
> | Evidence bundle custody | ResponsibleParty or routing placeholder; currently `TBD` until human assignment. |
> | Blocker list | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |

- **VER-001** — Run or review the accepted pre-packaging checks, desktop:dist and desktop:pack evidence; inspect DMG and app-bundle identities, architecture, minimum OS, signing posture, packaged resources, integrity summary, SDK subprocess probe, network guardrails, and residual blocker records.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> #### Guidance: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-020 — Purpose

> ##### Purpose
>
> This deliverable makes release packaging explicit and repeatable for the current macOS-only target. Its job is not just to produce a DMG, but to prove that packaged Chirality preserves the instruction-root resource boundary and can execute the SDK subprocess/binary from the packaged layout.
>

### CLM-021 — Principles

> ##### Principles
>
> - Treat `desktop:dist` as release-significant. `docs/CONTRACT.md` K-VALIDATE-1 includes `desktop:dist` among checks required before release-significant changes are accepted.
> - Keep the release target narrow. `docs/PRD.md` KG-014 and decomposition SOW-078 make Windows/Linux packaging out of scope without amendment.
> - Treat instruction-root resources as package blockers. `docs/SPEC.md` Section 1.1 says missing required instruction-root assets are a P0 packaging and runtime-readiness blocker.
> - Preserve Chirality-owned boundaries in packaged form. Packaged validation should still exercise instruction-root integrity, working-root availability, current shipped Anthropic network guardrails, and SDK package execution.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-022 — Considerations

> ##### Considerations
>
> - The instruction-root required asset set includes `AGENTS.md`, `README.md`, `agents/`, `docs/`, core docs, and root-level assets where packaging/integrity policy requires them. If the code-level integrity manifest differs from this list, record the difference as a conflict or source-completeness blocker rather than silently passing packaging readiness.
> - SDK subprocess packaging is an empirical check. `docs/PRD.md` KG-025 flags potential needs such as `asarUnpack`, signing, environment, or path adjustments; the accepted result must come from a probe or build evidence, not from configuration review alone.
> - The integrity summary path is part of expected packaging evidence: `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
> - The unsigned/adhoc local-builder DMG posture is acceptable only because `docs/CONTRACT.md` K-RELEASE-1 and `docs/PRD.md` Section 6.2 define that as the current release target. A notarized distribution target would require scope amendment rather than silent tightening of this deliverable.
> - Release evidence should be reviewable without rerunning the build: command transcript, artifact listing or checksum, integrity summary, first-adapter probe output, and blocker list need stable paths or attachment identifiers.
> - `ASSUMPTION: PACKAGE_HEURISTIC` associates OBJ-008 because the decomposition maps this deliverable through PKG-09 and SOW-072/SOW-073, but no human has assigned a hard objective-specific owner.
>

### CLM-023 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Strict asset completeness vs. build progress | Prefer failing readiness with a documented blocker when required instruction-root assets are absent. Do not weaken integrity requirements without a governed amendment. |
> | `app.asar` packing convenience vs. SDK executable access | Prefer package layout that allows the SDK subprocess/binary to be found and executed. If `asar` trapping prevents execution, record the packaging probe failure and adjust packaging under this deliverable. |
> | Local unsigned DMG vs. notarized distribution | Keep unsigned/adhoc posture for current scope. Notarization is outside this deliverable unless scope changes. |
> | General release checklist vs. DEL-09-04 scope | Keep CI artifact upload and broader release workflow details in DEL-09-05 unless directly needed to prove the DMG/instruction-root/SDK packaging result. |
>

### CLM-024 — Examples

> ##### Examples
>
> TBD: No source-backed example transcript or accepted packaging probe output is available in the local reference corpus for this deliverable.
>

### CLM-025 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | DEL-09-04-CONF-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | Assignment override | All PRD-backed requirements | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | TBD — reconciled under D-APP-38 |
> | DEL-09-04-CONF-002 | Required instruction-root assets may be incomplete in current source or package state. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1 | Decomposition OI-004 | Specification requirements, Procedure verification | Treat missing assets as P0 readiness blocker until completed or amended. | TBD |
> | DEL-09-04-CONF-003 | The accepted authority for the required instruction-root packaged asset set must be explicit when code-level integrity manifests differ from policy-level required assets. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` FR-058 | Code-level integrity manifest, location TBD | Specification requirements, Procedure verification | Treat policy-level required assets as readiness blockers unless a governed amendment narrows the manifest. | TBD |
> | DEL-09-04-CONF-004 | Whether SDK-backed turn start after R1 is a DEL-09-04 closure blocker or deferred packaged-app validation needs human/source ruling. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 | `_CONTEXT.md` deliverable scope | Procedure packaged runtime guardrail check | Keep SDK subprocess/package-layout proof in scope; mark full packaged SDK-backed turn start as `TBD` until owner ruling. | TBD |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-030 SOW-072 SOW-073 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
