# R0 calibration report — RUN_D128_CONCORDANCE_2026-09-21_1614Z (D-APP-128)

> **To:** the owner, through HELP_HUMAN (Agent 0).
> **From:** the WORKING_ITEMS R0 calibration manager.
> **Status:** agent judgment and measurement. **This is not a ruling.** No convention
> below is in force until the owner decides at the R0 gate (ruling §5.5). No deliverable
> was edited, and no lifecycle, hold or register state was changed.
>
> **Source state:** `00115c71931bcae79909602d653740d3bb72dfa1`, read from the frozen tree.
> **Companion files:**
> - `VERIFICATION.md` (verifier);
> - `DOUBLE_BLIND_COMPARISON.md` (script `_scripts/double_blind.py`);
> - `STATE.jsonl` (dispatch log);
> - `_verify/` (selection, shard files, aggregated tables);
> - `_scripts/` (census, poll, selection and table scripts).

## §1 Sample and roster

Every child ran as **Opus 5**, requested as `model: "opus"`. Each was a Claude Code
harness-native descendant of this manager (D-GOV-35), with effort inherited from the
session. Agent IDs are in `STATE.jsonl`.

APP-HOLD-1: before dispatch the manager confirmed that all 8 `PREFLIGHT/R0_*.json` files
exist and read `verdict: ALLOW`, with `hold_status: NOT_HELD` for each target.

| Unit | Target | Pass 1 | Pass 2 mechanism | Output |
|---|---|---|---|---|
| S-H | `frontend/src/lib/harness/**` (HARNESS) | fresh TASK | — | `SURFACES/` (60 capabilities, 64/64 files covered) |
| F-01 | DEL-01-01 | fresh TASK | SendMessage resume, same worker | `DEL-01-01/` |
| F-02 | DEL-02-05 | fresh TASK | SendMessage resume, same worker | `DEL-02-05/` |
| F-03A | DEL-03-01 (blind A) | fresh TASK | SendMessage resume, same worker | `DEL-03-01_A/` |
| F-03B | DEL-03-01 (blind B) | fresh TASK | SendMessage resume, same worker | `DEL-03-01_B/` |
| F-04 | DEL-04-05 | fresh TASK | SendMessage resume, same worker | `DEL-04-05/` |
| F-06 | DEL-06-04 | fresh TASK | SendMessage resume, same worker | `DEL-06-04/` |
| F-08 | DEL-08-04 | fresh TASK | SendMessage resume, same worker | `DEL-08-04/` |
| F-09 | DEL-09-07 | fresh TASK | SendMessage resume, same worker | `DEL-09-07/` |
| F-10 | DEL-10-01 | fresh TASK | SendMessage resume, same worker | `DEL-10-01/` |
| V (shards ×9) | one shard per ledger unit; SURFACES class d rides with DEL-09-07 | fresh TASK each | — | `_verify/V-*.csv`, `_verify/V-*_notes.md` |
| V (aggregator) | all shard outputs | fresh TASK | — | `VERIFICATION.md` |

Peak concurrency was 10 children (S-H plus 9 forward workers); the verifier phase ran 9.
The limit was 12.

**Deviations and events, disclosed:**

1. **The verifier was sharded.** The brief specifies one verifier. The deterministic
   selection (`_scripts/select_rechecks.py`) produced 465 items, and class (a) alone
   (all non-ALIGNED, LOW or self-flagged rows) contributed 409 of them. One context cannot
   open that much evidence, so V ran as 9 fresh evidence-only shards plus one fresh
   aggregator. Selection, verdicts and outputs otherwise follow the brief. The shard brief
   is `_verify/SHARD_BRIEF.md`, sha256 `d814bad8…`.
2. **The git clarification came mid-run.** Agent 0 clarified during the run that
   read-only `git -C <frozen> log|show` is permitted for PostReleaseBasis. It reached
   workers only in pass 2, so all 9 forward ledgers set PostReleaseBasis **by assumption**
   in pass 1. Workers revisited it in reverse_notes. The finding is in §3.
3. **Git use outside the rule at the time.**
   - F-10 ran one read-only `git log` during pass 1, when that was still prohibited, and
     disclosed it. No row relies on it.
   - F-01, F-03B and several verifier shards also used read-only `git blame`, which goes
     slightly beyond the "log/show" wording, and disclosed it.
   - No other git operation, install or test run was reported.
4. **The dispatch log has malformed lines.** A shell word-splitting error in the manager's
   own logging wrote 16 lines with a space-joined `unit` field and null hashes. They are
   left in place because the log is append-only. A `MANAGER correction` line, followed by
   correct re-records, supersedes them. No child output was affected.
5. **Completion was detected by polling.** Worker completion notifications were routed to
   Agent 0, not to this manager. On Agent 0's instruction the manager detected returns by
   polling the output files: `#END` present, validator PASS, and the file stable across
   one cycle.

**Seals:** 9 of 9 forward ledgers were hashed before pass 2 and re-hashed after it.
**All 9 are intact. No seal was broken.** No worker needed a validator rerun or a fresh
replacement.

## §2 Per-deliverable census (script: `_scripts/census.py`)

| Unit | Indexed units | Rows | Split units | LOW | Main dispositions | Main causes | HumanDecisionNeeded ≠ NO |
|---|---|---|---|---|---|---|---|
| DEL-01-01 | 26 | 54 | 9 (35%) | 3 | ALIGNED 30, STALE_SPEC 14, NOT_AUDITABLE 6, STALE_VERIF 2, PARTIAL 1, DOC_UNIMPL 1 | DOC_HYGIENE 7, A2 5, CARRIER 3, CODEX 2, OTHER:PENDING_HUMAN_GATE 1 | 7 |
| DEL-02-05 | 32 | 66 | 8 (25%) | 4 | STALE_SPEC 27, ALIGNED 16, NOT_AUDITABLE 10, IMPL_DIFF 9, PARTIAL 3, RSM 1 | A2 13, CODEX 8, PRE_V3 5, CARRIER 4, DOC 4, UNRECORDED 3 | 28 |
| DEL-03-01 A | 28 | 60 | 6 (21%) | 2 | STALE_SPEC 24, ALIGNED 14, PARTIAL 11, NOT_AUDITABLE 7, DOC_UNIMPL 2 | CODEX 12, DOC 10, A2 5, PRE_V3 5, RUNTIME_EXTR 3 | 2 |
| DEL-03-01 B | 28 | 65 | 9 (32%) | 3 | STALE_SPEC 25, ALIGNED 14, PARTIAL 10, NOT_AUDITABLE 8, AUTH_CONFLICT 6 | CODEX 26, DOC 9 | 8 |
| DEL-04-05 | 36 | 63 | 4 (11%) | 4 | STALE_SPEC 24, IMPL_DIFF 14, PARTIAL 9, ALIGNED 5, NOT_AUDITABLE 5, AUTH_CONFLICT 2, UNKNOWN 1 | CODEX 21, DOC 15, A2 7 | 26 |
| DEL-06-04 | 32 | 56 | 4 (12.5%) | 1 | STALE_SPEC 20, IMPL_DIFF 17, ALIGNED 8, PARTIAL 5, NOT_AUDITABLE 5 | CODEX 23, CARRIER 13, DOC 6 | 23 |
| DEL-08-04 | 39 | 80 | 14 (36%) | 4 | STALE_SPEC 29, ALIGNED 27, NOT_AUDITABLE 9, PARTIAL 6, IMPL_DIFF 3, RSM 3, DOC_UNIMPL 2 | CARRIER 10, NATIVE_DELEG 8, PRE_V3 7, CODEX 6, A2 6 | 15 |
| DEL-09-07 | 4 | 31 | 4 (100%) | 4 | ACCEPTED_DIV 24, ALIGNED 4, STALE_SPEC 3 | A2 24, DOC 3 | 3 |
| DEL-10-01 | 32 | 73 | 14 (44%) | 2 | ALIGNED 42, STALE_SPEC 18, NOT_AUDITABLE 10, IMPL_DIFF 3 | CARRIER 8, DOC 8, CODEX 2, UNRECORDED 2 | 3 |

**Totals** cover 579 rows across 9 ledgers; DEL-03-01 is counted twice.

- **Dispositions:**
  - STALE_SPECIFICATION 184;
  - ALIGNED 160;
  - NOT_AUDITABLE 60;
  - IMPLEMENTED_DIFFERENTLY 48;
  - PARTIALLY_IMPLEMENTED 45;
  - ACCEPTED_DIVERGENCE 24;
  - AUTHORITY_CONFLICT 8;
  - REMAINING_STATE_MISMATCH 7;
  - DOCUMENTED_UNIMPLEMENTED 5;
  - STALE_VERIFICATION 3;
  - STALE_ASSESSMENT 3;
  - UNKNOWN 1.
- **Causes:**
  - NONE 220;
  - CODEX_SOLE_ENGINE 100;
  - DOC_HYGIENE 67;
  - A2_TOPOLOGY 60;
  - CARRIER_PROPAGATION 45;
  - PRE_V3_DRIFT 22;
  - NATIVE_DELEGATION 9;
  - UNRECORDED_JUDGMENT 7;
  - RUNTIME_EXTRACTION 6;
  - FACADE_DEPRECATION 5;
  - SHELL_REDESIGN 3;
  - CREDENTIAL_CUSTODY 3.
- **OTHER tokens:** exactly one, `OTHER:PENDING_HUMAN_GATE` (DEL-01-01#CLM-017.3), for a
  normal open human approval gate.
- **Run-local rows:** 46 (29 REGISTER, 17 STATE). Every ledger found at least 2 register
  defects.
- **PostReleaseBasis = YES:** 0 rows in the sealed ledgers. After checking, 1 row should
  be YES (§3).

## §3 Validator and verifier outcomes

- **Structural validator.** All 19 files pass with 0 errors and 0 warnings: 9 ledgers, 9
  reverse files and 1 capability file. Table and SHA-256 values are in
  `VERIFICATION.md` §1.
  - Every worker reached 0 errors before returning, so no structural send-back was needed.
- **Verifier.** 466 checks: the 465 selected items plus 1 extra capability check.

| Verdict | Count | Share |
|---|---:|---:|
| CONFIRMED | 371 | 79.6% |
| REFUTED | 25 | 5.4% |
| CONTESTED | 70 | 15.0% |

- **Disposition-level refutations:** 6 of 442 ledger rows checked, 1.4%. They are:
  - DEL-03-01_B#CLM-009.13;
  - DEL-04-05#CLM-009.14;
  - DEL-08-04#SEC-1.2 and #CLM-016.3;
  - DEL-09-07#STATE-2;
  - DEL-10-01#REM-1.
- **Field-level refutations:** 18, where the Disposition holds but a field does not.
  - 7 are DirectionEvidence.
  - The others are AuthorityTier 2, VerificationEvidence 2, ImplementationEvidence 2,
    CauseTag 2, AssessmentEvidence 1 and PostReleaseBasis 1.
- **Contested Dispositions:** 60, or 13.6%. Most sit on the MR-11 / AUTHORITY_CONFLICT
  boundary (§7) and on "implemented only on a retained path".
- **Per-unit refute-plus-contest rate:**
  - DEL-04-05 lowest (5/61);
  - DEL-06-04 6/55;
  - DEL-10-01 7/43;
  - DEL-03-01_A 11/51;
  - DEL-03-01_B 12/58;
  - DEL-01-01 12/34;
  - DEL-02-05 16/57, all contested, none refuted;
  - DEL-08-04 highest (18/66).
- **The capability file** has one refutation. CAP-HARNESS-058 describes the subagent bridge
  as executable, but at `00115c719` it is disabled.
- **The PostReleaseBasis-by-assumption experiment** (§1 item 2):
  - Checked afterwards with read-only git, 578 of 579 assumed `NO` values were correct.
  - **1 was wrong:** DEL-06-04#CLM-009.10. Its cited line `codex-supervisor.ts:653` blames
    to post-release commit `da95ec194`. The worker and the verifier both caught it.
  - Two workers noted that `da95ec194` shifted line numbers in `session-store.ts`, so line
    citations can drift even when the content predates the commit.
- **Reverse-pass corrections to sealed ledgers.** Pass 2 exposed forward errors in 4
  units, recorded in reverse_notes because the ledgers are sealed:
  - DEL-01-01: CLM-009.2 and CLM-004.1 human-authority rows overstated (verifier:
    CONTESTED).
  - DEL-03-01_A: CLM-019's section-9 link is nominal (verifier: CONFIRMED).
  - DEL-04-05: the D-APP-72 oMLX work has no row, a coverage gap (verifier: CONFIRMED).
  - DEL-06-04: CLM-009.10 PostReleaseBasis (verifier: CONFIRMED).
  - The conventions give these corrections no route into the ledger (§7, reverse-pass
    rule).
- **Verifier consistency caveat.** The two DEL-03-01 shards graded the same HANDOFF
  misgloss differently: one refuted it, the other confirmed it with a note. They also used
  different bases for line anchors. Refuted counts are therefore not strictly comparable
  across units. This is itself calibration evidence for R2: give verifier shards a shared
  grading key.

## §4 Double-blind variance (DEL-03-01; `DOUBLE_BLIND_COMPARISON.md`)

Agreement between workers A and B, on 28 indexed base keys:

| Measure | Exact agreement | Overlap / strict |
|---|---|---|
| Disposition | 23/28 (82%) | overlap 27/28 (96%); on the 19 keys neither split, 18/19 (95%) |
| ALIGNED vs non-ALIGNED | — | **19/19** on unsplit keys |
| ClaimType | 22/28 (79%) | unsplit 16/19 |
| AuthorityTier | 18/28 (64%) | unsplit 16/19 |
| CauseTag | 18/28 (64%) | unsplit 15/19 |
| Split rate | A 17.6% (6 keys), B 25.0% (9 keys) | difference 7.4 pp; B alone split CLM-018, CLM-019 and CLM-022 |
| Reverse Response | 52/60 (87%) | where both claimed a capability, same base key 2/2; B answered PARTIAL on 7 capabilities A called NOT_MINE |

**Where the variance came from.** Row-level histograms show three sources:

1. **AUTHORITY_CONFLICT.** B marked 6 rows for the `codex.*` event-type question
   (K-ENGINE-1/4 against SPEC §11); A marked none, reading them as STALE_SPECIFICATION or
   PARTIALLY_IMPLEMENTED. This is the MR-11 ambiguity.
2. **AuthorityTier.** A used NOT_APPLICABLE on 12 rows and B on 30. B also applied it to
   STATE_ASSERTION and guidance rows, and tiered SPEC restatements as PRD.
3. **CauseTag.** B used CODEX_SOLE_ENGINE on 26 rows and A on 12. A spread the same rows
   over A2_TOPOLOGY, PRE_V3_DRIFT and RUNTIME_EXTRACTION, so causes overlap without a
   precedence rule.

**Reading.** The Disposition core is reproducible: 95% on unsplit keys, and 100% on
whether a key is ALIGNED. The metadata columns are not reproducible without tighter
rules: AuthorityTier and CauseTag both agree only 64% of the time. Both workers
independently found the headline defects: the Codex adapter has never been run through
K-ENGINE-2 conformance, the SoW was not revised under D-APP-127, and the reference hashes
drifted.

## §5 Reverse-pass findings (HARNESS)

- **Capability granularity.**
  - 60 rows cover 64 of 64 files, at the top of the 20–60 target.
  - The verifier checked 10 rows and confirmed 8.
    - Two were contested on granularity. CAP-HARNESS-011 and 021 are close to
      per-function rows.
    - One was refuted on behavior: CAP-HARNESS-058 is described as executable but is
      disabled.
  - S-H tagged **36 of 60 capabilities as legacy in-process code**, reachable only through
    the retained Claude SDK / Pi path and not from any App production route. This is the
    single most useful product fact the reverse pass produced. Forward workers on
    DEL-06-04, DEL-08-04, DEL-10-01 and DEL-04-05 independently cited it as corroboration.
  - PostReleaseBasis is NO on all 60 rows.
- **Response distribution** (per ledger, over 60 capabilities):

  | Ledger | CLAIMED_BY | PARTIAL | NOT_MINE |
  |---|---:|---:|---:|
  | DEL-01-01 | 0 | 2 | 58 |
  | DEL-02-05 | 2 | 7 | 51 |
  | DEL-03-01 A | 1 | 2 | 57 |
  | DEL-03-01 B | 1 | 8 | 51 |
  | DEL-04-05 | 2 | 7 | 51 |
  | DEL-06-04 | 2 | 6 | 52 |
  | DEL-08-04 | 2 | 5 | 53 |
  | DEL-09-07 | 0 | 0 | 60 |
  | DEL-10-01 | 0 | 1 | 59 |

  Total across the 9 ledgers: CLAIMED_BY 10, PARTIAL 38, NOT_MINE 492.
  - The low claim rate is expected, since HARNESS is one area and the sample is 8 of 54
    deliverables. It is not a coverage signal by itself.
  - Several capabilities are claimed by more than one deliverable, all as PARTIAL except
    one CLAIMED_BY each. For example, 027 (key redaction) has three claimants and 031
    (Claude SDK adapter) has three. These overlaps are the ownership seams that R3 should
    resolve.
- **29 of 60 capabilities are claimed by no calibration deliverable:** 001, 003–012,
  018, 020–023, 026, 030, 037, 040, 042, 044, 048, 049, 052, 054, 055, 057 and 060.
  - Most belong to non-sampled owners. Examples: the session, steering and
    server-request clients (001, 003, 004, 006) likely belong to PKG-02/03/05; the
    plan-mode clients (010–012); the workflow-draft clients (020, 021); the PKG-10 sibling
    tools (054, 055).
  - **CAP-HARNESS-057** (coordination notices) was contested. The DEL-08-04 verifier
    reads it as PARTIAL via CLM-014 or CLM-005.1, not NOT_MINE.
  - The 29 are **candidates for R3's unowned-capability sweep, not findings of unowned
    code**. Only a full-corpus reverse pass can make that call.

## §6 Effort, context and a proposed oversize threshold

**Per-unit effort.** Token figures are the harness-reported subagent context at return.
Durations are wall-clock as reported. Pass 2 durations appear to include queue time and
are not comparable.

| Unit | SoW + _STATUS bytes | Indexed units | Rows | Pass-1 tokens | Pass-1 tool uses | Pass-1 time | After pass 2 | Worker's context report |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DEL-01-01 | 35,069 | 26 | 54 | 190k | 53 | 9.1 min | 213k | not tight (~35 files) |
| DEL-02-05 | 53,957 | 32 | 66 | 208k | 57 | 9.9 min | 222k | **moderately tight** (~40 files; 18 KB `_STATUS`) |
| DEL-03-01 A | 38,225 | 28 | 60 | 206k | 59 | 9.6 min | 231k | moderate |
| DEL-03-01 B | 38,225 | 28 | 65 | 221k | 68 | 11.1 min | 243k | comfortable |
| DEL-04-05 | 45,431 | 36 | 63 | 233k | 72 | 12.2 min | 254k | not tight (~45 files) |
| DEL-06-04 | 37,777 | 32 | 56 | 204k | 64 | 9.5 min | 231k | moderate |
| DEL-08-04 | 50,539 | 39 | 80 | 220k | 70 | 10.7 min | 244k | **moderately tight** (502-line SoW plus import tracing) |
| DEL-09-07 | 13,966 | 4 | 31 | n/a (return went to Agent 0) | n/a | n/a | 135k | not tight |
| DEL-10-01 | 34,451 | 32 | 73 | 201k | 58 | 10.1 min | 220k | not tight (~30 files) |

**Verifier shards.** The 9 shards checked 34–66 items each, reached 166k–233k tokens and
took 6–10 minutes. The 58-item DEL-03-01_B shard reported that "about 60 items is near the
ceiling for one context."

**Proposed oversize threshold, justified by these data.** Context pressure tracked
SoW + `_STATUS` bytes and indexed-unit count more closely than row count. Both
"moderately tight" units were above about 50 KB, or had 39 units, and so did the
highest-token pass 2.

- **Pre-gather:** when SoW + `_STATUS` ≥ **48 KB** or indexed units ≥ **38**, the manager
  pre-gathers the evidence pack (§9) before dispatch. Applied to the frozen corpus, this
  flags **13 deliverables**: DEL-01-02, 02-01, 02-02, 02-05, 04-01, 05-04, 06-03, 08-03,
  08-04, 08-05, 09-04, 09-05 and 09-06.
- **Split:** when SoW + `_STATUS` ≥ **55 KB** or indexed units ≥ **50**, the deliverable is
  split across two workers by SoW section range, and the manager merges the two ledgers.
  This flags **4 deliverables**:

  | Deliverable | Units | SoW + `_STATUS` |
  |---|---:|---:|
  | DEL-01-02 | 61 | 54 KB |
  | DEL-02-01 | 42 | 55 KB |
  | DEL-09-04 | 28 | 71 KB |
  | DEL-09-05 | 38 | 61 KB |

- **Verifier shards:** at most **50 items** each.

## §7 Convention verdicts

Evidence abbreviations:
- **V§4.n** is a pattern in `VERIFICATION.md` §4.
- **DB** is `DOUBLE_BLIND_COMPARISON.md`.
- **Fn** is the method-friction section of worker Fn's notes.

### 7.1 MR-1..MR-11

| Rule | Verdict | Evidence |
|---|---|---|
| **MR-1** Assessment recency lives only in AssessmentEvidence (one token) | **REVISE:** "AssessmentEvidence carries exactly one of `OVERTAKEN` · `STILL CURRENT` · `NOT APPLICABLE`, and no other token's phrase anywhere in the cell. `NOT APPLICABLE` only when the INSP-03 assessment reached no conclusion on this claim. A recorded MATCH or PASS that no longer reproduces at the frozen basis is `OVERTAKEN`. `STALE_ASSESSMENT` is reserved for rows where the overtaken conclusion is the operative defect." | 1 REFUTED (DEL-01-01#CLM-009.11). DEL-02-05 applied it inconsistently on REF-006 rows (NOT APPLICABLE on some, OVERTAKEN on CLM-027). F-03A and F-03B both reported the substring trap. |
| **MR-2** MechanicallyUnblocked is `NO` on non-REMAINING rows | **ADOPT** | The validator enforces it; 0 violations across 579 rows. |
| **MR-3**, replaced by frozen-basis gate transcripts (RUN_BASIS) | **ADOPT** (replacement) | Every checked test case exists; for example, 21 were checked in DEL-02-05. The frozen basis makes one transcript sound. See the reachability addition under the ImplementationEvidence rule below. |
| **MR-4** Fold datasheet restatements into REQ rows | **REVISE:** "When the same normative statement recurs across SoW sections, disposition it once on the earliest indexed unit. Each later unit gets a row with the same Disposition and `SEE:<ClaimKey>` in Notes. The census counts SEE rows separately." | F-03A: the SSE names are repeated in 4 units, so identical rows multiply. DEL-09-07 has 27 rows for one ruling. MR-4 is not restated in the candidate conventions, and workers did not apply it. |
| **MR-5** Register defects become REGISTER-n rows | **REVISE:** "REGISTER_DEFECT rows take `REMAINING_STATE_MISMATCH` for metadata lag, or `STALE_SPECIFICATION` when the register asserts a now-false fact. Each `_REFERENCES.md` MATCH hash that does not reproduce at the frozen basis is one REGISTER row per deliverable, and SoW rows restating it cite that key." | 46 run-local rows (29 REGISTER), useful everywhere. The DEL-02-05 verifier found a missed REGISTER row for the stale hash MATCH. DEL-10-01 had no clear disposition for a register defect (F-10 §5.5). |
| **MR-6** Verbatim gates; cross-project status only from App surfaces, else UNKNOWN | **REVISE:** add "For a gate phrased as code landing on the App production path, App code at the frozen basis is an App surface. Runtime lifecycle or gate status still needs an App carrier, else `UNKNOWN`. A gate whose premise a GOVERNING ruling retired is `NO`, with `MOOT:<ruling>` in Notes." | REM-2 on DEL-03-01 was contested in both blinds (A and B chose YES; the verifier found UNKNOWN defensible). F-09 and F-04 raised the "moot gate" case. |
| **MR-7** LatestDecision distinguishes governing from context | **REVISE:** "LatestDecision takes `D-APP-nn` or `D-GOV-nn`, or either with `(context)`, or `NONE_FOUND`." | F-08: the controlling ruling was Root D-GOV-43, but the column admits only D-APP-nn. |
| **MR-8** Flatly false state → STALE_SPECIFICATION; acknowledged gate plus ruling → ACCEPTED_DIVERGENCE | **REVISE:** "(i) Text flatly asserting a now-false state → `STALE_SPECIFICATION`. (ii) Text acknowledging the gate where a GOVERNING ruling permits the difference → `ACCEPTED_DIVERGENCE`. (iii) **New disposition `RETIRED_BY_RULING`:** a GOVERNING ruling names the deliverable or item retired and preserves its text as history. It applies to every file in the preserved set, and one whole-section row per ruling is allowed. Text outside the preserved set stays under MR-11. (iv) A claim true only of a recorded snapshot (for example 'REF-006 MATCH at v23') is a REGISTER row (MR-5), not STALE_SPECIFICATION." | V§4.5. On DEL-09-07, 21 of 24 ACCEPTED_DIVERGENCE rows hold, but the same preserved folder was split across dispositions (STATE-2 refuted). The DEL-09-07 shard judged RETIRED_BY_RULING a real improvement. REF-006 claims were spread over three dispositions (DEL-01-01, DEL-02-05). |
| **MR-9** Pre-SoW assessments cite the old REQ-ID | **ADOPT** | Used correctly (F-10 §5.4). Optional improvement: R1 adds an old-ID → new-ID mapping column to the claim index. |
| **MR-10** Verification tokens for non-behavioural claims | **REVISE:** add `HASH-RECOMPUTE@<sha>` (a recomputed file hash) and `REACHABILITY(static)@<sha>` (entry point → module import chain) to the vocabulary. | F-06 §5.5 and F-10 §5.2. The DEL-01-01 verifier refuted one misattributed `DOC-BASIS` token (CLM-009.4). |
| **MR-11 (generalized)** A ruling stands over untranscribed wording | **REVISE:** "Apply MR-11 only when the ruling **explicitly** addresses the clause or the deliverable. Where DIRECTIVE §0's authority order resolves a disagreement among GOVERNING sources, apply it, cite both sources and do not use AUTHORITY_CONFLICT. Where a ruling undercuts an unamended GOVERNING clause without naming it, or two GOVERNING texts conflict and the authority order does not resolve it, the row is `AUTHORITY_CONFLICT` with `HumanDecisionNeeded = R4`. It is never resolved by the worker." | V§4.1: about 30 items across 6 units, the largest source of contested Dispositions. DB: the 6-row AUTHORITY_CONFLICT split between the blinds. F-01, F-03B, F-04 and F-06 each proposed a variant. |

### 7.2 [EXT] and other candidate rules

| Rule | Verdict | Evidence |
|---|---|---|
| 25-column ledger schema, `#END`, repo-relative paths | **ADOPT** | 19 of 19 files pass; no absolute paths appear anywhere in R0 outputs. |
| ClaimType `CONTEXT_CLAIM` [EXT] | **REVISE:** "`CONTEXT_CLAIM` rows that make a checkable, now-false factual assertion may take `STALE_SPECIFICATION`. Otherwise use `NOT_AUDITABLE`, with the reason in Notes." | F-03A and F-03B both asked. The verifier found CLM-023/025 against CLM-010/024 inconsistent (DEL-03-01_A). |
| ClaimType `STATE_ASSERTION` [EXT] | **ADOPT** | 91 rows. Useful for Remaining prose and carrier notes. |
| AuthorityTier [EXT] | **REVISE:** "Use `GOVERNANCE_INVARIANT` when the claim restates App or Root DIRECTIVE, CONTRACT, SPEC or TYPES, or a D-GOV rule. Use `PRD` only when the highest source restated is `PRD.md`. Use `LOCAL_DESIGN` for a decomposition, SCA or deliverable-level choice. Use `NOT_APPLICABLE` for `CONTEXT_CLAIM`, and for `STATE_ASSERTION` or `REGISTER_DEFECT` rows that restate no normative source. The validator errors on `CONTEXT_CLAIM` with any other tier." | DB: 64% agreement, the worst column. V§4.6: SPEC restatements tiered PRD in 4 units; LOCAL_DESIGN on CONTEXT_CLAIM rows (2 REFUTED). |
| `MechanicallyUnblocked` rename [EXT] | **ADOPT** | No friction beyond the MR-6 items. |
| DirectionEvidence [EXT], CONTEXT-only | **REVISE:** "DirectionEvidence cites the explaining record with a class prefix: `CTX:<path §>` for a CONTEXT source, or `GOV:<ruling>` when a GOVERNING ruling itself explains the divergence. Before writing `NONE_FOUND`, the worker must search `_DECISIONS/_REGISTER.md` and the CONTEXT sources, and name the search in Notes. CONTEXT still never changes a Disposition." | V§4.2 and V§4.3: 7 DirectionEvidence refutations; 12+ rows put GOVERNING citations in a CONTEXT-only column. Both DEL-10-01 refutations came from not grepping the register (D-APP-73/76/89; DEC-019). F-01, F-02, F-06 and F-08 all raised it. |
| PostReleaseBasis [EXT] | **REVISE:** "The manager supplies, in each brief, the paths touched by `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a`. For a cited file on that list, the worker runs read-only `git -C <frozen> blame -L` on the relied-on lines, and sets `YES` if any line blames to one of the four commits. Otherwise `NO`. Line citations inside touched files are taken at the frozen basis." | The assumption experiment gave 578 of 579 correct and 1 wrong (DEL-06-04#CLM-009.10), caught only by line-level blame. `da95ec194` shifted cited line numbers. The value lies in the check being cheap with a supplied path list, not in the default. |
| CauseTag vocabulary [EXT] | **REVISE:** "CauseTag names the mechanism. A divergence that predates 2026-08-22 is `PRE_V3_DRIFT` unless a named v3 mechanism applies. `UNRECORDED_JUDGMENT` is used only when no vocabulary mechanism fits **and** neither the decision register nor CONTEXT records the direction. With mixed causes, put the primary in CauseTag and the secondary as `CAUSE2:<tag>` in Notes. Add `LIFECYCLE_GATE_PENDING` for a normal open human gate." | DB: 64% agreement; causes overlap without precedence. V§4.3: UNRECORDED_JUDGMENT was declared without a register search. The only OTHER token was a pending human gate. Mixed-cause rows: F-03B and the DEL-08-04 verifier. |
| NOT_AUDITABLE [EXT] | **ADOPT** | 60 rows. The remaining contests are covered by the MR-8(iv) and CONTEXT_CLAIM revisions. |
| ImplementationEvidence: reachability (new, from R0) | **REVISE** (add): "For every row whose evidence is code, append `REACH=LIVE`, `REACH=LEGACY_ONLY` or `REACH=TEST_ONLY` to ImplementationEvidence, determined statically from a product entry point. A requirement met only on a `LEGACY_ONLY` path is judged on the live path: `PARTIALLY_IMPLEMENTED` if the live path covers part of it, `IMPLEMENTED_DIFFERENTLY` if the live path uses another mechanism, `DOCUMENTED_UNIMPLEMENTED` if the live path lacks it. A claim about the retained module itself is judged at module level and carries the REACH tag." | V§4.4: the same fact was recorded as IMPLEMENTED_DIFFERENTLY, PARTIAL or ALIGNED inside one ledger (DEL-06-04, 04-05, 08-04, 10-01). S-H found 36 of 60 capabilities legacy-only. Five workers asked for this independently. |
| ClaimKey splitting and run-local keys | **REVISE:** "Split only when a unit holds separately numbered REQ-, AC- or VER- items, or a table of independently dispositionable rows. R1 should emit REQ, AC and VER bullets as index units. Run-local REGISTER and STATE numbering stays per deliverable." | Split rates ranged from 11% to 44%, and 100% on DEL-09-07. DB: 7.4 pp difference between blinds, and B alone split 3 keys. F-02 and F-08 had to split just to reach REQ/AC/VER bullets. |
| Reverse pass [EXT] (two sealed passes) | **REVISE:** keep the sealing and add "Forward-row corrections found in pass 2 are written to `<DEL-ID>_errata.csv` (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, ending `#END`). The verifier rechecks every errata row, and the census reports sealed and errata-applied figures side by side." | Seals held 9 of 9. Pass 2 exposed forward errors in 4 units, but they are stranded in prose reverse_notes (V§4.9). Resuming the same worker kept claim context and was fast (pass 2 added about 13–30k tokens). |
| Capability file [EXT] (granularity, no owner column) | **REVISE:** add "Each capability states its live/legacy/test-only reach and its enabled or disabled state at the frozen basis, verified from code, not inferred from names. Per-function rows fold into their behaviour." | 8 of 10 checked rows confirmed. CAP-HARNESS-058 was refuted (disabled bridge described as executable); 011 and 021 were contested on granularity. The LEGACY tagging was the pass's most useful output. |
| Double-blind check | **ADOPT** for R2, on 1 deliverable per wave | Cheap and informative. It found the AuthorityTier and CauseTag unreliability that single workers cannot reveal. |
| Validator (§6) | **REVISE:** "The validator parses CSV records rather than lines, so quoted newlines are safe. It adds errors for the AuthorityTier/CONTEXT_CLAIM rule and for DirectionEvidence without a `CTX:` or `GOV:` prefix on non-ALIGNED rows, and it validates `_errata.csv`." | No false passes were observed, but every worker had to avoid in-field newlines. Two of the most common verifier findings are mechanical and can be checked. |
| `OTHER:<TOKEN>` escape hatch | **ADOPT** | Used once, and correctly. |

## §8 Findings requiring owner attention (no action taken)

These are agent observations with evidence in the ledgers and `VERIFICATION.md`. Each
needs an owner decision or framing; none has been acted on.

1. **Legacy in-process harness versus the live Codex path (cluster; R4 rows: DEL-04-05 24, DEL-06-04 23, DEL-08-04 14).**
   - **What the code does:** the App's own write/edit path gate (DEL-06-04), managed
     delegation bridge (DEL-08-04), domain tools (DEL-10-01) and Anthropic provider path
     (DEL-04-05) exist and are tested. They are reachable only through the retained Claude
     SDK path.
   - **What bounds the live path:** only the user's Codex sandbox and approval choice.
   - **Why a ruling is needed:** CONTRACT K-PATH-2/3, K-ROOT-2, K-HOOK-1 and SPEC §15.2
     were not amended for D-GOV-43.
   - **The question:** is the retained harness code history, compatibility or obligation?
2. **The Codex engine was never run through the K-ENGINE-2 conformance suite.** It is the
   production default, and the suite passes only against the scripted Claude SDK and Pi
   adapters.
   - Both blind workers found this independently. It is tracked as V3-01.
   - The HANDOFF citation that seemed to explain the gap was refuted: it describes a
     different check.
3. **`codex.*` canonical event types (DEL-03-01).** CONTRACT K-ENGINE-1/4 appears to
   conflict with SPEC §11 and K-EVENT-6. Worker B marked AUTHORITY_CONFLICT, worker A did
   not, and the verifier marked it CONTESTED. This needs framing as a ruling question.
4. **Human-authority check on the legacy `status_transition` MCP tool (DEL-01-01).**
   - The agent supplies the actor string. `HUMAN`, `USER` and `OPERATOR` count as human,
     and `approvalSha` is checked for format only. A test exercises exactly this path.
   - The tool is off by default and sits on the legacy path; the verifier marked it
     CONTESTED.
   - It is flagged because it bears on K-HUMAN-style invariants.
5. **App CONTRACT K-SUBAGENT-1 still says "0→1 or 1→2"** (DEL-08-04). The code and root
   `AGENTS.md` admit Agent 0 → TASK, following the 2026-08-16 repair, and no D-APP ruling
   was found for that repair. There are 6 contested rows.
6. **D-APP-127 and D-GOV-43 were applied to `_STATUS.md` but not transcribed into SoW,
   `_CONTEXT.md` or `Dependencies.csv`** (DEL-02-05, 03-01, 04-05, 08-04: the
   CARRIER_PROPAGATION cluster).
   - DEL-04-05-V3-02 is still gated on the retired consent contract.
   - DEL-02-05's REM-1 depends on it.
7. **`_REFERENCES.md` MATCH hashes for CONTRACT, SPEC and PRD are stale in every sampled
   deliverable** (the DOC_HYGIENE cluster). The 2026-09-19 work graph defers this drift;
   the owner may want one corpus-wide repair rather than 54 local ones.
8. **The audit-log location disagrees across GOVERNING texts** (DEL-01-01). CONTRACT
   K-EVENT-4 and the code use the Runtime-owned store, while SPEC §8.2 and PRD FR-121 still
   name the project-local `events.jsonl`.
9. **The Anthropic API-key rows may not need R4** (DEL-02-05). The verifier notes that
   the `PRD.md:15` and `CONTRACT.md:15` preambles already mark Anthropic text as
   compatibility history. This could turn up to 12 of DEL-02-05's R4 rows into STALE_SPECIFICATION, with a similar effect on DEL-04-05 (24 R4 rows).
10. **Smaller items:**
    - The D-APP-72 oMLX work delivered under DEL-04-05 is undocumented in its SoW.
    - The per-chat delegation policy (SOW-083) is unimplemented (DEL-08-04 V3-02).
    - The carrier for DEL-09-07 reads `OPEN` while the tranche return says RETIRED.
    - `section9.runtime_engine_contract` links only nominally, to a legacy file.

**Early cause clusters** (579 rows): CODEX_SOLE_ENGINE 100, DOC_HYGIENE 67, A2_TOPOLOGY 60
and CARRIER_PROPAGATION 45. Together they are 272 of the 359 non-NONE causes (76%). The
pattern is consistent: the v3 re-platform landed in code and in `_STATUS`, but not in the
deliverables' normative text or registers.

## §9 Proposed R2 plan adjustment

- **Evidence pack, built once per wave by the manager and put into every brief:**
  - the post-release touched-path list;
  - the static reachability map, taken from the HARNESS capability file plus App entry
    points (`app/api/**`, `electron/main.ts`);
  - hash recomputes of CONTRACT, SPEC and PRD against each `_REFERENCES.md`;
  - a per-deliverable decision-register grep (D-APP and D-GOV hits);
  - the D-APP-127 application map, showing which carriers were and were not revised.
  This removes the most common verifier findings (§7: DirectionEvidence, PostReleaseBasis,
  REFERENCES hashes) and cuts about 20–40k tokens of repeated discovery per worker.
- **Worker sizing:**
  - one deliverable per worker;
  - pre-gather for the 13 flagged deliverables;
  - split the 4 oversize deliverables (§6);
  - retired deliverables such as DEL-09-07 get a light worker using RETIRED_BY_RULING,
    if adopted.
- **Manager span:**
  - at most 10 forward workers per manager, which this manager handled comfortably;
  - verifier shards of at most 50 items each;
  - one shared grading key across shards;
  - at scale, change class (a) to: all LOW, self-flagged, AUTHORITY_CONFLICT, UNKNOWN,
    REMAINING-type and errata rows, plus 30% of other non-ALIGNED rows. Otherwise, at the
    R0 ratio of 0.8 items per row, 54 deliverables would give about 2,500 items.
- **Wave order.** Cluster by shared evidence so each wave reuses its pack:
  1. **Legacy-harness cluster** (PKG-04, 06, 08, 10), which reuses the HARNESS reverse
     pass;
  2. **engine, runtime and session** (PKG-03, 05);
  3. **shell and UI** (PKG-02, 07), with a new reverse-pass area for
     `frontend/src/components/**` and `lib/runtime-client/**`;
  4. **governance and docs** (PKG-00, 01);
  5. **release and installer** (PKG-09), which carries the retired-deliverable handling.
  - Run one double-blind deliverable per wave.
  - Add reverse-pass areas for `frontend/electron/**` and `projects/chirality-runtime/packages/**`
    before PKG-09 and PKG-03.
- **Before R2:**
  - owner verdicts on §7, especially MR-11, AuthorityTier, reachability, errata and
    RETIRED_BY_RULING;
  - framing of findings 1, 3 and 5 as ruling questions, so that R2 rows can cite them
    instead of multiplying R4.
