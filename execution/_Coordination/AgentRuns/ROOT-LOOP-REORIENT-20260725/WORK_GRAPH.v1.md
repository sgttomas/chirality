# Work Graph v1 — ROOT-LOOP-REORIENT-20260725

| Node | Executor | Model | Objective | Read scope | Write targets | Depends on | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|---|---|
| N1 | Agent 1 PROJECT_SETUP (sealed brief `briefs/WORKPLAN-AUTHOR-BRIEF.md`) | opus-5 | Author successor root workplan; update standing pointer | `execution/_Coordination/**` (read), `docs/governance_harness/**` (read), `docs/DIRECTIVE.md`, `docs/SPEC.md`, `AGENTS.md`, `agents/AGENT_PROJECT_SETUP.md` | `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md` (new), `execution/_Coordination/CURRENT_WORKPLAN.md` (pointer update only) | — | Terminal text: files written, workplan outline, self-check assertions | Agent 0 validation V1 |
| N2 | Agent 0 (parent-executed; disjoint from N1) | — | EffectiveSHA backfill into D-GOV-21 decision record + implementation handoff; loop receipt | governance records | `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`, `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`, `execution/_Coordination/LOOP_RECEIPTS.md` | N1 accepted | — | tranche commit |

## Validation gate V1 (Agent 0, before N2)

- Pointer `CURRENT_WORKPLAN.md` resolves to the new workplan file; target
  exists; closed workplans untouched.
- New workplan encodes the D-GOV-21 §6 remaining sequence (steps 5–9) with
  the §5.3 gate, parked class (b)/(c) lanes, and stop conditions; carries no
  authority claim; cites the ruling and EffectiveSHA.
- No machine-absolute paths (SPEC §0.2.4); no instruction-surface writes; no
  `PKG-*`/`DEL-*` creation (G0 must remain PASS-idle).
- Write targets match the brief exactly; any excess is rejected at fan-in.

## Failure handling

N1 failure or invalid return blocks N2 and returns to the owner; nothing is
committed. Partial returns are not accepted at fan-in.
