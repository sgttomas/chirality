# Brief — R2 verifier shard (TASK, Type 2, evidence-only) — PKG-04

You are a fresh, evidence-only verifier shard in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-04 WORKING_ITEMS manager. **Do not delegate. Never edit any ledger, notes,
reverse, errata or selection file.** Your dispatch prompt gives `<SHARD>` (a deliverable ID),
`<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`; never write them or any absolute path into outputs.

## Inputs

- Your items: rows of `<RUN>/R2/PKG-04/_verify/SELECTION.csv` with `Unit = <SHARD>` (read by
  script). Classes: `a` must-check (LOW, self-flag, AUTHORITY_CONFLICT, UNKNOWN, REMAINING_WORK),
  `n` 30% sample of other non-ALIGNED, `b` 15% sample of ALIGNED, `c` 20% sample of
  CLAIMED_BY/PARTIAL reverse responses (CapabilityID given), `e` every errata row (ErrataField given).
- **The shared grading key `<RUN>/R2/PKG-04/_verify/GRADING_KEY.md` — read it first and apply it
  exactly.** The rulebook is `<RUN>/CONVENTIONS.md` (read it in full); `<RUN>/RUN_BASIS.md` §3, §5.
- The unit's files in `<RUN>/R2/PKG-04/<SHARD>/` (claims, notes, reverse, errata, reverse_notes);
  the capability files in `<RUN>/R2/SURFACES/` for class c; the evidence pack
  `<RUN>/R2/PKG-04/EVIDENCE_PACK/`; the frozen tree for all deliverable, code, test and decision
  evidence. You may consult `<RUN>/R0_CALIBRATION/VERIFICATION.md` §4 for known patterns.
- Do not read other PKG-04 units' folders unless an item's evidence explicitly requires it.

## Method

For each item, open the cited evidence at the frozen tree and grade per the key. Check the row's
Disposition first, then the fields the key names (reach at symbol level, DirectionEvidence prefix
and register search, CauseTag, AuthorityTier, PostReleaseBasis by blame for touched files,
MechanicallyUnblocked, AssessmentEvidence, HumanDecisionNeeded). Many rows share evidence; open it
once, but give every item its own verdict line.

## Discipline

Read from `<FROZEN_TREE>` only for deliverables and code; never the working repository's deliverable
folders; never `projects/chirality-runtime/execution/**`. Git: only read-only
`git -C <FROZEN_TREE> log|show|blame -L`. No installs, test runs or builds. Grep before reading.

## Outputs (write only these two files)

1. `<RUN>/R2/PKG-04/_verify/V-<SHARD>.csv` — header exactly
   `Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`;
   one line per selected item, in SELECTION order; no newlines inside fields; final line `#END`.
   `Field` = the field at issue (`-` when CONFIRMED; for class e the ErrataField). `RowValue` = the
   ledger value (class e: SealedValue). `CorrectReading` = your reading (CONTESTED: both, joined by
   ` || `). `Evidence` = repo-relative `path:line`. `ConventionIssue` = the rule misapplied or found
   ambiguous (e.g. `§2.3 reach`, `§1 authority`, `GRADING_KEY 2`), else `-`.
2. `<RUN>/R2/PKG-04/_verify/V-<SHARD>_notes.md` — (i) counts checked / CONFIRMED / REFUTED /
   CONTESTED by class; (ii) systematic patterns, each with example keys; (iii) any capability-file
   inaccuracy seen; (iv) effort.

## Return (≤ 6 lines)

Counts by verdict; Disposition-level refutations (keys); top 2 patterns; SHA-256 of your CSV.
