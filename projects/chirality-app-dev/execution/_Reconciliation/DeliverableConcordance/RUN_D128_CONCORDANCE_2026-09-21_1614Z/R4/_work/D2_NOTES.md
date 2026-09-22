# D2 notes — R4 packets P-04, P-05, P-08, P-10, P-12, P-16 (RUN_D128)

TASK D2 (Type 2). Drafts only; no rulings. Interrupted once by an API overload and resumed; the only artifacts from before the interruption were `D2_scripts/d2_q6_pop.py` and its output.

## Method
- Read the common brief, the D2 brief, CONVENTIONS §1, §2.4, §2.6 and §4, RUN_BASIS §5 and Addenda 1–13, OWNER_DIRECTION, R3_SUMMARY §8, the six CLUSTERS sections, RUNWIDE_CALLS (d) and (g), R3_SPOT_CHECK, T1_NOTES, XPF-013/036/041/045, and the six fact sheets.
- Rows were read only through `r4lib` / `r3lib` (`D2_scripts/d2_dump.py`).
- Verified against the frozen tree:
  - the clause texts: CONTRACT :15-17, :62, :64, :78, :83, :90, :95; DIRECTIVE :115, :144, :227, :250, :320; SPEC :673-680;
  - D-GOV-43 ruling and proposal items 1–12;
  - Runtime `delegated-engine-adapter.ts:282,289`, `session-store.ts:112,170,813-822`, `bootstrap-project.ts:43-53`, `project-registry.ts:225-233`, `codex-app-server-client.ts:44-70`;
  - App `run-logger.ts:95`, `engine-conformance.test.ts:208,270` and `preload.ts:77`;
  - register rows 132–152.

## Scripts and outputs
- `D2_scripts/d2_q6_pop.py` writes `SUBQ/P-04_subq.csv` (86 rows: a 78, b 8) and `D2_scripts/q6_sets.txt`.
  - **Rule.** A row is **a** if its NormativeSource or Notes name DIRECTIVE 2.8/2.10/4.1/4.2, K-PERM-1/6, "Full access" or the API key. A row whose Notes point by key to an a-row is also a. Every other row is **b**.
  - An earlier pass that also searched ImplementationEvidence gave 75/11. Dropping ImplementationEvidence without following references gave 66/20. The final rule is the one above.
  - K-NET-1 rows `DEL-01-04#CLM-006.1` and `#CLM-010.2`, and K-PERM-4/5 rows `DEL-06-01#CLM-009.5` and `.6`, land in **a** through cross-references. T1 read them as broad-only. The owner can move them.
- **Broad-reading population.** The adjacent list is transcribed from `RUNWIDE_CALLS.md` (d), with ranges expanded: 61 keys, all present. 2 are already in P-04 and 59 are outside it (P-09 56, P-20 3), including 3 of the 4 Full-access rows. `DEL-04-05#CLM-024` is the fourth.
  - Narrow = 78 + 4 = **82**.
  - Broad = 86 + 59 + 1 = **146**.
  - The 23 ED "text out of date" rows (P-20 18, P-09 5) are left out of both counts.
- `D2_scripts/d2_p10_subq.py` writes `SUBQ/P-10_subq.csv` (a 8, b 5, c 5).
  - **Rule.** A row is **a** if its HDN names D-APP-116..119. Otherwise it is **b** if its HDN names D-APP-127 or D-GOV-43. Every other row is **c**.
  - Across the concordance, 18 rows name D-APP-116..119: 8 in P-10, 9 in P-09 and 1 in P-05. The 10 outside P-10 are listed in P-10 "On ruling".

## For the manager
- **The R3 "about 13 T1 rows" figure is not reproduced.** The scripted split replaces it: 8 broad-only rows are inside P-04. The broad reading adds rows from other packets, not from P-04.
- **P-04 is about 1,250 words,** over the soft limit. That is the cost of the four confirmation items and the population table.
- **Cross-packet effects:**
  - P-09 must carry R4-Q6 for the 4 Full-access rows (and for 56 adjacent rows under the broad reading).
  - Under P-04 Option A, the 8 b-rows would move to P-11.
  - P-16's ALSO row `DEL-05-01#CLM-010.3` is PRIMARY in P-09, and its answer should match P-16's.
  - P-12 depends on P-05. P-08 depends on P-05.
- **Runtime code.** The code options in P-08, P-12 and P-16 touch Runtime packages, which are outside the App run's write scope. The packets route those briefs to the Runtime loop.
- **Register.** The next free D-APP ID in the working register is D-APP-130. The packets say "next free D-APP ID".
