# QA Report — COV_SCA002_POSTCHANGE_FINAL

## Scan coverage

Identical method and surfaces to `COV_SCA002_PRECHANGE_2026-07-25_1040`:
`SOFTWARE_DECOMP.md` parsed by heading-bound semantic section binding (§4
Packages, §5 Deliverables, §3 Objectives with range expansion, §7 telemetry);
`ScopeLedger.csv` 94 rows; `Deliverables.csv` 64 rows; `ContextBudgetQA.csv` 64
rows; 11 package folders; 64 deliverable folders; 64 `_CONTEXT.md`; 64
`_STATUS.md`.

## Parse issues

None. Every declared entity parsed cleanly.

## Limits of this run

1. **Artifact presence is not meaningfully measurable** — `AnticipatedArtifacts`
   holds prose, not filenames, and all 64 deliverables are `OPEN`.
2. **`OI-013` remains open** — this inline audit is a SCOPE_CHANGE-run
   baseline, not a standing build gate. It does not close `OI-013`.
3. **Semantic quality is out of scope** — whether a given objective
   attribution is *correct* was Gate 3 judgment, owner-ruled; this audit checks
   structural consistency only.
4. **Binding-table drift (`OI-A`)** — the `SOFTWARE_DECOMP` section numbers
   hard-coded in `AGENT_AUDIT_DECOMP.md` do not match the live document;
   resolved here by heading-text binding, as at the pre-change pass.

## Two-pass note

This is the second of two passes (plan amendment v2.1). The interim pass
`COV_SCA002_POSTCHANGE_2026-07-25_1252` returned one Check-10 blocker because
the SCA-002 snapshot was necessarily incomplete at that point. That snapshot is
retained as immutable first-pass evidence and is **superseded by this run** for
closure purposes.
