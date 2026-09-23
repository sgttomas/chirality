---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-06
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-019, SOW-020, SOW-022, SOW-023]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-06

## Current Codex MVP conformity

Codex is the sole MVP engine. Under D-GOV-43 topology A2 and D-APP-127, the App owns its Runtime service child and Runtime owns the stock Codex App Server child. Hosted supplier admission, per-root account consent, the LaunchAgent, packaged-basis hashing and supplier-containment evidence are retired subjects; they are not present-day qualification gates.

The App must preserve Codex-held credential custody and separation from other Codex clients, user-selected approval and sandbox policy, truthful event/approval presentation, and applicable renderer, attachment, secret-protection and package-executability controls. Historical Anthropic/Claude/Pi descriptions remain compatibility evidence and do not qualify the live Codex path.

The accepted S0/default-app PDF fallback remains the current MVP basis; S1 built-in multi-page PDF criteria remain inapplicable to this release. Applicable attachment budgets, containment, nonce/window/IPC, renderer-egress and packaged default-app observations remain required. No native PASS is inferred from source tests.

Verification hooks: `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md` in the same folder, plus `frontend/package.json` registered packaging/security commands. These procedures supersede the retired Stage 9–13 spine; repeat affected checks when source, configuration or packaging changes invalidate earlier evidence. No publication or product acceptance follows from this text repair.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-06` in service of project scope [SOW-019, SOW-020, SOW-022, SOW-023] and package objectives [OBJ-008].

- **OUT-001** — A security-control evidence set covering renderer network restrictions, the accepted fixed update-metadata request, Codex-custodied private authentication and credential non-disclosure, structural secret redaction, attachment validation and budgets, partial and total attachment failure behavior, retry preservation, and repeatable security-significant validation. Include the D121 bounded built-in PDF renderer-policy security evidence set; existing attachment budgets are unchanged.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Datasheet: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-06 |
> | DeliverableName | Network, Key, Attachment, and Renderer Security Checks |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | SECURITY_CONTROL |
> | ContextEnvelope | M |
> | ResponsibleParty | TBD |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary scope | Verify renderer restrictions, current Codex credential custody and non-disclosure, structural secret redaction, accepted network exceptions, and attachment validation/retry behavior. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |
> | Covered SOW items | SOW-019, SOW-020, SOW-022, SOW-023 | `_CONTEXT.md` Traceability; decomposition DEL-09-06 |
> | Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition objective mapping |
> | Anticipated artifacts | Security tests; network guard tests; attachment resolver validation; Codex custody and App secret-exclusion checks | `_CONTEXT.md` Anticipated Artifacts |
> | API key resolution order | Codex owns current sign-in/out and credential custody; App must not read, copy or relay credentials. The safeStorage/Anthropic precedence chain is retained compatibility history. | `docs/PRD.md` Section 8.5, FR-030 |
> | API key storage path | Chirality-private auth.json in the effective Codex home, custodied by Codex under D-GOV-43/D-APP-127; the App-held api-key.enc path is legacy. | `docs/SPEC.md` Section 16.2 |
> | Allowed Anthropic base URL | Anthropic endpoint validation is retained legacy evidence; current Codex transports follow the accepted K-NET-1 scope and user configuration. | `docs/PRD.md` Section 8.5, FR-032 |
> | Renderer network allowlist | Renderer restrictions remain enforced; distinguish loopback App transport, Codex-owned outbound execution and the accepted update-metadata request. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
> | Supported attachment extensions | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, `.csv` | `docs/SPEC.md` Section 16.1 |
> | Attachment size limits | 10 MB per file; 18 MB total raw bytes per turn. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-038 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source warning | REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes. | Assignment instruction; `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Pass 3 source-state disposition | B-001 preserves REF-006 as warning-only source tension for all PRD-grounded security checks until a later human/source ruling records otherwise. | `_REFERENCES.md` REF-006; `Guidance.md` Conflict Table |
> | Security posture | API keys are non-project convenience state and must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` NFR-002 |
> | Attachment trust boundary | Client attachment metadata is non-authoritative; server revalidates attachment properties. | `docs/PRD.md` Section 8.6, FR-037; `docs/CONTRACT.md` K-ATTACH-1 |
> | Failure handling | Partial attachment failure is non-fatal when executable content remains; all attachments failing with empty text returns `ATTACHMENT_FAILURE`. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-040 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected Check Coverage | Source |
> |---|---|---|
> | Renderer network guard | Tests showing renderer requests obey current K-NET-1 and packaged renderer containment; policy metadata excludes secrets. The fixed unauthenticated release-metadata check is separately bounded and does not grant arbitrary renderer or Codex transport access. | `docs/PRD.md` FR-033; `docs/PRD.md` NFR-003 |
> | Execution and update network boundary | Verify Codex owns user-configured execution transports; verify the App update check uses only its fixed unauthenticated metadata endpoint, refuses credentials/redirects, and requires explicit verified browser handoff. Anthropic base-URL variants are historical compatibility evidence. | `docs/CONTRACT.md` K-NET-1; D-GOV-43/D-APP-127 |
> | Credential custody and non-disclosure | Verify Chirality-private Codex authentication, no App credential read/copy/relay, no credential material in project files, logs, events or artifacts, and structural redaction at actual sinks. App safeStorage precedence and environment handoff tests remain historical compatibility evidence. | D-GOV-43/D-APP-127; `docs/CONTRACT.md` K-KEY-1; current S-8 checks |
> | Attachment resolver | Tests for path validation, regular-file check, symlink rejection, extension allowlist, readability, and byte budgets. | `docs/SPEC.md` Section 16.1 |
> | Retry behavior | Tests showing UI preserves draft/attachments after failed send where source scope requires retry preservation. | `docs/PRD.md` FR-040 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Path | Status | Use |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` | historical D-APP-38 source state; verify current candidate bytes | Invariants K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
> | REF-003 | `docs/SPEC.md` | historical D-APP-38 source state; verify current candidate bytes | Section 16 attachment, API key, and network policy mechanics |
> | REF-005 | `docs/PLAN.md` | historical D-APP-38 source state; verify current candidate bytes | Implementation sequencing context for key handoff and validation |
> | REF-006 | `docs/PRD.md` | historical D-APP-38 source state; verify current candidate bytes status | Product requirements FR-030 through FR-040 and NFR security/privacy requirements — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | accessible | DEL-09-06 scope and SOW/objective mapping |
>

### CLM-007 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | B-001 | Incorporated as an explicit warning-only source-state condition; no PRD-derived value was promoted beyond the existing REF-006 warning. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Specification: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable defines validation checks for the security-sensitive surfaces named by DEL-09-06: renderer outbound network allowlisting, Codex credential custody/redaction, current K-NET-1 transport policy, and attachment validation/retry behavior.
>
> In scope:
>
> - Security tests and network guard tests for renderer and provider policy.
> - Attachment resolver validation for server-side file checks and failure behavior.
> - Codex custody and redaction checks proving credential material remains private non-project state.
> - Evidence sufficient to support PKG-09 security validation without a release-readiness claim.
>
> Out of scope:
>
> - Feature implementation except test fixtures and packaging glue, per PKG-09 package exclusions.
> - Independent App marketplace/plugin engines or new App network transports without their owning scope. Codex-native MCP/plugins/resources follow shared user configuration and selected policy under D-GOV-43.
> - Assignment of `ResponsibleParty`; it remains `TBD`.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-09-06-REQ-001 | Current credential checks shall verify Codex-held sign-in/out and Chirality-private custody without App read/copy/relay; S-8 verifies other Codex clients remain unaffected. Legacy key precedence is compatibility evidence. | Current account-route/renderer non-disclosure fixtures and native S-8 client-isolation result; old key precedence tests remain historical. |
> | DEL-09-06-REQ-002 | Key material shall not be written to working root, project docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts. | Redaction/storage tests and fixture scan. |
> | DEL-09-06-REQ-003 | Credentials shall be custodied by Codex in the effective Chirality-private home; App code must not read, copy or relay them. Verify the configured file backend and client isolation through S-8. | Current Codex account/custody integration fixture and S-8 other-client isolation evidence without credential inspection. |
> | DEL-09-06-REQ-004 | Current network checks shall verify accepted Codex transports and user-selected policy. Anthropic base-URL tests remain legacy evidence and cannot qualify the live Codex path. | Current K-NET-1 App transport/update restrictions and actual user-selected Codex request/policy witnesses, labelled by surface. |
> | DEL-09-06-REQ-005 | Renderer outbound traffic shall obey its accepted loopback/explicit transport restrictions independently of Codex-owned outbound execution; verify actual denial and secret-safe logging. | Renderer network guard tests using `webRequest.onBeforeRequest` behavior or equivalent test seam. |
> | DEL-09-06-REQ-006 | Renderer network policy logs shall include policy metadata without secrets. | Network guard log redaction assertions. |
> | DEL-09-06-REQ-007 | App-owned service/update transports shall stay within current K-NET-1; Codex command transport honors the user-selected configuration and actual sandbox without a retired App provider allowlist. | App transport boundary fixtures and current Codex policy/request witnesses; SDK handoff assertions are compatibility-only. |
> | DEL-09-06-REQ-008 | Attachment validation shall treat client metadata as non-authoritative and revalidate path, extension, file type, readability, symlink status, regular-file status, and size. | Attachment resolver validation tests. |
> | DEL-09-06-REQ-009 | Attachment resolver checks shall reject symlinks, directories, special files, unsupported extensions, unreadable files, files over 10 MB, and turns over 18 MB raw bytes. | Resolver negative-case fixtures. |
> | DEL-09-06-REQ-010 | Supported attachment extensions shall include `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, and `.csv`. | Resolver allowlist tests. |
> | DEL-09-06-REQ-011 | The live Codex path shall reject an invalid attachment set before model submission. Partial attachment continuation remains compatibility behavior on the retained legacy path. | Route or resolver integration tests. |
> | DEL-09-06-REQ-012 | Live attachment rejection shall preserve a useful failure result and user draft/attachments; INVALID_REQUEST is current source evidence. The legacy ATTACHMENT_FAILURE name does not define the native response. | Route or resolver integration tests. |
> | DEL-09-06-REQ-013 | UI-facing retry behavior shall preserve draft and attachments on failed send where attachment failure recovery is exercised. | UI or integration retry-preservation tests. |
> | DEL-09-06-REQ-014 | Required local checks must remain explicit and repeatable before security-significant evidence acceptance. | CI/premerge validation evidence. |
> | DEL-09-06-REQ-015 | Security evidence shall record actual candidate-bound results from applicable test, typecheck, premerge, instruction-root:integrity and desktop:dist commands; named hooks alone do not establish execution. | Command output or CI artifact references tied to the selected implementation targets. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Source | Applicability | Location |
> |---|---|---|
> | Product PRD security requirements | Governs FR-030 through FR-040 and NFR-002 through NFR-004. | `docs/PRD.md` Sections 8.5, 8.6, 11.1; historical D-APP-38 source state; verify current candidate bytes status applies — reconciled under D-APP-38 |
> | Runtime/API specification | Governs attachment, key, and network mechanics. | `docs/SPEC.md` Section 16 |
> | Contract invariants | Governs security invariants for network, keys, attachments, and validation. | `docs/CONTRACT.md` K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
> | SOFTWARE_DECOMP v3.2 | Defines deliverable scope and SOW/objective mapping. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach | Evidence Artifact |
> |---|---|---|
> | REQ-001, REQ-002, REQ-003 | Verify Codex custody, no App credential read/copy/relay, other-client isolation and secret-safe sinks; S-8 is the production-path hook. Legacy key precedence/safeStorage fixtures are compatibility evidence. | Key storage checks; redaction fixtures |
> | Current secret-field families | Run synthetic-secret fixtures for account, approval, thread, policy and tool-activity fields at each App/Runtime event, log, artifact and renderer sink; record candidate, fixture bytes, result and unavailable sinks. | Candidate-bound sink matrix; missing results remain open |
> | REQ-004, REQ-007 | Verify current K-NET-1 transports and user-selected Codex policy, separately from renderer restrictions; legacy base-URL fixtures do not qualify current endpoints. | Provider endpoint policy tests |
> | REQ-005, REQ-006 | Electron network guard tests for allowed and denied URLs plus secret-free policy logs. | Network guard tests |
> | REQ-008, REQ-009, REQ-010 | Attachment resolver tests covering positive and negative file cases. | Attachment resolver validation |
> | REQ-011, REQ-012, REQ-013 | Verify live whole-set rejection and draft/attachment retry preservation. Partial/total continuation remains a legacy-only fixture subject. | Attachment retry/failure tests |
> | REQ-014, REQ-015 | Record candidate-bound results from the named CLM-017 hooks and registered checks, including post-A2 packaged evidence or HOST_RERUN_REQUIRED. | Premerge validation evidence; exact test file paths, package-script aliases, and artifact paths `TBD` |
>

### CLM-013 — Documentation

> Use the accepted requirement and verification contract in CLM-017 and frontend/src/__tests__/electron/renderer-window-policy.test.ts. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit gaps against governing scope and any selected graph. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-014 — Pass 3 Disposition Notes

> Earlier Pass 3 path slots describe drafting history. Current hooks are named in CLM-017; actual candidate outputs remain unrun. Apply Codex custody and whole-set attachment validation to the live path. Retained safeStorage/provider and partial-failure tests are compatibility evidence. D121 S1 inline-PDF feasibility remains deferred; S0/default-app behavior and existing renderer/IPC/CSP controls remain current.

- **AC-001** — Evidence verifies current Codex credential custody and secrecy, accepted K-NET-1 network boundaries, renderer/IPC/CSP protections and secret-free logs, server-authoritative native selection/containment/type/symlink/readability/byte-budget checks, whole-set rejection before dispatch and preserved retry state. Retained provider/key-store behaviors are labelled compatibility. Require actual candidate-bound unit/integration and applicable packaged S-8/S0 results; missing outputs remain open. D121 S1 inline-PDF work is deferred under D-APP-127 and is not a current MVP release prerequisite.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Procedure: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>

### CLM-016 — Purpose

> ##### Purpose
>
> Produce and verify the DEL-09-06 security-control evidence set for renderer network allowlisting, API key storage/redaction, provider endpoint policy, and attachment validation/retry behavior.
>

### CLM-017 — Prerequisites

> Prerequisites are the current source/dependency basis, actual Runtime/Codex binding and candidate package where native checks apply. Existing hook families are frontend attachment, renderer/network, IPC sender, retry and security-script tests; production-path custody is S-8 in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`. Retained safeStorage/Anthropic tests are compatibility evidence. Record actual command outputs and blockers; names are selected, not future TBD slots. The discovery snapshot had 11 ACTIVE dependency rows; current counts and reviewed retirements are recorded in Dependencies.csv and the current dependency audit, without rewriting that history. ResponsibleParty remains human-owned.

### CLM-018 — Steps

> 1. Verify source and candidate identity under D-APP-38. Preserve mismatch or bypass evidence; do not infer current MATCH from the historical authoring run. Scope remains SOW-019, SOW-020, SOW-022 and SOW-023.
> 2. Map live Runtime/Codex credential custody, native selection and attachment resolution, renderer/IPC/network controls and retry behavior to the named tests in CLM-017. Record a missing hook or production binding as an explicit gap.
> 3. Verify credential secrecy across project files, durable events, logs, support bundles and tool artifacts; verify App does not read, copy or relay Codex credentials. Check typed non-destructive authentication failures on the applicable path. The older UI safeStorage/environment-precedence checks qualify only retained compatibility.
> 4. Check K-NET-1 separately for App loopback transport, Codex-owned endpoints and command network under the user-selected policy. Check fixed unauthenticated release metadata GET on manual/startup/six-hour triggers, rejecting redirects/credentials and unverified browser destinations; DEL09-05 owns update maintenance and DEL02-01 presentation. Retained Anthropic endpoint rules do not constrain Codex provider choice or create a generic network exception.
> 5. Verify actual renderer denials, trusted IPC sender/origin checks and secret-free diagnostics; native command-policy results do not replace renderer controls.
> 6. Exercise native picker copying into the captured project and Runtime root validation before reads. Validate supported png/jpg/jpeg/gif/webp/pdf/txt/md/csv, regular-file status, symlink rejection, type/readability, 10 MB per-file and 18 MB aggregate raw-byte limits. Reject external Runtime inputs, special files, unsupported or over-budget inputs before dispatch. Native selection grants no new source-directory or Codex permission.
> 7. Verify entire-set validation before Codex dispatch: any invalid attachment rejects the request and preserves draft/selections for correction. Retained provider partial-failure/ATTACHMENT_FAILURE checks remain separately labelled compatibility.
> 8. Run affected unit/API/integration and packaged checks, including applicable npm test/typecheck, harness:validate:premerge, instruction-root:integrity and desktop:dist. Record candidate, command, result and artifact paths; absent native S-8 results remain blockers. Apply S0/default-app PDF checks; deferred D121 S1 is not a current MVP prerequisite.

### CLM-019 — Verification

> ##### Verification
>
> | Check | Pass Criteria | Source |
> |---|---|---|
> | API key precedence | Legacy compatibility only: UI safeStorage, then ANTHROPIC_API_KEY, then CHIRALITY_ANTHROPIC_API_KEY. Live path verifies Codex custody and no App credential copy/relay. | `docs/PRD.md` FR-030 |
> | API key secrecy | Key material absent from project files, logs, runtime events, and tool artifacts. | `docs/PRD.md` FR-031; `docs/CONTRACT.md` K-KEY-1 |
> | Base URL allowlist | Legacy compatibility only: accepted Anthropic URL form; live Codex endpoints and bounded update metadata follow current K-NET-1. | `docs/PRD.md` FR-032 |
> | Renderer network allowlist | Renderer restrictions remain enforced; distinguish loopback App transport, Codex-owned outbound execution and the accepted update-metadata request. | `docs/PRD.md` FR-033; `docs/SPEC.md` Section 16.3 |
> | Attachment validation | Server revalidates client metadata and rejects unsupported or unsafe files. | `docs/PRD.md` FR-037; `docs/SPEC.md` Section 16.1 |
> | Attachment budgets | 10 MB per file and 18 MB per turn raw-byte limits enforced. | `docs/SPEC.md` Section 16.1 |
> | Attachment failure handling | Live Codex path rejects any invalid selected attachment before dispatch and preserves draft/selections; partial/total-failure behavior is retained provider compatibility. | `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1 |
>

### CLM-020 — Records

> Use the accepted requirement and verification contract in CLM-017 and frontend/src/__tests__/electron/renderer-window-policy.test.ts. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit gaps against governing scope and any selected graph. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-021 — Pass 3 Disposition Notes

> Earlier F-001 path-selection and X-001 output-location slots are historical. CLM-017 names current verification hooks; actual candidate output artifacts must be recorded after execution. Current custody, network and attachment verification follows CLM-018/019. Missing post-A2/native evidence remains open, without reviving deferred D121 S1 as a release prerequisite.

- **VER-001** — Execute the named current custody/redaction, renderer/network/IPC, attachment selection/containment/budget/whole-set rejection and retry tests, then applicable packaged S-8/S0 checks. Record actual candidate, source/fixture identities, command outputs and gaps. Keep legacy provider partial-failure and key-precedence results separately labelled; do not claim deferred D121 S1 or unrun native proof.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Guidance: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable exists to keep validation, packaging, network, key, and instruction-root checks explicit and repeatable for PKG-09 security evidence. Its security checks should demonstrate that key material remains outside project truth, renderer/network access is bounded, provider endpoint selection is constrained, and attachment handling does not rely on client-supplied metadata.
>
> Sources: `_CONTEXT.md` Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OBJ-008 and DEL-09-06.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Runtime code is the security boundary. Prompts and documentation can reinforce policy, but tests should target runtime behavior such as path containment, permission policy, hooks, redaction, and network controls.
>    Source: `docs/PRD.md` Section 4, principles 18-19.
>
> 2. API keys are convenience state, not project truth. Treat any write of key material to working root, runtime events, logs, git-tracked execution files, SDK transcripts if avoidable, or tool artifacts as a security-evidence blocker.
>    Source: `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031 and NFR-002.
>
> 3. Renderer and provider network checks should be allowlist-oriented. Current K-NET-1 enumerates App/Runtime loopback, Codex-owned endpoints and the bounded update metadata check; command network follows the user-selected Codex policy.
>    Source: `docs/CONTRACT.md` K-NET-1; `docs/SPEC.md` Section 16.3.
>
> 4. Codex-owned execution and renderer restrictions are separate surfaces; actual renderer denials do not prove native Codex network policy, and native policy does not replace renderer restrictions.
>    Source: `docs/PRD.md` FR-032 and FR-033; `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1.
>
> 5. Attachment metadata from the browser is advisory only. Server-side validation must be the authority for path, type, symlink status, readability, regular-file status, and byte budgets.
>    Source: `docs/PRD.md` FR-037; `docs/CONTRACT.md` K-ATTACH-1.
>
> 6. Failure behavior is part of the security surface. Tests must verify whole-set attachment rejection on the live Codex path and preserved retry state; partial/all-failure continuation is retained compatibility under SPEC §16.1.
>    Source: `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1.
>

### CLM-025 — Considerations

> Use the accepted requirement and verification contract in CLM-017 and frontend/src/__tests__/electron/renderer-window-policy.test.ts. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit gaps against governing scope and any selected graph. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Topic | Trade-off | Guidance |
> |---|---|---|
> | Unit tests vs integration tests | Unit tests isolate policy logic; integration tests prove route/Electron behavior. | Use both where the surface crosses Electron, SDK provider, or route boundaries. |
> | Redaction assertions | Broad fixture scanning may produce false positives; narrow checks may miss variants. | Include representative key variants and verify both positive redaction and non-secret metadata retention. |
> | Attachment retries | UI retry behavior may sit outside the resolver. | Keep resolver validation separate from route/UI retry preservation so failures are easier to localize. |
> | Network policy | Codex-owned execution follows the selected user policy, while renderer traffic and update metadata remain bounded. | Test renderer, Codex command policy and bounded update transports separately; legacy provider tests remain compatibility. |
>

### CLM-027 — Examples

> | Example | Expected result | Source |
> |---|---|---|
> | Runtime receives an external or symlink attachment input | Reject before reading or dispatch; native picker uses contained project copies. | SPEC §16.1; K-ATTACH-1 |
> | One selected Codex attachment is invalid | Reject entire request and preserve draft/selections for correction. | SPEC §16.1 |
> | Update metadata URL redirects or includes credentials | Refuse; browser handoff requires an explicit act and a verified release destination. | K-NET-1 |
> | Renderer requests an undeclared destination | Deny and log without secrets; user-selected Codex command network is a separate boundary. | K-NET-1; SPEC §16.3 |
> | Legacy provider URL/partial-attachment fixtures | Preserve their compatibility expectations, explicitly excluded as proof of the live Codex path. | SPEC §16.1–16.3; D-GOV-43/D-APP-127 |

### CLM-028 — Conflict Table (for human ruling)

> The former key-custody/provider-endpoint and partial-failure questions are settled for the live path by D-GOV-43/D-APP-127 and SPEC §16.1: Codex custody, current transports and whole-set rejection apply; legacy modules remain compatibility evidence. S0/default-app PDF remains current; D121 S1 inline-PDF work is deferred and is not an MVP release prerequisite. Renderer/IPC/CSP, attachment budgets, retry and secret protections survive. Record absent post-A2 packaged evidence explicitly. D-APP-127’s affected-check rule replaces A1 re-stage; a relevant source, configuration or package change triggers only the affected rerun.

### CLM-029 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | E-001 | Current rationale distinguishes Codex-owned execution, renderer restrictions and bounded update metadata; earlier Anthropic endpoint checks are compatibility history. |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 SOW-020 SOW-022 SOW-023 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R085:** Synthetic-secret fixtures must cover account, approval, thread, policy and tool-activity fields at each current App/Runtime event, log, artifact and renderer sink, with explicit unavailable-sink results.

- **APP-R086:** D-APP-121 A-design/A-proof leaves isolated unpublished PDF proof, observability and the S0 release boundary in force. No PDF publication or product acceptance follows from documentary alignment.
