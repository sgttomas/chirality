# D-PEC-79 carrier — PEC PRD v2.3 §16.3 loop-registry concordance

**Carrier state:** PREPARED / CONDITIONAL / NOT YET RULED / NOT EFFECTIVE

**DecisionID:** D-PEC-79

**Prepared:** 2026-08-09

**Owning loop:** PEC

**Preparation basis:** `origin/main@d269f0e04204bc463a11684499213b2283bd28f7`

**Live PRD preimage SHA-256:**
`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`

**Exact PRD v2.3 candidate postimage:**
`projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md`

**Exact PRD v2.3 candidate postimage SHA-256:**
`92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0`

## 1. Authority chain and preparation boundary

The owner ruled in-session on 2026-08-09, verbatim:

> PRD §16.3 candidate: ADOPT.

That ruling adopts only the exact semantic candidate and authorizes the
candidate's exact-postimage preparation mechanism. It does not adopt this
carrier or the byte-pinned PRD v2.3 postimage, apply any live edit, record
D-PEC-79 as ruled, or authorize Git closeout.

The non-authoritative preparation basis is:

`projects/pec/execution/_Coordination/PRD_V22_SECTION16_3_AMENDMENT_CANDIDATE_2026-08-09.md`
at SHA-256
`5b9cfef6976be2406d014d217d3a0106676f5e6d37edcc4328b07a83859ed97d`.

Accepted authority remains:

- D-PEC-78 O-A, which settled upstream PRD §16.3 / OI-003;
- SCA-004 Gates 1–5 and accepted SOFTWARE_DECOMP revision 1.4, which already
  propagated that product decision into decomposition truth; and
- the live PRD v2.2 until an exact-byte owner ruling and later application
  replace its bytes.

This carrier and the candidate postimage are coordination artifacts. They are
not product or decomposition authority before the next exact-byte owner act.

## 2. Exact candidate postimage

The candidate postimage starts from the live PRD v2.2 preimage identified
above and contains only these proposed changes:

1. Advance the header from v2.2 / 2026-07-27 / D-PEC-68-current to v2.3 /
   2026-08-09 / D-PEC-79-current.
2. Extend the epistemic-status paragraph to record the v2.3 §16.3
   concordance.
3. Add a v2.3 provenance block classifying the §16 heading/closing change as
   `CLARIFIED` and the §16.3 disposition as `TRANSCRIBED` from D-PEC-78 O-A
   and accepted SCA-004 revision 1.4.
4. Replace `## 16. Open product decisions (owner)` with
   `## 16. Product decisions (owner)`.
5. Preserve stable item number 3 and replace its open-question sentence with
   the exact adopted semantic wording that records D-PEC-78 O-A, the existing
   PEC-owned strict-version-1 JSON/schema paths, the core-owned typed
   `LoopRegistry` port, loop-local authority, owner-gated PEC configuration
   changes, graceful absence, and no implied duties.
6. Replace `None of these blocks P0–P2.` with
   `None of the remaining open decisions blocks P0–P2.`

The byte identity named at the top of this carrier is the complete proposed
live PRD postimage. No prose summary, diff, or later regeneration substitutes
for that hash.

## 3. Ruled behavior if and only if the owner adopts the exact bytes

If the owner later adopts both this carrier and the identified PRD postimage
by exact SHA-256:

1. PEC PRD v2.3 becomes the product definition of record after the separately
   authorized application tranche writes the exact postimage to the live PRD
   path.
2. PRD §16.3 records the already-settled D-PEC-78 O-A product disposition;
   the other eight §16 decisions remain open.
3. Stable `§16.3` citations remain valid because item 3 is not deleted or
   renumbered.
4. No new product meaning is created. The PRD is reconciled to the product
   ruling and already-accepted decomposition truth; the decomposition is not
   re-derived from this candidate postimage.
5. No SCOPE_CHANGE intake or SCA is opened because SCA-004 already propagated
   the identical meaning. Any owner amendment introducing new or conflicting
   meaning requires a separately gated SCOPE_CHANGE impact intake.

## 4. Exact proposed live path fence for a later ruling

The next owner ruling may authorize only these live paths:

1. `projects/pec/docs/PRD.md`
   - replace the exact preimage hash with the exact candidate postimage hash;
2. `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-79_prd_v2_3_section16_3_concordance.md`
   - materialize this carrier byte-for-byte as the D-PEC-79 decision carrier;
3. `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
   - add only the D-PEC-79 row recording the exact owner ruling, live PRD
     postimage hash, carrier hash presented with that ruling, and `RULED`
     status.

No standing plan, status, receipt, SCA, decomposition, source, configuration,
lifecycle, artifact, dependency, estimate, schedule, review, Task Management,
foreign-loop, or other path is in the proposed live fence. If any additional
path is desired, it requires an amended exact-byte packet and another owner
gate.

## 5. Later application sequence

No step in this section is authorized yet.

1. Re-run the PEC reliance-hold preflight for candidate validation and exact
   correction application.
2. Verify the live PRD still has preimage SHA-256
   `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
3. Verify this carrier and the candidate postimage match the exact hashes
   presented to and ruled by the owner.
4. Apply only the three-path fence in §4. The live PRD receives the candidate
   postimage byte-for-byte; the carrier receives no semantic rewrite; the
   register receives only the D-PEC-79 row.
5. Run the verification in §6.
6. Return Git closeout separately to CHANGE. Do not stage, commit, push, or
   merge as part of product adoption/application.

## 6. Verification

The later applying tranche must record all of the following:

1. The ruled immutable basis contains the exact live PRD preimage.
2. The applied live PRD SHA-256 equals
   `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0`.
3. The live D-PEC-79 carrier SHA-256 equals the carrier hash presented with
   the exact-byte ruling.
4. The final PRD diff from v2.2 is limited to the header/provenance and §16
   changes enumerated in §2.
5. D-PEC-78 and its packet remain byte-unchanged.
6. `_ScopeChange/_LATEST.md`, `_Decomposition/_LATEST.md`, SCA-004,
   `SOFTWARE_DECOMP.md`, and `ScopeLedger.csv` remain byte-unchanged at their
   accepted identities.
7. A targeted search finds no current PRD representation of §16.3 as open and
   confirms that the other eight §16 decisions remain open.
8. The changed live-path set equals §4 exactly; no unruled concordance path is
   included.
9. `git diff --check` and the applicable PEC governance/path checks pass.

## 7. Rollback

- Before Git publication, restore `projects/pec/docs/PRD.md` to preimage
  SHA-256
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`,
  restore the live decision register to its exact pre-application blob, and
  remove only the newly materialized live D-PEC-79 carrier.
- After Git publication, use a separately approved revert or successor
  product decision. Never silently rewrite D-PEC-78, D-PEC-79, the PRD
  adoption history, or SCA-004.
- No decomposition rollback exists in this tranche because no decomposition
  byte or pointer is authorized to change.

## 8. Non-effects

Preparation, exact-byte adoption, and later application do not by themselves:

- amend, reopen, supersede, rerun, or replace SCA-004;
- alter revision 1.4 decomposition truth, mappings, topology, counts,
  pointers, hashes, or derivative-closure state;
- open or execute a SCOPE_CHANGE gate;
- change `loops.json`, `loops.schema.json`, `RegisteredLoop`, `LoopRegistry`,
  adapters, tests, or any source/configuration byte;
- add, remove, retarget, activate, poll, or impose a duty on a loop or
  consumer;
- resolve any of the other eight PRD §16 decisions;
- update the standing plan, status, receipts, Task Management, lifecycle,
  dependencies, estimates, schedules, artifacts, reviews, releases, or
  reliance state;
- cure SCA-004's separately recorded stale derivative surfaces;
- authorize implementation, external writes, professional reliance, or
  another loop's act; or
- authorize Git staging, commit, push, merge, or publication.

## 9. Exact-byte owner decision still required

No ruling is recorded here. The owner must next identify:

- D-PEC-79;
- the live PRD preimage SHA-256;
- the exact PRD v2.3 candidate postimage SHA-256;
- this carrier's presentation-time SHA-256; and
- the exact three-path live fence in §4.

Only that later exact-byte ruling opens application. Silence, review,
recommendation, or the prior semantic `ADOPT` ruling does not.
