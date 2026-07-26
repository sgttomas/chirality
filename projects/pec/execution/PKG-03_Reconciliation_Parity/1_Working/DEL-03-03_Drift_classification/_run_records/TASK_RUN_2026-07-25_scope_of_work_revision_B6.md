# TASK RUN — DEL-03-03 ScopeOfWork revision (D-PEC-63 batch B6 fan-in, wave-level F3)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B6 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B6 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md`
- **Standing:** this is a previously **accepted** (batch B5) contract. Only the
  wave-level F3 correction was applied; nothing else in the document was
  touched. `git diff --numstat` reports `2 2` — two lines changed, every other
  line byte-identical.
- **Mode:** minimal corrective revision. No renumbering, no reflow, no record added or removed, no scope change.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F3a | MAJ (wave-level) | Restate AX-008's falsification-clause claim to the record-supported form | APPLIED |
| F3b | MAJ (wave-level) | Replace CON-005's false "mis-arm" consequence | APPLIED |

## Ground truth

`projects/pec/docs/PRD.md` §11, falsification clause: "**Falsification clause:**
if, after Phase 3, harness poll adoption remains negligible and the owner does
not consult the dashboards, the product thesis is falsified; PEC is deleted and,
by `PEC-K-01`, nothing breaks." Its two limbs are poll adoption and owner
dashboard consultation — not parity.

`_Decomposition/ScopeLedger.csv` annotates those limbs against other scope items:

- `SOW-060` `Notes` cell, in full: `Measures uptake of SOW-004; arms limb 1 of
  the falsification clause (limb 2: SOW-085)`
- `SOW-085` `ScopeItemStatement` names "limb 2 of the §11 falsification clause"
- `SOW-093` (the §11 parity metric) carries **no** limb annotation in any cell.

The accepted contract asserted, in its own voice, that the falsification clause
is armed on the parity count and that an over-count would "mis-arm" it. Neither
is supported by the accepted corpus.

## F3a — before / after

Location: AX-008 (Axiology), second clause.

**Before**

> The §11 parity metric counts one producer's findings, the falsification clause
> is armed on that count, and nothing in the accepted corpus obliges the type to
> say which producer made a given finding (CON-005).

**After**

> The §11 parity metric counts one producer's findings; the §11 falsification
> clause is armed on its own two limbs, which the ledger annotates against other
> scope items — the `SOW-060` `Notes` cell reads in full "Measures uptake of
> SOW-004; arms limb 1 of the falsification clause (limb 2: SOW-085)", and
> `SOW-085`'s own scope-item statement carries limb 2, while `SOW-093`, the
> parity-metric row, carries no limb annotation at all — and nothing in the
> accepted corpus obliges the type to say which producer made a given finding
> (CON-005).

The CON-005 cross-reference and the record's closing sentence (REQ-010 holds
this side of the line; the discriminator is the schema owner's) are unchanged.

## F3b — before / after

Location: CON-005 (Conflicts), the consequence clause.

**Before**

> (CLM-012) — a metric that counted this classifier's findings as well would
> over-count and mis-arm the falsification clause.

**After**

> (CLM-012) — a metric that counted this classifier's findings as well would
> over-count, and so would corrupt the §11 parity metric that `SOW-093` reports.
> It would not mis-arm the §11 falsification clause, which is not armed on this
> count: the ledger annotates that clause's two limbs against other scope items,
> limb 1 to `SOW-060` — whose `Notes` cell reads in full "Measures uptake of
> SOW-004; arms limb 1 of the falsification clause (limb 2: SOW-085)" — and limb
> 2 to `SOW-085`, whose own scope-item statement names it, while `SOW-093`
> carries no limb annotation.

The rest of CON-005 — the two-producer statement, the `PRD.md` §11 metric-5
quotation, the pre-existing `SOW-093` `Notes` quotation, and the REQ-010
disposition — is unchanged.

## Quotation-record compatibility

This contract's quotation record states that none of its quotations is elided
and that "Where a quotation presents one cell, one row, or one record, that is
stated at the point of quotation and the cell, row, or record is complete." The
one quotation added by this revision is the `SOW-060` `Notes` cell, quoted
**in full** and identified as that cell at both points of quotation. `SOW-085`'s
limb-2 attribution is cited by reference to its scope-item statement and is not
quoted, so no partial cell was introduced. `grep -c '…'` over the document = 0.
The quotation record itself required no change and was not touched.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-03-03_Drift_classification"` → `item_count = 15` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 2, REQ 14, AC 15, VER 14, CLM 14, AX 12, TBD 4, CON 5.
- Frontmatter byte-identical (lines 1–8 untouched).
- `git diff -U0` hunk ranges: `@@ -272 +272 @@` and `@@ -316 +316 @@` only.

## Artifact hash

- `ScopeOfWork.md` sha256 `2e2c0f1e1196358ec0aee6c5e59187a8ec5dd0fde1600b50b8ce33a55f73bfd5`
- Superseded hash (B5 acceptance): `83366eee4d11a26ca65e9c81d4baa29fe88c099998b37021821ec1eb4a1fbf70`

## Downstream note (coordination, not authority)

The accepted `DEL-10-11` contract (CLM-003, CON-003, AC-015 and its matrix row)
cites this contract's former reading as a recorded corpus divergence — "the
accepted `DEL-03-03` contract states the relation more strongly in its own
voice". With this revision that divergence is closed in this contract's
direction. `DEL-10-11` was **not** amended for it: its citations remain accurate
as statements about what that contract records, and amending them is a
`DEL-10-11` disposition for PROJECT_SETUP, not this run's write scope.

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.

---

# APPENDIX v2 — Brief amendment v2 (anomaly 4 disposition)

Everything above records the v1 application and is unchanged. This appendix
records a second, separately authorized pass over the same target.

- **Date:** 2026-07-25
- **Authority:** PROJECT_SETUP brief amendment v2, ruling 2 (disposition of the
  anomaly this run reported at v1 return). Fence unchanged: contracts A and E
  and their run records only.
- **Supersedes:** the v1 "Downstream note", which recorded that `DEL-10-11` was
  not amended for this contract's F3 correction. Amendment v2 ruling 1 has since
  amended `DEL-10-11`; see that deliverable's run record, APPENDIX v2.

## Ruling applied

| Ruling | Disposition | Status |
|---|---|---|
| Amendment v2 §2 | Fix CON-005's partial `SOW-093` `Notes` quotation, smallest fix consistent with this contract's own quotation-record categories | APPLIED |

## Basis

CON-005 quoted the `SOW-093` `Notes` cell as "Measures the output of SOW-020
(DL-14)" while the accepted `_Decomposition/ScopeLedger.csv` cell reads in full
`Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the metric is
PKG-10`. This contract's quotation record states that none of its quotations is
elided and that "Where a quotation presents one cell, one row, or one record,
that is stated at the point of quotation and the cell, row, or record is
complete." The partial quotation falsified that claim. This deliverable's own
CLM-012 already quotes the same cell in full, so the pre-existing category was
"complete cell" and completing the quotation is both the smaller diff and the
option consistent with the record; ellipsis-marking would have required opening
an elision account this contract otherwise has none of.

## Before / after

Location: CON-005, the load-bearing-downstream sentence.

**Before**

> …and the register note on the deliverable that reports it records that it
> "Measures the output of SOW-020 (DL-14)" (CLM-012) — a metric that counted…

**After**

> …and the `SOW-093` `Notes` cell on the deliverable that reports it reads in
> full "Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the
> metric is PKG-10" (CLM-012) — a metric that counted…

The quoted cell is now byte-identical to the register cell, and the point of
quotation names it as the `SOW-093` `Notes` cell and states that it is complete
("reads in full"), which is exactly what the quotation record requires.

## Trailer accounting

No trailer change was required or made. The existing quotation record —
"Every quotation in this contract is verbatim from the named source, and **none
is elided** … Where a quotation presents one cell, one row, or one record, that
is stated at the point of quotation and the cell, row, or record is complete."
— was false only because of this partial quotation and is now literally true as
written. Verified: `grep -c '…'` over the document = 0.

## Post-edit verification (v2)

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification`

- `derive_review_checklist.py` → `item_count = 15` (UNCHANGED). JSON not persisted.
- Record counts unchanged: OUT 2, REQ 14, AC 15, VER 14, CLM 14, AX 12, TBD 4, CON 5.
- Frontmatter byte-identical.
- `git diff --numstat` against the B5 accepted baseline remains `2 2`, hunks
  `@@ -272 +272 @@` and `@@ -316 +316 @@` — the v2 edit lands inside the same
  CON-005 line the v1 F3b edit already touched, so no additional line diverges
  from the accepted baseline.
- The register cell was re-read from `_Decomposition/ScopeLedger.csv` by CSV
  parse (not by grep) and compared byte-for-byte against the string now in
  CON-005: equal.

## Artifact hash (v2)

- `ScopeOfWork.md` sha256 `5ce8ab72425ab417c90c3e64a152912a7e39b243f3905e65477dbfd91a40eaa7`
- Superseded (v1) hash: `2e2c0f1e1196358ec0aee6c5e59187a8ec5dd0fde1600b50b8ce33a55f73bfd5`
- Superseded (B5 acceptance) hash: `83366eee4d11a26ca65e9c81d4baa29fe88c099998b37021821ec1eb4a1fbf70`

## Write scope (v2)

Exactly two paths written by the v2 pass: this run record and the target
`ScopeOfWork.md` — the same two paths as v1.
