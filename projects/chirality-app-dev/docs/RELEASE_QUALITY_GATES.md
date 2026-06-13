# RELEASE QUALITY GATES - Chirality App Dev

**Status:** Draft governance support surface
**Date:** 2026-06-13
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** release-significant app-dev changes, validation evidence, packaging evidence, and release-quality review

## 1. Purpose

This checklist routes app-dev changes through release-quality evidence gates. It complements `docs/VALIDATION_STRATEGY.md`, `docs/BUILD_AND_RELEASE.md`, and the invariants in `docs/CONTRACT.md`.

These gates define evidence to collect or explicitly waive before a release-significant change is accepted. They do not publish a release, approve lifecycle issuance, certify professional work, seal or authenticate work product, declare code compliance, or authorize external distribution.

## 2. Gate Routing

Run every release-significant change through all applicable gate families.

| Change type | Gate family | Examples |
|---|---|---|
| Coordination policy, completion plans, decision-register pointers, docs-only governance | Governance gate | `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, active plan/log, quality docs |
| Runtime contract, adapter boundary, turn lifecycle, session events, event schemas | Runtime contract gate | `AgentEnginePort`, `TurnEngine`, `SessionEvents`, `HarnessEvent`, SDK mapper |
| SDK options, permissions, tools, hooks, MCP, path policy | Permission/tool gate | `sdk-options-builder`, tool descriptors, permission overlay, read MCP, write hooks |
| API routes, harness workflow, running-app validation, attachments, interrupt behavior | Harness workflow gate | session boot, turn SSE, validation scripts, working-root APIs |
| Network, API key handling, redaction, provider policy | Security and network gate | Electron network guardrails, key storage, Anthropic policy, redaction helpers |
| UI workflow, product identity, professional-boundary copy | UI and claims gate | navigation, dense professional UI, copy that distinguishes drafts from approvals |
| Instruction-root resources, Electron build, package metadata, DMG output | Packaging gate | `desktop:pack`, `desktop:dist`, extra resources, integrity verification |
| Future domain-engine profiles, adapters, operation proposals | Domain-adapter gate | protected paths, proposal records, human gates, solver/domain truth boundaries |

Mixed changes run the union of applicable gates unless a human project authority records an explicit waiver and risk disposition.

## 3. Common Required Evidence

Every gate record or closeout summary should include:

- change identifier, scope, affected files, and owner/agent;
- commands run and pass/fail results;
- generated summary artifact path where a command emits one;
- skipped checks and the reason each was skipped;
- known limitations, unresolved `TBD` items, and human-ruling blockers;
- confirmation that runtime events, logs, plans, and completion logs are evidence/history only;
- confirmation that the work makes no release-readiness, professional-approval, certification, sealing, authentication, or code-compliance claim.

## 4. Governance Gate

Use this gate for docs-only governance, coordination, plan, and decision-register changes.

Required evidence:

- `git diff --check` over affected docs, plans, and coordination paths;
- targeted stale-reference searches for the rule or authority being replaced;
- existence checks for new relative links and referenced local paths;
- confirmation that `_DECISIONS/_REGISTER.md` remains the decision-tracking table when decision state is not being changed;
- confirmation that no runtime source, package manifest, or wrapper file changed when the tranche is governance-only.

Frontend tests are normally skipped for governance-only tranches. The closeout must say so explicitly.

## 5. Runtime Contract Gate

Use this gate for changes to the runtime engine contract, adapter boundary, turn lifecycle, persisted events, replay behavior, or session storage.

Required evidence:

- focused tests for the touched runtime modules;
- `npm run typecheck`;
- broader `npm run test` when shared event or route behavior changes;
- harness premerge validation when browser-facing session, SSE, or turn behavior changes;
- review that public/core Chirality contracts do not become SDK-shaped except as adapter metadata.

## 6. Permission And Tool Gate

Use this gate for SDK options, permission overlay, tool descriptors, tool exposure, hooks, MCP wrappers, path policy, or tool-result evidence.

Required evidence:

- tests for allow, deny, ask, and unknown-tool behavior where applicable;
- tests proving write/edit/bash/network/subagent capabilities remain denied until the active plan and human rulings authorize them;
- `npm run typecheck`;
- no new model-visible tool exposure without descriptor, permission, event, and validation coverage;
- no path write policy relaxation without human ruling and tests.

## 7. Harness Workflow Gate

Use this gate for session boot, turn execution, SSE streaming, interrupt/cancel behavior, attachment validation, working-root behavior, and validation scripts.

Required evidence:

- relevant API and library tests;
- `npm run harness:validate:premerge` against a reachable local harness API;
- review of `frontend/artifacts/harness/section8/latest/summary.json` when generated;
- preservation of stable browser-facing SSE event names unless a governed compatibility change authorizes them.

## 8. Security And Network Gate

Use this gate for API keys, network policy, provider scope, redaction, stored logs, or outbound request behavior.

Required evidence:

- relevant key-storage, redaction, and network-policy tests;
- `npm run proof:network-policy` when network or provider behavior changes;
- confirmation that API keys are not written to project files, runtime events, logs, tool artifacts, or SDK transcript imports;
- confirmation that outbound network remains loopback plus current Anthropic-centered scope unless a human ruling broadens it.

## 9. UI And Claims Gate

Use this gate for product copy, workflow labels, navigation, review states, professional-boundary notices, and user-facing validation or release text.

Required evidence:

- relevant component or library tests where available;
- targeted visual/manual review when layout, labels, or user-facing workflow changes;
- no wording that says or implies Chirality approves professional work, proves code compliance, externally validates work, signs, seals, certifies, authenticates, publishes, or issues work for reliance;
- clear distinction between draft/proposal/runtime evidence and human-accepted project truth.

## 10. Packaging Gate

Use this gate for instruction-root resources, Electron build configuration, package metadata, release scripts, DMG output, or distribution artifacts.

Required evidence:

- review the command and artifact posture in `docs/BUILD_AND_RELEASE.md`;
- `npm run instruction-root:integrity`;
- `npm run build`;
- `npm run desktop:pack` for package-layout changes;
- `npm run desktop:dist` for DMG/distribution changes or release-candidate review;
- generated artifact path, checksum when applicable, signing/notarization state, and known limitations.

Current release target remains macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless a governed amendment changes it.

## 11. Domain-Adapter Gate

Use this gate for future domain-engine profiles, protected paths, adapters, operation proposals, deterministic domain checks, or domain-output presentation.

Required evidence:

- human ruling that the domain-adapter tranche is in scope;
- proposal-record and human-gate semantics before any protected domain state mutation;
- path containment and write-quarantine tests where implementation exists;
- product copy review preserving that domain engines own domain truth and Chirality governs interaction, proposals, records, and human gates.

## 12. Waivers And Open Decisions

A waiver must be explicit and must name the waived gate item, reason, affected scope, compensating evidence, known risk, and human decision record. No waiver may authorize hidden project truth, protected instruction-root writes, private-data exposure, broad network access, unapproved bash/tool exposure, professional-approval claims, or release-publication claims.

Open release-quality decisions:

- hosted CI provider and workflow location;
- final release matrix, signing, notarization, publication, and attestation;
- release-label vocabulary and release-candidate evidence bundle format;
- coverage, performance, and permitted-variance thresholds;
- broader provider/network policy;
- Pi-backed adapter import/runtime strategy.
