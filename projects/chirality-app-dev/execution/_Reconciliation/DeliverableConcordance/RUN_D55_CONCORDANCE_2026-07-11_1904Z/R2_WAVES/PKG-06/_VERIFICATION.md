# W2 (PKG-06) — wave-local verification record

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; R2 Wave 2, PKG-06
  (DEL-06-01..06).
- **Roster (Receipt 18 steer):** six `opus` discovery agents; fan-in by
  `fable` at high effort (package-scoped, read-only); verdicts composed here
  by the fable orchestrator. Refutations returned to owning agents; owners
  re-verified independently before editing.
- **Source state:** frontend/ at `fac46e33f` = HEAD byte-identical (verifier
  reproduced the diff, the PRD hash, and — per the fan-in brief's directed
  sample — verified 40+ D-APP-48 re-anchored citations across
  `frontend/packages/harness-contract/` and seven test files all exist at the
  cited lines; the old `src/lib/harness/tool-descriptor.ts` path is dead).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Deterministic structural validation

Final pass: 0 errors / 0 warnings; 131 rows (22+22+23+22+20+22). Three rows
were dropped and one reworked at fan-in (see §2), from a pre-fan-in 134.

## 2. Fan-in recheck outcomes (34 rows rechecked + directed ALIGNED sample)

| Deliverable | Rechecked | Confirmed | Refuted → resolution | Contested |
|---|---|---|---|---|
| DEL-06-01 | 6 | 5 | REGISTER-2 ("corpus v2" labels) → not a defect: provenance-accurate, `[HISTORICAL WARNING]`-tagged narration of the ADQ-11-era event; no false current-state assertion. Owner accepted, dropped the row. | 0 |
| DEL-06-02 | 6 | 3 | UNMAPPED-2 (mutating tools) → accepted mapping exists intra-package (DEL-06-04 Spec REQ-010 line 40); owner reworked it as exclusion row EXC-005 (ALIGNED), R3 question withdrawn. REGISTER-1 (Declared-TBD narrative) → refuted on SPEC §5.2 (human-owned Declared sections, TBD by design); owner accepted and dropped, preserving the "extracted"-wording nit as a notes observation. | **REGISTER-2 stands explicitly CONTESTED** (owner kept it, LOW confidence, HumanDecisionNeeded=NEW-PACKET): single-row SATISFIED advance beside four equally-MATCH TBD siblings — defect vs by-design; deciding fact is whether ADQ-11/D-APP-43 scope obligated sibling-row review. R3/R4 input. |
| DEL-06-03 | 5 | 5 | — (EXC-005 ACCEPTED_DIVERGENCE upheld — flat exclusion vs five ruled domain tools on the owned surface; distinct from DEL-06-04 EXC-005 ALIGNED, both correct; STILL-CURRENT token treatment on relocated-evidence REQ rows upheld). | 0 |
| DEL-06-04 | 4 | 4 | — | 0 |
| DEL-06-05 | 7 | 7 | — (REGISTER-1 CONFIRMED but NARROWED by its owner to the single present-tense false cell — DEP-06-05-008 Notes "PRD remains warning-qualified"; the v2 provenance labels are excluded from the defect and from R5 scope). | 0 |
| DEL-06-06 | 6 | 5 | REGISTER-1 (Declared-TBD prose) → refuted on the same SPEC §5.2 basis; owner accepted and dropped. Notes corrections applied: `HarnessToolPermission` has a sixth member `'danger'`; UNMAPPED-1's hook.progress coverage is ZERO (strengthens the row). | 0 |

Net: 34 rechecked — 29 confirmed (one narrowed), 4 refuted (all accepted),
**1 standing contested row (DEL-06-02 REGISTER-2)**. Final census: 131 rows —
ALIGNED 113, STALE_SPECIFICATION 9, REMAINING_STATE_MISMATCH 4,
IMPLEMENTED_UNDOCUMENTED 3, ACCEPTED_DIVERGENCE 2.

## 3. Cross-checks and R3 flags

1. **Class-level inter-verifier conflict originates here:** this package's
   verifier refuted the "Declared Upstream/Downstream: TBD" register-defect
   class on `docs/SPEC.md` §5.2 (verified by the orchestrator), while
   PKG-03/04/05 verifiers confirmed identical rows without consulting §5.2.
   PKG-06's two class rows are dropped (owners accepted); the six standing
   same-class rows elsewhere (DEL-03-02 REGISTER-2, DEL-03-03 REGISTER-1,
   DEL-04-01/02/03 REGISTER-1, DEL-05-02 REGISTER-1) plus merged W1 rows
   (DEL-02-02 REGISTER-1, DEL-02-03 REGISTER-1) await R3 harmonization —
   full statement in `R2_WAVES/PKG-03/_VERIFICATION.md` §3.5.
2. PRD-hash STALE_SPECIFICATION family uniformly confirmed across all six
   kits (~80 stale HASH_MISMATCH assertions, one root cause: D-APP-38/ADQ-11
   never transcribed into kit text). Natural single package-wide R5 tranche;
   the MR-4 fold divergence (standalone ACC rows vs folded REQ-016/REQ-014)
   is justified by covering-requirement presence.
3. Mutating-MCP ownership split internally consistent after fan-in
   (DEL-06-04 owns; DEL-06-03/DEL-06-02 exclude).
4. Cross-package handles for R3: domain-roster formal ownership (DEL-06-02
   UNMAPPED-1 ↔ PKG-10/D-APP-50/51/52); subagent permission-class owner
   (DEL-06-01 UNMAPPED-1 ↔ D-APP-10 bridge, PKG-08 W3); `session-events.ts`
   owning deliverable (DEL-06-01 REGISTER-1 ↔ PKG-05); hook.progress adoption
   (DEL-06-06 UNMAPPED-1); Bash timeout numerics ruling (DEL-06-05 UNMAPPED-1
   NEW-PACKET, Guidance conflict DEL-06-05-TIMEOUT-001); DEP-06-03-007 schema
   alignment with DEL-07-05 (W3).
