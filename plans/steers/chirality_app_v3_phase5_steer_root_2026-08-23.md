# ROOT LOOP STEER — v3 Phase 5: acceptance transcription, schedule basis, evidence reruns — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: Root loop (repository root `execution/`). The loop's instruments govern; this steer directs one bounded phase under them. Companion instruments: `plans/steers/chirality_app_v3_root_ruling_record_r8_2026-08-23.md` (the R8 acceptance; SHA-256 recorded in the PR that published this steer — both files merged together), `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md` (SHA-256 `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`).

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `5b2edfb895f79b00fa883c010ff9a9e8b4606bc9` (PR #648, Root v3 Phase 4) and Receipt 124.
- The estimate snapshot at
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/`
  matches every SHA-256 identity listed in ruling record R8 (`SUMMARY.md`
  `788341ba…`, `ESTIMATE_METHOD.md` `18ca936c…`, `ARTIFACT_HASHES.csv`
  `99c2a8bd…`, `INPUT_HASHES.csv` `a838553f…`, `RETURN.md` `6ac93dc5…`,
  `REVIEW.md` `2ae917a7…`; verify full values against R8).
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` SHA-256 `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`.
- `execution/_ScopeChange/_LATEST.md` SHA-256 `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
- `execution/_harness/adapter.yaml` SHA-256 `71f603ad463c14dbba6b02806d67cfc4d859219ff828812fb37de35e78025f3c` (53/53 pin; this phase must not disturb it).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 rows; byte-identity required at close as well).
- The eight `_DEPENDENCIES.md` files at their Phase-3 identities recorded in the Phase-3 evidence (`DEL-02-06` `20773668…` and the seven carrier files; verify against `DEP_GRAPH_POST_PHASE3` input pins).

## Authority context

R8-A accepts the exact estimate snapshot as the accepted estimate basis for
the SCA-004 slice. R8-B authorizes exactly this phase. Propagation_Plan §4.3
permits scheduling now that dependency extraction (Receipt 123) and estimate
acceptance (R8-A) both exist. The schedule basis this phase produces is a
draft returned for owner acceptance; it is not a commitment, calendar
promise, staffing plan, lifecycle change, or implementation dispatch.
TM-ROOT-106/122 remain G1 blockers and must appear only as exclusions or
risks, never as resolved assumptions. All ten DEL-02-06 bindings remain
held. No App-loop coupling beyond the existing non-gating notice edges may
be introduced.

## N1 — R8 acceptance transcription

Write one new file
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/OWNER_ACCEPTANCE.md`
recording: the R8 record path and SHA-256; the acceptance date; the exact
accepted artifact identities (restated from R8); and the sentence that
acceptance creates estimate-basis truth only. Modify no existing snapshot
file — the accepted bytes are immutable; this is an addition beside them.

## N2 — schedule-basis snapshot

Produce a new immutable snapshot at
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/SCHEDULE_BASIS_POST_PHASE4/`
computing the objective-relative schedule basis for the SCA-004 slice from
exactly two accepted inputs: the R8-accepted estimates and the Phase-3
dependency truth. Required content:

1. **Sequencing derivation** — an ordered work-stream structure derived
   from the accepted gating edges (six carrier evidence fan-ins into
   DEL-02-06; DEL-04-05 and DEL-05-02 into DEL-04-11; DEL-04-11's
   non-gating validation relationship must not gate). The A2-B/R7-A SCC
   context does not apply here; use only Root Phase-3 edges. State
   explicitly which carriers are parallelizable (no gating edge between
   them) and what strictly precedes the DEL-02-06 fan-in closure.
2. **Effort-loaded profile** — per work stream, base/low/high hours from
   the accepted estimates; totals must re-derive exactly from the accepted
   snapshot (1012 / 560–1464). No calendar dates, no staffing counts, no
   velocity assumptions: express the basis in effort-hours and ordering
   only, with any duration illustration clearly labeled non-normative.
3. **Blocker register** — TM-ROOT-106/122, C1, the ten held DEL-02-06
   bindings, and every App-owned obligation, each stated as a blocker or
   exclusion with the gate that resolves it; no pin or hold treated as
   resolved.
4. **Hash manifests** — `INPUT_HASHES.csv` (the accepted estimate snapshot
   files, the eight `_DEPENDENCIES.md` files, the register, and the R8
   record) and `ARTIFACT_HASHES.csv` over the package; `RETURN.md` closes
   `AWAITING_OWNER_ACCEPTANCE`; fresh independent review under the
   unlimited-repair/fresh-review rule.

## N3 — mandated evidence reruns

Regenerate the objective-relative graph and dependency-closure audit as new
immutable snapshots
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_PHASE5/`
and
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE_POST_PHASE5/`,
consuming current live state (unchanged dependency truth plus the
now-accepted estimate basis recorded as context). Pin inputs at their
current identities — including the current post-repair run-record bytes, so
the Phase-3 rerun staleness (the repaired N1 return file) is cured in the
new pins. The Phase-3 evidence folders remain untouched history. Expected
shape: same node/edge/SCC results as Phase 3 (nothing changed dependency
truth); any deviation is a stop-and-report finding, not something to
reconcile silently.

## Write set, exactly

- One new file `OWNER_ACCEPTANCE.md` inside `ESTIMATE_SNAPSHOT_POST_PHASE3/`
  (no existing file in that folder may change).
- New files strictly inside `SCHEDULE_BASIS_POST_PHASE4/`,
  `DEP_GRAPH_POST_PHASE5/`, and `AUDIT_DEP_CLOSURE_POST_PHASE5/`.
- Run/control evidence under
  `execution/_Coordination/AgentRuns/ROOT_V3_PHASE5_2026-08-<DD>/`.
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 125;
  incorporate this steer and the R8 record by immutable path and SHA-256).
- One dated append to `execution/_Coordination/HANDOFF_STATE.md` (Phase 5
  drafted; schedule acceptance remains; SCA-004 propagation otherwise
  complete).

Not selectable: any deliverable-folder file; the decomposition registers;
`execution/_ScopeChange/_LATEST.md`; `execution/_harness/adapter.yaml` and
both pinned harness test files; the TM register; any existing evidence
file under `Evidence/` (Phase-3 and Phase-4 snapshots are immutable
history); `plans/**`, `agents/**`, `tools/**`, `docs/**`, `AGENTS.md`,
`exports/**`; any `projects/**` path.

## Discipline

- Run the candidate-whitespace validator before generating any artifact
  that pins another artifact's hash; if a later repair changes pinned
  bytes, regenerate the pinning artifact or record exact pre→post lineage
  in the receipt.
- Run before pushing: candidate whitespace (base = current `origin/main`),
  agent instructions, instruction entrypoints, CI-form G4 (expect zero
  instruction-surface paths and zero required manifests), taskmgmt validate
  (register byte-identity preserved), the focused practitioner-harness pair
  (must stay 56 green with no repin), and `git diff --check`.
- Branch `codex/root-v3-phase5-2026-08-<DD>`. Do not merge. If `main`
  advances, request sync authorization from the owner and record the grant
  verbatim in the receipt. HELP_HUMAN byte-verifies before endorsement.
