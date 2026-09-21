# V-SHARD-DEL-08-03-1: verifier notes (RUN_D128, R2 PKG-08)

These notes are evidence for the PKG-08 manager, not rulings. The shard covered 23 items from `DEL-08-03_claims.csv` and `DEL-08-03_reverse.csv`. All reading used the frozen tree at `00115c719`.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW, self-flagged) | 3 | 0 | 0 | 3 |
| a30 | 14 | 13 | 0 | 1 |
| b (ALIGNED sample) | 3 | 3 | 0 | 0 |
| c (reverse responses) | 3 | 3 | 0 | 0 |
| **Total** | **23** | **19** | **0** | **4** |

- **Disposition-level REFUTED:** none.
- **CONTESTED items and the field at issue:**
  - `CLM-013.11`: Disposition.
  - `CLM-031`: Disposition. This is a SEE row that follows `CLM-013.11`.
  - `CLM-006`: Disposition.
  - `CLM-013.13`: CauseTag.

## (ii) Systematic patterns

1. **Negative requirements whose proof exists only on the legacy or test-only path** (`CLM-013.11`, `CLM-031`).
   - On the live path, selector state cannot reach execution:
     - `turn/route.ts` forwards only a `V3TurnRequest` to the Runtime;
     - the live `delegate_agent` descriptor requires `contextSealed`, `pipelineRunApproved` and `approvalRef`.
   - The recorded pass evidence runs only on the TEST_ONLY dispatch contract and the LEGACY_ONLY SDK route.
   - The §2.3 LEGACY_ONLY rule does not settle whether this is `PARTIALLY_IMPLEMENTED` or `STALE_VERIFICATION`. The worker self-flagged the same alternative.
   - `R4-Q1`, the REACH tags and `OVERTAKEN` are correct.
2. **The Gate-5 "compatibility history" reading is applied unevenly across the older SoW tables.**
   - `CLM-004`, `CLM-005`, `CLM-012` and `CLM-013.1` take `ACCEPTED_DIVERGENCE` because the Gate-5 section (SoW:25-27) demotes the earlier tables.
   - `CLM-006` (the Implementation Slots table) takes `IMPLEMENTED_UNDOCUMENTED` instead.
   - The same unrendered-PipelineSurface premise yields three different treatments:
     - `CLM-013.7`: `ALIGNED` / `STILL CURRENT`. Seen through class-c `CAP-WORKSPACE-029`, whose capability row records `STATE=DISABLED`.
     - `CLM-013.1`: `ACCEPTED_DIVERGENCE` / `OVERTAKEN`.
     - `CLM-013.12`: `PARTIALLY_IMPLEMENTED`.
   - Recommendation: a manager-level consistency pass over rows whose only evidence is `pipeline-surface.tsx`.
3. **A mechanism CauseTag paired with DirectionEvidence `NONE_FOUND`** (`CLM-013.13`).
   - The row tags `SHELL_REDESIGN`, inferred from commit history (7941722f6 added the neutral contract beside the Pipeline surface), but no record explains keeping a hand-copied taxonomy with no parity test.
   - §4 does not say whether an unrecorded mechanism still takes precedence over `UNRECORDED_JUDGMENT`.
   - I spot-checked the `NONE_FOUND` search. In `_REGISTER.md`, only D-APP-86 mentions Workbench/Pipeline parity, and it concerns the UI/API parity instrument, not the taxonomy.

**Other observations (not refutations):**
- **Line anchor:** `CLM-012` cites `pipeline-dispatch-contract.ts:120-245`, but the function ends at line 235. The symbol is correct.
- **AssessmentEvidence:** `CLM-013.12` carries `STILL CURRENT` next to a `PARTIALLY_IMPLEMENTED` finding. The INSP-03 PASS still reproduces, but it never covered the root-change case. MR-1 has no token for a PASS that was incomplete when made.
- **MR-8 (iv) vs §2.7:** `CLM-007` restates the REGISTER-2 snapshot. The rules leave open which Disposition a SoW row that restates a snapshot should take.
- **CLM-016, class c:** `CLM-016` cites D-APP-56 P21, which does address DEL-08-03 REQ-010, so MR-11 is applicable. Its CauseTag `CARRIER_PROPAGATION` concerns a partial R5 repair from 2026-07-12, which is before 2026-08-22, so `PRE_V3_DRIFT` may apply. Not graded, because `CLM-016` was a class-c item only.
- **PostReleaseBasis:** no cited path appears in `TOUCHED_PATHS.csv`, so `NO` holds on all 20 forward rows.
- **REACH tags:** every tag checked matches `REACHABILITY.csv`. The "LIVE (unrendered)" annotations for `pipeline-surface.tsx` and `workbench-surface.tsx` are code-verified: `woven-dialogue-route.tsx:18` discards the `legacy` prop.

## (iii) Effort

- **Reading:**
  - about 25 files or ranges: the SoW in full, the ledger and reverse rows (read by script), CONVENTIONS, RUN_BASIS §3 and §5 plus addenda, and the evidence-pack CSVs;
  - code: `pipeline-surface`, `pipeline-dispatch-contract`, `task-scope`, `deliverables-provider`, both scan routes, `turn/route`, `tool-descriptor`, `coordination-panel`, and test case lists;
  - decisions: the D-APP-56 P21 packet, D-APP-108, the `_REGISTER.md` rows and CORPUS_V21_CANDIDATE.
- **Git:** two read-only `git log` calls against the frozen tree.
- **Context budget:** comfortable.
