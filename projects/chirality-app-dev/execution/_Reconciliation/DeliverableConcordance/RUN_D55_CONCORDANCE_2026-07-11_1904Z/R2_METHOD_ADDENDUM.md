# R2 Method Addendum — adopted run-local method revisions, operationalized

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; applies to R1/R2/R3 execution.
- **Authority:** owner R0-gate ruling 2026-07-11 — "Adopt all 11 (Recommended)"
  (verbatim in loop Receipt 16; register row cell updated). This file
  operationalizes `R0_CALIBRATION/R0_CALIBRATION_REPORT.md` §4 MR-1..MR-11 into
  dispatch-ready rules; it extends the pinned plan §§6–7 contract run-locally
  and never weakens it (kernel §3). On any conflict with the pinned plan, the
  plan governs and the conflict is surfaced.

## Binding rules for every R2 claims CSV

1. **(MR-1)** `Disposition` records live concordance at the source state.
   Assessment recency lives exclusively in `AssessmentEvidence`, which MUST
   contain exactly one machine-scannable token: `OVERTAKEN`, `STILL CURRENT`,
   or `NOT APPLICABLE`. Reserve the `STALE_ASSESSMENT` disposition for rows
   where the overtaken conclusion is the operative defect (live surfaces agree
   and some surface still presents the stale conclusion as current truth).
2. **(MR-2)** `SelectableUnderCurrentLoop` is derived only for `REMAINING_WORK`
   rows; every other row carries `NO` by definition. A `YES` on a
   non-REMAINING row is an error.
3. **(MR-3, owner-ruled fork: per-wave transcript)** Behavioral verification
   evidence cites `GATE-TRANSCRIPT(W1@fac46e33f)`
   (`R1_INVENTORY/GATE_TRANSCRIPT_W1_fac46e33f.md`: typecheck exit 0, Vitest
   667 passed/4 skipped) PLUS the named test file/case (with line anchor where
   useful). Do not execute test suites; do not install dependencies. Fallback
   indirect binding (recorded pass at `61d70bdb0` + byte-identity diff) is
   permitted only if a row needs a state the transcript does not cover — name
   both elements.
4. **(MR-4)** Fold Datasheet restatements into REQ rows. Emit ACCEPTANCE rows
   only for datasheet-distinct conditions; ACC rows may cite their covering
   REQ rows' evidence.
5. **(MR-5)** Register defects get ledger rows: `ClaimID = REGISTER-<n>`
   (run-local numbering per deliverable), `ClaimType = REGISTER_DEFECT`
   (run-local extension), typical `Disposition = REMAINING_STATE_MISMATCH`.
   Use for `Dependencies.csv` / `_DEPENDENCIES.md` / `_REFERENCES.md` internal
   inconsistencies or metadata lag.
6. **(MR-6)** `RemainingGate` = concatenated verbatim suffixes, never
   normalized. `SelectableUnderCurrentLoop = NO` if ANY gate is unsatisfied.
   Cross-project gate status is derived ONLY from this project's own pinned
   surfaces (descriptors, catalogs, kit text at the source state); if no such
   surface states it, write `UNKNOWN` — never read another project's execution
   tree (F-APP-3 discipline).
7. **(MR-7)** `LatestDecision` distinguishes governance from context:
   `D-APP-nn` when the ruling governs the row; `D-APP-nn (context)` when it
   merely touches it; `NONE_FOUND` otherwise.
8. **(MR-8)** Tie-break: kit text flatly asserting a now-false state →
   `STALE_SPECIFICATION` (repair-shaped). Text acknowledging the gate where a
   ruling permits a bounded/transitional difference → `ACCEPTED_DIVERGENCE`
   (no repair implied).
9. **(MR-9)** Where a Specification was rewritten after its INSP-03 assessment,
   `AssessmentEvidence` cites `old-REQnnn` explicitly and states the
   old-ID→claim mapping, or "no direct conclusion".
10. **(MR-10)** Verification-basis vocabulary for non-behavioral claims —
    use these forms verbatim: `DOC-BASIS(D-APP-nn)`, `RUN-INSPECTION@<sha>`,
    `RULING-RECORD(D-APP-nn)`, `SNAPSHOT+LIVE-REVERIFY(<snapshot>)`,
    `GATE-TRANSCRIPT(W1@fac46e33f)`. For doc-only rows,
    `ImplementationEvidence` = `documentary claim` + the exact doc sections.
11. **(MR-11)** Authority-map interaction rule: the 2026-07-11 corpus
    re-ratification (v6) was lifecycle-scoped and did not re-adjudicate earlier
    ruled pivots; a ruled decision stands over older corpus wording that has
    not yet been transcribed into the corpus (AUTHORITY_MAP precedence note 1).
    Cite the ruling in `LatestDecision`; classify the corpus wording per MR-8.

## Unchanged from the pinned plan and the D-APP-55 ruling

19-column §6 header; §7 controlled dispositions (plus the single MR-5
ClaimType extension above); read-only discovery; evidence bound to the named
source state; no lifecycle transitions; no `CHECKING -> ISSUED` (F-APP-4); no
agent-workflow judgments (`DEFERRED_AGENT_WORKFLOW` routes to
`AGENT_WORKFLOW_OBSERVATIONS.md` at R3); claim-level dispositions only; no
agent disposition is a human ruling; `AUTHORITY_CONFLICT` on unresolvable
precedence — never choose.

## R2 wave artifacts

Wave outputs live in `R2_WAVES/PKG-XX/` as `<DEL-ID>_claims.csv` +
`<DEL-ID>_notes.md` (notes are lighter than R0: census; least-confident rows
with the alternative reading; register-defect summary; any method deviation —
no calibration self-report). Package summaries (`PACKAGE_SUMMARIES/PKG-XX.md`)
are derived by the orchestrator at wave fan-in from the claim rows (plan §7).
