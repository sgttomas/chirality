# SCOPE_CHANGE_INIT Seed: PKG00-SCA-PACKET-004

This seed is not valid until a human explicitly initiates SCOPE_CHANGE. It is a prepared intake draft for SCC-001 tooling permissions MCP concerns.

## Requested Intake

Initiate SCOPE_CHANGE review for SCC-001 packet `PKG00-SCA-PACKET-004`, focused on PKG-06 permission overlay, SDK read tool surface, Chirality MCP read tools, write/edit path hooks, and hook lifecycle/compaction mirror integration.

## Proposed Scope

- Affected deliverables: `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`, `DEL-06-06`.
- Evidence baseline: DepClosure snapshot `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431`.
- Decomposition baseline: `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Focus rows: TBD.

## Initial Questions For SCOPE_CHANGE

1. Which packet-relevant SCC-001 pairs require dependency classification only, and which require decomposition or handoff clarification?
2. Should DEL-06-01 remain the sole permission-policy owner while DEL-06-02 and DEL-06-03 own read-tool exposure and MCP metadata?
3. What is the accepted event writer/session JSONL append API owner for permission, MCP, hook, and compaction events?
4. What exact boundary separates DEL-06-04 path/write enforcement from DEL-06-06 lifecycle and compaction mirroring?
5. What ruling governs PRD-derived details while REF-006 remains hash-mismatched?

## Requested Outputs If Initiated

- Human-approved SCOPE_CHANGE brief.
- Evidence-grounded amendment or no-amendment decisions.
- Any authorized dependency-register or decomposition changes in the owning workflow only.
- New snapshot or handoff state if governed state changes.
