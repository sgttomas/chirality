# W2 (PKG-04) — wave-local verification record

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; R2 Wave 2, PKG-04
  (DEL-04-01..05).
- **Roster (Receipt 18 steer):** five `opus` discovery agents; fan-in by
  `fable` at high effort (package-scoped, read-only); verdicts composed here
  by the fable orchestrator. No verifier edited any CSV; refutations returned
  to owning agents, who re-verified independently before editing.
- **Source state:** frontend/ at `fac46e33f` = HEAD `1625b396a` byte-identical
  (verifier reproduced the diff and the docs/PRD.md hash `ac35fba4…`).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Deterministic structural validation

0 errors / 0 warnings on every pass. Final: 115 rows (26+23+22+19+25).
(One pre-fan-in count: 118; three rows were dropped/folded by their owners at
fan-in — see §2.)

## 2. Fan-in recheck outcomes (44 rows rechecked)

| Deliverable | Rechecked | Confirmed | Refuted → resolution | Contested |
|---|---|---|---|---|
| DEL-04-01 | 14 | 14 | — | 0 |
| DEL-04-02 | 8 | 7 | UNMAPPED-1 (executable subagent definitions) → surface owned by DEL-08-04/SOW-063 per decomposition v3.2 line 353; owner accepted, dropped the row, folded consumption into REQ-013/EXC-004, removed NEW-PACKET, left an R3 handle toward the W3 PKG-08 wave. | 0 |
| DEL-04-03 | 9 | 7 | UNMAPPED-2 (artifact materialization) → owned by DEL-05-05/DEL-08-05 per decomposition; owner accepted, deleted the row, folded into REQ012 as owned-surface cross-reference. | REQ014 verifier-CONTESTED (ASSUMPTION-wording vs D-APP-52-gate instrument); owner resolved it by flipping ACCEPTED_DIVERGENCE → ALIGNED on the requirement-wording ground — no longer contested. |
| DEL-04-04 | 7 | 7 | — | 0 |
| DEL-04-05 | 6 | 4 | UNMAPPED-1 (settings escape hatch, IMPLEMENTED_DIFFERENTLY) → refuted on three grounds (SPEC §12.2 authorizes it; DEL-04-02-REQ-004/DEL-04-01-REQ-005 map it; the "no test" predicate false — sdk-options-builder.test.ts:309-328). Owner accepted, dropped the row, corrected the same false claim in RQ-015's evidence cell and notes. | **RQ-011 remains explicitly CONTESTED**: owner kept ALIGNED (classification is a source-level property, fully present; coverage gap in RemainingWork) vs verifier's per-class verification-bar reading (4 of 7 error classes not test-asserted by name; INSP-03 PARTIAL). Deciding fact: whether the §6 behavioral-verification bar applies per-class. R3/R4 input. |

Net: 44 rechecked — 39 confirmed, 3 refuted (all accepted), 1 contest
resolved by owner flip (REQ014), **1 standing contested row (DEL-04-05
RQ-011, ALIGNED-with-contest-note)**.

## 3. Cross-checks and R3 flags

1. All three refuted rows failed the same way: discovery tested for a
   deliverable-local mapping but not a corpus-wide one. R3 should treat
   decomposition-of-record assignments as accepted mappings when sweeping
   IMPLEMENTED_UNDOCUMENTED rows. DEL-04-03 UNMAPPED-1 (message.*/queue.*
   event lane) is the package's one surviving genuine coverage query.
2. REF-006 HASH_MISMATCH staleness confirmed in four kits (ACC-001 rows in
   04-01/02/05, PC-ACC-001 in 04-04) with DEL-04-03's inline-fold disclosed —
   one R5 doc-repair sweep candidate with PKG-05/PKG-06's same family.
3. Register-defect classes: DEL-04-01/02/03 REGISTER-1 are the
   "Declared Upstream/Downstream TBD narrative" class — **subject to the
   class-level inter-verifier conflict recorded in
   `R2_WAVES/PKG-03/_VERIFICATION.md` §3.5** (PKG-06's verifier refuted the
   class on SPEC §5.2; these three rows stand pending R3 harmonization).
   DEL-04-04 REGISTER-1 (retirement not mirrored) and DEL-04-05 REGISTER-1
   (discharged constraint still ACTIVE/TBD) are per-row lifecycle lags,
   unaffected by that conflict.
4. Open cross-package handles for R3: DEP-04-02-011 max-turn terminal
   consumer; PKG-05 transcript/store metadata closure; PKG-06/PKG-08
   fail-closed policy-input closure (DEL-04-02 REQ-014); DEP-04-04-008
   fingerprint consumer; D-APP-46 relocated tool-descriptor assessment
   pointers (evidence-pointer refresh candidate).
5. Notes-file corrections applied at fan-in: DEL-04-05 false "no test"
   claim (removed everywhere); DEL-04-02/04-03 censuses updated after row
   drops. Verifier confirmed the R1-index gap claims in all five notes files
   are accurate.
