# PKG-09 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (instance G6)

Agent claims only; no verdict here is an owner act. Window: `c313325b7` (R6 repaired basis) -> `ff2f68c82` (HEAD).

## Counts

- In-scope selected: **113 of 113** prior claim rows (all of PKG-09).
- Confirmed (ScopedDisposition == PriorDisposition): **95**.
- Re-dispositioned (delta rows): **18** — DEL-09-01 REQ-003, REQ-005, REQ-010, REGISTER-1, REGISTER-2; DEL-09-02 RQ-014, RQ-015, ACC-001, EXC-001, REGISTER-1; DEL-09-03 ACC-001; DEL-09-04 ACC-001, UNMAPPED-1, REGISTER-1; DEL-09-05 ACC-001, REGISTER-1; DEL-09-06 ACC-001, REGISTER-1. Every delta is drift->ALIGNED (repairs executed under D-APP-56 R5/R6 at or before the baseline, or rulings such as R4-P23/R4-P03 that the prior ledger predated).
- New rows minted: **3** — DEL-09-01-SCOPED-S01 (kit->SOW conversion provenance, UNKNOWN, HumanDecisionNeeded=YES), DEL-09-01-SCOPED-S02 and DEL-09-05-SCOPED-S01 (REF-006 hash-value lag after the in-window `docs/PRD.md` edit).

## Selection reasoning

Every prior row is in scope under rule (a): in the drift window the four-document kit files (Datasheet/Guidance/Procedure/Specification.md) of **every** PKG-09 deliverable were deleted and consolidated into a new `ScopeOfWork.md` (schema `chirality-deliverable-sow/v1`), and `_REFERENCES.md`/`_STATUS.md` changed — so each deliverable folder changed under every claim. Many rows are additionally (b) (shared frontend runtime/test surfaces changed under the ruled D-APP-61/64/65 tranches) and some (c) (D-APP-56 R4-P03/P23/P37/P48/P49 dispositions, D-APP-65 T2 test tranche, D-APP-66/67 rulings). InScopeReason lists the primary codes.

## Path convention

Evidence cells use `DEL-09-0X/<file>` as shorthand for `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-0X_*/<file>`; `frontend/...` for `projects/chirality-app-dev/frontend/...`. Line numbers are live-at-HEAD.

## Key findings

1. **Kit->SOW conversion (S01, HumanDecisionNeeded=YES).** The conversion carried the R5-repaired kit content faithfully (spot-verified across all six deliverables), but this discovery could not locate the authorizing/executing record inside the app-dev decision register (D-APP-01..67 enumerated; none records the conversion). The Scope-of-Work Standard is cited as ruled `D-GOV-16` by `execution/_Coordination/AgentRuns/CORPUS-REMEDIATION-2026-07-18/RUN_RECORD.md` (E1), but the D-GOV register itself was not found in the repo paths probed (docs/, root). Consequences ledgered on S01: all prior-ledger kit citations and register `EvidenceFile` cells now point at deleted files.
2. **Prior drift largely repaired.** All six ACC-001 PRD-hash rows, both DEL-09-01 register rows, and the four other register rows are repaired via one of two executed patterns: rewording (DEL-09-01, 09-04, 09-05, 09-06) or blanket `D-APP-56 R5 P40` current-state notes plus dated reconciliation CLMs (DEL-09-02, 09-03). The blanket-note pattern leaves the original stale sentences physically present as declared "dated drafting history" — treated here as RESOLVED, not PERSISTING, per the note's explicit supersession.
3. **Persisting drift is concentrated and mostly gated.** The packaging/release evidence family (09-04 REQ-002/003/004/005/008/009; 09-05 REQ-003/006/013/014/015; 09-06 REQ-002/015) persists by explicit ruling: D-APP-56 R4-P49 defers it to an owner-authorized release-preparation phase (recorded in the live `_STATUS.md` Remaining items). Ungated persisting items: 09-02 RQ-010 compaction fixture, 09-02 RQ-001 adapter_-name doc lag, 09-03 REQ-012 closure-record evidence, 09-06 REQ-013 retry e2e test, and the partially-executed CI-description repairs (09-01 REQ-007, 09-05 REQ-004, 09-05 REQ-012 — TBD/legacy wording persists beside correct reconciliation notes).
4. **New drift is minor:** REF-006 was rebaselined to `d95d826a1` after the in-window PRD edit; two SOWs (09-01 CLM-027, 09-05 CLM-004) still pin the superseded `ac35fba40` value as current (S-rows). MATCH status itself remains true.
5. **D-APP-65 T2 additive tests** (harness-anthropic-agent-sdk-manager.test.ts, +5, 82->87) shift line anchors cited by prior 09-06/09-03 rows; substance unaffected (RETURN_N4_CODE_TEST.md: pure insertions).

## Ambiguities / method notes

- **No Bash and no Grep/Glob tools were available in this session** (harness limitation); all verification is Read-based. Behavioral claims citing files changed in the window are bound to (i) anchor-presence re-reads at HEAD where load-bearing (turn-engine ATTACHMENT_FAILURE, permission-overlay hard-deny, package.json, premerge wrapper fixtures, workflow test) and (ii) the fact that every window change landed through ruled tranches whose merges passed the premerge CI gate (typecheck + full Vitest); **no fresh full-suite transcript is bound to HEAD by this pass** — verification-freshness caveat.
- DEL-09-06 REGISTER-1: the `Dependencies.csv` DEP-09-06-007 Notes cell was not independently re-read; RESOLVED verdict rests on the P40 annotation's after-UPD-077..079 statement (confidence MEDIUM).
- DEL-09-05 REQ-008's prior standing contest (K-VALIDATE-1 packaging interpretation) was routed to R3 and consolidated under D-APP-56; this pass found no window surface reopening it and did not re-litigate the interpretation.
- The DEL-09-04 CQ-F1 affinity items (R4-P48) are tagged "revisit: next concordance pass"; they are ownership questions outside this pass's claim re-adjudication and are re-sighted, not adjudicated.

## Not examined (stands on R3/R6)

Out-of-scope bulk: none for PKG-09 — all 113 rows were re-adjudicated because the kit conversion touched every deliverable folder. However, depth was calibrated: prior-ALIGNED rows whose cited frontend surfaces are absent from the changed-file manifests were confirmed on the unchanged-in-window basis plus prior R2/R6 verification, without re-deriving the full prior evidence chains; the R2 evidence itself (R2_WAVES/PKG-09) was not re-audited.
