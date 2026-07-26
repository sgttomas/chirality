# Decision Log — COV_SCA002_POSTCHANGE_FINAL

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | `SCOPE = ALL` | Matches the pre-change baseline so the pre/post comparison is like-for-like. |
| D-2 | Executed **inline** by the SCOPE_CHANGE Agent 1 instance | Agent 2 dispatch unavailable in this harness; root `AGENTS.md` single-agent fallback. Same substitution recorded at Gate 1. |
| D-3 | Check 9 `SKIPPED` | `DECOMP_VARIANT != DOMAIN`. |
| D-4 | Checks 9b.2/9b.3 at full severity | Companion registers are present, so the protocol's full-severity condition applies. This is what surfaced W-1 pre-change; it now passes. |
| D-5 | §3 `MappedDeliverables` parsed with range expansion | The table uses `DEL-04-01..05` notation; a literal scan undercounts and produces spurious Check-7 blockers. |
| D-6 | **Second pass** run under plan amendment v2.1 | The first pass could not satisfy Check 10 by construction — the artifacts it checks for are written after it. Agent 0 dispositioned a two-pass audit; the interim run is retained, this run is the closure evidence. |
| D-7 | Interim snapshot retained, not deleted | It is immutable evidence of a real run and of the ordering defect that produced the amendment. |
