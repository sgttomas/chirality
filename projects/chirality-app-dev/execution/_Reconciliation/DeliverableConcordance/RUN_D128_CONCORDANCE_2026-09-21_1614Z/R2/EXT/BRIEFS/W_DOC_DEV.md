# EXT worker brief — items 6 and 7, product guidance and harness developer docs (audit-only)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and follow it; it binds this brief.

- **Folder (only write target):** `<RUN>/R2/EXT/DOC_DEV/`.
- **Outputs**, one ledger + notes per DOCID, then `RETURN.md`:
  - item 6: `DOC-PRODAGENTS_claims.csv` / `_notes.md` (9 units, source
    `projects/chirality-app-dev/instructions/AGENTS.md`);
  - item 7 (sources under `projects/chirality-app-dev/frontend/docs/harness/`):
    `DOC-ADDING_A_TOOL` (8, `adding_a_tool.md`), `DOC-README` (7, `README.md`),
    `DOC-RUNTIME_ENGINE_CONTRACT` (11, `runtime_engine_contract.md`), `DOC-TOOL_CATALOG`
    (4, `tool_catalog.md`), `DOC-TRACEABILITY` (2, `TRACEABILITY.md`).
- **Units:** the `Item = 6` and `Item = 7` rows of `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv`.
  `<n>` is the 1-based `##`/`###` heading ordinal (ignoring fenced code); `#0` is the
  preamble. ClaimKey = unit key (e.g. `DOC:README#3`); ClaimID = `README#3`; split rows
  `DOC:README#3.1`; run-local `DOC:README#STATE-n`. PackageID `EXT`; DeliverableID = the
  owning deliverable when evident, else `NONE`.
- **Audit questions:** item 6 — is the section accurate about product behavior (what the App
  actually does at the frozen basis)? Item 7 — is the developer documentation accurate
  (files, APIs, tools, flows it describes exist and behave as described)?
  - Evidence: App `frontend/**`, runtime `packages/**`/`tests/**`, REACH tags from
    `EVIDENCE_PACK/REACHABILITY.csv`, `<RUN>/R2/SURFACES/*_capabilities.csv` (HARNESS,
    INSTRUCTIONS, RTCORE, RTCONTRACT, …) and `<RUN>/GATE_TRANSCRIPTS/`.
  - Item 6 is packaged product content (Root-owned guidance packaged by the App, Δ10). Judge
    only its accuracy about product behavior; it is not governing.
  - Docs describing the in-process harness: apply the Addendum 6 subject test. A developer
    doc that describes a specific module's own contract is a module-level claim (judge at
    module level with the REACH tag); a doc stating what the product does is a
    product-behaviour claim judged on the live path. R4-Q1 by rule 3 and the mixed-row
    reading.
- **Audit-only (CONVENTIONS §8):** record the accuracy finding with the normal Disposition,
  and on **every non-ALIGNED row** begin `RemainingWork` with `AUDIT-ONLY`; item 6 rows
  additionally carry `ROUTE:ROOT (Δ10)` right after it (e.g.
  `AUDIT-ONLY ROUTE:ROOT (Δ10) — <residual>`). Nothing is repaired by this run.
- **Column guidance:** tier by the source the section restates; sections restating nothing
  normative are `STATE_ASSERTION` with `NOT_APPLICABLE`, or `CONTEXT_CLAIM` (then only
  `STALE_SPECIFICATION` or `NOT_AUDITABLE`).
