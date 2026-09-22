# DEL-02-01 split plan (CONVENTIONS §10; manager brief step 3)

DEL-02-01 is on the split list. Two forward workers each own one SoW section range and write their
own ledger. The manager merges the two sealed halves by script (`_scripts/merge_split.py`) and
validates the merged file against the full claim index.

| Half | Output folder `<OUT>` | Units (CLAIM_INDEX) | Source range |
|---|---|---|---|
| A | `<RUN>/R2/PKG-02/DEL-02-01/A` | SEC-1..SEC-5, CLM-001..CLM-015 (20 units) | `ScopeOfWork.md` lines 1–319: SCA-APP-004 and SCA-APP-010 Gate-5 current contracts, Ontology, Epistemology |
| B | `<RUN>/R2/PKG-02/DEL-02-01/B` | CLM-016..CLM-030, REM-1..REM-7 (22 units) | `ScopeOfWork.md` line 320 to end (Praxeology, Axiology, Conflict Table) and `_STATUS.md` `## Remaining` |

Half indexes (for the validator's coverage check): `<RUN>/R2/PKG-02/_split/INDEX_A.csv` and
`INDEX_B.csv`, written by `_scripts/split_index.py` from `R1_INVENTORY/CLAIM_INDEX.csv`.

## Rules for each half

1. Read the whole deliverable for context, but write rows **only for your half's units** and for
   run-local rows your half owns.
2. File names are the normal ones inside your half folder: `<OUT>/DEL-02-01_claims.csv`,
   `<OUT>/DEL-02-01_notes.md` (and later reverse files if the manager resumes you).
3. Run-local keys are numbered by half so the merge has no collisions:
   - **Half A:** `REGISTER-1..REGISTER-49` and `STATE-1..STATE-49`. Half A owns the `_REFERENCES.md`
     hash REGISTER rows (CONVENTIONS §2.7) and register defects in `_REFERENCES.md`,
     `Dependencies.csv`, `_CONTEXT.md` and the SoW front matter.
   - **Half B:** `REGISTER-50..` and `STATE-50..`. Half B owns register defects and state assertions
     in `_STATUS.md` (other than the `## Remaining` units themselves, which are REM rows) and
     `MEMORY.md`.
4. `SEE:<ClaimKey>` may only point to a row in your own half (the validator checks within the file).
   Where a statement in your half repeats one owned by the other half, disposition it yourself and
   mention the repetition in Notes in prose (no `SEE:` token).
5. Validate your half from `<APP_WORK>` with the half index:
   `python3 <RUN>/_scripts/validate_ledger.py ledger --index <RUN>/R2/PKG-02/_split/INDEX_<A|B>.csv <OUT>/DEL-02-01_claims.csv`
   Errors must be zero. Then compute the SHA-256; your half is sealed.
6. Your notes file covers your half only (all six §3 sections; census of your rows).
7. Do not read the other half's folder at any time before the manager's reverse-pass message.
