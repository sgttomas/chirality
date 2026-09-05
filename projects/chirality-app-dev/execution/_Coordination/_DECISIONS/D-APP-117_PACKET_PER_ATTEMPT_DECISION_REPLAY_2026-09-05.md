# D-APP-117 — Per-attempt subagent decision replay

**Status:** PROPOSAL — AWAITING_RULING
**Prepared:** 2026-09-05 by WORKING_ITEMS, instance `pkg08_packet`, run `APP_LOOP_SHELL_2026-09-05`.
**Authority to prepare:** D-APP-103 B4. Implementation requires a later owner ruling. No option below has been selected by the owner.

## 1. Decision and accepted basis

Choose whether to add bounded, explicit decision evidence for each managed delegation attempt. The recommended first implementation is the DEL-08-04 decision-capture and handoff seam; storage and consumer work retain their existing owners and require separately scoped activation.

D-APP-103 authorizes this packet, including brief hash, scope, decision points, outcome, attribution, AgentRuns/canonical-session relationship, Desktop/CLI rendering, checks, and exact implementation scope. D-APP-53 §3 Option C identifies the deferred item; its original Option-A ruling did not authorize it. D-APP-60 and D-APP-64 govern this proposal's truthful attribution and independent verification, not its adoption.

Source basis is commit `044a009e215e08b69c9e0887da424938a34aafcb`. Exact consulted bytes are recorded in `execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg08_packet/SOURCE_IDENTITIES.sha256`. Accepted upstream truth is the applied `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` and DEL-08-04 `ScopeOfWork.md` at that basis. Dependency evidence is the accepted pointer to `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`; it is derivative evidence, not decomposition authority.

Current facts:

- `frontend/src/lib/harness/managed-delegation.ts` renders and hashes the launch brief, records instruction hash, parent session, run/instance IDs, scope and tools in an AgentRuns instance, and replaces `STATUS.json` atomically through lifecycle states. A child session ID appears after the launcher returns. This does not preserve a complete per-attempt sequence of decision points, including refusals before child launch.
- `subagent-governance.ts` returns gate/allow/reason metadata and logs decisions. Logs and mutable status are not an immutable decision-attempt artifact.
- `recorded-agent-hierarchy.ts` groups exact recorded `parentSessionId` values, labels unavailable parents/conflicting IDs, and leaves missing roles absent. `selected-session-replay.ts` projects canonical session/event replay with explicit conflict, stale, malformed and bounded disclosures. Neither is a source for reconstructing unrecorded decisions.
- `docs/SPEC.md` §17.5 permits evidence-conditional parentage presentation. The applied decomposition assigns DEL-08-04 admission/delegation semantics, DEL-08-05 child evidence persistence, DEL-05-04 replay/projection semantics, and DEL-02-02 presentation. DEL-08-04 SOW CLM-011/032 explicitly preserves that handoff ownership.
- Root owns `runtime/packages/contracts` and `runtime/packages/cli`; the existing CLI `session replay` invokes canonical replay. The App must not create an independent runtime or alter canonical session truth to implement this feature.

The packet preparation item has no Depends line naming the still-TBD permission-overlay prerequisite DEP-08-04-004. DEP-08-04-002/003 are SATISFIED. DEP-08-04-006 is a handover, and 009/010/013/014 are interfaces; they do not bar this planning node under LOOP_INIT §5 Step 1. The explicit Root fixture gate on DEL-08-04-V3-01 and per-session-policy gate on V3-02 remain separate and unchanged.

## 2. Options (non-binding recommendation)

| Option | Proposed outcome and scope | Tradeoff |
|---|---|---|
| **A — Explicit attempt evidence beside AgentRuns (recommended)** | Adopt the candidate semantics in §§3–5; authorize only the bounded DEL-08-04 capture/handoff slice in §6. Preserve DEL-08-05 persistence ownership and separately activate storage/projection/Desktop work; route CLI needs to Root. | Makes refused and retried attempts inspectable without replacing canonical sessions. Full product rendering depends on later consumer activations and an accepted persistence handoff. |
| **B — Defer** | Keep canonical hierarchy/session replay and existing launch/status/return evidence; retain an explicitly gated residual. | No implementation cost; absence of per-attempt decision evidence remains visible. Do not synthesize it from conversation or historical logs. |
| **C — Coordinated canonical event extension** | Request a separate Root/App design and authority process to add attempt identifiers/decision events to daemon-owned contracts before App consumption. | Potentially one canonical event transport for all clients, but crosses Root ownership and may change session/event truth. This packet cannot authorize those writes, migrations or acceptance acts. |

A best fits K-ENGINE-6's governance/audit layer and the existing checkout-evidence boundary. B leaves the authorized question unresolved; C adds a materially larger contract transaction than the requested bounded artifact. This is an agent recommendation, not an owner case selection. The implementation fork fast-rejects under D-APP-64 §5.1 (new scope/acceptance and possible project-truth changes); the proposal remains held for ruling.

## 3. Candidate record semantics for Option A

All schema names/paths in §§3–6 are **proposed**, not current product contracts. An attempt is one invocation of managed-delegation admission for one intended child, including refusal before a child session exists. Retry means a new attempt ID referencing the preceding attempt; transport redelivery with the same idempotency key is the same attempt. Approval resumption within the same sealed input is another recorded decision point; changed brief, authority basis, scope or policy makes a new attempt. This evidence never causes retry, approval or dispatch.

Proposed schema `chirality-decision-attempt/v1`:

| Field family | Exact proposed contents and provenance |
|---|---|
| Identity | `schema`, `attemptId` (opaque unique ID), `runId`, `planVersion`, `instanceId`, `retryOfAttemptId` (nullable), `idempotencyKey`, `recordedAt`. Run/instance references must identify the existing governed work graph; an unbound/invalid request cannot invent a valid run. |
| Basis | `acceptedBasis[]` as exact source path/commit/hash references; `briefRef`, `briefHash` (SHA-256 of exact UTF-8 sealed brief bytes); nullable `instructionRef`/`instructionHash`; policy version and configuration digest. Missing source bytes are disclosed as unavailable; a digest alone does not prove recomputability or authority. |
| Scope | Requested and admitted context, cwd, tools and write-target arrays, stored as checkout-relative contained paths or symbolic scope values; `contextSealed`, dependency/predecessor references and gate evidence. Keep requested/admitted separate; a refused request has no admitted capability. |
| Linkage | `delegationClass`; `parentSessionId`; nullable `childSessionId`; optional canonical event/turn IDs only when the accepted owner returns them; `parentInstanceId` if recorded. A refusal before launch has `childSessionId: null` with `NOT_CREATED`, not a fabricated session. |
| Decision points | Ordered `decisions[]`, each with `decisionId`, `sequence`, `kind` (admission/policy/scope/approval/launch/return-validation), `outcome` (ALLOW/DENY/ASK/ERROR/UNAVAILABLE), stable `reasonCode`, bounded non-secret summary, source reference and source kind (policy/hook/governance/SDK-callback/human-evidence/agent-authored), input digest and recorded time. Unevaluated later gates remain unevaluated; no invented ALLOW rows. |
| Outcome | `attemptState` (PENDING/RUNNING/COMPLETED/FAILED/BLOCKED/INTERRUPTED/UNKNOWN), terminal reason, return/output references and hashes where available. Keep admission outcome separate from execution outcome and from deliverable acceptance. Terminal completion is not acceptance. |
| Attribution | Actual adapter/provider/model when observed, explicit unavailable values otherwise; role-entry state and its source; approval reference and recorded actor evidence; authored-by instance; role-enforcement evidence. Native origin never assigns Agent 0/1/2. Preserve `role not mechanically enforced` and `instruction-asserted` when applicable. Requested model/configuration is not actual execution attribution. |
| Integrity/currency | Snapshot sequence, preceding snapshot hash, source inventory (relative path, byte count, SHA-256), completeness flags and gaps; CURRENT/STALE/CONFLICTING/UNKNOWN evaluated from referenced evidence, with diagnostics. No hash chain claims tamper-proof storage or authenticates human approval. |

Decision points are explicit observable policy outcomes or deliberately authored concise decision summaries with references. They are not hidden model reasoning, inferred thought processes, or transcript-derived reconstructions. Do not copy credentials, raw environment values, sensitive prompt fragments, or unrestricted error text. If the exact sealed brief cannot be preserved safely, retain its authorized reference/digest and mark recomputation unavailable; a redacted copy gets its own digest and never masquerades as the exact brief.

## 4. Storage, canonical relationships and recovery

Proposed evidence home: `execution/_Coordination/AgentRuns/<runId>/instances/<instanceId>/attempts/<attemptId>/snapshots/<sequence>/DECISION_REPLAY.json`, with an adjacent sorted `MANIFEST.sha256` and only approved non-secret source material. Existing instance `LAUNCH_BRIEF.md`, `STATUS.json`, `RETURN.md`, and work graph remain owned by their existing writer. No new standing global index, queue, register or latest pointer is introduced.

DEL-08-05 would publish snapshots as exclusive immutable files, using its accepted containment/atomic-publication mechanism. A pending attempt may have a snapshot with partial decisions; terminal knowledge produces a new snapshot, never a rewritten old verdict. Readers select only complete validated snapshots and report gaps, not success from a partially written directory. Deterministic same-attempt redelivery must not create contradictory duplicate snapshots; a different payload for the same idempotency identity is a conflict. Recording failure before dispatch fails closed for that proposed instrumented path; failure after launch records an evidence gap without pretending the launch did not occur or automatically repeating it. Crash recovery consumes existing session identity and evidence; no second runtime or inferred child creation.

The checkout artifact is derivative governance evidence citing accepted upstream inputs. The daemon remains owner of operational canonical sessions/events. Equality of explicit project/run/instance/session identifiers joins the records; proximity, persona, timestamps and transcript wording never join them. An attempt may have no child session, or a recorded one; several attempts may reference a reused canonical session only when the owning runtime explicitly reports that linkage. Replay never creates/updates sessions, repairs parentage or rewrites transcripts. Missing/offline daemon evidence allows a labelled evidence-only view; mismatching canonical identity is CONFLICTING and disables any claimed verified join.

A request rejected before a valid run/instance and safe path exists is reported through the existing error boundary. Its absence from AgentRuns is a declared coverage limit, not grounds to write into an untrusted path. Option A does not promise capture of all malformed inbound requests.

## 5. Desktop, CLI and proving checks

Desktop proposal: from the selected recorded child/session in the right-panel Who is working / read-only Session view, show an optional **Decision attempts** section. Each row gives attempt, admission outcome, execution state and evidence currency. Selecting a row shows its sealed-brief reference/hash, requested/admitted scope, ordered recorded decisions, approval/attribution evidence, output links and gaps. Show unlaunched refusals only within an explicitly selected run/instance evidence context supplied by an accepted reader; do not invent global AgentRun discovery. Keep canonical transcript replay separate and preserve the primary dialogue. No edit, retry, approve, dispatch or send-message button is introduced.

CLI proposal for Root consideration: a read-only `session replay --decisions` presentation using the same accepted evidence projection, with `--json` exposing exact structured values and diagnostics. It includes attempts linked by exact session ID; unlaunched refusals require an explicit run/instance selector that Root must separately approve. Ordinary `session replay` remains canonical replay. The spelling is candidate UX, not an implemented or authorized Root command. The App does not fork CLI or directly read daemon user-data files.

Future proving matrix (acceptance criteria proposed for the later ruling; **not executed by packet preparation**):

| Check | Required evidence/result |
|---|---|
| Capture and semantics | Fixtures for allow, deny, ask, resumed approval, missing approval, invalid child role, changed brief/scope, launch failure and return-validation failure. Compare decision payload to the actual evaluated inputs; deny overrides allow; later unevaluated gates are not marked passed. |
| Identity and retry | Two attempts for a genuine retry; same attempt for identical redelivery; conflicting duplicate rejected; refusal has null child ID; matching versus mismatching canonical IDs; no linkage guessed from timestamps/persona. |
| Integrity and recovery | Independently recompute exact brief/instruction/source and snapshot hashes; malformed/unknown schema and truncated publication rejected; missing sequence/time/source disclosed; restart never overwrites old evidence or repeats execution; immutable snapshots survive current STATUS replacement. |
| Containment and confidentiality | Traversal, symlink, wrong project/instance and active-sibling overlap failures; attempts do not widen scope. Secret-bearing fixtures prove summaries and manifests omit forbidden bytes; redacted and exact source hashes remain distinct. |
| Projection and ownership | Same admitted fixture yields equivalent Desktop/CLI fields and disclosures when both consumers are authorized. Missing/null/native-role and G-ROLE labels remain truthful; recorded completion never advances deliverable state; no write/dispatch call from replay; offline evidence and stale/conflicting joins visibly differ. |
| Regression and evidence | Registered typecheck/Vitest/build/premerge and D-APP-36 render bar for affected UI, A1 re-stage declaration for frontend changes, fresh read-only review of 100% of each frozen product diff, APP-HOLD-1 preflights, receipt validation, self-check, practitioner pytest and diff check. Preserve fixture/evaluator bytes, command/argv/cwd/env/version/exit status, canonical output, machine-readable results and sorted recomputable manifests per LOOP_INIT §9. |

## 6. Exact proposed implementation boundary and on-ruling mechanism

**Option A first slice: DEL-08-04 only.** Allow `frontend/src/lib/harness/subagent-governance.ts` and `managed-delegation.ts` to expose bounded decision capture/handoff without weakening admission; new App-local `frontend/src/lib/harness/decision-attempt.ts` for the candidate DTO/validation; focused tests under `frontend/src/__tests__/lib/`; and this deliverable's `_run_records/**`, `_STATUS.md`, `MEMORY.md`. An injected evidence sink may be tested with fixtures, but production persistence is not silently assigned to DEL-08-04. No Root-owned contract, CLI, daemon, session schema, instruction package, tools, provider or lifecycle surface is in this slice. Preserve sibling-overlap fail-close. Root fixture and class-aware gates remain applicable to any class-aware integration; this packet does not unlock V3-01 or V3-02.

Before engineering, the owner ruling must accept/amend the candidate schema/criteria and this exact slice, with any required deliverable-contract amendment handled by its owning instrument. The manager then records one CANDIDATE brief and reruns live dependency/preflight checks. If authoring reveals a needed scope expansion, stop and return the delta for ruling.

**Separate consumer activations:** DEL-08-05 owns persistence/publication/recovery; DEL-05-04 owns projection/replay semantics; DEL-02-02 owns Desktop composition. This proposal identifies their interfaces without changing their Remaining items or authorizing their work. No production feature can be declared complete until these required consumer packages are accepted and integrated, or explicitly deferred by the owner with the resulting limitation stated.

**Root follow-on:** through the established Root coordination route, request assessment of the CLI presentation and any canonical linkage/event fields absent from the accepted API. Root retains its own approval, contracts, implementation and return. App consumes only an accepted routed return; no Root path/target authority is invented. Native attempt capture likewise waits for accepted Root-origin evidence instead of applying the managed writer to native descendants.

On a later owner ruling, transcribe the actual act in a new ruling record and update the decision register and deliverable Remaining through the owning loop. Do not turn a recommendation, PR merge alone, record existence or test PASS into an implementation ruling. Option B records explicit deferral; Option C requires a separate coordinated design/authority transaction before implementation.

## 7. Packet handoff

This packet is a derivative proposal, not accepted decomposition truth, runtime evidence or a project-truth migration. Packet-preparation obligation is prepared; implementation is **OPEN / AWAITING_RULING D-APP-117**. No lifecycle or Checking Approval SHA change is proposed. D-APP-103 remains an immutable ruled authorization to prepare.

Manager evidence: `execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg08_packet/`. Fresh governed-diff review and global closeout checks are performed by the supervising run; this packet claims no unreturned verdict. Rerun review after any packet edit; refresh source/ownership analysis if cited contracts or canonical linkage change before ruling or implementation. Remaining blockers are the owner ruling, subsequently activated persistence/projection/Desktop work, and separately accepted Root work for CLI/native coverage.
