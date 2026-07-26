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
| N1 | Agent 1 — SOFTWARE_DECOMP (`opus-5`), sealed brief | Author the CANDIDATE first root decomposition from `docs/PRD_ROOT.md` | `execution/_Decomposition/**` (new), `returns/N1_RETURN_RAW.md` | COMPLETE (+2 directed continuations: V1 corrections; ruling application) |
| V1 | Agent 2 — ephemeral verifier (`opus-5`), sealed brief | Adversarial verification: F4 bidirectional traceability, D-15 coverage, I1–I10 + SPEC ID conformance, G2 literal-containment readiness | `returns/V1_RETURN_RAW.md` only | COMPLETE (1 BLOCKER corrected pre-staging; 1 MAJOR routed to owner as OI-013) |
| A0 | Agent 0 | Fan-in: verify scope held, re-run battery, dispositions; stage candidate tranche (receipt, PR #347) | run record, `LOOP_RECEIPTS.md` | COMPLETE |
| GATE | Owner | Ruling over the exact candidate SHA (Gates 1–7 + acceptance) | — | **RULED 2026-07-25** — acceptance + 3 dispositions against `ec62af070` (D-GOV-25); PR #347 merged `ea0ad7a56` |
| N1b | N1 continuation (`opus-5`) | Apply the three ruled dispositions to the decomposition package (publication tranche) | `execution/_Decomposition/**` | COMPLETE |
| N2 | Agent 1 — PROJECT_SETUP (`opus-5`), sealed brief `briefs/PROJECT-SETUP-BRIEF.md` | Root Project Setup: instantiate guard state (adapter, ownership register, first accepted work graph, guard registration) | `execution/_harness/**` (new), `returns/N2_RETURN_RAW.md` | COMPLETE — G0–G4 all PASS against written state |
| A0b | Agent 0 | Acceptance-tranche authoring (D-GOV-25 record, register row, tranche manifest) + fan-in, Receipt 47, PR | `docs/governance_harness/**`, run record, `LOOP_RECEIPTS.md` | COMPLETE |
| GATE2 | Owner | Human-gated merge of the acceptance-application PR | — | **MERGED** — PR #348 → `653fabc9b`; owner released step 9 in the same direction |
| M1 | N2 continuation — PROJECT_SETUP (`opus-5`), sealed brief `briefs/MATERIALIZATION-BRIEF.md` | Step-9 materialization: 6 PKG / 45 DEL at OPEN per SPEC §1; adapter baselines repinned (45, `653fabc9b`) | `execution/PKG-*/**` (new), `execution/_harness/adapter.yaml` (baselines), `returns/M1_RETURN_RAW.md` | COMPLETE — G0 second branch exercised and PASS; all guards + both suites green |
| A0c | Agent 0 | Step-9 tranche: EffectiveSHA backfill, manifest, F-1/F-2/F-3 dispositions (F-3 test rename applied as governed edit), Receipt 48, PR | `docs/governance_harness/**`, `tools/validation/test_validate_root_materialization_fence.py`, run record, `LOOP_RECEIPTS.md` | COMPLETE |
| GATE3 | Owner | Human-gated merge of the step-9 materialization PR | — | STOP STATE |

Step-9 fan-in dispositions (A0c): F-1 ACCEPTED — the executor followed the
repo's real placeholder convention (README.md) over the brief's incorrect
`.gitkeep` example; recorded so the error does not propagate. F-2 ROUTED TO
OWNER — SPEC §1.1 requires `_Archive/` subfolders while `.gitignore`
`**/_Archive/` policy makes them untrackable; the 18 local dirs stand; no
`.gitignore` or SPEC change made. F-3 APPLIED — G0 live test renamed
`test_live_repo_fence_passes` with a both-branches docstring (assertion
unchanged; manifest-covered). M1 open items 4–7 carried (SPEC §2.1
five-file vs §12.3 four-file tension incl. `_SEMANTIC.md`; practitioner-
harness adoption; per-deliverable initialization gated; Discipline /
Acceptance-Criteria TBDs are a decomposition-format gap, not 45 defects).

Fan-in dispositions (A0b): N1b's uncleaned ledger `OpenIssue` flags ACCEPTED
(clearing them would be an unruled edit to accepted content; the flag→issue
mapping is stated in telemetry §6); DEC-014..020 numbering ACCEPTED (I5);
N2's twelve recorded design choices ACCEPTED as read-from-source; N2 open
items 1–6 carried (practitioner-harness adoption separately gated;
root_guards first load-bearing at step 9; DEL-level entries at
materialization; no ordering edges — add via decomposition first; basis pin
provenance; explicit staging at commit).

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
