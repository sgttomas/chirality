# T8 — Independent spot check of the final R3 concordance (blind)

Read `_COMMON.md` first. Also read CONVENTIONS §1, §2.3 (reach), §2.4 (named questions; R4-Q1 subject
test), §2.6 (dispositions, tie-break, absence rule) and RUN_BASIS Addenda 3–11.

**You are blind to R3's reasoning.** Do NOT open `<RUN>/R3/REMAP_LOG.csv`, `<RUN>/R3/_work/T*_*`
files, `<RUN>/R3/RUNWIDE_CALLS.md`, or the `Notes` column of the concordance files. Judge each item
from the claim text in the frozen tree, the frozen code and records, and the rulebook. You may read the
sealed R2 ledgers only to find the deliverable text a row points at.

**Input.** Your sample file (named in your dispatch prompt), one row per item:
- `S1-*` rows (stratified ~5% sample): check the final `Disposition` (and note any clear error in
  `HumanDecisionNeeded`).
- `S2-*` rows (every AUTHORITY_CONFLICT and UNKNOWN row): check `Disposition` and
  `HumanDecisionNeeded`. Do every `MANDATORY` row; then as many `OPTIONAL` rows as your budget allows,
  in file order.
- `S3-*` rows (30 R3 re-mappings): `CheckField` changed from `PriorValue` to `RemappedValue`. Decide
  whether `RemappedValue` is right under the rulebook and the evidence.

**Verdicts.** `CONFIRMED` (the checked value is right), `REFUTED` (it is wrong: give the value you
would put, with evidence), or `UNVERIFIABLE` (the evidence roots cannot settle it: say why). For an
off-code event (signing, notarization, publication, CI or manual steps), absence of a record never
refutes an `UNKNOWN`. Evidence cites repo-relative paths with lines.

**Output.** `<RUN>/R3/_work/<your task id>_VERDICTS.csv`:
`SampleID,ClaimKey,CheckField,CheckedValue,Verdict,ProposedValue,Evidence` — one row per item checked
(for S2 rows, one row for Disposition and one for HumanDecisionNeeded). Plus
`<RUN>/R3/_work/<your task id>_NOTES.md` (≤ 40 lines): counts by verdict and by sample class, the
refuted items in one line each, and anything systematic you saw.
