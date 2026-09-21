# Verifier shard brief (R0 calibration, unit V)

> Manager adaptation, recorded for the report: the brief's single verifier V faced 465
> deterministic recheck items (script `_scripts/select_rechecks.py`, output
> `_verify/SELECTION.csv`). One context cannot open that much evidence, so V runs as fresh
> evidence-only shards, one per ledger unit (SURFACES rows ride with DEL-09-07), plus one
> fresh aggregator that writes `VERIFICATION.md`. Selection, verdict vocabulary and
> outputs are otherwise exactly the brief's.

You are a fresh, evidence-only TASK (Type 2) verifier shard. Do not delegate. **Never edit any
ledger, notes or reverse file.** Write only your two shard files under `R0_CALIBRATION/_verify/`.

Inputs: your unit's rows in `_verify/SELECTION.csv`; that unit's `_claims.csv`, `_notes.md`,
`_reverse.csv`, `_reverse_notes.md`; `SURFACES/HARNESS_capabilities.csv`; the run's
`CONVENTIONS_CANDIDATE.md` (read all of it — it is the rulebook you check against) and
`RUN_BASIS.md` §3 and §5; the frozen tree. Do not read other units' ledgers except where
a SELECTION row requires it (double-blind shards: do not read the other DEL-03-01 folder).

For each selected item, open the cited evidence at the frozen tree (deliverable files,
code, tests, decision records) and record:
- `CONFIRMED` — the row's Disposition, CauseTag, evidence citation and (for class c) the
  capability-to-claim response hold;
- `REFUTED` — they do not; give the correct reading (e.g. the right Disposition/CauseTag)
  and the evidence;
- `CONTESTED` — reasonable either way; give both readings.
Check the convention application too: MR-8 (STALE_SPECIFICATION vs ACCEPTED_DIVERGENCE:
ACCEPTED_DIVERGENCE needs the text to acknowledge the gate AND a GOVERNING ruling),
MR-2/MR-6 MechanicallyUnblocked, CONTEXT-only DirectionEvidence, AuthorityTier "highest
tier restated", CauseTag vocabulary, AssessmentEvidence token, and whether evidence paths
and line numbers actually exist at the frozen tree. Many rows share evidence; open it once
and apply it, but give every selected item its own verdict line.

Economize: grep before reading, read line ranges. Read-only everywhere except your shard
files. Git: only read-only `git -C <FROZEN_TREE> log|show|blame`. No installs, test runs, or
other git. Do not read `projects/chirality-runtime/execution/**` or the working
repository's deliverable folders. No absolute paths in outputs.

## Outputs

1. `_verify/V-<Unit>.csv` — header exactly
   `Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`
   one line per SELECTION item (same order), no newlines inside fields, last line `#END`.
   `Field` = the field at issue for REFUTED/CONTESTED (Disposition, CauseTag,
   ImplementationEvidence, Response, …; `-` when CONFIRMED). `RowValue` = the ledger's value
   for that field. `CorrectReading` = your reading (both readings for CONTESTED, separated
   by ` || `). `Evidence` = repo-relative path:line. `ConventionIssue` = the MR-n / rule
   misapplied or found ambiguous, or `-`.
2. `_verify/V-<Unit>_notes.md` — (i) counts: checked / CONFIRMED / REFUTED / CONTESTED by
   class; (ii) the systematic patterns you saw (which conventions the worker misapplied or
   found ambiguous), each with example keys; (iii) effort: approximate files read and
   whether context was tight.

Return (short): counts by verdict, the top 3 patterns, and the SHA-256 of your CSV.
