# Verifier shard brief and shared grading key — PKG-06 (TASK, Type 2)

You are a fresh, evidence-only verifier shard in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-06 manager (brief step 7). You do not delegate. **You never edit any
ledger, notes, reverse, errata or pregather file.** You write only your two shard files.
Your prompt supplies `<SHARD>` (e.g. `V-DEL-06-01`), `<UNIT>` (the unit folder), `<DEL-ID>`, and the
values of `<FROZEN_TREE>`, `<RUN>`. Never write an absolute path into an output.

## Inputs

- Your items: the rows of `<RUN>/R2/PKG-06/_verify/SELECTION.csv` whose `Shard` is `<SHARD>` (read by
  script; header `Shard,Unit,Class,ClaimKey,CapabilityID,ErrataField,Reason`).
- The unit's files in `<RUN>/R2/PKG-06/<UNIT>/`: `<DEL-ID>_claims.csv`, `_notes.md`, `_reverse.csv`,
  `_reverse_notes.md`, `_errata.csv` (if present). Read CSV rows by script, selecting your keys.
- The rulebook `<RUN>/CONVENTIONS.md` — read it in full; you grade against it.
- `<RUN>/RUN_BASIS.md` §3, §5 and the addenda; the evidence pack `<RUN>/R2/PKG-06/EVIDENCE_PACK/`;
  the capability files `<RUN>/R2/SURFACES/<AREA>_capabilities.csv` for class `c` items.
- The frozen tree `<FROZEN_TREE>` for deliverable text, code, tests and decision records.
- Do not read other units' folders, `<RUN>/R0_CALIBRATION/**` ledgers, the working repository's
  deliverable folders, or `projects/chirality-runtime/execution/**`.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No installs, test runs, builds.

## Verdicts

For each item open the cited evidence at the frozen tree and record one verdict:

- `CONFIRMED` — the Disposition, CauseTag and evidence citation hold, and the rulebook was applied
  correctly (class `c`: the capability-to-claim response holds; class `e`: the erratum's
  ProposedValue is correct and the SealedValue was wrong).
- `REFUTED` — something does not hold; give the correct reading and the evidence.
- `CONTESTED` — reasonable either way under the rulebook; give both readings.

## Shared grading key (apply identically in every shard)

1. **Field-level refutation.** A wrong citation, gloss, line anchor, token or metadata field is
   `REFUTED` on that field even when the Disposition holds. Name the field in `Field`. Line anchors
   are checked at the frozen tree; drift of 1–6 lines to the right content is immaterial (CONFIRMED,
   note it); a line that shows different content is REFUTED on ImplementationEvidence.
2. **Disposition refutation** requires that the rulebook, applied to the evidence, yields a different
   Disposition. Where the rulebook admits both, grade `CONTESTED`, not REFUTED.
3. **Legacy vs live (§2.3 reachability).** The evidence pack's `REACHABILITY.csv` is the static map the
   rulebook names; a REACH tag that matches it is correct. Where the capability files' symbol-level
   notes (RTCORE/RTCONTRACT/HARNESS) disagree with the module map and the difference would change the
   Disposition, grade `CONTESTED` and give both readings. A requirement met only on a LEGACY_ONLY path
   judged ALIGNED is REFUTED.
4. **MR-11 vs AUTHORITY_CONFLICT (§1).** MR-11 needs a ruling that explicitly addresses the clause or
   deliverable. A ruling (D-GOV-43 / D-APP-127) that undercuts an unamended GOVERNING clause without
   naming it → AUTHORITY_CONFLICT with R4 / R4-Qn. Where DIRECTIVE §0 resolves it, AUTHORITY_CONFLICT is
   wrong. Check whether the row's `R4-Q1/Q2/Q3` citation fits the named question; a plain `R4` where a
   named question applies is REFUTED on HumanDecisionNeeded.
5. **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH vs STALE_ASSESSMENT (§2.6, §2.7, MR-8).**
   STALE_SPECIFICATION = text flatly asserting a now-false state; REMAINING_STATE_MISMATCH = metadata
   or register lag (dates, dependency mirrors, lifecycle state vs remaining); STALE_ASSESSMENT only when
   the overtaken assessment conclusion is the operative defect. A snapshot-true claim is a REGISTER row
   (MR-8 iv). Where both fit the text, CONTESTED.
6. **ACCEPTED_DIVERGENCE** needs the text to acknowledge the gate **and** a GOVERNING ruling permitting
   it; CONTEXT alone never suffices.
7. **DirectionEvidence** must carry `CTX:`/`GOV:` prefixes (or `NOT_APPLICABLE` on ALIGNED /
   NOT_AUDITABLE, or exactly `NONE_FOUND`). `NONE_FOUND` or `UNRECORDED_JUDGMENT` without a search of
   `_DECISIONS/_REGISTER.md` named in Notes is REFUTED on DirectionEvidence if a register or CONTEXT
   record does explain the divergence.
8. **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
   applies; check dates with `git log` when it matters.
9. **AuthorityTier** = highest source restated; `NOT_APPLICABLE` only for CONTEXT_CLAIM and
   non-normative STATE_ASSERTION / REGISTER_DEFECT rows.
10. **MechanicallyUnblocked / gates (§2.5).** YES only when every written gate is verified at the source
    it names; Runtime status needs an App carrier, else UNKNOWN; retired premise → NO + `MOOT:`.
11. **PostReleaseBasis.** For cited files in `TOUCHED_PATHS.csv`, check with `git blame -L`.
12. **AssessmentEvidence** carries exactly one of the three tokens.
13. **Class `c`** (reverse): CONFIRMED when the claim key genuinely owns (CLAIMED_BY) or partly covers
    (PARTIAL) the capability; REFUTED when the key does not address it or a different key in the ledger
    is the clear owner.
Many rows share evidence — open it once, apply it, but give every item its own verdict line.

## Outputs

1. `<RUN>/R2/PKG-06/_verify/<SHARD>.csv` — header exactly
   `Shard,Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`,
   one record per SELECTION item in SELECTION order, final record `#END`. Use a CSV writer (quote
   fields; no raw newlines inside fields). `Field` = the field at issue (`-` when CONFIRMED);
   `RowValue` = the row's value for it; `CorrectReading` = your reading (both readings for CONTESTED,
   separated by ` || `); `Evidence` = repo-relative `path:line`; `ConventionIssue` = the rule
   (e.g. `§2.6 MR-8`, `grading key 4`) or `-`. For class `e`, `Field` is the errata Field.
2. `<RUN>/R2/PKG-06/_verify/<SHARD>_notes.md` — (i) counts checked / CONFIRMED / REFUTED / CONTESTED
   by class; (ii) systematic patterns with example keys; (iii) effort.

Return ≤ 5 lines: verdict counts, the top 2 patterns, the SHA-256 of your CSV.
