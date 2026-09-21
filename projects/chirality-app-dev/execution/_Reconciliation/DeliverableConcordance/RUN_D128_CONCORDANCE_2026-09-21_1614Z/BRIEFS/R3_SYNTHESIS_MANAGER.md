# Brief — R3 cross-package synthesis manager (WORKING_ITEMS, Type 1)

**Role.**
- You are WORKING_ITEMS and own R3 (cross-package synthesis) for this run.
- You dispatch TASK workers (Type 2, no delegation) and integrate their returns.
- You never edit deliverables, governing documents, code or any R2 output. You never commit.
  You return to HELP_HUMAN.

**Run.** `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; D-APP-129). Method: kernel
`docs/DELIVERABLE_CONCORDANCE_METHOD.md` and `workflows/reconciliation/resources/method.md` §R3
("Do not change dependencies or deliverables during synthesis").

**Placeholders**, supplied at dispatch: `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.

**Read first:**
- `<RUN>/CONVENTIONS.md` in full.
- `<RUN>/RUN_BASIS.md` in full. **Addenda 3–11 are binding on R3.** Several of them direct R3 to
  apply a rule to ledgers sealed before the rule existed.
- `<APP_WORK>/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`
  (owner words; read-only).
- Every `<RUN>/R2/*/PACKAGE_SUMMARY.md` and `VERIFICATION.md`, `<RUN>/R2/EXT/EXT_SUMMARY.md` and
  `R3_OBSERVATIONS.md`, and each package's `STATE.jsonl` to identify ledgers of record.
- `<RUN>/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` (CONTEXT; Q-01..Q-13).

## Inputs and precedence

- **Ledgers of record.** One per deliverable (54) plus the 13 EXT ledgers. Identify each by
  script from the package's STATE.jsonl and PACKAGE_SUMMARY; do not guess from folder names.
  - Superseded attempts, double-blind B ledgers and split-half inputs are **evidence only**.
  - Exception: DEL-06-02 CLM-005 and CLM-032 carry **both** A and B verdicts, as owner-deferred
    items (Addendum 5).
  - DEL-04-05 is identified by its re-sealed SHA (Addendum 11).
  - R0 calibration ledgers are not inputs.
- **Row value precedence.** Build it by script, in this order:
  1. sealed ledger;
  2. that deliverable's `_errata.csv`, unless a `CORRECTIONS.csv` row rejects the erratum (for
     example DEL-09-03), in which case keep the sealed value;
  3. `CORRECTIONS.csv`;
  4. R3 re-mappings (below).

  Every change from the sealed value is written to `R3/REMAP_LOG.csv`:
  `ClaimKey,Field,SealedValue,NewValue,Source,RuleOrEvidence`.
  - `Source` ∈ `ERRATA`, `CORRECTION`, `R3_RULE`, `R3_RUNWIDE`.
  - Nothing is changed silently. Contested rows stay visible, with both readings.

## Undertaking

1. **Merge (script).**
   - `R3/CLAIM_CONCORDANCE.csv`: all deliverable ledgers of record with precedence applied.
   - `R3/EXTENSION_CONCORDANCE.csv`: the EXT ledgers.
   - `R3/REVERSE_CONCORDANCE.csv`: every reverse response, by capability.
   - Keys are unique. Every source SHA is recorded in `R3/INPUT_MANIFEST.md`.
2. **Rule re-mappings on sealed rows (script first; a TASK only where a script cannot decide).**
   Log each in REMAP_LOG, citing its addendum.
   - **Addendum 6 rule 3 with Addendum 8:** re-derive `R4-Q1` in HumanDecisionNeeded from the
     REACH tags. A row cites R4-Q1 when LEGACY_ONLY code is the only non-test code meeting it.
   - **Addenda 4, 7 and 9:** move plain `R4` rows to `R4-Q4`, `R4-Q5` or `R4-Q6` where the row
     turns on that question. Classify by a TASK with the question texts; the evidence is the row
     itself. Rows it cannot place stay `R4`.
   - **Addendum 5:** apply the STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break.
   - **Addendum 10:** find every row whose conclusion that an off-code event did not happen rests
     only on an absent record. Re-map it to `UNKNOWN` with `OWNER_CHECK: <question>`. Use a script
     candidate list: `NONE_FOUND` on process or event claims; "never ran / not performed / no
     record / not notarized / not signed" phrasing; the managers' OWNER_CHECK candidate lists
     (PKG-09 §8 has 30); and the EXT release-doc rows. A TASK confirms each candidate.
3. **Run-wide consistency calls** (`R3/RUNWIDE_CALLS.md`). One section per call: the evidence,
   the call, and the affected rows re-mapped under `R3_RUNWIDE`. Decide from code and records in
   the evidence roots only.
   - (a) **Reach of the domain contract modules:** the pack says LIVE, the RTCONTRACT capability
     file says TEST_ONLY.
   - (b) **Reach of build and validation scripts.** The PKG-09 briefs described it two ways.
   - (c) **SoW-conversion parity items** (AC-001/VER-001; D-APP-68 / D-GOV-16). These were
     disposed three ways across the corpus.
   - (d) **The D-GOV-43 policy rows:** shared config, approval policy, event pass-through, and
     "Full access". They are split between AUTHORITY_CONFLICT and IMPLEMENTED_DIFFERENTLY.
     Normalise them under R4-Q6, as rules conflicts pending the owner's confirmation.
     - The owner's recorded answer (Addendum 9) is not GOVERNING until R4, so do not re-disposition
       on the strength of it.
   - (e) **DEL-02-01 half A/B splits** on the matrix and loop-first rows, including the unsampled
     CLM-020.x and CLM-025. Re-examine them with a fresh TASK. Keep the disagreement visible.
   - (f) **DEL-09-04/09-05 release-signing split** (STALE_SPECIFICATION vs AUTHORITY_CONFLICT;
     K-RELEASE-1, D-APP-97 F-APP-2, G6a). Frame this as one cluster rather than resolving it.
   - (g) **RUN_BASIS §5 flags** that EXT found stale (D-APP-104, 107, 122, 123 landed). Record the
     correction as a finding. RUN_BASIS itself is HELP_HUMAN's.
4. **Coverage QA** (`R3/COVERAGE_AND_QA.md`). Deterministic, and each check gives PASS or FAIL
   with counts:
   - 1,746 of 1,746 CLAIM_INDEX units dispositioned;
   - 221 of 221 EXTENSION_INDEX units dispositioned;
   - every capability row in `R2/SURFACES/` either claimed (CLAIMED_BY or PARTIAL by at least one
     deliverable) or listed in `R3/UNMAPPED_IMPLEMENTATION.csv`, with its reach and enabled state;
   - package summaries reproduce from the ledgers;
   - no duplicate keys;
   - the REMAP_LOG reconciles the sealed census to the final census.

   Also compile every coverage gap the managers reported (work items or SoW scope with no forward
   row, and records with no index unit such as PKG-00's control records) into
   `R3/COVERAGE_GAPS.csv`.
5. **Cross-package findings** (`R3/CROSS_PACKAGE_FINDINGS.csv`). Cover duplicate or incompatible
   ownership, shared surfaces, inconsistent decisions or terminology, RULED-but-not-applied
   decisions (D-APP-127 carriers; D-APP-99/101/121/125.1), stale verification, lifecycle and
   Remaining-state defects, and register defects (for example the reference hashes, and D-APP-112
   item B's unregistered basis).
6. **Clusters** (`R3/CLUSTERS.md` plus `R3/CLUSTER_INDEX.csv`: `ClusterID,ClaimKey,Role`).
   - Group rows by CauseTag, then by HumanDecisionNeeded, into candidate R4 packets. Aim for about
     15–25 clusters plus an exceptions list.
   - Each cluster states its question, its full affected-row population by key, the packages
     involved, and its AuthorityTier mix.
   - The named questions R4-Q1..Q6 each head a cluster. R4-Q6 carries the owner's recorded answer
     as context, labelled not yet GOVERNING.
   - Separate clusters for: the owner-deferred DEL-06-02 keys; the done-declaration questions
     Q-01..Q-13 (CONTEXT); and the live-path findings that recur across packages. These are
     unredacted event storage (K-EVENT-6), unenforced protected paths (K-DOMAIN-2) with PKG-06's
     path and hook rows, the human gate and status transition (R4-Q3), scaffolding returning 501,
     and the legacy-session migration.
   - **Do not write options or recommendations.** R4 packets are drafted after the owner check.
7. **Owner check** (`R3/OWNER_CHECK.md`). One questionnaire for the owner, grouped by event
   (release, signing, notarization per version, publication, CI and release jobs, attestations,
   manual steps).
   - Each question is one line the owner can answer yes / no / don't know. It lists the row keys it
     decides and the evidence found, if any.
   - Include the owner-reported fact that v3.0.1 was notarized, as a statement to confirm (not
     applied).
   - Keep the list as short as correct grouping allows.
8. **Independent spot check** (`R3/R3_SPOT_CHECK.md`). A fresh TASK, blind to REMAP_LOG
   rationale, rechecks a stratified sample of the final concordance against the frozen tree:
   - about 5% of rows, stratified by package and Disposition;
   - every AUTHORITY_CONFLICT and UNKNOWN row it can reach within the budget, and at least 20;
   - 30 REMAP_LOG entries.

   Report CONFIRMED, REFUTED or UNVERIFIABLE with evidence. A REFUTED re-mapping is reverted in a
   second REMAP_LOG pass and logged.
9. **Summary** (`R3/R3_SUMMARY.md`, script-built census plus a short hand-written section):
   - the final Disposition census against the sealed census;
   - HumanDecisionNeeded by token;
   - the cluster list;
   - the owner-check question count;
   - open contested items;
   - anything R3 could not resolve.

## Rules

- **Concurrency.** At most **4** of your children alive at once. Every spawn uses
  `model: "opus"`.
- **Notifications.** Child completion notifications go to HELP_HUMAN; drive the work from files.
  Poll with a Bash `until` loop (sleep 30–60 s). Do not end your turn until the undertaking is
  complete.
- **Scripts.** Scripts live in `<RUN>/R3/_scripts/`. Every CSV is UTF-8, has a header and ends with
  `#END`. Read CSVs only through scripts.
- **Evidence roots, for every child:**
  - Read only `<FROZEN_TREE>/projects/chirality-app-dev/**`,
    `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, the run folder, and Root
    governance documents only where CONVENTIONS allows.
  - Not Root `execution/`, and not `projects/chirality-runtime/execution/**`.
  - Git: read-only `log`, `show`, `blame` against `<FROZEN_TREE>` only.
  - No installs, and no test runs.
- **Paths.** No absolute paths in outputs.
- **Write scope.** You and your children write only under `<RUN>/R3/`. Keep
  `<RUN>/R3/STATE.jsonl`, one line per dispatch or return; you are its only writer.

## Return

At most 15 lines:
- coverage QA verdicts;
- the sealed-to-final census deltas by Source;
- the cluster count and top clusters by row population;
- the owner-check question count;
- the spot-check result;
- unresolved items;
- the SHA-256 of `CLAIM_CONCORDANCE.csv`, `CLUSTERS.md`, `OWNER_CHECK.md` and `R3_SUMMARY.md`.
