# Return — CLOSE: closeout of HELP-HUMAN-PEC-20260925-POST-SCA005 (C1, Task Management intake, M1)

- **Actor:** WORKING_ITEMS (Type 1) closeout manager, Claude Code, model `claude-opus-5-5`
  (high reasoning is instruction-asserted). Parent: HELP_HUMAN.
- **Brief:** `briefs/CLOSE_POST_SCA005.md`, SHA-256
  `235ec63ee4cfe5f7719692c4eaaafb5a46e785c62dd214b1dbd1ef298f2306f6` (copied unchanged; hash
  verified before and after copying).
- **Worktree and branch:** own worktree `.claude/worktrees/pec-post-sca005-closeout`, branch
  `claude/pec-post-sca005-closeout`, cut from fresh `origin/main`
  `5d06809519851e8bae865eb5a9c8160705bf6928` (the PR #1008 merge). The file-write tool was
  not needed outside the launch worktree; all writes used the shell inside this worktree.
- **PR:** https://github.com/sgttomas/chirality/pull/1014 (F1; not merged). The head is the
  commit carrying this return; its SHA is in the hand-back, since a file cannot carry the
  SHA of its own commit.
- **Instruction and method sources (SHA-256):** Root `AGENTS.md`
  `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`; `projects/pec/AGENTS.md`
  `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`;
  `agents/AGENT_WORKING_ITEMS.md`
  `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665`;
  `projects/pec/loop/LOOP_INIT.md`
  `c97d49fff5c2fabca1c9c05b44bcde958e46fccb067d512ce93779d4cfad821b`;
  `workflows/bounded-reconciliation/WORKFLOW.md`
  `c7798c0ae59860f193d60f007996a215327c54e3e4dbd8eb0e62b57aab0f11bc`;
  `workflows/task-management/WORKFLOW.md`
  `d5e8eff5742326330c0f933dc322e07fbe6a2bb82ad151aadf803b001a02e654`, `resources/contract.md`
  `3162f7ed386bcac08c0e16c0feae3b7a7a5109ba4bf4f845acc66bd2d6dfd04e`, `resources/method.md`
  `d52403c983c92b1c65fe2b621d8c6bdc5c10e1fdb8c9ac99e95614137639c61e`;
  `docs/templates/MEMORY_TEMPLATE.md`
  `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`. Packet add-on M
  sources: the `D-PEC-98`, `-100`, `-102`, `-103`, `-104`, `-105`, `-106` proposals and
  rulings (proposal hashes `92b6f1a2…3e40`, `39c4331e…e25b`, `baf17812…cfdd`,
  `cfc2e65d…5417`, `35301840…5f51`, `07761005…a89f`, `677b59f6…d279`; rulings `039dc7e2…3e40`,
  `13690e20…725b`, `782ee02f…d288`, `67ff8f1e…e1eb`, `bb88deb5…ec1bd`, `401c2419…bd0ef`,
  `5161630b…96fe`), and `D-PEC-96` ruling row 5 with its proposal (~L570).
- **Delegation (Claude Code subagents, all `opus`, each in its own scratch directory):**
  three read-only `pec-task` comparison children (C1 groups A, B, C) and one fresh read-only
  `pec-reviewer` M1 verifier. All returned; none remains running.

## 1. C1 account

`execution/_Coordination/CLOSEOUT_POST_SCA005_2026-09-27/C1_ACCOUNT.md`. Supported
no-change for every deliverable-local record of the 33 touched deliverables; 127/127
ACTIVE EXECUTION dependency quotes verbatim; no missing implementation or evidence. No
direct edit was made. Warranted edits and homes:

| ID | Edit | Proposed home |
|---|---|---|
| S2-1 | Ten "(provisional `D-PEC-100`)" references in the seven S2 contracts (new; carried nowhere) | Fenced; next currency revision of each contract; intake CAND-01 |
| F-C2 | S4 CON items (DEL-10-03 CON-004, DEL-04-02 CON-008, DEL-08-01 CON-003, DEL-03-04 CON-001(b)/002/007) route to K2 first SOWs that merged first and left them open; DEL-08-06 CON-001 premise overtaken (new) | Fenced; later currency revisions; intake CAND-01 |
| F-C3 | K2 act carries (two register amends, release process, verifier notes 2 and 4) absent from the graph | HELP_HUMAN's graph and receipt (text in the account) |
| X1-1 | Graph still shows PR #1008 unmerged (L68, L90, L159, L161, L167) | HELP_HUMAN's graph at completion (text in the account) |
| X1-2 | Graph X1 residual list omits two parser-packet carries | HELP_HUMAN's graph and receipt |
| F-C1 | Stale completed-work table cells (L186, L188, L189, L190, L192) and missing rows | HELP_HUMAN's graph |
| RR-1, F-C4 | Run-root "not merged" lines; `_COORDINATION.md` item 15 tense | No edit (point-in-time / not false); optional text given |

## 2. Task Management intake

`execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/` —
`FEDERATION_PREFLIGHT.md` (COMPLETE, 4 registers, 28 findings, none involving PEC, 0
writes) and `INTAKE.md`. The brief names `projects/pec/execution/_TaskManagement/**`; no
such directory exists, so the intake is in PEC's actual Task Management home
(`execution/_Coordination/_TaskManagement/`, the LOOP_INIT pointer), under
`_Coordination/**`. Following the workflow contract, an intake is a candidate note, not a
register row; `REGISTER.csv` and `REGISTER_CLOSED.csv` are unchanged. Candidates awaiting
the owner:

- `CAND-PEC-2026-09-27-01` contract-currency residuals with no owning packet (brief item 1
  contract items, plus S2-1 and F-C2); recommended: one owner-ruled SOW-currency packet in
  the next undertaking.
- `CAND-PEC-2026-09-27-02` decomposition, PRD and instruction residual wording awaiting a
  scope change or instruction tranche (D1 "Other findings" 2, 3, 9; the `D-PEC-96`/`-101`
  `remaining-loop` and Lane B wording; the `D-PEC-100` proposal's register list).
- `CAND-PEC-2026-09-27-03` hosted CI does not run PEC v2 registered checks (Root/CI scope,
  excluded by every packet since `D-PEC-87`).

Judged already homed: lapsed acceptances (graph and receipt; recommended to be named with
RV1 for the next undertaking); RV1 (next undertaking); K3 (SCA-006 CP2 plan §B6, graph K3,
DEL-08-06 TBD-007/CON-002; trigger a DEL-08-06 production packet); the two dependency amends
and the release process (DEL-08-06 CON-003, DEL-10-13 CON-002 and CON-004); X1 residuals
other than hosted CI (the first parser packet); D1 "Other findings" 10 (RV1) and 11
(`TM-PEC-021`).

## 3. M1 MEMORY records

Preflight: `pec_reliance_hold.py --operation exact-correction-preparation` on all 33 targets:
ALLOW ×33 (register header-only; `evidence/reliance_preflight_memory_targets.txt`). Written by
`evidence/write_memory.py` (template instances plus the tabled rows; slots `{D}` =
2026-09-27, `{PR}` = act PR, receipt and ruling links relative to each file).

| Deliverable | Act | Rows | SHA-256 |
|---|---|---|---|
| DEL-00-01 | created | D-PEC-105 | `0596e9c67b25ecc65193b3e1df9f21233e1af73446b31d4ccd940a611e9afa76` |
| DEL-00-03 | created | D-PEC-105 | `dfdadecee99afbd63a35d2e8c2f7f9d6b91b1a7c97d89bdde708bd5435adb447` |
| DEL-01-01 | created | D-PEC-100 | `f3ce30d9b73cd84250d06f293bc69e90c29f72036d1f06c33e3583791e48aa47` |
| DEL-01-03 | appended section | D-PEC-104 | `6b5304d504bd9aa50ab012d510509a7ce2509c1997eddb7d1d3b31bd22852fa5` |
| DEL-01-04 | created | D-PEC-104 | `223e30ea73c8ae49c1f8d9777110d9587cdde8582b6893f109396b75e9b28cc6` |
| DEL-01-05 | created | D-PEC-104 | `7fa44dfec89a10890f0a3a8484e56440da20596a08f77311bb5bbaa029de62b8` |
| DEL-01-06 | appended | D-PEC-96, D-PEC-100 | `fb27f23b30b457b110a981f93fe92623b69cca1ed3deded969fa9a9428de1a25` |
| DEL-02-01 | created | D-PEC-104 | `e2c53abd2868013e367ffef194da9915bbe313189669ab10f713d6165842a620` |
| DEL-02-02 | created | D-PEC-104 | `ac70957ae8a8bfb02a2b9c5fd0a1ffdc8af7c70955dd8c39e3f074d71ee5dd9d` |
| DEL-02-03 | created | D-PEC-100, D-PEC-106 | `e97134e8a3f17dcea9c056b46671586446f080df0c7d6c56a1dc2f2464a004f0` |
| DEL-02-04 | created | D-PEC-100 | `e143585b8664d775fca1a9853e08a1cf4dd05fe0c952003f10c5bcc6ee85b121` |
| DEL-02-05 | created | D-PEC-100 | `4a9ad7844aa30c291534e26e2363f0e8acdd540905078297ab2800d5b9cd0698` |
| DEL-02-06 | created | D-PEC-100 | `d3b5172e954785374f8569b6f663e2f8d86b58f3318c70eef6807b8b909d4316` |
| DEL-02-07 | created | D-PEC-100 | `94ac323f67b81e23b9a7a511715ebcf6fb0a329cbb8820f9d71bb1670e07d651` |
| DEL-02-08 | created | D-PEC-98, D-PEC-106 | `76605078f0f85793db22f6f15d32d34e2a143aa41126c4caa4ccce4a6e7ccc76` |
| DEL-02-09 | created | D-PEC-98, D-PEC-106 | `42754e8afac1359ed73fd3de24d55ae32f75f7c86ab27075f69532333ab0f373` |
| DEL-03-01 | created | D-PEC-104 | `862e7aada928abe96b34f974550b0bf94a8fa95d1179d0f9a9b5dceb453575e6` |
| DEL-03-02 | created | D-PEC-104 | `fbe8f2f21fff1b3ce0f38b443808cb2b4f2c90606363fa17d203d08766b41960` |
| DEL-03-03 | created | D-PEC-104 | `b887c552556babbbda09a55e56a4925760dfe3852ec541f33af62d0fe9bed106` |
| DEL-03-04 | created | D-PEC-102 | `5808c99aafc3cf042aac40ff9dc07fd9ad2c2285860239ed4d7434d80ca3e441` |
| DEL-03-06 | created | D-PEC-104 | `acb58f73d1b516346ea9edc5b61893b48ceb0d4c7fb2afa265804acd360dddb1` |
| DEL-04-01 | created | D-PEC-102 | `a24b7fd4bb4c91e2e6931c288bc5c3c316eeb421009ea085b82f901b4511e4c1` |
| DEL-04-02 | created | D-PEC-102 | `4cd46a2ac040e3fb0e498a2adf2bbe5480ac1a1f0ad3e3219888e5b6183ef60d` |
| DEL-04-03 | created | D-PEC-102 | `f887c798d180d9e45d0167557f4ff52203bc8f817bcfc0707ed4ed90744774bb` |
| DEL-04-05 | created | D-PEC-104 | `e16d4017e4a74298810dcb2a37c9766f5a848574beac994bb7c9ad5db3c45296` |
| DEL-08-01 | created | D-PEC-102 | `2fbd03d453e3cb72ebcbcba4319f69ff3cb9f1a65fcb4768d5e1e4087f9e44c6` |
| DEL-08-03 | created | D-PEC-102 | `0e9fdf28bd1ec569d3ef394528b2c3abbbd053dfe0bf7309594e6956e47d4e3c` |
| DEL-08-04 | created | D-PEC-102 | `36ef29abf4d474f99fb43465b8c4d2a6243de84ec641ed96d7727a273314be7a` |
| DEL-08-06 | created | D-PEC-103 | `c0f3ddd02b1497fb7acffea44dcc7e09f79acfed392a72e66560e98ae8f760c2` |
| DEL-10-02 | created | D-PEC-104 | `dcc297750439887e424d7902882670be2d387433dbc3e6f21f42a3bcfc4b4cc1` |
| DEL-10-03 | created | D-PEC-102 | `165412eb22c93b2eec966734282ee40709de4f25147df29d8f0fcbe9a22c48cf` |
| DEL-10-10 | created | D-PEC-104 | `4f2a2e2e7c61c8683582849a5008651b0c24188a6694cf353f4a1d83b75d02e2` |
| DEL-10-13 | created | D-PEC-103 | `212e5532559735865dd588e46390dd80fe31966cd9e47142cee9a144251e2756` |

**The D-PEC-96 row (caller to confirm).** The brief asks for the `D-PEC-100` row "after the
`D-PEC-96` row", but DEL-01-06's file (created by PR #950) had no rows. `D-PEC-96` ruling
row 5 says "The undertaking's closeout writes the run row", and the `D-PEC-100` packet puts
its row after that one. The manager therefore wrote the `D-PEC-96` row first, composed from
the proposal's named components (no byte-exact row is tabled):
`| HELP-HUMAN-PEC-20260925-POST-SCA005 / 2026-09-27 | Schema version 2 source act under
D-PEC-96 (graph node G1). | [central receipt](…); PR #950 |`. It is in its own commit
(`0f90959d5`, with the `D-PEC-100` row) so it can be reworded or dropped.

## 4. Verifier verdict

M1: **PASS WITH NOTES** (`CLOSEOUT_POST_SCA005_2026-09-27/M1_VERIFIER_VERDICT_01.md`,
brief `M1_VERIFIER_BRIEF.md` `e252760d…8dfb8b`). All five checks pass: 33 MEMORY paths plus
the brief copy only; created files equal the template plus the tabled rows in order; row
text byte-identical per packet with correct slots and resolving links; DEL-01-03 and
DEL-01-06 preimages are exact prefixes; `git diff --check` clean. Notes: N1 the D-PEC-96
row (above); N2 link text is the manager's uniform choice; N3 `RECEIPT.md` is absent until
HELP_HUMAN writes it. The verifier covered commits `25c5f403b` and `0f90959d5`; the later
commits add only `_Coordination/**` records and this return, and touch no `MEMORY.md`.

## 5. Checks

`CLOSEOUT_POST_SCA005_2026-09-27/CHECKS.md`: strict registers (0 ERROR / 26 WARNING, exit
1), harness self-check (exit 0), `validate_pec_loop_receipts.py` (exit 0) and both
`taskmgmt validate` runs (PASS) give byte-identical output before and after; `git diff
--check` clean. The harness was rerun at the final candidate (see hand-back).

## For HELP_HUMAN to resolve

1. Write the central `RECEIPT.md` at
   `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md` (the
   33 MEMORY files link that exact path), complete the graph (C1, M1, F1; X1 COMPLETE) and
   STATUS, and apply or decline the graph text proposed in `C1_ACCOUNT.md` (X1-1, X1-2,
   F-C1, F-C3 and the carry additions S2-1 and F-C2).
2. Confirm, reword or drop the DEL-01-06 `D-PEC-96` row (commit `0f90959d5`).
3. Link the intake from the receipt; bring the three candidates to the owner for
   disposition (promotion, disposition and assignment are the owner's acts).
4. Carry in the receipt, for the next undertaking: RV1; the lapsed acceptances as
   re-review candidates; K3 with its trigger; the K2 carries (F-C3); the X1 parser-packet
   residuals; and the run-root `HANDOFF_STATE.md` files named in `C1_ACCOUNT.md` N-1 as
   carry sources.
5. Review and merge PR #1014 once the receipt, graph and STATUS are added and required CI
   passes.

## Limits

No lifecycle, acceptance, REVIEW or CHECKING act; nothing asked about CHECKING; no ruling;
no Task Management promotion or disposition; no write to any `ScopeOfWork.md`,
`_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, context, reference, register,
`v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**` or the work graph. One child
disclosed a momentary 902-byte scratch write to the system temp directory before
exporting `TMPDIR`, deleted at once, with no repository effect.
