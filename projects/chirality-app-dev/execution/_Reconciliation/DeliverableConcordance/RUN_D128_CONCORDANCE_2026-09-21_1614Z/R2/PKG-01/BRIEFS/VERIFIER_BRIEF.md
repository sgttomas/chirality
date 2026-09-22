# Verifier shard brief and shared grading key — PKG-01 (TASK, Type 2)

You are a fresh, evidence-only verifier shard in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-01 manager (brief step 7). You do not delegate. **You never edit any
ledger, notes, reverse, errata or pregather file.** You write only your two shard files.
Your prompt supplies `<SHARD>` (e.g. `V-DEL-01-01`), `<UNIT>` (the unit folder), `<DEL-ID>`, and the
values of `<FROZEN_TREE>`, `<RUN>`. Never write an absolute path into an output.

## Inputs

- Your items: the rows of `<RUN>/R2/PKG-01/_verify/SELECTION.csv` whose `Shard` is `<SHARD>` (read by
  script; header `Shard,Unit,Class,ClaimKey,CapabilityID,ErrataField,Reason`).
- The unit's files in `<RUN>/R2/PKG-01/<UNIT>/`: `<DEL-ID>_claims.csv`, `_notes.md`, `_reverse.csv`,
  `_reverse_notes.md`, `_errata.csv` (if present). Read CSV rows by script, selecting your keys.
- The rulebook `<RUN>/CONVENTIONS.md` — read it in full; you grade against it.
- `<RUN>/RUN_BASIS.md` §3, §5 and the addenda; the evidence pack `<RUN>/R2/PKG-01/EVIDENCE_PACK/`;
  the capability files `<RUN>/R2/SURFACES/<AREA>_capabilities.csv` for class `c` items.
- The frozen tree `<FROZEN_TREE>` for deliverable text, code, tests and decision records.
- Evidence roots: read only `<FROZEN_TREE>/projects/chirality-app-dev/**` (not other packages'
  deliverable folders) and `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, plus the
  run-folder inputs above; Root `docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md` where App docs defer to them and
  the D-GOV-43 record (`docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/**`);
  Root instruction sources only where the deliverable packages them. **Never** Root `execution/**`, never
  `projects/chirality-runtime/execution/**` (exclude it explicitly in any search), never the working
  repository's deliverable folders.
- Do not read other units' folders (you may read the unit named in your prompt and, for DEL-01-02, its
  `S1/` and `S2/` halves and `PREGATHER.md`) or other `<RUN>/R2/PKG-*` folders. You may consult
  `<RUN>/R0_CALIBRATION/VERIFICATION.md` for grading patterns only; do not read R0 ledgers.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L` — no other git subcommand, nothing
  against the working repository. No installs, test runs, builds.

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
3. **Legacy vs live (§2.3 reachability).** The evidence pack's `REACHABILITY.csv` is the static,
   import-based, module-level map: a re-export or one imported helper marks a whole module LIVE, and
   some LIVE-tagged modules are never rendered or executed. Check reach **for the specific symbol**
   from an actual entry point (rendered page/component, executed API route, `frontend/electron/main.ts`,
   packaged runtime-service entry). A `REACH=LIVE` tag on a symbol no entry reaches is REFUTED on
   ImplementationEvidence; if that changes the Disposition (e.g. ALIGNED on an unreached symbol), it is
   REFUTED on Disposition. Where the capability files' symbol-level notes disagree with the module map
   and reach genuinely cannot be settled statically, grade `CONTESTED` with both readings. A
   requirement met only on a LEGACY_ONLY path judged ALIGNED is REFUTED.
4. **MR-11 vs AUTHORITY_CONFLICT (§1).** MR-11 needs a ruling that explicitly addresses the clause or
   deliverable. A ruling (D-GOV-43 / D-APP-127) that undercuts an unamended GOVERNING clause without
   naming it → AUTHORITY_CONFLICT with R4 / R4-Qn. Where App DIRECTIVE §0's authority order resolves a
   disagreement among GOVERNING sources, AUTHORITY_CONFLICT is wrong (the row should apply the order and
   cite both). PKG-01 note: App DIRECTIVE (including §2.8, the Claude/Anthropic key-aware default) carries
   no D-GOV-43 amendment, while PRD and CONTRACT carry Codex-only preambles. A row that treats a lower
   document's preamble as overriding a higher unamended source, without a ruling that names the clause,
   misapplies §1; grade it on the rulebook, CONTESTED only where §1 genuinely admits both readings.
   Check whether the row's `R4-Q1/Q2/Q3/Q4/Q5` citation fits the named question; a plain `R4` where a
   named question applies is REFUTED on HumanDecisionNeeded (every PKG-01 ledger was sealed after
   Addenda 4–7 reached its worker).
4a. **Legacy-versus-live subject test (CONVENTIONS §2.4, RUN_BASIS Addendum 6).** Every PKG-01 ledger
   was sealed after the test reached its worker; grade against it: subject decided from the claim text
   (product behaviour if it names the App/system/user/session/turn/agent run, an observable outcome, or a
   guarantee or control; module only if it names a code unit and only that unit's own contract); if both
   readings fit, product behaviour on the live path; `R4-Q1` in HumanDecisionNeeded on every row whose
   only meeting code is `REACH=LEGACY_ONLY` (missing R4-Q1 there is REFUTED on HumanDecisionNeeded; R4-Q1
   on a row met by LIVE code or with no code evidence is REFUTED on HumanDecisionNeeded); product-behaviour
   rows met only by legacy code carry `ALSO_MODULE:<verdict>` in Notes. CONTESTED on subject grounds only
   where rule 1 leaves it open and rule 2 still cannot decide.
   HELP_HUMAN clarification of rule 3: cite R4-Q1 only when LEGACY_ONLY code is the only code meeting the
   claim on the product path. TEST_ONLY code does not meet a product claim. Every PKG-01 ledger sealed before this
   clarification: where a row's R4-Q1 differs only because of it, grade CONTESTED with a note, not REFUTED.
5. **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH vs STALE_ASSESSMENT (§2.6 incl. the Addendum 5
   tie-break, §2.7, MR-8).** Apply the §2.6 tie-break exactly:
   (1) STALE_SPECIFICATION when the text states a present fact that is now false (a hash recorded as
   `MATCH`, a path called "current", a dependency marked `SATISFIED`, a file said to exist) — same for
   SoW, `_STATUS`, register and references text; (2) REMAINING_STATE_MISMATCH only for (a) a
   `## Remaining` item or `REMAINING_WORK` row whose open/done status is contradicted by evidence, or
   (b) register bookkeeping that is behind but says nothing false about the product or its references
   (a `Last Updated` date, a `TBD` placeholder, a lagging status field); (3) a snapshot-tied claim
   ("MATCH at v23") stays a REGISTER row, a restatement as current takes STALE_SPECIFICATION with
   `SEE:` to it; (4) if both still fit, the verdict whose repair is a change to deliverable text, with
   `ALSO:<verdict>` in Notes. A row that picks the other verdict where the tie-break clearly decides is
   REFUTED on Disposition; CONTESTED only where the tie-break itself leaves it open. STALE_ASSESSMENT
   only when the overtaken assessment conclusion is the operative defect.
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
14. **Evidence roots.** A verdict that relies on evidence outside the permitted roots (for example Root
    `execution/`) is recorded as `CONTESTED`, never `REFUTED` (HELP_HUMAN note). Better: do not read it.
15. **CauseTag spelling.** Where the cause is the 2026-09-09 v3 four-role adoption, the converged spelling is
    `OTHER:V3_ROLE_ADOPTION`; a different spelling of the same cause is a note, not a refutation.
Many rows share evidence — open it once, apply it, but give every item its own verdict line.

## Outputs

1. `<RUN>/R2/PKG-01/_verify/<SHARD>.csv` — header exactly
   `Shard,Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`,
   one record per SELECTION item in SELECTION order, final record `#END`. Use a CSV writer (quote
   fields; no raw newlines inside fields). `Field` = the field at issue (`-` when CONFIRMED; several
   fields separated by `; `); `RowValue` = the row's value for it; `CorrectReading` = your reading (both
   readings for CONTESTED, separated by ` || `); `Evidence` = repo-relative `path:line`;
   `ConventionIssue` = the rule (e.g. `§2.6 MR-8`, `grading key 4`) or `-`. For class `e`, `Field` is the
   errata Field.
2. `<RUN>/R2/PKG-01/_verify/<SHARD>_notes.md` — (i) counts checked / CONFIRMED / REFUTED / CONTESTED
   by class; (ii) systematic patterns with example keys; (iii) effort.

Return ≤ 5 lines: verdict counts, the top 2 patterns, the SHA-256 of your CSV.
