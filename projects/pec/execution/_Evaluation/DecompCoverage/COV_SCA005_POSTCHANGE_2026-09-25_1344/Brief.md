# Brief — AUDIT_DECOMP post-change validation (SCA-005 checkpoint 3, Lane C4)

The WORKING_ITEMS manager of node B3 dispatched this run. B3 belongs to
HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, which is preparing SCA-005
checkpoint 3 (scope-change workflow step C4). The run went to a Type 2 TASK
instance executing `chirality-root:bundled:workflow:audit-decomp`. Type 2 does
not delegate. The model steer was claude-opus-5-5 at high reasoning (D-PEC-86
I-8). The host reports the model as Opus 5.5 (`claude-opus-5-5`). This report
records that identity as the runtime exposes it and does not treat the steer as
evidence of the model used.

## Parameters (as supplied, normalized)

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`. This is revision 1.5, applied during SCA-005 checkpoint-3 preparation. Its front matter reads `status: candidate_pending_checkpoint_3`. Expected live SHA-256 `37ea1084…a6cc` |
| Companion registers (live) | `ScopeLedger.csv` `83152a94…fd9df`; `Deliverables.csv` `b8628fc4…3d65a`; `ContextBudgetQA.csv` `2a194105…eb0df`; `Companion_Inventory.csv` `7c8a24a8…6ef8` |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA005_POSTCHANGE` |
| Output folder (exact name, supplied) | `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/` |
| `REQUESTED_BY` | `SCOPE_CHANGE` (WORKING_ITEMS, SCA-005 checkpoint-3 preparation, Lane C4) |
| `PRIOR_RUN_LABEL` | `COV_SCA005_PRECHANGE_2026-09-23_2139`. Its `coverage_summary.json` hashes to `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` (verified) |
| `EXPECTED_SOURCE_SNAPSHOT` | The SCA-005 candidate revision 1.5 (expected revision `1.5`). It was applied under the owner's checkpoint-group-2 acceptance of 2026-09-25, recorded in `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md` and register row D-PEC-92, with Lane A4 deferred. The candidate SCA snapshot is `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/` |
| `EXPECTED_HANDOFF_PHASE` | SCA-005 checkpoint-3 post-change validation before pointer movement |

## Expected pre-acceptance posture, as briefed (not defects)

The brief listed these conditions as expected. Each one had to be classified,
not suppressed:

- **Pointers have not moved.** `_Decomposition/_LATEST.md` names revision 1.4
  and `_ScopeChange/_LATEST.md` names SCA-004. The decomposition front matter
  carries the candidate status and a pre-acceptance `accepted:` line.
- **Lane A4 is deferred.** DEL-02-08 and DEL-02-09 (SOW-095, SOW-096) have
  register rows but no folders.
- **Lane B3 is not opened.** The dependency registers are pre-B3:
  - 119 execution edges and 0 SCCs
  - DEL-00-03 and DEL-01-05 are isolated
  - `DEP-09-05-005` still runs to the retired DEL-06-04
- **Four deliverables are retired.** DEL-06-04, DEL-07-02, DEL-07-04 and
  DEL-07-05 keep their rows and folders, and their `_STATUS.md` reads
  `RETIRED`. The plan expects this representation to raise no blocker and at
  most INFO. This run confirms or refutes that on the real files.
- **B1 and B4 are open downstream work.** 40 `_CONTEXT.md` and 64
  `_REFERENCES.md` provenance lines still name revision 1.4, and the SOWs are
  not refreshed. The run observed 42 contexts, not 40; see COV-072.

Every finding is classified as `DEFECT`, `EXPECTED_CONSEQUENCE` (with the
decision clause that makes it expected), or `PRE-EXISTING` (also present in
the PRECHANGE audit).

## Required outputs

The workflow's canonical outputs are all required. The run also adds a
pre/post comparison (`PrePost_Comparison.md`). `coverage_summary.json`
carries `overall_status` and `closure_readiness`.

## Sealed boundary

- Write only inside this folder.
- Do not update `_Evaluation/DecompCoverage/_LATEST.md`. This brief overrides
  the protocol's pointer-update step.
- Do not modify any decomposition file, register, `_ScopeChange` path,
  deliverable file, decision, receipt, source, `v2/**` path or foreign path.
- No git commit, stage, push, stash, reset or checkout.
- Use read-only tools and deterministic read-only scripts only. Scratch output
  goes to the session scratchpad.
- Run the PEC reliance-hold preflight before writing, and stop if the result
  is not `ALLOW`. The result was `ALLOW`; see `QA_Report.md`.
- This snapshot is derivative evidence. It accepts nothing and authorizes
  nothing.

## Instruction and method basis (SHA-256, verified before loading)

| File | SHA-256 | Brief value |
|---|---|---|
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` | match |
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | match |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` | match |
| `workflows/audit-decomp/WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` | match |
| `workflows/audit-decomp/resources/contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` | match |
| `workflows/audit-decomp/resources/method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` | match |

No other role instructions were consulted. The scope-change method was not
loaded. For Check 10, the SCA-005 artifact set was taken from the accepted
`Propagation_Plan.md` §A5/§C5, not from the scope-change contract.

## Audited inputs (SHA-256, live bytes)

| File | SHA-256 | Brief / accepted value |
|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc` | matches the brief. It differs from the accepted CP2 postimage `dc2b8479…9660` only in front-matter lines 5 and 8 (the pre-acceptance lines) |
| `_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` | matches the brief and the CP2 postimage |
| `_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` | matches the brief and the CP2 postimage |
| `_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` | matches the brief and the CP2 postimage |
| `_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` | matches the brief and the CP2 postimage |
| `_Decomposition/_LATEST.md` | `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3` | pre-acceptance value (revision 1.4) |
| `_ScopeChange/_LATEST.md` | `721a14dc27b4b595be79f591f49b7374a121c52a77eb0451d32d9aa32a9e6280` | pre-acceptance value (SCA-004) |
| `_Evaluation/DecompCoverage/_LATEST.md` | `0084d218b6106482dbf3f73933d44de5ed43c15b8515b48c70b098c985df7432` | not updated by this run |
| `projects/pec/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` | equals the adopted v2.3 candidate |
| group-2 `DECISION.md` | `ca88f6a8f9bca197f64a56f07c73364cd8f7533acb7bf64206a34e0e1fba3d66` | — |
| group-2 `ACCEPTED_MANIFEST.csv` | `10d2c250e2d2daf3d5f43a145c3fbcaf29863f16b005c47dd5999fbd7788b9dc` | — |
| `SCA-005_2026-09-23_2139/Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` | equals the accepted manifest value |
| `SCA-005_2026-09-23_2139/Supersession_Map.csv` | `4ca705ba090cafb9a74870a0095be490c1d507149767dac32ec52879c487240c` | — |
| `_Coordination/ACTIVE_RELIANCE_HOLDS.csv` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` | header only |

**Git basis.** The first scan found the Lane A1–A3 writes uncommitted in this
worktree (branch `claude/pec-sca005-cp3-execution`, base `2b0572fe0`). During
the run the caller committed them as `5d2770350ceb3469182929bef5db516a1d2e5403`.
It then added `7e8374ae2bc9cbd099e8ebfd3109751bef7c6b33`, which adds only an
AgentRuns return file outside the audited paths. On re-verification the
working tree was clean, and a second census over the committed state gave the
same result (see `QA_Report.md`). The audited bytes are therefore those of
commit `5d2770350`.
