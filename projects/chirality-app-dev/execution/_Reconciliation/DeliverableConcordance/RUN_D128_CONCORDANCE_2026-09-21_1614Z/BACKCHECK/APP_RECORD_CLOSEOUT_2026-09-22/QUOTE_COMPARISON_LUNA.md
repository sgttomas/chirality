# Independent dependency quote comparison — Luna

Task: independently compare the 36 still-unmatched dependency rows against their current cited source files. This is comparison evidence only; no register, Scope of Work, status, or authority-source files were edited.

The original census contains 149 rows. The parent applied 113 source-faithful quote repairs before this final pass (56 PKG-00–03, 23 supported PKG-04–06, and 34 PKG-07–10 safe-preview rows). This file covers only the 36 rows still unresolved: 13 PKG-04–06 semantic mismatches and 23 PKG-07–10 uncovered rows. The CSV retains each selected row’s complete original fields, canonical original row preimage and SHA-256, current live register row preimage and SHA-256, the original source hash, and the current source hash.

The current source bytes for all 14 distinct files cited by these 36 rows match the census `SourceSHA256` values (0 differences). All 36 original `EvidenceQuote` values are unmatched literally in their current resolved source. The CSV supplies 17 verified exact current-source quote candidates; 19 rows have no safe quote-only repair because their Statement, source target, ownership, or source text is semantically mismatched or internally conflicting. Proposed status and satisfaction are copied unchanged from the original census for every row.

## Exact remaining rows

PKG-04–06 semantic mismatch (13):

DEP-04-04-013, DEP-04-04-014, DEP-05-02-006, DEP-05-02-016, DEP-05-03-009, DEP-05-04-003, DEP-06-03-006, DEP-06-03-007, DEP-06-03-008, DEP-06-03-010, DEP-06-03-014, DEP-06-03-015, DEP-06-03-016

PKG-07–10 not covered by the applied safe preview (23):

DEP-07-01-010, DEP-08-01-013, DEP-08-01-018, DEP-08-01-019, DEP-08-01-021, DEP-08-03-006, DEP-08-03-008, DEP-08-03-009, DEP-08-04-002, DEP-08-04-003, DEP-08-04-004, DEP-08-04-006, DEP-08-04-013, DEP-08-05-005, DEP-08-05-006, DEP-08-05-008, DEP-09-05-004, DEP-09-05-008, DEP-09-05-009, DEP-09-05-010, DEP-09-05-011, DEP-09-05-013, DEP-09-05-014

The semantic findings are recorded per row in `ComparisonAssessment`, `ComparisonRationale`, and `CurrentSourceExcerpt`. Specific issues include obsolete SDK/HarnessEvent or fixed-Pipeline wording, target ownership claims not established by current sources, statements that exceed current status evidence, and one conflicting workflow-path statement inside DEL-09-05 itself (CLM-004 L82 names `.github/workflows/harness-premerge.yml`; CLM-020 L351 says keep the path TBD). Those cases remain for manager review rather than quote-only application.

## APP-HOLD-1 reliance preflight

Ran from the App working root with the exact operation and entry path below, one invocation covering all 54 current `PKG-*/1_Working/DEL-*` targets. Result: exit 0, `verdict: ALLOW`, `active_hold_deliverables: []`, `scan_held_deliverables: []`, `structural_bootstrap_deliverables: []`. Register SHA-256: `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`. Scan fingerprint SHA-256: `e4197287316e62db84950ccbc46de95bcd9866afb36894023b400e0fe4fa7be1`. Preflight-reported HEAD: `0fb42b36df5c93c34c02e209670f3cede937ce84`.

```text
python3 execution/_Scripts/app_hold.py check --operation reliance --entry-path TASK/dependency_quote_comparison_luna/APP_RECORD_CLOSEOUT_2026-09-22 --target DEL-00-01 --target DEL-00-02 --target DEL-01-01 --target DEL-01-02 --target DEL-01-03 --target DEL-01-04 --target DEL-02-01 --target DEL-02-02 --target DEL-02-03 --target DEL-02-04 --target DEL-02-05 --target DEL-03-01 --target DEL-03-02 --target DEL-03-03 --target DEL-03-04 --target DEL-04-01 --target DEL-04-02 --target DEL-04-03 --target DEL-04-04 --target DEL-04-05 --target DEL-05-01 --target DEL-05-02 --target DEL-05-03 --target DEL-05-04 --target DEL-05-05 --target DEL-06-01 --target DEL-06-02 --target DEL-06-03 --target DEL-06-04 --target DEL-06-05 --target DEL-06-06 --target DEL-07-01 --target DEL-07-02 --target DEL-07-03 --target DEL-07-04 --target DEL-07-05 --target DEL-07-06 --target DEL-08-01 --target DEL-08-02 --target DEL-08-03 --target DEL-08-04 --target DEL-08-05 --target DEL-09-01 --target DEL-09-02 --target DEL-09-03 --target DEL-09-04 --target DEL-09-05 --target DEL-09-06 --target DEL-09-07 --target DEL-10-01 --target DEL-10-02 --target DEL-10-03 --target DEL-10-04 --target DEL-10-05
```

## Basis and hashes

Branch: `codex/app-reconciliation-closeout-20260922`; current checkout HEAD when this report was written: `0fb42b36df5c93c34c02e209670f3cede937ce84`. Census file SHA-256: `c269c71db0fb21564c29a6f5fbaa896a77c34eeadb19b1502c6805d165b2bdc0`. Output SHA-256 is intentionally not self-recorded here; recompute after receipt.

Loaded instruction files and SHA-256:

- `AGENTS.md` — `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`
- `agents/AGENT_TASK.md` — `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/chirality-app-dev/AGENTS.md` — `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f`
- `projects/chirality-app-dev/instructions/AGENTS.md` — `12b2c01c7e960bc35ef7bf55d2a968687bef776826f12edfea8b8fdbc778e3de`


The CSV’s `OriginalRowSHA256` and `CurrentRegisterRowSHA256` hash the canonical UTF-8 JSON form preserving source field order. `CurrentCandidateSourceSHA256` hashes the source file from which the excerpt or semantic review context was read. Literal candidates were checked as exact source substrings before being written as ProposedEvidenceQuote.
