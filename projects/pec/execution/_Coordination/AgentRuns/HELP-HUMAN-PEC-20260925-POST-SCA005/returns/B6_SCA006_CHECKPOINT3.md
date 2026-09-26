# B6 return — SCA-006 checkpoint-3 preparation (INTERIM: forced handback)

WORKING_ITEMS, brief B6 (SHA-256 `8bdc718105f05dd2f72378e50fea246eb99a38a937938da72afa221bb8872df4`, read from `origin/main` `94e9255b6`), node R3. Application date: 2026-09-26 (local, America/Edmonton). This is an interim return: the host forced a handback before C4 finished. It claims nothing beyond what is listed.

## State

- PR: https://github.com/sgttomas/chirality/pull/943 (branch `claude/pec-sca006-cp3-execution`, open, **not merged**). Early CI checks pass; `harness` was pending.
- Done: preconditions; A1; A2; A4 (AGENTS.md with amendment-1 hunk, manifest, three notices, `AGENTS_MD_AMENDMENT1_DIFF.md`); A4 checks; A5 `Supersession_Map.csv`; C1 (interim); C2; C3.
- Not done: C4 audit child still running at handback (output folder `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/` partly written, uncommitted); C4.3 review instance; `Post_Change_Coverage.json`; `RUN_SUMMARY.md` with the checkpoint-3 question; `Decision_Log.md` SCA006-CP3 row; `Handoff_State.md` append; C5; independent verifier (none dispatched, no verdicts).

## Instruction and method sources (SHA-256)

Root `AGENTS.md` `c8ce87ef…fffd`; `CLAUDE.md` `336cc4fb…ab49`; `projects/pec/AGENTS.md` (preimage) `c9d3b44d…197a`; `agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`. Pinned scope-change from `4d5f7b911`: `WORKFLOW.md` `58f5d1d5…7a90`, `contract.md` `4453a719…4f344d02`, `method.md` `34187e83…d167f5` (all match the brief). Current `audit-decomp`: `WORKFLOW.md` `7ba6291c…246b`, `contract.md` `704929c7…4e75`, `method.md` `51a0c69b…8827`. Group-2 `DECISION.md` `30aebd16…a989`; `ACCEPTED_MANIFEST.csv` `b9563489…2bc52`; amendment-1 `DECISION.md` `15720eb1…777e`.

## Preconditions

All live preimages, both `_LATEST.md`, the three A2 contexts, and every group-2 manifest artifact matched (`CP3_EVIDENCE/precheck.py`, 0 fails). `D-PEC-97` row present; amendment 1 carries §"Verification rule". Reliance-hold preflight: 22 targets × 3 operations (exact-correction-preparation, candidate-validation, dispatch-for-production) all ALLOW.

## Writes (preimage → postimage)

| Path | Pre | Post |
|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | `dc2b8479…9660` | `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` (pre-acceptance lines; slot proof reverses to `3ad0de68…` and `4eed1247…`) |
| `ScopeLedger.csv` / `Deliverables.csv` / `ContextBudgetQA.csv` / `Companion_Inventory.csv` | `83152a94…` / `b8628fc4…` / `2a194105…` / `7c8a24a8…` | `1d24a4b8…` / `94ee5d18…` / `93b0bb07…` / `1597ceec…` (byte for byte) |
| `docs/PRD.md` | `fff27a66…dfc32` | `ae49b8065698…483fbe` (byte for byte) |
| DEL-04-03 / DEL-08-01 / DEL-08-03 `_CONTEXT.md` | `a505c268…` / `151e1e34…` / `4644758f…` | `b28ada46…` / `74b12e73…` / `95fa815a…` |
| `projects/pec/AGENTS.md` | `c9d3b44d…197a` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` (candidate slot-filled `6f6f2ed1…64e6` plus the hunk) |
| `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml` | new (draft `852b1d5b…`) | `f7f48690…0a72` |
| Root / App / Runtime `NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (drafts `43cfa318…` / `eb927e1f…` / `385e5e2f…`) | `b3c60bf4…c601` / `af4f6342…68ef` / `e883efac…bb93` |
| `SCA-006…/Supersession_Map.csv` | new | `010ce5c4…ab92` (accumulator: 45 rows, 29 + 16, 0 findings) |
| `SCA-006…/AGENTS_MD_AMENDMENT1_DIFF.md`, `CP3_EVIDENCE/*` | new | scripts and C3 result |

## Slot values

- Decomposition (application-date): front-matter `date:`, §7 Revision row, DL-21 date → `2026-09-26`; `status`/`accepted` in pre-acceptance form. The preview binds these slots to the checkpoint-3 acceptance date; if acceptance falls after 2026-09-26, A6 must re-substitute them.
- PRD S1–S4 and group-2 token: `2026-09-25` / `SCA-006_GROUP-2_2026-09-25` (unchanged).
- AGENTS.md: L6 `amended:` → `2026-09-26`; L209 token unchanged.
- Manifest: ID/filename/notice dates `20260926`/`2026-09-26`; `date: 2026-09-26`; `basis: 94e9255b6…`; CP2-ACT `'SCA-006 CP2: accept; Q1 a; Q2 a'`; CP2-VARIANT `AGENTS.candidate.md` (with I1); `authorization_date` kept `2026-09-25` (manager choice: the checkpoint-2 act date); `m6_notice.disposition: routed`; one named addition `group2_amendment_1`.
- Notices: manifest path date `20260926`; group-2 token unchanged; one named amendment-1 addition each (owner's words verbatim, snapshot path, correction).

## Amendment-1 hunk (verbatim; owner must explicitly approve before merge)

Replaces candidate L261–270 (applied L261–272):

```text
PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries
(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2
amendment 1). No PEC feed profile reads them, so the coordination plane does
not scan them, and they are not a work-selection surface. Steering selects the
undertaking; record new open scope in its work graph and governing records.
Until any retirement ruling, the existing sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). A Remaining item's own gate markers still bind that item.
Update an item only under the packet that opens that `_STATUS.md`. If an
undertaking completes or affects an item without such a grant, record the
consequence in the graph and bring it to the owner. Retiring the sections, as
App and Piping did, is a separate owner-directed undertaking.
```

Dropped clause (disclosed): "its graph accounts for the Remaining items it touches", on the reading that it implies scanning, contrary to "no need to scan for them".

## Checks

- `validate_instruction_entrypoints.py .` PASS (0); G4 CI mode PASS, 124 manifests (0); G4 `--base origin/main --head HEAD --added-manifests-only` PASS, 1 instruction-surface path covered (0); `validate_pec_loop_receipts.py` VALID (0); `git diff --check origin/main HEAD` clean (0); pytest entrypoints + receipts 33 passed; harness self-check exit 0, no finding names a changed file.
- C1 (interim, before A5 completion): 24 changed paths all in the allowlist; 34 hash checks pass (14 planned postimages, 20 frozen checkpoint-1/2 artifacts and both `_LATEST.md`).
- C2: strict validator 0 ERROR, exactly 2 WARNING DRB-008 (DEL-08-06, DEL-10-13), exit 1 by design; `analyze_dep_closure.py` 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs.
- C3: 31/31 PASS (100 = 74/18/8; 68 = 64/4; envelopes 28/34/2/0; union 64/64; PKG-04/08/10 = 7/8/13; issues 10/3; 29 terms; 6 objectives unchanged; 49 PRD requirements; K-01, K-02, K-11, P1 rows byte-identical; IDs append-only; no new folders).

## For HELP_HUMAN to resolve

1. Resume this manager (or a new one) to finish C4 (collect the audit child's return, commit its folder), C4.3 review, A5 (`Post_Change_Coverage.json`, `RUN_SUMMARY.md` with the checkpoint-3 question, Decision_Log SCA006-CP3 → `PREPARED / AWAITING_OWNER`, Handoff append), C5, and the fresh `pec-reviewer` loop. The audit child's completion notice may reach HELP_HUMAN; relay it.
2. Obtain the owner's explicit approval of the exact hunk above before merge.
3. Review the three notices; add the `docs/STATUS.md` D-PEC-88 correction.
4. Slot timing risk for the decomposition acceptance-date slots (see Slot values).

## Delegation record

- C4 audit: Claude Code Agent tool, `subagent_type: pec-task`, `model: opus` (Opus 5.5), background; parent this WORKING_ITEMS; brief given inline (read-only except the COV folder; no git state change; no `_LATEST.md` move); instruction-asserted, not tool-enforced. Running at handback; no return received.
- No verifier dispatched yet.
