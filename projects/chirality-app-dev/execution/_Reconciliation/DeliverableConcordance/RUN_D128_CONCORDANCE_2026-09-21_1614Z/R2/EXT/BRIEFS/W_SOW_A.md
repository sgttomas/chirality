# EXT worker brief — item 5, scope ledger half A (`SOW`, SOW-001..SOW-042)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and follow it; it binds this brief.

- **Folder (only write target):** `<RUN>/R2/EXT/SOW_A/`.
- **Outputs:** `SOW_claims.csv`, `SOW_notes.md`, then `RETURN.md`. The manager merges
  the two halves by script; do not read the other half's folder.
- **Units:** the 42 units SOW-001..SOW-042, listed in `<RUN>/R2/EXT/_inputs/EXTENSION_INDEX_SOW_A.csv`
  (a filtered copy of the Item 5 rows of `EXTENSION_INDEX.csv`). Source: the rows of
  `## 9. Scope Ledger` in
  `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
  ClaimKey = unit key (`SOW:SOW-007`); ClaimID = `SOW-007`; split rows `SOW:SOW-007.1`.
  **Run-local keys in this half are numbered 1–49 only** (`SOW:REGISTER-n`, `SOW:STATE-n`)
  so the merge cannot collide. PackageID `EXT`; DeliverableID = the owning live deliverable
  when one is evident, else `NONE`.
- **Validate with the half index:**
  `python3 <RUN>/_scripts/validate_ledger.py ledger --extension-index <RUN>/R2/EXT/_inputs/EXTENSION_INDEX_SOW_A.csv <RUN>/R2/EXT/SOW_A/SOW_claims.csv`
- **Audit question (two parts):** does the row map to at least one *live* deliverable, and to
  code or an explicit deferral?
  - Mapping to a live deliverable is judged from the decomposition text (its deliverable
    tables and trace columns) and the deliverables' `ScopeOfWork.md` / `_STATUS.md` in
    the frozen tree (`projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/`), which
    you may read. `<RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv` lists the 54 deliverables
    and their lifecycle (DEL-09-07 is retired/OPEN). A retired deliverable is not live.
  - "Code" = App `frontend/**` or runtime `packages/**` at the frozen basis, with REACH tags
    from `EVIDENCE_PACK/REACHABILITY.csv`. "Explicit deferral" = a GOVERNING ruling or
    deliverable text that explicitly defers or excludes it (cite it).
  - Split `.1` (live-deliverable mapping) and `.2` (code or explicit deferral) **when they
    disposition differently**; otherwise one row. An `OUT` row is a boundary trace:
    `ALIGNED` when no live deliverable implements it (`ClaimType = EXCLUSION`).
  - IN rows: `ClaimType = REQUIREMENT`; tier `LOCAL_DESIGN` unless the row restates
    PRD/CONTRACT/SPEC etc.
- **For the manager's summary**, put in Notes: `NO_LIVE_DELIVERABLE` on every row that maps to
  no live deliverable, and `NO_CODE_NO_DEFERRAL` on every IN row with neither code nor an
  explicit deferral.
