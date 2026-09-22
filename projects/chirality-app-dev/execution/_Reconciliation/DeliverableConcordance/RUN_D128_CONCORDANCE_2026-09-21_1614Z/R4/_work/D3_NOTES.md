# D3 notes — R4 packets P-09, P-07, P-13, P-14, P-15, P-11 (RUN_D128)

TASK D3 (Type 2), dispatched by the R4 packet manager. Drafts only; no rulings. Resumed once after a
server-side interruption (nothing had been written before it).

## Method
- Read the common and D3 briefs; CONVENTIONS §1, §2.4, §2.6, §4; RUN_BASIS §5 and Addenda 6–13; owner
  direction; R3_SUMMARY §8; CLUSTERS CL-07/09/11/13/14/15; RUNWIDE_CALLS (a), (d), (e); R3_SPOT_CHECK;
  T8B/T8C notes; CROSS_PACKAGE_FINDINGS XPF-042..044; fact sheets P-07/09/11/13/14/15.
- CSVs read only through `r4lib`/`r3lib` (`_work/D3_scripts/`):
  - `d3_p09.py`: P-09 reach mix, mixed-evidence count effect, held rows;
  - `d3_reach.py`: rows whose R4-Q1 depends on the symbol-level reach reading (call (a));
  - `d3_p09_subq.py`: writes `SUBQ/P-09_subq.csv` (a 161, b 136, c 333);
  - `d3_subq_small.py`: writes `SUBQ/P-15_subq.csv` (a 21, b 7) and `SUBQ/P-11_subq.csv` (a 11, b 5, c 2, d 3, e 5).
- Frozen-tree checks (read-only): the SPEC/CONTRACT/PRD Codex-only basis (`:15`), SPEC §15.2 (`:847-860`), CONTRACT
  K-GATE-1/K-ROOT-2/K-HOOK-1/K-PATH-2/K-STATUS-2/K-DOMAIN-2 lines, D-GOV-43 record and proposal item 4, `runtime-service.ts:580,619-624`,
  `app-owned-composition.ts:225-226`, `codex-supervisor.ts:107`, `delegated.ts:318-330`, the legacy tool schema `read-tools.ts:1125-1136`,
  the transition route `:52-62`, `woven-dialogue-route.tsx:18`, D-APP-13 ruling `:24-26`, D-APP-56 ruling `:60`, SPEC §17.6, PRD FR-008,
  decomposition v3_2 `:336`, `git show --stat 39c0bb6ab`, `git log -1 0ed1a1a7f`.

## Things the manager must know
- **428 vs 410.** At the final concordance, 410 rows run-wide cite R4-Q1 and carry both REACH=LIVE and REACH=LEGACY_ONLY
  (602 rows carry both tags regardless of R4-Q1). R3_SUMMARY §8's "428" was computed at an earlier build. P-09 uses 333 PRIMARY
  (316 would drop to HDN NO under whole-claim reading; 17 keep D-APP-73/116..119/R4 tokens).
- **P-09 SUBQ a/b is a keyword triage** (rule in the script docstring). It is deliberately coarse. Rows may move between a and b on review.
- **The "Claude/Anthropic default" statement (ED)** belongs to P-04. All 11 AUTHORITY_CONFLICT rows are PRIMARY in P-04; the
  STALE_SPECIFICATION half is in P-20 (7) and P-09 (5) (the other 11 are outside my packets). This is stated in P-11 and P-09.
- **S2-047 and S2-059** are PRIMARY in P-09, not P-11. They are listed in P-09 risks and noted in P-11.
- **The four "missing R4-Q6" rows** from T8C: three are Full access (`DEL-07-01#CLM-011.4`, `#CLM-011.6`, `DEL-06-05#CLM-024`), and one
  is DIRECTIVE §2.8 (`DEL-04-05#CLM-024`). All are P-09 PRIMARY, SubQ c/c/c/a.
- **P-09 length.** About 1,270 words with header and paths. The largest packet; above the ~900 target.
- **P-15.b** (DEL-09-01, DEL-09-06) sits in CL-15 by the cluster rule, but its key-storage rows depend on P-04.
- Cross-packet dependencies:
  - P-07 ↔ P-14 (same actor mechanism);
  - P-09.b ↔ P-13 (hooks, instruction root);
  - P-04 → P-09 (Full access and §2.8 rows), P-13, P-15.b, P-11.d;
  - P-10 → P-09 (D-APP-73 rows);
  - P-06 → P-14 (retired Pipeline surface).
