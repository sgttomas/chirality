# D-PEC-65 — per-package fan-in records (consolidated), 2026-07-25

Dispatcher fan-in per packet §3.3. One consolidated file, eleven sections
(§3.3 contemplated per-package files; consolidation noted as a deviation of
form, not substance — every per-package check below was run at that package's
fan-in, before the next dispatch was released). Fan-in commands per package:
whole-corpus `validate_decomposition_registers.py --json` filtered by path
prefix; `check_verbatim_quotes.py <root> PKG-NN`; `git status --porcelain`
scoped to the package vs `porcelain_baseline_dispatch.txt`.

| PKG | Baseline findings | EXEC rows | REPAIRED | WAIVED | BLOCKED | Post-repair findings (pkg) | Verbatim | Fence | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| PKG-00 | 1 | 1 | 1 | 0 | 0 | 0 | 1/1 | exact | PASS |
| PKG-01 | 3 | 2 | 2 | 0 | 0 | 0 | 2/2 | exact | PASS |
| PKG-02 | 7 | 7 | 7 | 0 | 0 | 0 | 7/7 | exact | PASS |
| PKG-03 | 24 | 17 | 17 | 0 | 0 | 0 | 17/17 | exact | PASS¹ |
| PKG-04 | 14 | 9 | 9 | 0 | 0 | 0 | 9/9 | exact | PASS |
| PKG-05 | 6 | 4 | 4 | 0 | 0 | 0 | 4/4 | exact | PASS |
| PKG-06 | 17 | 11 | 11 | 0 | 0 | 0 | 11/11 | exact | PASS |
| PKG-07 | 17 | 12 | 11 | 1 | 0 | 0 ERROR + 2 waiver WARNING | 11/11 (+1 waived-empty) | exact | PASS² |
| PKG-08 | 14 | 9 | 9 | 0 | 0 | 0 | 9/9 | exact | PASS |
| PKG-09 | 31 | 29 | 29 | 0 | 0 | 0 | 29/29 | exact | PASS |
| PKG-10 | 19 | 19 | 19 | 0 | 0 | 0 | 19/19 | exact | PASS |
| **Σ** | **153** | **120** | **119** | **1** | **0** | **0 ERROR / 2 WARNING** | **119/119** | — | — |

¹ PKG-03 return prose said "16 EXECUTION rows"; its own disposition table
lists 17 and the register truth is 17 (11+1+1+1+1+2). Dispatcher-verified
arithmetic slip in the return summary only; all 17 dispositioned.
² PKG-07's waiver (DEP-07-05-004, two rows EVQ-003+EVQ-004) upheld as
truthful at closure refutation; DL-11 counter-evidence verified verbatim.
The waived edge (E-N13, LOW_CONFIDENCE, PROPOSAL, "owner may decline")
carries an owner-routed edge-validity question — surfaced in the closure
report.

## Dispatch-conduct notes

- Repair children were briefed file-tool-only. PKG-01, PKG-02, and PKG-04
  each disclosed one reflexive no-op Bash probe (`echo`) before the bound
  took hold; all were sandbox-rejected or touched nothing, none repeated,
  all disclosed unprompted. Later briefs (PKG-05 onward) preempted the
  probe explicitly; no later child attempted one.
- Grep/Glob were unavailable in child sessions; children enumerated
  registers via `register_findings_before.json` + `Deliverables.csv` +
  the `scaffold_pec.py` sanitize rule, confirmed by direct Read. The
  dispatcher's whole-corpus validator run backstops completeness (64/64).
- Statement edits: **11 total** (flagged in run records) — the dispatcher's
  interim count of 8 was a transcription error caused by heterogeneous
  run-record formats (closure-refutation MIN-5); corrected here. The
  closure refuter verified at cell level against git: 0 unflagged edits,
  0 phantom flags.

## Closure refutation and remediation

Sealed closure refuter (opus-5), 44-row adversarial aptness sample (37%,
≥20%/pkg, worst-first) plus three full-corpus defect-shape scans:
**0 CRIT / 7 MAJ / 6 MIN**. Machine gates, fence, waiver, Statement ledger
all CONFIRMED. MAJ findings = 14 rows whose verbatim quotes did not warrant
their claims (8 ID-tuple quotes in PKG-10; 4 wrong-row loci in PKG-06/09;
1 negation-context excerpt in PKG-08; 1 contradicting pairing) + 1 dropped
owner-routing clause. All dispositioned ACCEPTED; remediated by one fresh
sealed revision dispatch (per §3.3 no-inline-repair) applying the refuter's
named smallest fixes; backchecked by dispatcher gate re-runs recorded in
the closure record.
