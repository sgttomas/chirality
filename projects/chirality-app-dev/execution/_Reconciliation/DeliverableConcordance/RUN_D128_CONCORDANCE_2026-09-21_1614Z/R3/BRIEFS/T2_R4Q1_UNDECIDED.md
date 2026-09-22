# T2 — R4-Q1 on rows the REACH-tag script cannot decide (Addendum 6 rule 3, Addendum 8)

Read `_COMMON.md` first. Also read CONVENTIONS §2.3 (ImplementationEvidence reachability) and §2.4
("Legacy-versus-live subject test (R4-Q1)", rules 1–4 and the Addendum 8 reading), RUN_BASIS
Addenda 6 and 8, and `<RUN>/R3/_work/T4A_RUNWIDE.md` (R3's run-wide reach calls (a) and (b),
which R3 applies before this step).

**Rule 3 as R3 applies it.** Cite `R4-Q1` in HumanDecisionNeeded on every row where the only code
meeting the claim (apart from tests) is tagged `REACH=LEGACY_ONLY`, whether the row is judged on
the live path or at module level. Rows met by LIVE code, and rows with no code evidence, do not
cite R4-Q1 *for this reason*. R3 has already added R4-Q1 by script where the tags are LEGACY_ONLY
(and TEST_ONLY) only and the Disposition says the code meets the claim in whole or part
(ALIGNED, PARTIALLY_IMPLEMENTED).

**Input.** `<RUN>/R3/_work/CAND_R4Q1_TASK.csv`, column `Question`:
- `ADD?` — tags are LEGACY_ONLY (± TEST_ONLY) only, but the Disposition (STALE_SPECIFICATION,
  IMPLEMENTED_DIFFERENTLY, AUTHORITY_CONFLICT, ACCEPTED_DIVERGENCE, …) does not say whether the
  legacy code meets the claim. Decide whether LEGACY_ONLY code is the only non-test code meeting
  (part of) the claim → `ADD`; else `NO_ADD`.
- `KEEP?` — the row cites R4-Q1 but carries no LEGACY_ONLY tag (tags LIVE and/or TEST_ONLY, or
  none). Decide: `KEEP_RULE3` (the evidence names legacy code that meets the claim but the tag is
  missing or wrong — give the corrected tag), `KEEP_OTHER` (the row turns on the R4-Q1 question
  itself for another stated reason, for example it is about whether the retained harness is an
  obligation; quote that reason), or `DROP` (neither: the claim is met by LIVE code or by nothing,
  and the row gives no other R4-Q1 reason).
Also apply rule 4: on a product-behaviour row met only by legacy code, Notes should record
`ALSO_MODULE:<verdict>`; list it when missing.

Evidence is the row, the frozen code it cites and `<RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv`.

**Output 1.** `<RUN>/R3/_work/T2_R4Q1_VERDICTS.csv`:
`ClaimKey,Question,Verdict,NewHumanDecisionNeeded,TagFix,AlsoModule,Basis`
- `NewHumanDecisionNeeded`: the full new cell (keep other tokens; `NO` stands alone).
- `TagFix`: for KEEP_RULE3 only, `Find=>Replace` on ImplementationEvidence (exact substring
  occurring once), else empty.
- `AlsoModule`: `ALSO_MODULE:<verdict>` to append to Notes, else empty.
- `Basis`: one sentence with the path or row text that decides it.

**Output 2.** `<RUN>/R3/_work/T2_NOTES.md` (≤ 40 lines): counts and patterns.
