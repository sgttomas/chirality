# TASK RUN — DEL-10-10 ScopeOfWork revision (D-PEC-63 batch B5 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B5 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B5 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F2 | MAJ | The batch fan-in record does not yet exist; align the assertion to sibling `DEL-03-04`'s compliant forward-looking form | APPLIED |
| F8 | MIN | CLM-008 quoted a mid-sentence clause of `D-PEC-62` §1(4) without marking it as a clause; extend to the whole sentence | APPLIED |
| F6a | MIN | Add CLM-017's source-own leading ellipsis to the Quotation record's source-own accounting | APPLIED |
| F6b | MIN | Add a trailing ellipsis mark to the `DL-11` quotation | **BLOCKED** — see below; superseded by brief amendment v2, applied in the appendix |

## F2 — before / after

Location: Purpose and Objective Traceability, "Standing character
(load-bearing), and what authorizes it".

**Before**

> That sentence is carried durably at
> `execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md`, the batch fan-in
> record, which records it verbatim. The framing is informed by, not derived
> from, …

**After**

> That sentence is carried durably at
> `execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md`, the batch fan-in
> record for the batch this run belongs to, which the dispatcher writes in this
> tranche and which records it verbatim. The framing is informed by, not
> derived from, …

**Basis.** `execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md` does not
exist at authoring time; the prior wording asserted its present existence.
Sibling `DEL-03-04`'s accepted contract carries the compliant forward-looking
form, which this revision adopts. The sentence's surrounding structure and the
following sentence are untouched.

## F8 — before / after

Location: CLM-008, second paragraph.

**Before** (mid-sentence clause quoted without clause marking)

> … and that packet reads the acceptance as taking the exhibit's **flags as
> flags**: "E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION), E-N13/E-N18
> (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set remain
> recorded-but-unresolved, non-gating annotations". What is settled …

**After** (whole sentence, as sibling `DEL-10-02`'s CLM-009 does)

> … and that packet states its own reading of that acceptance in one sentence,
> quoted here whole: "This packet reads "as presented" as accepting the exhibit
> **flags as flags** — E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION),
> E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set remain
> recorded-but-unresolved, non-gating annotations; each flag is carried
> verbatim into the seeded rows' `Notes`." What is settled …

**Basis.** `_Coordination/_DECISIONS/D-PEC-62_project_setup_scaffold_and_local_dependency_registers.md`
§1 item 4, lines 27–31, reads as one sentence terminating at "…carried verbatim
into the seeded rows' `Notes`." The whole-sentence option was taken, per the
disposition's stated preference. No ellipsis was introduced, so the document's
omission enumeration is unaffected by this edit.

## F6a — before / after

Location: Quotation record, closing paragraph.

**Before**

> One further ellipsis appears inside the `DEL-02-05` `CON-004` quotation in
> CLM-013. That ellipsis is the upstream contract's own omission of the
> `OI-010` text it quotes; it is not an omission by this contract, which quotes
> `CON-004` in full. No other quotation in this document omits text from the
> span it presents.

**After**

> Two further ellipses appear in this document and both are the sources' own
> rather than this contract's. The first is inside the `DEL-02-05` `CON-004`
> quotation in CLM-013: it is the upstream contract's own omission of the
> `OI-010` text it quotes, not an omission by this contract, which quotes
> `CON-004` in full. The second is the leading ellipsis on the Gate 2
> confirmation quoted in CLM-017, which is the `SOFTWARE_DECOMP.md` Gate Log
> `DL-10` Rationale cell's own wording, carried verbatim rather than introduced
> here. No other quotation in this document omits text from the span it
> presents.

**Basis.** `_Decomposition/SOFTWARE_DECOMP.md` Gate Log row `DL-10` (line 628)
carries, in its Rationale cell, the register's own text: `Gate 2 confirmation
verbatim in the Gate Log: "…based on acceptance of your recommendations for
OI-010 and OI-011"`. The leading ellipsis is the register's, not this
contract's, so it belongs in the source-own accounting rather than in the
enumerated omissions list.

## F6b — BLOCKED

**Disposition as issued:** "add the trailing ellipsis mark to the `DL-11`
quotation" (because Quotation-record item 6 enumerates a trailing omission that
carries no ellipsis mark).

**Exact discrepancy found.** The finding assumes text follows the `SOW-064`
clause inside the quoted span. It does not. `_Decomposition/SOFTWARE_DECOMP.md`
Gate Log row `DL-11` (line 629) has a Decision cell that **terminates** at that
clause:

> … `SOW-054` (rebuild bounds) → PKG-03 as reconcile performance; `SOW-064`
> (bootstrap) → PKG-10 as a validation act, not a reconciler feature

The next character in the source is the table's closing pipe; the Rationale
cell then begins. There are therefore **no clauses following** the `SOW-064`
clause within the quoted Decision cell. Adding a trailing ellipsis would mark an
omission the source does not contain — the same defect as the F1 spurious
ellipsis corrected in `DEL-03-04` this tranche.

**Action taken:** none. The `DL-11` quotation in CLM-017 and Quotation-record
item 6 were left byte-unchanged. Per the run brief, this is reported rather
than improvised.

**Residual defect, unrepaired and routed to the dispatcher.** Two statements in
this contract remain inaccurate for the same underlying reason and are *not*
what the disposition authorized changing:

1. CLM-017's lead-in says the `DL-11` clause is quoted "with the preceding and
   following clauses elided". Only preceding clauses are elided.
2. Quotation-record item 6 ("The same `DL-11` quotation, omitting the clauses
   following the `SOW-064` clause") enumerates an omission that does not exist,
   and the trailer's count "Exactly six omissions are made by this contract"
   over-counts by one — the document carries five contract-made ellipsis marks
   (CLM-010 ×2, CLM-012 ×2, CLM-017 ×1), which is the correct number.

The true repair is to drop item 6, renumber the enumeration to five, correct
the count word, and drop "and following" from CLM-017's lead-in. That is
outside the issued disposition and is returned for a dispositioning decision.

**Dispositioned.** PROJECT_SETUP independently verified this analysis and ruled
the proposed repair in at brief amendment v2. It is applied in the appendix
below; the F6b judgment itself stands — no trailing ellipsis was added.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-10-10_Directed_bootstrap_self_ingest_validation"` → `item_count = 16` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 1, REQ 14, AC 16, VER 14, CLM 20, AX 11, TBD 5, CON 5.
- Frontmatter byte-identical (lines 1–8 untouched).
- Ellipsis census re-run after edits: seven occurrences — five contract-made
  (CLM-010 ×2, CLM-012 ×2, CLM-017 `DL-11` leading ×1) and two source-own
  (CLM-013 `CON-004`, CLM-017 `DL-10` leading). The source-own accounting in
  the Quotation record now matches the census exactly; the contract-made
  enumeration remains over-counted by one for the reason recorded under F6b.

## Artifact hash

- `ScopeOfWork.md` sha256 `d11fccd3fc32ff7b5e9d0c50d44f5ccee4189b420d7e796ccd5073d9d230f2b3`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written. In particular
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md` was **not** written by
this run; it remains the dispatcher's to write in this tranche.

---

# APPENDIX — Brief amendment v2 (F6b dispositioning), applied 2026-07-25

- **Amendment source:** PROJECT_SETUP, brief amendment v2, issued on this run's
  F6b BLOCKED return. Fence unchanged; scope restricted to contract E.
- **Ruling:** PROJECT_SETUP independently verified that `SOFTWARE_DECOMP.md`
  line 629's `DL-11` Decision cell terminates at the `SOW-064` clause, and that
  this contract's actual contract-made ellipsis census is **five** (CLM-010 ×2,
  CLM-012 ×2, CLM-017 `DL-11` leading ×1) with **two** source-own (CLM-013's
  carried upstream ellipsis; CLM-017's Gate 2 unicode ellipsis). The repair
  formulated under F6b was ruled in **exactly as proposed, nothing more**.
- **Prior artifact state at amendment time:** sha256
  `d11fccd3fc32ff7b5e9d0c50d44f5ccee4189b420d7e796ccd5073d9d230f2b3`.

## Amendment items applied

| # | Instruction | Status |
|---|---|---|
| 1 | Drop Quotation-record item 6; renumber so the list has five items | APPLIED |
| 2 | Change "Exactly six omissions" to "Exactly five omissions" | APPLIED |
| 3 | CLM-017 lead-in: "with the preceding and following clauses elided" → "with the preceding clauses elided" | APPLIED |
| 4 | Leave the `DL-11` quotation text byte-unchanged; add no trailing ellipsis | HONORED |

### Item 1 — before / after

Location: Quotation record enumeration.

**Before**

> 5. The `DL-11` Decision-cell quotation in CLM-017, omitting the clauses
>    preceding the `SOW-064` clause.
> 6. The same `DL-11` quotation, omitting the clauses following the `SOW-064`
>    clause.

**After**

> 5. The `DL-11` Decision-cell quotation in CLM-017, omitting the clauses
>    preceding the `SOW-064` clause.

Item 6 removed. Items 1–5 were already correctly numbered and were left
byte-unchanged, so no renumbering of surviving items was required and none was
performed.

### Item 2 — before / after

**Before**

> named source. Exactly six omissions are made by this contract, each marked
> with an ellipsis at the point of omission and enumerated here in full:

**After**

> named source. Exactly five omissions are made by this contract, each marked
> with an ellipsis at the point of omission and enumerated here in full:

### Item 3 — before / after

Location: CLM-017, lead-in to the `DL-11` Decision-cell quotation.

**Before**

> `DL-11` (2026-07-24) records the Phase 4 forced boundary assignment for this
> scope item; quoting the clause that bears on it, with the preceding and
> following clauses elided: "Phase 4 forced boundary assignments: … "

**After**

> `DL-11` (2026-07-24) records the Phase 4 forced boundary assignment for this
> scope item; quoting the clause that bears on it, with the preceding clauses
> elided: "Phase 4 forced boundary assignments: … "

### Item 4 — honored

The `DL-11` quotation itself — `"Phase 4 forced boundary assignments: ...
SOW-064 (bootstrap) → PKG-10 as a validation act, not a reconciler feature"` —
is byte-unchanged. Confirmed by grep against the exact post-edit string. No
trailing ellipsis was added; the F6b judgment stands.

## Verification after amendment

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-10-10_Directed_bootstrap_self_ingest_validation"` → `"item_count": 16` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 1, REQ 14, AC 16, VER 14, CLM 20, AX 11, TBD 5, CON 5.
- Frontmatter byte-identical (lines 1–8 untouched).
- **Quotation accounting now fully reconciled.** Ellipsis census: seven
  occurrences across six lines — five contract-made (CLM-010 ×2, CLM-012 ×2,
  CLM-017 `DL-11` leading ×1), matching the trailer's "Exactly five omissions"
  and its five enumerated items one-for-one; and two source-own (CLM-013
  `CON-004`, CLM-017 `DL-10` Gate 2), matching the trailer's source-own
  paragraph. No residual over-count, and no marked omission lacks a
  corresponding source omission.

## Artifact hash after amendment

- `ScopeOfWork.md` sha256 `a174099336f5fe62df27648514afa3121abcede57932dd17894a336696246377`
  (supersedes `d11fccd3fc32ff7b5e9d0c50d44f5ccee4189b420d7e796ccd5073d9d230f2b3`)

## Write scope of the amendment

Exactly two paths written under amendment v2: this run record and contract E's
`ScopeOfWork.md`. Contracts A–D were not reopened and are byte-unchanged from
their originally reported hashes. No control file, no register, no sibling
deliverable, and no coordination surface was written.
