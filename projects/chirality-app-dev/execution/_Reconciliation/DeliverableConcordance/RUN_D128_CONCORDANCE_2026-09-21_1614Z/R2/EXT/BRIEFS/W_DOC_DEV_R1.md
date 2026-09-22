# EXT worker brief — item 7 rerun, `DOC-ADDING_A_TOOL` (fresh worker)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and `<RUN>/R2/EXT/BRIEFS/W_DOC_DEV.md` and
follow them; they bind this brief. This is a fresh, independent rerun of one ledger under the
R2 rerun rule (RUN_BASIS Addendum 3: > 10% of checked rows refuted on Disposition). Do not
read the earlier attempt (`<RUN>/R2/EXT/DOC_DEV/`) or any `<RUN>/R2/EXT/_verify/` file.

- **Folder (only write target):** `<RUN>/R2/EXT/DOC_DEV_R1/`.
- **Outputs:** `DOC-ADDING_A_TOOL_claims.csv`, `DOC-ADDING_A_TOOL_notes.md`, then `RETURN.md`.
- **Units:** the 8 `DOC:ADDING_A_TOOL#n` rows of `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv`
  (source `projects/chirality-app-dev/frontend/docs/harness/adding_a_tool.md`). Item 7,
  audit-only (`AUDIT-ONLY` first in RemainingWork on every non-ALIGNED row; no `ROUTE:ROOT`,
  which is item 6 only).
- **Rules restated in general terms (apply them to every row):**
  - `ACCEPTED_DIVERGENCE` needs a GOVERNING ruling (RUN_BASIS §5) that permits the specific
    difference. A document's own banner or note that calls its text history or compatibility
    is not a ruling. CONTEXT alone never makes a row ACCEPTED_DIVERGENCE (CONVENTIONS §2.6).
    Where no governing ruling permits it, judge the live path by the normal vocabulary.
  - Addendum 6 subject test and the mixed-row R4-Q1 reading (see `_COMMON_RULES.md`). On
    every product-behaviour row met only by legacy code, `ALSO_MODULE:<verdict>` in Notes is
    mandatory.
  - Named questions now include `R4-Q6` (RUN_BASIS Addendum 9; CONVENTIONS §2.4): whether the
    unamended App DIRECTIVE §2.8/§2.10/§4.1/§4.2 and CONTRACT K-PERM-1/K-PERM-6 still bind the
    Codex-hosted App, or were superseded by D-GOV-43. Cite it instead of plain `R4` when a row
    turns on it. Dispositions follow CONVENTIONS §1 unchanged.
  - Build/validation scripts that are outside `REACHABILITY.csv`: tag by how a product or test
    entry uses them, and say so in Notes.
- Validate from `<APP_WORK>`:
  `python3 <RUN>/_scripts/validate_ledger.py ledger <RUN>/R2/EXT/DOC_DEV_R1/DOC-ADDING_A_TOOL_claims.csv`
  (errors must be zero), record the SHA-256, write `RETURN.md` last.
