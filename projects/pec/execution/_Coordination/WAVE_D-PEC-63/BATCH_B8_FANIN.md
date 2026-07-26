# BATCH B8 FAN-IN — D-PEC-63 SOW initialization wave (internal fan-in; final batch)

**Date:** 2026-07-25 · **Decision:** D-PEC-63 · **Cadence:** internal
fan-in (owner cleared B3–B8; no halt re-armed) · **Verdict:** **B8
ACCEPTED — wave authoring COMPLETE (32/32)**

## 1. Member and final state

| Deliverable | Final sha256 | item_count | State |
|---|---|---|---|
| DEL-08-04 | `ef40833af6112f179d9021f036e37d78af486b9d39a19cb5d994bf693e5c3f23` | 16 | INITIALIZED |

The wave's terminal node (no exhibit row names it as a predecessor).
Four upstream contracts bound: DECLARED E-A28 → DEL-10-01 (C-10 verb
*baselines* via the SOW-058 Notes "baselines SOW-004/041", the E-A27
pattern, with the register-grounded token-cost vs wall-clock-latency
distinction the refuter verified as not an invented relation) plus
PROPOSAL E-N12/E-P51/E-P52 (DEL-08-03, DEL-04-01, DEL-08-01). The
numeric ≤100 ms p95 bound is bound as stated, unweakened, with the
enforcing act recorded as unowned (CON-006, owner-routed) — PRD §12 P1
exit tests and §11 metrics verified to name no latency condition.
Authoring first-pass PASS; status act 1/1
(`_run_records/TASK_RUN_2026-07-25_status_B8.md`).

## 2. Refutation (B8 round) and remediation

Sealed refuter (opus-5): **0 CRIT, 3 MAJ, 5 MIN**; verdict "accept
conditional on repair of F1–F3". Warrant (incl. the SOW-040/SOW-041
near-miss statement), bound handling, E-A28 stratum handling, both
generator-defect observations, perf-pattern conformance vs DEL-03-06,
and cross-wave latency-owner consistency across five accepted
contracts all verified clean at byte level (53-span quotation record
held).

- **F1 MAJ:** REQ-007's "each is cited to its owner" orphaned five
  acts (dashboard rendering, drill-down, incremental reconcile, drift
  classification, adoption) — the third wave appearance of the B6-F2
  class; the authoring run record shows the briefed one-for-one check
  was not performed → owners added from register cells (DEL-09-01 +
  PKG-09 family, DEL-09-06, DEL-03-02, DEL-03-03, DEL-10-12);
  CLM-012 phases extended; AC-016 now names PKG-09.
- **F2 MAJ:** CLM-012 staged DEL-10-11 at P2 against register P1 →
  corrected.
- **F3 MAJ:** "Three PKG-08 members" in the A002 cell; actual two →
  corrected.
- **F4–F6 MIN:** ContextBudgetQA row re-attributed off §8 prose;
  OI-010/OI-011 loci added (SOFTWARE_DECOMP §10); "hit is exact"
  softened to "list-membered by suffix compression". **F7:** ruled
  NO-ACTION (nothing false; §7 citation would be enrichment).
  **F8:** run-record `..`-census erratum (24→25) appended to the init
  record.

Revision: one sealed dispatch, 6 applied + F8 erratum, nothing
BLOCKED; post-edit owner check 17/17, phase check 28/28, censuses
unchanged, record counts and frontmatter unchanged. Independent
re-validation PASS; hash recomputed; register cross-check token-exact.
F4 discretion (drop the §8 conjunct rather than mint a new quoted
span) accepted as the smaller diff. The revision agent's CLM-005 note
(C-08 set restated inside a quoted register cell, outside CLM-012's
own-voice scope) dispositioned NO-ACTION — the established
own-voice/quoted-cell boundary.

## 3. Dispositions at this fan-in

1. **B6-F2 class recurrence (meta):** three appearances (B6, B8; B7
   caught at authoring). The one-for-one boundary-owner check is
   deterministic and register-readable — added to the closure
   handoff as a validator candidate for the OI-013/REQUEST item 2
   consolidation (a checkable rule: every act enumerated in a
   boundary-exclusion requirement resolves to a named owner in the
   cited claim).
2. **DEP-08-04-003 generator defect (both halves)** confirmed by the
   refuter; already inventoried in REQUEST item 2 at the B7 fan-in
   (the three PROPOSAL rows' empty-EvidenceQuote instances likewise).
   No new routing.

## 4. Verification numbers (wave-terminal)

Census `32 INITIALIZED / 32 OPEN` — calibrated terminal census (B8 =
32). Blocker snapshot (`BLOCKER_STATE_2026-07-25_B8_final.md`): **24
BLOCKED / 40 UNBLOCKED — exactly the calibrated closure state; all 32
wave members UNBLOCKED** (verified per-member). Invariants held (64
registers, 255 rows = 135 ANCHOR + 120 EXECUTION, standing-excluded
1). `analyze_dep_closure.py` at D-PEC-62 landing values, unchanged:
64 files, 255 rows, 64/0 schema, 135/120 ANCHOR/EXECUTION, 64
IMPLEMENTS_NODE, evidence 255/255, 62 nodes / 120 edges, orphans 2,
SCCs 0.

## 5. Next

STEP 5 closure: docs/STATUS.md authorized fixes (item-1 amendment +
four stale rev-1.1 lines); refutation R4 (reproduce every closure
number; receipt-claim audit; stale-pointer sweep); Receipt in
`_DomainEngines/pec/LOOP_RECEIPTS.md`; `_DECISIONS/_REGISTER.md` row;
`_COORDINATION.md` item; session-plan closure verdict; final commit +
merge to local main; owner presentation.
