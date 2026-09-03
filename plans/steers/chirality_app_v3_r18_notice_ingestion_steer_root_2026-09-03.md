# ROOT LOOP STEER — R18 notice ingestion and TM-ROOT-122 disposition: record the routed App Electron-authority notice and apply the owner's ruling — 2026-09-03

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (repository root `execution/`). The loop's instruments govern; this steer
> directs one bounded tranche under them. Authorizing ruling: R18
> (`chirality_app_v3_root_ruling_record_r18_2026-09-03.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together). This
> steer is the contract for one bounded act and records exactly what that
> act did. Read it in full before any write.

## Basis gate (checked before any write; any failure stops and reports)

1. PR #680 (`codex/app-electron-concordance-2026-09-03`) is `MERGED` on
   `origin/main`; its merge commit is
   `8140daec7ab7165f8972451dbdd3a67b8bb2fd38`. Work on a fresh branch
   `codex/root-r18-tm-root-122-2026-09-03` from current `origin/main`; the
   recorded basis commit equals that merge commit.
2. The App notice exists on the basis at
   `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`,
   recomputed SHA-256
   `b68ed592b310fa996bb10d2aaf6889a25eb0481e6a57ce3fb2e414b775e4ee2b`
   (5228 bytes). Reading this and every other App path is authorized for
   verification and copying only; no App path may be written.
3. A11 at
   `plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md`
   recomputes to SHA-256
   `6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27`.
4. The Root destination
   `execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`
   does not yet exist.
5. The Root register row `TM-ROOT-122` is `OPEN` with empty `Disposition`
   and `Closed`, and `TM-ROOT-106` is present and `OPEN`.
6. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record R18 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.

Observed at execution: every line held. Basis `HEAD` = `origin/main` =
`8140daec7ab7165f8972451dbdd3a67b8bb2fd38`; the notice's content commit
`cd45390ae3331ea2748f5df5d934922ec90e8c55` and stated basis
`1537ddad1f9227dee1ba3233c0146694a779026a` are both ancestors.

## Authority context

Root's 2026-08-03 notice routed the PI082-F09 Electron drift to the App
loop and set `TM-ROOT-122` to close on the App's disposition. A11 E2
authorized the App concordance tranche; PR #680 applied it and was merged by
owner direction. R18-A routes the App echo onto the Root surface as
coordination input citing that merge identity; R18-B applies the owner's
ruling that `TM-ROOT-122` closes `RESOLVED_BY_DECISION` on D-APP-98 plus the
applied concordance; R18-C retains every negative grant. The notice is
cross-loop coordination, not authority: recording it changes no Root
contract, pin, schedule, workplan, or lifecycle state. The register act is a
`TASK_MANAGEMENT` act under `agents/AGENT_TASK_MANAGEMENT.md`: mandatory
read-only federation preflight before any write; the disposition is the
owner's recorded act (K-TM-3); evidence binds to bytes (K-TM-5).

## N1 — record the routed notice (Root ordinary session)

1. Create
   `execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`
   as a Root ingestion header followed by the App notice body copied as raw
   bytes. The header records: routed 2026-09-03 under R18; source path and
   SHA-256 on the App surface; the PR #680 merge commit as the final
   concordance identity the App notice could not name; Root's adoption
   disposition `ADOPTED_AS_COORDINATION_INPUT` (not authority); the run
   path; and the divergence from the 2026-08-24 precedent (a pure copy with
   no header). The body must be byte-identical to the source: verify by
   comparing the trailing 5228 bytes of the destination with the source.
2. Run a recorded contract-drift check as run evidence (not as a notice
   edit): recompute, at the basis, every identity the App notice asserts —
   D-APP-98, D-APP-72, `frontend/package.json` and its Electron pin,
   `frontend/scripts/verify-electron-dist.mjs` and its frozen supply
   identity, each of the eight post-image document SHA-256 values, the
   authority corpus v20 identity, the candidate and A11 identities, and the
   Root 2026-08-03 notice identity — and confirm the notice's Git claims
   (content commit and basis ancestry, merge identity). Any exact mismatch
   stops the tranche with a report; repair nothing.
3. Write `LAUNCH_BRIEF.md`, `CONTRACT_DRIFT_CHECK.md`, `RETURN.md`, and a
   terminal `STATUS.json` under
   `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-09-03/instances/N1_NOTICE_INGESTION/`,
   with `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `HANDOFF_STATE.md`, and a
   sorted `MANIFEST.sha256` at the run root.

## N2 — Root register act (TASK_MANAGEMENT)

1. Run the read-only federation preflight
   (`python3 tools/taskmgmt/taskmgmt.py federation --register execution/_Coordination/_TaskManagement/REGISTER.csv`)
   and record coverage, per-register counts, and typed finding counts.
   Zero writes before it completes.
2. On `execution/_Coordination/_TaskManagement/REGISTER.csv`, change the
   `TM-ROOT-122` row only: `Status=CLOSED`,
   `Disposition=RESOLVED_BY_DECISION`, `Closed=LastReviewed=2026-09-03`,
   `EvidenceRef` citing D-APP-98 (path), the ingested Root notice (path), and
   the PR #680 merge commit; `EvidenceSha` = recomputed SHA-256 of D-APP-98
   and of the ingested notice; `EvidenceQuote` = one exact D-APP-98
   sentence; one appended dated `Notes` entry citing R18, stating that the
   App document concordance (corpus v20) is applied and that G1 itself is
   not passed. Assert the recorded `EvidenceSha` values against fresh
   recomputation before any archive. `TM-ROOT-106` and every other row must
   remain byte-identical.
3. `taskmgmt validate` the live register; `taskmgmt archive` (relocates the
   CLOSED row to `REGISTER_CLOSED.csv`); validate both; run the final
   federation pass and record counts.
4. Write
   `execution/_Coordination/_TaskManagement/RULING_2026-09-03_ROOT_TM-ROOT-122_DISPOSITION.md`
   in the format of the existing Root `RULING_*` files: provenance, verbatim
   owner block, federation preflight, nine-domain scan, exact application
   with pre/post SHA-256 of the complete newline-terminated CSV row and of
   both register files, and the effect boundary.

## N3 — R18 instrument pair

Write `plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md`
(R16/R17 structure; R18-A/B/C; note on receipt numbering) and this steer.

## Post-write validation (run each; repair and rerun until passing)

- `git diff --check`; candidate whitespace against the basis commit.
- `taskmgmt validate` on both register files; federation preflight before
  and final pass after the register act.
- Root standing guards exactly as the idle workplan names them: G0
  `validate_root_materialization_fence.py`, G1
  `validate_root_harness_adapter.py`, G2 `validate_root_surface_ownership.py`,
  G3 `validate_root_work_graph_dispatch.py`, G4
  `validate_instruction_tranche_manifest.py` (CI form; this tranche touches
  no instruction surface, so no covering manifest is expected — if G4
  demands one, stop and report). Any guard that cannot run in the sandbox is
  recorded as skipped with the reason.
- `python3 tools/practitioner_harness/harness.py self-check`;
  `python3 -m pytest -q tools/practitioner_harness`;
  `python3 tools/validation/validate_agent_instructions.py agents`;
  `python3 tools/validation/validate_instruction_entrypoints.py`;
  `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`
  (must remain `VALID`; the App ledger is not touched).
- Frontend gates are skipped: no product source changes.
- Confirm with `git status`/diff that exactly the write set below changed
  and nothing else; confirm the `TM-ROOT-106` row hash is unchanged.

## Receipt and return

- Append the next free main-line receipt (Receipt 131 at execution time) to
  `execution/_Coordination/LOOP_RECEIPTS.md` per the ledger's rules:
  pointer to R18 for the owner act, pointers to the run record, notice,
  register post-images with SHA-256, the `RULING` file, and the R18 pair;
  check summary; model attribution; gate outcome. State that the R17
  seating steer's "Receipt 131" reference must be read at seating time as
  the next free main-line receipt (flagged, not ruled).
- Commit, push the branch, and open one PR against `main`. Do not merge.
  The owner decides the merge separately.

## Write set, exactly

- `execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`
  (new).
- New files strictly inside
  `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-09-03/`.
- `execution/_Coordination/_TaskManagement/REGISTER.csv` and
  `REGISTER_CLOSED.csv` (the `TM-ROOT-122` row and its mechanical
  relocation only).
- `execution/_Coordination/_TaskManagement/RULING_2026-09-03_ROOT_TM-ROOT-122_DISPOSITION.md`
  (new).
- `plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md` and
  this steer (new).
- One append to `execution/_Coordination/LOOP_RECEIPTS.md`.
- `execution/_Coordination/HANDOFF_STATE.md` only if the Root workplan
  requires an update on every tranche. The idle workplan reads it (Step 0.3)
  and does not require it; it is left unchanged, and its already-stale
  register counts are flagged in the receipt rather than repaired here.

Not selectable: any App surface (`projects/**`; read-only verification
excepted); any decision record; `TM-ROOT-106` or any other register row;
any `DEL-02-*` deliverable; the R17 steer or any prior ruling/steer; any
prior receipt byte; the closed PR #676 branch; `docs/**`, `agents/**`,
`tools/**`, `AGENTS.md`, `exports/**`, `skills/**`, `runtime/**`,
`_DomainEngines/**`.

## Sync rule

If `origin/main` advances mid-run, one non-rewriting sync is permitted under
the standing routine-sync authorization recorded in Receipt 125; record it,
and stop fail-closed if the sync changes any identity named in the basis
gate. A concurrent App tranche preparing an unmerged App seating PR writes
only App surfaces and is ignored.

## Rollback and abort

Any validation failure, identity disagreement, drift finding, or unexpected
write reverts the additions on the branch (or abandons the branch), verifies
that every pre-existing surface remains byte-identical to the basis, and
stops with a report. A stop-and-report is a compliant outcome of this steer,
not a failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set for any reason; if the act appears to require a
write outside the set, stop and report — the owner decides. No authority is
inferred from this steer beyond the recording and the one owner-ruled
register disposition it names.
