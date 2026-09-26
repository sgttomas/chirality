# K14P return — provisional D-PEC-101 (revision-1.6 currency and setup packet)

Role: WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, nodes K4 and K1. Brief: `../briefs/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md`, SHA-256 `3c16bb93710b63429cd04b3ccb8d41bc5620584965dcb5228218c3dfaf1f38b1` (verified). Model: the host reports Opus 5.5 (`claude-opus-5-5`); `high` reasoning is instruction-asserted for the manager and every child. Nothing was applied: no production path, `_DECISIONS/**`, register, work graph or `docs/**` file changed.

## Brief amendments received (HELP_HUMAN, 2026-09-26; recorded as received)

1. Replaced the brief's "Method choice as an owner option" bullet: prepare K1 on PEC's current practice (the `D-PEC-93` precedent); disclose `project-setup` `INCREMENTAL` in one line only; do not put its adoption to the owner (Root notice: "no adoption, `SETUP_LOG.md` baseline or incremental setup run is expected in this loop now").
2. Resume instructions: keep the human-owned `_COORDINATION.md` Notes line as a separate optional question with exact replacement text, applied by HELP_HUMAN only if the owner authorizes; drop the DEL-10-13 C-08 question if it can wait for K2 without affecting this packet's bytes (it can: the new `_DEPENDENCIES.md` records the observation and makes no classification); confirm no pinned preimage changed at the newer `origin/main` and rerun the checks there; do not repair the "Update the PR base" failure.

## PR, draft and artifacts

- PR https://github.com/sgttomas/chirality/pull/962, branch `claude/pec-rev16-currency-setup-proposal` (cut from `aca930622`), not merged. The head is the last commit on the branch that carries this file.
- Draft: `PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/DRAFT_D-PEC-101_rev16_currency_setup_proposal.md` — hash in the prep folder's `SHA256SUMS` (rendered from `.src.md` by `fill_draft.py`).
- Bound generators: K4 `k4/gen_d101_k4.py` `075036f0a8c214a156aec151aaa52f6d1b78c2694f4306d410579ffcef9f0e73` (TASK-authored under `child_briefs/T_K4_GENERATOR.md` `daa69a74…9d16`; manager-rebuilt byte-identically); K1 `k1/gen_d101_k1.py` `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb` (manager-authored). Verifiers, runners, builders, templates and evidence are in `k1/` and `k4/`; hold preflights in `evidence/`.

## Target census (at `aca930622`; unchanged at `dfb089b8a`)

- **K4 (B7):** 129 paths, all modifications, slot-free — 63 `_CONTEXT.md` (61 standard revision-1.5 tails + DEL-02-08/09 in the D-PEC-93 form; the three SCA-006 A2 mirrors are read-only) and 66 `_REFERENCES.md`. The plan's 63/66 holds. Lifecycle: CHECKING 4, INITIALIZED 28, IN_PROGRESS 2, OPEN 28, RETIRED 4 (folders touched).
- **K1 (B1–B3):** 32 paths — 12 created (`PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/`, `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/`, six files each) and 20 modified (4 `Dependencies.csv`, 16 `_DEPENDENCIES.md` mirrors). Rows: 22 added (6 ANCHOR incl. SOW-097..100 traces; 16 EXECUTION, E-P84..E-P99; E-P83 skipped because D-PEC-93's unselected option O named it), 2 refreshed (DEP-09-06-003, DEP-10-03-003), 0 retired or deleted. New `_STATUS.md` = `OPEN` (`TASK+preparation`); new `_DEPENDENCIES.md` use the D-GOV-46 §5.2 skeleton; `_SEMANTIC.md` zero-byte (precedent).

## Parts, recommendations and method choice

- K4 with add-on C (recommended; C fixes the DEL-04-03 / DEL-08-03 covers bullets to include SOW-097 / SOW-098; no extra path).
- K1 as prepared (recommended). Disclosed alternatives (amend): add DEL-02-07; add DEL-08-06 → DEL-04-03.
- Add-on V: re-audit (`audit-decomp`), pointer move only on 0 BLOCKERs — recommended with K1, not with K4 alone.
- Parts are separately rulable; either order gives the same tree (prototyped).
- Method: the D-PEC-93 practice (WORKING_ITEMS with `project-setup`, `preparation` skill scaffold via the repository tools; rows bound by the generator with `dependency-extract` Function 5 checks as acceptance checks). `INCREMENTAL` disclosed only.

## Expected validator outputs (all reproduced on the prototypes)

| Check | K4 only | K1 (with or without K4) |
|---|---|---|
| Strict registers (`--strict`) | exit 1, byte-identical to base: 0 ERROR / 26 XRG-013 / 2 DRB-008 | exit 1: 0 ERROR / the same 26 XRG-013 / 0 DRB-008; 68 registers, 285 rows (ANCHOR 146, EXECUTION 139) |
| Closure | `closure_summary.json` byte-identical to base | 127 edges, 68 nodes, 0 SCC, 0 bidirectional, 0 orphans, 0 declared disagreements, same six isolated, hub DEL-03-01 only |
| Quote currency | unchanged (109/111) | 127/127 |
| Anchor coverage (COV-080) | — | 74/74 IN items; SOW-097..100 traced |
| Schema / fileset | — | VALID ×6; PASS ×2 |
| Receipts validator, harness self-check | identical before/after | identical before/after |

Other checks: determinism, fail-closed rerun, wrong-date refusal, `--check-only` non-writing, K1 slot rule (exactly 14 date-bearing files), git-clone containment and `git diff --check`, instruction entrypoints, and 161/161 `exact-correction-preparation` hold preflights `ALLOW`. `origin/main` advanced to `dfb089b8a` (PR #961, PR #960) during preparation: only two PEC work graphs and two review returns changed under `projects/pec`, no pinned preimage, tool, workflow or index changed, both generators rebuild byte-identically there, and the K1 suite plus combined K4/K1 runs were rerun there (`k1/evidence/`; first run `k1/evidence_aca930622/`).

## Verifier verdicts

See `PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/REVIEW_VERDICT_NN.md` (fresh read-only `pec-reviewer`, opus). Summary: {{VERDICTS}}

## Owner questions (in the draft)

1. K4: with C (recommended), without C, amend, or defer.
2. K1: as prepared (recommended), amend, or defer.
3. Add-on V: with K1 yes (recommended); with K4 alone none.
4. Optional, outside the grant: the `_COORDINATION.md` Notes line L225–227 — exact replacement text (with-K1 and without-K1 variants), applied by HELP_HUMAN only on explicit owner authorization.
5. Actor string `TASK+preparation` and model defaults.

## Unresolved / for HELP_HUMAN

- **"Update the PR base" CI failure — reported, not repaired.** "Select source coverage" fails with `ValueError: Update the PR base: event target base is missing, unavailable or not integrated into head` (and "Desktop E2E (source mode)" as its consequence): the branch is based on `aca930622` while `origin/main` is `dfb089b8a`. HELP_HUMAN updates the branch.
- The number D-PEC-101 is provisional; filing in `_DECISIONS/` and the register row are HELP_HUMAN's.
- K4 TASK disclosures: manager commit `3430993ea` captured a mid-run `k4/` snapshot (superseded by current bytes and `k4/SHA256SUMS`); one TASK run lost evidence files to an external deletion and was wiped and rerun cleanly (all K4 results from the clean run).
- Host notes: the Write tool was blocked on the new worktree until it was entered with EnterWorktree(path); two forced handbacks occurred during this run (both reported).
