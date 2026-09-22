# PEC operational guidance review

Recorded 2026-09-22 for the alignment-manual undertaking. This is a bounded TASK research return to `/root/project_coverage_manager`, not a PEC adoption, ruling, acceptance, production activation, or instruction amendment. The parent brief declares repository basis `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`; this task inspected the supplied working tree and did not run Git, fetch remote state, launch PEC, or run a full suite. Source identities and inspection limits are recorded in `project-pec-sources.json`. The manager reported a model-capacity interruption before output writing; this same TASK resumed from its retained investigation, wrote the outputs, and performed a source-hash backcheck. The interrupted partial inspection was not represented as a completed output or a new agent run.

## Operational conclusion

Enter PEC through `projects/pec/init/dev-loop-init-prompt.md` and `projects/pec/loop/LOOP_INIT.md`. The live loop has a deliberate distinction between instructions, current work, and history: instructions carry protocol and fences; deliverable `_STATUS.md` `## Remaining` sections carry selectable work; exact decisions and accepted contracts govern; receipts and `docs/STATUS.md` aid discovery. A receipt or register summary is not its own ruling. The manual should preserve this distinction instead of presenting PEC's dated README, AGENTS product-stage prose, or retired workplans as current state. [Sources: `projects/pec/init/dev-loop-init-prompt.md`, lines 1–14; `projects/pec/loop/LOOP_INIT.md` §§1–2, lines 3–69; §5 Step 0, lines 188–196.]

PEC remains an optional, content-minimal coordination plane: governed file truth is authoritative; PEC output is derivative; consumers own whether and when they use it; PEC dispatches and arbitrates nothing. Its deletion must not prevent a governed act. These are product constraints, not permission to build arbitrary PEC functionality. [Source: `projects/pec/AGENTS.md`, **Product Posture**, **Data And Residency**; `projects/pec/loop/LOOP_INIT.md` §3, lines 91–113.]

## Root-relative entry recipe

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`, set `WORKING_ROOT` to `${REPO_ROOT}/projects/pec`, and begin from repository root. Load Root `AGENTS.md`, the actual active role file, PEC `AGENTS.md`, and the selected run brief. The normal PEC development launcher selects `agents/AGENT_HELP_HUMAN.md`; a delegated TASK retains its bounded assignment rather than pretending to be that entry role. [Sources: Root `AGENTS.md`, **Roles**; `agents/AGENT_TASK.md`, **PROTOCOL/SPEC**; PEC launcher lines 2–11.]
2. Read `projects/pec/loop/LOOP_INIT.md`. Perform its complete Step 0 block when actually entering the development loop: fetch, inspect Git state, validate receipts, reject a committed workplan beside the init, inspect recent receipts, decisions/profile/decomposition/scope-change, validate live and closed Task Management registers, discover deliverable status/Remaining surfaces and notices, then run the harness self-check. This research task did not perform that Git-dependent loop entry and does not claim fresh `origin/main` observability. [Source: loop §5 Step 0, lines 130–196.]
3. Open the exact decision records behind relevant register rows and later receipts; read accepted decomposition `_LATEST.md`, the selected deliverable's `ScopeOfWork.md`, `_STATUS.md`, dependencies and local run evidence. Reproduce hashes pinned by the item. Scope comes from accepted decomposition and deliverable contracts, not directly from the PRD. [Source: loop §2, lines 22–38; §5, lines 188–223.]
4. Select only recorded `Remaining` work with its gates satisfied. Owner rulings, notices used as prerequisites, and hold releases are observable only in fetched `origin/main`; predecessor work can be observed on the run branch, without replacing a human acceptance gate. An explicitly scoped owner preparation/correction request is the documented exception when Remaining is missing; it does not invent production scope. [Source: loop §5 Step 1, lines 198–228.]
5. Run the exact-target, exact-operation reliance preflight before dispatch, review, fan-in, promotion, or reliance. Prepare a bounded candidate brief or proposal with paths, checks, rollback, and ruling mechanics. Execution requires the applicable exact-path grant. Technical completion, Git merge, artifact acceptance, lifecycle change, release, and professional reliance remain separate acts. [Source: loop §3, lines 76–89; §5 Steps 2–5, lines 230–275; §8, lines 309–325.]

The current loop still calls for one branch per run from `origin/main`, one commit and receipt per iteration, an append-only receipt chain, and a PR at terminus or a merged prerequisite. The 2026-09-22 Root local-work-graph notice changes App/Piping narration requirements; it explicitly leaves PEC's accepted basis and selected method unchanged. It is not permission to drop PEC receipts. [Sources: loop §5 Steps 4–5, lines 248–275; `projects/pec/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md`, lines 14–24.]

## Layout to explain in the manual

| Root-relative location | Operational role |
|---|---|
| `projects/pec/loop/LOOP_INIT.md`, `LOOP_RECEIPTS.md` | Single live generic loop and derivative append-only handoff ledger. |
| `projects/pec/execution/PKG-*/1_Working/DEL-*/` | Deliverable contracts, lifecycle and Remaining, local `Dependencies.csv` / `_DEPENDENCIES.md`, optional `MEMORY.md`, and `_run_records/**`. |
| `projects/pec/execution/_Decomposition/`, `_ScopeChange/` | Accepted software decomposition and companion registers; scope-change snapshots and pointers. The current decomposition pointer names revision 1.4, accepted through SCA-004. Its dated downstream-state claims must be reconciled with successors. |
| `projects/pec/execution/_Coordination/_DECISIONS/` | Exact D-PEC packets and owner records; `_REGISTER.md` is navigation. |
| `projects/pec/execution/_Coordination/_TaskManagement/` | Local concern register, archive and routed handoffs. A concern is not an assignment or substitute work queue. |
| `projects/pec/execution/_Reconciliation/DeliverableConcordance/` | Source-bound reconciliation packets. Current discovery includes `PEC_REMAINING_CONCORDANCE_2026-09-05/`; later application and repair evidence remains separate. |
| `projects/pec/execution/_Evaluation/Reviews/` | Review/acceptance snapshots and pointer; do not equate a review snapshot with lifecycle or release. |
| `projects/pec/v2/src/pec_v2/` | Bounded Python v2 source; core capability ports/guard, configuration and storage adapters. |
| `projects/pec/v2/contracts/api/`, `v2/config/` | Versioned API contract and project configuration. |
| `projects/pec/v2/tests/{contracts/api,config,enforcement,storage}/`, `v2/tools/`, `v2/docs/` | v2 test families, deterministic posture checker and capability notes. |
| `projects/pec/software-workflow.json` | Current development check registry and path routing; neither a Domain Engine Profile nor an invocation grant. |
| `_DomainEngines/profiles/pec.yaml` and `_DomainEngines/_DECISIONS/` | Read-only profile and Tier-0 authority lineage remain here despite PEC loop migration. |
| `projects/pec/{core,server,web,agent-sidecar,tools,fixtures}/` plus prototype workspace manifests | Frozen prototype reference corpus. Read/cite only; historical machinery is a pattern source, not active v2 implementation. |
| `projects/pec/plans/workplans/`, `docs/.archive/` | Retired workplans and product documentation; historical references only. |

Layout sources: loop §2, lines 22–69; PEC `AGENTS.md`, **Frozen Reference Corpus**; `projects/pec/README.md`, **Layout**; maintained `software-workflow.json`; directory inventory of `v2/`; profile lines 100–106. Deliverable-local dependency storage and rejection of a standing central register are recorded in `execution/_Coordination/_COORDINATION.md`, **Phase 1.3 owner rulings**, lines 25–30.

## D80 migration and subsequent current-work evidence

D-PEC-80 A/B/C/D were owner-ruled on 2026-09-05 for the reviewed candidate and became effective on merge. The migration moved the loop from `_DomainEngines/pec/` to `projects/pec/loop/`, Task Management to project coordination, and historical AgentRuns to project coordination. D-retirement then moved workplans/currency notes from the intermediate loop home to `projects/pec/plans/workplans/`. Both relocation maps are needed to resolve old citations. The current filesystem has no `_DomainEngines/pec/LOOP_INIT.md` and no workplan beside the new init. [Sources: `execution/_Coordination/_DECISIONS/D-PEC-80_RULING_2026-09-05.md`, line 1; `D-PEC-80_LOOP_HOME_2026-09-05/RELOCATION_MAP.csv`, rows 4–5, 332; its `D_RETIREMENT/RELOCATION_MAP.csv`; loop §10, lines 337–346.]

The D80 owner-intent record preserves standing purpose and explicitly makes its parked list dated history. It selects no work and opens no fence. Its statement that all 64 statuses lacked Remaining was true at that recorded audit, not now. D83 later accepted the source-bound concordance report and authorized exact append-only Remaining bookkeeping for 57 ordinary carriers. It excluded the frozen DEL-01-05 carrier, and selected no individual evidence inquiry for execution. Receipt 174 records that ordinary application; Receipt 175 records later bounded scanner repair and changed-claim backcheck. [Sources: `D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md`, lines 17–24, 56–60, 128–141; `D-PEC-83_RULING_2026-09-07.md`, lines 13–18; loop receipts 174–175, lines 1938–1956.]

A machine inspection of the 64 current deliverable `_STATUS.md` files found 57 Remaining sections and states `OPEN=32`, `INITIALIZED=26`, `IN_PROGRESS=2`, `CHECKING=4`. This is a local-tree census on 2026-09-22, not accepted production state or a selectable-work count. In particular, missing Remaining does not mean complete, and a Remaining item may still be gated. The JSON manifest records all 64 inspected files and exact hashes.

The latest local receipt is Receipt 177, dated 2026-09-08. D85 granted exactly nine store/guard source, test, document and configuration paths plus bounded DEL-01-03 administration. The local deliverable is `IN_PROGRESS`; its three Remaining evidence inquiries remain gated and unchanged. The recorded technical fan-in passed the finite five-check set, but did not accept artifact fitness, enter CHECKING, complete all DEL-01-03/P1, integrate Runtime, perform system kill/parity, issue, or release. These are historical recorded results, not suites rerun by this task. [Sources: `D-PEC-85_RULING_2026-09-08.md`, lines 22–73; `D85_PRODUCTION_CLOSEOUT_2026-09-08/HANDOFF_STATE.md`, lines 3–29; DEL-01-03 `_STATUS.md`, lines 3–24; `MEMORY.md`, lines 16–37; Receipt 177, lines 1969–1977.]

DEL-01-05 is also `IN_PROGRESS`, following the exact owner-authorized D84 `CHECKING → IN_PROGRESS` reversal for scanner repairs. The August D77 acceptance remains history for its original bytes; later repaired-artifact acceptance and lifecycle promotion require separate acts. DEL-01-06 remains `INITIALIZED`; the older map's CHECKING claim for DEL-01-05 is stale. [Sources: `D-PEC-84_L_RULING_2026-09-07.md`, lines 19–44; respective DEL-01-05 and DEL-01-06 `_STATUS.md` files.]

## Commands verified in maintained files

These are commands read from maintained instructions/registries, not newly passing tests. Choose only checks applicable to the authorized packet and record cwd, selected interpreter/version, source identity, exit code and output. Loop §8 requires a compatible explicit Python and says the registry requires Python 3.10+. The current v2 work uses standard-library checks; the prototype npm scripts are not the v2 entry procedure.

From repository root, the loop's maintained governance checks are:

```sh
python3 tools/validation/validate_pec_loop_receipts.py --repo-root .
PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check
python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv
python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv
python3 tools/validation/validate_instruction_entrypoints.py .
python3 -m pytest -q tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py
```

The first two apply to every loop closeout; the register commands apply to Task Management changes; the last two apply to launcher/init/posture changes. [Source: loop §8, lines 296–309.]

From `projects/pec`, `software-workflow.json` registers:

```sh
python3 -m unittest discover -s v2/tests/contracts/api -p 'test_*.py'
python3 -m unittest discover -s v2/tests/config -p 'test_*.py'
python3 -m unittest discover -s v2/tests/storage -p 'test_*.py'
python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json
```

The fifth registry command runs the Root harness from `../..`. API, posture and harness are the registry's `always_checks`; config/source and storage paths add their respective checks. Do not omit a packet's additional finite checks or presume the checker itself runs the enforcement regression suite. [Source: `software-workflow.json`, lines 5–48.]

The maintained runner accepts the profile positionally, repeatable `--check`, and mandatory `--output`; no `--check` means all checks. For an already authorized evidence path, the root-relative form is `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check v2-store-guard --output <authorized-repository-relative-evidence.json>`. It writes the report and creates its output parent, so authorization must include that exact evidence location. [Source: `tools/software_workflow/run_registered_checks.py`, lines 253–303; profile lines 51–57.]

Exact reliance-preflight form from `projects/pec`:

```sh
python3 execution/_Scripts/pec_reliance_hold.py \
  --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv \
  --target execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md \
  --operation historical-read-only-inspection
```

This one command was executed in this research task: exit 0, `ALLOW`. The current register contains only its header, with zero active rows. This permits the tested inspection, not a production act. The tool exposes the seven operations listed in loop §8, fails closed for missing/malformed input, returns 3 for invalid register and 4 for held operation, and has no runtime override. Use the intended operation and exact target, not `candidate-validation` to evade a production hold. [Sources: `execution/_Scripts/README.md`, lines 6–16; `pec_reliance_hold.py`, lines 12–36, 40–84; `ACTIVE_RELIANCE_HOLDS.csv`; loop lines 311–325.]

The repository's `.github/workflows/pec-tests.yml` currently provisions Node 24, builds shared Runtime, installs PEC dependencies, and runs `npm test` in `projects/pec`. This is the retained prototype-workspace CI lane, not evidence that v2 Python checks ran. `projects/pec/package.json` identifies its four prototype workspaces and scripts. Never use a green legacy CI lane to infer v2 acceptance; apply the exact packet's registered checks as well. Do not run the old server or mutating CLI against a non-scratch database. [Sources: `.github/workflows/pec-tests.yml`, lines 29–52; PEC `package.json`; PEC `AGENTS.md`, **Frozen Reference Corpus**; loop §8, lines 306–308.]

## Currency, adoption and launcher traps to preserve explicitly

| Observed surface | Correct reading and source |
|---|---|
| PEC `AGENTS.md` says implementation does not exist; live PRD header says coordination plane not implemented. | Those product-stage statements are dated. Bounded v2 source exists under D74/D75/D77/D84/D85, and D85 technical production is recorded. Full product readiness is not established. Use current exact packet/deliverable evidence, leaving original bytes intact. |
| Live PRD remains v2.2; a v2.3 candidate exists. | Version 2.2 remains the live product definition. D79 adopted exact candidate/carrier bytes but explicitly withheld live application; adoption of a postimage is distinct from applying it. Source: `PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/OWNER_RULING_2026-08-09.md`, lines 12–42. |
| Decomposition/scope-change pointers still describe unstarted downstream alignment; README/STATUS describe two incomplete currency categories and TM-PEC-011 OPEN. | Preserve revision 1.4 authority, then follow the August 9 currency closeout and exact acceptance evidence. That closeout says ordinary currency complete, incomplete only for TM-PEC-023. The live TM register has TM-PEC-011 CLOSED / RESOLVED_WITH_CHANGE; TM-PEC-013/014 remain OPEN administrative concerns, TM-PEC-022 DEFERRED and TM-PEC-023 OPEN. Source: `PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`, lines 12–31, 69–108; live Task Management register rows. |
| Profile first comments say candidate-only/awaiting ruling; receipt header still names old profile lineage. | `_DomainEngines/_DECISIONS/D-T0-27_pec_v2_profile_successor.md` records exact adoption/effectiveness and no invocation grant, lines 48–66, 81–103. The current YAML fields are `ADOPTED / READ_ONLY`, but its hash differs from the historical `be3044d3…` adoption bytes. D-PEC-80 explicitly amended the profile output/write locators to project-local AgentRuns and says the old exact hash is historical lineage, not the new identity (`D-PEC-80_loop_home_and_instruction_surface_2026-09-05.md`, lines 117–119). Candidate header prose is historical, not a new denial. The final manifest records the current hash and this ruled path amendment. |
| PEC AGENTS lists retired specialized roles and `skills/software-*`; model convention names opus/fable. | Root now has four roles. The September 9 D-GOV-41/42 notices explicitly preserve the receiving loop's accepted basis until its owned adoption; do not treat notices as automatic PEC adoption or invent a model identity. This task found no PEC post-notice adoption in the searched current decision/TM registers. That limited search does not prove none exists elsewhere. Source: notices `NOTICE_2026-09-09_FOUR_ROLE_WORKFLOW_OVERHAUL.md`, lines 15–37, and `NOTICE_2026-09-09_CHIRALITY_V3_ROLE_SKILL_WORKFLOW_ADOPTION.md`, lines 8–10. |
| `init/taskmgmt-init-prompt.md` claims paste-ready, invokes `agents/AGENT_TASK_MANAGEMENT.md`, and requires owner-only merge. | The referenced role file is absent in this checkout. The launcher needs an owned migration/compatibility decision; this review does not silently replace its role or workflow. Its generic owner-only merge default is superseded by the September 12 standing Git application notice, but explicit task-specific holds survive. Sources: launcher lines 3–8, 16–23, 48–50; `NOTICE_2026-09-12_STANDING_GIT_AUTHORIZATION.md`, lines 3–14. |
| Old `LAUNCH_RUNBOOK.md`, prototype `npm run dev`, embedded `web`, and project metadata adapter IDs suggest a runnable current app. | They describe retained prototype/compatibility surfaces. `chirality.project.json` still names `claude-agent-sdk` and `pi`; this does not establish current Codex qualification or a v2 start command. No current v2 service-start/deployment command was located in the inspected registry/docs; D85 explicitly excludes service/runtime integration. |
| PEC instructions describe a shared Runtime daemon. | D-GOV-43's September 12 application notice re-expresses the target as an application-owned Runtime service. PEC remains a potential Runtime client; compatibility is unverified, it is not the qualified MVP consumer, and no PEC source/contract/lifecycle/release act follows. Source: `NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md`, lines 11–31. |
| A local work-graph notice or Root method availability appears newer than PEC's loop. | Availability is not PEC adoption, a current graph, or a waiver of its receipt/packet obligations. Source: `NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md`, lines 14–24. |

The unresolved instruction-adoption/launcher mismatch should be returned to the owning loop as a precise issue, not repaired in this manual undertaking. The evidence files are guidance for the author and do not change PEC project instructions, live pointers, acceptance records, or production scope. Before any later execution, repeat actual loop discovery and exact authority checks against fetched `origin/main`; this report is tied to the 2026-09-22 inspected snapshot.
