# Receipt — HELP-HUMAN-PEC-20260927-RV1-INTAKE

This receipt is a derivative account. The [work graph](../../WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md) carries execution, and the sources below keep their authority.

## Owner direction

Ryan Tufts, 2026-09-27, verbatim:
- The direction: `../../_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md`. It covers the intake dispositions, RV1 authorized, K3 as a Task Management row, production left to a different session, and the freeze point ("This work you're proposing now is meant just to be put in the record so that it can be considered when everything undergoes a reassessment from the ground up."), followed by "Yes I still want you to complete the task management work and the RV1."
- The MEMORY grant: "grant the MEMORY rows for DEL-00-01 and DEL-00-03" (`../../_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md`).
- The re-acceptance: "ACC: option 1; accept all findings as is; re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001" (`../../_DECISIONS/D-PEC-108_D1_REACCEPTANCE_2026-09-27.md`).

## Result

- **Direction (DIR, PR #1018, `acc7d3cc7`).** `D-PEC-107` record and register row; this graph; STATUS.
- **Task Management (TM1, PR #1021, `56f7d4602`).**
  - CAND-01 disposition (b).
  - TM-PEC-026 (CAND-02, OPEN), which now also holds the consumer-contract design item.
  - TM-PEC-027 (CAND-03, ELEVATED to Root) and the notice `../../../../../../execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md` (Root).
  - TM-PEC-028 (K3, DEFERRED until a DEL-08-06 production packet).
  - The MEMORY grant supplement.
- **REVIEW (RV1, PR #1023, `31a90f3e6`).** Run folder `../../RV1_D1_REVIEW_2026-09-27/`; bundled `review` pinned at `2f825f180`.
  - DEL-00-01, `SELF_CHECK`: RF-001 MAJOR (AC-002 partly met), three MINOR and one OBSERVATION.
  - DEL-00-03, `PEER_REVIEW`: AC-001 to AC-010 pass, with two MINOR, five OBSERVATION and CU-001.
  - No lifecycle, SOW or artifact write.
- **Re-acceptance (ACC, `D-PEC-108`).** Every RV1 finding is `ACCEPT_AS_IS`; for RF-001 this means AC-002 is accepted as partly met.
  - `ACCEPT_EXACT_BYTES`: DEL-00-01 ADRs `ad6bab7e…c49e` and SOW `3757632b…a647` (its first owner acceptance); DEL-00-03 SOW `0fed4ecb…e843` and SPEC `f84c067b…f617`.
  - AC-007 and AC-011 are confirmed, and CU-001 is retired as history.
  - The decision is recorded in both `_REVIEW.md` and `Review_Findings.csv` files and in one acceptance snapshot each (`REV_DEL-00-01_2026-09-27_1655/` and `REV_DEL-00-03_2026-09-27_1658/`; evidence `../../RV1_ACCEPTANCE_RECORD_2026-09-27/`; PR #1028).
- **MEMORY (M1).** One `## Runs` row each in the DEL-00-01 and DEL-00-03 `MEMORY.md`, under the owner's grant.

## Checks

- Every PR had independent review of its actual head and green CI:
  - `REVIEW_PR1018_0{1,2,3}.md`, `REVIEW_PR1021_0{1,2,3}.md` and `REVIEW_PR1023_0{1,2}.md` under `returns/`;
  - this PR's reviews are listed under Final PR.
- **RV1:** verifier verdicts 01 and 02 PASS WITH NOTES.
- **Closeout (C1)**, at `origin/main` `31a90f3e6`, compared the undertaking's records against their sources:
  - graph, TM rows, notice, both review records and MEMORY rows;
  - `docs/STATUS.md` (refreshed under `D-PEC-88`) and `README.md` (no warranted change).
  - It carried one wording error in the MEMORY-grant supplement, found by PR #1021 review 03 (Q1). The correction is made here, not in the supplement's bytes. The supplement is a merged owner-direction record, and the convention it cites keeps a merged record unedited. `../../RV1_ACCEPTANCE_RECORD_2026-09-27/MANIFEST.md`, written in this PR, also pins its hash. This changes review 03's intended in-place edit into an erratum. The supplement describes `D-PEC-96_AMEND_DIRECTION_2026-09-26.md` as a record "where a later owner direction on a ruling gets its own record". It should read "where a later owner direction gets its own record": that precedent records a later owner direction, not one on a ruling.
- **In this PR:**
  - Strict registers, the harness self-check and loop receipts give output identical to the basis; the evidence is in `../../RV1_ACCEPTANCE_RECORD_2026-09-27/evidence/`.
  - The reliance-hold preflight ran 22 times, all `ALLOW`, with evidence in the same folder.
  - HELP_HUMAN and PR review 01 also ran `taskmgmt validate` (PASS, 12 rows, register unchanged) and `git diff --check` (clean). No evidence file was saved for these two.
  - ACCCLOSE review 01, dispatched by the manager, was PASS WITH NOTES. Notes 1–3 were repaired in `a1a95aa01`, and its backcheck was PASS.

## Final PR

[sgttomas/chirality#1028](https://github.com/sgttomas/chirality/pull/1028), from branch `claude/pec-rv1-intake-closeout`. Its description is this receipt's result, checks and limits. It carries the manager's acceptance records and MEMORY rows (brief `briefs/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`, return `returns/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`), and HELP_HUMAN's `D-PEC-108` record and register row, this receipt, the graph completion and STATUS. HELP_HUMAN's independent PR reviews are saved as `returns/REVIEW_PR1028_0N.md`.

## Limits and what carries

- **Freeze point.** PEC rests here for the owner's ground-up reassessment (`D-PEC-107` §Freeze point). The considerations are recorded, not prepared:
  - the consumer-contract design and the next scope change (TM-PEC-026);
  - hosted CI (TM-PEC-027, Root's);
  - K3 (TM-PEC-028);
  - the RV1 REVISE proposals (`D-PEC-108`);
  - re-reviews of DEL-04-01 and DEL-03-01.
- Production is left to a different session.
- No lifecycle change and no ISSUED, Gate 5, P1, production or C-05 act. DEL-00-01 and DEL-00-03 stay `CHECKING`.
