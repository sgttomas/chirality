# Component design — Runtime delivery separation

Date: 2026-09-05. Status: `DESIGN_COMPLETE — ARCHITECTURE AND MIGRATION UNSELECTED`.
Author: `/root/runtime_separation_design`, OpenAI GPT-6, acting as HELPS_HUMANS Agent 1 for parent `/root` HELP_HUMAN. Exact serving model ID unavailable. Native delegation and role are instruction-asserted; Agent 0 role is not mechanically enforced. No child delegation occurred.

Owner commission: “Proceed with all recommended options.” This selects E2's bounded study, not one of the new implementation choices below. Basis: proposal commit `d02feaae5f73cba3d7501efe9c1028a97b81c887`; fetched main `faf22452528b5ba895e88ba0ad3770855100de08`. This is derivative decision support, not accepted decomposition or execution authority. Paths are repository-relative; exact source hashes are appended.

## Recommendation and reason

Separate runtime delivery management before separating its working root. Retain Root's semantic/release accountability in DEL-02-06, retain the six existing delivery carriers DEL-02-07–12, and retain code at `runtime/`. Give one existing WORKING_ITEMS manager a bounded PKG-02 runtime delivery run after the owner refreshes the R17 seating authority and accepts the necessary deliverable-local Remaining contracts. HELP_HUMAN continues Root integration and owner decision routing. No new agent persona, project, product, runtime client, scope ID, or instruction package is needed for this first step.

This is option B below with the least disruptive location choice. It gives delivery an independently managed cadence and explicit fan-in without transferring accountability or inventing sibling writes. A dedicated registered workspace is a later structural choice, justified if the measured scheduling benefit outweighs its added integration boundary. Merely clarifying the current Root loop (A) is cheaper but leaves one manager interleaving all program work. Fully separate product ownership (C) has the highest reconciliation cost and no demonstrated need in the inspected evidence. The evidence establishes sparse seated work and a stale execution steer, not a measured filesystem or management throughput failure. The recommendation is therefore a staged organizational design, not a claim that migration will improve throughput.

## Verified constraints and current state

- PRD_ROOT §1 ID-1 and independently accepted ID-1a retain Root's dual nature and self-application. §5.2 O-11 is effective under D-GOV-28 despite its retained PROPOSED-origin row label; current document control §10.5 says Revision 8. Generic semantics, affected-client evidence and human release disposition remain Root responsibilities. D-GOV-20 explicitly names the Root-owned `runtime/` workspace.
- SPEC §0.2.2 places `runtime/` inside Root's WORKING_ROOT=REPO_ROOT. §0.2.1 excludes it from the shared instruction enumeration, consistently with product code. G2's `execution/_harness/surface_ownership.yaml` explicitly assigns `runtime/**` to PKG-02 and DEL-02-06. This is a real home, not a path-model gap; registration is a static ownership fact, not write or concurrency authority.
- Accepted SCA-004 revision 1.3 and SOW-104 split implementation into six carriers while retaining DEL-02-06 integration. A management split using those boundaries need not amend the decomposition. A transfer into another authoritative decomposition does. The existing seven carrier ScopeOfWork files are accepted records; historical candidate language in their prose is not a substitute for their owner-acceptance status and current amendments.
- The SCA-004 post-Phase-5 graph snapshot reports nine Root relationships (eight gating), two non-gating cross-loop edges, and no non-trivial SCCs. It also reports 45 legacy containers NOT_RUN_YET. Recompute affected dependency truth for a transfer; do not reuse the old “edgeless Root” characterization or equate the extracted slice with whole-corpus completeness.
- App has seven local `file:../../../runtime/packages/...` dependencies. `frontend/scripts/build-electron.mjs` resolves repositoryRoot/runtime, bundles package sources, and emits `dist-runtime/chirality-cli.mjs`; package.json copies dist-runtime to runtime-cli. A physical code move is an App build/lockfile/packaging migration through the App loop. No App files were changed in this study.

## Options and independent location choices

| Choice | Management and authority | Delivery/governance location | Code location | Cost and consequence |
|---|---|---|---|---|
| A — Current workspace, clearer Root management | Existing Root loop selects and supervises all Root streams; DEL-02-06 still integrates the six carriers | Current Root execution tree | Current runtime/ | Minimum change; refreshed R17 and Remaining seating still required. No distinct delivery manager cadence. |
| B — Root accountability, separately managed delivery **(recommended)** | Root owns semantics and final release fan-in; a WORKING_ITEMS Agent 1 manages the bounded runtime delivery stream | Initially the existing seven Root carriers, with an independently sealed PKG-02 run; a later destination workspace is optional | Keep runtime/ initially | Separates scheduling and delivery returns without moving accepted truth. Requires real activation/brief/scope gates, not a new product. |
| B with a registered delivery workspace — structural extension, unselected | Root retains DEL-02-06 and O-11; destination owns only accepted implementation outputs and local acceptance | Transfer or replace DEL-02-07–12 through Root SCOPE_CHANGE plus accepted destination PRD/decomposition; stable-ID mapping prevents duplicate authority | Either runtime/ with Root integration, or move code into destination | Introduces cross-root acceptance, dependency, registration and handoff overhead. Code remaining at Root requires a separate Root-contained integration executor. |
| C — Fully separate runtime product, unselected | New product owns generic semantics and release accountability; Root retains the instruction system and whatever boundary-governance role is explicitly retained | Transfer DEL-02-06 and all six carriers through accepted source/destination scope changes | Keep a Root integration boundary temporarily, or move to destination/repository | Must amend O-11/D-GOV-28, D-GOV-20 ownership architecture and corresponding scope; appoint accountable human and client contract authority before cutover. Root ID-1/ID-1a need not be retired merely to transfer this stream. |

An implementation working root and a physical code directory are separate decisions. Do not label a records-only project an implementation workspace while granting it `../runtime` writes. Under SPEC §0.2.3 those writes must fail. In the recommended first step, all delegated runtime executors explicitly operate within the Root working root under bounded Root-authorized targets; no narrower sibling workspace is asserted.

If a distinct workspace is selected later, these registration choices are concrete alternatives:

| Registration shape | Required contract |
|---|---|
| Explicitly governed in-tree project using the existing v1 dialect | A manifest using `chirality.project/v1`, contained declared references and canonical-tree overlap as enforced by ProjectRegistry; separate practitioner adapter using `practitioner-harness-adapter/v1`. Root repo instruction writes still require separate M2/G4. An in-tree project cannot write Root runtime/ through its project scope. |
| v2 workspace with disjoint instruction deployment | A `chirality.project/v2` manifest using `instructionRoot: {"mode":"runtime"}`; a real readable CHIRALITY_INSTRUCTION_ROOT disjoint from the working root; realpath/reference/manifest-drift tests. A packaged or separate instruction installation can supply this disjoint root. |
| Separate repository | The same v2 containment and registration proof plus a pinned package-distribution/consumer contract replacing App relative file dependencies. Working-root Git identity, source supply, licensing and release integration must be explicit. |

`runtime/packages/core/src/project-registry.ts` requires overlap for v1 and rejects overlap for v2, validates referenced real paths, and disables adapters on manifest drift until re-registration. A folder creation or a practitioner-harness alias alone does not prove runtime registration or authorization. The design does not choose a destination name, ID, dialect, deployment path or external repository.

## Concrete delivery contract for recommended B

| Carrier | Continuing responsibility and manager return |
|---|---|
| DEL-02-06 | Root-owned versioned semantics, compatibility identity, six-carrier fan-in, affected-client matrix, binding-disposition snapshot and accountable-human release disposition. Sole semantic integration point; no delegated acceptance authority. |
| DEL-02-07 | Process supervisor and purpose-limited control: exact code/contract candidate and containment, authentication, generation and socket tests. |
| DEL-02-08 | Exact supply/protocol pinning: accepted supply references, endpoint/prompt-policy evidence, pin drift and refusal evidence; R15's documented gaps carried explicitly. |
| DEL-02-09 | Hosted account/consent boundary: per-root identity, login home, role/consent continuity and isolation evidence. |
| DEL-02-10 | Adapter event schema/approval API v2: versioned event and approval candidate plus wire, attribution/redaction and compatibility evidence. |
| DEL-02-11 | Worker retirement/restart/terminal reconciliation: journal/replay and exactly-once terminalization candidate with failure/restart evidence. |
| DEL-02-12 | Runtime conformance evidence/shared release fan-in: sealed test/client evidence and unfulfilled gate inventory; it prepares rather than performs human release. |

Runtime position: HELP_HUMAN Agent 0 supervises one existing WORKING_ITEMS Agent 1 for the authorized PKG-02 stream. That manager dispatches bounded Agent 2 TASK+appropriate live software skill or ephemeral generalists under the actual AGENTS contract; no new dedicated specialist is justified. It returns exact output/source identities, tests, dependency satisfaction, remaining holds and a handoff to DEL-02-06/HELP_HUMAN. Scope changes go through SCOPE_CHANGE; instruction changes through HELPS_HUMANS/M2; Git through the approved CHANGE closeout. Actual role enforcement is reported, not inferred from native ancestry.

Inputs: refreshed owner execution steer at a pinned main, accepted ScopeOfWork and seated Remaining items, exact accepted semantic/compatibility/supply snapshots, current caller census, and a sealed disjoint-write graph. Activation and selection remain deliverable-local. Each executor receives explicit working root, tools, allowed write targets and evidence paths. Overlap in runtime/** is serialized or decomposed into disjoint scopes; G2 alone cannot authorize parallel writes. Human decisions remain outside agent returns.

Run output: candidate changes and durable test/identity returns per item; the manager's aggregate return is derivative fan-in. The parent may accept branch predecessors only under the consumer's actual gate contract. Neither the run boundary nor this design satisfies a requirement for owner acceptance or a merged act. Failures hold dependents while independent authorized work continues. A manager run cannot turn routed notices into product Remaining scope.

If B later uses a narrower working root while code stays at runtime/, the destination produces a sealed patch/package against an exact Root base plus tests in its own contained scratch/candidate tree. A separately authorized Root executor reviews applicability, writes runtime/ within Root scope, reruns integration checks, and returns exact applied bytes to DEL-02-06. The destination's local completion is not Root application or release acceptance. This extra integration queue is the principal cost of that location choice.

## Accepted identities and unresolved bindings

DEL-02-06's semantic acceptance snapshot binds six exact semantic members and the sorted package manifest `6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`. Its later compatibility acceptance binds `root-runtime-1`, epoch 1: exactly 14,191 bytes, SHA-256 `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`. This study rehashed the JSON and counted ten literal HELD_UNAVAILABLE objects with null identity. The acceptance snapshot—not the JSON's historical PREPARATION_ONLY_UNACCEPTED label—governs acceptance. No historical bytes or hash-bound citations may be edited to simulate a migration.

The live later meaning is not “all ten still undisposed.” R16-A/B substantively adopts `CONTINUE_SEPARATE_WITH_EXPLICIT_COORDINATION_ONLY` for the Tier-0 relationship. R17 preserves genuine R16-A/B/C/E while rejecting the execution attempt in PR #676. A successor disposition snapshot may carry that later act without modifying the old ten-marker package. Piping and Tier-0 are not runtime clients on that accepted basis; PEC remains an unresolved census matter until an exact accepted instrument says otherwise.

| Nine still-held binding identities | Required evidence/act retained from R16-A |
|---|---|
| Source identity | Exact proposed implementation bytes and Root accountable-human acceptance of their identity |
| Release identity | G6a accountable-human release act |
| App conformance/migration | App-owned G5/G7 conformance fan-in |
| Root CLI conformance/migration | Root-owned G5/G7 conformance fan-in |
| Root semantic/regression evidence | Accepted Root implementation followed by G5/G7 evidence acceptance |
| Affected-loop notice | Routing to affected owning loops before cutover/release fan-in |
| Implementation act | Feasibility results frozen or rejected; exact sealed WP-03/WP-05 briefs; separate accountable-human act |
| Cutover act | Required G2–G5 fan-in accepted |
| Release act | G6a |

R15 accepts only the exact App Server 0.149.0 G2 supply unit, with unavailable generated schema/types/method inventory, missing version-run gate evidence and a G5 vendor-signature finding. No pin/implementation/release follows from that acceptance. R16-C withholds implementation. R17's original fixed-main/pin condition is stale and needs a refreshed owner execution steer; Root loop adoption does not revive its product-seating authorization. R18 closes TM-ROOT-122 RESOLVED_BY_DECISION but expressly leaves TM-ROOT-106 and G1 unresolved. These are independent of this design and remain in the proposed manager's blocked-input inventory.

The 2026-09-04 App notice identifies DEL-02-09 login semantics, DEL-02-10 proposal.* candidates and DEL-02-11 stored delegation policy. Record them as caller needs, with Root acceptance/amendment/decline still required. No notice-created implementation scope, client adoption, schedule or release is implied.

## Change-impact map

| Surface | Recommended B now | If carrier/workspace or full ownership transfer is selected |
|---|---|---|
| `docs/PRD_ROOT.md` §1 ID-1/ID-1a, §5.2 O-11, §5.3 D-7, §6, §8 | No amendment; accountability, self-application and Root pointer remain | B may retain all these; C must amend O-11 and affected trace/falsifiers. Broader Root retirement would separately require ID-1/ID-1a, §6 and §8 decisions. |
| `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`, `D-GOV-28_root_runtime_stewardship.md`, `D-GOV-21_root_working_root_exception.md` | Preserve; new scoped owner run/activation instruments and refreshed R17 only | Superseding records, never historical edits: amend D-GOV-20 if its Root-owned path/accountability statement changes; amend D-GOV-28/O-11 for C. D-GOV-21 Root exception survives unless separately retired. |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` and `chirality_root_{deliverable_register,scope_ledger,objective_register,prd_coverage_forward,trace_reverse,coverage_telemetry}_v1_0` CSV/MD companions | No scope transfer; seat within accepted ScopeOfWork through refreshed authority | SCOPE_CHANGE for SOW-104 and seven carriers, accepted destination basis, retain/transfer/retire ID map, regenerated forward/reverse trace and telemetry. Existing files use CSV except decomposition/telemetry MD. |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06...` through `DEL-02-12...`: ScopeOfWork, _CONTEXT, _STATUS, _DEPENDENCIES, Dependencies.csv and _run_records where present | Authorized Remaining/activation/graph changes only; historical runs retained | Accepted source/destination SOW/status/dependency mapping and evidence references; no duplicate authoritative ID or copied completion claim. Re-extract changed interfaces and audit actual SCCs. |
| `execution/_ScopeChange/_LATEST.md`, SCA-004 lineage and its graph/audit derivatives | No pointer or snapshot change | New immutable source/destination snapshots and separately authorized pointer moves; preserve old SCA lineage. |
| `execution/_harness/{adapter,surface_ownership,work_graph,root_guards}.yaml` | Update authorized dispatch/ownership scopes when seating requires it; adapter count unchanged unless lifecycle changes need pins | Root and destination census/pin/ownership/dispatch reconciliation, new destination `_harness/adapter.yaml`; new runtime project manifest and registration consent when relevant. |
| `tools/validation/validate_root_{materialization_fence,harness_adapter,surface_ownership,work_graph_dispatch}.py`, `tools/validation/validate_instruction_tranche_manifest.py`, their tests; `tools/practitioner_harness/{adapter_loader,adapter_project,brief_adoption,test_root_adoption,test_path_containment}.py` | Run existing checks; no new bypass | Update affected fixtures/pins/alias assumptions only through M2/G4. Root test explicitly pins 53 INITIALIZED and refuses ambiguous registration; do not weaken it merely to hide drift. |
| `runtime/packages/core/src/project-registry.ts`, `runtime/tests/contracts-and-project.test.ts`; `runtime/package.json`, `runtime/package-lock.json` | No location or registry code change | Prove chosen v1/v2 containment, symlink/escape refusal, manifest drift and re-registration. Physical relocation may require build/lockfile/reference updates; no invented schema needed if existing dialect fits. |
| App `projects/chirality-app-dev/frontend/{package.json,package-lock.json,scripts/build-electron.mjs}` and runtime integration tests | No change | App-owned dependency resolution, bundling, packaged CLI and shared-daemon tests; external repository requires distribution/version pinning. Route exact accepted result to App rather than editing its authority from Root. |
| `execution/_Coordination/`, `plans/steers/`, Task Management federation | Separate management returns and exact owner decisions through existing forms | Accepted cross-loop migration/handoff notices; separate authority vs coordination. Canon changes need export/corpus/mirror impact evaluation and G4; agents changes additionally require AGENTS routed notices. |

## Staged adoption, cutover and rollback

1. **Select management contract.** Owner chooses A, recommended B with existing Root paths, B with a destination, or C. Record exact boundaries and accountable human. This study supplies the design; it does not authorize stage 2. For B using existing paths, no structural migration is necessary.
2. **Refresh and seat.** Produce a current-main R17 successor steer and obtain its owner act; seat exact deliverable Remaining items, gates and disjoint write/evidence graph against accepted SOWs. Recheck R15–R18, TM-ROOT-106, supply identities and App notice needs. Do not reuse R17's occupied receipt number or stale pins. Launch only after its applicable gates pass.
3. **Prove management benefit.** Run a bounded owner-authorized delivery iteration with actual WORKING_ITEMS execution, durable Agent 2 returns and DEL-02-06 fan-in. Record selectable work, time waiting for Root integration/owner/client gates, completed independent items and failed boundaries. Compare with the prior Root-managed run; no invented speedup target. If the new manager adds only coordination overhead, stop that run and return selection to Root without a product migration.
4. **Conditional structural preparation.** Only if B-workspace or C is selected: freeze accepted source snapshots; prepare source/destination PRD/SCOPE_CHANGE, stable-ID/path/identity map and registration candidate. Inventory every hash-bound reference and caller. Preserve historical evidence at original paths, or use an explicitly accepted immutable archive with old-to-new resolution; publish a versioned successor mapping instead of rewriting old identities. Root DEL-02-06 remains for B. C transfers its obligations only after O-11 and accountability amendments are accepted. Destination Remaining stays unselectable until its gates are satisfied.
5. **Rehearse before cutover.** In isolated test roots, verify that destination execution cannot write sibling runtime/ or instructions; test chosen registrations and denied escapes. If code moves, build Root/runtime and App candidates against exact source/package pins, exercise packaged CLI and shared-daemon behavior, and prove no second active authority/registry entry or second broker. Keep operational user session/credential stores out of a code-only move. Any requested operational-data migration needs its own exact backup/restore contract.
6. **Accept and apply coherently.** Obtain source/destination scope and human identity/implementation/cutover acts in their order; publish accepted snapshots, registration and dependency changes together or behind explicit inactive transition state. Only the owner moves owning pointers and approves merges. G2–G5, G6a and client gates remain independent; a management or filesystem cutover is not runtime release. Recompute required derivatives and record accepted fan-in or explicit deferrals.
7. **Rollback / re-entry.** Before cutover, discard candidate registrations/patches without changing source authority. After accepted cutover, do not erase its act or rewrite history: freeze failing new work, preserve evidence, obtain a corrective owner decision, and restore the previously accepted registration/package/consumer pins through a new coherent change. Old accepted bytes and the versioned identity map make rollback reviewable. A change of operational data format, if separately authorized, requires tested restore compatibility before cutover; this design asserts none. Retest affected paths and re-accept dispositions before resuming.

## Acceptance criteria and remaining decisions

Design completion checks performed here: principal sources independently inspected; compatibility JSON byte length/SHA and ten null-identity markers verified; source hashes recorded; the two output paths are the whole child write scope. Runtime tests were not run because no runtime behavior changes are proposed for immediate application. The following are acceptance criteria for a later authorized execution, not claimed results:

- Each selected Remaining item traces to an accepted carrier, live owner grant and exact dependency gate; the old R17 execution attempt is not reused. One manager run and all actual descendants have durable scope/parentage/returns.
- All six carrier returns reach DEL-02-06 with exact source/evidence identities or an explicit unresolved hold. The nine unresolved identities cannot become non-null solely through a move or test PASS. R16-B's later meaning is carried separately from the frozen ten-marker JSON.
- No accepted semantic member, compatibility JSON or historical SCA/R-record is rewritten. A migration manifest resolves every affected accepted path, ID and hash with no duplicate authority or missing reference.
- Root G0–G4, harness status/self-check, instruction-entrypoint and whitespace checks, and affected tests pass with consciously updated fixtures. For transfers, run decomposition-register and scope-change validators and affected dependency audits; regenerate required derivative packages or record explicit authorized deferral.
- For code/registration changes, run runtime `npm ci`, `npm run typecheck`, `npm test`, `npm run build` in the isolated authorized checkout; ensure local Unix socket support. Run the App-owned build, packaging and affected integration profiles including shared desktop/CLI daemon and canonical replay/restart. These commands test conformance, not human release authority.
- Destination root containment, registration drift/refusal and rollback are demonstrated at exact pins. No unintended App/Piping/PEC scope, pin, client classification, operational data or instruction write is introduced.

Owner decisions returned upward: select the management design; if a distinct working root is desired, choose destination/dialect/instruction deployment and whether code moves; if accountability transfers, name the new semantic/release owner and authorize the O-11/D-GOV-20/28 amendment package; separately authorize the refreshed R17 seating and subsequent implementation/cutover acts. Broader Root-product retirement remains deferred. The immediate recommendation is B with existing Root carriers/code, followed by a measured run before any structural transfer.

## Handoff

Accepted upstream: hashed PRD Revision 8, SCA-004 revision 1.3, D-GOV-20/21/28, accepted semantic/compatibility bytes, R15, preserved R16 decisions, R17 and R18. This design and its return are derivative; no migration, implementation, acceptance, release or project scope changed. Closure: E2 design complete for owner review; architecture and execution unselected. No authoritative/derived package regeneration is required because none was structurally changed. Parent validates/integrates and returns owner choices. Re-entry rechecks main drift, source hashes, current notices and gates, then runs the chosen stage's checks. Next lawful decision owner: Ryan Tufts via HELP_HUMAN.

## Exact source inventory

SHA-256 values are whole-file hashes read for this study. They identify evidence, not additional acceptance acts. The runtime code and fixture hashes describe inspected implementation, not a claim of current v3 release acceptance.

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3` |
| `agents/AGENT_HELPS_HUMANS.md` | `47a30075b4286a7352d78aae9d033d8eead8ef125e4063d0cc7c1235b3e9101a` |
| `docs/WORKFLOW_COMPONENT_STANDARD.md` | `6b747e073c2a7b24ffbc763241fb8d901c539fb27d1c1c05899ca9e48b6ce313` |
| `docs/PRD_ROOT.md` | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| `docs/SPEC.md` | `f666385e3d79a9634db58087d8b1bd4c4e60bd02ab0ab78fe866d7d911350143` |
| `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` | `a6a4fc4f0c8136f0cdf25eab155c98a03276248776ed9ff779df6c4b88523f11` |
| `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md` | `5bb19c82e1aaf245fc0832b12feb5a2e0bff04d7ad3f0d0ae6c2d83d153f7d83` |
| `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md` | `370668f0a53e11642f9758ce7e33a38e376e09fba4632e58595a88b3e4b0c718` |
| `execution/_ScopeChange/_LATEST.md` | `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c` |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| `execution/_harness/adapter.yaml` | `71f603ad463c14dbba6b02806d67cfc4d859219ff828812fb37de35e78025f3c` |
| `execution/_harness/surface_ownership.yaml` | `18ff8241d96e3d6e1c94e6bb7a39f5f5a7ad7444c9bb5685467ab3da512e932b` |
| `execution/_harness/work_graph.yaml` | `29dc3e35b92418f9cccbdc693aee7cc30943f505415952b57c8f291a647b54cc` |
| `runtime/README.md` | `a90c9e19bb83c32229255db19102bc34095060a0fc2feeb4736f6ecd0370a7bb` |
| `runtime/package.json` | `499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071` |
| `runtime/packages/core/src/project-registry.ts` | `32ed0b2e716736f683026f2bda831fd759876121fcc80218964f688045538df5` |
| `projects/chirality-app-dev/frontend/package.json` | `5f81bcb08c6fadf1f5f1cbd80020cf707e434184990dc5a0a4040fc6f933a9cc` |
| `projects/chirality-app-dev/frontend/scripts/build-electron.mjs` | `a0d6f87d1253cec386996db2d6998b3d81fe18f455dd18fcf94e1b6566f49ce1` |
| `tools/practitioner_harness/test_root_adoption.py` | `acd0a21242a891a8223e7c5008aaf0415031f2a023ac993446f4d77167c63d38` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_PHASE5/SUMMARY.md` | `f72c98f544858aa04a6efde62888b43ab45b6cd96ee3bc4e9c708de04b9d9d74` |
| `execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md` | `299a3b138825b31218ad40e1c90aa61a702bc7462bc3fce09958f718ff34ec49` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_SNAPSHOT.md` | `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md` | `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-COMPLETION-004/candidate/COMPATIBILITY_COMPLETION_CANDIDATE.json` | `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c` |
| `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md` | `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301` |
| `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md` | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| `plans/steers/chirality_app_v3_root_ruling_record_r17_2026-08-27.md` | `23532e46893d8bd79f05775b4744f1438bbb29dbc58b6c70b04b3ae912752faf` |
| `plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md` | `1f315a482ddcaf253d13d6b219f8534c1ddcf7b9d818a72f94c988534d9b8d69` |
| `plans/steers/chirality_app_v3_r17_pathway_seating_steer_root_2026-08-27.md` | `8e96c8fc37e5ac21d93b846a2f1efce15fe6564ebad6fe07334571f473339de6` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/ScopeOfWork.md` | `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/ScopeOfWork.md` | `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/ScopeOfWork.md` | `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/ScopeOfWork.md` | `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/ScopeOfWork.md` | `abd5dcef7a835bafac3e1dd29d7f7b6771ad0aeb60e4af9c25734bfa2534ab02` |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/ScopeOfWork.md` | `62bcfbdd6a20b647f15594fdd35b312d62942f85cf96aedb4aae5db12ea04663` |
