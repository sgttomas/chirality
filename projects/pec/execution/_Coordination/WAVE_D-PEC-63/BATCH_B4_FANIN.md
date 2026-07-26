# BATCH B4 FAN-IN — D-PEC-63 SOW initialization wave (internal fan-in)

**Date:** 2026-07-25 · **Decision:** D-PEC-63 · **Cadence:** internal
fan-in (owner cleared B3–B8; no halt re-armed) · **Verdict:** **B4
ACCEPTED**

## 1. Member and final state

| Deliverable | Final sha256 | item_count | State |
|---|---|---|---|
| DEL-03-01 | `756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19` | 17 | INITIALIZED |

The wave's convergence node: eleven upstream contracts bound (E-N14,
E-P10, E-P15, E-P18, E-P19..E-P25), all contract-only inputs, all
verified byte-faithful by the refuter. Warrant two-legged: SOW-010
register-direct (pre-SCA-002, "Valid but narrow" quoted at record
strength); SOW-021 fixed by the owner's Gate 1 constraint
SOW-021 ⊆ {OBJ-005} (ruled and closed — no owner-confirmation AC).
Authoring first-pass PASS; status act 1/1
(`_run_records/TASK_RUN_2026-07-25_status_B4.md`).

## 2. Refutation (B4 round) and remediation

Sealed refuter (opus-5): **0 CRIT, 3 MAJ, 7 MIN**. The
eleven-contract binding surface, both ledger rows, the SCA-002 warrant
chain, and the two-elision claim all survived adversarial reading.

- **F1/F2 MAJ:** CON-001's exhaustive negatives false — D-GOV-01
  Option A supplies the accepted CLASS referent for "generated views"
  (labeled generated artifacts under declared paths), and PEC-I-02 /
  PEC-DSH-002 / PKG-09 uses of "views" were missed. Effect: the
  contract's most consequential open item is a **citation-anchored
  instance-level gap** (which views, where), not an unwarranted
  permission needing SCOPE_CHANGE → R1/R2.
- **F3 MAJ:** obliged declared-view artifact outside the two-output
  bound; register admits only "Reconciler entry point + rebuild tests",
  so fixed as a declared component of OUT-001, not a new OUT → R3.
- **F4–F10 MIN** → R4–R10 (counts, cross-refs, stand-in conditioning,
  origination language; all applied).

Revision: one sealed dispatch, 10/10 APPLIED, item_count 17 unchanged,
elision count still exactly two, upstream quotes byte-unchanged.
Independent re-validation PASS; hash recomputed; register cross-check
exact ([SOW-010, SOW-021] / [OBJ-005]).

## 3. Dispositions at this fan-in

1. **DEL-02-03 feed-absence narrowness** (surfaced by R8): its contract
   obliges field-level best-effort limits (REQ-004) and
   malformed/unreadable at AC-004, but feed *absence* nowhere; its six
   PKG-02 siblings oblige the full condition set at REQ level.
   Dispositioned: **accepted narrowness** — REQ-001 uncovered-loop
   reporting covers the practical case; candidate for a later
   remediation packet; accepted B3 not re-opened.
2. **Register anomaly** (authoring run): DEP-03-01-006 (E-P15) is the
   only row of the eleven with an empty EvidenceQuote and SourceRef
   "location TBD"; the exhibit's E-P15 BasisCitation is likewise empty.
   Recorded as a register-hygiene observation for the OI-013/validator
   consolidation (REQUEST item 2 class); non-gating.
3. **CON-001 owner surfacing:** the instance-level "which generated
   views" gap plus CON-005 ("in full" vs limitation-bearing rebuilds)
   remain the contract's substantive open items — both carried as CONs
   with HUMAN_REVIEW routing at AC-017; they reach the owner at REVIEW,
   not as wave blockers.

## 4. Verification numbers

Census `19 INITIALIZED / 45 OPEN` — ladder match (B4 = 19). Blocker
snapshot (`BLOCKER_STATE_2026-07-25_B4.md`): 33 BLOCKED / 31 UNBLOCKED
(B3: 42/22; +9). Invariants held (64/255 = 135+120, standing-excluded
1). Newly unblocked: all six B5 members (DEL-03-02..04, DEL-04-01,
DEL-10-02, DEL-10-10) plus out-of-wave DEL-03-05 (P3), DEL-05-01,
DEL-05-02 (P2) — deferred to later packets by design.

## 5. Next

B5 = DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-01, DEL-10-02, DEL-10-10
(six; includes three C-08 standing nodes: DEL-03-04, DEL-10-02,
DEL-10-10 — standing-assertion pattern per DEL-01-05/DEL-10-03
precedent; DEL-04-01 carries the wave's first DECLARED-stratum edge
E-A27). Then B6, B7, B8.
