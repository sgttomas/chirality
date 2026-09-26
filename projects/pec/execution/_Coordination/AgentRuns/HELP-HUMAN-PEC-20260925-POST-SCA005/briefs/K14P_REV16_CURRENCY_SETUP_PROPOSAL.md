# Brief K14P — prepare the revision-1.6 currency and setup packet (provisional D-PEC-101): re-pin (K4) and DEL-08-06 / DEL-10-13 setup with dependency work (K1) (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph nodes K4 and K1. Role: WORKING_ITEMS (Type 1). Methods: the `D-PEC-95` currency method for the re-pin (`_DECISIONS/D-PEC-95_*` and run root `_Coordination/CURRENCY_REV15_D95_2026-09-25/`, generator `gen_d95.py`), and for setup the bundled `project-setup` (with the source-qualified `preparation` skill) and `dependency-extract` workflows resolved from `workflows/index.json` (record identities and hashes). Model steer: `claude-opus-5-5`, high reasoning, for you and every child.

## Why and authority

The owner directed on 2026-09-25 (`D-PEC-94`): "You can continue with all the open work you identified." SCA-006 checkpoint 3 was accepted on 2026-09-26 (`_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`); revision 1.6 is `current_basis`. Its Lane B (`_ScopeChange/SCA-006_2026-09-25_1912/RUN_SUMMARY.md` §6) names B1 (scaffold DEL-08-06 and DEL-10-13), B2 (dependency rows for the new deliverables and the SOW-097..100 anchors; closes audit COV-080), B3 (re-quote DEP-09-06-003 and DEP-10-03-003) and B7 (re-pin 63 `_CONTEXT.md` and 66 `_REFERENCES.md` to revision 1.6 / PRD v2.4). Each needs an owner-ruled packet. You prepare it; you apply nothing. HELP_HUMAN publishes it in `_DECISIONS/` with its register row. The number `D-PEC-101` is provisional.

## Scope

- **K4 (B7):** every deliverable `_CONTEXT.md` and `_REFERENCES.md` pin moves to revision 1.6 and PRD v2.4, reusing the `D-PEC-95` method (generator with pinned preimages, exact postimages, anchor lines only, semantic fields untouched). Recount the targets at current `origin/main` (the plan's 63/66 may be off, as `D-PEC-95` found 42 not 40). Account for the three SCA-006 direct mirrors (DEL-04-03, DEL-08-01, DEL-08-03) that already carry a revision-1.6 successor clause.
- **K1 (B1–B3):** scaffold DEL-08-06 and DEL-10-13 folders (the `D-PEC-93` precedent: `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/`), their `Dependencies.csv` rows and the SOW-097..100 anchors (B2), and refresh DEP-09-06-003 and DEP-10-03-003 EvidenceQuotes (B3). New `_DEPENDENCIES.md` files follow the D-GOV-46 heading schema (Root notice). Their first Scope of Work contracts are node K2, not this packet.
- **Method choice as an owner option.** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` adds `project-setup` `INCREMENTAL` mode for exactly this case, but the owner defers adopting it in PEC. Recommend the route (the `D-PEC-93` precedent, or `INCREMENTAL` with its `SETUP_LOG.md` baseline), and put the choice to the owner; do not assume adoption.
- **Option split.** Offer K4 and K1 as separately rulable parts of one packet (as `D-PEC-95` offered N1–N3), so the owner can take either.
- **Lifecycle.** New folders start `OPEN` per the scaffold; say exactly what `_STATUS.md` bytes result. No existing deliverable's lifecycle changes.
- **Checks to design in:** strict registers — the new rows must not add ERRORs; the 26 pre-existing D-GOV-48 `XRG-013` warnings and 2 DRB-008 warnings are the baseline, and the packet states the exact expected after-output (DRB-008 should clear once the two folders exist); dependency closure (0 SCCs); every ACTIVE EvidenceQuote verbatim; harness and receipt validators; audit COV-080 closure; containment. Say whether a re-audit (`audit-decomp`) is recommended afterwards and put it to the owner.

## Produce (published as a PR; nothing applied)

Own isolated git worktree on branch `claude/pec-rev16-currency-setup-proposal` from fresh `origin/main`. Write only under `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/` plus your return `…/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md` and a copy of this brief under `…/briefs/`:
- `DRAFT_D-PEC-101_rev16_currency_setup_proposal.md` in the D-PEC-95/96/99 format (provenance, findings, options with parts, exact grant with pre/postimage hashes, bound generator(s) with fail-closed semantics, finite verification, independent verifier, administrative grant, rollback, limits, owner questions);
- the generator(s), prototypes' outputs on a scratch export, `SHA256SUMS`.

Prototype only on a `git archive` export. Run `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) with `exact-correction-preparation` on every target. Before returning, dispatch one fresh read-only `pec-reviewer` (opus) to verify the packet (target census, postimage reproduction, quote fidelity, closure, limits); loop until nothing blocks; save verdicts in the prep folder. Commit and push early; open a PR against `main` (commit and PR attribution lines as usual); do not merge. Report, do not repair, any "Update the PR base" failure.

## Limits

No production write: no `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, new deliverable folder, `_STATUS.md`, SOW, register, decomposition, `v2/**`, PRD, `AGENTS.md`, `_DECISIONS/**`, work graph, `docs/**` or foreign path. No action on the D-GOV-48 warnings. No CHECKING, ISSUED or acceptance; do not ask the owner about CHECKING. The human-owned `_COORDINATION.md` Notes line is not yours to edit; you may add it as a separate owner question (the line still says revision 1.5 is `current_basis`; review record `returns/REVIEW_PR954_03.md`).

## Return

PR URL and head; draft path and hash; target census; parts and recommended options; method choice; expected validator outputs; check results; verifier verdicts; owner questions; anything unresolved.
