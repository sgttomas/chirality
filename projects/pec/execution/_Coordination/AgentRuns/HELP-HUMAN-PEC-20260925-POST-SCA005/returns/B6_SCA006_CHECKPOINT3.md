# B6 return: SCA-006 checkpoint-3 preparation (final)

This is the final return from WORKING_ITEMS (Type 1) for brief B6, work-graph node R3 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`. It supersedes the interim return of the same path (`850ad9e0…66ac`, commit `e07bafedb`), which the host forced before C4 finished.

- **Brief:** `briefs/B6_SCA006_CHECKPOINT3.md`, read from `origin/main` `94e9255b6`. Its SHA-256, `8bdc718105f05dd2f72378e50fea246eb99a38a937938da72afa221bb8872df4`, was verified before any work.
- **Application date:** 2026-09-26, local date (America/Edmonton).

**Checkpoint-3 preparation is complete.** The audited poststate awaits the owner's checkpoint-3 acceptance. Nothing is accepted, no pointer has moved, and nothing is merged.

## PR

- **PR:** https://github.com/sgttomas/chirality/pull/943, branch `claude/pec-sca006-cp3-execution`. It is open and **not merged**. The head is the commit that adds this file; the verifier passed `a2698a907f76a4d1b4fff4cb70c813ba6bc72595` (verdict 02).
- **Branch history:** the branch was cut from `94e9255b6`. It merged `origin/main` `f90320c1d` (Root `D-GOV-48`, the `D-PEC-96` ruling and workflows wave 3), which overlaps no SCA-006 path.
- **Hunk approval:** the owner's approval gate for the hunk is satisfied.
- **Before merge (HELP_HUMAN):** review the three notices, add the `docs/STATUS.md` correction under `D-PEC-88`, and confirm that the paragraph shown to the owner equals applied `projects/pec/AGENTS.md` L261–272. Required CI must pass.
- **CI:** the early checks passed at each push. The "Update the PR base" message did not appear; the branch was refreshed by a merge at HELP_HUMAN's request.

## Instruction and authority sources (SHA-256)

- **Instructions:**
  - Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
  - `CLAUDE.md` `336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49`
  - `projects/pec/AGENTS.md` (basis) `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`
  - `agents/AGENT_WORKING_ITEMS.md` `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665`
- **Pinned scope-change edition** (read with `git show 4d5f7b911:…`; all three match the brief):
  - `WORKFLOW.md` `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90`
  - `resources/contract.md` `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02`
  - `resources/method.md` `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5`
- **Current `audit-decomp`** (C4):
  - `WORKFLOW.md` `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b`
  - `contract.md` `704929c7c006a20a5fbe3fc903d4f172e2edb4c6a451c4b6db40506b40004e75`
  - `method.md` `51a0c69b389d0c641f88e8faa7bebbc2b3650518eede8882436853c583308827`
- **Authority records:**
  - Group-2 `DECISION.md` `30aebd162e98cdc91923468852af6833feda84c3a3d9d3efe252dc8a87abf989`
  - `ACCEPTED_MANIFEST.csv` `b95634899a48ed081711cc75478c6e8b7a23cbcb1e36cd25a323e82a9c62bc52`
  - Group-2 `Handoff_State.md` `2c2aba062303598d5f4bf9a8963e41c7bf143259e96321123251c6fbe3c489c7`
  - Amendment-1 `DECISION.md` `15720eb1d25ade4e7cb5d62765824634318e0e956129a6e6c3ad30cdaf74777e`
  - Register row `D-PEC-97`
  - `D-PEC-96_RULING_2026-09-26.md` `852057f0ff6989e0b1180232424ff9fd8de434b3345c1d6c775e76b8defb399e` (on `origin/main` through PR #946)
- **Wider consultation:** none beyond these, the accepted SCA-006 package and the SCA-005 precedent.

## Preconditions

All passed before the first write (`CP3_EVIDENCE/precheck.py`, 0 fails):
- the live preimages, both `_LATEST.md` and the three A2 contexts matched;
- every group-2 manifest artifact had its listed hash;
- `D-PEC-97` and amendment 1, with its §"Verification rule", were on fetched `origin/main`.

The reliance-hold preflight returned `ALLOW` on all 66 runs: 22 write targets under each of `exact-correction-preparation`, `candidate-validation` and `dispatch-for-production`.

## Written files (preimage → postimage)

| Path | Preimage | Postimage |
|---|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b8479…9660` | `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` (pre-acceptance form) |
| `…/_Decomposition/ScopeLedger.csv` | `83152a94…d9df` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `…/_Decomposition/Deliverables.csv` | `b8628fc4…d65a` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `…/_Decomposition/ContextBudgetQA.csv` | `2a194105…eb0df` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `…/_Decomposition/Companion_Inventory.csv` | `7c8a24a8…6ef8` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| `projects/pec/docs/PRD.md` | `fff27a66…dfc32` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| DEL-04-03 `_CONTEXT.md` | `a505c268…63da` | `b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22` |
| DEL-08-01 `_CONTEXT.md` | `151e1e34…3985` | `74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22` |
| DEL-08-03 `_CONTEXT.md` | `4644758f…c73d` | `95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5` |
| `projects/pec/AGENTS.md` | `c9d3b44d…197a` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml` | new (draft `852b1d5b…`) | `2b29af181947ba0ed75cd83a286c56a2863802d1d6a7e5b3ca9ab82330cdee74` |
| `execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (draft `43cfa318…`) | `b3c60bf489e41d45465bd38a0a7f3f3ca73ea4d392f987eff84a95bd888fc601` |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (draft `eb927e1f…`) | `af4f63426b55a96c4f18fee702b9af8eb5394b2b531dfddef3f8f090622f68ef` |
| `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (draft `385e5e2f…`) | `e883efac1829f0f2a10cceae778c92cd6baec6a37d1f4e6349442dd4c8f7bb93` |
| `SCA-006…/Supersession_Map.csv` (accumulator) | new | `010ce5c423530123f923413dbfad03ce70fc0ba0c072ee7726f7718847caab92` |
| `SCA-006…/Post_Change_Coverage.json` | new | `b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0` |
| `SCA-006…/RUN_SUMMARY.md` | new | `690b4923e7e7f7e62c25a6db35540e0e6b8bcd1276fbaa69dc078cf2b70c9b62` |
| `SCA-006…/AGENTS_MD_AMENDMENT1_DIFF.md` | new | `8b2386415b79f7666c5561873d8ce7b8a753d805c5e4bfbd1800fa5824206d4f` |
| `SCA-006…/Decision_Log.md` | `893c14ad…55b7` | `96cc5602…38c7` (SCA006-G2-A1 `HUNK APPROVED`; SCA006-CP3 `PREPARED / AWAITING_OWNER`; package hashes) |
| `SCA-006…/Handoff_State.md` | `a5f80525…8f1e` | `89af74b8…cfde` (checkpoint-3 section appended) |
| `SCA-006…/CP3_EVIDENCE/*` | new | scripts, `C4_3_REVIEW.md` `1ee6fe93…7035`, `c1_result.json`, `c3_result.json`, `c5_result.json` |
| `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/*` | new | 11 files; `coverage_summary.json` `b9a068c0…`, `RUN_SUMMARY.md` `f97bde4e…6499` |
| `returns/B6_VERIFIER_VERDICT_01.md`, `…_02.md`, this file | new | — |

All checkpoint-1 and checkpoint-2 artifacts are byte-unchanged; C1 checks them. No A3 or A6 write was made.

## Slot values

- **Decomposition.** `date:` (L7), the §7 Revision row (L574) and the DL-21 cell (L700) are `2026-09-26`, the application date the brief directed. The `status:` and `accepted:` lines are in their pre-acceptance form.
  - The first token of `accepted:` is the **fourth acceptance-date slot**. At A6 it takes the checkpoint-3 acceptance date.
  - If acceptance is later than 2026-09-26, A6 substitutes that date at all four slots, under the preview's slot rule.
  - For acceptance on 2026-09-26, the post-A6 file hashes `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`.
- **PRD.** S1–S4 are `2026-09-25` and the group-2 token is `SCA-006_GROUP-2_2026-09-25` (act-date values). The written file is byte-equal to the candidate.
- **`AGENTS.md`.** L6 `amended:` is `2026-09-26`; the L209 group-2 token is unchanged.
- **Manifest:**
  - ID, file name and notice dates use `20260926` / `2026-09-26`, and `date: 2026-09-26`.
  - `basis: 94e9255b68d6cda15926c7ee0187d6e9a759a43b`.
  - CP2-ACT is `'SCA-006 CP2: accept; Q1 a; Q2 a'`; CP2-VARIANT is `AGENTS.candidate.md` with I1.
  - `authorization_date: 2026-09-25`, the CP2 act date; HELP_HUMAN confirmed it.
  - `m6_notice.disposition: routed`.
  - One named addition, `group2_amendment_1`. At HELP_HUMAN's direction, and because the manifest is unmerged, it was updated in place to record the approval (first written as `f7f48690…`). The draft reverse proof still yields `852b1d5b…`.
- **Notices.** The manifest-path date part is `20260926`; the group-2 token is unchanged. Each has one named amendment-1 addition.

## The amendment-1 hunk (verbatim; approved by the owner)

It replaces `CP2_CANDIDATE/AGENTS.candidate.md` L261–270 (live preimage L241–250). In the applied file it occupies L261–272:

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

**Owner approval.** 2026-09-26, verbatim "approve hunk". HELP_HUMAN relayed it after presenting the exact paragraph, the dropped clause and COV-083. The act is recorded as HELP_HUMAN's K-AUTH-1 transcription in:
- `Decision_Log.md` SCA006-G2-A1;
- the manifest `group2_amendment_1.owner_hunk_approval`;
- `RUN_SUMMARY.md` §3.2.

The approved bytes are `4400c4e9…139c`.

**Disclosures:**
- The candidate clause "its graph accounts for the Remaining items it touches" was dropped. That was a judgment.
- The positive update duty became a restriction ("Update an item only under the packet…"), and "changes" became "affects". An undertaking holding a grant therefore has no explicit duty left to update an item it completes.
- COV-083: revision 1.6's SOW-094, DEL-01-06 and §9 text still says PEC's row "declares `remaining-loop` now". This contradicts the hunk and the `D-PEC-96` ruling, and is left for a later scope change (Q-CP3-1).

## Lane C results (final, at the merged head)

| Check | Result |
|---|---|
| C1 containment (`c1_containment.py` over `git diff --name-status f90320c1d HEAD`) | exit 0; every changed path allowed (47 at `a2698a907`; this return and verdict 02 are allowed B6 return paths); 34 hash checks pass (14 planned postimages + 20 frozen, including both `_LATEST.md`); no deletion |
| C2 registers (`--strict`) | exit 1 by design. 0 ERROR; 2 DRB-008 (DEL-08-06, DEL-10-13; planned); 26 XRG-013 from Root `D-GOV-48`. The XRG-013 findings are pre-existing: the same 26 revision-1.5 OUT/TBD IDs without a PackageID. SOW-097..100 are IN with packages. The owner defers action (PEC's D-GOV-48 notice). At the pre-merge basis: 0 ERROR and exactly 2 DRB-008 |
| C2 closure | 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs; unchanged |
| C3 | 31/31 PASS: 100 scope items (74/18/8); 68 deliverables (64/4); envelopes 28/34/2/0; union 64/64; PKG-04/08/10 7/8/13; issues 10/3; 29 terms; 6 objectives unchanged; 49 PRD requirements; K-01, K-02, K-11 and the P1 row byte-identical |
| C4 audit | `COV_SCA006_POSTCHANGE_2026-09-26_0051`: `WARNINGS` / `WARN`, with 0 BLOCKER, 3 pre-existing WARNING, 71 INFO and 12 EXPECTED_CONSEQUENCE |
| C4.3 review | fresh `pec-reviewer`: PASS WITH MINOR, 0 BLOCKING (`CP3_EVIDENCE/C4_3_REVIEW.md`, verbatim, with dispositions) |
| C5 | exit 0; every §C5 artifact present and hashed; the state fields are present in `RUN_SUMMARY.md` and in the `Handoff_State.md` checkpoint-3 section |
| A4 checks | `validate_instruction_entrypoints.py` PASS; G4 CI mode PASS (126 manifests); G4 `--added-manifests-only` PASS (1 instruction-surface path, 1 added manifest); `validate_pec_loop_receipts.py` VALID; pytest 33 passed; harness self-check exit 0 with no finding on a changed file |
| `git diff --check` | exit 2, only because of the accumulator's CRLF output in `Supersession_Map.csv` (46 lines), as in SCA-005's map; with that file excluded, exit 0. The interim return's "clean" was measured before the map existed |

## Audit and its reading

- **Baseline:** `COV_SCA005_POSTSETUP_2026-09-25_1606`.
- **D-PEC-95 attribution:** COV-068, COV-069 and COV-072 are resolved by `D-PEC-95` (N2 for the first two, N3 for COV-072), not by SCA-006. COV-073 is partial: N1 made the pointers current, and the residual is carried as COV-086 INFO.
- **The 12 EXPECTED_CONSEQUENCE rows** each cite `D-PEC-97` plus a plan section:
  - B1: the two folders;
  - B3: exactly DEP-09-06-003 and DEP-10-03-003;
  - B7: 63 contexts and 66 references;
  - A2: COV-079;
  - B2: COV-080;
  - A6/A1: COV-084;
  - A5: COV-085.
- **New INFO findings:**
  - COV-083: the `remaining-loop` text;
  - COV-001 and COV-002: first run of `audit_structure.py`; pre-existing.
- **Coverage:** forward deliverable coverage is 97.06% (66/68), because the two B1 deliverables have no folders.

## Closure state fields

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `IN_PROGRESS` |
| `AuditState` | `WARNINGS` |
| `ReadyForNextPhase` | `NO` |

Closure verdict: `OPEN_PENDING_DERIVATIVE_CLOSURE`. It becomes `CLOSED_FOR_SCOPE_CHANGE_ONLY` only on the owner's checkpoint-3 acceptance.

## Checkpoint-3 question set (`RUN_SUMMARY.md` §9)

**Q-CP3-A: accept the audited poststate. Recommendation: accept.** The acceptance covers:
- the live decomposition `3ef0412a…9b29`, with post-A6 hash `9374c21f…08eb1` for acceptance on 2026-09-26;
- the registers `1d24a4b8…`, `94ee5d18…`, `93b0bb07…` and `1597ceec…`;
- PRD v2.4 `ae49b806…`;
- `AGENTS.md` `4400c4e9…`, with the approved hunk;
- the audit (verdict `WARNINGS`, 0 BLOCKER);
- the closure fields above;
- the Lane B consequences B1–B8, which stay `FROZEN`.

On acceptance, HELP_HUMAN performs A6: both pointers move, the front-matter lines are restored, and the four date slots take the acceptance date.

| # | Choice | Options | Recommendation |
|---|---|---|---|
| Q-CP3-1 | The revision-1.6 `remaining-loop` text (COV-083), which contradicts the approved hunk and the `D-PEC-96` ruling | (a) accept, knowingly carrying the drift, and correct it in a later PEC scope change (the ruling already routes it there and to S2); (b) return to checkpoint 2 to add the correction, which needs a new group-2 act | **(a)** |
| Q-CP3-2 | `_Evaluation/DecompCoverage/_LATEST.md`, which `D-PEC-97` does not open | (a) name it in the acceptance so HELP_HUMAN moves it to `COV_SCA006_POSTCHANGE_2026-09-26_0051` with A6 (0 BLOCKERs); (b) leave it for a later packet | **(a)** |

Nothing asks about CHECKING.

## Verifier verdicts

- **`returns/B6_VERIFIER_VERDICT_01.md` (head `9a8b7150d`): BLOCKING.** There was 1 BLOCKING finding: the A6 instructions and the post-A6 hash omitted the `accepted:` acceptance-date slot, and the old hash `86de50c3…` mixed two dates. There were also 1 MINOR finding (the hunk record overstated what it keeps) and 6 NOTEs. The repairs touched records only; no Lane A byte changed.
- **`returns/B6_VERIFIER_VERDICT_02.md` (head `a2698a907`): PASS.** Every finding was resolved or dispositioned, with 2 non-blocking NOTEs:
  - N1: the rollback note could also mention the Root and App notices. The plan's tranche revert already covers them.
  - N2: `c1_result.json` records 46 paths, within its stated scope; one line in the diff record exceeds 79 characters.
  - The manager did not act on these, to avoid disturbing the verified bytes.

## Containment

Every write is inside the brief's boundary:
- Lane A (A1, A2, A4);
- the SCA-006 snapshot folder;
- the `COV_SCA006_POSTCHANGE_*` folder;
- the B6 return and verdict files.

Nothing was written to:
- `_LATEST.md`, `checkpoint_snapshots/**` or `*_AUTHORIZED.md`;
- any SOW, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` or `Dependencies.csv`;
- `v2/**`, `software-workflow.json` or `_DomainEngines/**`;
- `loop/**`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**` or the work graph.

No Lane B item was performed, no lifecycle changed, no Remaining section was retired, and no CHECKING, ISSUED or acceptance was claimed.

## For HELP_HUMAN to resolve

1. **Owner checkpoint-3 decision:** Q-CP3-A, Q-CP3-1 and Q-CP3-2.
2. **Before merge:**
   - review the notices;
   - add the `docs/STATUS.md` `D-PEC-88` correction;
   - confirm the paragraph presented to the owner equals applied `AGENTS.md` L261–272;
   - let required CI pass.

   After those additions, an independent review of HELP_HUMAN's own commits is still needed.
3. **A6 after acceptance:** follow `Handoff_State.md` §"A6 instructions". There are four acceptance-date slots, and the post-A6 hash is `9374c21f…` if acceptance is on 2026-09-26.
4. **Root `D-GOV-48` XRG-013:** the 26 pre-existing warnings are deferred by the owner. If PEC CI runs the strict validator, it now reports them on `main` as well.
5. **Follow-up scope change:** the `remaining-loop` decomposition text (COV-083; `D-PEC-96` graph node S2).
6. **Stray file:** the audit child reported a gitignored `tools/evaluation/__pycache__/audit_common.cpython-313.pyc` (00:52). It is untracked and ignored; the child believes it did not create it. It was left alone.

## Delegation record

| Child | Mechanism | Parent | Basis supplied | Write scope | Enforcement | Return |
|---|---|---|---|---|---|---|
| C4 audit (TASK) | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus` (Opus 5.5), background | this WORKING_ITEMS | inline brief: the current `audit-decomp` hashes, settings, classification rules, `ACCEPTED_DECISIONS` | `COV_SCA006_POSTCHANGE_2026-09-26_0051/` only; no Git state change; no `_LATEST.md` | instruction-asserted; verified afterwards by containment (C1) | 11 files, hashes listed in its return; 0 BLOCKER; completed 01:14, and the manager committed them |
| C4.3 review (TASK, read-only) | Agent tool, `subagent_type: pec-reviewer`, `model: opus`, fresh | this WORKING_ITEMS | the candidate at `c5efad489`; the accepted records | none | tool-enforced (no write tools) | PASS WITH MINOR; saved verbatim |
| Independent verifier (TASK, read-only) | Agent tool, `subagent_type: pec-reviewer`, `model: opus`, fresh; round 2 by resuming the same instance | this WORKING_ITEMS | brief B6, candidate `9a8b7150d`, then `a2698a907` | none | tool-enforced | verdict 01 BLOCKING, then verdict 02 PASS; saved verbatim |

HELP_HUMAN's messages relayed the following: the audit-child notice, the slot confirmations, the owner's "approve hunk" and its presentation, the D-GOV-48 and D-PEC-96 basis points, and the direction to update the manifest block. The manager sent HELP_HUMAN one flag, the COV-083 tension, before the approval.
