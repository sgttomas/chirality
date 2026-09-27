# Return — S2A D-PEC-100 act (WORKING_ITEMS)

Brief `briefs/S2A_D100_SOW_ACT.md` (`818d9526e089befaba48360360b2138a511c6b8ba8982586fae81148abf54e58`, verified).
Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node S2 (the act), 2026-09-26.
Manager: WORKING_ITEMS (Type 1), `claude-opus-5-5` (host-reported; high effort instruction-asserted).

## PR

- PR #979 https://github.com/sgttomas/chirality/pull/979 (`claude/pec-d100-act` → `main`), **open, not merged**.
- Head at the records commit: `3f2ab9311`; this return is the next commit. Base `bdae9d66b` (PR #971 merge).

## Act report

- Preconditions met: fetched `origin/main` = `bdae9d66b` carries the ruling (`13690e20…729b`), the proposal (`39c4331e…e25b`) and register row `D-PEC-100` `RULED A / B CONFIRMED / M / EFFECTIVE ON MERGE`; bound script `42dc9553…3d20` in prep and run root; 28 run-root inputs equal the prep `SHA256SUMS`.
- Reliance preflight: `dispatch-for-production` ALLOW ×7 before the act; `rely-for-production` ALLOW ×7 after the write and before the act commit.
- `apply_s2p.py --check-only` exit 0; one real run exit 0: `CHECK targets 7/7 byte-exact; write set = grant (0 created, 7 modified, 0 removed under projects/pec outside the run root); pinned 23/23 unchanged`. Script output was captured in the session scratchpad and copied into the run root after exit.
- Act commit `23e065e4f`. No lifecycle change; add-on M not written (node M1).

## Written paths (SHA-256 at `3f2ab9311`)

| Path | SHA-256 |
|---|---|
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md` | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md` | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md` | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md` | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |
| `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/MANIFEST.md` (hash-lists every other run-root file; 159 files in the run root) | `8456ddb2f91d6823efab66bb323ccf8d980139b21d7972ff6b6f5234649fcddf` |
| `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/VALIDATION.md` | `6388c13d79dbe639fa03db4c64282037f1cb4aed91717f1826db32888cfd86b0` |
| `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/HANDOFF_STATE.md` | `2c664a7270fd1c14256904771fc7bb0716576379a4205583d8b7c64bc23135b5` |
| `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/VERIFIER_VERDICT_01.md` | `b0e6cb7d43d14c8d36d9483bef206620e9b6a5d9083178ddcf890fcee86fed8f` |
| `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S2A_D100_SOW_ACT.md` | `818d9526e089befaba48360360b2138a511c6b8ba8982586fae81148abf54e58` |
| this return | (not self-hashed) |

## Check results (proposal "Finite verification"; detail in `VALIDATION.md`)

validate `PASS format=SOW_V1` ×7; checklists exit 0, reruns byte-identical, equal to the prepared hashes; boundary owners exit 0, no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM`, `NOT_CHECKABLE` set exactly as tabled and hand-resolved; quotes `RESULT PASS 460/460`; state claims `RESULT PASS 1280/1280`; sibling IDs `RESULT PASS 92/92`; `_STATUS.md` diff empty; strict registers (exit 1, 0 errors, 28 warnings), harness self-check and receipts validator byte-identical before and after; `git diff --check` clean. Rerun method `run_s2p_checks.sh` on exports of `bdae9d66b`: `OVERALL PASS` (fault injection 9/9; consequence scan stale=31 kept=32, informational). Exports deleted.

## Verifier

`VERIFIER_VERDICT_01.md`: fresh read-only `pec-reviewer` (agent `a552c84c639784606`, foreground), candidate `eea486f48`: **PASS WITH NOTES**, no blocking finding. N1: DEL-02-07 `CLM-011` (L120) counts five `adapter.yaml` files where six exist at `aca930622` (observation only; not re-pinned; carried to the next DEL-02-07 revision). N2: `evidence/** -whitespace` disclosed. N3: records added (run root only). N4: stray ignored `__pycache__` (manager's listing without `PYTHONDONTWRITEBYTECODE`) deleted; never committed.

## Containment

`git diff --name-status origin/main...HEAD` at `3f2ab9311` (merge base `bdae9d66b`; `origin/main` then `19c38f221`): the seven `M` contracts, the brief copy, and 159 run-root files; with this return, one more path at the brief's return location. Nothing else: no `_STATUS.md`, `MEMORY.md`, register, dependency, context, reference, decomposition, `v2/**`, PRD, `docs/**`, README, `_DECISIONS/**` or work-graph path. `git diff --check` exit 0.

## Unresolved (for the caller)

1. PR #979 needs fresh independent review of the complete diff and CI; verdict 01 covered `eea486f48`; later commits add only run-root records and this return. Merge is the caller's.
2. `origin/main` has advanced (non-PEC merges and one PEC notice file, plus a changed register validator whose output on the act tree is byte-identical per the verifier). If CI asks to update the PR base, that is reported here, not repaired.
3. D-PEC-101 (PR #976) was open at handoff. If it merges first: re-fetch, confirm the 23 pins by hash, rerun quotes, state claims and sibling IDs on the updated base, and compare strict before/after at that base (its new DEL-08-06/DEL-10-13 folders should clear the two `DRB-008`).
4. Add-on M at node M1 (six new `MEMORY.md`, one row in DEL-01-06's), `{PR}` = #979.
5. HELP_HUMAN's records: register row, work graph, central receipt, and `docs/STATUS.md`/`README.md` under `D-PEC-88`.
6. Carried unchanged: the 15 downstream contracts with stale quotations (S1, S4, later DEL-02-08/09 revision); all `CON`/`TBD` items open; DEL-02-07 Part B production stays gated.
7. Host note: the Write tool refused paths in this worktree (hook binding it to the session's original worktree); files were written with shell commands inside this act's own worktree, as the caller directed. The caller's checkout `pec-project-assessment-6106d5` was not modified.
