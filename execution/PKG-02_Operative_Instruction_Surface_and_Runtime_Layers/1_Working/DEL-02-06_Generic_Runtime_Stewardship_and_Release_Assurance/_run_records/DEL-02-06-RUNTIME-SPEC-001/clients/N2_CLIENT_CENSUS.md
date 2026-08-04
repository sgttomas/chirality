# N2 affected-client census

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N2`
- RecordedBy: `EPHEMERAL_AGENT_2_GENERALIST`
- Date: `2026-08-03`
- Governing brief: `briefs/N2.md` @ `ff573b6eb1a493ab1f18a01446aa56d9ffd61ab787c0673421506b65d240f2f8`
- Sealed launch: `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/W6-DEL0206-POST-N0-PLANNING/children/N2/LAUNCH_BRIEF.md` @ `44196cc49b216b9e43605728b04717c26e7f439ad4c3e9836b22a1f64a2b8d79`
- Accepted dependency: `basis/N0_R2_RETURN.md` @ `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522`; machine report `basis/BASIS_REPORT_R2.json` @ `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8`
- Accepted Scope of Work: `ScopeOfWork.md` @ `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`

## Classification rule

Only an accepted implementation or migration obligation for the exact Root
change permits `AFFECTED`. Prospect naming, source proximity, shared route or
transport, and coordination status do not create work, a closure veto, or a
client-evidence dependency. The only allowed classifications are `AFFECTED`,
`NOT_AFFECTED`, `PROSPECTIVE_ONLY`, and `UNRESOLVED`.

## Census

| Client | Classification | Accepted obligation source | Exact affected operation | Retained functions | Conformance/migration artifact | Result | Owning gate |
|---|---|---|---|---|---|---|---|
| Root CLI (including the Root generic-client path it invokes) | `AFFECTED` | Accepted `ScopeOfWork.md` @ `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`, `REQ-004`, `REQ-005`, `REQ-009`, and `REQ-048` | Before each consequential runtime-dependent CLI operation, obtain and exactly compare the daemon compatibility identity; stop on mismatch or any failed precondition without alternate transport, daemon, model, downgrade, or automatic replay; preserve exact machine-readable behavior. | File-native and individually accepted local-only CLI commands remain available only as separately named functions, never as an alternate agent runtime. | Not yet produced; the required Root client/CLI conformance matrix remains a later output. | Accepted exact Root-client obligation exists; client evidence remains pending and no implementation is authorized here. | N4 may integrate a semantic candidate; a separate Root CLI implementation/conformance gate must accept exact behavior and evidence before release. |
| Chirality App | `AFFECTED` | Accepted App decomposition `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` @ `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`, Gate posture and `SOW-037`, `OI-007`, `DEC-021`; scope-change closure `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/RUN_SUMMARY.md` @ `bce5b987049d08476988fe705bfcaeb1d723f68cc1cd11928c726fbb059c7621` | Conform App client session, proxy, compatibility, error/presentation, interruption, and runtime-evidence surfaces to the Root-owned generic contract while preserving the ruled contract re-export and preventing silent fallback or replay. | Browser/API/UI/packaging, packaged-daemon mode, project authority, project-specific deterministic acts, human gates, and client presentation/evidence remain App-owned. | No conformance or migration artifact is accepted in the allowed evidence set; SCA-APP-005 closed scope change only and expressly preserved later implementation and conformance work. | Accepted exact App client/conformance obligations exist; evidence and implementation remain separately gated. | A separately accepted App-owned implementation/conformance tranche, followed by its acceptance evidence and the Root accountable-human release gate. |
| PEC v2 | `UNRESOLVED` | Live `projects/pec/AGENTS.md` @ `5882161b66fb667f2a451ba8e5f9dc379afdf3fb1a4b3fe34dd8bd42ef5aefde`; accepted `projects/pec/execution/_Decomposition/Deliverables.csv` @ `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`, `DEL-07-02` and `DEL-07-05`; accepted `projects/pec/execution/_Decomposition/ScopeLedger.csv` @ `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`, `SOW-035` and `SOW-087`; `D-T0-23` @ `0629e16da62a68ce9648432dfa7293a426fe7278cea1efa43da2a6a00a624ae5` | The v2 decomposition names a daemon SSE subscriber and a shared-runtime client seam, but the allowed sources do not bind either operation to the exact compatibility/degraded-mode Root change or show the separately owner-ruled PEC implementation packet required by the live PEC fence. | PEC file-native coordination truth, deterministic human-only acts, project acceptance evidence, graceful absence, and the no-dual-loop boundary remain independent; runtime session authority remains Root-owned. | None. PEC implementation does not exist, and no exact PEC conformance/migration artifact or owner-ruled implementation packet is present in the allowed source set. | Evidence proves a future client seam but not the exact accepted obligation threshold required for this Root change; preserve unresolved and create no work or closure veto. | A PEC-owned, owner-ruled `D-PEC` packet must name the exact affected v2 operation and bind it to exact accepted Root contract bytes, or explicitly rule no effect. |
| Chirality Piping | `NOT_AFFECTED` | Accepted `ScopeOfWork.md` @ `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`, `TBD-013` / `OD6-OPEN-013` | None. The accepted basis says Piping remains metadata-only and non-client unless new evidence proves actual Root runtime consumption. No such evidence appears in the declared consumer-census sources. | Existing Piping metadata and coordination functions remain outside this client census. | Not applicable. | No accepted implementation or migration obligation for this Root change. | A later Piping-owned accepted obligation instrument would be required to change this classification. |
| Tier-0 domain coordination | `NOT_AFFECTED` | `D-T0-07` @ `5fb96fdcf2bb0db660bff84d80abb57ecadfb420f57cfda61cd5782972204851`, `D-T0-09` @ `544d7517d97b6a5e446fc784b10671ad7d5a0fc70b6d9ae4194c7adbaf6dec7a`, and `D-T0-23` @ `0629e16da62a68ce9648432dfa7293a426fe7278cea1efa43da2a6a00a624ae5` | None. These accepted decisions govern cross-project version relationships and shared-runtime convergence; they do not make Tier-0 a runtime client or transfer generic semantic ownership. | Tier-0 relationship, version-reference, and cross-loop coordination acts remain independent authority functions. | Not applicable. | Accepted coordination effects exist, but no Tier-0 client implementation or migration obligation exists for the exact Root change. | Any later Tier-0 relationship act may coordinate exact identities but cannot by itself create client work or amend Root semantics. |

No additional consumer is evidenced by the eight declared item-5 sources. A
producer, authority surface, route label, transport endpoint, package location,
or prospective integration is not added as a client.

## Source coverage

All eight Scope-of-Work consumer-census sources were read and hash-checked:

| SourceRef | SHA-256 | Census use |
|---|---|---|
| `_DomainEngines/_DECISIONS/D-T0-07_contract_versioning.md` | `5fb96fdcf2bb0db660bff84d80abb57ecadfb420f57cfda61cd5782972204851` | Tier-0 version-relationship boundary |
| `_DomainEngines/_DECISIONS/D-T0-09_flow_a_contract_version_value.md` | `544d7517d97b6a5e446fc784b10671ad7d5a0fc70b6d9ae4194c7adbaf6dec7a` | Tier-0 concrete Flow-A coordination value |
| `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md` | `0629e16da62a68ce9648432dfa7293a426fe7278cea1efa43da2a6a00a624ae5` | Shared-runtime ownership and PEC migration direction |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/RUN_SUMMARY.md` | `bce5b987049d08476988fe705bfcaeb1d723f68cc1cd11928c726fbb059c7621` | App affected-client ownership partition and scope-change-only closure |
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | Accepted App client implementation/conformance obligations |
| `projects/pec/AGENTS.md` | `5882161b66fb667f2a451ba8e5f9dc379afdf3fb1a4b3fe34dd8bd42ef5aefde` | Live PEC v2 product, fence, and shared-runtime posture |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` | PEC v2 daemon-subscriber and client-seam deliverables |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` | PEC v2 exact IN rows and Root-runtime write exclusion |

## Finding

- `N2-F-001` — PEC v2 has accepted future daemon-subscriber and client-seam
  scope, but the declared sources do not supply the exact owner-gated binding
  that would make either operation affected by this exact Root semantic change.
  The row remains `UNRESOLVED`; N4 must preserve that status and must not infer
  a PEC obligation, dependency, or closure veto.

## Boundary

This census is planning evidence only. It performs no semantic selection,
implementation, client or project write, profile/check adoption, lifecycle
transition, release, reliance, SCA/decomposition/PRD act, Task Management act,
Git act, notice, or foreign write.
