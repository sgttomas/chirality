# RETURN — W_DOC_DEV_R1 (item 7 rerun, DOC-ADDING_A_TOOL)

- **Ledger:** `DOC-ADDING_A_TOOL_claims.csv` has 8 rows, one for each index unit (#0–#7). No splits, no SEE rows, no errata.
- **Dispositions:**

  | Disposition | Count | Rows |
  |---|---|---|
  | IMPLEMENTED_DIFFERENTLY | 3 | #1, #3, #6 |
  | ALIGNED | 2 | #2, #7 |
  | DOCUMENTED_UNIMPLEMENTED | 2 | #4, #5 |
  | STALE_SPECIFICATION | 1 | #0 |
  | ACCEPTED_DIVERGENCE | 0 | — |

  No row is ACCEPTED_DIVERGENCE because the D-GOV-43 banner is the document's own note, not a ruling.
- **HumanDecisionNeeded:** 5 rows cite `R4-Q1` (#1, #3–#6). The other 3 are `NO`.
- **Validator:** `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
- **SHA-256 (sealed):** `655604ed7d20dc6c00070e1fd6f13340b644f1c225fe4851e0973890de9c8f26`
- **Notes:** `DOC-ADDING_A_TOOL_notes.md`

## For the manager

1. **#0 stale paths.** The Primary sources list names `frontend/src/lib/harness/tool-descriptor.ts` and `mcp/tool-names.ts`. Neither file exists: they were removed under D-APP-47 (`ee290e22a`, 2026-07-04), and the registry now lives in `@chirality/runtime-contracts`. The same stale paths appear in step 1–2 of #1 and are recorded there as `ALSO_MODULE:STALE_SPECIFICATION`.
2. **#4 module finding.** The coordination MCP tools have `mutating` descriptors but do not go through the handler-level permission/evidence wrapper that the guide requires for every mutating MCP tool. This is recorded as `ALSO_MODULE:PARTIALLY_IMPLEMENTED`. Whether this counts as a K-MCP-1 bypass is open, because the guide's test is about project state and these tools write control-plane records.
3. **#4 post-release basis.** `PostReleaseBasis=YES` because the row cites the daemon application-tools registry, which was touched by `da95ec194`.
4. **No `OTHER:` CauseTags.**
