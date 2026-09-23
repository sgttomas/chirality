# App exception factual-transfer candidates

Status: **candidate receiving-document diffs only; no live SOW, status, register or product edit in this follow-on**. The exact bounded hunks are in [CANDIDATE_FACTUAL_RECEIVING_DIFF.patch](CANDIDATE_FACTUAL_RECEIVING_DIFF.patch), built against merged PR #861 basis `46ac555032bac3d7ad345bc2bdfcc1cd5255e682`. `git apply --unidiff-zero --check` passes at that basis. Applying a hunk later requires the owning App/Runtime/domain contract review, source recheck and an actual human exception disposition before any live `Remaining` entry is removed. The text records accepted meaning; it is not delivery evidence.

The earlier 29-row A screen was rechecked against current governing clauses. Twelve rows have a narrow missing factual detail worth a receiving-document candidate. Nine are already substantially preserved in their current SOW and remain product/evidence gaps (R011, R012, R030, R034, R056, R058, R065, R066, R074). Eight require an owner or consumer decision before any diff (R016, R017, R018, R020, R024, R060, R078, R096). The remaining held rows have no factual SOW transfer proposed. `ROWS.csv` records this treatment for each original.

| Original | Candidate receiving clause in patch | Accepted source and exact limit |
|---|---|---|
| APP-R003 | DEL-01-01 CLM-011 P0 enforcement review row | DEL-01-01 CLM-009 REQ-006; R003 live text; D-GOV-43/D-APP-127. Include DEL-07-01 ordinary instruction-root and Runtime selected-policy checks without assigning every proposal/domain control to DEL-07-01. |
| APP-R009 | DEL-01-03 CLM-011 rendered-journey review row | DEL-01-03 REQ-04–06; R009 live text. Records shell/dialogue/replay copy evidence; no human review is invented. |
| APP-R013 | DEL-02-01 SCA-APP-010 current acceptance item 7 | D-APP-108 seated shell work and target-spec Stone/wordmark design. Target spec §10 contains pre-D-GOV-43 role and consent labels, so the patch checks current copy against D-GOV-43/D-APP-127 and four-role guidance instead of importing stale labels. |
| APP-R015 | DEL-02-01 SCA-APP-010 current acceptance item 8 | Applied folder scope SOW-002/005/010; known roots stay convenience state. No Runtime daemon root field is created. |
| APP-R022 | DEL-02-03 CLM-009 viewer detail | D-APP-108 Q4a/b: 10 MB in-panel text cap, PDF in-panel and Office Quick Look. D-APP-121 isolated PDF proof and publication boundary remain separate. |
| APP-R023 | DEL-02-03 CLM-009 reference detail | D-APP-108 Q2: chips, Ask/Attach and `clientType: 'quote'` with source path/range using existing attachment controls; no new harness event. |
| APP-R028 | DEL-02-05 CLM-009 REQ-001/003 detail | D-GOV-43/D-APP-127 Codex login methods and per-turn model/effort. Existing S-8, retry and policy obligations stay unchanged. |
| APP-R044 | DEL-05-02 CLM-012 verification detail | SOW-082 actual producer and R044 current declined-trigger/once-per-chat fixture; no replay result is asserted. |
| APP-R075 | DEL-09-02 RQ-016 current Section 9 coverage detail | D-GOV-43/D-APP-127 descendant class/attribution/cancellation families and compatibility-only first-adapter IDs; Section 9 remains report-only. |
| APP-R085 | DEL-09-06 CLM-012 secret-field family verification row | R085 live text and existing K-KEY/S-8 boundary. Account, approval, thread, policy and tool-activity sinks need actual candidate-bound fixtures. |
| APP-R089 | DEL-10-01 CLM-007 staged profile/registry validation note | D-APP-49–52 staged authority and current R089; invalid profiles fail before Codex exposure. Apply, protected writes and integration-level advance remain gated by tier-0/F-APP-3. |
| APP-R094 | DEL-10-03 CLM-010 proposal-path coordination note | Current TYPES §11.2 proposal-only status and DEL-10-02 path policy; denial/allowance fixtures are unperformed. This transfers interface/evidence meaning, not enforcement ownership. |

The patch has ten SOW target files because R013/R015 share DEL-02-01 and R022/R023 share DEL-02-03. Its hunks are candidates, not a second maintained work list; the live 54 exception bullets and their actual evidence/authority gates remain the current discovery source until separately dispositioned.

## Exact source preimages

The ten candidate hunks are bound to these current `ScopeOfWork.md` bytes. Recompute before any later application.

| Deliverable | Census originals | ScopeOfWork SHA-256 |
|---|---|---|
| DEL-01-01 | R003 | `e1717fd234ab2b9734c23a7996b03691b3fb557048fe5a929ff37ab9d7907b2b` |
| DEL-01-03 | R009 | `9045e4be3365ea4754cb80c1ec7fe0e48965102b5d5658479b098e752e1d3ebc` |
| DEL-02-01 | R013/R015 | `e6101511521c6ea1af89aedceca9c14d69f94f1e5bedca7614ec3ae6bf88910e` |
| DEL-02-03 | R022/R023 | `6f70120b0cdf0bcc3e0740745f7a2b7a5d23f5e97fca67acec52aca159603be3` |
| DEL-02-05 | R028 | `32f725b3c2892ce19fe43579cc5dad2a1f51f2cddc625db986f30cfdbf449c15` |
| DEL-05-02 | R044 | `64580ca35b58e0949f6d6aaa32de8f766ae6571bb0952de25bd804e6cdbd53b3` |
| DEL-09-02 | R075 | `4e554d38f5a0920280734c9cbd0f6103f0acd17efe89ceaf9f617c38bfc9d1c5` |
| DEL-09-06 | R085 | `6d0137565f0c90dabb2e311307b4b069b4f61d83cc9503fb48ab18924dca878a` |
| DEL-10-01 | R089 | `b0bad5b9255bf6b6e8c5db389ad791f2f5615e0ae83b9ac756eda00152c427d8` |
| DEL-10-03 | R094 | `2423f6e874b415aa3f503b0cec52d7deb75de3286bee3fd6551a6206245d9ae6` |

Patch SHA-256: `51b145da6a59174caf9069978cc4879614f8c6760556e824d8d2ef8e9426d4db`.
