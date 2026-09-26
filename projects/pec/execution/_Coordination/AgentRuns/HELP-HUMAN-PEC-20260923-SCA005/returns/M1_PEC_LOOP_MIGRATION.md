# M1 return — PEC development-loop migration tranche

- Run: HELP_HUMAN `HELP-HUMAN-PEC-20260923-SCA005`, node M1.
- Role: HELPS_HUMANS (Type 1), running under the `pec-manager` definition and serving `claude-opus-5-5`. The role is asserted by instruction, not enforced mechanically.
- Date: 2026-09-25.
- Brief: `M1_PEC_LOOP_MIGRATION.md`, supplied from the HELP_HUMAN session scratchpad. SHA-256 `d42f55db4456671052b46b17f0f0e061675d94d5fe5ff6f7dae29be28a60cfdf`, recomputed on receipt. The brief file is not committed in this repository.
- Role file consulted: `agents/AGENT_HELPS_HUMANS.md`, SHA-256 `a0c9fb9443d8671d694c1f7b24ff3c402ffd626c781a2739342c938f2f3c3d1e`.
- Git: branch `claude/pec-loop-migration`, cut from fetched `origin/main` `eb56e108377c102ded295a39abcf91986da247aa`. That commit contains the required base.
- PR: #917, https://github.com/sgttomas/chirality/pull/917. It is open and was not merged, as the brief directs.

## 1. What changed

Before and after SHA-256 for each file:

| Path | Before | After |
|---|---|---|
| `projects/pec/loop/LOOP_INIT.md` | `ec9cc14df99dc627122ec99c6b5b5e9dffd26631445ebec42679205b49835053` | `c97d49fff5c2fabca1c9c05b44bcde958e46fccb067d512ce93779d4cfad821b` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` | `97e9cf896486cc22c6d770bb79892e6fef44358ffd1ab06fb52b13d61977e8bc` |
| `projects/pec/loop/LOOP_RECEIPTS.md` | `1c228c9fa1fed1fd01222c6bdb7a4b3ccd903cbdfe3b879bc9229af9c8da67fc` | `9f766eb47fd38b2a7f9f8547bc02a54954907d8a05086e2985967e9b6b1ad7ec` |
| `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml` | (new) | `0493968ff167a052f8a6b20354cc25d80d7499dc3f5e5f84b968d3dfd141e0d6` |
| `execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` (Root) | (new) | `37089888a6a59bc5b2f9a65c003a614d113b60cb624446510fd50b72a189ed3a` |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` | (new) | `b57341c8ca91fcf8dd68ad2e6b2c7934159858d44d9e8de24582307a5545e561` |
| `projects/chirality-piping/execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` | (new) | `d3e37286d3539346520a0c602d8ad23b4759dce25e43de2861ed7147554ed0b3` |
| `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` | (new) | `59a48d7162be58e19ce224f1c75d93f399280252bcb19dd0babfe7b7d3a81273` |
| `.../returns/M1_VERIFIER_VERDICT_01.md` | (new) | `d702aac0139b98ee4d82858ca3f328c2613fc667298bf8d3ca2a4536e2c4dc34` |
| `.../returns/M1_VERIFIER_VERDICT_02.md` | (new) | `3d4e1180ba7565a33def54a7d433d0c4952be6705329a9b2b0473544f3f9339a` |
| `.../returns/M1_PEC_LOOP_MIGRATION.md` (this file) | (new) | not self-hashable |

Two files in the brief's Produce list were deliberately left unchanged (see §2):

| Path | SHA-256 (unchanged) |
|---|---|
| `projects/pec/init/dev-loop-init-prompt.md` | `6bc8f2a5e7a905561ea92e7366ea769e3381681203c5571f64c0fd52bd623874` |
| `projects/pec/execution/_Coordination/_COORDINATION.md` | `8da03a2f0157ba097e4db5b34dff4cd68c03e69c5d0ec72f8a8f49c23d38879c` |

Commits, in order:
- `11be801130add3bbf2da6bcd19e18fd87ff1e4d3`: the tranche.
- `9a20c86d0`: repairs from verdict 01, plus the verdict 01 transcription.
- `2ae8b7f1acb0bbfe17df4ed126bea4b89b986137`: binds PR #917 into Receipt 197.
- A final commit adds this return and verdict 02.

## 2. Design choices

Items marked **[owner]** should be confirmed by the owner.

1. **LOOP_INIT is App's text with PEC pointers.**
   - It was generated mechanically from `projects/chirality-app-dev/loop/LOOP_INIT.md`.
   - Only the title, `WORKING_ROOT`, the `_Decomposition/_LATEST.md` pointer and the `NOTICE_*` pointer differ.
   - Steps 0–6 are byte-identical to App and Piping.
   - Why: highest fidelity, and the shared method stays identical across the three loops.
2. **The PRD version is not named in LOOP_INIT.** The pointer is `docs/PRD.md`; `AGENTS.md` names v2.3. Why: naming the version would make the evergreen file go stale at the next PRD.
3. **PEC-specific rules live in `AGENTS.md`, not LOOP_INIT.**
   - This covers the fences, checks, reliance-hold command, evidence contract, historical mapping, Remaining treatment, D-PEC-80 reading and selection clauses.
   - Why: App and Piping put project rules in `AGENTS.md`. It also keeps LOOP_INIT identical in its steps.
4. **Deliverable `## Remaining` sections stay but no longer select work.**
   - When an undertaking completes or changes an item, it updates that item under the packet that opens its `_STATUS.md`.
   - **[owner]** New open scope is recorded in the graph and its governing records, not as a new Remaining entry. This is a new PEC-local restriction. Retiring the sections, as App and Piping did, is left to a separate owner-directed undertaking.
5. **[owner] MEMORY rows stay under the PEC fence.**
   - A deliverable's `MEMORY.md` is outside PEC's default-writable surfaces. A run row therefore needs the governing `D-PEC` packet's path grant.
   - If no grant exists, the run is recorded in the graph and central receipt, and the missing grant goes to the owner. The graph completes only after the grant, or after the owner decides to complete without the row.
   - Why: the shared method assumes MEMORY writes are routine, and PEC's fence says otherwise. The owner may want a standing packet clause for terse MEMORY rows, which would amend the fence and so needs the owner.
6. **Receipt 197 closes the ledger.**
   - App and Piping stopped their ledgers without a closing receipt. Their manifests say only that existing ledgers "stay historical".
   - PEC appends a closing receipt, as the brief directs, and because its former procedure required a receipt at every closeout. `AGENTS.md` states this difference.
   - The ledger header's rule 2 (the ledger is "the one place chat-only directions become durable") is superseded in practice by the new owner-direction rule in `AGENTS.md`. The header itself is not edited.
7. **[owner] How D-PEC-80 is now read.** Its ruling text is not edited.

   | Item | Status after adoption |
   |---|---|
   | A: loop home, Task Management home, AgentRuns home | Stands |
   | B: generic instruction surface | Replaced by the evergreen LOOP_INIT. Its fences, checks and evidence contract move to `AGENTS.md`. |
   | C: per-iteration commit and receipt, one PR at terminus | Replaced by the graph's PR sequence and one central receipt |
   | D: workplan retirement and owner-intent record | Stands. The Step 0 mechanical plan check is retired; the no-plan rule stays. |
   | D: selection only from `## Remaining` | Replaced |

   The brief named only "Remaining selection and the per-loop receipt ledger" as superseded. Items B and C are also replaced in substance, so I stated them too.
8. **[owner] D-PEC-88 carry-over depends on D-PEC-94.** D-PEC-88 item 6 leaves to this migration whether the standing STATUS/README grant carries into the migrated loop. The texts therefore say that D-PEC-94 records that disposition. While D-PEC-88 applies, its trace clause (item 4) is met by naming each change in the graph, carrying it into the central receipt, and reviewing it with the PR.
9. **Shared Runtime Boundary.**
   - `AGENTS.md` records that D-GOV-43 supersedes D-GOV-20 items 2–4 on the App MVP Codex path, as the ruled record states, and describes topology A2.
   - Reading D-T0-23 as amended is labelled an interpretation.
   - Agents in other hosts follow Root `AGENTS.md` and D-GOV-35.
   - "Daemon" became "Runtime and user-data state".
10. **Old protective clauses are carried into `AGENTS.md`.**
    - Old LOOP_INIT Step 1 rule: owner acts count only once observable on `origin/main`.
    - Blocking semantics for PREREQUISITE and SatisfactionStatus.
    - Hash recompute.
    - "A tracking row is not its ruling source."
    - Legacy rows do not revive retired work.
    - The decision-register routing rule.
    - Gate outcomes are recorded in the graph.
    - "Never record a ruling that did not occur."
    - Why: nothing protective should be dropped silently.
11. **Issue-Plan Rule.** The graph now records actionable issues. Homeless material concerns go to Task Management intake. This follows App.
12. **The launcher is unchanged.**
    - `projects/pec/init/dev-loop-init-prompt.md` must byte-match the tagged block in Root `init/dev-loop-init-prompt.md` §4 (`validate_instruction_entrypoints.py`).
    - Root `init/**` is outside my write boundary.
    - The only difference from the App and Piping launchers is their closing phrase "within the owner's steering and live authority". Aligning it needs a two-file change, disclosed in the Root notice.
13. **`_COORDINATION.md` is unchanged.** No present-current loop-description line becomes false. Its Provenance section still says revision 1.4 is `current_basis`, which is stale. The brief allows fixing that only in a section where a loop line changed, so I left it.
14. **Notices go to Root, App, Piping and Runtime.** The Root manifests routed notices to Runtime. The Root notice names SPEC §9.8, PRD_ROOT E-1, the 2026-09-22 amendment, the bundled graph workflow and template, and the alignment manual's row describing PEC.
15. **Manifest paths.** The manifest lists PEC and notice paths under `instruction_surface_paths`, following precedent. The G4 validator reports them as non-blocking over-declaration. The return and verdicts are listed under `candidate_paths`.

## 3. Check results

Commands run from the worktree root unless stated otherwise:

| Check | Result |
|---|---|
| `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | VALID, exit 0, at every candidate |
| `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | 0 errors, 0 warnings, exit 0 |
| `git diff --check` (tracked), `git diff --cached --check` (new files) | clean |
| `python3 tools/validation/validate_instruction_entrypoints.py .` | PASS. This also runs the structural-duplication check on LOOP_INIT. |
| `python3 tools/validation/validate_instruction_tranche_manifest.py` (CI mode) | G4 PASS: 113 manifests schema-valid |
| same with `--base origin/main --head HEAD --added-manifests-only` | G4 PASS (diff mode): 8 changed paths, 1 on the instruction surface |
| `python3 -m pytest -q tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` | 33 passed |
| `python3 tools/validation/validate_path_anchors.py` | PASS |
| `python3 tools/validation/validate_conflict_markers.py --base origin/main --head HEAD` | PASS |
| `python3 tools/validation/validate_candidate_whitespace.py` | PASS |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0; INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124 at base, at `11be80113` and at `2ae8b7f1a` |

The self-check matches the last recorded baseline in `returns/L2A_REVIEW_DEL-01-03.md` and `PRE_RUN_CHECKS.md`. Its body output at `11be80113` was identical to the base, apart from header lines.

Reliance-hold preflight: `execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --operation exact-correction-preparation`, run from `projects/pec`. It returned ALLOW for `loop/LOOP_INIT.md`, `AGENTS.md`, `loop/LOOP_RECEIPTS.md` and `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/M1_PEC_LOOP_MIGRATION.md`. The register has only its header row.

Checked and not applicable:
- `validate_agent_instructions.py`: no `agents/**` change.
- `validate_run_record_leaks.py`: the CI leak scan covers new run records. The return and verdicts contain no credentials.

## 4. Basis read, with SHA-256 at `eb56e108`

**Root**

| File | SHA-256 | Notes |
|---|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | |
| `agents/AGENT_HELPS_HUMANS.md` | `a0c9fb9443d8671d694c1f7b24ff3c402ffd626c781a2739342c938f2f3c3d1e` | |
| `docs/SPEC.md` | `2d8b92471b9e33c58afede827116cfecedb4a1432ac029544418474bd81ca186` | §8 and §9.8 read |
| `docs/governance_harness/_DECISIONS/AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md` | `f934eeec032bc109e4c1180feb74e63c7179e90f087bcd34109d29543e5dc17e` | |
| `ROOT-DEVELOPMENT-LOOP-MEMORY-20260922.yaml` | `7df517e6cfe0da4a9dc35cef146aa070edef677e76c0df2afc2fa7222232735b` | |
| `ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml` | `e56dd83654b35875933a869f3d6ba9494ad10fa110c521f17a632f7aa38a40be` | |
| `ROOT-EVERGREEN-DEVELOPMENT-LOOPS-20260923.yaml` | `bfe305e9461d228d171d5e66102f8dd2ba36f85570aa2fab13bdd6d430e5147f` | |
| `PEC-LOOP-CONSOLIDATION-20260905.yaml` | `83dea609ad6c53419e906d76b154f4a803c573aeeafedd3fe805e06cfdecd464` | |
| `docs/templates/MEMORY_TEMPLATE.md` | `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a` | |
| `workflows/construct-local-work-graph/WORKFLOW.md` | `24268f3545eae68ac86bbfcb830314f5c8539f6da9de08bf4365b14d6f544525` | |
| its `resources/work-graph-template.md` | `4411d0c25b1dc88da182e05660cb061d8e885ab97f4de8f27b05f7d3b0f12261` | |
| `workflows/bounded-reconciliation/WORKFLOW.md` | `b40daec5d14877f32bcee133150ad66fc3fc9501116b5507591c7db0308bf683` | identified and hashed, not read in full |
| `workflows/task-management/WORKFLOW.md` | `db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b` | identified and hashed, not read in full |
| `init/dev-loop-init-prompt.md` | `aaa2280ad423d82af75892b37df9ee907738bdf5a2f8143f12a296e254d294da` | |
| `D-GOV-43_codex_host_replatform.md` | `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899` | |
| `D-GOV-43_supplement_topology_A2.md` | `fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2` | |
| `D-GOV-20_shared_runtime_local_agent_pilot.md` | `a6a4fc4f0c8136f0cdf25eab155c98a03276248776ed9ff779df6c4b88523f11` | |
| `tools/validation/validate_pec_loop_receipts.py` | `8eb6299558a4038f5a62f5f979a86460f16fece6ed6e2fcb8dd00ce12952bad9` | |
| `tools/validation/loop_receipt_contract.py` | `1b6907f5cc9ec4506a9954562a99df3e43c4fa62fab120f1dbec2726c4f687aa` | |
| `tools/validation/validate_instruction_entrypoints.py` | `04ffcc7c8f3fb886718f2bc5bbb3561addc4ed093274e36a15b1a469812a45e7` | |
| `tools/validation/validate_instruction_tranche_manifest.py` | `1b2bd3941ace82924028d8e21f909d6f927712c22ed97fb26d9c2aa2a34d286f` | |
| `execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-005_ROOT_LOOP_INIT_HISTORICAL_LEDGERS.md` | `a1bdc4d47c04cb4b21a54e5af385950c79f80a8dd2489e359a9d3ce80de0d9e6` | precedent for notice form |

The bounded-reconciliation and task-management workflows are referenced only through the shared LOOP_INIT text, which is mirrored unchanged.

**Method instances**

| File | SHA-256 |
|---|---|
| `projects/chirality-piping/loop/LOOP_INIT.md` | `c712b6487faa3fab461e181aad1a6c16a2cb0eb734c510744e5037289105df1b` |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` | `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25` |
| Piping `init/dev-loop-init-prompt.md` | `b4ad6c6d4bdbd52d76f12361457c454ddd55785f425b4756680e18aeda8d304a` |
| App `init/dev-loop-init-prompt.md` | `ee617f5fa910b8a43dc161f746d03b1688b7f9fb10e426541433e78b5a256cbe` |
| Piping `AGENTS.md` | `d9481951912ceffdd5bc47dbb6549bf0044f5d92f9fe6a9b11ba5969bfebc792` |
| App `AGENTS.md` | `41995dfe123041e1d0235a73e532fddb913f2c2124a9e8ec43857a87d7e5822c` |

The App and Piping `LOOP_RECEIPTS.md` heads and tails were also read, to see how they froze.

**PEC**

| File | SHA-256 | Notes |
|---|---|---|
| `init/taskmgmt-init-prompt.md` | `d22267336a2d12abd2c1334becaab190f6edb634e05d2d63d02933b87b58d224` | |
| `docs/STATUS.md` | `c747aff140abfe321fcdb77dc860132a674f752f1f1e825f2f8c2903ad407ce8` | loop lines grepped |
| `README.md` | `6c98a2c0a2185a540704f0be9c9b9f1259ac97282bb2d78ff2f1773f139c322d` | loop lines grepped |
| `docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` | header |
| `execution/_Decomposition/_LATEST.md` | `1f2cdcba31b3db2fd8818b16202d2bbc89c3f4a20702a962d133a73e10f556b6` | |
| `execution/_ScopeChange/_LATEST.md` | `a2b5b789d996d52aa43c86419c9a4f02d1aa01f438f1616f3d51921e34f84268` | |
| `D-PEC-80_loop_home_and_instruction_surface_2026-09-05.md` | `d73b5f22697c6737ad748a89192251cb03934d10d74bb7d0d57c9696efb0ff61` | |
| `D-PEC-80_RULING_2026-09-05.md` | `b821157ea6abc69b71044037d75a74e6708d20460f3e4139cecbb2d6928afe33` | |
| `D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md` | `585d764b2a50e0be823e72955a556694127fd68710302aa151aec4f72d85124f` | |
| `D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` | `bf0046cb455e9ac335b620c0ba4d77bdd76f3f5b9dd85465a7258cff749e347f` | |
| `D-PEC-88_standing_status_readme_maintenance_2026-09-24.md` | `266a1411854b36d3ed8e9cf4879bd57b31021199f683696897c29e49e398fef5` | |
| `_DECISIONS/_REGISTER.md` | `6ffc49ab5ece73790771d7845bf650e16ceb8b650b41ad8b2f2720fc3f46fc60` | |
| `NOTICE_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md` | `545092c1841a55766fd58932216b852db43c3a2663d61125e317140821a35d5e` | |
| `NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md` | `83515ebd8745372eb63b12b02948d065cbe7a9428eaef2da5a698a46060ac37b` | |
| `NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md` | `8e7170aee2c40ddd0f0be5b72f934d3af3fcdc158a1dc0a4d28a9f4f25850a71` | |
| `NOTICE_2026-09-23_EVERGREEN_LOOP_INSTRUCTIONS.md` | `cc62933dd294c31cefa1c2abd5d36a742f5e67d48b9bcac6883dfd34baf95e5b` | |
| `NOTICE_2026-09-23_SCOPED_PR_CI.md` | `26d763192e88432afb1d996ec99791591b7d72cb94ecb3dcac2acaf16db6f744` | |
| `NOTICE_2026-09-25_AGENT_RUN_ARCHIVE.md` | `16040b05266ed483df93f875dc3e1508befab8b657e2ef579a04424603272825` | |
| `_TaskManagement/REGISTER.csv` | `d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d` | present |

The preimages of the three changed PEC files are hashed in §1.

**Wider consultation:** none beyond the brief's basis. `agents/AGENT_TASK.md` was not read by the manager; the verifier read it.

## 5. Independent verification

The verifier was fresh and read-only: host type `pec-reviewer`, `model: opus`, agent id `ad2b41ddfeec8a218`.

**Verdict 01** (`returns/M1_VERIFIER_VERDICT_01.md`), at `11be80113`: **FAIL**.
- The only blocking finding was B1: the D-PEC-94 record and register row, the M1 node and brief, and the M1 return and verdict files were absent. B1 also covered the D-PEC-88 item-6 wording.
- Content review of the manager's bytes found no blocking defect.
- It raised five non-blocking findings (N1–N5) and eight notes.
- Every manager-side item was repaired in `9a20c86d0` and `2ae8b7f1a`.

**Verdict 02** (`returns/M1_VERIFIER_VERDICT_02.md`), a backcheck at `2ae8b7f1acb0bbfe17df4ed126bea4b89b986137`: **PASS** for the manager's bytes.
- Every verdict 01 repair is made and truthful. There are no new blocking or non-blocking findings.
- It left three notes, which I left as they are:
  - `AGENTS.md` says D-PEC-94 "records" the D-PEC-88 disposition, while the manifest says it "must record" it. Both are true once D-PEC-94 exists.
  - The blocking condition is now "the work needs its target". That is less mechanical than the old `Depends` line, but not weaker.
  - The no-new-Remaining rule could optionally add "unless an owner-ruled packet directs otherwise". Later owner directions already prevail.
- Not merge-ready: the B1 records outside my boundary are still open (§7 item 1).
- This return and verdict 02 were committed after the backcheck. The tranche files are byte-identical to the reviewed head.

## 6. Containment

Every path I changed is inside the brief's write boundary: the Produce files, this return and the verdict files. I did not write:
- `_DECISIONS/**`, `RUN.md`, `docs/STATUS.md`, `README.md`
- any decomposition file, register, SOW, `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `_STATUS.md` or `MEMORY.md`
- `v2/**`, `software-workflow.json`
- Root `AGENTS.md`, Root `docs/**` other than the new manifest, `workflows/**`, `tools/**`, Root `init/**`
- any App, Piping or Runtime file other than the notices

Scratch work stayed in the session scratchpad. The receipt append is byte-for-byte append-only against the base; verdict 01 confirmed this with `cmp`. No work graph was created.

## 7. Unresolved: what HELP_HUMAN or the owner must resolve

1. **Merge precondition (verdict 01 B1).** The `D-PEC-94` record and register row must be on this branch or on `origin/main` before merge.
   - It must name the paths this tranche writes: the two `loop/` files, `AGENTS.md`, the four notices and the manifest.
   - It must name the acts, the verification and the rollback.
   - It must dispose of D-PEC-88 item 6 (carry-over), stating whether that is the owner's decision or a labelled HELP_HUMAN interpretation.
   - The M1 node and brief should be recorded in `RUN.md` and `briefs/`.
   - The owner quote in Receipt 197 and the manifest is taken from the brief. D-PEC-94 is where it becomes verifiable.
2. **Stale PEC texts outside my boundary** (listed in the Receipt 197 Stale-Map-Delta and the manifest `scope_limits`):
   - `init/taskmgmt-init-prompt.md` lines 7–8 say this pointer does not adopt the App/Piping loop. That now misleads.
   - `README.md` lines 54–55, 114 and 136–137 describe the ledger and Remaining selection.
   - `docs/STATUS.md` lines 127–132, 311, 317, 322 and 347 describe the same.
   - HELP_HUMAN can refresh STATUS and README under D-PEC-88 once its carry-over is recorded. The taskmgmt prompt needs a D-PEC-94 path grant.
3. **Launcher alignment is optional.** Aligning PEC's launcher with App and Piping ("within the owner's steering and live authority") needs the same edit in Root `init/dev-loop-init-prompt.md` §4 and in `projects/pec/init/dev-loop-init-prompt.md`, together, so the byte-match validator passes.
4. **Owner confirmations:** design choices 4 (no new Remaining entries), 5 (MEMORY rows need a packet grant; a standing clause is possible), 7 (D-PEC-80 items B and C also replaced) and 8 (D-PEC-88).
5. **Other stale texts noticed, not changed:**
   - `projects/pec/AGENTS.md` still says "Implementation does not exist yet", although v2 source slices have landed under D-PEC-87/89/91.
   - The Primary Agents table uses pre-v3 role names.
   - The "Session model convention" prescribes models, which App rescinded under D-GOV-17 M1-D.
   - `_COORDINATION.md` Provenance still says revision 1.4 is `current_basis`.
   - None of these was in the brief's scope.
6. **Archiving.** D-GOV-45 archives run folders untouched for 14 days. Central receipts under `AgentRuns/<RunID>/` will leave the working tree once their runs close, and resolve from the archive tag. App and Piping are in the same position. No change is proposed.
