# RV1 — REVIEW of the D-PEC-105 bytes for DEL-00-01 and DEL-00-03 — run manifest

- **Undertaking / node:** `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, node RV1
  (graph `../WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md`).
- **Manager:** WORKING_ITEMS (Type 1) under HELP_HUMAN; brief
  `../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/RV1A_D1_REVIEW.md`
  (`3212458cbeabd09d5590c5a9efc694f087f3c4b8b35c38909ef2ccd478ad5d32`, copied
  unchanged). The host reports the serving model as Opus 5.5
  (`claude-opus-5-5`); roles and the high reasoning effort are
  instruction-asserted.
- **Branch / base:** `claude/pec-rv1-d1-review`, cut from fetched
  `origin/main` `acc7d3cc7f5183152752c35995c73ad34673011b` (PR #1018 merge,
  `D-PEC-107`).
- **Date:** 2026-09-27.

## Authority and instruction sources (SHA-256 as read)

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` (manager role) | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `agents/AGENT_TASK.md` (read by the TASK performers) | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md` §"RV1 authorization", §"Freeze point" | `403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346` |
| `_DECISIONS/D-PEC-105_RULING_2026-09-27.md` (RR1) | `401c2419ba26c8a43610d8416663e745a80d8061363d5abb73459dea931bd0ef` |
| `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md` | `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f` |
| Root `docs/SPEC.md` (§3.4) | `feb5e79c0b60b5156ea9ad2b00e32e338ab42c4351da0b0cbca6f30df5f3109e` |
| `D1_PREMISE_AMEND_2026-09-27/HANDOFF_STATE.md` (items 6–7) | `a893885a90e1686fde5f3e0324e617ad3697e56a887ddc3566448ccbc71b8c20` |
| `_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md` (CAND-PEC-2026-09-27-01) | `e2ccf3e33b6636c46afe3fe68eff586f22141b405364bcb6b6eeefd63077818a` |
| `TM-PEC-014_SPEC_CURRENCY_2026-08-09/REVISION_01_RF-002_RF-003_2026-08-09/OWNER_CUSTOM_CU-001.json` | `36ec35f3869f02e935c21b62a767309c8763afbd97ff5f13e515da6e44507dc3` |

Owner confirmation relied on, verbatim (`D-PEC-107`): "Yes I still want you
to complete the task management work and the RV1."

## Method basis

The bundled `review` workflow **as of commit `2f825f180`**, read only with
`git show 2f825f180:<path>`:

| File | SHA-256 |
|---|---|
| `workflows/review/WORKFLOW.md` | `f8a8f240a034395dd1d069799449215eca29ce14887a20653f1cec9a674906bc` |
| `workflows/review/execution.json` | `d1c668ae85f9f5a0edf2ecb312a449e21aa9101f99da9997fc4a7805677074df` |
| `workflows/review/resources/contract.md` | `d3d7eb27993068fbdf4ea3b06c78a19106ff4d145f149d5cf50040756144b328` |
| `workflows/review/resources/method.md` | `63c8a3959cd6286f95acf30ae87e42a5dd99d951b2ae2ab3ec6212a81f930daa` |

The revised edition (`77dbfcb72` onward; CHECKING-entry, frozen-SHA, Gate 5
and reversal rules) was not read or applied. Tools used (SHA-256):
`tools/scope_of_work/derive_review_checklist.py` `bfb64dc9…0109`,
`tools/scope_of_work/validate_scope_of_work.py` `f0f10590…fecfe`,
`tools/scaffolding/create_snapshot_folder.sh` `7db42ee6…5640`,
`tools/scaffolding/update_latest_pointer.sh` `21899520…15bc`,
`tools/validation/validate_decomposition_registers.py` `5442049e…26f5`,
`tools/practitioner_harness/harness.py` `01a9b954…61f3`,
`tools/validation/validate_pec_loop_receipts.py` `8eb62995…bad9`,
`execution/_Scripts/pec_reliance_hold.py` `b1712e4b…d0e`.

### Substitutions and precedent (manager level)

1. **Gate 1 `audit-decomp` TASK.** A Type 2 performer cannot delegate. Each
   performer used the strict register validator plus a direct identity check
   of `_CONTEXT.md`, the SOW and the decomposition registers, as the nearest
   current equivalent (recorded in each `_REVIEW.md`).
2. **Who writes the review files.** The old method has WORKING_ITEMS write
   `_REVIEW.md`, `Review_Findings.csv` and the snapshot. The two performers
   drafted them in their own scratch directories; the manager placed them
   with only these edits: the snapshot name filled in for the
   `{SNAPSHOT_NAME}` placeholder, and one sentence in each `_REVIEW.md` naming
   where the evidence and snapshot are filed.
3. **Review-type rows.** The old method gives no ID format for `SELF_CHECK`
   or `PEER_REVIEW` focus rows; they are review-local `SC-*` and `PEER-*`
   rows, not `CU-*` items.
4. **Gate 5 and snapshot finalization.** Following the 2026-08-09 precedent,
   no transition is attempted and Gate 5 is not entered. The old method ties
   snapshot finalization and the pointer move to the Gate 5 decision; as in
   that precedent, each snapshot was finalized after the review
   (`create_snapshot_folder.sh`) and the pointer moved to the newest snapshot
   (`update_latest_pointer.sh`, then rewritten in the precedent's narrative
   form with the same `Latest:` and `Updated:` lines).
5. **Deferral.** No CRITICAL or MAJOR finding is proposed or recorded as
   `DEFER`/`DEFERRED` (root `docs/SPEC.md` §3.4), although the `2f825f180`
   edition would allow it.
6. **Human gates.** Gate 1 human input is `D-PEC-107`; no new owner
   confirmation of either checklist was given; every new finding is
   `AGENT_CHECK` with `HumanDisposition=TBD`.

## Review type, performers and independence

Delegation mechanism: Claude Code harness-native descendants (`D-GOV-35`),
launched by this manager with the Agent tool, `subagent_type` `pec-task`,
model `opus` (host-reported Opus 5.5), in the foreground; each created files
only in its own `mktemp -d` directory under the session scratchpad with
`TMPDIR` exported and `PYTHONDONTWRITEBYTECODE=1`; neither ran `git fetch`
or wrote to the repository (one exception, below).

| Deliverable | Review type (as the prior acceptance) | Performer identity | Brief | Scratch dir |
|---|---|---|---|---|
| DEL-00-01 | `SELF_CHECK` (owner replacement ruling of 2026-08-01) | `REVIEW-SELF-DEL-00-01-20260927-RV1` — fresh Type 2 TASK on the producer side; not independent review; authored none of the `D-PEC-105` bytes | `briefs/RV1_SELF_CHECK_DEL-00-01.md` `4e41ac4c…9ea83` with `briefs/COMMON_REVIEW_TASK.md` `3b48557d…3cd6` | `rv1-selfcheck-0001.HqYj70` |
| DEL-00-03 | `PEER_REVIEW` (owner ruling of 2026-08-09) | `REVIEW-PEER-DEL-00-03-20260927-RV1` — fresh Type 2 TASK, agent-performed as the prior PEER_REVIEW was, independent of the `D-PEC-105` authors (it authored, drafted, verified or reviewed none of those bytes or that packet); findings labelled `AGENT_CHECK` | `briefs/RV1_PEER_REVIEW_DEL-00-03.md` `55a3d25d…14db52` with the common brief | `rv1-peer-0003.9trXkn` |

**Boundary incident (disclosed).** Before it began logging, the DEL-00-03
performer ran the two tools' `--help` once without
`PYTHONDONTWRITEBYTECODE=1`, which wrote the gitignored
`tools/scope_of_work/__pycache__/common.cpython-313.pyc` into this worktree.
No tracked file changed and no reviewed byte or check was affected. The
manager removed the cache directory; `git status --ignored` then showed no
ignored or untracked residue outside the RV1 paths.

## Bytes reviewed (verified before dispatch; unchanged at the end)

| Deliverable | File | SHA-256 |
|---|---|---|
| DEL-00-03 | `artifacts/v2/SPEC.md` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` |
| DEL-00-03 | `ScopeOfWork.md` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` |
| DEL-00-01 | `artifacts/v2/ADRs.md` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| DEL-00-01 | `ScopeOfWork.md` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` |

## Checklists

`derive_review_checklist.py --output checklists/checklist_<DEL>.json <DEL folder>`,
run twice from the repository root (CPython 3.13.7), exit 0, byte-identical;
both equal the `D-PEC-105` proposal's expectation, so no difference needs
explaining. Both SOWs validate `PASS format=SOW_V1`.

| Deliverable | Criteria | SHA-256 |
|---|---|---|
| DEL-00-01 | 7 | `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |
| DEL-00-03 | 11 | `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1` |

## Reliance-hold preflight

`evidence/reliance_hold_preflight.out`: register
`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` (header
only), script `b1712e4b…d0e`; each of the four targets with
`candidate-validation` (the matching review operation) and
`dispatch-for-production` (run additionally at dispatch): `ALLOW`, exit 0, ×8.

## Results

| Deliverable | CRITICAL | MAJOR | MINOR | OBSERVATION | Owner-only criterion |
|---|---|---|---|---|---|
| DEL-00-01 (`SELF_CHECK`) | 0 | 1 open (RF-001, AC-002) | 3 open (RF-002, RF-003, RF-005) | 1 open (RF-004) | AC-007 unsatisfied — READY FOR OWNER DECISION |
| DEL-00-03 (`PEER_REVIEW`) | 0 | 0 new (RF-001..003 historical, resolved) | 2 open (RF-004, RF-005) | 5 open (RF-006..RF-010) | AC-011 unsatisfied — READY FOR OWNER DECISION |

CU-001 (DEL-00-03) is not carried as an active item; it is kept as history
(its revision-1.4 totals no longer describe the rebound bytes, and an agent
may not restate an owner custom item). Every new finding is `OPEN`,
`HumanDisposition=TBD`. Any correction is recorded only, not prepared
(`D-PEC-107` §"Freeze point"); a `ScopeOfWork.md` or artifact change needs an
owner-ruled correction packet before re-acceptance.

## Written paths

Listed with their SHA-256 in `SHA256SUMS` beside this file (paths relative
to `projects/pec/execution/`).

## Checks (candidate against `origin/main` `acc7d3cc7`)

Baselines were run in a clean detached worktree at `acc7d3cc7` (removed
afterwards); candidates in this worktree. Outputs are in `evidence/checks/`
(the receipt validator's absolute root is written as `{REPO_ROOT}`).

| Check | `origin/main` | Candidate |
|---|---|---|
| `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | exit 1; 0 errors, 26 warnings | identical output |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0 | identical output |
| `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0, VALID | identical output (modulo the root path) |
| `git diff --check` | — | clean |

## Limits

No `_STATUS.md`, `ScopeOfWork.md`, artifact, `MEMORY.md`, register,
dependency, context, reference, graph, STATUS, `_DECISIONS/**` or foreign
write. No lifecycle change; no CHECKING, ISSUED or Gate 5 act; no acceptance,
readiness, release or reliance claim. Nothing here prompts about CHECKING.
