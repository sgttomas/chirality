# EXT worker brief — item 3, decision-effect audit (`DEC`)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and follow it; it binds this brief.

- **Folder (only write target):** `<RUN>/R2/EXT/DEC/`.
- **Outputs:** `DEC_claims.csv`, `DEC_notes.md`, then `RETURN.md`.
- **Units:** the 38 `Item = 3` rows of `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv`
  (`DEC:D-APP-86` .. `DEC:D-APP-127`, RULED only; D-APP-116..119 are not units). Every unit
  gets at least one row. ClaimKey = unit key; ClaimID = `D-APP-nn`; PackageID `EXT`;
  DeliverableID = the owning deliverable when one is evident, else `NONE`. Run-local rows:
  `DEC:STATE-n`, `DEC:REGISTER-n`.
- **Audit question:** did the ruling's stated effect land in code or corpus at the frozen
  basis? Per unit: read the register row in
  `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`
  and its ruling record in the same folder; then find where the stated effect should appear
  (code, deliverable text, or the deliverable's `_STATUS.md`).
  - You **may** read any deliverable folder under
    `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-*/1_Working/`, read-only, because
    that is where the effect lands. Use `EVIDENCE_PACK/DECISION_HITS.csv` to find which
    deliverables cite each decision.
  - For D-APP-127 use `EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv` (per deliverable and
    carrier: YES / PARTIAL / NO / ABSENT); summarise it, do not re-derive it.
  - **Flagged rows** (RUN_BASIS §5 "GOVERNING, flagged": D-APP-104, 107, 121, 122, 123, 125,
    126, some superseded in part by D-APP-127) are judged against their recorded flag
    (effect pending, held or unapplied), **not treated as landed**. Say in Notes which flag
    applies and whether the recorded pending/held state is itself accurate.
- **Column guidance (CONVENTIONS §8):** `ClaimType = REQUIREMENT` for the ruling's stated
  effect; `LatestDecision` = the ruling itself (or a later superseding ruling where one
  governs); `ALIGNED` when the effect landed; `DOCUMENTED_UNIMPLEMENTED` /
  `PARTIALLY_IMPLEMENTED` when it did not; `RETIRED_BY_RULING` or `ACCEPTED_DIVERGENCE` when a
  later ruling superseded it. Split `.n` only when a ruling states separately numbered
  effects that disposition differently (e.g. a ruling with items A–D where some landed and
  some did not); name the item in Notes. `AuthorityTier`: `GOVERNANCE_INVARIANT` when the
  effect restates DIRECTIVE/CONTRACT/SPEC/TYPES or a D-GOV rule, `PRD` when the highest
  source is PRD, else `LOCAL_DESIGN`.
- **For the manager's summary**, put `EFFECT_NOT_LANDED:<short what>` in Notes on every row
  whose ruled effect did not (fully) land at the frozen basis, flagged rows included.
- Context budget: 38 rulings is a lot. Read each ruling's decision/effect section, not the
  whole packet; grep the register row by ID; keep per-row evidence to the strongest 1–3
  citations.
