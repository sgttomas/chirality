# RR1 return — PEC Remaining retirement: census, decision account and draft D-PEC-99 (provisional) packet

Role: WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking
`HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, node RR1. The brief
`RR1_REMAINING_RETIREMENT_ACCOUNT.md`, SHA-256
`e0bda78f24357181457409b5f035e7b2717d32f9e3c20ab6584a5ceca6486227`, was
verified before work. This return replaces the interim return that the host
forced. **This stage prepared only.** It applied no retirement write, made no
lifecycle change, wrote no register row, and made no CHECKING, ISSUED or
acceptance claim.

## PR

- **PR:** https://github.com/sgttomas/chirality/pull/951 (open, not merged).
- **Branch:** `claude/pec-remaining-retirement-account`.
- **Base:** rebased onto `origin/main` `db9328789`, the commit where PR #943 (SCA-006 checkpoint 3) merged.
- **Head:** the commit carrying this return. HELP_HUMAN's handoff message gives its SHA. The last reviewed candidate is `0729769bea4f10b668839948fdace5845374a1dc`; the only later commit adds this return and `VERIFIER_VERDICT_03.md`.

## Census

The census is 92 keys (`REMAINING_CENSUS.csv`, `b0e25361…45eb4`): 89 live items in 57 sections, plus the 3 items of the frozen DEL-01-05 carrier, which was never applied. It equals the D-PEC-83 counts exactly:

- 57 carriers and 89 items were applied under Receipt 174.
- 1 frozen carrier with 3 items was excluded.
- 92 items were proposed.

Every live item's text, `Depends:` value and gate is byte-identical to the concordance proposal.

- Ticked since application: DEL-01-03 ×3 under D-PEC-87 L-1a, and the four RETIRED deliverables, where SCA-005 closed each item unexecuted.
- Lifecycles of the section-bearing deliverables: OPEN 27, INITIALIZED 25, IN_PROGRESS 1, RETIRED 4. None is CHECKING or ISSUED.
- The 73 held or conditional D-PEC-83 residuals are recorded as outside the census. They stay in the accepted report (`CARRIER_DISPOSITIONS.csv`, `RESIDUAL_RECOMMENDATIONS.csv`).

## Dispositions (proposed; `HumanDecision=PENDING`)

| Class | Count | Keys |
|---|---:|---|
| (a) move into a governing document now | 0 | — |
| (b) Task Management row | 0 | — |
| (c) satisfied or superseded | 9 | DEL-01-03-REM-001..003 (executed); four RETIRED items (closed unexecuted, D-PEC-92); DEL-01-05-REM-001/-002 (scanner repairs executed in `52bb1dddc`; accepting the new bytes is still a separate act) |
| (d) moved to the exhibit | 82 | 71 in Part A, the D-PEC-83 E evidence-inquiry set, still unselected. 11 in Part B, Scope of Work carry-forwards: S1 takes DEL-03-02-REM-016, DEL-03-03-REM-004 and DEL-04-05-REM-003; S2 takes DEL-02-07-REM-001..004; S4 takes DEL-04-01-REM-001/-002, DEL-04-02-REM-002 and DEL-04-03-REM-002; D1 takes none |
| (e) owner decision | 1 | DEL-03-06-REM-004 |

**Why there are no (a) rows.** The sequencing rule from HELP_HUMAN sends an item to (d) when a pending currency node will rewrite its Scope of Work. The only Scope of Work that no node rewrites and that would receive an item is DEL-03-06, which is question 1.

**Gates.** Every moved item keeps its gate line verbatim, and the new `AGENTS.md` paragraph says the gate still binds at the destination.

## Draft packet

- **Proposal:** `projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/DRAFT_D-PEC-99_remaining_retirement_proposal.md`, SHA-256 `29e2ff5704d45f0da31f41fd80bf822003743fbf9effdda4ebbc2806306d5c79`.
- **Bound generator:** `gen_d99.py` `1fad023951f8fca887974452a6b65cfd312b74c1312997ac99a5260b64ee7237`.
- **Closure check:** `verify_d99.py` `c1d50dfd267894f8602b6b4497136e41a6fa2cf5f9ffe614efdb4314ea791865`.
- **Rendered exhibit:** `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`.
- **Account:** `SEMANTIC_DECISION_ACCOUNT.csv` `b240b38d940448a66b37752a1f2509ea4c6783f388c0a8d6cb0d3d21a465f7e2`.

**The act writes 62 paths:**
- The 57 `_STATUS.md` files. In each, the section is removed, `Last Updated` is changed and one History line is appended.
- `projects/pec/AGENTS.md`. Its front-matter line changes, and the Remaining paragraph at L261–272 is replaced. Preimage `4400c4e9…139c`, postimage `df9196d1…25eb8`.
- The decision-owned exhibit.
- The tranche manifest `PEC-REMAINING-RETIREMENT-{DC}.yaml`.
- Two notices, one to Root and one to Runtime, each with its basis recorded. None goes to App or Piping.

**Checks run:**
- `gen_d99.py --check-only` passes on the current worktree.
- `verify_d99.py` passes in account mode, and in act mode (17 checks) on a scratch act.
- Manifest validation (CI mode): G4 PASS.
- Entrypoints: PASS.
- Strict registers: identical before and after.
- 32/32 Scope of Work files validate. The act writes no Scope of Work.
- Task Management validation, the receipts validator and harness self-check pass before the act. The Git-dependent post-act checks are listed as act-time checks.

## Owner questions (in the packet)

None of them concerns CHECKING or ISSUED: no edit touches a CHECKING or ISSUED deliverable.

1. **DEL-03-06-REM-004.**
   - (a) Carry it for S1 (recommended).
   - (b) Park it in Part A.
   - (c) Decline it.
   - The generator takes the answer as `--q1 s1|park|decline`. Without an answer, the act waits.
2. **The 71 evidence inquiries.**
   - (a) Keep them unselected in Part A (recommended).
   - (b) Close them as superseded.
   - (c) Move them into their Scope of Work (amend).
3. **The four RETIRED deliverables' `_STATUS.md`.**
   - (a) Remove their closed sections too (recommended).
   - (b) Leave those files untouched (amend).
4. **Close D-PEC-83 F without application.** Confirmation is recommended. Without it, the act waits.
5. **MEMORY row.** No row is recommended. DEL-01-03 is the only section-bearing deliverable with a `MEMORY.md`.
6. **Model steer.**

**Files that frozen, issued or checking states protect, all left untouched:**
- the whole folders of the CHECKING deliverables DEL-00-01, DEL-00-03, DEL-08-02 and DEL-10-01;
- every DEL-01-05 file, whose repaired bytes still await acceptance;
- every `ScopeOfWork.md`, `Dependencies.csv`, `_CONTEXT.md` and decomposition file;
- `v2/**`.

## Verifier verdicts (fresh `pec-reviewer`, read-only)

| Review | Candidate | Verdict | Outcome |
|---|---|---|---|
| 01 | `f5446bab2` | FAIL | One blocking finding: the disposition totals did not sum to 92. It and the 13 other findings were repaired. |
| 02 | `4f4534ab6` | PASS WITH NOTES | 2 non-blocking findings and 8 notes, all repaired except the return replacement, which this file completes. |
| 03 | `0729769be` | PASS WITH NOTES | 0 blocking, 0 non-blocking, 2 notes. One note is left open (below); the other is this return. |

Transcriptions: `VERIFIER_VERDICT_01.md`, `_02.md` and `_03.md`.

## Containment

`git diff --name-status origin/main...HEAD` shows only files this brief allows:
- the TM folder `projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`, which holds:
  - the census and comparison;
  - the federation preflight;
  - the account (CSV and MD);
  - the run basis;
  - the draft proposal, generator, closure check and rendered exhibit;
  - three verdicts;
- this return.

Nothing was written to any `_STATUS.md`, Scope of Work, `_DECISIONS/**`, register, `AGENTS.md`, `loop/**`, `docs/**`, README, work graph, `v2/**` or foreign path.

## Unresolved, for the caller

1. **Owner ruling.** The owner must rule on the packet (graph node RR2). HELP_HUMAN publishes it under `_DECISIONS/` with the register row, and the number is fixed then.
2. **Graph maintenance.** At application, HELP_HUMAN adds the "Absorbs … Part B items" sentences to rows S1, S2 and S4 of the POST-SCA005 graph. The S1, S2 and S4 packets must absorb their Part B items as exact carry-forwards.
3. **Findings for other nodes** (packet "Findings beyond the brief"):
   - DEL-02-01's Scope of Work still parses `remaining-items` (for S1).
   - DEL-04-01's Scope of Work lags SOW-004, and TM-PEC-004 pins an older SOW hash (for S4).
   - Two quotes of "fourteen" entity types go stale after the S2 rebuild. The DEL-03-06 one has no node.
   - `docs/STATUS.md` needs a D-PEC-88 update after the act.
4. **Open verifier note.** Review 03 note 1: `verify_d99.py` cannot tell the s1 answer from park by heading. The act-time byte comparison already covers this. A small verifier hardening can ride the act's preparation.
5. **Git-dependent act-time checks.** The post-act harness self-check and the manifest diff mode could not run on the scratch tree, because this manager's Git access is confined to its worktree.
