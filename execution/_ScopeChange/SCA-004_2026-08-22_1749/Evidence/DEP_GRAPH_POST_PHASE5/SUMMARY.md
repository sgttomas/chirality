# Graph derivation summary

- Result: `PASS_PHASE3_SHAPE_EXACT_MATCH`.
- Node set: exact equality with 53 applied register rows plus six packages.
- Package-membership edges: 53, structural and non-gating.
- Authoritative local declarations: 16 rows across eight current `_DEPENDENCIES.md` files.
- Unique Root relationships: nine (eight gating, one non-gating).
- Cross-loop notice/fan-in edges: two, non-gating and non-authoritative.
- SCCs: 59 singleton, zero non-trivial.
- Phase-3 comparison: node/edge/gating/notice/SCC shape exact; deviations zero.
- Human-gated cut/merge required: no.
- All seven initialized-empty warnings remain cleared; 45 legacy containers remain `NOT_RUN_YET`.
- Accepted estimates and sealed schedule are context only and did not alter dependency truth.
- Status: immutable derivative evidence; rerun triggers are recorded in `Decision_Log.md`.
