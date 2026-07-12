# DEL-05-02 concordance notes (R2 Wave-2)

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: `frontend/` at `fac46e33f`
(byte-identical to `4c8ed8907`/`61d70bdb0`). Behavioral rows bind to
`GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed / 4 skipped).

## Census

Total rows: 25 (24 at initial submission; +1 at the fan-in revision below).

By ClaimType:
- REQUIREMENT: 15 (RQ-001..RQ-015)
- ACCEPTANCE: 2 (ACC-001, ACC-002)
- EXCLUSION: 5 (EXC-001..EXC-005)
- REMAINING_WORK: 1 (REMAINING-1)
- REGISTER_DEFECT: 2 (REGISTER-1, REGISTER-2)

By Disposition:
- ALIGNED: 20 — RQ-001,002,003,004,005,006,007,008,009,010,011,012,014,015 (14) + EXC-001..005 (5) + REMAINING-1 (1)
- PARTIALLY_IMPLEMENTED: 1 (RQ-013)
- STALE_SPECIFICATION: 2 (ACC-001, ACC-002)
- REMAINING_STATE_MISMATCH: 2 (REGISTER-1, REGISTER-2)

## Fan-in revision (orchestrator verification round)

The fan-in verifier confirmed all 8 rechecked rows as dispositioned; two refinements
(no disposition changes) followed:

1. **RQ-007 residual withdrawn (verifier correction, independently re-verified).** My
   initial notes posed an R3 check on whether the cancel path durably persists
   `turn.cancelled`. Re-verified this run: `frontend/src/lib/harness/turn-engine.ts`
   lines 327-353 durably persist `turn.cancelled` (reason `client_disconnect`, per the
   D-APP-40 comment at line 334) via `appendHarnessEvent` BEFORE best-effort provider
   shutdown, guarded by `cancellationPersisted` for idempotence — a live code path, not
   fixtures; exercised by `routes.test.ts` 1214-1235. RQ-007's ImplementationEvidence
   now cites turn-engine.ts:327-353, RemainingWork is NONE_OBSERVED, Confidence raised
   MEDIUM→HIGH, and RQ-007 is withdrawn from the self-flag list below.
2. **ACC-002 added (verifier flag adopted).** The stale Datasheet line 30 / Guidance
   lines 71-72 event names (`sdk.system.init`/`sdk.mirror.error` vs live
   `adapter.initialized`/`runtime.mirror.error`), initially folded into RQ-012's
   RemainingWork per MR-4, now carry their own STALE_SPECIFICATION row for the R5
   repair tally (MR-8: flat now-false kit text), matching the ACC-001 treatment.
   Additional check while adding it: live `docs/SPEC.md` (lines 570, 592) and
   `docs/TYPES.md` (lines 318, 340) already use the provider-neutral names — the
   staleness is kit-only, so the repair needs no corpus amendment. RQ-012's
   RemainingWork now points at ACC-002 instead of duplicating the finding.

## R1 index gap (recorded per brief)

`R1_INVENTORY/REQUIREMENT_INDEX.csv` contains ZERO rows for DEL-05-02 (the regex
parser scanned no IDs for this deliverable — the same known W2 parser gap the brief
warned about). `IMPLEMENTATION_SURFACES.csv` and `VERIFICATION_INDEX.csv` likewise
have no DEL-05-02 entries. Only `ASSESSMENT_INDEX.csv` (row 23), `REMAINING_INVENTORY.csv`
(row 26, one UNGATED bootstrap item), and `DELIVERABLE_INVENTORY.csv` carry DEL-05-02.
The real 15-requirement claim set (RQ-001..RQ-015) was re-derived directly from
`Specification.md` Requirements table (lines 26-40), Datasheet conditions, and the live
`frontend/` surfaces. The Specification uses `DEL-05-02-RQ-nnn` IDs (not `REQ-nnn`); I
kept the spec's `RQ-nnn` form.

## Cross-package context: DEL-03-03 UNMAPPED-1 (three /api/harness/* routes)

Sibling ledger `R2_WAVES/PKG-03/DEL-03-03_claims.csv` UNMAPPED-1 flagged three live
routes beyond the SPEC-17.1 catalog, one candidate-owned by DEL-05-02:
`/api/harness/session/[id]/events` (JSONL replay).

Finding: my Specification does NOT own this HTTP route. DEL-05-02's requirements cover
the replay-safe **library** (`session-events.ts::replayHarnessEvents`, RQ-008) and the
canonical **filesystem** path `.chirality/sessions/<sessionId>/events.jsonl` (RQ-014) —
never an HTTP route. Specification Out-of-scope bullet 3 (line 18) explicitly assigns
"Runtime replay/transcript view implementation" to DEL-05-04. The events HTTP route is a
thin consumer of my library and reads as DEL-05-04 (transcript view) or DEL-03-03
(harness API) surface. Per the brief I did **not** silently adopt it: the R3 ownership
question is left standing and recorded on EXC-003's RemainingWork cell. The route does
serve as one verification vehicle for RQ-008 (`routes.test.ts` 1214-1235, 1405+), which I
cite there. The permission (`/api/harness/permission`) and agents (`/api/harness/agents`)
routes are clearly not DEL-05-02 (permission is Out-of-scope bullet 1 / PKG-06; agents is
PKG-08) — no claim made.

## Assessment relocation (affects RQ-001,002,003,004,012,013,015)

INSP-03 (2026-06-21, SHA `18511e933`) cites `frontend/src/lib/harness/event-schema.ts`.
That file was relocated 2026-07-04 by the D-APP-48 harness-contract publishability ruling
to `frontend/packages/harness-contract/src/event-schema.ts` (pinned per D-APP-48 /
AUTHORITY_MAP implementation-evidence class). The assessment CONCLUSIONS still hold at the
new location; I re-anchored every row's ImplementationEvidence to the current path and
noted the relocation in AssessmentEvidence rather than treating the assessment as stale.

## Least-confident rows (with the reading that would flip them)

- **RQ-007 — self-flag withdrawn at fan-in.** Initially flagged over durable
  cancellation persistence on the cancel path; resolved affirmatively (see Fan-in
  revision item 1: turn-engine.ts:327-353 persists `turn.cancelled` on the live cancel
  path). The residual flip reading (ACCEPTED_DIVERGENCE if DEL-03-04 co-ownership is
  read as ongoing bounded divergence rather than resolved by D-APP-40) is recorded for
  completeness but no longer materially in doubt; Confidence is now HIGH.
- **RQ-010 (ALIGNED, MEDIUM).** Flip to PARTIALLY_IMPLEMENTED if RQ-010 is read to require
  schema-level size ENFORCEMENT (as INSP-03's PARTIAL implied). I read the requirement's
  literal wording ("stored as artifacts and referenced by path") as met, with numeric
  thresholds bounded out to DEL-05-05 (Spec Out-of-scope line 19, DEP-05-02-010).
- **RQ-008 (ALIGNED, MEDIUM).** The implementation tolerates ANY malformed line, not only
  a trailing tail (preserves valid records before and after). This is a superset of the
  spec; harmless, but a strict reader could call it IMPLEMENTED_DIFFERENTLY. INSP-03 rated
  it PASS with the same observation.
- **RQ-012 (ALIGNED, MEDIUM) + Datasheet drift.** The live taxonomy is provider-neutral
  (satisfies RQ-012). The stale kit category names, initially folded here per MR-4, were
  promoted to their own row ACC-002 (STALE_SPECIFICATION) at the fan-in revision — see
  above. RQ-012's remaining MEDIUM reflects only the breadth of the K-CORE-1/K-ENGINE-4
  claim versus the two named neutrality tests.
- **ACC-001 (STALE_SPECIFICATION, HIGH).** Confident. Live `_REFERENCES.md` shows REF-006
  MATCH and I reproduced the hash (`ac35fba40...c30bfd`) this run; the kit's HASH_MISMATCH
  wording is the operative stale surface. Mirrors the R0 exemplar DEL-02-01 ACC-001.

## Register-defect summary

Both defects are in `_DEPENDENCIES.md` (Dependencies.csv itself is internally consistent):
- **REGISTER-1** — "Declared Upstream/Downstream: TBD - no accepted dependency edges have
  been extracted yet" (lines 12-18) contradicts the file's own 12-row Extracted Register
  (lines 44-59). Metadata lag.
- **REGISTER-2** — `_DEPENDENCIES.md` counts 12 ACTIVE / 0 RETIRED and lists DEP-05-02-007
  as ACTIVE (lines 40, 54, 67-72), but `Dependencies.csv` marks DEP-05-02-007 RETIRED
  (retired 2026-05-24, RUL-SCC-001-RESIDUAL-001). Correct counts: 11 ACTIVE / 1 RETIRED.
  LatestDecision recorded NONE_FOUND — the retirement authority is a SCC residual ruling
  (RUL-SCC-001-RESIDUAL-001), not a D-APP-nn register decision (MR-7).

## Method deviations

None. 19-column header copied verbatim from the R0 exemplar. MR-1 tokens present on every
row; MR-2 (SelectableUnderCurrentLoop=YES only on REMAINING-1); MR-3 gate-transcript +
named test binding; MR-5 bare `REGISTER-<n>` ClaimIDs; MR-10 vocabulary used verbatim
(GATE-TRANSCRIPT, RUN-INSPECTION@fac46e33f, SNAPSHOT+LIVE-REVERIFY). No lifecycle
transitions, no deliverable-document edits, read-only throughout.
