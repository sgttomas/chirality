# PEC feed model v2 — design note (DESIGN PROPOSAL)

> **DESIGN PROPOSAL.** This note gives the owner and the SCA-005 scope-change
> manager options to consider. It asserts no scope status. It does not rule,
> accept, amend or select anything, and it is not an Impact Assessment,
> Decision Log or amendment action. The PRD, the accepted decomposition,
> decisions and each loop's own files govern if this note disagrees with them.

| | |
|---|---|
| Brief | `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/A4_FEED_MODEL_DESIGN.md` |
| Accepted basis for the work | `D-PEC-86` §3 I-1 (SCA-005 opened at Gate 1; checkpoint groups 1–3 remain owner acceptances) |
| Role | HELPS_HUMANS (Type 1), engaged through HELP_HUMAN. Single instance with no delegation. Role identity comes from the instructions and is not mechanically enforced. |
| Examined basis | `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (worktree HEAD; run basis per `SUPPLIED_BASIS.json`) |
| Write boundary | This file only |
| Sibling outputs | A1 (`SURVEY_SISTER_LOOP_FILE_TRUTH.md`) and A2 (`IMPACT_INVENTORY_PEC_BASIS.md`) had not landed when this was written (`SCA-005_PREP_2026-09-23/` was empty). This note does not rely on them or duplicate them. Where they bind hashes or counts more carefully, theirs govern. |

All paths are repository-relative unless prefixed `PEC:` (= `projects/pec/`).

## 0. Provenance of relied-on files

SHA-256 values come from `shasum -a 256` at the examined basis. Where
`SUPPLIED_BASIS.json` lists a file, the hash matches its recorded value.

**Instructions and brief**

| Path | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `CLAUDE.md` (imports `AGENTS.md`) | `336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49` |
| `PEC:AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_HELPS_HUMANS.md` | `a0c9fb9443d8671d694c1f7b24ff3c402ffd626c781a2739342c938f2f3c3d1e` |
| `PEC:execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/A4_FEED_MODEL_DESIGN.md` | `49186ebb2af841fd40bb5b144b313973f726f15531f35ceb12efce76b4b1bb1d` |
| `PEC:execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/RUN.md` | `cb4f8fe1b24053dc08594c13ad2743364875bb9b847792df46fd8113cc130583` |
| `PEC:execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/SUPPLIED_BASIS.json` | `d59821be6a0e3f3ccecb375344307c4d151a50ca7be7b84a18c68118a9b14354` |
| `PEC:execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |
| `PEC:execution/_Coordination/ASSESSMENT_2026-09-23_APP_PIPING_PEC_UNISON.md` | `0eed76e529a0640d20115413f7125710e8ebb07e9c9c0a4887b1fc70867b1974` |

**Role-file consultation:** I read only this role's own file,
`agents/AGENT_HELPS_HUMANS.md`. I consulted no other role file.

**PEC authority and inputs**

| Path | SHA-256 |
|---|---|
| `PEC:docs/PRD.md` (v2.2 live) | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `PEC:execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.4) | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| `PEC:execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md` | `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0` |
| `PEC:execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md` | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` |
| `PEC:loop/LOOP_INIT.md` | `ec9cc14df99dc627122ec99c6b5b5e9dffd26631445ebec42679205b49835053` |
| `PEC:v2/config/loops.json` | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |
| `PEC:v2/config/loops.schema.json` | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` |
| `PEC:v2/src/pec_v2/core/ports/loop_registry.py` | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` |
| `PEC:execution/PKG-00_…/DEL-00-01_…/artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| `PEC:execution/PKG-00_…/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` |
| `PEC:execution/PKG-01_…/DEL-01-06_…/ScopeOfWork.md` | `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` |
| `PEC:execution/PKG-02_…/DEL-02-03_…/ScopeOfWork.md` | `c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872` |
| `PEC:execution/PKG-02_…/DEL-02-04_…/ScopeOfWork.md` | `bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87` |
| `PEC:execution/PKG-02_…/DEL-02-05_…/ScopeOfWork.md` | `192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e` |
| `PEC:execution/PKG-02_…/DEL-02-06_…/ScopeOfWork.md` | `c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8` |
| `PEC:execution/PKG-02_…/DEL-02-07_…/ScopeOfWork.md` | `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559` |
| `PEC:execution/PKG-03_…/DEL-03-04_…/ScopeOfWork.md` | `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02` |
| `PEC:execution/PKG-10_…/DEL-10-10_…/ScopeOfWork.md` | `640f23711f93ec7e987742ed5ed998bea04c681f14bff06bdf2e35a669fcbd5e` |
| `PEC:execution/_Coordination/NOTICE_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md` | `545092c1841a55766fd58932216b852db43c3a2663d61125e317140821a35d5e` |
| `PEC:execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md` | `83515ebd8745372eb63b12b02948d065cbe7a9428eaef2da5a698a46060ac37b` |
| `PEC:execution/_Coordination/NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md` | `8e7170aee2c40ddd0f0be5b72f934d3af3fcdc158a1dc0a4d28a9f4f25850a71` |
| `PEC:execution/_Coordination/NOTICE_2026-09-23_EVERGREEN_LOOP_INSTRUCTIONS.md` | `cc62933dd294c31cefa1c2abd5d36a742f5e67d48b9bcac6883dfd34baf95e5b` |
| `PEC:execution/_Coordination/NOTICE_2026-09-23_SCOPED_PR_CI.md` | `26d763192e88432afb1d996ec99791591b7d72cb94ecb3dcac2acaf16db6f744` |
| `_DomainEngines/profiles/pec.yaml` | `6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f` |

**Root method, governance and sister-loop inputs**

| Path | SHA-256 |
|---|---|
| `workflows/construct-local-work-graph/WORKFLOW.md` | `24268f3545eae68ac86bbfcb830314f5c8539f6da9de08bf4365b14d6f544525` |
| `workflows/construct-local-work-graph/resources/work-graph-template.md` | `4411d0c25b1dc88da182e05660cb061d8e885ab97f4de8f27b05f7d3b0f12261` |
| `workflows/bounded-reconciliation/WORKFLOW.md` | `b40daec5d14877f32bcee133150ad66fc3fc9501116b5507591c7db0308bf683` |
| `workflows/task-management/WORKFLOW.md` | `db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b` |
| `workflows/task-management/resources/contract.md` | `e1c97a76b8a411873ca86a6ef4351a7f76303e74331a52307a3705a83827c837` |
| `docs/SPEC.md` (§9.8) | `2d8b92471b9e33c58afede827116cfecedb4a1432ac029544418474bd81ca186` |
| `docs/CONTRACT.md` (K-AUTH-1) | `64747d2a3c58ae93194bd5c7118d89a591b7b4ebe8cec7e88cb6a95dc55895bd` |
| `docs/templates/MEMORY_TEMPLATE.md` | `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a` |
| `docs/governance_harness/_DECISIONS/AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md` | `f934eeec032bc109e4c1180feb74e63c7179e90f087bcd34109d29543e5dc17e` |
| `docs/governance_harness/_DECISIONS/D-GOV-01_substrate_authority.md` | `be2db839eaab0ae82395e6ee6c96ebb0ce61952aa008e519b10d9c857b3ece4b` |
| `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` | `a6a4fc4f0c8136f0cdf25eab155c98a03276248776ed9ff779df6c4b88523f11` |
| `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` | `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899` |
| `docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md` | `fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2` |
| `docs/governance_harness/tranche_manifests/ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml` | `e56dd83654b35875933a869f3d6ba9494ad10fa110c521f17a632f7aa38a40be` |
| `docs/governance_harness/tranche_manifests/ROOT-WORKGRAPHS-PATH-ANCHOR-20260923.yaml` | `e7149e9bd9330e738b650af090f23dec0d2abb927e377cd78a54bdc00b450dc4` |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` | `8b975c10acf6c4394f5423d4def20aeb4583159c691e8d3d11a41ce7451e6a25` |
| `projects/chirality-piping/loop/LOOP_INIT.md` | `c712b6487faa3fab461e181aad1a6c16a2cb0eb734c510744e5037289105df1b` |
| `projects/chirality-app-dev/AGENTS.md` | `41995dfe123041e1d0235a73e532fddb913f2c2124a9e8ec43857a87d7e5822c` |
| `projects/chirality-piping/AGENTS.md` | `d9481951912ceffdd5bc47dbb6549bf0044f5d92f9fe6a9b11ba5969bfebc792` |
| `projects/chirality-app-dev/_harness/adapter.yaml` | `f4fbbf1f675b9aa7e9e7b71f26841de7d5031107c498f72e48cee4b5f0009e98` |
| `projects/chirality-piping/_harness/adapter.yaml` | `2de9d3ab3b3e3b2eb622c0959dc292eff06a11c3da7c2665798978df08c20554` |
| `projects/chirality-runtime/README.md` | `025eab1edd95b9dcdd793c410270b491f11bbf52b8f5fb9c98ccb791bdd9d889` |
| `projects/chirality-runtime/docs/APPLICATION_CONSUMER_GUIDE.md` | `2f9f37788a17be9c5030c631dbb53be2f1b59a325bd51bc5bf6ac4e86a781865` |
| `tools/practitioner_harness/README.md` | `b30448ef70ace0f7933c14cc27841d47cc1043c51761f81957e02a0617894088` |
| `tools/practitioner_harness/harness.py` | `01a9b9541ded993364f7db8a8e8a59087bf26649094a522867a658e2eae561f3` |
| `tools/practitioner_harness/surface_roles.py` | `7786998c8eb047e770c98b3e846353d40a307f5cfa9862c95681c3405866949e` |
| `.github/workflows/pec-tests.yml` | `337611cef97e0c691f5a3cb305b804aef6f5300b7337a3ad23dd2b53689f5a7d` |

**2026-09-23 trial-run surfaces**, cited here as fixture candidates only (§6)

| Path | SHA-256 | Git blob at basis |
|---|---|---|
| `projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md` | `6dbb884aed7ebf573abf476d54b404a3c6f8620208327dcae2453fef5757081f` | `d25cae6130a7139d077c2e3bf848ea9aa70bae1f` |
| `projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/RUN_EVIDENCE.md` | `8427cd337c5be32148355748ca0cab5a2063f8dd06d6d0b5ff5995c5b96f2d44` | — |
| `projects/chirality-piping/execution/_Coordination/WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md` | `50933010aef9920d1a615006775ea8997080e5388532ef7d3e9ac8bad92a9a9d` | `ae942d99c7e0f698291c5d8ace95f65390df061d` |
| `projects/chirality-piping/execution/_Coordination/WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md` | `74f068846dd56d97414244635fb6b99c642ffc33ddde5c1f3cf128d30d621428` | `e471421ce8ad094d5cf7b49ed95bad39bf0ae3d7` |
| `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md` | `eef5434b0ea17d757d4f8a8892d383df4edaab53a571c075af2f3d498c46dfa8` | `23623e2cf846bc4673603c9b7991ecf10e026825` |
| `projects/chirality-piping/execution/_Coordination/AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md` | `f2c8dab41d6af54a916baeebede81e058d8aacf58672d8092b06e4dff421ab4a` | `76e618a5a5c137b4f51bf63016a3b3a9997fb76a` |
| `projects/chirality-app-dev/execution/PKG-05_…/1_Working/DEL-05-04_…/MEMORY.md` | `bbf3ed50c94eda9f2b7cf796ebac170ce64b783e5f7359902e33955a0577b144` | — |
| `projects/chirality-piping/execution/PKG-08_…/1_Working/DEL-08-05_…/MEMORY.md` | `ec984ac7b59f6be791112b8eae16b2717f58db70fca240c5ec6f5dc4a8ae8bca` | — |
| `projects/chirality-piping/execution/PKG-10_…/1_Working/DEL-10-04_…/MEMORY.md` | `8526eff38ab8b288f0ceb2a0fd2056f82f6ef1b9e676489ff0f066e2db80fa89` | — |

---

## 1. The problem

PEC's accepted basis tells it what to ingest: PRD v2.2 PEC-RCN-002, the §7.1/§7.2
entity model, PEC-PRS-001/-004, PEC-STR-003, SSOW SOW-011..017 and
SOW-026..037, PKG-02 DEL-02-01..07, and PKG-06/07. That basis describes the
sister loops and the Runtime as they stood in July. On 2026-09-22/23, App and
Piping converged on one shared development-loop method:

- a single Git-tracked `WORK_GRAPH.md` per undertaking under
  `execution/_Coordination/WorkGraphs/<undertaking>/`;
- one derivative `AgentRuns/<RunID>/RECEIPT.md` per undertaking, with the old
  ledgers now historical;
- MEMORY `## Runs` indexes;
- retired `## Remaining` sections and workplans;
- an evergreen `LOOP_INIT.md`.

D-GOV-43 A2 separately replaced the per-user runtime daemon with one
application-owned Runtime service per application, with private tokens. PEC's
own loop still writes the July shape, and its migration is deferred
(`D-PEC-86` I-7). So PEC has to read two generations of file truth at once.
Its declared feed manifest, `_harness/adapter.yaml`, is harness configuration
that describes neither the new surfaces nor PEC itself. Its presence and
stream inputs have lost their source.

The design question is therefore: **what does PEC ingest, from where, in what
shape, with what provenance and freshness semantics, and who declares which
grammar applies to which loop**, without making any loop write for PEC and
without PEC becoming an authority, an executor or a content store.

---

## 2. Invariants that bound the design

| # | Invariant | Source (file · anchor) | What it forces on a feed model |
|---|---|---|---|
| I-01 | Graceful absence: no governed act may require a PEC read or write; the kill test is a standing release gate | `PEC:docs/PRD.md` §6 PEC-K-01; PEC-SVC-004 · `PEC:AGENTS.md` "Binding on every agent" | No feed may assume a loop writes anything *for* PEC. A missing or late surface is a coverage limit, never nonconformance. `_DomainEngines/profiles/pec.yaml` forbids claiming "another loop must consume, poll, inject, subscribe to, or implement PEC". |
| I-02 | Files govern: the record tier is rebuildable by one command; the store is gitignored and safe to delete; PEC output is never citable as authority; rulings and lifecycle stay file-native | PRD §6 PEC-K-02; §4.2 · `docs/governance_harness/_DECISIONS/D-GOV-01_substrate_authority.md` Option A · `docs/CONTRACT.md` K-AUTH-1 | Every record-tier fact must be regenerable from committed files and Git alone. A derived status such as "undertaking complete" is Explain-shaped and advisory. |
| I-03 | Pull-oriented, consumer-owned use; mode-capable and never forced | PRD §6 PEC-K-03, PEC-K-11 (exact rows adopted by `D-PEC-67`; concordance `D-PEC-68`) | Feeds are read when a consumer asks or a reconcile runs. Nothing in the feed model schedules or pushes to a consumer. |
| I-04 | Staleness is a comparison: every response carries the examined-through SHA and per-feed freshness | PRD §6 PEC-K-04; PEC-ORI-003 | Each feed needs a *structural* freshness signal (§3.3). |
| I-05 | Two trust tiers, never blurred | PRD §6 PEC-K-05; PEC-PRS-007 | Committed graph state is record tier, even when it says `ACTIVE`. Only heartbeat/TTL data is presence tier. Neither may be presented as the other (§5). |
| I-06 | Observation, not participation: read-only over Git; no dispatch, leases or arbitration | PRD §6 PEC-K-06; §4.2 | Git plumbing is read-only. PEC never writes a graph, receipt or MEMORY row. |
| I-07 | Ingest is best-effort; reconciliation is guaranteed | PRD §6 PEC-K-07; PEC-STR-004 | Streams can only add freshness. No record-tier fact may rest on a stream. |
| I-08 | Everything derived is explainable | PRD §6 PEC-K-08 | Every applied grammar and every derived state names its rule, grammar version and contributing citations. |
| I-09 | Content-minimal: paths, counts, SHAs, states and hashes, never file or diff content | PRD §6 PEC-K-10; PEC-SVC-005 · `PEC:AGENTS.md` §Data And Residency · SOW-073 (permanent OUT) | Graph cells, receipt "Result" prose and MEMORY run descriptions are content. Only identifiers, closed-vocabulary tokens, SHAs, PR numbers, paths and counts may be extracted (§3.2). |
| I-10 | No second execution loop; the Runtime owns sessions; PEC is an optional client | `PEC:AGENTS.md` §Shared Runtime Boundary (D-GOV-20, D-PEC-56 behaviors 4/7 surviving per D-PEC-58 b8) · `SOFTWARE_DECOMP.md` C13 · `DEL-00-01 ADRs.md` ADR-PEC-V2-002 carried posture 3 · SOW-067 (permanent OUT) | PEC may not host a Runtime or Codex execution instance to obtain presence (§5). |
| I-11 | Loop registry home: PEC-owned strict-v1 JSON at `v2/config/loops.json` with a core-owned typed `LoopRegistry` port. PEC owns only its configured service set; each listed loop stays authoritative for its entrypoint and truth; row changes are owner-gated PEC configuration acts | `PEC:execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md` (ruling O-A) · SOW-077/094 · `loops.schema.json` (`additionalProperties: false`, `schema_version const 1`) | Any per-loop feed declaration inside `loops.json` needs a schema version 2, an owner-gated configuration change and a core-port change (`RegisteredLoop` has two fields). Such a declaration is PEC's *reading hypothesis*, never a statement of the loop's truth. |
| I-12 | Frozen reference corpus: cite-only; machinery carries as pattern, never code | `PEC:AGENTS.md` §Frozen Reference Corpus · `SOFTWARE_DECOMP.md` C11 | Fixtures and grammars are newly authored under v2 packets. Nothing is lifted from `core/` etc. |
| I-13 | Permanent parity peer: PEC parity-diffs against the practitioner harness and neither directs it nor opens its cache half | PRD PEC-RCN-005, §4.2, §15 · `SOFTWARE_DECOMP.md` C10 | PEC cannot require the harness to learn new surfaces. Parity differences are PEC-side DriftFindings. |
| I-14 | §16 open decisions are not guessed; architecture-affecting ones are fenced or flagged | `SOFTWARE_DECOMP.md` C12 | Where A2 moots or reshapes §16.2, §16.6, §16.8 or §16.9, this note flags the fact and does not rule (§8). |
| I-15 | Receiving-loop autonomy and no backfill: each loop decides its own adoption; existing ledgers and completed-run evidence stay historical | `PEC:execution/_Coordination/NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md` · `ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml` `scope_limits` · `AMENDMENT_2026-09-22_…` "Supersession and preservation" | PEC must read old and new generations side by side. It cannot expect retrofitted receipts. |
| I-16 | PEC's own loop migration is deferred until SCA-005 closes | `D-PEC-86` §3 I-7; ASSESSMENT recommendation 4 · `PEC:loop/LOOP_INIT.md` §2, §4 | PEC's P1 self-ingest corpus remains old-shape (`## Remaining` in 57 `_STATUS.md`, prose `LOOP_RECEIPTS.md`, 64 `Dependencies.csv`) for the whole SCA-005 horizon. |
| I-17 | Hexagonal isolation: filesystem grammars are adapters behind core-owned capability ports; actor names do not enter the core | `DEL-00-01 ADRs.md` ADR-PEC-V2-001 decision items 1–2, Consequences | A grammar generation is an adapter concern. The core entity model should name capabilities (work node, run record), not "App ledger". |
| I-18 | Local-only, no egress | PRD PEC-SVC-002, PEC-API-001 · `SOFTWARE_DECOMP.md` C8 | PR state cannot be fetched from GitHub. PR facts must resolve through local Git (merge commits), or else be reported as unresolved. |
| I-19 | Runtime-client invocation requires a profile amendment first | `_DomainEngines/profiles/pec.yaml` notes ("Before any future adapter or runtime-client invocation, amend this profile …") | Any Runtime-sourced presence path carries a profile amendment in addition to scope work. |

---

## 3. The converged shared shape

### 3.1 Surfaces and their authority class

Classes follow the brief: **authority** (governs its subject), **derivative**
(an account that its sources override), **evidence** (factual record of what
happened) and **operational** (runtime state, non-authoritative). "Loops" means
the loops that currently write the surface.

| # | Surface | Path pattern (project-relative) | Written now by | Class | Method source | PEC tier / entity it could feed |
|---|---|---|---|---|---|---|
| S1 | Current undertaking graph | `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` | App, Piping | **Authority for undertaking execution state only**. Graph construction "changes no scope, hold, lifecycle or release authority" | `construct-local-work-graph` §4; template; `docs/SPEC.md` §9.8; App/Piping `LOOP_INIT.md` §1 | Record: a new *WorkGraph/WorkNode* shape (run identity, node IDs, node state, DEL bindings, PR/commit references). Candidate source for CandidateBrief, parked lanes and DependencyEdge (intra-undertaking) |
| S2 | Colocated graph evidence | `WorkGraphs/<undertaking>/*` other than `WORK_GRAPH.md` (App trial: `RUN_EVIDENCE.md`, check JSON/TXT) | App (trial) | **Evidence** | App trial folder; `ROOT-WORKGRAPHS-PATH-ANCHOR-20260923.yaml` `scope_limits` ("Colocated run evidence remains outside the live-surface selection") | Record: RunRecord evidence pointers (path + SHA only) |
| S3 | Central loop receipt | `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` | App, Piping (prospective from 2026-09-23; one exists) | **Derivative**: "a concise, derivative account … neither a second execution graph, a future-work list nor decision authority" | App/Piping `LOOP_INIT.md` §5; receipt's own banner; central-receipts manifest | Record: Receipt (re-sourced); RunRecord join |
| S4 | Run evidence in AgentRuns | `execution/_Coordination/AgentRuns/<RunID>/**` (e.g. `EVIDENCE.md`, `checks/*.log.gz`) | App, Piping, PEC, Runtime | **Evidence** | `docs/SPEC.md` §9.8 ¶1 | Record: RunRecord evidence pointers |
| S5 | Deliverable run index | `execution/PKG-*/1_Working/DEL-*/MEMORY.md` `## Runs` | App, Piping | **Derivative index**: "not a decision record or future assignment" | `docs/templates/MEMORY_TEMPLATE.md`; `AMENDMENT_2026-09-22_…` item 1 | Record: Deliverable↔RunRecord join (run ID token, date, link targets) |
| S6 | Lifecycle | `execution/PKG-*/1_Working/DEL-*/_STATUS.md` | all | **Authority** (lifecycle and history) | harness README §Authority classes; App/Piping `AGENTS.md` | Record: Package/Deliverable census. The "remaining items" field is empty by design in App/Piping (0 `## Remaining` headings at basis), live in PEC (57) |
| S7 | Production commitments | `DEL-*/ScopeOfWork.md` | all | **Authority** | App/Piping `AGENTS.md` | Not a PRD feed today; possibly a deliverable-contract presence/SHA only |
| S8 | Dependency registers | `DEL-*/Dependencies.csv`, `_DEPENDENCIES.md` | all | **Authority** (formal rows) | `bounded-reconciliation` §2 | Record: DependencyEdge (unchanged) |
| S9 | Decisions | `execution/_Coordination/_DECISIONS/_REGISTER.md` + packets | all | **Authority** (rulings, K-AUTH-1) | PRD §7.1 DecisionRow | Record: DecisionRow (unchanged) |
| S10 | Task Management register | `execution/_Coordination/_TaskManagement/REGISTER.csv` | App, Piping, PEC, Root | **Authority for concern disposition only**: "neither direct production nor grant scope" | `workflows/task-management/resources/contract.md` §Ownership | Not in PEC-RCN-002 today. Candidate slate input (rows awaiting human disposition) |
| S11 | Loop procedure | `loop/LOOP_INIT.md` | all | **Authority (instruction surface)**; evergreen for App/Piping, with "no undertaking-specific pointer or execution state" | `docs/SPEC.md` §9.8 ¶2; `NOTICE_2026-09-23_EVERGREEN_…` | Record: Loop identity and procedure SHA only. **Carries no Step/Gate state any more** |
| S12 | Scope-change state | `execution/_ScopeChange/_LATEST.md` + packages | all | **Authority** | App `LOOP_INIT.md` pointers | Candidate gate source (checkpoint state) |
| S13 | Git history and refs | commits, merges, branches, worktrees | — | Committed/merged history is **authority** for what landed (D-GOV-01 "Git-tracked"). Worktree and dirty state is **operational** | PRD PEC-PRS-002 | Record: merge resolution of PR numbers (I-18). Presence: worktree/branch/dirty scan |
| S14 | Historical ledgers | `loop/LOOP_RECEIPTS.md` | App, Piping: **historical** (frozen; the linter receipt states the Piping ledger "remains unchanged at Receipt-162"). PEC, Root, Runtime, bridge: live | **Derivative** (historical where frozen) | App/Piping `AGENTS.md`; central-receipts manifest `scope_limits` | Record: Receipt (historical or live grammar per loop) |
| S15 | Historical JSON run evidence | `AgentRuns/**/WORK_GRAPH.json` (App 56, Piping 83, Runtime 2, PEC 1 at basis); `STATUS.json` (App 246, Piping 292, PEC 13); `RUNTIME_SUMMARY.json` (App 39, Piping 34, Runtime 8) | none prospectively for App/Piping | **Evidence** (historical) | `surface_roles.py` still lists `WORK_GRAPH.json` as CONTROL and `STATUS.json` as EVIDENCE names | Record: historical RunRecord/DependencyEdge |
| S16 | Workplans | `plans/workplans/**` etc. | none (PEC retired them under D-PEC-80; App/Piping retired) | Historical | `PEC:loop/LOOP_INIT.md` §4 | None live |
| S17 | Harness config | `_harness/adapter.yaml` | App, Piping, Runtime (root at `execution/_harness/`). **None in PEC** | "Harness configuration authority only … never lifecycle or project truth" | harness README §Authority classes; `DEL-02-07` CLM-011 | Feed manifest today (SOW-017). Declares `status_glob`, `parser_dialect`, `decision_register`, `dag_pointer`; **declares no WorkGraphs, receipt or MEMORY surface** |
| S18 | Runtime service state | application-private data dir, socket, tokens | App's own Runtime instance | **Operational** (D-GOV-20 item 5 survives; A2 "client tokens private to the application") | `D-GOV-43_supplement_topology_A2.md`; Runtime README §Architecture; consumer guide §Host configuration | Presence only, and only if reachable (§5: it is not) |
| S19 | PEC loop registry | `PEC:v2/config/loops.json` | PEC | **PEC configuration authority** over PEC's service set only | D-PEC-78 | Loop entity; candidate feed declaration home (O-B) |

Two facts from the method shape the model more than any single path does:

- **The terminal graph node trails Git by design.** The method forbids
  "requir[ing] a later commit solely to write the final merge result back into
  its own candidate" (`construct-local-work-graph` §4; template "Current state
  and recovery"). All three trial graphs at basis show `F1` `ACTIVE`, yet the
  cited final PRs are merged in local Git: #868 → `10b672cae`, #876 →
  `0b276a7fa`, #873 → `c56ae4a28`. PEC must *derive* completion from Git
  ("F1's PR merge commit is reachable from the integration ref"). It must not
  read completion from the cell, and it must not classify the lag as drift.
- **The run identity is declared, not implied by path.** Graph folder names
  and stable run IDs differ in two of the three trials
  (`replay-session-boundary-2026-09-23` ↔ `APP-REPLAY-BOUNDARY-2026-09-23`;
  `dec025-clean-base-repair-2026-09-23` ↔ `PIP-DEC025-BASELINE-2026-09-23`).
  The join key across graph, receipt, AgentRuns folder and MEMORY row is the
  run ID token declared in the graph's "Stable run identity" bullet.

### 3.2 What PEC may extract (content-minimal, I-09)

| Surface | Extractable (identifiers, tokens, SHAs, counts, paths) | Never extracted |
|---|---|---|
| S1 graph | run ID token; section presence; Work-table node IDs (leading `[A-Z][0-9]+` token); node state from the closed vocabulary `PLANNED/READY/ACTIVE/BLOCKED/UNCERTAIN/COMPLETE` (template); `DEL-\d\d-\d\d` tokens per node; PR numbers; hex SHAs; linked paths; per-state node counts; blob SHA; last-touch commit | Outcome, "needs", completion-check and result prose; intent and steering bullets; "Open questions" text |
| S3 receipt | `Receipt-ID`, `Examined-Through` SHA, `Parent-Receipt` token, PR numbers, linked paths; *presence* of `Owner-Direction`, `Model-Attribution` and `Gate-Outcome` fields | Result, checks/limits prose; owner-direction quotations; the gate-outcome text (prose in the only example) |
| S5 MEMORY | run ID tokens and dates under `## Runs`; link targets (paths, PR numbers); row count | Run descriptions |
| S2/S4 evidence | paths, SHAs, sizes, file counts | Any content |
| S14/S15 historical | per-grammar fields already scoped by DEL-02-03/-04/-05 | as before |

### 3.3 Provenance and freshness semantics (proposed for every option)

1. **Citation tuple.** Every record-tier fact carries a citation tuple:
   `(loop_id, path, blob_sha, examined_commit, grammar_id@version,
   parse_outcome ∈ {parsed, partial, unparseable, absent})`. This extends
   PEC-ORI-004 and is the Explain source for PEC-K-08.
2. **Per-feed freshness** (PEC-ORI-003). Record the examined-through commit.
   Per surface, record the last-touch commit and its age. Per graph, also
   record:
   - *graph–Git lag* for each referenced PR (merged per Git, but the node is
     not `COMPLETE`);
   - where the graph's own "Checked basis" line has a parseable SHA, its
     ancestry distance to the examined commit.

   Per receipt, record `Examined-Through` ancestry to the examined commit.
3. **Classes of lag.**

   | Lag | Classification |
   |---|---|
   | Terminal-node lag after a final-PR merge | *trailing by method design*: derived completion, advisory, Explain-cited |
   | Non-terminal lag | DriftFinding "graph behind Git" (PEC-RCN-004) |
   | Historical surfaces that do not change | Not stale. They carry a `historical` label, so silence is never reported as staleness (PEC-ORI-006) |

4. **Declared vs live.** A graph node in `ACTIVE` is reported as "declared
   ACTIVE as of commit X (age N)". That is a record-tier claim, never a
   liveness assertion (PEC-K-05, PEC-PRS-005).
5. **Ref scope.** Graphs are committed "early in the undertaking's PR
   sequence" (`construct-local-work-graph` §4), so an in-flight graph first
   exists on an unmerged branch. Reading only the integration ref hides
   in-flight undertakings until their first PR merges. Reading local branch
   refs is read-only plumbing, but it cites unintegrated commits. This is an
   owner choice (Q7).

---

## 4. Options

All three options keep I-01..I-19. They differ in **what PEC treats as a
first-class feed** and **who declares which grammar applies to which loop**.

### O-A — Shared-method surfaces first-class; JSON run evidence and workplans become declared historical grammars

**Shape.** S1, S3 and S5 become first-class feeds. Their paths are fixed by
convention in PEC grammar adapters (SPEC §9.8 fixes them for App/Piping).
S15 and S16 become *historical grammars*: they are parsed only to label and
index history, never as live feeds. S14 stays live for loops that still write
ledgers (PEC, Root, bridge, Runtime) and historical for App/Piping.
`adapter.yaml` stays the manifest for what it already declares (`status_glob`,
dialect, register, DAG pointer). The new surfaces are discovered by
convention, not by declaration.

**PRD rows affected.**
- PEC-RCN-002: feed list rewritten; manifest clause retained.
- §7.1: Workplan/Step/Gate retired or re-sourced (S11 no longer carries gates;
  gates re-source to S9/S12 and graph `BLOCKED` nodes). Receipt re-sourced
  (S3 primary, S14 per-loop). RunRecord re-sourced from S1/S3/S4 instead of
  `STATUS.json`/`RUNTIME_SUMMARY.json`. DependencyEdge loses `WORK_GRAPH.json`
  as a live source. CandidateBrief is redefined over graph nodes.
- PEC-ORI-001: "newest applicable receipt", "open tranches/candidate briefs"
  and "parked lanes" are re-expressed over S1/S3.
- Informational: §2 corpus description.

**Decomposition entities.**
- SOW-001 MODIFY (entity list).
- SOW-013 MODIFY (central receipts primary; ledger grammars per loop).
- SOW-014 MODIFY/RECLASSIFY (JSON becomes a historical grammar; the RunRecord
  source moves).
- SOW-015 MODIFY (`WORK_GRAPH.json` historical; add intra-graph edges from S1).
- SOW-016 MODIFY (workplans historical; `LOOP_INIT` gives identity/SHA only).
- SOW-017 unchanged.
- ADD a WorkGraphs discovery/parse item and a MEMORY `## Runs` item.
- C-list unchanged.
- Vocabulary Map gains a disambiguation: graph node IDs `P1`/`C1`/`F1` collide
  with PEC release phases P1–P4 and constraints C1–C16.

**Deliverables.**
- PKG-02: DEL-02-03 (L), DEL-02-04, DEL-02-05 and DEL-02-06 need Scope of Work
  currency. A new work-graph parser deliverable (candidate DEL-02-08) and a
  MEMORY-runs parser (candidate DEL-02-09) are added, or these are folded into
  DEL-02-05/DEL-02-04 with re-enveloping. DEL-02-07 unchanged.
- PKG-03: DEL-03-03 gains the "trailing by design" class; DEL-03-01's
  `[E-P25]` edge is unchanged.
- PKG-04: DEL-04-01 and DEL-04-05 need Scope of Work currency.
- PKG-06/07: see §5, which is independent of O-A/O-B/O-C.

**Parity target.**
- The harness already classifies canonical `WorkGraphs/<u>/WORK_GRAPH.md` as a
  live CONTROL surface (`surface_roles.py` `classify_surface`; tranche
  `ROOT-WORKGRAPHS-PATH-ANCHOR-20260923`).
- `RECEIPT.md` under AgentRuns falls through to **UNCLASSIFIED "unknown
  managed AgentRuns artifact"**: it is in neither `CONTROL_NAMES` nor
  `EVIDENCE_NAMES`.
- The harness parses neither surface's grammar. Parity on S1/S3/S5 is
  therefore "no counterpart: explained". The comparable set stays lifecycle
  census plus DAG pointer (`DEL-03-04` TBD-003).

**P1 exit test.**
- PEC's own build has no WorkGraphs, no central receipts and no MEMORY
  `## Runs` (I-16). The P1 self-ingest therefore exercises almost none of
  O-A's first-class feeds. These are validated only through parser fixture
  suites (§6).
- `adapter.yaml` is the manifest, and **PEC has none** (`DEL-02-07` CLM-011).
  The P1 reconciler over PEC's own build therefore has no declared manifest
  and falls back to an implicit one. This gap already exists in the accepted
  basis. O-A does not close it.

### O-B — Dual-shape feeds declared per loop in the PEC-owned registry (manifest moves from `adapter.yaml` to `loops.json`)

**Shape.** `loops.json` moves to schema version 2. Each row declares which
feed grammars PEC applies to that loop and whether each is `live` or
`historical`, citing the loop's own record for the declaration (e.g. a loop's
`AGENTS.md` for "ledger historical"). Old and new surfaces are disjoint files,
so PEC reads both generations side by side with no cutover date. `adapter.yaml`
stops being PEC's manifest. PEC may still *read* it as a parity-peer input, to
compare its declared census population with the harness's `status_glob`. There
are two sub-variants:

- **O-B1, free declarations:** each row lists feed kinds with path globs and a
  grammar ID.
- **O-B2, closed profiles:** each row selects from a closed, PEC-versioned
  vocabulary of *feed profiles*. Path conventions and grammars live in PEC
  adapter code. A row carries only a profile ID, a version, a state and a
  basis citation. Illustrative shape only, not a configuration proposal:

  ```json
  {"loop_id": "…", "loop_init_path": "…/loop/LOOP_INIT.md",
   "feed_profiles": [
     {"profile": "shared-dev-loop", "version": 1, "state": "live", "basis": "<path to the loop's own adopting record>"},
     {"profile": "loop-receipts-ledger", "version": 1, "state": "historical", "basis": "<path>"}]}
  ```

  Example profiles:

  | Profile | Covers |
  |---|---|
  | `shared-dev-loop` | S1 + S3 + S5 + S6 + S8 + S9 |
  | `remaining-loop` | S6 with a live `## Remaining` + S14 live + S8 + S9 (PEC's own current loop) |
  | `loop-receipts-ledger` | S14 |
  | `agentruns-json` | S15 |

**PRD rows affected.**
- PEC-RCN-002: the feed list is re-expressed as feed *kinds*; the manifest
  clause moves from "per-project `_harness/adapter.yaml`" to "the PEC loop
  registry's per-loop feed declarations".
- §7.1 changes as in O-A.
- §16.3 text (D-PEC-79 postimage) stays true: the registry home and shape are
  unchanged, and only the schema version advances. The v2.3 candidate needs
  one added clause saying that rows may declare feed profiles.
- PEC-RCN-005 is unchanged.

**Decomposition entities.**
- Everything in O-A, plus SOW-017 MODIFY or RECLASSIFY: "consume per-project
  `adapter.yaml` as the feed manifest" becomes either (a) OUT, replaced by
  registry-declared feeds, or (b) re-scoped to a parity-peer read.
- SOW-077 and SOW-094 MODIFY: registry rows gain feed declarations.
- OI-003 stays resolved (the home is unchanged). A2 is expected to record
  whether the strict-v1 wording in D-PEC-78 needs an owner note for v2.

**Deliverables.**
- DEL-01-06: its Scope of Work gains a v2 schema; `RegisteredLoop` gains a
  field; VER-001/VER-003 re-run against the new fixtures. This is a v2 source
  change and needs its own D-PEC packet (`D-PEC-86` §4 opens no `v2/**`).
- DEL-02-07 is re-purposed (feed-declaration consumer, or parity-peer reader)
  or retired.
- PKG-02/03/04 are as in O-A. DEL-03-01's `[E-P25]` manifest edge re-points
  from DEL-02-07 to DEL-01-06.
- PKG-06/07: see §5.

**Parity target.** The same as O-A for the surfaces. In addition, PEC's census
population and the harness `status_glob` can now diverge, because they are
declared in two places. PEC reads `adapter.yaml` and reports the divergence as
a DriftFinding ("census population mismatch").

**P1 exit test.** PEC's own row already exists (`loop_id: pec`) and would
declare `remaining-loop`. **The absent-manifest gap in P1 self-ingest closes.**
PEC's later migration to the shared method (I-16, Q8) becomes one owner-gated
row change from `remaining-loop` to `shared-dev-loop`, with the ledger
declared `historical`, and no parser rework.

**O-B1 versus O-B2.**
- O-B1 lets any row describe any layout. It also turns PEC configuration into
  a second description of each foreign loop's file layout, with every
  foreign-method change needing an owner-gated PEC edit.
- O-B2 keeps the configuration small and strictly validatable. It keeps path
  knowledge in versioned grammar adapters (I-17) and limits owner-gated edits
  to adopting a profile. The cost is that a genuinely new layout needs a new
  profile version, which is code plus a packet.

### O-C — Minimal re-pointing of PEC-RCN-002 only

**Shape.**
- In PEC-RCN-002 (and mirrored SOW-013/-015 wording), `WORK_GRAPH.json` is
  replaced by `WorkGraphs/<undertaking>/WORK_GRAPH.md`, and `LOOP_RECEIPTS.md`
  becomes "`LOOP_RECEIPTS.md` or `AgentRuns/<RunID>/RECEIPT.md`".
- Nothing else changes: the entity model, the `adapter.yaml` manifest,
  `STATUS.json`/`RUNTIME_SUMMARY.json` as live RunRecord sources, workplan
  parsing, and the presence and stream rows all stay as written.

**PRD rows affected.** PEC-RCN-002 only. The following stay stale and
contradict current file truth:
- §7.1 Workplan/Step/Gate and the RunRecord sources;
- PEC-PRS-001/-004, PEC-STR-003, §8 and §12 P4 (daemon SSE), and §15 (D-GOV-20
  "complemented").

**Decomposition entities.** SOW-013 and SOW-015 wording MODIFY. SOW-014,
SOW-016, SOW-001, SOW-026..037 and SOW-087 are left as is, with their drift
recorded as known. No ADD.

**Deliverables.** DEL-02-03 and DEL-02-05 need Scope of Work currency. Every
other PKG-02/03/04/06/07 contract keeps July premises, so the drift moves into
the Scope of Work currency list and future scope changes.

**Parity target.** Unchanged.

**P1 exit test.** Unchanged, including the absent-manifest gap.

**The trade.** O-C is the smallest and fastest SCA-005, and it resolves the
two parser-blocking premises. But it defers every model question, so the next
SCA inherits a PRD that describes a daemon that no longer exists. That
conflicts with the ASSESSMENT's intent to "rebaseline", and with PRD §12's
instruction that drift "becomes a scope-change request rather than silent
parser work". O-C turns known model drift into silent parser work.

### 4.1 Side-by-side

| Dimension | O-A | O-B (B2) | O-C |
|---|---|---|---|
| New surfaces first-class | yes, by convention | yes, by declared profile | re-pointed paths only |
| Who declares the grammar for a loop | PEC code convention and heuristics | PEC registry row, owner-gated, citing the loop's own record | harness `adapter.yaml` (only `parser_dialect`) |
| `adapter.yaml` role | manifest | parity-peer input only (or retired from scope) | manifest |
| PEC self-ingest manifest gap | open | **closed** | open |
| Future PEC loop migration | parser and heuristics revisit | one row change | new SCA |
| Changes to D-PEC-78 artifacts | none | schema v2 + port field (packeted) | none |
| PRD rows touched | RCN-002, §7.1, ORI-001, (§2) | same + §16.3 clause | RCN-002 |
| New SOW/DEL candidates | 2 SOW, ≤2 DEL | same, + DEL-02-07 re-purpose | none |
| Residual stale premises | presence/streams unless §5 is also taken | same | many |
| SCA-005 size | medium | medium-plus | small |

---

## 5. Presence and streams under D-GOV-43 A2

### 5.1 What changed (facts)

- The per-user daemon is retired. The Runtime is "an application-owned
  service", started, owned and stopped by the App as a child process, and it
  owns the stock Codex child (`D-GOV-43_supplement_topology_A2.md`
  "Effect on the ruled items"; Runtime `README.md` §Architecture).
- "Client tokens are private to the owning application." Each consuming
  application runs "a separate Runtime instance and private data directory";
  its client ID "is not a globally shared account or a broker for multiple
  applications". Consumers must not "point a new consumer at the running
  Chirality App's socket or token file" (`APPLICATION_CONSUMER_GUIDE.md`
  §Host configuration and startup).
- D-GOV-43 supersedes D-GOV-20 items 2–4 on the App MVP path
  (`D-GOV-43_codex_host_replatform.md`, "Supersedes in the stated parts").
  D-GOV-20 item 5 is not superseded: runtime state is operational and
  non-authoritative, and AgentRuns stay checkout-contained.
- "PEC's integration opportunity … is preserved; its compatibility unverified
  and not an MVP prerequisite" (A2 supplement; Runtime `README.md`).
- Consequently the PRD's presence and stream sources now name absent actors:
  - PEC-PRS-001 ("session identity and lifecycle remain daemon-owned");
  - PEC-PRS-004 ("daemon and hook feeds");
  - PEC-STR-003 ("runtime-daemon SSE subscriber");
  - PEC-API-001's D-GOV-20 reference;
  - §8 ("runtime daemon");
  - §12 P4;
  - §16.2 (a "daemon global event feed");
  - §16.6 ("the daemon's project-scoped token registry");
  - SOW-035, SOW-076, SOW-080 and SOW-087, and DEL-07-02 and DEL-07-05.

  None of these has a present referent.

### 5.2 P-α — PEC as its own Runtime consumer instance (not recommended)

A PEC-owned Runtime instance would see only the sessions **it** hosts. Tokens
are private per application, and no instance brokers another's sessions. It
therefore yields no presence about App, Piping or any Codex session the human
runs elsewhere. Obtaining anything at all would mean hosting sessions, and
that fails the invariants:

- The standalone composition is "one application-owned service and stock
  Codex child", configured with a pinned Codex executable (consumer guide
  §What can be reused and §Host configuration). That makes PEC an execution
  host, which conflicts with I-10 (C13, ADR-PEC-V2-002 posture 3) and the
  permanent OUT SOW-067.
- It would also require a `pec.yaml` profile amendment (I-19), so it lacks the
  authority basis as well as the purpose.

**Verdict: P-α yields no presence of value and fails I-10.**

### 5.3 P-β — Presence from Git only; declared activity from files as record tier; Runtime-sourced presence deferred with an explicit trigger (recommended)

- **Presence tier (operational, TTL'd).**
  - Git/worktree observation (PEC-PRS-002) of local worktrees, branches, HEAD,
    ahead/behind counts, and dirty path names/counts. This requires no Runtime
    and no consumer, so it survives unchanged. The scan snapshot carries a
    scan age as its heartbeat analogue (PEC-PRS-005).
  - Hooks-CLI push from a *separately authorized* consumer (PEC-STR-003 second
    bridge, P3) stays as a PEC-side capability. Its live use still needs that
    consumer's own authorization (PRD §12 P3).
- **Record tier, labelled "declared activity", never liveness.**
  - Graph nodes in `ACTIVE`/`READY`/`BLOCKED`, with their `DEL-` bindings and
    the graph's commit age (S1, §3.3.4).
  - Graphs found on local unmerged refs, if Q7 permits.
  - This is the durable, declared, attributable surface that PRD §3 outcome 3
    and PEC-K-09 ask for. The shared method now produces it natively.
- **Overlap detection (PEC-PRS-006) without sessions.**
  - Deliverable-level: two or more graphs declaring `ACTIVE` nodes bound to
    the same `DEL-` ID.
  - Path-level: dirty-path intersections across worktrees.
  - Both are advisory. Write boundaries in graphs are prose, so path-level
    overlap from graph *declarations* is not extractable under I-09. This
    limit is stated per PEC-ORI-006.
- **Deferred, with a trigger.**
  - The Runtime SSE bridge (DEL-07-02) and the shared-runtime client seam
    (DEL-07-05, SOW-087) move to *Deferred OUT*, alongside SOW-074 and
    SOW-086.
  - The trigger is: a Runtime-owning loop publishes, under its own authority,
    an observation interface usable by a non-owning local reader, **and**
    `pec.yaml` is amended, **and** a D-PEC packet names the bridge.
  - PEC can neither request nor require that interface (I-01; `pec.yaml`
    forbidden claims).
  - Live hierarchy edges (DEL-06-04, PEC-PRS-004) are deferred with the same
    trigger, because file truth carries parentage only as run-evidence prose.
- **Considered and rejected.** Reading Codex or Runtime user-data (session
  rollouts, private data directories). It is content-bearing (I-09), crosses
  another application's credential and custody boundary (A2; consumer guide
  "Keep token/config paths … in the trusted host"), and treats operational
  state as a feed.

### 5.4 Consequences of P-β

**PRD rows**
- PEC-PRS-001 is re-expressed: sessions are "reported by an explicitly
  authorized consumer through the hooks interface". Its "daemon-owned" clause
  becomes "Runtime-owned per application (D-GOV-43 A2)".
- PEC-PRS-004 is deferred.
- PEC-STR-003: the daemon bridge is deferred; hooks and cmux stay.
- PEC-API-005 (SSE to dashboards) is unaffected: that is PEC's own outbound
  subscription.
- §4.2 and §15: the D-GOV-20 wording is updated to D-GOV-43 A2. The surviving
  "no second loop" meaning is unchanged.
- §12 P4 is narrowed.
- §16.2 is re-expressed or retired, and §16.6 narrowed, as owner questions
  (Q6).

**Decomposition**
- SOW-026 MODIFY; SOW-029 RECLASSIFY to deferred; SOW-035 RECLASSIFY to
  deferred; SOW-087 RECLASSIFY to deferred.
- SOW-076 and SOW-080 go to owner disposition (Q6).
- OI-002 and OI-006 need re-expression.

**PKG-06**
- DEL-06-02, DEL-06-05 and DEL-06-06 stay, with Scope of Work currency.
- DEL-06-01 is sourced only from hooks.
- DEL-06-03 correlation degrades to a worktree × branch × graph join (session
  identity unavailable without hooks).
- DEL-06-04 is deferred.

**PKG-07**
- DEL-07-01 and DEL-07-03 stay.
- DEL-07-02 and DEL-07-05 are deferred.
- DEL-07-04 is unchanged.

**Validation**
- SOW-061 (seeded-conflict overlap) stays feasible from graphs plus Git.
- SOW-062 (TTL honesty) applies to hook-pushed records and scan snapshots.
- SOW-063 (stream-loss recovery) keeps its meaning for the hooks stream only.

**Graceful absence.** Every presence input is optional. With no hooks consumer
and no scan, orientation is still served from the record tier and nothing
blocks (I-01).

**An honest observation for the falsification clause (PRD §11).** The shared
method now delivers natively part of what PEC was meant to add:

- The evergreen `LOOP_INIT` and a single current graph shrink Step-0
  re-derivation.
- Committed graphs give a declared, durable activity surface.

PEC's marginal value therefore concentrates on cross-loop aggregation,
Git-derived completion, drift and overlap detection, and the decision slate.
The Step-0 baseline (SOW-058, DEL-10-01) measured against July-shaped loops
would overstate PEC's benefit. Whether to re-baseline it against shared-method
loops is Q9.

---

## 6. Fixture strategy using the 2026-09-23 trial runs

**Principle.** Fixtures must not copy another loop's prose into PEC's tree
(I-09 spirit, I-12, and drift avoidance). Golden expectations must themselves
be content-minimal.

1. **Golden-by-reference, real corpus.**
   - Each fixture is a pinned `(commit, path, blob)` triple, read through
     read-only Git plumbing (`git cat-file`/`git show`; I-06). Its expected
     output is a content-minimal golden record (§3.2 fields only).
   - `pec-tests.yml` checks out with `fetch-depth: 0`, so pinned objects are
     available in CI.
   - Pin to the examined basis `d61981ee2`. Later edits by App/Piping to these
     files do not break PEC tests. A separate, non-gating *live* read at HEAD
     reports differences as DriftFindings.

   | Fixture | Pinned blobs (at `d61981ee2`) | What it exercises |
   |---|---|---|
   | FX-APP-1 App replay trial | graph `d25cae61…`; `RUN_EVIDENCE.md`; DEL-05-04 `MEMORY.md` | Run ID ≠ folder name. `F1 ACTIVE` while #868 is merged at `10b672cae` (derived completion, trailing by design). **No `RECEIPT.md`**: the trial predates the 2026-09-23 receipt rule, so this is an explicit coverage limit, not nonconformance (I-15). Evidence is colocated in the WorkGraphs folder. MEMORY `## Runs` uses a bullet form (template prescribes a table) above legacy `## Decisions And Evidence` sections. Node IDs carry an em-dash suffix |
   | FX-PIP-1 Piping linter trial | graph `ae942d99…`; `RECEIPT.md` `23623e2c…`; DEL-08-05/08-01/10-04 `MEMORY.md` | Full shared shape. An extra `R1` receipt node not in the template. Receipt fields `Receipt-ID`, `Examined-Through` (`8645c269…` = #867 merge), `Parent-Receipt: none`, and prose `Gate-Outcome` (field presence only). `F1 ACTIVE` while #876 is merged at `0b276a7f`. Run ID = folder. Ledger declared historical at Receipt-162 |
   | FX-PIP-2 Piping DEC-025 trial | graph `e471421c…`; AgentRuns `EVIDENCE.md` `76e618a5…` + `checks/*.log.gz`; four `MEMORY.md` | Run ID ≠ folder. **Evidence but no receipt** in AgentRuns. Two `W` nodes. `F1 ACTIVE` while #873 is merged at `c56ae4a2`. Not every touched MEMORY has `## Runs`, which is a partial-coverage case. Compressed logs are indexed by path/SHA/size only |
   | FX-PEC-0 PEC self-ingest | PEC `_STATUS.md` (57 with `## Remaining`), `LOOP_RECEIPTS.md`, 64 `Dependencies.csv`, the one historical `WORK_GRAPH.json` | P1 directed bootstrap (DEL-10-10) under the `remaining-loop` grammar. Proves that dual-generation reading works on the loop PEC actually builds |
   | FX-HIST samples | a few historical App/Piping `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json` and the frozen ledgers | Historical-grammar labelling. Silence is not staleness |

2. **Synthetic grammar-edge fixtures** are authored fresh in PEC's tree under a
   v2 packet. Cases:
   - a missing "Stable run identity";
   - duplicate run IDs across graphs;
   - an unknown state token;
   - a Work table with no terminal node;
   - a receipt without `Examined-Through`;
   - an `Examined-Through` SHA that is not an ancestor;
   - a MEMORY `## Runs` row naming a run with no graph;
   - a PR number with no local merge commit (I-18: reported "unresolved
     locally", never guessed);
   - two `ACTIVE` graphs bound to the same `DEL-` ID (seeded overlap for
     SOW-061).
3. **Content-minimal assertion.** Every golden test also asserts that the
   store holds no run of source text above a small length threshold from any
   fixture blob. This ties to the DEL-01-03 guard without broadening it.
4. **Kill-test pairing.** The three trials completed, merged and closed with
   no PEC present. The kill test cites them as observed absence baselines
   (PEC-SVC-004).
5. **Where fixtures land in the phases.** At P1 these are *parser fixture
   suites* (DEL-02-x OUT fixture tests), not live ingestion of a second loop.
   Live second-loop ingestion remains the PRD §12 generality test after
   self-ingestion (OI-010 unaffected). Whether to pull it forward is Q5.

---

## 7. Recommendation

**Recommend O-B2 with P-β.**

- **O-B2 content.** The feed content is O-A's: shared-method surfaces are
  first class; JSON run evidence, workplans and App/Piping ledgers are declared
  historical grammars. The *declaration* of which grammar generation applies
  to which loop moves into the PEC-owned registry as a closed, versioned
  feed-profile vocabulary. `adapter.yaml` is kept only as a parity-peer input,
  used to compare census populations with the harness.
- **P-β presence.** Presence is Git-only plus hooks. Graph-declared activity
  is record tier. Runtime bridges and live hierarchy are deferred with an
  explicit trigger.
- **Freshness semantics.** Adopt the §3.3 semantics, including derived
  completion for the terminal node.

**Why.**

1. **A declaration is needed, and PEC is the only lawful home for it.** PEC
   will read two generations for at least the SCA-005 horizon (I-15, I-16).
   PEC-ORI-006 honesty and DEL-02-03 OUT-001 ("applies the grammar declared
   for that loop") both need a *declared* grammar per loop. Heuristic
   detection (O-A) makes coverage limits guesswork. `adapter.yaml` (O-C) is
   harness configuration authority that PEC does not own and cannot extend
   without writing into other loops' governed files. D-PEC-78 already made
   PEC's registry the lawful home for "which loops, read how".
2. **It closes an existing P1 defect.** PEC's own loop has no `adapter.yaml`,
   and the harness does not observe PEC (`harness.py` `OBSERVABLE_PROJECTS`
   excludes it; `status --project pec` is refused). Under O-A or O-C, the P1
   self-ingest has no declared manifest. Under O-B, PEC's existing `pec` row
   declares it.
3. **It makes the deferred PEC migration cheap.** Under O-B, PEC's own later
   migration is one owner-gated row change, not another SCA.
4. **B2 over B1.** Path conventions stay in versioned adapters (I-17), and
   the configuration stays strict and small (I-11). Owner-gated edits then
   mean "adopt profile X", which is the level at which the owner actually
   decides.
5. **P-β over P-α.** P-α yields no cross-application presence under A2 and
   would make PEC an execution host. P-β keeps outcome 3 reachable through
   file-native graphs and Git, and keeps every input optional.

**What it trades away.**

- **Parity by construction.** With `adapter.yaml` as the shared manifest, PEC
  and the harness look at the same `_STATUS.md` population automatically.
  Under O-B they can diverge, and PEC must detect and explain the divergence.
- **Zero-configuration onboarding.** Every loop PEC serves needs an
  owner-gated registry row with profiles, and every new layout generation
  needs a new profile version (code plus a D-PEC packet).
- **Size and schedule.**
  - SCA-005 grows: 2 ADD SOWs, SOW-017 re-scoped, SOW-077/094 amended, up to
    2 new DEL, DEL-02-07 re-purposed, and PKG-06/07 reclassifications.
  - A v2 source change to `loops.schema.json`, `loops.json` and the
    `RegisteredLoop` port needs its own packet after SCA-005.
  - DEL-01-06's accepted verification must re-run against v2.
- **Session-level presence.** Presence loses session identity, live hierarchy
  and Runtime-sourced liveness indefinitely. The presence board (DEL-09-05)
  becomes a worktree and declared-activity board unless a hooks consumer is
  separately authorized.
- **Some product ambition.** Defer-with-trigger admits that PEC-PRS-004 and
  the §12 P4 hierarchy tier may never have a source. The PRD should say so
  rather than keep a phase exit that no lawful input can satisfy.

---

## 8. Open owner questions (phrased as decisions)

| # | Decision | Options | Proposal note |
|---|---|---|---|
| Q1 | Feed model for SCA-005 | O-A convention / **O-B2 declared profiles** / O-B1 free declarations / O-C minimal re-point | §7 |
| Q2 | Fate of `adapter.yaml` in PEC scope (SOW-017, DEL-02-07) | (a) remains PEC's manifest; (b) **parity-peer input only (DEL-02-07 re-purposed)**; (c) removed from PEC scope | (b) follows from O-B |
| Q3 | Presence and streams under A2 | **P-β (Git + hooks; declared activity is record tier; Runtime bridges and hierarchy deferred with trigger)** / P-α PEC-owned Runtime instance / P-δ drop the presence tier and PKG-06/07 from the product entirely / keep rows as written | P-α fails I-10. P-δ is the leanest falsification-friendly choice but gives up PRD outcome 3's Git-based half |
| Q4 | Orientation semantics over graphs (PEC-ORI-001; SOW-004) | (a) **re-source "open tranches/candidate briefs" and "parked lanes" to graph `READY`/`ACTIVE`/`BLOCKED` nodes, with derived terminal completion from Git**; (b) report node states verbatim only, with no derived completion; (c) keep ORI-001 wording and let parsers approximate | (b) will show every finished undertaking as `ACTIVE` by method design |
| Q5 | When the external trials enter | (a) **P1 as pinned parser fixture suites only**; (b) P1 live read-only ingest of App/Piping (a second loop at P1, beyond OI-010's first-loop reading); (c) P2 only | (a) keeps OI-010 and the bootstrap shape |
| Q6 | A2 effects on §16 items | For each of §16.2 (daemon global feed), §16.6 (auth reuse), §16.8 (receipt contract) and §16.9 (contract home/transport): **re-express in the PRD v2.3 candidate as a stated factual premise with the decision still open** / retire as moot / leave untouched for separate rulings | §16.2's daemon no longer exists. §16.6 reuse of the App registry is foreclosed by the consumer guide. §16.8 is partly overtaken, because App/Piping receipts carry D-APP-57-like fields "more or less" (central-receipts manifest). None is ruled here (I-14) |
| Q7 | Ref scope for in-flight graphs (§3.3.5) | (a) integration ref only; (b) **integration ref by default, with local branch refs as an opt-in labelled "unintegrated"**; (c) all local refs always | Affects overlap detection and the "declared activity" view |
| Q8 | PEC's own loop in the registry during and after SCA-005 | (a) **declare `remaining-loop` now; migration later as one row change under its own ruling (I-16)**; (b) declare both generations now; (c) defer PEC's own row changes until migration | Keeps recommendation 4's deferral intact |
| Q9 | Step-0 baseline (SOW-058, DEL-10-01) given the shared method's native gains | (a) **measure on shared-method loops (App/Piping) as the "before"**; (b) measure on PEC's own July-shaped loop; (c) both, reported separately | Affects the honesty of the §11 falsification clause |
| Q10 | P1 parity comparable set, given the harness does not observe PEC (`DEL-03-04` TBD-003) | (a) harness `self-check` facts over `projects/pec`, plus an explained absence of `status` census; (b) PEC seeks harness observability of `projects/pec` (Root harness change plus a PEC adapter file: cross-loop, outside PEC fences); (c) **move the census parity leg to P2 over App/Piping and state it in the P1 exit as explained** | (c) needs an exact P1 exit-test wording change in the PRD |

---

## 9. What this note does not decide

- It does not rule, accept or select any option, and it asserts no scope
  status. SCA-005 checkpoint groups 1–3 remain owner acceptances (`D-PEC-86`
  §3 I-1).
- It writes no Brief, Impact Assessment, Decision Log, `Amendment_Actions` or
  coverage snapshot. Its SOW/DEL action words (MODIFY, ADD, RECLASSIFY) are
  illustrative consequences, not parsed atomic actions.
- It changes no PRD text, accepted decomposition, Scope of Work, `_STATUS.md`,
  registry row, schema, port or other `v2/**` byte. It does not propose exact
  configuration bytes; the JSON in §4 is illustrative.
- It does not apply or alter the D-PEC-79 v2.3 postimage, and it does not
  select any TM-PEC-023 objective blank (`D-PEC-86` I-2, I-3).
- It does not migrate PEC's own loop (`D-PEC-86` I-7), and it creates no duty for App,
  Piping, Runtime, Root or the harness to write, publish, poll or change
  anything.
- It rules on no §16 item. It only flags where A2 or the shared method changed
  the premise.
- It does not dispose of DEL-01-03 remaining items or Task Management notices.
- It makes no claim about A1/A2 findings, and it is not a hash-bound survey or
  inventory. Their outputs govern on overlap.
