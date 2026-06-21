# INSP-05 Development Roadmap

Date: 2026-06-21
Persona: WORKING_ITEMS
Status: COMPLETE
Basis: 53/53 INSP-03 assessments, INSP-04 gate-process evaluation, active plan D-APP-19 Option D
Reviewed SHA basis: `2a0e250f9bbe8dc5c96d55782265df18fdf33122`

## Executive Recommendation

Proceed with a ruling-first, evidence-profiled development roadmap. Do not issue deliverables yet.
The highest-leverage next work is to resolve cross-cutting human rulings, then repair stale
documentation/status truth, then close the genuine code and evidence gaps found by INSP-03.

No semantic files were used or produced.

## Human Rulings To Clear First

| ID | Topic | Why it blocks roadmap execution |
|---|---|---|
| D-APP-34 | Post-INSP-03 issuance gate model | RULED Option B: future issue-readiness uses evidence profiles. |
| D-APP-35 | REF-006 PRD hash/source-state treatment | RULED Option A: current PRD is accepted and downstream references may be refreshed. |
| D-APP-36 | AMD-01 UI render-test acceptance bar | RULED Option B: component/render tests required; browser checks for high layout risk. |
| D-APP-37 | PKG-10 doc-only acceptance basis and status-truth repair | RULED Option A: PKG-10 uses doc-only profile and bounded status-truth repair. |

Packets for D-APP-35 through D-APP-37 were prepared with this roadmap and subsequently ruled.

## Roadmap

| Priority | Work Item | Type | Size | Prerequisites | Strategic fit |
|---|---|---|---:|---|---|
| P0 | Apply D-APP-34 evidence-profiled issue-readiness model to future issue attempts. | governance | S | D-APP-34 ruled Option B | ON-STRATEGY |
| P0 | Refresh REF-006 PRD hash/source-state references. | governance | S | D-APP-35 ruled Option A | ON-STRATEGY |
| P0 | Apply AMD-01 component/render UI evidence bar. | governance/test policy | S | D-APP-36 ruled Option B | ON-STRATEGY |
| P0 | Repair PKG-10 status truth under doc-only profile. | governance/status policy | S | D-APP-37 ruled Option A | ON-STRATEGY |
| P1 | Reconcile stale control/governance local-kit wording found in PKG-00 and PKG-01. | docs/reconcile | S | P0 source-state rulings where referenced | ON-STRATEGY |
| P1 | Create the reliance-boundary register and enforcement/test index for DEL-01-02. | docs/governance | M | REF-006 treatment | ON-STRATEGY |
| P1 | Normalize scope-boundary and professional-boundary review checklists. | docs/governance | S | REF-006 treatment | ON-STRATEGY |
| P1 | Refresh runtime evidence records and spec-to-implementation reconciliations for PKG-03 and PKG-04. | docs/test | M | D-APP-18/D-APP-17 evidence accepted as history | ON-STRATEGY |
| P1 | Reconcile G5 naming/taxonomy issues: `runTurn`/`startTurn`, event ownership, interruption taxonomy, and child-run IDs. | docs/code/test | M | Runtime evidence refresh | ON-STRATEGY |
| P1 | Implement G1 execution-root scaffolding baseline seeding. | code/test | M | Filesystem profile and lifecycle fixture agreement | ON-STRATEGY |
| P1 | Implement G2 document-kit/metadata scanner with missing-state warnings. | code/test | M | G1 or explicit scaffold contract boundary | ON-STRATEGY |
| P1 | Implement G3 canonical session folder plus legacy-flat migration. | code/test | L | Runtime event/session contract reconciliation | ON-STRATEGY |
| P1 | Implement G4 transcript view using existing replay/event data. | code/UI/test | M | G3 storage decision or stable compatibility adapter | ON-STRATEGY |
| P2 | Close DEL-05-05 tool-result residuals: metadata, checksum/retention, and concurrency replay test. | code/test | M | Session/artifact contract decisions | ON-STRATEGY |
| P2 | Close PKG-06 permission/tool residuals: boot/version fingerprint, missing-register fallback, exact-edit preconditions, atomicity proof, Bash interruption proof, and PreCompact/Stop semantics. | code/test/docs | M | Filesystem and runtime-event reconciliations | ON-STRATEGY |
| P2 | Close PKG-08 agent/subagent residuals: full conformance fixtures, persona spec correction, Pipeline component coverage, and child-run contract alignment. | code/test/docs | M | G5 child-run decision | ON-STRATEGY |
| P2 | Reconcile PKG-02 UI specs against the loop-first app and add tests required by AMD-01. | docs/UI/test | M | AMD-01 ruling | ON-STRATEGY |
| P2 | Build release-quality validation wrapper/runbook for PKG-09, including current full test, premerge, Section 9 policy, and summary artifact consistency. | validation/docs | M | D-APP-34 evidence-profile decision | ON-STRATEGY |
| P2 | Refresh packaging and instruction-root evidence, including packaged SDK subprocess proof where required. | validation/package | M | Release-validation wrapper | ON-STRATEGY |
| P2 | Add whole-product secret scan and network proof evidence for release/security deliverables. | security/validation | M | Release-validation wrapper | ON-STRATEGY |
| P3 | Repair PKG-10 status-history wording and preserve all R7 work as future-boundary until a governed amendment. | docs/status | S | D-APP-37 | ON-STRATEGY |
| P3 | Prepare future R7 amendment brief for profile validators, OperationProposal workflow, protected paths, and boundary notices. | future governance | L | D-APP-37 plus explicit owner selection | ON-STRATEGY only if kept behind the domain-engine amendment gate |

## Package Coverage

- PKG-00: Control-plane closure is mostly aligned; stale historical conflict text should be reconciled.
- PKG-01: Governance copy is useful, but reliance-boundary register and row-level human rulings remain material.
- PKG-02: Baseline UI is functionally strong, but route/layout wording and UI render-test acceptance need AMD-01.
- PKG-03: Runtime engine surfaces are implemented, but evidence records and taxonomy/spec drift need cleanup.
- PKG-04: Adapter/settings/provider surfaces are strong, with probe/adoption and packaged-evidence refresh items.
- PKG-05: Audit/event mechanics are strong, while session folder migration and transcript view are genuine code gaps.
- PKG-06: Permission/tool controls are substantial, with proof, fallback, atomicity, and event-semantics residuals.
- PKG-07: Filesystem execution needs scaffold seeding and document-kit scanner work before lifecycle issuance.
- PKG-08: Agent/subagent governance works at key boundaries, but conformance and child-run contract cleanup remain.
- PKG-09: Validation/release surfaces need current command artifacts, runbook/CI consistency, and security proofs.
- PKG-10: Future-boundary documents are conservative, but doc-only acceptance and status truth need human handling.

## Non-Goals

- No `CHECKING -> ISSUED` transition.
- No provider expansion beyond the current Anthropic path.
- No R7 domain-engine implementation.
- No release/distribution posture change.
- No professional approval, certification, sealing, authentication, or code-compliance acceptance.

## Validation Note

This roadmap is a planning synthesis. It changed no runtime source, package manifest, lockfile, provider
policy, release artifact, or lifecycle state.
