# Brief — R2 reverse pass (resumed forward worker, TASK Type 2) — PKG-04

This continues your forward-pass assignment for `<DEL-ID>`; every discipline rule of
`_BRIEFS/FORWARD_WORKER.md` still applies (frozen tree only, read-only git against it only, no
installs or test runs, no absolute paths, write only in `<RUN>/R2/PKG-04/<DEL-ID>/`,
`<RUN>/R0_CALIBRATION/**` still out of bounds). Rules: CONVENTIONS §5.1.

## Inputs

- Your **sealed** ledger `<DEL-ID>_claims.csv`. **Do not edit it.** Its SHA-256 must still equal
  the sealed value when you finish.
- The capability files listed in `<RUN>/R2/PKG-04/_reverse_inputs/<DEL-ID>_AREAS.md` (they live in
  `<RUN>/R2/SURFACES/<AREA>_capabilities.csv`; the matching `<AREA>_notes.md` may be consulted for
  tag meanings). Areas were chosen by script from the paths your ledger cites and your hints file.
  Read nothing else under `R2/SURFACES/`.

## Outputs (in your folder)

1. `<DEL-ID>_reverse.csv` — header `CapabilityID,Response,ClaimKey,Rationale`; **one row for every
   capability row of every listed area file**; final record `#END`.
   - `CLAIMED_BY` + the key of one of your ledger rows that owns the capability;
   - `PARTIAL` + the key of a row that covers part of it;
   - `NOT_MINE` with an empty `ClaimKey`.
   - Rationale: short, evidence-based (why this deliverable does or does not own it). Note the
     capability's REACH/STATE where it matters to ownership.
2. `<DEL-ID>_errata.csv` — **only if** the reverse pass shows a sealed forward row was wrong.
   Header `ClaimKey,Field,SealedValue,ProposedValue,Evidence`, final `#END`; one row per
   (ClaimKey, Field); `SealedValue` copied exactly from the sealed ledger; `Field` is any column
   except ClaimKey/ClaimID. A **missing** forward row (coverage gap: something your deliverable
   owns that no row covers) is not an erratum — describe it in reverse_notes.
3. `<DEL-ID>_reverse_notes.md` — response counts; errata explanations; coverage gaps; capabilities
   that look owned by another deliverable (name it if evident); any capability-file accuracy issue
   you noticed (e.g. a REACH/STATE tag contradicted by code); effort.
   Also update nothing in `<DEL-ID>_notes.md` (it is part of the sealed forward pass); put the
   sealed-vs-errata-applied census figures in reverse_notes instead.

## Validate (from `<APP_WORK>`)

```
python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <RUN>/R2/PKG-04/_reverse_inputs/<DEL-ID>_capabilities.csv <RUN>/R2/PKG-04/<DEL-ID>/<DEL-ID>_reverse.csv
python3 <RUN>/_scripts/validate_ledger.py errata <RUN>/R2/PKG-04/<DEL-ID>/<DEL-ID>_errata.csv   # only if written
```
(The concatenated file is a manager-built validator input: the listed area files' rows in one CSV.)
Fix to 0 errors. Recompute `shasum -a 256` of `<DEL-ID>_claims.csv` and confirm it is unchanged.

## Return (≤ 8 lines)

Counts by Response; errata rows (count and fields); coverage gaps; validator RESULT lines; SHA-256
of `_reverse.csv` (and `_errata.csv`); confirmation that the sealed SHA-256 is unchanged.
