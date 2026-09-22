# Brief — R2 verifier shard, PKG-00 (TASK, Type 2), with the shared grading key

**Role.** You are a fresh, evidence-only TASK (Type 2) verifier shard under the PKG-00 WORKING_ITEMS
manager of run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`. You do not delegate. **Never edit any ledger,
notes, reverse or errata file.** Write only your two shard files. No installs, no test runs.

**Placeholders** (values in your dispatch prompt): `<FROZEN_TREE>`, `<RUN>`, `<SHARD>` (shard name),
`<UNIT>` (deliverable). Never write absolute paths into outputs; use repo-relative paths.

## Inputs

- Your items: the rows of `<RUN>/R2/PKG-00/_verify/SELECTION.csv` whose `Unit` is `<UNIT>` (all of
  them; there are at most 50).
- That unit's files in `<RUN>/R2/PKG-00/<UNIT>/`: `_claims.csv`, `_notes.md`, `_reverse.csv`,
  `_errata.csv` and `_reverse_notes.md` if present, and `REVERSE_INPUT/COMBINED_capabilities.csv`.
  Read the CSVs with a script (python csv), not by dumping them whole.
- `<RUN>/CONVENTIONS.md` (read all of it: it is the rulebook you grade against), `<RUN>/RUN_BASIS.md`
  §3, §5 and Addenda 1–8, the evidence pack `<RUN>/R2/PKG-00/EVIDENCE_PACK/`.
- Do not read the other PKG-00 unit's folder, any other R2 package folder, `<RUN>/R2/EXT`, or any R0
  ledger or R0 verifier output.

## Evidence roots (strict)

Same as the workers': read only `<FROZEN_TREE>/projects/chirality-app-dev/**` (except other packages'
deliverable folders `execution/PKG-01*`…`PKG-10*`), `<FROZEN_TREE>/projects/chirality-runtime/packages/**`
and `.../tests/**`, the run inputs above, and Root governance docs (`docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md`,
root `AGENTS.md`, `agents/**`) only where App docs defer to them or an App deliverable packages them. Never
Root `execution/`, never `projects/chirality-runtime/execution/**` (exclude it explicitly in every search),
never the working repository's deliverable folders. Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`;
no other subcommand; nothing against the working repository. **If your verdict would rely on evidence
outside these roots, record it as CONTESTED and say so.**

## Shared grading key (identical for every shard)

For each item open the cited evidence at the frozen tree and grade:

1. **Disposition** (verdict field): per CONVENTIONS §2.6, including the Addendum 5 tie-break
   (STALE_SPECIFICATION for a now-false present fact in any text; REMAINING_STATE_MISMATCH only for a
   Remaining/REMAINING_WORK item whose open/done status is contradicted, or bookkeeping lag that says
   nothing false; if both fit, the verdict whose repair is a text change, other in Notes as `ALSO:`).
   MR-8: ACCEPTED_DIVERGENCE needs the text to acknowledge the gate AND a GOVERNING ruling; CONTEXT alone
   never makes it. RETIRED_BY_RULING needs a governing ruling that names the item retired and preserves it.
   CONTEXT_CLAIM: STALE_SPECIFICATION only for a checkable now-false assertion, else NOT_AUDITABLE.
2. **Authority** (§1): AUTHORITY_CONFLICT only when a ruling undercuts an unamended GOVERNING clause
   without naming it, or two GOVERNING texts conflict unresolved by DIRECTIVE §0. The App DIRECTIVE was never
   amended for D-GOV-43; that fact alone is not a conflict — apply §1 as written.
3. **R4-Q1 subject test and Addendum 8**: the subject is product behaviour unless the claim names a code unit
   and only its own contract; R4-Q1 is cited iff `LEGACY_ONLY` code is the only code meeting the claim on the
   product path (`TEST_ONLY` code does not meet a product claim). Missing or superfluous R4-Q1 is a
   HumanDecisionNeeded refutation, not a Disposition one, unless the live-path reading changes the verdict.
4. **REACH**: the pack's REACHABILITY.csv is module-level; check that the specific symbol is reached from a
   product entry point before accepting `REACH=LIVE`.
5. **Other fields**: ClaimType; AuthorityTier (highest tier restated; NOT_APPLICABLE only as §2.3 allows);
   LatestDecision; CauseTag (§4 vocabulary and precedence; 2026-09-09 v3 four-role adoption = exactly
   `OTHER:V3_ROLE_ADOPTION`; UNRECORDED_JUDGMENT only with DirectionEvidence NONE_FOUND); DirectionEvidence
   (`CTX:`/`GOV:` prefixes; NOT_APPLICABLE on ALIGNED/NOT_AUDITABLE); AssessmentEvidence token (MR-1);
   MechanicallyUnblocked (MR-2/MR-6); PostReleaseBasis (blame the relied-on lines if the file is in
   TOUCHED_PATHS.csv); ImplementationEvidence / VerificationEvidence paths and line anchors exist at the frozen
   tree and say what the row claims.
6. **Class c** (reverse response): does the named claim own (CLAIMED_BY) or cover part of (PARTIAL) the
   capability? The Field is `Response`.
7. **Class e** (errata row): is the ProposedValue correct for that Field? Grade the proposed value.

Verdicts: `CONFIRMED` (the Disposition/Response and the fields you checked hold), `REFUTED` (a field is wrong;
give the correct value and evidence), `CONTESTED` (reasonable either way, or evidence outside roots; give both
readings). Many rows share evidence: open it once and apply it, but give each item its own verdict.

## Outputs (write only these two files)

1. `<RUN>/R2/PKG-00/_verify/V-<SHARD>.csv`, header exactly
   `Unit,Class,ClaimKey,CapabilityID,Verdict,Field,SealedValue,CorrectReading,Evidence,ConventionIssue`
   - one line for each CONFIRMED item (`Field` = `-`, `SealedValue` = `-`, `CorrectReading` = `-`);
   - for REFUTED or CONTESTED items, **one line per field at issue** (so an item refuted on Disposition and
     CauseTag has two lines). `Field` is the ledger column name exactly (`Disposition`, `CauseTag`,
     `HumanDecisionNeeded`, `ImplementationEvidence`, … or `Response` for class c). `SealedValue` is the
     value copied exactly from the sealed ledger (for class e, the errata ProposedValue). `CorrectReading` is
     the value you would write (for CONTESTED: both readings separated by ` || `). `Evidence` = repo-relative
     `path:line`. `ConventionIssue` = the rule at issue or `-`.
   - Items in SELECTION order; standard CSV quoting; final record `#END`.
2. `<RUN>/R2/PKG-00/_verify/V-<SHARD>_notes.md`: (i) counts checked / CONFIRMED / REFUTED / CONTESTED by
   class, and distinct items refuted on a verdict field (Disposition or Response); (ii) systematic patterns
   with example keys; (iii) effort.

Return (≤ 6 lines): counts by verdict, verdict-field refutations, top 3 patterns, the SHA-256 of your CSV.
