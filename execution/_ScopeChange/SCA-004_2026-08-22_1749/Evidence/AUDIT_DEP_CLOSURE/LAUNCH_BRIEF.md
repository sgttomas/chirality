# Sealed brief — AUDIT_DEP_CLOSURE for SCA-004 Gate-1 graph

- Parent: SCOPE_CHANGE, SCA-004 Gate 1.
- Agent role: dedicated Agent 2 `AUDIT_DEP_CLOSURE` approved by D-GOV-13.
- One objective: independently audit
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/WORK_GRAPH.json` for parse
  validity, endpoint resolution, edge semantics, SCC completeness, strict-layer
  acyclicity, cycle-edge gating, and cross-loop notice-only treatment.
- Accepted repository basis:
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.
- Read scope:
  - this brief;
  - `agents/AGENT_AUDIT_DEP_CLOSURE.md`;
  - `AGENTS.md` cycle-resolution rule;
  - `docs/CYCLE_DRIVEN_RESOLUTION.md`;
  - the SCA `WORK_GRAPH.json` and `DAG.md`;
  - node paths named in `WORK_GRAPH.json`, existence checks only.
- Write scope: only
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE/RETURN.md`
  and `Decision_Log.md` in the same folder.
- Human-authorized output override: the owner expressly requires the audit
  return inside the SCA folder and prohibits `execution/_Evaluation/**` and
  pointer writes for this tranche. This narrower write fence overrides the
  dedicated agent's default tool-root output contract. No default snapshot or
  `_LATEST.md` may be created or updated.
- Tools: read-only shell/file inspection; no network; no mutation outside the
  two output files.
- No delegation: as Agent 2, do not spawn or delegate.
- Required return:
  - exact graph SHA-256;
  - `PASS`, `WARNING`, or `BLOCKER` verdict;
  - JSON parse result;
  - node endpoint-resolution counts and failures;
  - strict/candidate edge counts;
  - independently computed SCC inventory and comparison with declared SCCs;
  - confirmation that every unresolved cycle edge is non-gating;
  - confirmation that App edges are notice-only and have no foreign path;
  - findings and repair recommendation.
- Acceptance: no BLOCKER; every claim evidence-cited; outputs remain within
  the override path; no delegation and no deliverable mutation.
