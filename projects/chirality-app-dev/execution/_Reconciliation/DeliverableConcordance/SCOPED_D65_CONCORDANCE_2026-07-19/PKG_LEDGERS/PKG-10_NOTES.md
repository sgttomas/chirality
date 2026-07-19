# PKG-10 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (instance G6)

Agent claims only; no verdict here is an owner act. Window: `c313325b7` (R6 repaired basis) -> `ff2f68c82` (HEAD). PKG-10 is the F-APP-3 fence-adjacent package; fence handling below.

## Counts

- In-scope selected: **105 of 105** prior claim rows (all of PKG-10).
- Confirmed (ScopedDisposition == PriorDisposition): **77**.
- Re-dispositioned (delta rows): **28** — DEL-10-01: REQ-002, ACC-001, ACC-002, ACC-004, UNMAPPED-1, UNMAPPED-2, REGISTER-1 (7). DEL-10-02: REQ-001, ACC-001, ACC-002, REGISTER-1 (4). DEL-10-03: REQ-003, REQ-004, REQ-005, REQ-010, EXC-002, UNMAPPED-1, REGISTER-1 (7). DEL-10-04: REQ-001, REQ-002, REQ-009, UNMAPPED-1, REGISTER-1, REGISTER-2 (6). DEL-10-05: REQ-004, REQ-007, ACC-001, REGISTER-1 (4). Every delta is drift->ALIGNED, produced by repairs/rulings the prior ledger predated: D-APP-56 R5 (P40 blanket notes, P41 REF-path repair, P43 INSP-03 superseding annotations UPD-091..094, P45 reconciliation notes UPD-148..157, P06 authority/kit transcription) plus post-R6 rulings D-APP-58, D-APP-59, and D-APP-65 dispositions 3/7.
- Persisting drift (**6 rows**): DEL-10-01 ACC-003; DEL-10-03 REQ-007, ACC-002; DEL-10-04 REQ-005/REQ-007/REQ-010 (test-shaped, ungated), plus DEL-10-04 REQ-012, ACC-001, ACC-002 (note-vs-row wording residue). All are doc-only or small-test repairs; proposals in the ledger.
- New rows minted: **1** — DEL-10-01-SCOPED-S01 (kit->SOW conversion provenance; UNKNOWN; HumanDecisionNeeded=YES; mirrors DEL-09-01-SCOPED-S01).

## F-APP-3 fence handling (per dispatch binding)

- **DEP-10-03-004:** re-verified live — `Dependencies.csv` row 5 remains `PENDING` and now carries the dated D-APP-65 note verbatim ("precursors to, not the accepted amendment"; F-APP-3 reaffirmed; LastSeen 2026-07-18). The DEL-10-03 REMAINING-1 ledger row records the item as discharged-by-ruling while the register row stays PENDING by design. No fence ambiguity: HumanDecisionNeeded=NO because the owner ruling itself is the disposition.
- **No `_DomainEngines/**` or `projects/chirality-piping/**` file was read or written by this instance.** Claims resting on `_DomainEngines` profile bytes (e.g. DEL-10-01 REQ-005/REQ-011 instance evidence) were confirmed from this project's own unchanged frontend surfaces plus prior R2/R6 evidence; the profile files themselves were not re-read (conservative fence posture; their absence from the package manifests means no in-window change is claimed either way).
- **DEL-10-03 REMAINING-2** keeps its `UNKNOWN` cross-project gate status: no app-dev pinned surface states piping-side `operation_applier.validate` transport soundness (MR-6 rule).

## Selection reasoning

All 105 rows are in scope under rule (a): the kit->SOW conversion deleted/replaced every deliverable's four-document kit in the window, and `_REFERENCES.md`/`_STATUS.md` (and for 10-03/10-04 the registers and new evidence/run-record files) changed. Post-R6 governed records under rule (c) bearing on PKG-10: D-APP-58 (adapter-manifest disposition), D-APP-59 (standing delegation + DEL-10-04 ResponsibleParty), D-APP-65 dispositions 3 (DEP-10-03-004) and context, the D-APP-52 live-LLM demonstration evidence (2026-07-18), and the D-APP-61/64 tranches touching harness-contract tool surfaces cited by PKG-10 claims.

## Path convention

`DEL-10-0X/<file>` = `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-0X_*/<file>`; `frontend/...` = `projects/chirality-app-dev/frontend/...`.

## Key findings

1. **The package's post-R6 story is closure, not drift.** DEL-10-04 discharged all four prior Remaining items (DEP-10-04-006/-007/-008 SATISFIED under D-APP-59/D-APP-58/UPD-157; DEP-10-04-004 judged precursors-not-amendment under the D-APP-59 S1 delegation, Receipt-56) and gained an assigned ResponsibleParty (Ryan Tufts). DEL-10-03 discharged the DEP-10-03-004 owner call (D-APP-65 disposition 3) and the live-LLM demonstration (owner-at-screen act, evidence in-folder). The only open PKG-10 Remaining items at HEAD: 10-01 staged-boundary advance (gated: new owner ruling), 10-01 headless-preview flip (stage-gated, piping side), 10-02 glob/hook packet (stage-gated), 10-03 open_pipe_stress transport (stage-gated, UNKNOWN), 10-04 CQ-F1 pec-fixture affinity (R4-P48 revisit-next-pass).
2. **Note-vs-row wording residue is the dominant remaining defect class:** dated reconciliation notes (UPD-148..157) correctly record the current state while a handful of operative rows still carry pre-repair flat assertions (ledgered as PERSISTING on 10-01 ACC-003, 10-03 REQ-007/ACC-002, 10-04 REQ-012/ACC-001/ACC-002). All repairs proposed are doc-only fold-ins.
3. **The four prior IMPLEMENTED_UNDOCUMENTED rows are re-dispositioned ALIGNED**: the staged surface is now documented in-kit as separately-ruled program work, and D-APP-65 disposition 3 pins formal deliverable adoption behind the future amendment gate. If the verifier prefers to keep IU until a decomposition mapping exists, that is the stated alternative reading; the operative facts (documented, ruled, gated) are not in dispute.
4. **Kit->SOW conversion (S01, HumanDecisionNeeded=YES):** same corpus-wide finding as PKG-09; provenance/authority record not locatable in the app-dev register.

## Ambiguities / confidence notes

- No Bash/Grep/Glob tools were available; all verification is Read-based. DEL-10-02's converted SOW was **not** directly re-read (its verdicts rest on the `_STATUS.md` UPD/P-entries, the R6 CLOSED/PASS backcheck of those updates, and the repair-pattern verified on the four sibling SOWs read in full or part) — DEL-10-02 ACC-001/ACC-002 confidence MEDIUM. DEL-10-03's Scope CLM beyond line 120 and DEL-10-01's Procedure-derived CLMs beyond line 200 were not exhaustively re-read (EXC-002 / ACC-004 confidence MEDIUM).
- Behavioral confirmations for surfaces changed in the window (tool-catalog.ts, tool-descriptor.ts, tool-names.ts, read-tools.ts, event-schema.ts, types.ts) rest on the ruled-tranche provenance (D-APP-61/64/65) plus premerge-CI-gated merges; no fresh full-suite transcript is bound to HEAD by this pass.
- The stale-hash-value class (superseded `ac35fba40` pinned as current) does not recur in PKG-10 operative rows: DEL-10-05's old-pair row sits under the P40 blanket quarantine and is noted, not minted.

## Not examined (stands on R3/R6)

No PKG-10 rows were left unexamined (all 105 re-adjudicated). Depth calibration: prior-ALIGNED rows whose evidence lives in window-unchanged modules (domain-profile.ts, operation-proposal.ts, domain-profile-registry.ts, domain-proposal-tools.ts and their tests) were confirmed on the unchanged-in-window basis plus prior R2/R6 verification without re-deriving full evidence chains; `_DomainEngines/**` bytes and the R2_WAVES evidence were not re-audited.
