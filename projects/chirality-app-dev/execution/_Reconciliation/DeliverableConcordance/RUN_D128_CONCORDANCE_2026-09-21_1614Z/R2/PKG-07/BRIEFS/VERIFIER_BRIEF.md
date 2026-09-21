# Verifier shard brief and shared grading key — PKG-07 (TASK, Type 2)

You are a fresh, evidence-only verifier shard in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-07 manager (brief step 7). You do not delegate. **You never edit any
ledger, notes, reverse, errata or pregather file.** You write only your two shard files.
Your prompt supplies `<SHARD>` (e.g. `V-DEL-07-01`), `<UNIT>` (the unit folder), `<DEL-ID>`, and the
values of `<FROZEN_TREE>`, `<RUN>`. Never write an absolute path into an output.

## Inputs

- Your items: the rows of `<RUN>/R2/PKG-07/_verify/SELECTION.csv` whose `Shard` is `<SHARD>` (read by
  script; header `Shard,Unit,Class,ClaimKey,CapabilityID,ErrataField,Reason`).
- The unit's files in `<RUN>/R2/PKG-07/<UNIT>/`: `<DEL-ID>_claims.csv`, `_notes.md`, `_reverse.csv`,
  `_reverse_notes.md`, `_errata.csv` (if present). Read CSV rows by script, selecting your keys.
- The rulebook `<RUN>/CONVENTIONS.md` — read it in full; you grade against it.
- `<RUN>/RUN_BASIS.md` §3, §5 and the addenda; the evidence pack `<RUN>/R2/PKG-07/EVIDENCE_PACK/`;
  the capability files `<RUN>/R2/SURFACES/<AREA>_capabilities.csv` for class `c` items.
- The frozen tree `<FROZEN_TREE>` for deliverable text, code, tests and decision records.
- Do not read other units' folders, `<RUN>/R0_CALIBRATION/**` ledgers, the working repository's
  deliverable folders, or `projects/chirality-runtime/execution/**` (never list, grep or read it;
  exclude it explicitly in any search under `projects/chirality-runtime`). You may consult
  `<RUN>/R0_CALIBRATION/VERIFICATION.md` for grading patterns.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No installs, test runs, builds.
- [HELP_HUMAN consistency note, added after all PKG-07 shards had returned] Evidence roots are only
  the frozen App tree, `projects/chirality-runtime/{packages,tests}` and the run inputs — not Root
  `execution/`, not runtime `execution/**`. A verdict that relies on out-of-root evidence is recorded
  as `CONTESTED`, not `REFUTED`.

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
3. **Legacy vs live (§2.3 reachability).** The evidence pack's `REACHABILITY.csv` is an import-based,
   module-level starting map; in wave 1 it tagged as LIVE some modules the product never renders or
   executes. Workers were told to confirm reach from the actual entry point (rendered page, executed
   route handler, packaged runtime-service entry). Check the REACH tag against what the entry point
   actually executes: a tag that departs from the map with a stated, correct reason is CONFIRMED; a LIVE
   tag on code the product demonstrably never executes is REFUTED on ImplementationEvidence (REACH).
   Where the capability files' symbol-level notes (RTCORE/RTCONTRACT/HARNESS) disagree with the module
   map and the difference would change the Disposition, grade `CONTESTED` and give both readings. A
   requirement met only on a LEGACY_ONLY or non-executed path judged ALIGNED is REFUTED.
4. **MR-11 vs AUTHORITY_CONFLICT (§1).** MR-11 needs a ruling that explicitly addresses the clause or
   deliverable. A ruling (D-GOV-43 / D-APP-127) that undercuts an unamended GOVERNING clause without
   naming it → AUTHORITY_CONFLICT with R4 / R4-Qn. Where DIRECTIVE §0 resolves it, AUTHORITY_CONFLICT is
   wrong. Check whether the row's `R4-Q1..Q5` citation fits the named question; a plain `R4` where a
   named question applies is REFUTED on HumanDecisionNeeded.
5. **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH vs STALE_ASSESSMENT (§2.6, §2.7, MR-8).**
   STALE_SPECIFICATION = text flatly asserting a now-false state; REMAINING_STATE_MISMATCH = metadata
   or register lag (dates, dependency mirrors, lifecycle state vs remaining); STALE_ASSESSMENT only when
   the overtaken assessment conclusion is the operative defect. A snapshot-true claim is a REGISTER row
   (MR-8 iv). Apply the adopted tie-break in CONVENTIONS §2.6 (RUN_BASIS Addendum 5) to these ledgers:
   a present fact now false → STALE_SPECIFICATION; REMAINING_STATE_MISMATCH only for Remaining /
   REMAINING_WORK status contradictions or register bookkeeping lag that says nothing false; if both
   still fit, the deliverable-text-repair verdict with `ALSO:<verdict>` in Notes. A verdict contrary to
   the tie-break is REFUTED; where the tie-break itself leaves both open, CONTESTED.
   `R4-Q4` (Addendum 4) and `R4-Q5` (Addendum 7: Codex event payloads stored as received vs
   translated) are valid named questions; plain `R4` where R4-Q4 or R4-Q5 applies is REFUTED on
   HumanDecisionNeeded.
5a. **Legacy-versus-live subject test (RUN_BASIS Addendum 6; CONVENTIONS §2.4).** Grade against it:
   the subject is product behaviour when the claim names the App/system/user/session/turn/agent run,
   states an observable outcome, or states a guarantee or control (permission, path containment,
   hooks, redaction, approval); it is the module only when the claim names a specific code unit and
   describes only that unit's own contract. Both readings possible → product behaviour, judged on the
   live path. `R4-Q1` must appear in HumanDecisionNeeded on every row whose only code meeting the claim
   is `REACH=LEGACY_ONLY` (missing → REFUTED on HumanDecisionNeeded); rows met by LIVE code or with no
   code evidence must not cite R4-Q1 for that reason. A product-behaviour row met only by legacy code
   should carry `ALSO_MODULE:<verdict>` in Notes (missing → REFUTED on Notes). A module-level reading
   of a product-behaviour claim that produced a different Disposition is REFUTED on Disposition. Where
   rule 1 genuinely leaves the subject open, rule 2 decides it, so CONTESTED on subject grounds should
   be rare.
5b. **Authority order.** The App DIRECTIVE §2.8 was never amended for D-GOV-43; do not assume the
   Codex-only preambles of PRD/CONTRACT win automatically. Grade by CONVENTIONS §1 and DIRECTIVE §0.
5c. **Implementation outside evidence roots.** Evidence roots are App `projects/chirality-app-dev/**`
   and `projects/chirality-runtime/{packages,tests}/**` only. A row that cites Root `tools/` or Root
   `execution/` as ImplementationEvidence is REFUTED on ImplementationEvidence; do not read those
   trees yourself.
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

1. `<RUN>/R2/PKG-07/_verify/<SHARD>.csv` — header exactly
   `Shard,Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`,
   one record per SELECTION item in SELECTION order, final record `#END`. Use a CSV writer (quote
   fields; no raw newlines inside fields). `Field` = the field at issue (`-` when CONFIRMED);
   `RowValue` = the row's value for it; `CorrectReading` = your reading (both readings for CONTESTED,
   separated by ` || `); `Evidence` = repo-relative `path:line`; `ConventionIssue` = the rule
   (e.g. `§2.6 MR-8`, `grading key 4`) or `-`. For class `e`, `Field` is the errata Field.
2. `<RUN>/R2/PKG-07/_verify/<SHARD>_notes.md` — (i) counts checked / CONFIRMED / REFUTED / CONTESTED
   by class; (ii) systematic patterns with example keys; (iii) effort.

Return ≤ 5 lines: verdict counts, the top 2 patterns, the SHA-256 of your CSV.
