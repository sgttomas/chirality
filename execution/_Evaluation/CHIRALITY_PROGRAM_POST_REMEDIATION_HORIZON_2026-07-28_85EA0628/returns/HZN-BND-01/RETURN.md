# HZN-BND-01 — Static Program Boundary Concordance

## Verdict

The accepted architecture is coherent at the authority, decomposition, and visible static-composition layers:

- Root owns generic runtime semantics and stewardship.
- App is a current Root-runtime client with accepted client/conformance obligations.
- PEC has accepted prospective v2 client capabilities, but no v2 implementation or activated runtime-client work.
- Piping is affirmatively a non-client; its former App-era mechanism is historical, current reliance is retired, and the replacement remains unresolved under an active reliance hold.

No program-wide architecture blocker was found. Static evidence does not establish runtime use, conformance, security, release fitness, or affected-client status for any exact operation.

Basis: `85ea0628fa4e57dd6aae53b06139b2b8734a9612`. All repository evidence below was read from that Git object.

## Consumer classification

| Surface | Classification | Finding |
|---|---|---|
| App | `CURRENT_ACCEPTED_OBLIGATION` | App’s accepted decomposition defines PKG-03 through PKG-06 as client, compatibility, presentation, and conformance work while excluding generic runtime ownership (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:267`, `:303`, `:312`, `:316`, `:322`, `:332`, `:538`). Static dependencies and Electron composition support that reading but do not prove runtime use (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-app-dev/frontend/package.json:39`, `85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-app-dev/frontend/electron/main.ts:1`, `:75`, `:525`, `:575`). |
| PEC v2 | `CURRENT_ACCEPTED_OBLIGATION` | PEC v2.2 permits explicitly enabled consumers and defines a P3 shared-runtime client seam, while requiring separate receiving-consumer authority (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/docs/PRD.md:42`, `:236`, `:288`, `:301`; `85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:100`, `:111`, `:372`, `:470`). The specific deliverable is `OPEN`, not implemented or activated (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_STATUS.md:3`). |
| PEC v0.4 source | `FROZEN_REFERENCE` | The accepted status explicitly labels the old `core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`, and `fixtures/` tree read/cite-only (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/docs/STATUS.md:25`, `:30`). |
| Piping current | `NONE` | D-58 and DEC-091 expressly keep Piping outside both Root-runtime and App-harness client sets and create no client obligation (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-piping/execution/_Coordination/_DECISIONS/D-58_current_mechanism_retirement.md:48`, `:55`; `85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:677`). |
| Piping App-era mechanism | `CANDIDATE_OR_HISTORICAL` | D-30/D-31 remain historical, while current reliance on their synchronized mechanism is retired (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-piping/execution/_Coordination/_DECISIONS/D-58_EFFECTIVE_STATE_CLOSEOUT_2026-07-27.md:46`, `:49`). |

## Load-bearing boundary seams

| Seam | Static concordance |
|---|---|
| Contracts and authority | Root O-11 requires a Root-owned carrier and write locus for consequential generic runtime semantics; clients do not acquire ownership through implementation (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md:45`, `:48`, `:51`). App’s decomposition now states client conformance rather than semantic ownership. |
| Credentials and packaging | The daemon exclusively owns credentials; Electron supplies daemon mode so the encrypted `safeStorage` boundary remains single-owner (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:docs/PRD_ROOT.md:428`, `:429`). App DEL-04-05 preserves UI and packaged-daemon participation without creating a second owner (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:316`). |
| Sessions, locks, interruption | Root/daemon ownership is consistent across Root doctrine and App client deliverables (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:runtime/README.md:7`; App decomposition `:304`, `:306`, `:322`). PEC’s accepted presence requirements consume harness-reported information while leaving session lifecycle daemon-owned (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/docs/PRD.md:288`). |
| Adapters | Generic safe engine adapters belong to Root; App owns project inputs, UI mapping, packaging participation, and conformance; PEC retains its own future bridge acts and requires separate authority for Root writes; Piping has no current adapter/client obligation (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:runtime/README.md:27`, App decomposition `:312`, `:314`, PEC PRD `:301`, Piping D-58 `:55`). |
| Fallback | Root forbids hidden substitution through DEL-02-06’s accepted contract (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md:590`). PEC expressly preserves file-native operation without PEC (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/docs/PRD.md:42`). Piping’s replacement automation mechanism remains unresolved and current reliance remains held (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_REMEDIATION_TERMINAL_2026-07-28_058B294C/HOLD_CLOSURE_MATRIX.csv:4`). |
| Public export | Root describes generic runtime/CLI/contracts/safe adapters as eligible, excluding credentials, machine state, and private adapters (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:docs/PRD_ROOT.md:436`). The staged public README expresses the same boundary and excludes the desktop source and private state (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:exports/chirality-app/PUBLIC_README.md:57`, `:68`, `:100`). This is staging evidence, not a claim about any external repository. |

## Findings

### HZN-BND-F01 — `NECESSARY_BEFORE_NEXT_WORK`

The horizon scan must not substitute for DEL-02-06’s activation-time affected-client census. The accepted contract allows `AFFECTED` only when an exact operation has an accepted obligation source; other cases must remain `NOT_AFFECTED`, `PROSPECTIVE_ONLY`, or `UNRESOLVED` (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md:503`, `:507`, `:543`, `:563`). DEL-02-06 remains `INITIALIZED`, with its first production activation unauthorized (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_STATUS.md:3`, `:11`).

Smallest owner: DEL-02-06/WORKING_ITEMS activation gate. No new instrument is needed for this scan.

### HZN-BND-F02 — `NECESSARY_BEFORE_NEXT_WORK`

Before App runtime work relies on the PRD body as its ownership statement, its older runtime-owner wording must be read through or reconciled with §17 and the accepted decomposition. The body still speaks of “Chirality-owned” contracts and product-owned runtime/event/session semantics (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/chirality-app-dev/docs/PRD.md:52`, `:64`, `:103`), while §17 expressly makes the provider-neutral runtime Root-owned (`:1692`, `:1694`) and the current decomposition consistently assigns App client/conformance work. This does not overturn the accepted boundary, but it is unsafe as a standalone basis for a future App runtime tranche.

Smallest owner: App product authority before the affected App work relies on those clauses. It is not a blocker to this assessment or to Root’s read-only census.

### HZN-BND-F03 — `NECESSARY_BEFORE_NEXT_WORK`

The eventual comparison-HTML revision should preserve the distinctions above:

- App is a current accepted client, but static composition is not runtime proof.
- PEC has an accepted prospective P3 client seam, not merely an unspecified future “gate,” while v2 implementation remains absent.
- Piping is positively non-client and its active control is a professional-reliance hold, not a runtime-client hold.
- Open work-surface, profile, and resource-governance questions are not missing requirements.

The local HTML already recognizes most of this but compresses PEC to “gated until its own gate” and should be made lifecycle-specific (`sha256:5b442280fdf43f850a2b70b0865f20678c5e5da056179bebc95d89be0d1c52c8:/Users/ryan/dev/chirality/plans/chirality_program_architecture_tandem_comparison_2026-07-28.html:742`). Its App-body qualification is accurate (`same-sha:path:787`). Publication should wait for the D-8 lane and owner disposition as planned.

### HZN-BND-F04 — `BENEFICIAL_LATER`

PEC DEL-07-05’s `_CONTEXT.md` provenance still calls decomposition revision 1.2 the `current_basis`, while live accepted decomposition truth is revision 1.3 (`85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md:29`; `85ea0628fa4e57dd6aae53b06139b2b8734a9612:projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md:5`). The file declares itself a restatement, so this is descriptive pointer hygiene, not an authority or topology defect.

### HZN-BND-F05 — `DELIBERATELY_OPEN`

Reusable work surfaces, application profiles, and optional resource governance remain intentionally unminted. No accepted product authority was found that makes any of them mandatory or assigns their final home. The comparison HTML correctly treats them as open rather than filling the gap through interpretation (`sha256:5b442280fdf43f850a2b70b0865f20678c5e5da056179bebc95d89be0d1c52c8:/Users/ryan/dev/chirality/plans/chirality_program_architecture_tandem_comparison_2026-07-28.html:769`, `:1137`, `:1143`, `:1153`).

### HZN-BND-F06 — `OUTSIDE_PROGRAM_OBJECTIVE`

Implementation fitness, UI/API parity, security effectiveness, release readiness, live daemon behavior, and external public-repository currency were not evaluated. They require their own owning instruments and evidence.

### HZN-BND-F07 — `UNKNOWN`

The static corpus does not establish:

- whether App currently exercises the shared daemon successfully;
- whether any PEC v2 operation currently consumes the runtime;
- whether Piping has any unrecorded runtime interaction;
- whether the staged public export matches a live remote;
- exact client conformance for a future Root operation.

No runtime-behavior claim should be drawn from imports, dependencies, filenames, or accepted prospective scope.

## Handoff

No accepted ruling is invalidated, no retroactive cure is claimed, and no named next work is globally blocked. A fresh adversarial child is unnecessary. The manager can close this lane with deterministic backcheck, carry F01–F03 into the compact assessment and eventual HTML revision, route F02 only when App runtime work is next, and leave F05 open.
