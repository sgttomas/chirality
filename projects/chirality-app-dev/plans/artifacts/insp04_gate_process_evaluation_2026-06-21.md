# INSP-04 Gate-Process Evaluation

Date: 2026-06-21
Persona: WORKING_ITEMS
Status: COMPLETE
Reviewed SHA basis: `5c6cebb0a1fdafe8e39c0c8d93ba0307a1bbc4bd`
Input sweep: `plans/artifacts/insp03_assessment_index_2026-06-20.md`
Decision packet: `execution/_Coordination/_DECISIONS/D-APP-34_PACKET_2026-06-21.md`

## Recommendation

Modify the per-deliverable gate. Keep the human, SHA-bound lifecycle model in `CHECKING` and `ISSUED`,
but add evidence profiles and an issue-readiness package before any `CHECKING -> ISSUED` transition.

Do not replace the gate outright. The non-delegable human gate is still correct for provenance,
reliance boundaries, and professional-boundary control. Do not keep the gate exactly as-is either:
the INSP-03 sweep showed that a single implementation-style checklist does not fit all deliverable
classes.

## Basis

- `docs/CONTRACT.md` requires humans to author binding approval records, binds approvals to content
  evidence, and makes human gates non-delegable (`K-AUTH-1`, `K-AUTH-2`, `K-GATE-1`).
- `docs/SPEC.md` defines `CHECKING` as human review and `ISSUED` as human release, with approval SHA
  evidence required for both human-gate states.
- `docs/PRD.md` requires forward-only lifecycle transitions, actor authorization, and approval SHA
  evidence for checking/issued transitions.
- INSP-01 proved that the project can mechanically move all 53 deliverables into `CHECKING` with an
  owner-approved SHA without changing runtime source.
- INSP-03 proved that all 53 deliverables can be inspected, but their evidence classes differ enough
  that one issuance checklist would either overstate doc-only work or under-check runtime/release work.

No semantic files were used or produced.

## Findings

1. `CHECKING` worked well as admission to inspection.
   The 53-deliverable transition created a clear review boundary and did not imply issuance.

2. `ISSUED` needs a fresh content SHA, not the inspection-entry SHA.
   The INSP-03 assessment records were added after the INSP-01 `CHECKING` approval SHA. That SHA is
   still valid as inspection-entry evidence, but any future issue approval must bind to the then-current
   content after remediation, deferrals, and evidence packaging.

3. Evidence classes differ.
   Runtime deliverables need source/test evidence. UI deliverables need the AMD-01 render-test ruling.
   Validation/release deliverables need current command artifacts. Governance/control deliverables need
   document and dependency evidence. PKG-10 future-boundary deliverables need a doc-only acceptance
   basis and must not imply R7 implementation.

4. Several blockers are cross-cutting, not deliverable-local.
   REF-006, AMD-01, PKG-10 doc-only basis, stale status-history wording, and spec-to-implementation
   drift appear across multiple deliverables. Per-deliverable issue decisions should consume resolved
   cross-cutting rulings instead of asking the human to rediscover them 53 times.

5. Dependency closure is necessary but not sufficient.
   The accepted DepClosure snapshot reports SCC 0, and the analyzer still reports 0 SCCs. That supports
   sequencing, but it is not lifecycle issuance, release readiness, or professional acceptance.

## Proposed Gate Model

Keep the lifecycle states:

1. `CHECKING`: admitted to review. Requires human actor and SHA. It may bind to the reviewed baseline
   before assessment artifacts are written.
2. `ISSUED`: accepted deliverable state. Requires a new human actor and SHA after all issue-readiness
   evidence is assembled.

Add issue-readiness profiles before `ISSUED`:

| Profile | Applies to | Required evidence before issue |
|---|---|---|
| Runtime/source | Runtime, API, MCP, hooks, lifecycle, provider, session, tool, and UI logic deliverables | Current source/test evidence, focused tests, stale spec reconciliation, dependency disposition, skipped-check rationale. |
| UI/product | Desktop shell, matrix, sidebar, workbench/pipeline, and visual interaction deliverables | Runtime/source evidence plus AMD-01 ruling on render/browser evidence. |
| Governance/control | Control-plane, policy, boundary, and documentation deliverables | Source-state caveats resolved or explicitly deferred, dependency rows disposed, stale local-kit wording reconciled, no runtime/release claim. |
| Validation/release | Packaging, CI, security, network, release, and validation deliverables | Current command artifacts, full-suite or scoped-release check rationale, packaged/build/security evidence where required. |
| Future-boundary/doc-only | PKG-10 and any future fenced-domain documents | Human-ruling basis for doc-only acceptance, explicit non-implementation language, future-amendment blockers preserved, no solver/professional/release claim. |

## Decision Need

D-APP-34 is prepared as a proposal because changing the issuance gate is a human-governed process
decision. The recommended option is to modify the gate with evidence profiles while preserving
non-delegable human approval and SHA binding.

## Next Work

INSP-05 should synthesize the 53 assessments into a dependency-ordered development roadmap using this
modified-gate recommendation as an input, but not as a ruling. Open rulings remain:

- REF-006 PRD hash/source-state treatment.
- AMD-01 UI render-test acceptance bar.
- PKG-10 doc-only acceptance basis and status-truth repair.
- D-APP-34 gate-process model.
- Any future `CHECKING -> ISSUED` transition.
