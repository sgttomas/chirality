# Brief D1P — D1 derivative premise review: DEL-00-01 ADRs and DEL-00-03 SPEC (provisional D-PEC-105) — WORKING_ITEMS preparation

- **Parent:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1.
- **Role:** WORKING_ITEMS (Type 1).
- **Branch:** `claude/pec-d1-premise-proposal`.
- **Prep folder:** `projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-27/` (use the actual date).

Read `COMMON.md` beside this brief. It applies here with the overrides below.

## What D1 is

Two accepted derivative artifacts carry premises that later scope changes made stale. Both deliverables are `CHECKING`. They change only through their owning deliverable workflow, under an exact-byte gate, by an owner-ruled packet. D1 prepares that packet as **premise-only amendments**: the accepted bytes remain history, and no other content is revised.

**Sources that bind the scope:**
- SCA-005 `Propagation_Plan.md` §B5, and its rows at L50, L828–829 and L873–876 (`_ScopeChange/SCA-005_2026-09-23_2139/`):
  - DEL-00-01 `artifacts/v2/ADRs.md`: the runtime-ownership premise (D-GOV-20 → D-GOV-43 A2, ADR carried posture 3), and the daemon and cmux mentions (cmux deferred out of scope, SCA-005 amendment 1).
  - DEL-00-03 `artifacts/v2/SPEC.md`: §4 information model, the §6 PKG-07 row, §8 open decisions, and the daemon and cmux mentions.
- SCA-006 `Propagation_Plan.md` §B5, and its rows at L89, L307 and L313 (`_ScopeChange/SCA-006_2026-09-25_1912/`), for DEL-00-03 `SPEC.md` (`cc9f4754…1bae`):
  - the K-03 row L46;
  - requirement counts L23 and L62 (46 → 49);
  - the API row L73 (response budgets and the tool-call surface);
  - the release-proof list.
- **DEL-00-03 `ScopeOfWork.md`:** its CLM-004 (L70) and CLM-006 (L77), the "46 requirements" premise, now 49. This is premise only, at review level.
- **Anything else the owning workflow's own review finds** that is a premise made false by SCA-005 or SCA-006, reported with evidence. Keep D1 to premises; list other findings for later.

## Overrides of COMMON.md

- **Lifecycle.** Both targets are `CHECKING`. That does **not** stop this packet. The graph routes these amendments through an owner-ruled exact-byte packet. It **does** mean:
  - no lifecycle change is proposed or implied;
  - nothing asks the owner about CHECKING;
  - you touch only the named artifacts and, if needed, DEL-00-03's `ScopeOfWork.md`, each with exact pre- and postimages.
- **Owning workflow.** Identify the workflow that owns each artifact from the deliverable's records (`_REVIEW.md`, `_run_records/`, `MEMORY.md` if any, and the decisions that accepted the bytes, such as `D-PEC-90` and the 2026-08-09 re-acceptances). Record its identity and hashes, and follow its amendment and verification discipline.
- **Owner-acceptance records.**
  - DEL-00-03's `_REVIEW.md` records an owner `ACCEPT_EXACT_BYTES`. It says any byte change invalidates the acceptance and requires a REVIEW rerun.
  - Check DEL-00-01's records too.
  - The packet must say plainly which acceptances lapse and what re-review it proposes. Offer the REVIEW rerun, or an exact owner re-acceptance of the new bytes, as an explicit owner option; do not assume it. The S4 packet (`D-PEC-102`, `_DECISIONS/D-PEC-102_*` once published, and prep `PEC_SOW_CURRENCY_S4_PREP_2026-09-26/`) shows the disclosure form.
- **External anchors.** Any `Dependencies.csv` `EvidenceQuote`, and any other contract quotation of ADR, SPEC or DEL-00-03 SOW text, that stops being verbatim must be listed.
- **Precedents:**
  - `D-PEC-90` (it pinned the SPEC);
  - the 2026-08-09 SPEC re-acceptance (commits `8f02609b5` and `e92a82ca9`, `PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/`);
  - `D-PEC-100` for act-script rigour.
- **Add-on M:** offer it only if the deliverables' records support it.

## Return

Everything COMMON.md lists, plus:
- the owning-workflow identity;
- the premise inventory with its evidence;
- the acceptance-lapse account;
- the proposed re-review option.
