# D-PEC-66 — Post-repair follow-ons: E-N13 decline, DEL-10-10 REQ-011 repair, QA-item-20 dispositions

**Status:** RULED 2026-07-26 AT CREATION — EXECUTING
**Ruling (owner, verbatim):** "You are in the `HELP_HUMAN` posture as Agent 0.
I authorize: 1. decline E-N13 2. fold the DEL-10-10 fix into the next sealed
act now 3. the 9-contract QA items repair: proceed with parallel agents as
you see fit."
**Basis:** D-PEC-65 closure (Receipt 111; `../REPAIR_D-PEC-65/CLOSURE_2026-07-26.md`
owner-routed items) and the HELPS_HUMANS deferral-tranche coordination notice
(`../NOTICE_2026-07-25_helps_humans_p1_p7_applied.md`: DEL-10-10 boundary-owner
finding; QA-item-20 per-row disposition list).

## Ruled behavior

1. **E-N13 DECLINED (topology change).** Remove register row `DEP-07-05-004`
   (DEL-07-05 → DEL-08-02) from `PKG-07.../DEL-07-05_*/Dependencies.csv` and
   retire its two waiver rows (sidecar emptied by the sealed agent;
   file removal is a recorded dispatcher act at fan-in). Amend the
   deliverable-local `_DEPENDENCIES.md` derivative restatement to record the
   decline (annotate, never silently drop). Basis: repair-time search found
   no warranting text and DL-11 counter-evidence (seam is daemon-facing);
   edge was seeded PROPOSAL / LOW_CONFIDENCE / "owner may decline".
   **New calibrated invariants after this act:** 64 files, **254 rows = 135
   ANCHOR + 119 EXECUTION**, 62 nodes / **119 edges**, orphans 2, SCCs 0;
   zero waiver sidecars corpus-wide; validator exit 0 with **0 WARNINGs**;
   `--strict` exit 0. Blocker state re-measured, not assumed.
2. **DEL-10-10 `ScopeOfWork.md` REQ-011 repair (sealed revision of an
   accepted contract).** REQ-011 excludes DEL-03-02/DEL-03-03 acts citing
   CLM-017/CLM-018, neither of which names those owners. Fix per the
   verified finding: cite the claim that carries the owners, or extend the
   cited claim's enumeration truthfully — smallest honest diff; the revision
   agent reads the contract and chooses, flagging its choice. Post-state:
   `validate_scope_of_work.py` PASS; `check_boundary_owner_resolution.py`
   reports 0 failing contracts; new contract sha256 recorded. `_STATUS.md`
   untouched (remains `INITIALIZED`).
3. **QA-item-20 per-row dispositions (9 contracts / 21 flagged rows).**
   DEL-00-01(1), DEL-00-03(3), DEL-01-01(2), DEL-01-03(2), DEL-01-04(2),
   DEL-01-05(5), DEL-01-06(2), DEL-08-01(1), DEL-10-03(3). Per flagged
   multi-AC/multi-VER matrix row, the sealed agent rules: **CONFORMS**
   (row VER set = union of the row's ACs' own methods; recorded, no edit)
   or **OVER-LINKED** (repaired by splitting the row / trimming refs to
   exact linkage — content-preserving, no new scope, no AC or VER added or
   dropped). Every edited contract re-validates PASS; new sha256 recorded;
   derived-checklist changes noted (deriver re-run is the dispatcher's).

## Execution form

Parallel sealed Agent 2 dispatches (opus-5, file-tool-only, ≤4 in flight,
disjoint write sets): one for act 1, one for act 2, three for act 3
(3 contracts each). Dispatcher fan-in re-runs all validators; sealed
adversarial refutation precedes closure (standing steer). Records under
`execution/_Coordination/FOLLOWON_D-PEC-66/`.

## Fence (writes authorized by this packet)

- `PKG-07.../DEL-07-05_*/`: `Dependencies.csv`, `Dependencies_EvidenceWaivers.csv`
  (empty/remove), `_DEPENDENCIES.md`, `_run_records/`
- `PKG-10.../DEL-10-10_*/`: `ScopeOfWork.md`, `_run_records/`
- The nine act-3 deliverable folders: `ScopeOfWork.md`, `_run_records/`
- `PKG-08.../DEL-08-02_*/_DEPENDENCIES.md` — E-N13 downstream-mirror
  annotation *(fence amendment v1.1, 2026-07-26: the act-1 sweep found this
  live derivative mirror; annotating it is intrinsic to executing the ruled
  decline — dispatcher act, recorded in the closure record. DEL-08-02's
  `ScopeOfWork.md` CLM-002/AX-006 mentions cite the frozen exhibit as
  provenance and already carry "owner may decline" — truthful as written,
  left untouched, noted as residuals.)*
- `execution/_Coordination/FOLLOWON_D-PEC-66/**`; closure pointers
  (register row, receipt, `_COORDINATION.md` item, one-line STATUS
  amendment if warranted); scoped commits by explicit path; merge to local
  main. No `_STATUS.md` writes; no other surfaces.

## Rollback

`git revert` of the tranche commits restores the edge, waivers, and
contracts; pointer lines annotated, never deleted.
