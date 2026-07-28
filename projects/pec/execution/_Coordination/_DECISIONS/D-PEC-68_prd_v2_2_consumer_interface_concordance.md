# D-PEC-68 — PEC PRD v2.2 consumer-interface concordance

**Status:** RULED AND EFFECTIVE
**Date:** 2026-07-27
**Immutable basis:** `7b0be4d8772a16e5a4774a17988479587d00acca`
**Accepted direct-postimage manifest:** `28ba2d1841f81977249d5f3f5da2ce864d2e9799d5013a6643bdf8192c4afd68`
**Accepted PRD v2.2 SHA-256:** `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`
**Selected release option:** `P2-B`

## Context

D-PEC-67 adopted exact replacement rows for PEC-K-03 and PEC-K-11. Those
rows make PEC a pull-oriented, non-authoritative interface whose explicitly
enabled consumer owns use, mode mapping, cadence, and any injection. The
application deliberately changed only those two PRD rows. A later
object-pinned concordance review found that surrounding PRD and live pointer
prose still carried the superseded harness-owned polling/injection model.

This decision adopts the exact successor postimages identified above. It does
not amend D-PEC-67 and does not use downstream decomposition to decide
upstream product meaning.

## Ruled behavior

1. **PRD v2.2 adoption.** `projects/pec/docs/PRD.md` advances from v2.1 to
   v2.2 as the exact accepted postimage.
2. **Protected invariant rows.** PEC-K-03 and PEC-K-11 remain byte-identical
   to the PRD rows adopted by D-PEC-67.
3. **Consumer-interface concordance.** The thesis, optional coordination
   surface, modes ladder, users/access, API latency rationale, uptake metric,
   falsification clause, and P2–P4 release wording are reconciled to
   pull-oriented, consumer-owned, never-forced use. No receiving loop gains a
   duty, cadence, injection requirement, or nonconformance condition.
4. **P2-B uptake observation.** The P2 exit records owner use or non-use as
   uptake/falsification evidence. Manual Step 0 remains available, and no PEC
   read or write becomes a governed duty.
5. **P3/P4 product boundary.** P3 and P4 supply PEC-side
   interfaces/adapters, streams, and measurement. Live consumer use requires
   its own receiving-owner authority. Non-adoption remains evidence about PEC
   and may falsify PEC; it is never receiving-loop nonconformance.
6. **D-PEC-61 transcription.** The stale P1 table parenthetical is corrected
   to the already-ruled first-ingestion direction: PEC's own build graph is
   first.
7. **Live-surface concordance.** PEC `AGENTS.md`, README, STATUS, and the
   standing workplan advance their current pointers and consumer-interface
   posture to v2.2. The historical D-PEC-57 framed-direction block and
   decision records remain unchanged.
8. **Downstream hold.** The proposed SCA-003 remains unopened. Read-only
   preparation does not open a gate. Any C3/C15 decomposition propagation
   requires a later SCOPE_CHANGE intake on the adopted PRD v2.2 Git identity.
9. **No implementation authority.** This act creates no implementation,
   runtime, lifecycle, release, dependency, estimate, schedule, external-loop,
   SCOPE_CHANGE-gate, ScopeOfWork, reliance-hold-release, or Git-closeout
   authority.

## Provenance discipline

- `TRANSCRIBED`: the protected PEC-K-03/-11 rows and D-PEC-61 P1
  first-ingestion direction.
- `CLARIFIED`: surrounding prose reconciled to D-PEC-67 without creating an
  external duty.
- `PROPOSED`: the P3/P4 capability-exit formulation, adopted only through
  this owner act.

The accepted candidate's `PROVENANCE_MAP.csv` and deterministic check are
derivative validation artifacts. They do not replace this ruling or the PRD.

## Exact fence

- `projects/pec/docs/PRD.md`
- `projects/pec/AGENTS.md`
- `projects/pec/README.md`
- `projects/pec/docs/STATUS.md`
- `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-68_prd_v2_2_consumer_interface_concordance.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md` (Receipt 115 only)

No historical decision, archived PRD, adopted decomposition, ScopeOfWork,
dependency register, source, runtime, profile, lifecycle, hold, estimate,
schedule, or external-loop surface is in the fence.

## Verification

1. Reproduce every direct-postimage hash in the accepted manifest.
2. Run the accepted deterministic candidate checker.
3. Confirm the current and candidate PEC-K-03/-11 rows are byte-identical.
4. Confirm every `TRANSCRIBED` source check passes.
5. Confirm the legacy categorical polling/injection anchors are absent from
   current live prose except preserved historical quotations explicitly
   labeled as superseded.
6. Confirm no SCA-003 snapshot or pointer exists.
7. Confirm the immutable basis descends from L-A2 merge
   `a01d8e01bf14db4d91fe3e3d13f7be43a11594ea`, contains its accepted
   ScopeOfWork/application archive, and preserves Receipt 114.
8. Run `git diff --check` and scope the staged paths to the exact fence.

## Rollback

Before Git closeout, restore the seven pre-existing surfaces to their exact
basis blobs and remove only the new D-PEC-68 decision record. After
publication, use a separately approved revert or successor decision. Never
rewrite D-PEC-67.

## Human ruling

Owner ruling of record, received in-session on 2026-07-27, verbatim:

> 1. D-PEC-68 / PEC PRD v2.2
>     Approve on main@7b0be4d…:
>     * Direct manifest: 28ba2d1841f81977249d5f3f5da2ce864d2e9799d5013a6643bdf8192c4afd68
>     * Carrier: 7109a60c90ec284b0dda7a49b2f8138c9d21ec343882f993a83dc41ba7481bb1
>     * PRD: 6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba
>     Select P2-B, preserve K03/K11, materialize Receipt 115, keep SCA-003 unopened, and return Git closeout separately.

## Transcript-correction disposition

The approved carrier named above contained a prospective paraphrase in its
Human ruling section rather than this actual compact owner ruling. That
carrier and its attempted materialization are `NON_APPLICABLE`; they are not
relied upon. This successor carrier corrects only the ruling transcript and
dependent identities. It preserves the approved PRD v2.2 semantic bytes,
P2-B, PEC-K-03/-11, the eight-path fence, Receipt 115, L-A2, the active hold,
and every authority exclusion. It becomes applicable only through the later
exact correction gate; that gate creates no additional product meaning.

## Application disposition

- Exact PRD v2.2 and current live-pointer/workplan postimages are adopted.
- P2-B is selected; owner use or non-use remains evidence, not a duty.
- D-PEC-67 remains preserved and effective.
- SCA-003 remains unopened.
- Git closeout requires a separate CHANGE gate.
