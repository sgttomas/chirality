# ROOT LOOP STEER — v3 Phase 4: SCA-004 carrier estimate snapshot — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: Root loop (repository root `execution/`). The loop's instruments govern; this steer directs one bounded phase under them. Companion instruments: `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md` (SHA-256 `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`), `plans/steers/chirality_app_v3_phase3_steer_root_2026-08-23.md` (SHA-256 `9c8d3884f97733f674269014c1735977c9628be1d929f6859889c79710ae4186`).

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `e245d54e399d19436124e46e21d353fa11e774ed` (PR #643, Root v3 Phase 3) and Receipt 123.
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` SHA-256 `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` (applied revision 1.3; 53 deliverables).
- `execution/_ScopeChange/_LATEST.md` SHA-256 `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
- `execution/_harness/adapter.yaml` SHA-256 `71f603ad463c14dbba6b02806d67cfc4d859219ff828812fb37de35e78025f3c` (53/53-INITIALIZED pin; this phase must not disturb it).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 rows; byte-identity required at close as well).
- The seven carrier `ScopeOfWork.md` files at their accepted post-R7 identities recorded in Receipt 123 (DEL-02-07 `9fb8703b…`, DEL-02-08 `d9871a4a…`, DEL-02-09 `e0cf3285…`, DEL-02-10 `bfe374aa…`, DEL-02-11 `abd5dcef…`, DEL-02-12 `62bcfbdd…`, DEL-04-11 `2d5cd066…`; verify full 64-hex values against Receipt 123).
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_DEPENDENCIES.md` SHA-256 `20773668bd8086164c1cd7ee4119d7744d0c2f9a045e546b5565791bc772537f`.

## Authority context

Propagation_Plan §4.2 requires a fresh estimate snapshot for the seven new
carriers and a DEL-02-06 reassessment, and its prerequisites are now met:
accepted SOWs (R7-A), Context Envelopes, write loci, gates, and acceptance
checks exist, and dependency extraction is complete (Receipt 123).
Propagation_Plan §4.3 sequences scheduling strictly after estimate
acceptance; no schedule artifact is produced in this phase. TM-ROOT-106 and
TM-ROOT-122 remain G1 blockers; no estimate may embed a pin assumption.
This phase produces decision-support truth only: nothing it writes is an
accepted estimate, a schedule, a lifecycle change, an activation, or an
implementation act. Estimate acceptance is a separate owner ruling; seating
accepted estimates into deliverable folders is a separate later phase.

## N1 — seven carrier estimates

For each of DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11,
DEL-02-12, and DEL-04-11, draft one estimate grounded strictly in: the
accepted SOW (objectives, outputs, requirements, gates, acceptance checks),
the applied register row, the deliverable's `_CONTEXT.md`, and the Phase-3
`_DEPENDENCIES.md`. Each estimate must state:

1. **Basis of estimate** — which accepted clauses drive each element; no
   scope invention, no reliance on unaccepted or foreign material.
2. **Work breakdown** — the SOW outputs as the top level; effort per output
   in hours with a named uncertainty class per element (house classes; if
   none exist, define LOW/MEDIUM/HIGH spread bands once in the package
   preamble and use them consistently).
3. **Assumptions and exclusions** — explicit; every held binding
   (all ten DEL-02-06 bindings), TM-ROOT-106/122, C1, and every App-owned
   obligation is an exclusion, not an assumption.
4. **Dependency interactions** — how the Phase-3 edges (evidence fan-in to
   DEL-02-06; DEL-04-11's two accepted inputs) shape sequencing risk, without
   computing a schedule.

## N2 — DEL-02-06 reassessment

Reassess DEL-02-06 as the integration/fan-in carrier per §4.2: the
incremental integration effort implied by six accepted evidence fan-ins and
the non-gating DEL-04-11 validation relationship, with the same structure as
N1. The ten `HELD_UNAVAILABLE` bindings remain held; the reassessment states
what is estimable now versus blocked behind holds, and does not price held
work as if available.

## N3 — immutable snapshot package

Assemble the eight estimates into one immutable snapshot at
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/`:
a `SUMMARY.md` with per-deliverable totals and uncertainty ranges; per-
deliverable estimate files; `INPUT_HASHES.csv` pinning every consumed input
(the seven SOWs, register, `_CONTEXT.md` and `_DEPENDENCIES.md` files, and
the R7 record); `ARTIFACT_HASHES.csv` over the package; and a
`RETURN.md` closing `AWAITING_OWNER_ACCEPTANCE`. Fresh independent review
with the unlimited-repair/fresh-review rule; every repair disclosed. The
package is derivative decision support and must say so; it cites Receipt 123
and this steer and grants nothing.

## Write set, exactly

- New files strictly inside
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/`.
- Run/control evidence under
  `execution/_Coordination/AgentRuns/ROOT_V3_PHASE4_2026-08-<DD>/`.
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 124;
  incorporate this steer by immutable path and SHA-256).
- One dated append to `execution/_Coordination/HANDOFF_STATE.md` (Phase 4
  drafted; estimate acceptance and schedule remain).

Not selectable: any deliverable-folder file (`ScopeOfWork.md`, `_STATUS.md`,
`_DEPENDENCIES.md`, `_CONTEXT.md`); the decomposition registers;
`execution/_ScopeChange/_LATEST.md`; `execution/_harness/adapter.yaml` and
both pinned harness test files (no status file changes occur, so the live
pin must not move); the TM register; `plans/**`, `agents/**`, `tools/**`,
`docs/**`, `AGENTS.md`, `exports/**`; any `projects/**` path.

## Discipline

- The Phase-3 graph/closure packages remain current through this phase
  (estimates are drafted, not accepted); the mandated evidence rerun comes
  after estimate acceptance and scheduling, not here.
- Run the candidate-whitespace validator before generating any artifact that
  pins another artifact's hash; if a later repair changes pinned bytes,
  regenerate the pinning artifact or record exact pre→post lineage in the
  receipt (Phase-3 lesson).
- Run before pushing: candidate whitespace (base = current `origin/main`),
  agent instructions, instruction entrypoints, CI-form G4 (expect zero
  instruction-surface paths and zero required manifests), taskmgmt validate
  (register byte-identity preserved), the focused practitioner-harness pair
  (`python3 -m pytest tools/practitioner_harness/test_root_adoption.py
  tools/validation/test_validate_root_harness_adapter.py -q` — must stay
  56 green with no repin), and `git diff --check`.
- Branch `codex/root-v3-phase4-2026-08-<DD>`. Do not merge. If `main`
  advances, request sync authorization from the owner and record the grant
  verbatim in the receipt. HELP_HUMAN byte-verifies before endorsement.
