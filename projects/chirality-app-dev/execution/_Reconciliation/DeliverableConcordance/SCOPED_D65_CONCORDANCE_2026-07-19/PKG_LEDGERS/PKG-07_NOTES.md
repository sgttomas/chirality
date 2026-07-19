# PKG-07 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (Instance G5)

Agent claims only; no verdict here is an owner act. Drift window: R6 basis
`c313325b7` → HEAD `ff2f68c82`.

## Counts

| Metric | Value |
|---|---:|
| Prior claim rows loaded | 125 |
| In-scope selected | 125 (all) |
| Confirmed (ScopedDisposition == PriorDisposition) | 110 |
| Re-dispositioned (delta) | 15 |
| New SCOPED rows minted | 2 (DEL-07-01-SCOPED-S01, DEL-07-01-SCOPED-S02) |
| DriftClass NONE | 88 |
| DriftClass RESOLVED | 29 |
| DriftClass PERSISTING | 8 |
| DriftClass NEW_DRIFT | 2 |
| HumanDecisionNeeded = YES | 0 |

Delta rows (15): DEL-07-01 ACC-001, REGISTER-1, REGISTER-2; DEL-07-02
ACC-001, REGISTER-1; DEL-07-03 ACC-001, REGISTER-1; DEL-07-04 REQ-014
(PARTIALLY_IMPLEMENTED → ACCEPTED_DIVERGENCE under D-APP-66), REQ-017
(→ ALIGNED), REQ-018 (→ ALIGNED), REGISTER-1, REGISTER-2; DEL-07-05
REGISTER-1; DEL-07-06 REQ-014 (→ ALIGNED), REGISTER-1.

## Selection reasoning

Every prior row is in scope under rule (a): in the drift window each PKG-07
deliverable's four-document kit (Datasheet/Specification/Guidance/Procedure)
was deleted and consolidated into a single `ScopeOfWork.md`
(`schema: chirality-deliverable-sow/v1`, D-GOV-16 Scope-of-Work Standard), so
the NormativeSource file of every claim changed. Rows whose substance rests on
changed shared frontend surfaces (tool-path-policy.ts, filesystem.ts,
read-tools.ts, options.ts, harness-contract package) additionally carry (b);
rows touched by post-R6 governed records (D-APP-66 ruling closure, R6 closeout
`_STATUS.md` edits) carry (c).

## Key findings

1. **Kit consolidation, content preserved.** The SOW files embed the four-doc
   content (CLM-numbered blocks) including the R5 (D-APP-56) repairs verified
   at R6. All requirement declarations re-checked in this pass read the same;
   only file/line anchors moved. Downstream consumers of the R3 ledger's
   `Specification.md line NN` anchors must re-anchor to ScopeOfWork.md CLM
   blocks.
2. **D-APP-66 ruled Option C (2026-07-19, owner in-session):** content-change
   SHA revalidation is NOT added to the status-transition surface; the gap is
   a governance/checklist concern surviving to issuance (F-APP-4). DEL-07-04
   REQ-014 re-dispositioned to ACCEPTED_DIVERGENCE; the D-APP-53-gated
   Remaining item is discharged (verified in `_STATUS.md` and the
   `TASK_RUN_2026-07-19_DAPP66_ruling_closure.md` run record). No code landed.
3. **All D-APP-55 concordance-bootstrap REMAINING rows RESOLVED:** R6 closeout
   (2026-07-12, in-window commit) completed the bootstrap and emptied the
   Remaining sections of all six deliverables.
4. **All REF-006 HASH_MISMATCH stale-spec/register rows RESOLVED:** R5
   repairs (P40/P45 annotations, DEP row retirements/satisfactions) are live
   in the SOWs and `_DEPENDENCIES.md` files; live registers show
   DEP-07-01-004, DEP-07-04-005, DEP-07-05-026, DEP-07-06-013 RETIRED and
   DEP-07-01-005, DEP-07-04-008 SATISFIED.
5. **Persisting residuals (8, all ungated proposal-only):** DEL-07-01 REQ-008
   (domain hook-error fixture); DEL-07-02 REQ-011/012/013 (scaffold
   path-policy and parser fixtures); DEL-07-03 REQ-010 (stale ASSUMPTION /
   "Integration test TBD" framing — the R3-proposed rewrite was not adopted in
   the R5 tranche); DEL-07-05 REQ-009 (spec's location-TBD branch vs stricter
   code), REQ-010 (no resolver-backed target check), REQ-017 (unknown-option
   warning not bound to dependency tools). Plus the DEL-07-05
   UNMAPPED anchor-count spec-refresh residual (PERSISTING on an ALIGNED row).
6. **New drift (2 rows, both minor doc-consistency):** DEL-07-01-SCOPED-S01 —
   post-R6 tool-path-policy additions (managed-child scope deny classes,
   symlink-READ rejection) on the shared surface are unclaimed by the
   DEL-07-01 kit (cross-package mapping to the managed-delegation surface
   proposed); DEL-07-01-SCOPED-S02 — the newly minted SOW carries "Code
   locations TBD" while the deliverable's own register records DEP-07-01-005
   SATISFIED with landed modules.

## Ambiguities

- DriftClass for DEL-07-04 REQ-014 is recorded RESOLVED although the
  implementation gap physically persists: the *drift* (undispositioned
  spec-vs-code divergence) is closed by the D-APP-66 ruling, not by code. The
  ledger row states this explicitly.
- Several SOW bodies retain dated stale phrases (e.g. DEL-07-06 "with REF-006
  hash warning" source tags) governed by top-of-document P40 dated-history
  notes; treated as RESOLVED under the run's append-only supersession
  convention, with optional non-blocking tidy proposals recorded.

## What was NOT examined

- Out-of-scope bulk stands on R3/R6: no re-verification of test-suite
  execution was possible or attempted (tool fence: no Bash). Behavioral
  verdicts rest on GATE-TRANSCRIPT(W1@fac46e33f), the R6 backcheck (255
  claim-reference records at the repaired basis), live code reads at HEAD for
  changed files, and byte-stability inferred from the frozen MANIFESTS for
  unchanged files. No fresh full-suite transcript exists for HEAD in this run.
- Changed test files (chirality-hooks.test.ts, permission-overlay.test.ts,
  deliverables-route.test.ts, workspace scanner test) were not re-read
  line-by-line; their presence in MANIFESTS plus live implementation reads
  ground the ALIGNED confirmations.
- `Dependencies.csv` files were adjudicated through their `_DEPENDENCIES.md`
  current-register mirrors (P40/P45 blocks), not by re-parsing the CSVs.
- DEL-07-02/07-03 SOW tails (procedure/guidance blocks beyond the read
  windows) were skimmed only to the extent cited; requirement and
  previously-defective sections were read in full.
- Assessment_INSP-03 files (annotated by the corpus-remediation E1 exercise
  for DEL-07-01) were not re-read; the E1 note is interpretation-only per the
  CORPUS-REMEDIATION-2026-07-18 run record.
