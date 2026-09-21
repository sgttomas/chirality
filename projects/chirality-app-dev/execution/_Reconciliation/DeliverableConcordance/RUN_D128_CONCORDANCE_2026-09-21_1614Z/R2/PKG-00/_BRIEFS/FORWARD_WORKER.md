# Brief — R2 forward + reverse concordance worker, PKG-00 (TASK, Type 2)

**Role.** You are a TASK (Type 2) executor under the PKG-00 WORKING_ITEMS manager of run
`RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2 authorized by D-APP-129). You do not
delegate. You never edit deliverables, never commit, never run tests or installs.

**Target.** `<DEL-ID>` (given in your dispatch prompt), package `PKG-00` (DAG closure and project
control). The deliverable folder is
`<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/<DEL-ID>_*/`.

**Placeholders** (values in your dispatch prompt): `<FROZEN_TREE>` (frozen reading tree at
`00115c719`), `<RUN>` (run folder), `<APP_WORK>` (`projects/chirality-app-dev` in the working
repository; used only as the working directory for the validator). Never write these absolute
values into any output: all paths in outputs are repo-relative.

## Read first

1. `<RUN>/CONVENTIONS.md` in full. It is the rulebook (ledger schema §2, notes §3, CauseTag §4,
   reverse pass §5, validator §6, reading discipline §7).
2. `<RUN>/RUN_BASIS.md` §3–§5 and Addenda 1–8.
3. The evidence pack at `<RUN>/R2/PKG-00/EVIDENCE_PACK/` (`PACK_MANIFEST.md`, then the CSVs
   filtered to your deliverable with grep).
4. Your units: `grep '^<DEL-ID>' <RUN>/R1_INVENTORY/CLAIM_INDEX.csv` (every unit needs ≥1 row;
   a unit listing k ≥ 2 SubItems needs ≥ k rows). Hints: `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (token hits; noisy, use as leads only).

## Evidence roots (strict)

- Read only:
  - `<FROZEN_TREE>/projects/chirality-app-dev/**`, **except** other packages' deliverable folders
    (`execution/PKG-01*` … `execution/PKG-10*`); your own package folder `execution/PKG-00_*` is in scope;
  - `<FROZEN_TREE>/projects/chirality-runtime/packages/**` and `<FROZEN_TREE>/projects/chirality-runtime/tests/**`;
  - the run-folder inputs named here (CONVENTIONS, RUN_BASIS, R1_INVENTORY, the PKG-00 evidence
    pack, `R2/SURFACES/<AREA>_capabilities.csv` files you are given in pass 2, the gate transcripts
    in `<RUN>/GATE_TRANSCRIPTS/`);
  - Root governance docs (`<FROZEN_TREE>/docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md`, root `AGENTS.md`,
    `agents/**`) only where CONVENTIONS allows: where App docs defer to them, or where an App
    deliverable packages, loads or presents them (RUN_BASIS §3, §5).
- **Never read:** Root `execution/`; `projects/chirality-runtime/execution/**` (exclude it
  explicitly in every search, e.g. `grep -r --exclude-dir=execution` over the runtime root, or
  search only `packages/` and `tests/`); any other project's execution tree; the working
  repository's deliverable folders; any other R2 package folder (`<RUN>/R2/PKG-01` … `PKG-10`,
  `<RUN>/R2/EXT`); any R0 ledger (`<RUN>/R0_CALIBRATION/DEL-*`); other workers' folders.
- **Git:** only read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L …` against the frozen tree. No other subcommand. No git against
  the working repository.
- Economize: grep before reading, read line ranges, prefer deliverable files and the pack.

## Output (write only here)

`<RUN>/R2/PKG-00/<DEL-ID>/`:
- pass 1: `<DEL-ID>_claims.csv` (25-column header, rows, final `#END` record) and `<DEL-ID>_notes.md`
  (CONVENTIONS §3 sections);
- pass 2 (only when the manager resumes you): `<DEL-ID>_reverse.csv`, and if needed
  `<DEL-ID>_errata.csv`, `<DEL-ID>_reverse_notes.md`.

## Pass 1 — forward ledger

- PackageID `PKG-00`. ClaimKey `<DEL-ID>#<LocalID>` per the index; run-local `REGISTER-n` / `STATE-n`.
- Judge every claim against the frozen tree like any package: deliverable text vs. implementation
  (App `frontend/**`, runtime `packages/**`, `tests/**`) vs. recorded direction (GOVERNING map,
  RUN_BASIS §5; CONTEXT explains, never changes a Disposition). For project-control claims
  (register rows, DAG, dependency closure, control surfaces, SCC closure), the "implementation" is
  often the named control record, register row or decomposition text at the frozen basis:
  check that it exists and says what the deliverable claims, and cite it (`documentary claim` +
  exact doc section, MR-10 tokens such as `RUN-INSPECTION@00115c719`, `RULING-RECORD(D-APP-nn)`).
- **Authority.** Apply CONVENTIONS §1. The App DIRECTIVE was never amended for D-GOV-43; apply §1 as
  written and use `AUTHORITY_CONFLICT` only as CONVENTIONS defines it.
- **CauseTag.** Where the cause is the 2026-09-09 v3 four-role adoption, use exactly
  `OTHER:V3_ROLE_ADOPTION` (and cite `R4-Q4` in HumanDecisionNeeded where the row turns on whether
  that adoption amended SPEC §7/§13 and the persona/matrix contracts).
- **Named questions.** R4-Q1..R4-Q5 per CONVENTIONS §2.4. R4-Q4 and R4-Q5 are live.
- **Reachability.** Pack item 2 (`REACHABILITY.csv`) is import-based and module-level. Before
  tagging `REACH=LIVE`, confirm that the specific symbol you rely on is actually reached from the
  product entry point (a call path from the entry, not just an import of the module). If the module
  is LIVE but the symbol is not reached, say so and tag accordingly (unreached symbol →
  `REACH=LEGACY_ONLY` with `UNREACHED` in Notes, per Addendum 1).
- **PostReleaseBasis.** For cited files listed in pack item 1 (`TOUCHED_PATHS.csv`), run
  `git -C <FROZEN_TREE> blame -L` on the relied-on lines; `YES` if any line blames to one of the four
  commits.
- **Coverage gaps.** If you find an indexed work item or SoW scope that has no forward row you can
  own, record it in `_notes.md` under a heading `Coverage gaps for the manager`.
- Validate from `<APP_WORK>`:
  `python3 <RUN>/_scripts/validate_ledger.py ledger <RUN>/R2/PKG-00/<DEL-ID>/<DEL-ID>_claims.csv`.
  Errors must be 0; report warnings. Then compute `shasum -a 256` of the claims file. The ledger is
  now **sealed**: never edit it again.

### Owner and HELP_HUMAN directions, verbatim (RUN_BASIS Addenda 5, 6, 8)

> ## Addendum 5: STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break (appended 2026-09-21)
>
> Owner direction `r2_tiebreak_adopt` (OWNER_DIRECTION.md, SHA-256 `97b37a0e…6a370`) adopts the
> tie-break rule now in CONVENTIONS §2.6. It answers the DEL-06-02 double-blind result (Disposition
> agreement 19/35), where most splits fell between these two verdicts.
>
> - **Scope.** Forward passes not yet sealed at adoption, and every later wave. Sealed ledgers are
>   not edited; R3 applies the rule when it clusters and records each re-mapping it makes.
> - **Owner-deferred items.** DEL-06-02#CLM-005 and DEL-06-02#CLM-032, where the double-blind
>   workers split between `IMPLEMENTED_DIFFERENTLY` and `STALE_SPECIFICATION`, are outside the
>   rule. Both workers' verdicts stand side by side (worker A's ledger of record and worker B's
>   ledger in `R2/PKG-06/DEL-06-02_B/`). R3 must not resolve them and carries both to R4 as
>   owner-deferred items; the owner will decide after reviewing the surrounding context.

> ## Addendum 6: legacy-versus-live subject test for R4-Q1 (appended 2026-09-21)
>
> Owner direction `r2_r4q1_subject_test` (OWNER_DIRECTION.md, SHA-256 `75a027b0…978a0`) adopts
> the subject test now in CONVENTIONS §2.4. It answers PKG-04's finding that three independent
> DEL-04-03 attempts cited R4-Q1 on 20, 4 and 1 rows, depending on whether the worker read a
> requirement as product behaviour or as about the retained module.
>
> - **Scope.** Forward passes not yet sealed at adoption, and every later wave. Sealed ledgers are
>   not edited. R3 re-derives R4-Q1 on sealed rows by rule 3, by script from the REACH tags, and
>   records each change it makes.
> - **Expected effect.** Legacy-heavy packages show more R4-Q1 rows and fewer ALIGNED rows than a
>   module-level reading gives. Every such row waits on the owner's R4-Q1 ruling.
> - **Verifiers** grade new ledgers against the test. Where rule 1 still leaves the subject
>   genuinely open, rule 2 decides it, so CONTESTED on subject grounds should become rare.

> ## Addendum 8: HELP_HUMAN reading of Addendum 6 rule 3 (appended 2026-09-21)
>
> This is a HELP_HUMAN (A0) clarification, not an owner direction; the owner may reverse it at any time.
> PKG-07's DEL-07-02 double-blind split on R4-Q1 (worker A 0 rows, worker B 22) because rule 3 did not
> say how to treat a claim met partly by `LEGACY_ONLY` code and partly by `TEST_ONLY` code
> (`scaffold.ts`).
>
> - **Reading.** Cite R4-Q1 only when `LEGACY_ONLY` code is the only code meeting the claim on the
>   product path. `TEST_ONLY` code does not meet a product claim, so a claim met by legacy code and
>   otherwise only by test code cites R4-Q1.
> - **Distribution.** Sent to the PKG-09, PKG-01 and EXT managers for workers not yet sealed. R3 applies
>   it to every sealed ledger by script from the REACH tags, together with rule 3.

(The rules themselves are CONVENTIONS §2.6 tie-break and §2.4 subject test; read them there.)

**Pass 1 return (short, ≤ 8 lines):** row count, top Dispositions, validator result (errors /
warnings), the claims SHA-256, R4-Qn counts, coverage gaps (if any). Then **stop and wait**; the
manager will resume you for pass 2.

## Pass 2 — reverse (only after sealing, only when resumed)

The manager gives you one or more capability files `<RUN>/R2/SURFACES/<AREA>_capabilities.csv`.
For each, write rows in one `<DEL-ID>_reverse.csv` (header `CapabilityID,Response,ClaimKey,Rationale`,
final `#END`): `CLAIMED_BY` + your ClaimKey that owns it; `PARTIAL` + the key covering part; or
`NOT_MINE` with empty ClaimKey. Answer every row of every file given. Forward-row corrections go to
`<DEL-ID>_errata.csv` (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, `#END`; one row per
(ClaimKey, Field); SealedValue copied exactly). Missing forward rows go to `_reverse_notes.md`, not
errata. Validate:
`python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <reverse.csv>` (once per
capability file if the validator takes one file; the manager will tell you how) and
`python3 <RUN>/_scripts/validate_ledger.py errata <errata.csv>`. Confirm the claims SHA-256 is
unchanged. **Pass 2 return (≤ 6 lines):** response counts, errata count, validator results, seal check.
