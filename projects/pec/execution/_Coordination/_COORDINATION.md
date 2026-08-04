# Coordination Record

**Representation:** Full dependency graph (DAG)
**Dependency tracking mode:** FULL_GRAPH
**External schedule / coordination artifact:** N/A
**Default maturity threshold (if computing blockers):** `INITIALIZED` — owner-ruled 2026-07-25 (Phase 1.3 gate)

## Provenance

- Representation and mode are **owner-selected**, not agent-chosen: `D-PEC-61`
  ruled behavior 2 ("`FULL_GRAPH` is the owner-selected coordination
  representation for PEC Project Setup") and the SCA-001 closure released
  PROJECT_SETUP with `FULL_GRAPH` already selected
  (`execution/_Decomposition/_LATEST.md`, `execution/_ScopeChange/_LATEST.md`).
- Accepted upstream basis: `execution/_Decomposition/SOFTWARE_DECOMP.md`
  revision **1.4** (`current_basis`, SCA-004 successor, accepted
  2026-08-03 under D-PEC-78 O-A; evidence
  `execution/_ScopeChange/SCA-004_2026-08-02_2325/`). Historical:
  revision 1.1 was the basis at this gate's ruling, revision 1.2 was accepted
  through SCA-002, and revision 1.3 through SCA-003; read
  `execution/_Decomposition/_LATEST.md` first, always.

## Phase 1.3 owner rulings (2026-07-25 gate)

1. Maturity threshold: **`INITIALIZED`**.
2. Register storage: **deliverable-local `Dependencies.csv` (v3.1) +
   `_DEPENDENCIES.md`**, seeded at scaffolding; full accounting
   reconstructed on demand (`tools/coordination/analyze_dep_closure.py`);
   **no standing central register** — owner declined the central-aggregate
   pattern as "another surface for authority."
3. DAG candidate v0.2 **accepted, all strata as presented** (120 edges,
   10 constraints, 5 STANDING nodes) — exhibit in
   `PLAN_2026-07-25_project_setup_dag_gate.md`.
4. Phase-precedence and PHASE_TENSION items remain recorded flags/erratum
   candidates (PLAN §7); they do not alter threshold-based blocker
   arithmetic.
5. **`D-PEC-62` RULED and executed 2026-07-25:** scaffolding + local-register
   seeding authorized and landed — 11 packages / 64 deliverables (`OPEN`),
   64 deliverable-local `Dependencies.csv` (v3.1) + `_DEPENDENCIES.md`
   seeded from the frozen gate exhibit (evidence:
   `SEED_D-PEC-62/RUN_LOG.md`, Receipt 108). Blocker computation is active
   in advisory-reporting form from deliverable-local registers only.
6. **`D-PEC-64` RULED and SCA-002 closed 2026-07-25:** decomposition
   revision **1.2** accepted (`current_basis`) — deliverable→objective
   mapping completed for the O-A wave-minimum scope; all 32 Phase 2.2
   wave members now carry non-empty `SupportsObjectives`; residue 11 IN
   rows / 9 deliverables retained by design. Evidence:
   `execution/_ScopeChange/SCA-002_2026-07-25_1042/`, Receipt 109.
   Executed under owner-directed Agent 0 orchestration (managed
   SCOPE_CHANGE instance; control plane
   `AgentRuns/RUN_2026-07-25_sca002/`). Re-pins executed 2026-07-25
   (`6e558a2c0`). Next: the D-PEC-63 draft-v2 ruling *(ruled and
   executed — see item 7)*.
7. **`D-PEC-63` EXECUTED 2026-07-25:** the Phase 2.2 scope-of-work
   initialization wave is complete — all 32 wave deliverables (3 pre-P1 +
   29 P1) carry validated `ScopeOfWork.md` production contracts at
   `INITIALIZED` (terminal census 32 INITIALIZED / 32 OPEN; advisory
   blocker state 24 BLOCKED / 40 UNBLOCKED, all wave members unblocked;
   dep-closure invariants unchanged). Batches B1–B8 each closed with
   fan-in, sealed adversarial refutation, sealed revisions, deterministic
   status acts, and scoped commits; durable records at
   `WAVE_D-PEC-63/BATCH_B{1..8}_FANIN.md`. Evidence: Receipt 110. Open
   carries: DEL-04-05/DEL-08-03 seam gap (SCA candidate), OI-013
   register-anomaly inventory + boundary-owner validator candidate
   (routed, `REQUEST_2026-07-25_helps_humans_tooling_consolidation.md`),
   OI-B pointer sweep (deferred). Next: P1 build-slice packets
   (owner-gated; `F-PEC-1` fences source work); WORKING_ITEMS is the
   post-wave owning workflow.

8. **`D-PEC-65` RULED and EXECUTED 2026-07-25/26:** the OI-013 register
   evidence repair — all 120 EXECUTION rows across the 64 deliverable-local
   `Dependencies.csv` registers dispositioned row-by-row: **119 repaired**
   (real locus + 100% machine-verified verbatim quote + coherent
   `EvidenceFile`; the frozen D-PEC-62 exhibit is cited nowhere) and **1
   honestly waived** (`DEP-07-05-004`, two declared waiver rows with
   attributed rationale; the search found DL-11 counter-evidence — an
   owner-routed edge-validity question on E-N13). Validator:
   exit 0, 0 ERROR / 2 waiver WARNINGs (`--strict` exit 1 by design);
   EVQ-001 87→0, EVQ-002 held 0, empty-evidence 33→1-waived. Invariants
   byte-stable (64 files / 255 rows / 62 nodes / 120 edges / orphans 2 /
   SCCs 0; census 32/32; blocker 24/40). Closure refutation (44-row
   aptness sample + full-corpus defect scans): 0 CRIT / 7 MAJ / 6 MIN —
   14 inapt-locus rows remediated by fresh sealed revision, backchecked
   clean; 11 flagged `Statement` edits verified at cell level (0
   unflagged). Records: `REPAIR_D-PEC-65/`. Evidence: Receipt 111.

9. **`D-PEC-66` RULED and EXECUTED 2026-07-26** (owner ruling verbatim in
   the packet): **(1) E-N13 DECLINED** — register row `DEP-07-05-004`
   removed, waiver sidecar retired (zero waivers corpus-wide), both
   derivative mirrors annotated; **(2) DEL-10-10 REQ-011 repaired** (CLM-018
   extension; boundary checker 0 failing); **(3) QA-item-20 — all 21
   flagged rows across 9 contracts ruled OVER-LINKED** (operative test:
   QA item 20 in full; clause 1 passed 21/21, clause 2 failed 21/21) and
   repaired by content-preserving splits; deriver warnings → 1 recorded
   exact-union grouping. **This item supersedes item 8's invariant
   numbers:** the calibrated corpus state is now 64 registers / **254 rows
   = 135 ANCHOR + 119 EXECUTION** / 62 nodes / **119 edges** / orphans 2 /
   SCCs 0; validator **0 ERROR / 0 WARNING, `--strict` exit 0**; zero
   waivers; census 32/32; blocker 24/40 (unchanged by the decline —
   DEL-07-05 remains blocked on DEL-00-02). Closure refutation 0 CRIT /
   0 MAJ. Records: `FOLLOWON_D-PEC-66/CLOSURE_2026-07-26.md`; evidence
   Receipt 112. The three Receipt-111 owner-routed items are CLOSED by
   this tranche.

10. **SCA-003 / PROJECT_SETUP reference parity (2026-07-28):**
    decomposition revision **1.3** is accepted `current_basis`; all 64
    deliverable `_REFERENCES.md` packets are re-pinned to PRD v2.2 and
    revision 1.3. `D-PEC-69` subsequently reconciled the complete
    execution-time-confirmed eleven-contract affected population, and
    `D-PEC-70` released `PEC-HOLD-001` after full-corpus and independent
    validation. Lifecycle, topology, dependencies, implementation, estimates,
    schedules, and ordinary production gates remain unchanged.

11. **Step-5 loop-readiness pass (2026-07-29, GOV-STEP5-LOOPS-20260729):**
    the 61 deliverable `_CONTEXT.md` Provenance blocks still stopping at
    revision 1.2 were repaired to record the revision 1.3 (`current_basis`,
    SCA-003) succession, matching the three files already updated; the
    next-work readiness slate was published at
    `execution/_Coordination/PEC_NEXT_WORK_SLATE_2026-07-29.md`. Hygiene and
    presentation only — no packet drafted, nothing ruled or activated;
    `F-PEC-1` and all production gates unchanged. (This tranche's ledger
    entry could not be appended to `_DomainEngines/pec/LOOP_RECEIPTS.md`,
    which lies outside the tranche's `projects/`-only write scope; recorded
    here instead.)

12. **SCA-004 metadata alignment and currency sweep (2026-08-03):**
    revision **1.4** is accepted `current_basis`; SOW-077 maps to
    `PKG-01 → DEL-01-06 → OBJ-004`, SOW-094 carries the settled implementation
    basis, and OI-003 is resolved by D-PEC-78 O-A. PROJECT_SETUP completed its
    exact subset: 64/64 context provenance blocks, 64/64 reference packets,
    and the DEL-01-06 non-gating SOW-077 anchor; strict registers remain clean
    at 64 files / 255 rows, and topology remains 119 execution edges / zero
    SCCs / zero bidirectional pairs. Evidence:
    `PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`.
    WORKING_ITEMS refreshed the present-current maps and appended
    supersession annotations to the four mutable historical handoffs, with
    evidence at `WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/`.
    TM-PEC-023 is held pending an exact SCOPE_CHANGE mapping-or-retain-blank
    ruling; DEL-01-06 RF-002 remains separate and open. No SOW, REVIEW,
    lifecycle, source, release, reliance, or foreign-loop act is inferred.

    Three historical handoffs are immutable and remain byte-identical. Their
    present-current superseding pointers are recorded here instead:

    - `execution/_Reconciliation/DeliverableConcordance/PEC_SOW_V22_SCA003_RECON_2026-07-28/HANDOFF_STATE.md`,
      SHA-256 `b92f52396e0d25bf40d04c0bef26f21077064174bb02d4c24c5f23d13f0794ee`
      → D-PEC-70 hold release, `execution/_Decomposition/_LATEST.md`, and the
      SCA-004 / PROJECT_SETUP / WORKING_ITEMS handoffs.
    - `execution/_ScopeChange/SCA-003_2026-07-28_0824/Handoff_State.md`,
      SHA-256 `ee5624241ac383aab49d0381f9c9f3b31a439888aec39a5f1016ab9aeeae3632`
      → `execution/_ScopeChange/_LATEST.md` and the SCA-004 handoff.
    - `execution/_Coordination/PROJECT_SETUP_REFERENCE_PARITY_2026-07-28/HANDOFF_STATE.md`,
      SHA-256 `604826885cd39aedb85fee1f53079123d4389496f3ec48ed3f437944877fd545`
      → `PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`.

13. **Superseding owner direction for remaining derivative lanes
    (2026-08-03):** TM-PEC-023 is directed to a dedicated SCOPE_CHANGE mapping
    session; neither an exact mapping nor blank retention is ruled, its nine
    semantic bytes and COV-062..COV-070 remain open, and no downstream gate or
    urgency is created. RF-002 disposition is `REVISE`, but revision and exact
    REVIEW acceptance are separately scheduled; RF-002 remains `TBD / OPEN`,
    Gate 5 remains HOLD, and DEL-01-06 remains `INITIALIZED`. Metadata alignment
    is cleared. Derivative state remains `INCOMPLETE` for exactly three
    component categories: (1) TM-PEC-023 mapping-session amendment; (2) RF-002
    revision plus exact REVIEW acceptance; and (3) ordinary SOW/SPEC currency
    under SCA-004 / TM-PEC-013/014 for DEL-02-07, DEL-03-01, DEL-04-01, and
    DEL-00-03. This item records no row closure.

## Notes (human-owned)

- Scaffolding and local-register seeding were authorized by `D-PEC-62`
  (RULED 2026-07-25) and executed the same day; further build tranches
  (the P1 slice) still require their own owner-ruled `D-PEC` packets per
  `docs/STATUS.md`.
- The owner-accepted dependency-DAG exhibit is embedded in
  `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` and
  is now **frozen gate provenance**: the deliverable-local
  `Dependencies.csv` registers are the sole live dependency basis. Both
  are derivative packages citing the accepted decomposition snapshot
  (revision 1.1 at seeding; revision 1.4 is `current_basis` since
  SCA-004, with topology and execution-dependency bytes preserved) and are never a
  substitute for decomposition truth.
