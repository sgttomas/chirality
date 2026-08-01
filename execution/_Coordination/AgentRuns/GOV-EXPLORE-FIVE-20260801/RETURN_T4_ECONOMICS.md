# T4 terminal return — governance economics (verbatim)

All computations are done. Here is the data return.

## Volume counts (with commands)

All commands run from the worktree root `/Users/ryan/dev/chirality/.claude/worktrees/chirality-architecture-remediation-e70332`.

| Metric | Value | Command |
|---|---|---|
| Total commits (current branch history) | 2,632 | `git log --oneline \| wc -l` |
| Total merge commits | 483 | `git log --oneline --merges \| wc -l` |
| Merges to main (first-parent) | 447 | `git log --oneline --merges --first-parent main \| wc -l` |
| Loop receipts, total | **419** | root 77 (Receipts 0–76: `grep -oE "^### Receipt [0-9]+" execution/_Coordination/LOOP_RECEIPTS.md \| sort -u \| wc -l`); app-dev 104 (0–103, legacy `- **date — Receipt N**` + versioned `Receipt-ID:`); piping 84 (0–83); pec 121 (0–120); bridge 33 (0–32) via `grep -oE "— Receipt [0-9]+" <ledger> \| sort -u \| wc -l` |
| Decision-register rows | **275** | gov 31 (`grep -cE "^\| *D-GOV-" docs/governance_harness/_DECISIONS/_REGISTER.md`), app-dev 82, pec 68, piping 68 (`^\| D-[0-9]`), tier-0/_DomainEngines 26 |
| Decision packet/ruling files | 351 | `find . -path "*_DECISIONS/*" -name "*.md" \| grep -v _REGISTER \| wc -l` |
| Coordination notices | 40 | `find . -name "NOTICE_*" \| wc -l` |
| Handoff states | 159 | `find . -name "HANDOFF_STATE*" \| wc -l` |
| AgentRuns run records (top-level dirs) | 80 | root 33 + piping 24 + app-dev 22 + pec 1 (`ls <dir>/AgentRuns \| wc -l`) |
| Tranche manifests | 21 | `ls docs/governance_harness/tranche_manifests \| wc -l` |
| Workplans | 28 | `find . -name "WORKPLAN*.md" \| wc -l` |
| TM register rows | 102 (46 CLOSED / 52 DEFERRED / 4 OPEN) | csv parse of `execution/_Coordination/_TaskManagement/REGISTER.csv` |
| Ledger prose mass | 859 KB across the 5 LOOP_RECEIPTS.md files | `wc -c` |

**Ratios:** 0.94 receipts per merge to main (419/447); counting receipts + decision rows + notices + handoff states + manifests + run records + workplans = 1,022 durable governance artifacts ≈ **2.3 governance artifacts per merge**. Note the prompt's priors were slightly off: root has 77 receipts (not 76), app-dev 104.

## Catch ledger (each instance, cited) and bypass ledger

**Catches — governance mechanism stopped or corrected a real error before propagation (12 concrete instances found):**

1. **CI tracked-whitespace guard, pre-merge**: rejected CRLF line terminators the CSV writer put in REGISTER.csv on PR #429; normalization commit `cca82c98e`, parsed content verified identical (root Receipt 69).
2. **Test-routing drift guard, on main**: `tools/taskmgmt` landed unrouted; the guard failed the full-estate main run "with a remediating message; routed within hours (PR #438)" — the evidence record itself labels it "first live catch" (`plans/evidence/2026-07-31_test_estate_optimization.md` §1, §3.4).
3. **Triage node-A verification**: corrected two wrong closure citations (TM-ROOT-033 → D-GOV-30 R-3 + frozen merge-approval matrix; TM-ROOT-045 → compound D-GOV-31 + Receipt 64) before the owner's bulk-close ruling (Receipt 70).
4. **Triage completeness check**: caught a malformed source row missed at seeding; TM-ROOT-101 minted by owner ruling (Receipt 70).
5. **Triage node-B sampling**: 4 of 6 sampled "open" packet questions already had answers/rulings (rows 054/062/068/076; D-APP-13, D-APP-40 of 2026-06-21, code evidence) — caught that blanket Stage-B deferral "materially overstates how open the C7 residue is" (`AgentRuns/GOV-TM-TRIAGE-CLUSTER-20260731/RETURN_B.md` line 31); TM-ROOT-054 was then closed on code evidence instead of deferred.
6. **Live-vs-derivative check at seeding**: the 07-28 review's "~115 items" resolved to 100 live rows; packet-question count 22 live vs the review's 23 (Receipt 68) — derivative drift caught before it seeded phantom work.
7. **G0 guard BLOCK** on scratch root materialization in the §7 preflight — fence worked as designed, and the same preflight proved 311 harness tests and all other validators blind to that class, which drove G1–G4 being built (root Receipt 45).
8. **Bridge severity pin + CI red**: at `a7e554d3a` the live-baseline pin FAILED (REVIEW=30 vs pinned 29, PR #38 harness red) — a machine-absolute path quoted in a decision packet after Receipt 18's checks ran; fixed `a605f1b37`, pin restored not weakened (bridge Receipt 19).
9. **Independent refutation pre-landing**: "T3 v1 physics defect refuted and cured pre-landing" in the piping mechanics campaign (piping Receipt 61).
10. **Evidence sweep**: caught one out-of-fence test failure (DEL-07-02 wind required-set mirror), repaired as disposition-class work; truthful FAIL sweep preserved beside the admitted one (piping Receipt 62; same pattern with preserved fail-closed halt in Receipt 63).
11. **Fan-in validation**: "one PDU-020 schema/fixture omission found and corrected through DEL-17-08 owner" before integrated fan-in PASS (piping ledger, D-41 R5 T4 receipt).
12. **Per-check verification before consolidation** (Ruling E): showed all 45 inline claims-language checks cover surfaces the repo-wide validator does not scan — zero were removed, reversing the orchestrator's own recommendation (evidence record §2). Related: 2 of 5 owner rulings that session resolved contrary to the recommendation once agents verified premises, and the dated-induction note records "~1/3 of confident upstream claims inverted under verification."

**Bypass/failure ledger (8 instances):**

1. PR #424 changed two `docs/` instruction-surface paths with no tranche manifest; G4 CI is schema-only so CI passed — disclosed, not cured (Receipt 66).
2. PR #427 changed `.github/workflows/` and `tools/` with no manifest — same class, disclosed (Receipt 69).
3. **PRs #431, #432, #438 also changed instruction-surface paths** (`tools/`, `.github/workflows/`; `tools/` is in SPEC §0.2.1's protected enumeration per `tools/validation/validate_instruction_tranche_manifest.py` lines 73–75) **with no manifest in `tranche_manifests/` and no receipt disclosure I could find** — found by this analysis, not by the archive. So the disclosed gap rate understates the actual gap rate: 5 of 11 merges in the instrumented window touched protected paths manifest-free, 2 disclosed.
4. G4 running schema-only in CI is the standing gap enabling all of the above (Receipt 66).
5. Branch protection could not be applied from the session (tool permissions); red-check merges remained "mechanically possible... barred only by the recorded explicit-verdict-gate discipline" (Receipt 30).
6. Bridge Receipt 18's recorded "pytest 255 passed" did not hold at the branch's final SHA (Receipt 19) — checks-then-drift.
7. `validate_architecture_basis.py` pinned `revision: 0.9` against an accepted 0.11, "failing for every contributor" — a governance validator defect found by profiling, not by governance (evidence record §1).
8. The pre-TM state itself: 29/30 notices TRACKED_OPEN, ~950 passing tests running on no machine, 159 tests uncollectable (evidence record; notice CSV below).

## The forgetting baseline, quantified

- **Notice ledger**: 29 of 30 rows `TRACKED_OPEN` in `PROGRAM_ARCH_REMEDIATION_NOTICE_STATUS_2026-07-28.csv` (`awk` on AcknowledgementState); Receipt 70 states the baseline as 1/30 ever closed.
- **Horizon findings**: 0 of 9 closed at source — `FINDINGS.csv` statuses are all PENDING/OPEN/DEFERRED variants, never updated, even though HZN-001/002 had been substantively addressed by D-GOV-31 on 07-29 and HZN-006 repaired at commit `d3ef6463c` on 07-29.
- **Packet questions**: 4 of 6 sampled already answered (RETURN_B.md); rulings D-APP-13 (2026-06-16) and D-APP-40 (2026-06-21) had answered questions that sat "open" for ~5–6 weeks; TM-ROOT-054's answering code (`claude-agent-sdk-manager.ts`) was created 2026-05-24 (`git log --diff-filter=A`).
- **The headline computation**: of the 46 rows closed at first triage, I dated every EvidenceRef (git path-creation dates via `--diff-filter=A`, receipt dates resolved from ledger headers). **42 of 46 (91%) closed entirely against evidence created before 2026-07-31**; 1 (TM-ROOT-052) mixed (07-29 change + same-day re-verification); 3 were administrative (1 DUPLICATE, 2 substance-carried-by-open-rows). Splitting the 42: 33 were stale-attention items (INFORMATIONAL_NO_ACTION — notices/questions that never needed action but nothing could ever mark them done), and **9 were genuinely done-but-untracked work** (6 RESOLVED_BY_DECISION + 034/049 resolved by 07-29 changes + 054 resolved by code). Method caveat: a naive git-blob dating of EvidenceSha gives the opposite answer (40/46 same-day) because ledger files' current blobs are always fresh — I rejected that method as biased and dated the cited artifacts/receipts instead.

## Overhead fraction for the instrumented session

For the 11 merges PRs #426–#436 (`git diff --numstat <merge>^1 <merge>` per merge, paths classified as governance-artifact if under `_Coordination/`, `governance_harness/`, `_DECISIONS/`, `_TaskManagement/`, `agents/`, `tranche_manifests/`, `docs/CONTRACT.md`, `AGENTS.md`, or named LOOP_RECEIPTS/HANDOFF_STATE/WORKPLAN/NOTICE_):

- **Whole window**: 2,005 governance lines vs 4,660 product lines → **30.1% of changed lines**; 36 of 158 files (22.8%).
- **Stage-A PRs only** (#426/428/429/430/433/434/435/436): 2,005 gov vs 625 product → 76.2% — but the "product" is `tools/taskmgmt` itself, i.e. Stage A's deliverable *was* governance infrastructure, so this number is definitionally high, not diagnostic.
- The cleaner reading: the engineering lane (#427/#431/#432, CI + test-estate work) shipped 4,035 lines with zero in-tranche governance lines (and, per the bypass ledger, no manifests); the governance lane carried all the paper. Per-merge, every Stage-A PR carried a receipt of roughly 30–90 lines. Bytes were not computed separately from lines; classification is my judgment call and is stated so results are reproducible.

## Honest limits and the missing instrumentation

Not computable from this archive: **agent or human wall-clock time, token/dollar cost of any receipt, packet, or triage** (no run carries token counts, though AgentRuns records attribute models); **catch *rate*** in the true sense (catches found / error opportunities — the denominator does not exist); **counterfactual cost of uncaught errors** (what the CRLF register or the unrouted tests would have cost downstream); **completeness of either ledger** — catches are enumerated by grep over self-reported receipts (lower bound), and the bypass ledger depends on disclosure honesty (I found 3 undisclosed manifest gaps in an 11-merge window, so under-reporting demonstrably exists). The forgetting baseline is measured only on surfaces TM chose to scan. A real study would need: token/time telemetry attached to each AgentRuns record and receipt; a defect registry tagging each catch with mechanism, stage caught, and estimated propagation blast radius; retained CI failure logs (GitHub Actions history is outside the archive); and a control period — the repo's own pre-governance early history is the only candidate control and differs in workload.

## Verdict-shaped summary

The archive proves the *forgetting* problem was real and large (29/30 notices unacknowledged, 0/9 findings advanced at source, 91% of first-triage closures resting on pre-existing evidence) and that the register's first session recovered it at a 46/101 closure rate versus the 1/30 baseline, at a marginal cost of ~30% of changed lines in the one instrumented session. Twelve concrete catches are documented against eight recorded bypasses/failures — including three manifest gaps the archive itself never disclosed — so the guards demonstrably work but are not uniformly applied. Whether the ~2.3 governance artifacts per merge pay for themselves overall is **not decidable from this archive**: no time or token cost is recorded anywhere, so the benefit side is enumerable but the cost side is not.
