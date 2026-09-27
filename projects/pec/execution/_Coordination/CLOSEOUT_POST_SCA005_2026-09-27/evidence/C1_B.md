# C1 group B — S2 (D-PEC-100), S3 (D-PEC-98), X1 (D-PEC-106), G1 (D-PEC-96). mktemp NAME: `c1b`

Read `C1_COMMON.md` (same folder, SHA-256 d8b790ac5412af98cf1dd164dcf94a9d50ad1098f91a01022b1e63a48ba0dfe1) first; it binds.

Deliverables and acts:
- S2, `D-PEC-100` (ruling `_Coordination/_DECISIONS/D-PEC-100_RULING_2026-09-26.md`; proposal `D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`), act PR #979 (merge `125cfacc1`), run root `_Coordination/SOW_REBUILD_S2_2026-09-26/` (incl. `POST_D101_RECHECK.md`), reviews `REVIEW_PR979_0{1,2}.md`: seven `ScopeOfWork.md` replaced — DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07. No lifecycle change.
- S3, `D-PEC-98` (ruling `D-PEC-98_RULING_2026-09-26.md`), act PR #958 (merge `aca930622`), run root `_Coordination/SOW_INIT_D98_2026-09-26/`, reviews `REVIEW_PR958_0{1,2}.md`: first `ScopeOfWork.md` for DEL-02-08 and DEL-02-09; add-on S set both `INITIALIZED`.
- X1, `D-PEC-106` (ruling `D-PEC-106_RULING_2026-09-27.md`), act PR #1008 (merge `5d0680951`), run root `_Coordination/X1_FIXTURES_2026-09-27/`, reviews `REVIEW_PR1008_0{1,2,3}.md`: 34 fixture files under `v2/tests/parsers/` and `software-workflow.json` replaced; add-on L moved DEL-02-03, DEL-02-08, DEL-02-09 `INITIALIZED → IN_PROGRESS`. Check that the three deliverables' records (status history, contracts' statements about fixtures/verification, dependency rows about fixtures) are consistent with the fixtures now committed.
- G1, `D-PEC-96` (ruling `D-PEC-96_RULING_2026-09-26.md`), act PR #950 (merge `73ed349ed`): `v2/config/loops.json`, schema v2, `RegisteredLoop` port; bears on DEL-01-06 records (its `_CONTEXT.md` mirror of register rows, the SOW rebuilt by S2).
Also relevant: `D-PEC-101` (PR #976) re-pinned contexts/references to revision 1.6.
