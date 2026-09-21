# V-DEL-07-04 — verifier shard notes (DEL-07-04)

Basis: the frozen tree at `00115c719`. Graded against CONVENTIONS.md and the shared grading key in `BRIEFS/VERIFIER_BRIEF.md`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 1 | 2 | 0 |
| a30 | 16 | 16 | 0 | 0 |
| b | 4 | 4 | 0 | 0 |
| c | 4 | 4 | 0 | 0 |
| **Total** | **27** | **25** | **2** | **0** |

Distinct ledger rows checked: 25. CLM-011.5 and CLM-011.7 appear in two classes each.

Verdict-field refutations (Addendum 3): 1 of 25 distinct rows (4%). It is CLM-032 (Disposition). No reverse `Response` was refuted.

## (ii) Patterns

1. **Snapshot-dated CONTEXT text graded as stale.** CLM-032's conflict table says "No source conflict identified during P1/P2 drafting". The text names its own drafting snapshot and was true at that time. The CONTEXT_CLAIM rule and MR-8(iv) / tie-break 3 therefore give `NOT_AUDITABLE`, not `STALE_SPECIFICATION`. The worker self-flagged this reading as the alternative. The later conflicts it lists are real and worth carrying in Notes for R3:
   - the SPEC §4.3 reversal rows (a9fb1af4a);
   - D-APP-13 against K-AUTH-1 and K-GATE-1;
   - D-GOV-43 against SPEC §14.2 and K-MCP-1.
2. **ALSO_MODULE missing on a legacy-only product-behaviour row.** CLM-013.7 is about output copy and event records not presenting tool actions as approval. Only the legacy `status_transition` test meets it. The row cites R4-Q1 correctly but omits `ALSO_MODULE:<verdict>`, so it is REFUTED on Notes (grading key 5a).
   - The live path has no wording or event check, so its Disposition could equally be `DOCUMENTED_UNIMPLEMENTED`. I recorded this as a secondary reading.
   - The other legacy-touching rows in the sample carry the required tokens: CLM-005, CLM-013.6 and CLM-022.
3. **Minor, no refutation:**
   - CLM-011.5 labels itself "Module subject". Actor authorization is a permission control, so subject-test rule 1 makes it product behaviour. The live path gives the same Disposition either way.
   - The route REACH=LIVE tags are correct as executable Next API entries. The worker states correctly that no rendered UI calls them (`woven-dialogue-route.tsx:18` voids the legacy element).
   - Every line anchor checked holds at the frozen tree: transition.ts, status-writer.ts, status-parser.ts, deliverable-contracts.ts, read-tools.ts and SPEC.md.
   - Every cited test case name exists.
   - None of the cited files is in `TOUCHED_PATHS.csv`, so `PostReleaseBasis=NO` holds.

## (iii) Effort

About 20 files or ranges read:
- the SoW, `_STATUS`, `_REFERENCES`, `_SEMANTIC`, `Dependencies.csv` and INSP-03;
- 7 code and test files;
- SPEC, CONTRACT and DIRECTIVE §0 excerpts;
- the D-APP-13 ruling;
- the evidence pack and capability rows.

Read-only `git blame` / `git log` was run on SPEC §4.3, transition.ts and the two missing module paths. The context budget was comfortable.
