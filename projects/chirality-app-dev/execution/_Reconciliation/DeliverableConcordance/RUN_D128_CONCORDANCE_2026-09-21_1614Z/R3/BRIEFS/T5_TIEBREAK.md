# T5 — Apply the Addendum 5 tie-break to sealed rows

Read `_COMMON.md` first. Also read CONVENTIONS §2.6 in full ("Tie-break between
STALE_SPECIFICATION and REMAINING_STATE_MISMATCH", MR-8(iv)) and §2.7, and RUN_BASIS Addendum 5.

**Input.** `<RUN>/R3/_work/CAND_TIEBREAK.csv` (column `Why` gives the screen reason): rows where the
Disposition may sit on the wrong side of the tie-break — `STALE_SPECIFICATION` on Remaining
items / REMAINING_WORK rows, `REMAINING_STATE_MISMATCH` on rows that are neither Remaining items
nor register bookkeeping, and register rows on either side. Ledgers sealed before Addendum 5 did not
apply the rule. `DEL-06-02#CLM-005` and `#CLM-032` are owner-deferred and excluded.

**Rule (summary; the CONVENTIONS text governs).**
1. `STALE_SPECIFICATION` when the text states a present fact that is now false (a hash recorded
   as MATCH, a path called "current", a dependency marked SATISFIED, a file said to exist) — same
   for SoW, `_STATUS`, register and references text.
2. `REMAINING_STATE_MISMATCH` only for (a) an item in `## Remaining`, or a REMAINING_WORK row,
   whose open or done status is contradicted by the evidence; or (b) register bookkeeping that is
   behind but says nothing false about the product or its references (Last Updated, TBD, a
   lagging status field).
3. A claim tied to a named snapshot ("MATCH at v23") stays a REGISTER row; text restating it as
   current without the snapshot takes STALE_SPECIFICATION and points to the REGISTER row (`SEE:`).
4. If both still fit, choose the verdict whose repair is a change to deliverable text, and record
   the other as `ALSO:<verdict>`.

Only these two verdicts are in scope: do not move a row to any third Disposition. If a row's
current Disposition is neither side's correct answer, say so as `OUT_OF_SCOPE` and leave it.
Evidence is the row itself; open the deliverable text in the frozen tree when the row does not
show whether the text is a Remaining item, a present-fact statement or bookkeeping.

**Output 1.** `<RUN>/R3/_work/T5_TIEBREAK_VERDICTS.csv`:
`ClaimKey,CurrentDisposition,Verdict,NewDisposition,AlsoNote,Basis`
- `Verdict`: `KEEP`, `MOVE`, `OUT_OF_SCOPE` or `UNDECIDED`.
- `NewDisposition`: for MOVE, the other verdict; else the current value.
- `AlsoNote`: the `ALSO:<verdict>` token when rule 4 applied, else empty.
- `Basis`: the rule number and one sentence quoting or paraphrasing the text that decides it.

**Output 2.** `<RUN>/R3/_work/T5_NOTES.md` (≤ 40 lines): counts by verdict and package, and the
patterns behind the moves.
