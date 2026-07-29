# SCA-002 Run Summary (drafting run GOV-STEP4-SCA-20260729)

RUN_STATUS = `CANDIDATE_DRAFTED_ALL_OWNER_GATES_PENDING`

## Result

The SCA-002 candidate restates the two decomposition rows that carry the
superseded Rev 6 D-8 obligation — SOW-042 (scope ledger line 43) and
DEL-04-06 (deliverable register line 27) — to the D-GOV-31 successor
merge-gate policy, and records the amendment in the working surface's change
register (DEC-023, v1.2 candidate metadata, REF-001 advanced to PRD
Revision 7 at effective merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`).

**No live decomposition surface changed.** The amendment exists only inside
this snapshot as `Gate_3_Candidate/` bytes plus
`Gate_3_Exact_Amendment.diff`. Application happens, if at all, only after
owner acceptance, in a later gated act. No grant is issued; the human-gated
PR default is unchanged; frozen packages and receipts are untouched.

Deterministic candidate validation passes **37/37** checks
(`Gate_3_Validation.json`): basis integrity (SCA-001 applied v1.1 hashes),
PRD Rev 7 subject parity, exactly one record changed per CSV, 12 columns per
row, CRLF/LF terminator preservation, unique IDs, 104/95/9/0 and 46 counts
unchanged, `SOW-042 → PKG-04 → DEL-04-06 → OBJ-002` with D-8 linkage
byte-preserved, successor-policy token presence, and old-text absence.

## Gate state

- Gate 1: `PENDING_OWNER_CONFIRMATION` (deterministic portion PASS)
- Gate 2: `PENDING_OWNER_ACCEPTANCE`
- Gate 3: `PENDING_OWNER_APPROVAL` (candidate validated deterministically)
- Gate 4: `PENDING_OWNER_APPROVAL`
- Gate 5: `NOT_OPENED`

## Fixed closure fields

| Field | Value |
|---|---|
| DecompositionTruthState | `INCOMPLETE` (candidate only) |
| DerivativePackageState | `INCOMPLETE` (rows 2–9 owned by others, unstarted) |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | `NOT_RUN` |
| ReadyForNextPhase | `NO` |

## Evidence

- `Gate_3_Candidate/` + `Gate_3_Exact_Amendment.diff` — exact candidate bytes
- `Gate_3_Validation.json` — 37/37 deterministic PASS
- `build_gate3_candidate.py` / `validate_gate3_candidate.py` — reproducibility
- `Pre_Change_Register_Baseline.json` — frozen-basis identities and counts
- `Supersession_Map.csv` — header-only cumulative map via the deterministic
  accumulator (prior: SCA-001 header-only map); no delta authored
- `Brief.md` census — the two in-scope old-text occurrences and the
  out-of-scope disposition

## Formatting note

`chirality_root_scope_ledger_v1_0.csv` carries CRLF record terminators at the
basis (all 105 records). The candidate preserves those exact terminators, so
`git diff --check` and whitespace scanners flag the candidate ledger copy and
the diff file's CRLF lines as trailing whitespace. As in SCA-001 (its Gate 5
validation note), the exact bytes are retained rather than silently
normalized. `Supersession_Map.csv` likewise carries the CRLF terminators the
deterministic accumulator emits, matching the SCA-001 committed map exactly.
Every SCA-002-authored prose/script/CSV artifact is LF-only with no trailing
whitespace.

## Handoff

To the owner for Gates 1–4 review. See `Handoff_State.md` for the exact next
step, flagged decisions, and the application-phase obligations.
