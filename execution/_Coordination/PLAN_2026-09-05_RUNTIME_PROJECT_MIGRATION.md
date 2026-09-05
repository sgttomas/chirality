# Plan — Runtime project migration and governance-only Root

Date: 2026-09-05. Status: **PLANNING CANDIDATE — TARGET DIRECTION REQUESTED; EXECUTION NOT AUTHORIZED**.
Owner request: “I want to plan a deliberate migration of the runtime to its own project, letting the Root remain governance.”
Prepared by OpenAI GPT-6, /root HELP_HUMAN, with an actual HELPS_HUMANS governance-analysis child; exact serving model ID unavailable. Agent 0 role is not mechanically enforced. Native roles are instruction-asserted.

Basis: fresh origin/main@39f51f1cd712b86c67c57270457fc09066eadb1c, including PR #723 merge 944e2015fafc745f3949f447359a6dc44ad95372. Evidence directory: execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_PLAN_2026-09-05/. This is a derivative planning package, not an accepted PRD, decomposition, formal SCOPE_CHANGE gate, migration grant or production work queue.

## Target and recommendation

Make the runtime a project that owns its contracts, semantics, implementation, conformance and product release evidence. Root owns repository governance, shared instructions, cross-project coordination and the rules for human acceptance. The accountable human still decides releases; that decision is recorded against the runtime project's evidence rather than making Root the runtime product owner.

Plan the full ownership transfer, including DEL-02-06. The earlier study's management-only recommendation is not the endpoint of this plan. Retaining Root semantic/release product ownership indefinitely would fail the requested separation. Root may hold temporary custody during migration, with an explicit end condition.

Provisional location: **projects/chirality-runtime in the same repository**, subject to the owner's pending location preference. Move the current runtime workspace contents directly into that project root: packages/, tests/, package.json, package-lock.json and TypeScript configuration. Do not add a second nested runtime/ code root. Keep @chirality package names and protocol identities stable during the location change; a directory move is not a product version or semantic change.

First establish the ownership and destination contracts; then land code relocation and all live consumer/build references coherently; finally close Root's remaining product-form obligations. Keep behavior change, feature development, operational-data migration and provider upgrades out of the relocation tranche. The final Root governance model is part of this migration program, not an indefinitely deferred cleanup.

## Responsibility boundary at completion

| Concern | Runtime project | Root governance | Consumer projects |
|---|---|---|---|
| Runtime contracts and compatibility | Own specifications, versions, tests and evidence | Govern amendment/acceptance rules and cross-project dispute routing | Own adoption and compatibility evidence for their applications |
| Runtime code, adapters, daemon, client and CLI | Own all seven package implementations and delivery scope | No standing runtime code or feature backlog | Consume runtime packages through explicit dependencies |
| Runtime product release | Assemble conformance, supply and regression evidence; accountable human acts on that project | Set repository-wide policy; preserve governing decision history | Accept their own cutover and release dependencies |
| Agent OS | Consume approved instructions under declared read/write boundaries | Maintain AGENTS, agents, skills, tools, shared canon and M2/G4 discipline | Consume the same governed instruction system |
| Work selection and history | Own runtime decomposition, Remaining, dependencies, activations and receipts | Own governance steers, notices, federation and governance assurance | Own their project scope and changes; Root notices grant no writes |

Root governance authority is not permission to implement another project's work. A runtime project being physically nested under REPO_ROOT does not make its product duties Root-owned. The declared working root and scoped executor permissions must enforce the distinction.

## Verified migration inventory

| Surface | Current evidence | Planned treatment |
|---|---|---|
| Runtime implementation | 79 tracked files under runtime/, seven npm packages | CODE_RELOCATION_CANDIDATE.csv maps every current tracked file to its proposed destination with SHA-256. Preserve source bytes initially; rebuild generated output and reinstall dependencies. Do not move node_modules or local runtime state. |
| Direct package consumers | Ten file declarations: seven App frontend, one App harness-contract facade, two PEC server | PACKAGE_CONSUMER_CANDIDATE.csv gives exact old and proposed values, resolved source and target. Rebuild the App and PEC lockfiles with the appropriate npm version; do not hand-edit only top-level declarations and leave old locks. |
| App source/build integration | frontend/tsconfig.electron.json, scripts/build-electron.mjs, scripts/verify-packaged-dependency-boundary.mjs and its fixtures/tests | Update path aliases, runtimeRoot and source-map expectations coherently. Preserve the CLI client-only boundary and current dist-runtime/runtime-cli packaged layout unless separately changed. |
| CI | .github/workflows/harness-premerge.yml, desktop-release-template.yml, pec-tests.yml | Update path triggers, sparse checkout, cache keys and working directories. Add runtime-path triggering to affected PEC testing: it currently triggers on PEC/workflow paths while depending on runtime. Root M2/G4 owns workflow edits. |
| Instruction/working-root registration | SPEC §0.2; ProjectRegistry v1/v2; existing App chirality.project.json | For provisional in-tree project, use existing v1 shape with workingRoot '.', instructionRoot '../..', contained execution/overlay references and only justified adapters. Practitioner adapter is a separate contract. Registration must never grant sibling or instruction writes. |
| Product carriers | DEL-02-06 integration plus DEL-02-07–12 delivery | Transfer all seven responsibilities and their accepted trace. No second active copy at Root. Stable identity and history treatment are explicit below. |
| Accepted evidence | Semantic six-member snapshot, compatibility root-runtime-1 epoch1, R15 supply acceptance, R16/R17/R18 | Preserve historical bytes and acts. Create a successor disposition/identity map instead of editing old snapshots or replacing their source hashes. |
| Root remainder | 46 non-runtime deliverables after the seven responsibility transfers | Review every obligation in GOVERNANCE_IMPACT.md. Preserve governance duties through explicit successor instruments; replace or retire product-specific commitments through owner-approved amendments. Do not assume a filesystem census of 46. |

App-specific Electron hosting, UI and packaged integration remain App responsibilities. The 79-file map scopes the current runtime/ workspace, not every file whose name contains runtime. Before exact scope approval, classify generic runtime logic currently implemented in consumer code against the transferred contracts; any additional code transfer needs an explicit source/destination disposition. Do not quietly move App host features or declare them part of the runtime project just because they start its daemon.

PEC is a verified technical consumer: its server declares both @chirality/runtime-client and @chirality/runtime-contracts, and pec-tests builds the workspace before testing PEC. That requires PEC-owned cutover checks even if its formal release/conformance classification still needs an accepted decision. Piping/Tier-0 remain separate under R16-B; do not enroll them as runtime clients by analogy.

The 79-file and ten-declaration inventories are complete for their stated tracked-path/package-manifest scans at the basis. They are not a claim that every historical prose reference has been classified. Before exact cutover approval, classify all remaining references as active loader/build/policy, accepted immutable citation, dated history, or irrelevant operational runtime path. Never global-replace the word runtime or rewrite historical source citations.

## Proposed layout and identity policy

```text
repository/
  AGENTS.md, agents/, skills/, tools/, docs/, init/   shared governance and instructions
  execution/_Coordination/                           Root governance coordination
  projects/chirality-runtime/
    package.json, package-lock.json, tsconfig*.json
    packages/{contracts,core,daemon,client,cli,engine-claude,engine-pi-omlx}/
    tests/
    docs/PRD.md                                      runtime product contract
    execution/{_Decomposition,_ScopeChange,PKG-*/...} runtime product truth and evidence
    loop/                                           minimal project entry and receipts
    _harness/adapter.yaml, chirality.project.json    separately validated registrations
```

Layout is proposed, not created. Product PRD/decomposition and project setup follow their owning workflows. Do not clone Root's 53-deliverable product or its stale execution steer into the project. Scope is the runtime product plus explicitly identified missing obligations; inherited holds are preserved.

Recommend retaining each transferring DEL-02-06–12 identifier and lineage through an owner-approved cross-root identity map. Destination project qualification distinguishes its authority locus; Root reserves historical IDs and records transfer/retirement, rather than creating two active identities or deleting old folders. If the destination decomposition needs new IDs, approve that exact renumbering and complete every mapping before activation. Never silently reuse an old ID for a different obligation.

Keep accepted historical evidence at its existing immutable Root paths initially. Runtime records cite those snapshots and the accepted transfer act. Historical custody does not retain product ownership. New product evidence and disposition snapshots live in the runtime project. This reduces hash-bound migration risk while allowing a later separately accepted archival relocation if needed.

The compatibility JSON remains 14,191 bytes with SHA-256 e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c. Its ten historical held markers remain unchanged. R16-B separately supplies the later Tier-0 relationship disposition; the other nine holds carry forward individually with owners, reasons and releasing acts. A source-location map is not acceptance of runtime source identity, implementation or release.

## Ordered migration stages

| Stage | Concrete output and responsible workflow | Exit evidence / owner act |
|---|---|---|
| 1. Approve destination and ownership contract | HELP_HUMAN/HELPS_HUMANS prepare exact runtime-vs-Root boundary and coordinated PRD/D-GOV amendment packet | Owner accepts target, transferred semantic/release responsibility, Root end-state, accountable human and bounded migration scope. No code moves yet. |
| 2. Establish accepted source/destination scope | SCOPE_CHANGE prepares Root retirement/transfer actions; SOFTWARE_DECOMP and PROJECT_SETUP prepare destination PRD/decomposition/setup; owning workflows prepare any consumer amendments | Explicit staged approvals of parsed request, impact, exact amendment bytes, propagation and post-change state. Accepted mapping has no gap or double ownership; destination work remains inactive until its gates pass. |
| 3. Freeze and rehearse the migration | Bounded runtime/App/PEC executors prepare exact post-images against frozen main and test in isolated authorized roots; Root owns CI/instruction tranche | All source hashes, live-reference map, consumer locks, containment and test results are frozen. Owner reviews a concrete landing set and migration-only act. Preparation is not source/product release acceptance. |
| 4. Land code and consumer references coherently | Runtime relocation plus App/PEC imports/locks/build changes and Root workflow changes through their owners, integrated by CHANGE | One tested landing set with exact branch HEAD, passing required CI and owner merge. All affected loops supply scoped authority/returns. No interval where main has missing file dependencies or two writable runtime sources. |
| 5. Transfer active product custody | Apply accepted source/destination mappings, ownership/dispatch registrations and allowed pointer acts; validate destination product entry and Root governance entry | Exactly one active runtime owner; all seven obligations, notices and holds accounted for; source evidence still resolves. Source and destination handoffs identify accepted snapshots and completed/deferred derivatives. |
| 6. Finish governance-only Root and close migration | Root owning workflows replace/retire remaining product-form commitments and preserve governance assurance in its proper instruments | Accepted Root PRD/instrument model, reconciled guards/fixtures/exports, zero unowned obligations and no active Root runtime product queue. Owner confirms closure; remaining runtime feature/release work belongs to the new project. |

Stages 4 and 5 must be one atomic owner-reviewed landing when no valid intermediate ownership state can be expressed. If staged separately, stage 4 explicitly retains temporary Root custody until stage 5; destination production remains inactive and the transfer cannot be claimed complete. Do not create a circular gate requiring the destination already to own code before the owner can authorize its transfer. A bounded migration-only grant may authorize relocation of a specified source snapshot while preserving all product implementation/release holds.

Separate PRs are appropriate at genuine owner decision boundaries, not for every planning substep. Within a run, use one branch, one receipt/commit per iteration and one PR at its terminus. A combined cross-project landing requires explicit participating-loop authority; current planning permission is not that authority. Existing restrictions on frontend/projects writes remain in force for this run.

## Authority changes to prepare

- **Root PRD/D-GOV:** amend O-11 and D-GOV-28 to transfer runtime product stewardship; supersede D-GOV-20's Root-owned runtime architecture/path statement while preserving repository-wide boundary rules. Reconcile ID-1 and independently accepted ID-1a, D-GOV-21 and their self-application/materialization obligations with the governance-only end-state. A renamed directory or changed ID-1 sentence alone does not perform that reconciliation.
- **Runtime PRD/decomposition:** own generic runtime semantics, package/API boundaries, implementation, conformance, client adoption coordination and release evidence. Accept the seven-carrier transfer and any newly identified scope explicitly; do not infer destination scope from code presence.
- **Root governance obligations:** inventory retained policy, instruction-release, export, audit and federation duties. Retain their acceptance tests and human accountability even if the Root product decomposition is eventually retired. Adopt replacement governance instruments before retiring their old carriers. GOVERNANCE_IMPACT.md identifies the full set and cases needing product-specific judgment.
- **G0–G4 and practitioner fixtures:** decide the new Root guard contract explicitly. G0/G1 currently encode Root product materialization/53-carrier expectations; retire or replace those Root-product assertions only with accepted governance successor checks. G2/G3 must separate Root instruction/governance targets from runtime project targets. G4 remains on shared instruction surfaces. Preserve generic validators needed by other projects; do not disable tests to hide a changed census. Historical folders may remain, so distinguish registered/active/retired/materialized counts.
- **R17 successor:** prepare a migration-specific replacement that carries valid accepted obligations to the destination and expressly supersedes the old Root seating destination and stale basis conditions as needed. Do not first populate Root's runtime Remaining merely to migrate it again. Its engineering/evidence requirements and genuine preserved R15/R16/R18 acts survive unless explicitly amended. Product implementation still needs its actual named gates after migration.
- **Cross-project instruments:** App and PEC own their contract/dependency/packaging changes and acceptance. Root routes coordination and integrates only explicitly scoped contributions. Root canon/agent changes require G4 and applicable authority-corpus/mirror notices; the recipient owns adoption.

The proposed final state retires Root's product decomposition as continuing production authority after preserving its useful duties. A transitional 46-obligation assurance structure is not the endpoint. The full inventory proposes 7 runtime transfers, 39 retained/re-homed governance duties and these seven product-form decisions:

| Current Root carrier | Recommended disposition to prepare for owner acceptance |
|---|---|
| DEL-03-06 first Root deliverable stream | Preserve historical readiness evidence; replace the future Root-product demonstration with a bounded governance/instruction change demonstration if still needed. |
| DEL-04-10 Root coverage demonstration | Replace product-decomposition coverage criteria with explicit coverage of retained governance controls and their evidence. |
| DEL-06-01 self-application/falsifiers | Recast observations around governance and instruction self-maintenance; identify retired product-specific falsifiers explicitly. |
| DEL-06-02 run-state reconstruction | Preserve reconstructable governance run evidence; do not infer an obligation for Root to operate the runtime product. |
| DEL-06-06 promotion pathway | Retain governance promotion rules and the required demonstration through a named governance instrument; do not mark promotion complete. |
| DEL-06-07 release authority | Retain universal human release policy and instruction-release evidence at Root; runtime product release evidence belongs to the runtime project. |
| DEL-06-08 working-root convergence demonstration | Retain the general assurance objective with an explicitly chosen representative working root, or retire the old demonstration by exact owner act; the file move itself proves neither. |

These are proposed replacement criteria, not seven new accepted obligations. The 39 governance-duty successors also need exact record/tool/check homes before their carriers are retired. Resolve the current incompatibility between SCOPE_CHANGE's retirement instructions and the adapter's lifecycle vocabulary (which lacks RETIRED) through the accepted archive/census model; do not insert a rejected state or erase source folders.

This plan prepares those acts; it does not mark any of the formal SCOPE_CHANGE gates confirmed. Exact amendment text and propagation matrices should be reviewed together for consistency, then accepted through their owning instruments. There is no new _LATEST pointer or invented SCA number in this planning package.

## Acceptance and rollback contract

Required proofs for the eventual cutover, beyond this planning run's checks:

1. **Source preservation:** every one of the 79 baseline tracked runtime files resolves at its mapped destination or has an individually approved change disposition; no npm package/API rename or behavior change is hidden in relocation. Preserved accepted snapshots and all successor identity references rehash correctly.
2. **Consumer closure:** all ten package declarations and applicable locks resolve to the destination. App Electron TypeScript aliases, bundles/source maps, desktop/CLI shared daemon, replay/restart, packaging and client-only CLI boundary pass. PEC server imports/client behavior and complete selected workspace tests pass. Actual formal conformance gates are recorded separately from technical test success.
3. **Runtime tests:** clean npm ci, typecheck, tests and build at the new root, with required Node/local-socket environment. New runtime path changes trigger both runtime and affected consumer checks. Sparse checkouts and cache keys include the destination. Root's Python affected-test runner alone does not verify this TypeScript migration.
4. **Containment and instruction boundary:** exact v1/v2 registration fixtures pass, including realpath/symlink/escape/drift/refusal cases. Runtime executors cannot write Root instructions or sibling projects; Root reads runtime evidence through declared references. Runtime project registration is separate from operator approval/adapter enablement and does not require unnecessary live credential or account mutation.
5. **Authority continuity:** all seven active runtime responsibilities have one owner; nine outstanding holds retain their actual releasing acts; Root/runtime/consumer snapshots, scope traces and derivative reports agree. Root receives governance notices instead of silently remaining the runtime release product owner.
6. **Governance closure:** retained Root duties have accepted instruments, tests and owners before their old product carriers are retired. Final Root guards express the new governance contract; no false 46-count shortcut, unresolved orphan or blanket test bypass remains.
7. **Operational neutrality:** package relocation does not rename user-data directories, sockets, token locations, LaunchAgent labels or persisted sessions. Those paths often contain the word runtime but are not repository code paths. Any operational migration requires a separate explicit backup/restore and authorization plan.

Before landing, keep the prior code and accepted authority intact; a failed rehearsal closes only the candidate. After landing, freeze affected work and preserve evidence, then use a reviewed corrective commit restoring code location, consumer locks, CI and registrations as one consistent set. Never rewrite the accepted migration act or restore only the code directory while leaving consumers on the new path. Source/destination scope and pointer reversals require their owning corrective decisions. Preserve previous usable pins and prove rollback before cutover. No reset/force-push or deletion of history is part of this plan.

## Decision boundary and next preparation

The owner has selected planning for real runtime-project separation and governance-only Root. The concrete details still needing selection are the repository/location, stable-ID mapping, final treatment of Root's remaining product-form commitments, and exact staged amendment/migration authority. Same-repository projects/chirality-runtime is the provisional recommendation, not a silent acceptance of its name or registration.

Next bounded preparation after plan review: the coordinated boundary/PRD supersession packet, destination charter/decomposition candidate, Root obligation disposition matrix and source/destination propagation plan. These can be prepared without moving code or granting feature implementation. The resulting owner review should bind exact bytes and an explicitly bounded cutover, rather than reopen the basic decision to give runtime its own project.

If a separate repository is selected instead, retain the responsibility/evidence plan but replace the path-only landing with versioned package distribution, reproducible release artifacts, consumer pinning and disjoint v2 instruction deployment. Do not attempt to publish private file dependencies across repositories. This is a materially different dependency cutover and needs its own exact candidate inventory.

## Handoff

Accepted upstream: current Root PRD Revision 8, decomposition 1.3/SCA-004, D-GOV-20/21/28/35, R15, preserved R16 acts, R17/R18 and merged loop adoption. User direction selects this planning target; existing authority remains until amended. Outputs are derivative planning evidence; no runtime/project/authority/registration/operational state changes or production acceptance occurred. Planning completion and checks are in the run record/receipt. Migration execution, authority amendments, accepted destination setup, Root retirement and consumer adoption remain unexecuted. Re-entry must refresh main, hashes, consumer census, disposition evidence and owning-loop grants. Next decision owner: Ryan Tufts.
