# Root Scope-of-Work Governance Handoff State

Status: `CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED`

## Accepted upstream basis

- Frozen root main: `2770fda4c63c98ee9f18cffbafd14c9aa59f497f`.
- D-GOV-15 published ruling:
  `58aa81d62f4a32e3c2d687e4356a1e4be8141674`, including its owner-authorized
  deterministic-checklist addendum.
- App pilot evidence branch/commit:
  `codex/sow-app-pilot@fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`.
- Piping pilot evidence branch/commit:
  `codex/sow-piping-pilot@31c35ea9798c29cd0af16b7089186f3942dcfcb1`.
- Stage-1 proposal/evidence snapshot:
  `31e5efd985db4cc7b25543e11a65933979e07e4f` on
  `codex/sow-stage1-execution`.
- D-GOV-16 owner ruling, 2026-07-12: items 1–10 `APPROVED` exactly as
  proposed; published ruling snapshot:
  `7584718aa32b112e415331736d1a8e68c12ac176`.
- Synchronized planning basis: `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`.
- Presented Stage-2 plan branch/snapshot:
  `codex/sow-stage2-plan@27f03730c956447b9a9696422cc9c63b8f061939`;
  package `execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/`.
- Accepted Stage-2 root-loop activation snapshot:
  `1eebc67ca0ce82bb2ae320fec49b1568fa037ba1`; deterministic pointer
  `CURRENT_WORKPLAN.md` selects
  `WORKPLAN_2026-07-12_scope_of_work_stage2.md`.

## Closure verdict

Stage 2 conversion and rollback closure is accepted on exact
`origin/main@79de30d83b91a2ab468a3f17536a5233c2f85fe7`. The live tracked census is
154: 146 valid clean single-format `SOW_V1` conversion members and eight exact
Piping PKG-00 legacy governance-context exemptions. Lifecycle remains 153
`IN_PROGRESS` plus sole issued Piping `DEL-01-01`; production migration residue
is zero. All 730 inverse rows and 146 composed rollback round trips pass. Root,
App, Piping, caller, compatibility, containment, and validator checks pass.

Final independent manifests:

- RECONCILIATION:
  `7975141369025a50087c6f8d94b51d59740d0adabb49576518c9c4d7926add27`.
- EVALUATION:
  `3a17c5b5637216b74018206a931a4a01fb6c90769094ac77d4a3c57da47b133f`.

H2 remains unapproved. The recommended ruling is H2-R: retain compatibility
and perform no retirement because the eight PKG-00 contracts and accepted
rollback path still require the legacy skill, validator, readers, and callers.
Silence performs no retirement.

## Historical Stage-1 and plan closure

Stage 1 is `PASS`. All ten authorized candidates passed independent
preservation audit: 325/325 claim mappings are `PRESERVED`, 3,466/3,466 source
lines are covered, the 40 legacy sources and ten statuses are byte-identical
to the frozen basis, all pilot lifecycle states remain `IN_PROGRESS`, and no
fresh conversion or verifier rerun was required. Schema, project content, and
preservation pass; authorized serialized conversion fallback is separately
reported from native verifier PASS.

The owner-authorized governance correction replaced repeated agentic checklist
extraction with a deterministic `AC-*` compiler and a REVIEW exact-consumer
contract. Ten-pilot reproduction passes byte-for-byte. The full evidence is
derivative and does not replace deliverable, decomposition, lifecycle, or
human-decision truth.

The fresh D-GOV-16 Stage-2 orchestration plan is accepted for the next
goal-oriented execution session and has been integrated into the deterministic
root bootstrap chain. The plan and loop activation passed their sealed checks,
but no Stage-2 node has been dispatched or implemented.

## D-GOV-16 ruled package

`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`
is `RULED`, with items 1–10 approved exactly as proposed and bound to the
proposal snapshot above. The exact successor-standard bytes are ratified. The
exact approved TYPES/SPEC patches remain unapplied and queued for a later
governed tranche. The evidence index and exact-byte artifacts remain under
`docs/governance_harness/_PROPOSALS/D-GOV-16/`; the patches require
`git apply --unidiff-zero --check` against the synchronized implementation
basis.

## Required stop and release condition

Conversion is closed. Stop before any compatibility or legacy-retirement act
until the human selects H2-R, H2-P, or H2-F against the exact accepted basis.
H2-R records retention only. H2-P and H2-F authorize preparation lanes only
and retain a second integration gate; neither permits immediate live deletion.
No option changes lifecycle, executes rollback, or modifies historical
evidence. Silence leaves every current compatibility surface supported.

## Rerun requirements

Before acting on H2, bind the selected ruling to exact main and both final
manifests. H2-P/H2-F require a fresh governed run, changed/caller manifest,
rollback analysis, root/App/Piping suites, independent EVALUATION and
RECONCILIATION, and a separate CHANGE integration gate. Any census, lifecycle,
caller, compatibility, rollback, or basis drift returns to the human.
