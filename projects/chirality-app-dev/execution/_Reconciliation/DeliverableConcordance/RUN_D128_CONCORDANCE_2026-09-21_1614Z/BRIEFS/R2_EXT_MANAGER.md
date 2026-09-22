# Brief — R2 scope-extension concordance manager (WORKING_ITEMS, Type 1)

**Role.**
- You are WORKING_ITEMS and own the scope-extension audit (`EXT`), items 3–7 of D-APP-129
  ruling D.
- You dispatch TASK workers (Type 2, no delegation) and verifier shards, and you integrate
  their returns.
- You never edit deliverables, governing documents or audited documents, and never commit.
  You return to HELP_HUMAN.

**Run.** `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2 and the scope extension
authorized by D-APP-129).

**Placeholders**, supplied at dispatch: `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`, as in the
other briefs.

**Read first:**
- `<RUN>/CONVENTIONS.md`, in full. **§8 is your unit and schema definition.** §10 is the
  operating rules, and §2.4 and §2.6 hold the rules added by RUN_BASIS Addenda 4–7.
- `<RUN>/RUN_BASIS.md`, including all addenda. §5 is the authority map, and flags the RULED
  rows whose effect is pending, held or unapplied.
- `<RUN>/BRIEFS/R2_PACKAGE_MANAGER.md`. Follow its steps 1, 5, 7 and 8 and its Rules section,
  adapted as below. Where this brief differs, this brief wins.
- `<RUN>/R0_CALIBRATION/R0_CALIBRATION_REPORT.md` §3, §4 and §8.
- `agents/AGENT_WORKING_ITEMS.md` and `agents/AGENT_TASK.md` in `<FROZEN_TREE>`.

## Units and ledgers

The checklist is `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv` (221 units). Every unit gets a row.

| Item | Ledger file(s) | Units | Workers |
|---|---|---:|---|
| 3 | `DEC_claims.csv` | 38 (`DEC:D-APP-86..127`, RULED only) | 1 |
| 4 | `DOC-BUILDREL`, `DOC-RQGATES`, `DOC-VALSTRAT`, `DOC-RQRUN`, `DOC-RELIANCE` `_claims.csv` | 15 + 14 + 9 + 7 + 13 = 58 | 2: (BUILDREL, RQGATES, RQRUN) and (VALSTRAT, RELIANCE) |
| 5 | `SOW_claims.csv` | 84 (`SOW:SOW-001..084`) | 2, split SOW-001..042 and SOW-043..084 into subfolders; you merge by script and validate the merged file |
| 6, 7 | `DOC-PRODAGENTS`, `DOC-ADDING_A_TOOL`, `DOC-README`, `DOC-RUNTIME_ENGINE_CONTRACT`, `DOC-TOOL_CATALOG`, `DOC-TRACEABILITY` `_claims.csv` | 9 + 32 = 41 | 1. **Audit-only** (§8): `AUDIT-ONLY` in RemainingWork on every non-ALIGNED row; item 6 adds `ROUTE:ROOT (Δ10)` |

That is 6 forward workers. Each writes its ledgers, `_notes.md` per ledger stem, and validates
with `validate_ledger.py ledger` (coverage is checked against EXTENSION_INDEX). You record the
sealed SHA-256.

## Steps

1. **Preflight.** `app_hold.py` accepts only deliverable targets (`--target EXT` is
   rejected), and extension workers read across deliverables. So, from `<APP_WORK>`, run
   `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path "RECONCILIATION:D-APP-128:R2" --target <DEL-ID>`
   for each of the 54 deliverables. Write stdout to `<RUN>/R2/EXT/PREFLIGHT/<DEL-ID>.json`;
   do not use `--output`. Any deliverable whose verdict is not `ALLOW` is out of bounds for
   every EXT worker: list it in every worker brief and report it.
2. **Evidence pack** at `<RUN>/R2/EXT/EVIDENCE_PACK/`:
   - copy items 1, 2 and 5 byte-for-byte from `<RUN>/R2/_shared/EVIDENCE_PACK/` and confirm
     the SHA-256 values;
   - run the `<RUN>/R2/_scripts/` item 3 and item 4 scripts (`reference_hashes.py`,
     `decision_hits.py`) with `--all` instead of `--package`, because extension units cut
     across packages;
   - write `PACK_MANIFEST.md`.
3. **Forward pass**: the 6 workers above, at most 4 at a time.
4. **No reverse pass.** [A0] Capability ownership is a deliverable question. Extension units
   do not answer CLAIMED_BY / PARTIAL / NOT_MINE; R3 uses extension findings as cross-package
   evidence. Workers may still file `_errata.csv` against their own sealed ledger if they find
   a defect before you verify. Validate errata with `validate_ledger.py errata --ledger`.
5. **Verification**, per the package brief step 7 as revised by Addendum 3:
   - the rerun threshold counts verdict-field (Disposition) refutations only; report it on
     ledger rows;
   - other-field refutations go to `<RUN>/R2/EXT/CORRECTIONS.csv`;
   - write `<RUN>/R2/EXT/VERIFICATION.md`.
6. **Summary.** Produce `<RUN>/R2/EXT/EXT_SUMMARY.md` **by script**, with the package
   summary's censuses per item and per ledger. Add a short hand-written section of
   cross-package observations for R3. It must include:
   - item 3: RULED decisions whose effect did not land, by decision;
   - item 5: SOW rows with no live deliverable, or with neither code nor an explicit deferral;
   - item 4: sections that describe a release process that did not run, including
     notarization, signing and the release-quality gates.

## Unit guidance (in addition to CONVENTIONS §8)

- **Item 3.** Read the register row and its ruling record, then find where the stated effect
  should appear: code, deliverable text or `_STATUS`.
  - Use the `D-APP-127_APPLICATION_MAP.csv` pack item for D-APP-127.
  - Judge each flagged row against its RUN_BASIS §5 flag.
  - A ruling's effect in deliverable text is judged from the frozen tree's deliverable
    folders. Unlike the package workers, the DEC worker **may** read any deliverable folder
    in `<FROZEN_TREE>`, read-only, because that is where the effect lands.
- **Item 5.** Mapping to "a live deliverable" is judged from the decomposition text and the
  deliverables' SoWs in the frozen tree, which the SOW workers may read. The same applies to
  the DOC workers where a section names a deliverable.
- **Items 4, 6 and 7.** `.github/workflows/{harness-premerge,desktop-release-template}.yml`
  and release AgentRuns records under `projects/chirality-app-dev/execution/_Coordination/AgentRuns/`
  are evidence only.
  - For "what shipped", use code, build scripts, the BUILD and ELECTRON capability files in
    `<RUN>/R2/SURFACES/`, and the gate transcripts in `<RUN>/GATE_TRANSCRIPTS/`.
  - Governing documents and the invariant coverage register are not audit targets (§8).
- **Rules to give every worker verbatim:** the Addendum 5 tie-break (§2.6) and the Addendum 6
  subject test (§2.4).
- **Named questions:** R4-Q1..R4-Q5 (§2.4).
- **CauseTag:** where the cause is the v3 four-role adoption, use exactly
  `OTHER:V3_ROLE_ADOPTION`.
- **Done-declaration questions** Q-01..Q-13 are CONTEXT: mention them in Notes, never as
  HumanDecisionNeeded.

## Rules

- **Concurrency.** At most **4** of your children alive at once, counting forward workers
  and verifiers. Every spawn uses `model: "opus"`.
- **Notifications.** Child completion notifications go to HELP_HUMAN, not to you. Drive the
  work from files: poll with a Bash `until` loop (sleep 30–60 s), checking for `#END` and a
  passing validator. Do not end your turn until the whole undertaking is complete.
- **Validation.** Run the validator from `<APP_WORK>`. A failing output goes back to its
  worker once; after that, a fresh worker reruns it. Never patch a child's CSV. A rerun brief
  may restate the rules in general terms, but must not cite the verifier's specific rows.
- **State.** Keep `<RUN>/R2/EXT/STATE.jsonl`, one line per dispatch or return. You are its
  only writer.
- **Evidence roots, for workers and verifiers alike:**
  - Read only `<FROZEN_TREE>/projects/chirality-app-dev/**`,
    `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, the run-folder inputs
    named here, and Root governance documents only where CONVENTIONS allows.
  - Not Root `execution/`, and not `projects/chirality-runtime/execution/**`. Exclude both
    explicitly in any search.
  - Never read the working repository's deliverable folders, other R2 package folders, or
    any R0 ledger before sealing.
  - A verifier verdict that relies on evidence outside these roots is recorded as
    CONTESTED.
- **Git.** Read-only `git log/show/blame` against `<FROZEN_TREE>` only. No other git, no
  installs, no test runs.
- **Paths.** No absolute paths in outputs.
- **Write scope.** You and your children write only under `<RUN>/R2/EXT/`.
- **Context discipline.** Read CSVs only through scripts. Children return short summaries.

## Return

At most 15 lines:
- per ledger: row count, top dispositions, and seal and validator status;
- coverage: 221 of 221 units;
- verifier counts;
- reruns and preflight issues;
- the SHA-256 of `EXT_SUMMARY.md` and `VERIFICATION.md`;
- the 3 most consequential findings for R3/R4.
