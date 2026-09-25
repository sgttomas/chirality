# B2 verifier verdict 01 (cycle 1)

Relayed verbatim by HELP_HUMAN on 2026-09-25: the fresh read-only verifier (`subagent_type: pec-reviewer`, `model: opus`) dispatched by B2 returned to HELP_HUMAN rather than to B2. Source: session scratchpad `relay_V1.md`, SHA-256 `18d5484e208bf3f5ce9ab8b0ac1a58aa460ccd595fe7e76b7536262c05cceaaa`. The verdict body below is unedited.

---

VERDICT: PASS WITH MINOR (BLOCKING 0 / MAJOR 0 / MINOR 9)

The package is sound. Every settled selection is applied exactly and nothing unselected is added without being disclosed. All hashes match, and the registers pass the strict validator with exactly the expected result. The nine findings below are wording, coverage and question-set gaps; none needs the package regenerated except as the repairs themselves require.

## Judgement on the specific items you asked about

- **Seq 80 (OBJ-004 view) and Seq 81 (§2.4 bridges bullet):** faithful. Amendment 1's impact delta requires both in so many words ("the OBJ-004 view … needs its own view action"; "checkpoint 2 adds the wording change for both deferred bridges"). Both take new sequence numbers after the intake, and Seq 68 and 72 stay reserved.
- **R1 source-reference edit folded into Seq 74:** faithful. It follows from the accepted Seq 74 front-matter `source_corpus` change, and the preview's A-74 hunk shows it.
- **INV-116 correction riding Seq 12:** allowed by IA §14 ("may ride Seq 12 … if the owner wishes"). The owner is asked about it as Q-CP2-2, with striking it offered as option (b). Acceptable.
- **PRD §7.1 WorkGraph/WorkNode row:** a coherent consequence of accepted Seq 1 and disclosed in A-75, but it goes beyond Annex B and beyond the §7.1 rows the Seq 75 intake lists. See finding 2.

## Findings

1. **MINOR — the plan never names what authorizes the Lane A writes under PEC's write fence.**
   - Location: `Propagation_Plan.md` L18 and L1001 ("authorizes Lane A only"); L1010 (Q-CP2-4 covers only the PRD's adoption record).
   - Evidence: `projects/pec/AGENTS.md` L122 says every write outside the default surfaces needs an owner-ruled D-PEC packet naming paths, acts, verification and rollback. D-PEC-86 §4 L85–88 lists live `docs/PRD.md`, live `_Decomposition/**` and every `_STATUS.md` as "Not opened". The Lane A4 preparation folders need the same authority.
   - Mitigation: the package already names exact paths, acts, checks (C1–C5) and rollback. The D-PEC-86 register row expects writes to follow each checkpoint acceptance.
   - Repair: extend Q-CP2-4 (or the Q-CP2-A text) to state that the group-2 decision record plus a D-PEC register row is the packet that opens every Lane A target, including A4.

2. **MINOR — the new PRD §7.1 WorkGraph/WorkNode row is not put to the owner.**
   - Location: `CP2_CANDIDATE/docs/PRD.md` L248; `Amendment_Preview.md` L1484–1486; SOW-095's SourceRef ("§7.1 WorkGraph/WorkNode").
   - Evidence: Annex B has 28 MODIFY rows and none adds an entity row. Intake Seq 75 lists the §7.1 rows it changes (Loop, Workplan/Step/Gate, Receipt, Package/Deliverable, DependencyEdge, RunRecord) and adds none.
   - Repair: name the row as a checkpoint-2-derived PRD addition in Q-CP2-A, so the owner accepts it explicitly. If the owner declines it, SOW-095's SourceRef has nothing to point at.

3. **MINOR — some overridden PRD v2.2 facts have incomplete or missing supersession bindings.**
   - D-001's reference cites L204/L210 and quotes only the Workplan row. Seq 1 also overrides the Package/Deliverable "remaining items" row (L208) and the Loop row's "LOOP_INIT/workplan-governed" wording (L203).
   - Seq 55 (vocabulary `harness`) overrides §8 L237 "Harnesses (runtime daemon; …)" but has `SupersessionBindingPresent=NO` and no row.
   - D-010's AppliesToSections omits SOW-094 (Seq 11, feed-profile selection).
   - The drafters' own policy (D-001 Notes) is to bind every v2.2 fact the amendment overrides, even where v2.3 restates it.
   - Repair: add the loci to D-001, add a D-055 row and set Seq 55 to YES, and add SOW-094 to D-010.

4. **MINOR — A-76 says the six D-PEC-79 hunks are "carried", but two are rewritten.**
   - Location: `Amendment_Preview.md` L1490–1492; `Amendment_Actions_CP2.csv` Seq 76.
   - Evidence: against the adopted postimage (`92627ee1…b5f0`), hunk 1's Date/Status and hunk 2's epistemic paragraph are rewritten; only the Version row is byte-identical. Hunks 3, 4 and 6 are byte-identical; hunk 5 (§16.3) changes only as stated. `PRD_V2_3_SUCCESSOR_DIFF.md` L54 and L72 do label hunks 1–2 "(extended)". The carried hunk-3 provenance line saying §16.3 "creates no new product meaning" is now qualified only by the new successor block.
   - Repair: state in A-76 and Seq 76 that hunks 1–2 are rewritten for the new adoption instrument.

5. **MINOR — the PRD candidate misstates how the no-listener posture descends from D-GOV-20.**
   - Location: `CP2_CANDIDATE/docs/PRD.md` L348 (PEC-API-001) and L580 (§16.9): "no-TCP-listener posture of D-GOV-43 A2 (carried from D-GOV-20 item 4)".
   - Evidence: `D-GOV-43_codex_host_replatform.md` L73 supersedes D-GOV-20 items 2, 3 and 4, and item 4 is the no-TCP listener. The A2 supplement (L50) says only "No network-exposed listener is introduced."
   - Repair: say "D-GOV-43 A2 (no network-exposed listener), superseding D-GOV-20 item 4".

6. **MINOR — the preview's "replay reproduces the candidate byte-for-byte" claim is overstated.**
   - Location: `Amendment_Preview.md` L16.
   - Evidence: replaying 139 hunks in document order, 14 fail. The failures are anchors that quote a later hunk's result (e.g. L696 quotes SOW-094 as already edited by A-11), inserts with no anchor line (L346–372, L705–719), and hunks cut off mid-line (L84, L159, L170, L1201, L1279, L1422). With order-tolerant application and the stated insert positions, the only remaining differences are exactly those inserts and cut-off lines; every real change is shown. The PRD diff has the same issue in 5 cut-off hunks (L154, L376, L390, L402, L416).
   - Repair: soften the claim, or make those hunks complete. Impact is low, because the candidate files and their hashes are what the owner accepts.

7. **MINOR — the rule for checking hashes when the date slots change is not stated.**
   - Location: `Propagation_Plan.md` C1 ("each written file's SHA-256 equals its planned postimage") against A1.3 and `Amendment_Preview.md` L36–54.
   - Evidence: the pre-acceptance variant hash `fbc558d8…` includes `date:`, §7 Revision and DL-20, all set to 2026-09-25. If either acceptance lands on another date, every accepted hash changes. During checkpoint-3 preparation the live file would also carry that acceptance date before any acceptance.
   - Repair: state the rule in C1 and Q-CP2-A: substitute the listed slot values, recompute, compare, and record.

8. **MINOR — the notice list misses `projects/pec/AGENTS.md`'s PRD-version lines.**
   - Location: `Propagation_Plan.md` L977 names only §Shared Runtime Boundary.
   - Evidence: `projects/pec/AGENTS.md` L28 ("`docs/PRD.md` v2.2 is the … definition of record") and L170 become false once v2.3 is adopted. README and STATUS are already covered under D-PEC-88 (B8).
   - Repair: add L28 and L170 to that notice row.

9. **MINOR — editorial.**
   - `CP2_CANDIDATE/_Decomposition/Deliverables.csv` L26 (DEL-04-01) says "parked lanes" twice: "…and parked lanes over graph READY/ACTIVE/BLOCKED nodes, parked lanes with unparking acts". SOW-004 reads "each parked lane with its unparking owner action". The same text is mirrored into the DEL-04-01 `_CONTEXT.md` (plan L327–330).
   - Vocabulary `loop` (candidate SOFTWARE_DECOMP L617) embeds a dated observation, "bridge [no receipt since 2026-08-02]", which will go stale.
   - Two long lines were not rewrapped (candidate SOFTWARE_DECOMP L103–104; candidate PRD L122–123).

## What checked clean

- **Selections:** Q1–Q10, CP1-R/D79/X/N/V/O, TM-PEC-023 rows 1, 2, 3, 5, 8 and 9 (4, 6 and 7 disposed without a mapping), and Seq 77, 78, 79 and 43, all match the accepted snapshots. Q9 leaves SOW-058 unchanged. Q10 (a) leaves PRD §12 P1 byte-unchanged.
- **Child closure:** 4 deliverables retired, no orphan. PKG-06 keeps 5 active children, PKG-07 keeps 2, and OBJ-003 has 14 supporters. The only surviving row that targets a retired deliverable is DEP-09-05-005, which is routed to Lane B3. Execution edges: 119 − 10 − 1 = 108, verified.
- **Stable identity:** only SOW-095/096 and DEL-02-08/09 are added, and physical row order is preserved. Every name and path is retained.
- **Invariants (recomputed independently):** union rule 0 mismatches over all 66 rows. Coverage links are reciprocal, package IDs agree, OUT/TBD rows are cleared, and every row keeps a PhaseHint. ContextBudgetQA covers all 66 rows and its envelopes agree with the register. Counts are 96 = 70 IN / 18 OUT / 8 TBD; 66 deliverables = 62 active / 4 retired; envelopes S28 / M32 / L2. The four objective views, 26 vocabulary terms and 10/3 open/resolved issues all match. The preview's §11 table agrees throughout.
- **Supersession:** all 26 quoted original texts occur at the cited PRD, D-PEC-78 and D-PEC-79 loci; four of them span wrapped lines, within the cited ranges. The 25 `YES` flags equal the 25 distinct binding IDs. The duplicate D-010 ID is tolerated because the accumulator keys on the full row.
- **PRD candidate vs Annex B and D-PEC-90:** all 28 MODIFY loci change and all 8 NOTE-ONLY loci are untouched. No PEC-K row changes and no reliance text is added.
- **Propagation plan:** all 22 `_CONTEXT.md` and 4 `_STATUS.md` preimage hashes match live bytes, and every planned postimage hash reproduces from its hunks. The plan's claims about `write_status.sh`, the Root RETIRED precedent, the SCA-004 repair commits and the 16 stale "revision 1.1" reference claims all verified.
- **Write boundary:** only the 11 new files, all within the allowed paths. Nothing else differs from `origin/main`.

## Checks run

All from REPO_ROOT unless noted. TMP = `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B2/verify`.

1. `shasum -a 256` on the accepted basis: IA, intake, Brief, group-1/amendment-1/amendment-2 snapshot files, resolution note, TM-PEC-023 decision surface, live SOFTWARE_DECOMP and PRD, the D-PEC-79 folder, both `_LATEST.md`, all package files and the candidate files. Exit 0; every quoted hash matches.
2. `sed` substitution of the two front-matter lines into TMP, then `shasum`: gives `fbc558d8…`, as claimed. Exit 0.
3. `diff` of each live register and the decomposition against its candidate. Exit 1 (differences expected).
4. `diff` of live PRD vs the D-PEC-79 postimage, and of the postimage vs the candidate. Exit 1 (differences expected).
5. `python3 TMP/replay2.py Amendment_Preview.md` (order-tolerant hunk replay). Exit 0; result as in finding 6.
6. `python3 TMP/replay_prd.py`. Exit 0; 5 cut-off hunks, otherwise reproduces.
7. `python3 TMP/pp.py` (Lane A2/A3 hashes and replay). Exit 0; 26/26 OK.
8. `python3 TMP/inv.py` (union rule and cross-register checks). Exit 0; 0 mismatches.
9. `python3 TMP/cite.py` (action citations vs intake). Exit 0; only the expected differences.
10. `python3 TMP/sd2.py` (supersession originals at cited lines). Exit 0; four span wrapped lines, confirmed with `sed`.
11. `python3 tools/validation/validate_decomposition_registers.py <TMP overlay>/projects/pec/execution --strict`. Baseline exit 0 (0 errors / 0 warnings). With the four candidate CSVs overlaid: exit 1 under `--strict`, 0 errors, 2 warnings (DRB-008 for DEL-02-08 and DEL-02-09).
12. `python3 tools/coordination/accumulate_supersession_map.py --prior-map …SCA-004…/Supersession_Map.csv --delta …/Supersession_Delta.csv --output-map TMP/Supersession_Map.csv`. Exit 0; 26 rows, 0 findings.
13. `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register …/ACTIVE_RELIANCE_HOLDS.csv --operation candidate-validation --target {snapshot, docs/PRD.md, SOFTWARE_DECOMP.md}`. Exit 0; ALLOW for all three.
14. `grep` checks on the dependency registers, D-GOV-20/43, `write_status.sh`, Root SPEC, the SOW reference claims and `git cat-file -t` on the cited commits. Exit 0.
15. `git status --porcelain --untracked-files=all`; `git diff --name-only origin/main`; `git diff --name-only`. Exit 0; only the 11 files.

The overlay copy and all derived files in TMP are deleted; only my read-only scripts remain there. I wrote nothing in the repository.