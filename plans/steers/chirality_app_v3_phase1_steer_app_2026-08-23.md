# APP-DEV LOOP STEER — v3 Phase 1: SCA-APP-008 Gate-3/Gate-4 amendment and propagation package — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: App-dev loop (`projects/chirality-app-dev/`). The loop's instruments govern; this steer directs one bounded phase under them. Companion instruments: `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md`, `plans/steers/chirality_app_v3_app_ruling_record_a2_2026-08-23.md`.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `436db9514a119c6d077e715f7c136882f3487772` (PR #644, App v3 Phase 0).
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`.
- `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` SHA-256 `f9b02806eeab1a578e6729c41fc367074758a2b95cc0eda9c8d2edbda446f314`.
- `plans/steers/chirality_app_v3_app_ruling_record_a2_2026-08-23.md` at the SHA-256 recorded in the PR that published this steer (both files merged together; verify against the merged bytes).
- `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` (still SCA-APP-007).
- `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6` (13 rows; byte-identity required at close as well).
- Frontend tree object `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb` for `projects/chirality-app-dev/frontend`.
- SCA-APP-008 assessment files at the exact SHA-256 identities listed in ruling record A2 (Brief `4bf54dc3…`, Impact `068c7b29…`, Carrier_Map `72a1b55b…`, Contract_Amendments.proposed `8a6a7999…`, DAG `0b721c2e…`, WORK_GRAPH `273c14cc…`, Handoff_State `7fa51832…`, DRAFT_NOTICE_TO_ROOT `8ebc728b…`, and the three Audit files).

## Authority context

A2-A accepts the SCA-APP-008 Gate-1/2 assessment as published, including the
DEL-02-05 account/consent UX and DEL-09-05 release-operations carrier
reassignments and the DEL-08-04/05 class-aware v3 delegation capability.
A2-B accepts all three SCC moves as orderings with feedback edges non-gating;
each SCC's separately stated downstream gate remains in force. A2-C
authorizes exactly this phase: draft the Gate-3/Gate-4 package and return it
for owner approval. Nothing in this steer applies an amendment, moves the
pointer, routes the Root notice, or touches contract, register, SOW,
lifecycle, code, docs, or frontend state as effective truth.

## N1 — Gate-3 amendment package (exact candidate texts)

Produce, inside the SCA-APP-008 snapshot folder, an exact amendment package
covering every surface the accepted assessment reaches, each entry carrying:
the target path; the pre-image identity (SHA-256 of the current file at the
basis, with line citations for the amended region); and the exact proposed
post-image bytes (full-file candidate or byte-precise hunk, per the loop's
Gate-5 byte-copy discipline — no paraphrase, no patch-edit re-expression).

Required coverage:

1. Decomposition/carrier surfaces for DEL-02-05, DEL-08-04, DEL-08-05, and
   DEL-09-05 — stable-ID amendments only; no topology change; WP-09
   authoring strictly separated from WP-11 owner acts in the DEL-09-05 text.
2. Contract amendment texts (K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1,
   K-EVENT-3, K-EVENT-4, K-EVENT-6, new K-CONSENT-1, new K-UNTYPED-1, and
   the consequential enforcement-map rows) carried as
   `CONCORDANCE_GATED_CANDIDATE` — explicitly not accepted truth. For
   K-EVENT-4, record the exact open concordance question (the exact live
   Root session path) as a question, not a resolved value.
3. The D-APP-103 deferral interaction restated unchanged (Brief.md line 55
   semantics); no decision-replay packet is produced in this phase.

## N2 — Gate-4 propagation plan

Produce an ordered, file-by-file propagation plan for a later Gate-5
application act: for every target, pre-image SHA-256 → post-image SHA-256;
the application order; the validator plan (including the App receipts
validator, register byte-identity, frontend tree identity, and candidate
whitespace); the post-application rerun obligations (dependency
re-extraction for amended carriers and a fresh named closure audit, per the
assessment's own PASS-cannot-substitute clause); a rollback statement; and
the A2-B SCC-ordering consumption plan with each SCC's downstream gate named
(SCC-ACCOUNT-MIGRATION-UX: accepted Root/App account/consent contract;
SCC-RUNBOOK-VALIDATION: G6a exact-candidate ruling). The plan must state
that `_LATEST.md` moves only in the separately approved Gate-5 act.

## N3 — Concordance workplan

A short workplan naming what Root/App concordance must resolve before the
contract candidates can be accepted: the K-EVENT-4 exact live Root session
path; any cross-loop invariant-ID collision; and the routing moment for
`DRAFT_NOTICE_TO_ROOT.md` (remains unrouted in this phase). Frame each item
as an owner/HELP_HUMAN decision input, not as resolved truth.

## Write set, exactly

- New files strictly inside
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/`
  (subfolder names per the loop's house convention; no existing file in the
  accepted assessment snapshot may be modified — the accepted bytes are
  frozen; additions only).
- Run/control evidence under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE1_2026-08-23/`.
- One append to `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
  (Receipt 196; parent Receipt-195; incorporate this steer and ruling record
  A2 by immutable path and SHA-256, the Receipt-195 convention).

Not selectable: `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md`;
any register, contract, SOW, `_STATUS.md`, `_DEPENDENCIES.md`,
`_Evaluation`, or `_Decomposition` file; anything under
`projects/chirality-app-dev/frontend/` or `projects/chirality-app-dev/docs/`;
any Root-loop path (`execution/**` at repo root, `plans/**`, `agents/**`,
`tools/**`, `docs/**`, `AGENTS.md`, `exports/**`); any other project.

## Discipline

- Return state: the package closes `AWAITING_OWNER_APPROVAL` with a
  four-state handoff; ReadyForNextPhase `NO`.
- Fresh independent package review with the unlimited-repair/fresh-review
  rule; every repair disclosed.
- Run the candidate-whitespace validator before generating any artifact that
  pins another artifact's hash; if a later repair changes pinned bytes,
  regenerate the pinning artifact or record exact pre→post lineage in the
  receipt (Root Phase-3 lesson).
- Run before pushing: candidate whitespace (base = the basis merge commit),
  agent instructions, instruction entrypoints, CI-form G4 (expect zero
  instruction-surface paths and zero required manifests), taskmgmt validate
  on the App register (byte-identity preserved), the App receipts validator,
  frontend tree identity, and `git diff --check`.
- Branch `codex/app-v3-phase1-2026-08-23`. Do not merge. If `main` advances,
  request sync authorization from the owner and record the grant verbatim in
  the receipt. HELP_HUMAN byte-verifies before endorsement.
