# R0 Calibration Notes — DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

- **RunID:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`
- **Deliverable:** DEL-03-04 (PKG-03 Runtime Engine Contract and Turn Lifecycle)
- **Source state under review:** `main` = `4c8ed8907` (all evidence citations bind to this SHA unless a row says otherwise)
- **Agent role:** TASK (bounded R0 method-calibration executor, one deliverable subscope)
- **Date:** 2026-07-11
- **Epistemic status:** immutable, source-state-bound evidence artifact of this run. Not authority, not a queue, not a work-selection surface; no disposition here is a human ruling.

## 1. Claim census

Companion ledger: `DEL-03-04_claims.csv` — 28 claim rows.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 15 (REQ-001..REQ-014 incl. REQ-006A) |
| ACCEPTANCE | 6 (Datasheet Conditions rows) |
| EXCLUSION | 4 (Specification Out-of-scope bullets) |
| REMAINING_WORK | 1 (concordance bootstrap item) |
| IMPLEMENTED_UNMAPPED | 2 |

By Disposition:

| Disposition | Count |
|---|---:|
| ALIGNED | 24 |
| PARTIALLY_IMPLEMENTED | 1 (REQ-006: stub-adapter terminal outcomes UI-only, not persisted) |
| STALE_SPECIFICATION | 1 (REQ-014: "exact hook or state API remains TBD" setup wording outlived by the implemented, tested observability basis) |
| IMPLEMENTED_UNDOCUMENTED | 2 (interrupt-time permission-broker clearing; additive HarnessEvent categories beyond SPEC §9.3/9.4 / TYPES §7.3 enumerations) |

Assessment recency (INSP-03, 2026-06-20 at reviewed SHA `0e1ba9a1e`), classified per claim in the `AssessmentEvidence` column per plan §10:
- **Current conclusions:** REQ-001, 002, 003, 009, 011, 012 (strengthened since), 013, plus the ACC facets they cover.
- **Stale (overtaken by the ORN-09 close, commit `24f40d5d8`, 2026-07-10):** REQ-004 and REQ-005 PARTIALs (INSP Gaps 1 and 2) — disconnect `turn.cancelled` persistence and pre-execution `message.accepted` recovery both landed with named tests (`routes.test.ts:1185`).
- **Stale evidence pointers, current conclusions:** REQ-007, 008, 010 — INSP cites `frontend/src/lib/harness/event-schema.ts` and old `types.ts` lines; the schema moved to `frontend/packages/harness-contract/src/event-schema.ts` (D-APP-48), and several cited line ranges drifted.
- **Split-currency:** REQ-006 (SDK/Anthropic facets superseded-stronger; stub-path Gap 3 still current) and REQ-014 (residual acknowledged, but the spec-side TBD is now the only remaining part).
- **Not covered:** REQ-006A (added by ADQ-05 on 2026-06-21, after the assessment) and both UNMAPPED rows.

Verification-evidence binding used for behavioral ALIGNED rows: named Vitest tests read directly at `4c8ed8907`, execution bound via loop Receipt 4 (full frontend Vitest 667 passed / 4 skipped + typecheck at `main` = `61d70bdb0`, 2026-07-10) plus `git diff 61d70bdb0..4c8ed8907 -- frontend/` being empty — the tested tree is byte-identical to this run's source state. Dependency baseline re-verified live: `Dependencies.csv` matches the D53A coverage row (DEL-03-04, 10 rows, parent anchor OK); `_REFERENCES.md` hashes for PRD/SPEC/CONTRACT/TYPES re-computed and MATCH at `4c8ed8907`.

## 2. R0 calibration self-report (plan §8/R0 criteria)

**(a) Authority precedence.** The AUTHORITY_MAP sufficed for every row; no `AUTHORITY_CONFLICT` was needed. The two spots where precedence took real work: (1) PRD FR-022's acceptance wording ("Success, failure, and cancellation each produce a terminal runtime event") enumerates three outcomes while CONTRACT K-EVENT-3, SPEC §9.3, TYPES §7.3, and D-APP-40 include interruption — I read FR-022 as a non-exclusive subset interpreted by the ruled D-APP-40 rather than a live conflict, since nothing in FR-022 forbids the fourth outcome; had FR-022 said "only", this would have been AUTHORITY_CONFLICT. (2) The INSP-03 assessment's classification as evidence-not-truth (plan §1, AUTHORITY_MAP provenance class) resolved cleanly once ORN-09's later evidence was found via deliverable MEMORY.md — the MEMORY.md pointer chain was essential; an agent that read only the assessment would have re-reported two closed gaps.

**(b) Evidence granularity.** File-level was NOT enough for this behavioral claim class; line ranges were necessary and cheap. Three reasons: (1) the same file (`turn-engine.ts`) carries claims for three deliverables (lock design DEL-03-02, disconnect terminalization DEL-03-04, event writer consumption DEL-05-02) — only line ranges keep the claim boundaries honest; (2) INSP-03's line citations had drifted in five files, which is itself a finding worth capturing and only visible at line granularity; (3) taxonomy claims (REQ-006A) turn on which branch emits which event type — file-level evidence cannot distinguish `turn.cancelled` from `turn.interrupted` paths. Test evidence needs test *names* plus line anchors; names survive drift better than line numbers.

**(c) False-positive risk.** Rows I am least confident in: (1) **UNMAPPED-1** (MEDIUM) — I checked the three plausible PKG-06 owner specs for interrupt-time permission clearing, not all 53 kits; a mapping may exist elsewhere, which would flip it from IMPLEMENTED_UNDOCUMENTED to someone else's ALIGNED. (2) **REQ-014 as STALE_SPECIFICATION** (MEDIUM) — an alternative reading is that the TBD is a live residual (PARTIALLY_IMPLEMENTED docs-side); I chose STALE_SPECIFICATION because the behavior and tests exist and only setup wording lags, but this is exactly the kind of judgment R0 should surface for the reviewer. (3) **EXC-002/EXC-004** (MEDIUM) — exclusion "alignment" was judged from this deliverable's side only; whether DEL-03-02/DEL-05-02 actually claim their side of the shared files is an R3 cross-package question I could not settle in-subscope. (4) The Receipt-4 suite binding is indirect (recorded pass + byte-identity proof) — I could not execute the suite because this worktree's `node_modules` is uninstalled and `npm install` would exceed my write scope; if the reviewer wants direct execution binding, that is an environment-provisioning question for R2 dispatch (see §3).

**(d) Scope vs current behavior.** Hardest to keep apart on three surfaces: the additive event vocabulary (`message.accepted`, `interruption.requested/completed` — current behavior, permitted by SPEC §9.2 evolution, but not enumerated scope; kept out of ALIGNED reasoning and isolated in UNMAPPED-2); the stub adapter (current behavior in a test-only provider mode — I still held it against REQ-006's letter because the event log *is* available in stub mode, rather than silently narrowing scope to "real providers"); and the permission-broker clearing (behavior that makes the interrupt requirement *work* in practice but is nobody's stated scope). The controlled-disposition list made this discipline workable.

**(e) Usefulness of RemainingWork statements.** The three non-trivial ones are executable as `## Remaining` items nearly verbatim: REQ-006's names a bounded choice with its smallest check already performed; REQ-014's names the exact files, the replacement wording basis, and the R5 vehicle; UNMAPPED-2's names the diff already computed and the two routing options (D-APP-38 corpus flow vs DEL-05-02 ownership). UNMAPPED-1's is R3-shaped rather than deliverable-shaped — it would not belong in DEL-03-04's `## Remaining` and that is correct behavior per plan §3 boundary 9 (findings never select work).

## 3. Method friction and proposed run-local method revisions

1. **ALIGNED-now vs assessment-stale cannot both be expressed in the single-valued `Disposition` (plan §6/§7).** REQ-004/REQ-005 are ALIGNED at `4c8ed8907` while their INSP-03 conclusions are overtaken. Choosing `STALE_ASSESSMENT` would hide the live alignment; choosing `ALIGNED` risks hiding the stale assessment. **Proposed run-local rule:** `Disposition` records live concordance; assessment recency is carried exclusively in `AssessmentEvidence` (which plan §10 already requires to classify current/stale/non-applicable); reserve `STALE_ASSESSMENT` as a Disposition for rows where the overtaken assessment is the *only* defect (live surfaces agree and some surface still presents the stale conclusion as current truth). I applied this rule in the CSV; R2 agents need it stated once, centrally.
2. **`SelectableUnderCurrentLoop` is only meaningful for REMAINING_WORK rows (plan §6).** For the other 27 rows there is no recorded work to select, so the column degenerates to a constant NO. **Proposed revision:** define the column as "derived for REMAINING_WORK rows; NO-by-definition otherwise" so R2 agents do not burn effort deriving a constant, and so a YES on a non-REMAINING row is machine-detectable as an error.
3. **Verification binding needs a named indirect-binding form (plan §6 `VerificationEvidence`).** Executing the suite per-agent is not always possible (uninstalled worktree; and 50+ agents each running the full suite is wasteful). The binding I used — newest recorded full-suite pass at SHA X + `git diff X..<source state> -- frontend/` empty — is sound and cheap. **Proposed revision:** bless this "recorded-pass + byte-identity" form explicitly in the run-local method, require both elements to be named in the row, and have R1's verification index precompute the newest recorded-pass SHA once for all R2 agents.
4. **Per-row repetition of the binding clause bloats the CSV.** ~20 rows repeat the same Receipt-4 sentence. **Proposed revision:** allow the notes header to define the run-local binding token once, with rows citing only test names/lines plus the token — but only if the reviewer accepts that the CSV is then not fully standalone (I kept it standalone for R0 pending that call).
5. **Row-generation rule produces near-duplicate ACCEPTANCE rows.** Datasheet Conditions restate requirement clusters; my 6 ACC rows are composites of REQ evidence. This is tolerable (they caught nothing new here) but at 53 deliverables it is real overhead. **Proposed revision:** permit ACC rows to cite their covering REQ rows for evidence (as I did) rather than re-deriving, and instruct R2 agents to add net-new ACC content only where a Datasheet condition is not requirement-covered.
6. **Register-internal inconsistency has no claim-row home (plan §6 row rule).** Found live: `Dependencies.csv` row DEP-03-04-008 is `RETIRED` (2026-05-24, RUL-SCC-001-TRANCHE-001) while `_DEPENDENCIES.md`'s digest tables still show it ACTIVE with counts "ACTIVE 10 / RETIRED 0" and a satisfaction tally (N/A 5, SATISFIED 1, TBD 4) that does not match the CSV (N/A 6, SATISFIED 1, TBD 3). This is a REMAINING_STATE_MISMATCH-shaped defect on a register surface, but the row-generation rule only mints rows for requirements/acceptance/exclusions/unmapped/remaining. **Proposed revision:** allow one run-local `REGISTER-<n>` row type (or an explicit notes-section contract, as here) for dependency/reference register defects, so R3 receives them in the ledger rather than in prose. Until revised, this finding lives here: *repair `_DEPENDENCIES.md` digest to match `Dependencies.csv` (008 RETIRED) via an authorized R5 tranche.*
7. **Minor, same shape:** `Datasheet.md` Attributes row "PRD source state" still says PRD is "hash-mismatched against `_REFERENCES.md`" while `_REFERENCES.md` REF-006 records MATCH (verified by live hash re-computation at `4c8ed8907`) and the Datasheet's own References section says reconciled. Stale setup wording; same R5 doc-repair class as REQ-014.
8. **DEFERRED_AGENT_WORKFLOW observations:** none arose. No claim in this deliverable required judging an agent instruction, skill contract, or workflow (plan §3 boundary 8 untriggered). For completeness: the permission-broker behavior (UNMAPPED-1) is product runtime, not agent-workflow, so it stays in the ledger.

## 4. LatestDecision-mapping verdict (D-APP-40 — the calibration question this deliverable was sampled for)

**Verdict: the ruling mapped onto claim rows cleanly and did real work on 7 of 28 rows; the mapping discipline is workable at scale with one refinement.**

- **Direct binding:** REQ-006A is the ruling made into a requirement (added by ADQ-05, 2026-06-21); its row binds `LatestDecision=D-APP-40` and its evidence is exactly the ruling's split — `turn.interrupted` on explicit interrupt (`routes.test.ts:1133`), `turn.cancelled`-never-interruption on disconnect (`routes.test.ts:1185`), `cancel()`-not-`interrupt()` dispatch (`turn-engine.test.ts:208`). The implementation even carries the ruling in a code comment (`turn-engine.ts:334`). This is the strongest decision-to-code trace in the deliverable.
- **Interpretive binding:** REQ-004 (disconnect cancellation), REQ-006 (terminal durability), REQ-007/REQ-010 (`harness:event` as a retained public name is a D-APP-40 term), REQ-013 (mapper taxonomy), ACC-001/ACC-002 all carry D-APP-40 because the ruling *interprets* their vocabulary even though their normative source is CONTRACT/SPEC. Deciding "does the ruling govern this row or merely touch it" was the only judgment cost; my rule of thumb — bind the ruling wherever its taxonomy chooses between otherwise-lawful implementations — was easy to apply consistently.
- **Boundary observed:** D-APP-40 does *not* enumerate the `interruption.requested/completed` audit events (UNMAPPED-2), and the row says so explicitly in its LatestDecision cell rather than stretching the ruling. The ruling's own provenance note (agent choice later explicitly owner-ratified) mattered for confidence but not for mapping.
- **Refinement for R2:** the `LatestDecision` column contract should distinguish "ruling governs this row" from "ruling is context" — I used a parenthetical qualifier on UNMAPPED-2; a controlled suffix (e.g. `D-APP-40` vs `D-APP-40 (context)`) would make the ledger machine-filterable.

Also load-bearing but unproblematic: D-APP-54 (lifecycle row reads IN_PROGRESS everywhere; CHECKING-era approval SHA treated as preserved historical evidence per the rebaseline, never a current-state claim) and D-APP-55 (binds only the REM-001 bootstrap row).
