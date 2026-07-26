# TASK RUN — DEL-10-11 ScopeOfWork revision (D-PEC-63 batch B6 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B6 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B6 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F1a | MAJ | Mark the `C-08` constraints-row truncation with an ellipsis | APPLIED |
| F1b | MAJ | Enumerate the TBD-003 `SOW-093` elision as elision (4) in the quotation record | APPLIED |
| F1c | MAJ | "Exactly three quotations elide text" → "Exactly four" | APPLIED |
| F1d | MAJ | Correct the DL-14 and DL-13 leading-ellipsis descriptions | APPLIED |

## F1a — before / after

Location: CLM-012, the `C-08` `STANDING_NODES` blockquote.

**Before**

> …they gate releases not successors,R3-F9; owner confirmation requested`

**After**

> …they gate releases not successors,R3-F9; owner confirmation requested …`

**Basis.** `_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.2
constraints register, `C-08` row: the `Notes` cell reads in full
`R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression
record itself`. The contract's quotation stopped at "owner confirmation
requested" with no elision mark, while its own trailing parenthetical already
declared the quotation "**elided** at the single point where the `Notes` cell
continues".

**Consequential same-sentence correction.** The lead-in to that blockquote read
"quoted **in full** under the constraints register's columns", which the
inserted ellipsis contradicts on its face. The two words "in full" were removed
from that lead-in. No other word of CLM-012 was touched.

## F1d — before / after

Location: CLM-005, the two Decision-Log blockquote attributions, and the
corresponding enumerations (1) and (2) in the Quotation record.

**Before (DL-14, both places)**

> **elided** at both ellipses, which stand for the remainder of a long Phase 6
> verification-errata list…

**After (DL-14, both places)**

> **elided** at both ellipses — the leading ellipsis stands for the cell's
> opening phrase, "Phase 6 adversarial verification (opus-5; 19 confirmed
> defects, 5 suspicions dispositioned) applied at revision 0.9:", and the
> trailing ellipsis for the remainder of a long Phase 6 verification-errata
> list…

**Before (DL-13, both places)**

> **elided** at both ellipses, which stand for the row's four other lettered
> Phase 5 conventions…

**After (DL-13, both places)**

> **elided** at both ellipses — the leading ellipsis stands for the cell's
> opening phrase, "Phase 5 conventions:", and the trailing ellipsis for the
> row's four other lettered Phase 5 conventions…

**Basis.** `_Decomposition/SOFTWARE_DECOMP.md` Decision Log. The `DL-14`
`Decision` cell opens "Phase 6 adversarial verification (opus-5; 19 confirmed
defects, 5 suspicions dispositioned) applied at revision 0.9:" before the
`SOW-093`/`SOW-094` clause the contract quotes. The `DL-13` `Decision` cell
opens "Phase 5 conventions:" before lettered convention (a). In each row the
leading ellipsis therefore stands for the cell's opening phrase, not for a list
item.

**Scope note.** The finding named "the two enumerated … elision descriptions".
The same false description appeared verbatim in the inline blockquote
parentheticals in CLM-005 and in enumerations (1) and (2) of the trailer.
Correcting only the trailer would have left the document self-contradictory, so
both locations were corrected identically. No other text was changed.

## F1b / F1c — before / after

Location: Quotation record trailer.

**Before**

> Exactly three quotations elide text, … and (3) the `C-08` constraints row in
> CLM-012 … No other quotation in this document omits text from the span it
> presents.

**After**

> Exactly four quotations elide text, … (3) the `C-08` constraints row in
> CLM-012 …; and (4) the `SOW-093` scope-item statement quoted in TBD-003,
> elided at the single medial point where the statement's own words "parity
> DriftFindings per reconcile" stand between "Report" and "as the §11 parity
> metric". No other quotation in this document omits text from the span it
> presents.

**Basis.** TBD-003 quotes `SOW-093` as "Report … as the §11 parity metric". The
accepted `ScopeLedger.csv` statement reads in full "Report parity DriftFindings
per reconcile as the §11 parity metric", so the ellipsis stands for "parity
DriftFindings per reconcile". The closing "No other quotation…" sentence
required no wording change: with the fourth elision now enumerated, it is
literally true as written.

## Post-edit ellipsis census

`grep -n '…\|\.\.\.'` over the whole document returns exactly four lines, one
per enumerated elision, and no three-dot form anywhere:

| Line | Quotation | Ellipses on the line |
|---|---|---|
| 89 | `DL-14` Decision cell (CLM-005) | 2 (leading + trailing) |
| 101 | `DL-13` Decision cell (CLM-005) | 2 (leading + trailing) |
| 160 | `C-08` constraints row (CLM-012) | 1 (terminal) |
| 207 | `SOW-093` statement (TBD-003) | 1 (medial) |

Four ellipsis-bearing quotations, matching "Exactly four quotations elide
text". No ellipsis of this contract's making appears outside those four
quotations; the trailer itself contains no ellipsis character.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-10-11_Parity_metric_DriftFindings_per_reconcile"` → `item_count = 15` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 1, REQ 13, AC 15, VER 13, CLM 17, AX 9, TBD 5, CON 6.
- Frontmatter byte-identical (lines 1–8 untouched).
- Heading set and Output and Evaluation Matrix untouched. No record was added,
  removed, or renumbered.

## Artifact hash

- `ScopeOfWork.md` sha256 `4fc7f68f58ec27a18d5fc63e2a8dec53ee37e98154bf15df51e23730291aad52`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.

---

# APPENDIX v2 — Brief amendment v2 (anomaly 3 disposition)

Everything above records the v1 application and is unchanged. This appendix
records a second, separately authorized pass over the same target.

- **Date:** 2026-07-25
- **Authority:** PROJECT_SETUP brief amendment v2, ruling 1 (disposition of the
  anomaly this run reported at v1 return). Fence unchanged: contracts A and E
  and their run records only.
- **Supersedes:** the v1 return's anomaly 3, which reported the divergence as
  left open and flagged it for PROJECT_SETUP disposition.

## Ruling applied

| Ruling | Disposition | Status |
|---|---|---|
| Amendment v2 §1 | Restate A's CLM-003 / CON-003 / AC-015 / AC-015 matrix row so the `DEL-03-03` divergence reads as corrected at the batch-B6 fan-in rather than as live; preserve CON-003's genuinely open remainder; keep AC-015 owner-routed for that remainder; delete no record | APPLIED |

## Basis

E's F3 correction (this wave, same fan-in) removed from `DEL-03-03` both
statements A cited as the contrary corpus reading. A's four citations were
written in the present tense and became false of the current corpus at the
moment E was written. The superseded sentences survive verbatim in
`execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_run_records/TASK_RUN_2026-07-25_scope_of_work_revision_B6.md`,
findings F3a and F3b before/after blocks, which A now names as the source of the
two phrases it still quotes.

## Location 1 — CLM-003, final sentence

**Before (v1)**

> The accepted `DEL-03-03` contract states the relation more strongly in its own
> voice ("the falsification clause is armed on that count"); this contract cites
> the `PRD.md` clause text and the two ledger limb annotations over that
> reading, and records the divergence at CON-003 rather than adopting either.

**After (v2)**

> The accepted `DEL-03-03` contract stated the relation more strongly in its own
> voice — "the falsification clause is armed on that count" — until that reading
> was corrected at the `D-PEC-63` batch-B6 fan-in (…`_run_records/TASK_RUN_2026-07-25_scope_of_work_revision_B6.md`,
> findings F3a and F3b, whose before/after blocks reproduce the superseded
> sentences verbatim and are the named source of both phrases quoted from them
> here and at CON-003). The corrected corpus reads the clause uniformly: its two
> limbs are armed by `SOW-060` and `SOW-085` per the ledger's own annotations,
> `SOW-093` carries none, and no accepted source now states that this count arms
> the clause. The divergence recorded at CON-003 is therefore closed; what
> CON-003 still records is the remainder that correction did not touch.

## Location 2 — CON-003

Record retained; open remainder preserved and sharpened. The heading clause lost
only "nor what the count arms", which is the part the correction settled.

**Before (v1)**

> No accepted source states a **threshold, target, direction, or interpretation
> rule** for metric 5, nor what the count arms. … and the accepted `DEL-03-03`
> contract nevertheless states in its own voice that the falsification clause is
> armed on the parity count and that an over-counted metric would "mis-arm" it.
> The corpus therefore carries two readings of what this number does, and this
> contract adopts neither. REQ-010 forbids …

**After (v2)**

> No accepted source states a **threshold, target, direction, or interpretation
> rule** for metric 5. … What this count *arms* is no longer contested in the
> corpus: the accepted `DEL-03-03` contract formerly stated in its own voice
> that the falsification clause is armed on the parity count and that an
> over-counted metric would "mis-arm" it, and both statements were corrected at
> the `D-PEC-63` batch-B6 fan-in, so every accepted source now reads the clause's
> limbs as `SOW-060`'s and `SOW-085`'s (CLM-003, which names the run record
> reproducing the superseded text). What remains open is what the figure is
> *for*: no accepted source states a threshold, a target, a direction of
> improvement, or a rule by which a reader interprets the number, and this
> contract invents none. REQ-010 forbids …

## Location 3 — AC-015

Kept as the owner-routed acceptance criterion for the surviving remainder; only
the stale premise was restated.

**Before (v1)**

> …with no limb annotation on `SOW-093`, the accepted `DEL-03-03` contract
> nonetheless states the clause is armed on this count, and the measured
> mechanism's own release-gating authority is unconfirmed…

**After (v2)**

> …with no limb annotation on `SOW-093` — the one corpus reading to the
> contrary, in the accepted `DEL-03-03` contract, having been corrected at the
> batch-B6 fan-in (CLM-003, CON-003) — and the measured mechanism's own
> release-gating authority is unconfirmed…

## Location 4 — Output and Evaluation Matrix, AC-015 evidence expectation

**Before (v1)** … "the DEL-03-03 contract's contrary reading" …

**After (v2)** … "the batch-B6 correction of the DEL-03-03 contract's former
contrary reading" …

## Deliberately not changed

REQ-013, AC-013, and VER-013 oblige production not to assert a resolution of
"the metric's meaning or arming" (REQ-013 / AC-013 / VER-013 wording). These are
prohibitions on this deliverable's future artifacts, not assertions about the
state of the corpus, and they remain sound: CON-003 survives as an open record,
and a production choice may still not settle it. No record was deleted,
renumbered, or merged.

## Post-edit verification (v2)

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile`

- `derive_review_checklist.py` → `item_count = 15` (UNCHANGED). JSON not persisted.
- Record counts unchanged: OUT 1, REQ 13, AC 15, VER 13, CLM 17, AX 9, TBD 5, CON 6.
- Frontmatter byte-identical.
- **Divergence-statement truth check.** `grep` for a present-tense assertion that
  `DEL-03-03` states the contrary reading returns 0 hits. The two surviving
  mentions read "`DEL-03-03` contract **stated**" (CLM-003) and "`DEL-03-03`
  contract **formerly**" (CON-003). The live `DEL-03-03` contract contains
  neither superseded phrase; its only "mis-arm" occurrence is the explicit
  negation "It would not mis-arm the §11 falsification clause".
- **Quotation-source check.** Both phrases A still quotes — "the falsification
  clause is armed on that count" and "would over-count and mis-arm the
  falsification clause" — are present verbatim (modulo blockquote line-wrapping)
  in the cited E run record's F3a and F3b before-blocks, which A names as their
  source. A's quotation record required no change: no elision was added or
  removed, and the census remains four elided quotations.

## Artifact hash (v2)

- `ScopeOfWork.md` sha256 `bd44b1e27efe57180185c350d3c4da03a7323a63ed71ddba15cad463bef1d8e6`
- Superseded (v1) hash: `4fc7f68f58ec27a18d5fc63e2a8dec53ee37e98154bf15df51e23730291aad52`

## Write scope (v2)

Exactly two paths written by the v2 pass: this run record and the target
`ScopeOfWork.md` — the same two paths as v1.
