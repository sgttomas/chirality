# Orchestration Plan — APP_SCA_APP_010_SEATING_2026-09-04

- **RunID:** `APP_SCA_APP_010_SEATING_2026-09-04`
- **Plan version:** 1 (frozen before any carrier write; `Evidence/pre_images.json` was recorded first)
- **Selection authority:** `HUMAN` — Ryan Tufts' direction and option selections on 2026-09-04, transcribed verbatim in `execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md`
- **Supervisor and applicator:** HELP_HUMAN (Agent 0; Claude Fable 5.1, `claude-fable-5-1`) in an untyped Claude Code session, acting for the carrier writes as WORKING_ITEMS' applicator under the owner's "You may run the WORKING_ITEMS alignment in the same PR." Role not mechanically enforced.
- **Independent reviewer:** one bounded Claude Code subagent, read-only except its named report file, dispatched over the frozen diff after all writes; per-carrier verdicts required.
- **Basis:** branch `claude/sca-app-010-seating` cut at `787a551e70d9fb33f6f9a9fe228443d890a8d02d` (PR #712 merge). Accepted upstream truth: applied decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (PR #708 merge `7795b0972cac147869607d994173753e4a2fc232`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (PR #711 merge `311a2f0b811d55315d6eb623130cad0be1417565`); authority corpus v20, no drift.
- **Governing plan:** SCA-APP-010 `Propagation_Plan.md` §6, `OWNER_ACTION_MATRIX.csv` steps 17, 18, 21, 22, `DOWNSTREAM_HANDOFFS.csv` rows 1, 2, 7, 8, `FUTURE_WRITE_SET.csv` WI-001 to WI-065, N-001, TM-001. Workplan overlay on `main`: `loop/WORKPLAN_2026-09-04_app_dev_loop.md` (focus item 3: "Shell redesign work, once seated by the owner into deliverable Remaining sections").
- **Working root:** `projects/chirality-app-dev`; one Root-surface write (N-001) under the owner's session Root write grant.

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| N0 | Re-derive current state: verify pointer, decomposition, and companion hashes; map every presented seating row to its carrier, applied row line, gate, and ruled questions; detect ID collisions; freeze pre-images | repo read-only | this packet (`MAPPING.md`, `Evidence/pre_images.json`, `Evidence/app_hold/*.json`) | map and pre-images | every carrier folder resolves uniquely; APP-HOLD dispatch preflight `ALLOW` for all seventeen |
| N1 | Deterministic seating and alignment through `build_seating.py --apply`: Remaining items, history and memory lines for seventeen carriers; Scope of Work re-pin plus SCA-APP-010 Gate-5 Current Contract, `_CONTEXT.md`, and `_REFERENCES.md` alignment for the thirteen | as N0 | the seventeen carriers' `_STATUS.md` and `MEMORY.md`; the thirteen carriers' `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md` | `Evidence/post_images.json`, `Evidence/seeded_items.json` | `--check` parity; every transaction keyed on exactly-once text; fail-closed before any write |
| N2 | Owner-decision and coordination records: D-APP-108 ruling record and register row; routed Root notice (N-001); TM-001 label check | as N0 | `_DECISIONS/D-APP-108_*.md`, `_DECISIONS/_REGISTER.md` (one row), repo-root `execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` | records | verbatim owner text; notice supersedes the frozen draft by hash |
| N3 | Validate: Scope of Work validator ×13, corpus status, harness self-check, G0 to G4, candidate whitespace, `git diff --check`, receipts validator, routed tests; independent review over the frozen diff | as N0 | `VALIDATION_EVIDENCE.md`, `REVIEW.md`, `Evidence/validation/*` | PASS or findings | review PASS per carrier with zero blockers before push |
| N4 | Handoff, receipt, manifest; commit, push, open one unmerged PR | as N0 | `HANDOFF_STATE.md`, `MANIFEST.sha256`, `loop/LOOP_RECEIPTS.md` (append) | PR | owner byte review and merge |

## Human decision points

- Owner byte review and merge of the candidate PR (confers selectability only).
- Owner acceptance of the alignment, which triggers the report-only dependency-extract preview (DEP-001 to DEP-026), the named closure audit, RECONCILIATION, and AUDIT_DECOMP reruns in that order.
- Every `NOT_SELECTABLE_UNTIL` gate or act named in the seated items; Root returns arrive as routed notices.
- Any tightening of a presented gate that this run recorded as a technical dependency instead (see `MAPPING.md` §C).

## Constraints carried

Sealed write set as listed per node; no `docs/**`, authority-corpus, `frontend/**`, decomposition, companion, pointer, snapshot, prior receipt, prior ruling, dependency register, or lifecycle write; no implementation, host mutation, signing, release, publication, or reliance act; fences F-APP-1 to F-APP-5 untouched; Checking Approval SHA and Current State unchanged in every carrier; truthful attribution.
