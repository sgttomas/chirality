# Orchestration Plan — ROOT-STEP8-DECOMP-20260725

Agent 0: `HELP_HUMAN` posture · Date: 2026-07-25 · Basis: `24726a73c`
(post-PR-#346 `main`) · Branch: `claude/root-step8-decomposition-20260725`

## Authorization

Owner direction, in-session, 2026-07-25: continue from D-GOV-21 §6 step 8,
making effective use of Agent 1 and Agent 2 instances. Step 8 (packet §6):
"Perform the first root decomposition from the adopted PRD; root Project
Setup instantiates the G2 ownership register and the first accepted work
graph (G3's input)." This releases authoring and staging only; every
decomposition gate (I1) and the acceptance ruling remain the owner's, and
step 9 materialization stays behind the §5.3 gate. Standing owner direction:
`opus-5` models for Agent 1/2 instances.

## Work graph

| Node | Actor | Work | Write targets | Status |
|---|---|---|---|---|
| N0 | Agent 0 + two read-only Explore scouts | Context assembly: decomposition standard, precedents, manager fit, guard-state schemas | `AgentRuns/ROOT-STEP8-DECOMP-20260725/evidence/` | COMPLETE |
| N1 | Agent 1 — SOFTWARE_DECOMP (`opus-5`), sealed brief | Author the CANDIDATE first root decomposition from `docs/PRD_ROOT.md` | `execution/_Decomposition/**` (new), `returns/N1_RETURN_RAW.md` | DISPATCHED |
| V1 | Agent 2 — ephemeral verifier (`opus-5`), sealed brief | Adversarial verification: F4 bidirectional traceability, D-15 coverage, I1–I10 + SPEC ID conformance, G2 literal-containment readiness | `returns/V1_RETURN_RAW.md` only | PENDING (after N1) |
| A0 | Agent 0 | Fan-in: verify scope held, re-run battery, dispositions; stage candidate tranche (receipt, PR) | run record, `LOOP_RECEIPTS.md` | PENDING |
| GATE | Owner | Ruling over the exact candidate SHA (Gates 1–7 + acceptance) | — | STOP STATE |

Write-target disjointness: N1 alone writes `execution/_Decomposition/`; V1
writes only its return file; serialized N1 → V1 → A0. No node touches
instruction surfaces, `execution/_harness/`, or creates `PKG-*`/`DEL-*`
folders anywhere.

## Constraints carried into briefs

- D-9 / packet §4: scope derives from the adopted PRD only; nothing invented
  from discussion. Incorporated-by-reference documents are interpretive
  context, not independent scope generators.
- D-15: coverage across all four §4.1 categories or recorded, reasoned
  deferral (D-15 is itself PROPOSED — noted, applied anyway as the PRD's
  only coverage obligation).
- F4: every scope unit traces to a PRD requirement/objective; every PRD
  requirement/objective has coverage or a recorded deferral.
- SPEC §1 ID format `PKG-XX_{Label}` / `DEL-XX-YY_{Label}`; stable IDs (I5);
  identifiers must be G2-literal-containment ready.
- Candidate posture: Gate Log marks all gates PENDING_OWNER_RULING; no
  acceptance claimed by any agent.

## Post-ruling tranche (recorded, not released here)

Decision record + register row + receipt; root Project Setup instantiates
`execution/_harness/{root_guards,adapter,surface_ownership,work_graph}.yaml`
per `evidence/GUARD_STATE_SPEC.md`, against the accepted decomposition and
the accepting merge SHA. Materialization (step 9) remains out of scope.

## Stop state

This run stops at the human gate: candidate committed, PR opened, owner
presented with the exact candidate SHA. No self-merge (D-8); no gate
self-acceptance.
