# D-APP-116 — Full tool-result audit policy

**Status:** PROPOSAL / AWAITING_RULING
**Prepared:** 2026-09-05 by WORKING_ITEMS, instance `pkg05_packet`, run `APP_LOOP_SHELL_2026-09-05`.
**Preparation authority:** D-APP-102 B3. **Owner case selection:** NONE.

## Decision requested

Choose A or B below. The recommendation is **A: route a bounded full policy to the Root runtime owner, then implement App consumption and conformance only after the accepted Root contract is available**. This packet does not implement or adopt that policy. D-APP-42's accepted SHA-256/session-lifetime behavior remains the baseline until the relevant later rulings take effect.

## Accepted basis and observed boundary

All paths below are relative to `WORKING_ROOT` unless prefixed `{REPO_ROOT}`. Source byte identities are frozen in `execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg05_packet/INPUT_IDENTITIES.json` at base `044a009e215e08b69c9e0887da424938a34aafcb`.

- `execution/_Coordination/_DECISIONS/D-APP-102_RULING_TOOL_RESULT_AUDIT_PACKET_2026-08-17.md` authorizes this one planning node, six named topics, and at most three options; implementation requires a later ruling.
- `D-APP-42_RULING_2026-06-21.md` beside it ratifies Option A: checksum of exact stored bytes after redaction/truncation, existing metadata and session-lifetime retention. Full Option C was deferred as an enhancement, not an open correctness defect. `D-APP-53_RULING_2026-07-10.md` selected dependency reconciliation only; its packet §3 Option C preserved separate gates for this hardening.
- `AGENTS.md` Shared Runtime Boundary, `docs/PRD.md` architectural ownership paragraphs, and `D-APP-73_RULING_2026-07-22.md` assign generic persistence/session ownership to the Root daemon. D-APP-73 requires non-destructive legacy migration and preserves checkout governance truth.
- Live DEL-05-05 `_CONTEXT.md` excludes generic session/event/tool-result persistence and daemon operational-state ownership. Its current `ScopeOfWork.md` preserves older App writer claims. Those historical loci cannot override the current decomposition/context and Root boundary. This proposal does not repin or rewrite the stable contract. Any subsequent scope/contract alignment must use the owning instrument before implementation; no wider authority is inferred from the older paths.
- `frontend/src/lib/harness/tool-result-artifacts.ts` still implements the legacy redacted/truncated tool artifact writer with checksum and `retentionPolicy: 'session-lifetime'`. `tool-evidence.ts` classifies descriptor budgets. These are evidence of existing compatibility behavior, not permission to create another operational store.
- `{REPO_ROOT}/runtime/packages/core/src/session-store.ts` owns central sessions: `delete` removes the central session directory and writes a separate deletion marker; `migrateLegacy` imports the session record and events without copying tool artifact payloads in that method. No artifact inventory completeness or independent cleanup service is established by these observations. Historical links therefore need explicit migration provenance, not an assumption that payloads migrated with events.
- Accepted upstream decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at the recorded Git base; scope snapshot `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/` remains `OPEN_PENDING_DERIVATIVE_CLOSURE`. Dependency evidence is `execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/`: closure PASS with carried warnings, including DEL-05-05 legacy enum non-conformance. Local prerequisite rows are SATISFIED; this packet changes none of them.

## Options

| Option | Policy and implementation sequence | Tradeoff |
|---|---|---|
| **A — explicit cleanup, Root-owned (recommended)** | Adopt the proposed requirements below as the App's requested contract; route generic implementation to Root for its own ruling/activation. Seat a gated DEL-05-05 App consumption/conformance slice after the accepted contract and owning App contract alignment. | Supplies the full six-topic policy without a TTL/quota scheduler; requires coordinated Root work and explicit owner decisions before destructive capability exists. |
| **B — retain D-APP-42 and defer full policy** | Record the full policy as deferred; keep session-lifetime metadata and existing deletion behavior. Add no manifest, independent cleanup, migration sweep, or new runtime/App implementation scope. | Lowest change cost; the full audit enhancement remains deliberately unimplemented. This is not rejection of the already closed checksum/budget work. |

No TTL, quota eviction, background purge, release-retention guarantee, legal hold system, or new tool exposure is included in A. Such a later policy would need its own decision with concrete retention values and consequences.

## A: proposed contract, subject to later owner ruling

### Per-session manifest

Root would own a versioned operational manifest (proposed logical name `artifacts/manifest.json`) for daemon tool-result artifacts. It is an index of operational payload availability and cleanup history, not a project-authority ledger. Original event JSONL remains unchanged; replay projects event provenance plus current artifact availability without rewriting historical `tool.completed` claims.

Proposed top-level fields: `schemaVersion`, `projectId`, `sessionId`, monotonic `revision`, `updatedAt`, `inventoryState` (`complete` or `partial`), and entries keyed by a stable `artifactId`. An entry carries:

- `artifactId`, `kind: tool-result`, optional `toolUseId`, `toolName` and `turnId` only where recorded;
- a relative storage locator paired with an explicit approved root kind (`daemon-session` or `legacy-session`), source event IDs, creation time if known, and discovery time separately;
- exact stored-byte `sha256`, `originalByteLength`, `artifactByteLength`, `redacted`, `truncated`, with unknown historic values absent and explained by `unknownFields`;
- `retentionClass: session-lifetime`, `cleanupEligibility` (`explicit-only`, `blocked-legacy`, or `blocked-unknown`), and `deletionState` (`present`, `delete-pending`, `deleted`, `delete-failed`, or `missing-unknown`);
- deletion operation ID, requested/completed timestamps when observed, safe reason code and attribution reference, plus `source` and `verificationState` identifying new writes versus legacy discovery and hash verification.

`ToolResultStore` record/API metadata carries the same artifact identity, retention class and current deletion state. Existing checksum, budget, redaction and path metadata remain available. A separately accepted checkout artifact is outside this manifest's cleanup jurisdiction: linkage may cite its accepted snapshot, but the daemon never deletes or infers acceptance of the governed copy. No raw content, credentials or arbitrary sensitive operator prose goes into metadata.

### Retention, deletion and independent cleanup

Under A, session lifetime remains the default retention class. The explicit cleanup exception requires a deliberate authorized request naming project, session, artifact IDs and expected manifest revision. Root must validate project identity, root containment and current state, and refuse traversal, symlinks, stale revision, active/incomplete writes, legacy/unknown entries and targets outside the owned artifact store. There is no implicit age or size trigger. This packet grants neither a cleanup command nor a tool capability.

The proposed Root operation persists `delete-pending` before payload unlink, then `deleted` only after successful removal; failures retain an actionable `delete-failed` state. A missing file discovered without a recorded successful deletion is `missing-unknown`, never a fabricated deletion. Retries use the same operation identity; crash recovery reconciles pending state without claiming success from a request alone. A daemon-serialized mutation and atomic revision publication prevent lost manifest updates under concurrent tool completions. Root's implementation brief must bind its precise journaling/recovery algorithm before coding.

Independent cleanup removes only the selected operational payloads. Session metadata, events and manifest tombstones remain readable; replay displays that bytes were removed while preserving original metadata/checksum as historical evidence. Deleting a session remains the existing separately authorized lifecycle operation; A adds no audit retention beyond session deletion. Erasure of every copy, secure wiping, and preservation of externally accepted evidence are not implied by operational unlink success.

### Migration posture

New artifacts receive the new record/manifest shape prospectively. Existing session/artifact bytes and event JSONL remain untouched. Root may inventory only registered legacy roots through a separately authorized migration implementation. Inventory records actual origin and measured hash/size; it never reconstructs an original timestamp, redaction assurance, or successful deletion from absence. Conflicting/malformed metadata yields `partial` inventory with diagnostics and cleanup blocked.

Legacy entries remain `blocked-legacy`; no bulk move, rewrite or delete occurs. A future explicit copy/adoption operation, if separately authorized by Root, must verify destination bytes against the source hash before making the owned copy eligible; the legacy source remains unchanged. Rerunning inventory is idempotent and reveals changed or missing bytes. No eager App-side crawler or parallel persistence layer is introduced. Rollback keeps original bytes and events readable, and readers lacking the new schema receive a disclosed unavailable/unsupported state instead of pretending the manifest is complete.

## Exact implementation boundary and proposed proving checks

These are future loci and checks, **not writes or test claims in this packet run**.

| Owner / carrier | Exact bounded locus | Proof required after authorization |
|---|---|---|
| Root owner; new or amended Root scope required | `{REPO_ROOT}/runtime/packages/core/src/session-store.ts`; proposed sibling `tool-result-store.ts`; `{REPO_ROOT}/runtime/packages/contracts/src/session.ts` and proposed `tool-result-artifact.ts`; `{REPO_ROOT}/runtime/packages/daemon/src/runtime-daemon.ts`; `{REPO_ROOT}/runtime/packages/client/src/client.ts`; `{REPO_ROOT}/runtime/packages/contracts/src/harness/transcript-replay.ts` | Root binds exact scope, accepted API/schema and registered checks under its own instruments. Prove manifest atomicity, interleaved writes, deletion failure/crash recovery/idempotency, containment, stale requests, cross-project denial, missing versus deleted, redaction, and non-destructive legacy inventory. App checks alone cannot prove these runtime semantics. |
| DEL-05-05 App client consumption | `frontend/src/lib/runtime-client/daemon-harness-port.ts`, `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts` | Consume the accepted Root metadata/API, disclose unavailable/unsupported states, preserve project attribution, and perform no local store mutation. No cleanup UI/control is seated by this proposed slice. |
| DEL-05-05 App conformance | `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`, `frontend/src/__tests__/lib/transcript-replay.test.ts`, `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`, `frontend/src/__tests__/lib/tool-evidence.test.ts`, `frontend/src/__tests__/lib/session-events.test.ts`; proposed `frontend/src/__tests__/integration/runtime-tool-result-audit.integration.test.ts` | New/legacy/unknown/deleted fixtures; unchanged thresholds/previews/naming; hash exact redacted stored bytes; malformed-tail/interleaved replay; live daemon cleanup/restart proof from Root-authorized fixture operations, with surviving session/events and unchanged accepted checkout artifact bytes. A fake port establishes client behavior only. |
| DEL-05-05 governed contract/evidence | Selected deliverable `ScopeOfWork.md` only after owning scope/contract alignment; `_STATUS.md`, `MEMORY.md`, `_run_records/**` | Bind the accepted requirement/acceptance mapping and Root contract identity before implementation; record conformance, limitations and handoff. Do not treat this proposal's test list as new accepted AC IDs. |

The legacy artifact writer is an inspection/regression locus only; A does not authorize extending it into App-owned operational persistence. The deprecated `frontend/packages/harness-contract` mirror is not edited independently of its governed pull contract. New presentation work on `frontend/src/components/shell/transcript-stream-view.tsx` belongs to its owning shell/replay carrier and needs a separately seated cross-package slice; it is excluded from DEL-05-05 implementation here. Subagent output storage and its thresholds remain DEL-08-05's separate scope.

`software-workflow.json` registers `frontend-typecheck` (`npm run typecheck`), `frontend-test` (`npm test`), `frontend-build` (`npm run build`), and `frontend-premerge` (`npm run harness:validate:premerge`) from `frontend`; run the product-source gates on the eventual App slice with fresh independent code review. Its always checks are `harness-self-check` and `app-hold-integrity`; governed evidence also requires `harness-pytest`, receipt validation and `git diff --check`. Host-only daemon/integration proof follows the exact-command escalation rule. Before any frontend tranche record the A1 re-stage consequence; any later UI slice also owes D-APP-36's render bar. Evidence must preserve non-secret inputs, commands/environment, outputs, fixture bytes, sorted hashes and rerun method under LOOP_INIT §9. These proposed tests have not been executed for A, because A is not implemented.

## Rationale and ruling mechanism

WORKING_ITEMS recommends A as agent judgment. Ontology: current `_CONTEXT.md`, PRD and D-APP-73 put operational records in Root and accepted artifacts in the checkout. Epistemology: exact stored-byte hashes and explicit unknown/deleted distinctions preserve D-APP-42's evidence strength without pretending an inventory proves custody. Praxeology: an explicit request, revision check and recoverable state transition are bounded to selected payloads and preserve non-destructive migration. Axiology: useful replay diagnostics improve auditability while avoiding an unsolicited automatic destruction policy. B is reasonable if this coordination cost is not presently worthwhile, but does not provide the full enhancement D-APP-102 asked to bring to decision.

D-APP-60 class-test attempted failure: misread packet authorization or old App writer paths as permission to create an independent runtime cleanup service. Rejected: that would cross D-APP-64 §5.1 scope, normative, destructive and ownership boundaries. Recommendation preparation passes; adoption and implementation remain owner-class.

`OwnerStandingApproval: D-APP-64 §3`; `AgentJudgment: SELECT_AND_ADVANCE` applies only to preparing this bounded recommended packet; `SelectedOutcome: prepare A recommendation with B alternative`; `JudgedBy: WORKING_ITEMS / pkg05_packet`; `OwnerCaseSelection: NONE`; `RejectedAlternatives: B for immediate recommendation, because it leaves the full enhancement deferred`; `RationaleArtifact: this packet`; `IndependentVerifier: pending parent-arranged governed-diff review`; `EffectStatus: HELD`; `PreservedGates: D-APP-102 later ruling, Root ownership, D-APP-60/64 nondelegable classes, F-APP-1..5`.

After a later observable owner ruling: record its exact choice and riders in a new ruling record. A requires routing a non-authoritative coordination request through HELP_HUMAN to the Root owner; that loop adopts/amends/declines under its own instruments. Only an accepted Root contract and separately authorized App scope/contract alignment can unblock the App implementation item. B records deferral with its owner-chosen reopen condition. Neither path grants issuance, release, publication, provider/network expansion, authority-corpus repinning, merge, or professional reliance.

## Preparation handoff

This is a derivative decision package citing the accepted upstream basis above, not decomposition truth. Packet preparation is complete for review; full-policy implementation is unstarted and blocked on later owner ruling and Root contract authority. No lifecycle or Checking Approval SHA changes. Parent owns independent governed-diff review, registered closeout checks and register/receipt integration; no verifier verdict is anticipated here. Rerun factual review on source/ownership/contract drift or changed proposal semantics. Release disposition: **none**.
