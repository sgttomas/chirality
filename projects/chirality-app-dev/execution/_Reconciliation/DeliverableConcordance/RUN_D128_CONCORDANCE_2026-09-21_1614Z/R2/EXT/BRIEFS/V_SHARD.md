# EXT verifier shard brief (shared grading key for every EXT shard)

You are a fresh, evidence-only TASK (Type 2) verifier shard. Do not delegate. **Never edit
any ledger, notes or errata file.** Write only your two shard files under
`<RUN>/R2/EXT/_verify/`. Your shard ID is given in your prompt.

## Inputs

- Your shard's rows in `<RUN>/R2/EXT/_verify/SELECTION.csv` (column `Shard`); read it with a
  small python `csv` script.
- The sealed ledgers they cite, read-only: `DEC` → `<RUN>/R2/EXT/DEC/DEC_claims.csv`;
  `SOW` → `<RUN>/R2/EXT/SOW/SOW_claims.csv`; `DOC-BUILDREL|RQGATES|RQRUN` →
  `<RUN>/R2/EXT/DOC_REL/`; `DOC-VALSTRAT|RELIANCE` → `<RUN>/R2/EXT/DOC_VAL/`; the six item
  6/7 ledgers → `<RUN>/R2/EXT/DOC_DEV/`. Also the matching `_notes.md` and any `_errata.csv`.
- The rulebook: `<RUN>/CONVENTIONS.md` (read §2, §4, §8 in full) and
  `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` (the rules the workers were given, including the
  Addendum 5 tie-break, the Addendum 6 subject test and the mixed-row R4-Q1 reading).
  `<RUN>/RUN_BASIS.md` §5 (authority map, flagged rulings) and Addenda 3–7.
- The worker brief for the ledger's family (`<RUN>/R2/EXT/BRIEFS/W_*.md`) for unit guidance.
- Evidence: same roots as the workers (see `_COMMON_RULES.md` "Evidence roots"). The
  evidence pack is `<RUN>/R2/EXT/EVIDENCE_PACK/`.

## Grading key (the same for every shard)

For each selected item open the cited evidence at `<FROZEN_TREE>` and decide:

- `CONFIRMED`: the row's Disposition holds, and the other fields you checked hold or have
  only immaterial slips (write them in `ConventionIssue`, not as REFUTED).
- `REFUTED`: a field is wrong on the evidence. Give **one verdict line per wrong field**
  (repeat the ClaimKey), with `Field` naming it and `CorrectReading` giving the right value.
  A wrong Disposition is always its own line with `Field = Disposition`.
- `CONTESTED`: reasonable either way on the evidence, or your verdict relies on evidence
  outside the roots (then say so). Give both readings separated by ` || `.

Check, in this order:

1. **Disposition** against CONVENTIONS §2.6 and §8 column guidance: item 3 ALIGNED only if
   the ruled effect actually landed; flagged rulings (D-APP-104, 107, 121, 122, 123, 125, 126)
   judged against their flag, never treated as landed; item 5 `.1`/`.2` logic and OUT rows
   ALIGNED when no live deliverable implements them; items 4/6/7 "does the section match what
   shipped / is it accurate". Apply the Addendum 5 tie-break literally
   (STALE_SPECIFICATION for a now-false present fact; REMAINING_STATE_MISMATCH only for
   Remaining items / REMAINING_WORK rows or lagging bookkeeping). `ACCEPTED_DIVERGENCE` needs
   a GOVERNING ruling permitting the difference; CONTEXT alone never suffices.
2. **Evidence**: cited paths and line numbers exist at `<FROZEN_TREE>` and say what the row
   says; REACH tags match `EVIDENCE_PACK/REACHABILITY.csv`; code-evidence rows carry a tag.
3. **R4-Q1** by rule 3 and the mixed-row reading: cited exactly when LEGACY_ONLY code is the
   only code meeting the claim on the product path (TEST_ONLY never meets a product claim);
   product-behaviour rows met only by legacy code carry `ALSO_MODULE:` in Notes. Other
   HumanDecisionNeeded tokens: named R4-Qn preferred over plain R4; Q-01..Q-13 never used.
4. **CauseTag** (§4 precedence; `OTHER:V3_ROLE_ADOPTION` for the four-role adoption;
   `UNRECORDED_JUDGMENT` only with DirectionEvidence NONE_FOUND), **DirectionEvidence**
   (CTX:/GOV: prefixes; NOT_APPLICABLE on ALIGNED/NOT_AUDITABLE), **AuthorityTier** (highest
   source restated), **LatestDecision**, **PostReleaseBasis** (against
   `EVIDENCE_PACK/TOUCHED_PATHS.csv` line ranges), **AUDIT-ONLY / ROUTE:ROOT (Δ10)** on item
   6/7 non-ALIGNED rows.
5. Class `e` items: check the errata row's ProposedValue for that Field instead of the sealed
   value.

Many rows share evidence; open it once and reuse it, but give every selected item at least
one verdict line.

## Limits

Git only as read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show`,
`git -C <FROZEN_TREE> blame -L`: no merge-base, no ls-files, no other subcommand, and no git
against the working repository. No installs, no test runs. Never read Root
`<FROZEN_TREE>/execution/**`, `projects/chirality-runtime/execution/**`, other R2 package
folders, R0 ledgers, or the working repository's deliverable folders. No absolute paths in
outputs.

## Outputs

1. `<RUN>/R2/EXT/_verify/V-<Shard>.csv`, header exactly
   `Shard,Ledger,Class,ClaimKey,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`,
   one or more lines per SELECTION item in selection order, no newlines inside fields, final
   record `#END`. `Field` = `-` when CONFIRMED. `RowValue` = the ledger's (or errata's)
   value for that field. `Evidence` = repo-relative `path:line`. `ConventionIssue` = the rule
   misapplied or found ambiguous, or `-`.
2. `<RUN>/R2/EXT/_verify/V-<Shard>_notes.md`: (i) counts checked / CONFIRMED / REFUTED /
   CONTESTED by class and by Field; (ii) systematic patterns with example keys; (iii) effort.

Write the notes file last (it is the manager's completion signal). Reply in at most 6 lines:
counts by verdict, top 3 patterns, SHA-256 of your CSV.
