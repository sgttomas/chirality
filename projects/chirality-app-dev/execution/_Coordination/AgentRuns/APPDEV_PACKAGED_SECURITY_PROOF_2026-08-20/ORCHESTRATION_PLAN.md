# WORKING_ITEMS activation and orchestration plan v1

Status: `FROZEN BEFORE DISPATCH — AGENT 0 PROCEED APPROVAL REQUIRED`

This record activates one PKG-09 engineering node and freezes its proposed
Agent 2 scopes. No child has been dispatched and no product, test, proof,
deliverable-state, shared coordination, receipt, completion-log, or Git
closeout write has occurred in this activation turn.

## Activation identity

- RunID: `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`
- InstanceID: `WI-PKG09-PACKAGED-SECURITY-01`
- Parent: `HELP_HUMAN`
- PackageID: `PKG-09`
- Primary deliverable: `DEL-09-06`
- Dependent consumer: `DEL-09-04`
- Selection authority: `HUMAN+AGENT_0` — the human prescribed the selection
  method and development-pressure posture; Agent 0 selected this already
  authorized node under D-APP-97 C1.
- Branch: `codex/app-packaged-security-proof-20260820`
- Accepted branch basis: `357a58b56726feba49507534159c3fbc4656b818`
- Intended PR base: `main`
- PR dependency: none declared; this tranche is not stacked on another open
  iteration.

## Accepted basis and live representation

- Authority: `execution/_Coordination/_DECISIONS/D-APP-97_RULING_RELEASE_PREPARATION_2026-08-17.md`, status `RULED — C1`. C1 explicitly authorizes DEL-09-06 network, key-attachment, and renderer-security checks over the packaged artifact and makes the named PKG-09 R4-P49 PARTIAL assessments open engineering scope.
- Accepted decomposition basis for both deliverables: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca`.
- Representation: `SOW_V1` for `DEL-09-06` and `DEL-09-04`. Each selected folder has one `ScopeOfWork.md` with `schema: chirality-deliverable-sow/v1`; no live legacy four-document production set is present.
- Lifecycle: both deliverables remain `IN_PROGRESS`; their Checking Approval SHA remains `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` and is outside this activation.
- Residual fit: DEL-09-06 Remaining names the packaged-artifact network, key-attachment, and renderer-security proof. DEL-09-04 Remaining names REQ-009 / R4-P49 packaged network-policy proof and explicitly coordinates it with DEL-09-06. This is one producer-to-consumer node, not a dependency cycle.
- Software method profile: `software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`, schema `chirality-software-workflow/v1`.
- RunID uniqueness: the run root did not exist and the exact RunID had no match under the live AgentRuns, loop, or plan surfaces before this record was created.

## APP-HOLD-1 dispatch preflight

Command, run from `{WORKING_ROOT}` on the accepted branch basis:

```text
python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path agents/AGENT_WORKING_ITEMS.md --target DEL-09-06 --target DEL-09-04
```

Result: `ALLOW`. Both contracts are `CLEAR`; both hold states are `NOT_HELD`;
the active and scanned held-deliverable sets are empty; register comparison
matches.

- Repository HEAD: `357a58b56726feba49507534159c3fbc4656b818`
- Register SHA-256: `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`
- Scan fingerprint SHA-256: `00ebfe65174eaf28332dba6c3b1da8f8034b29d91d596bf4543865087f7da1c2`

The preflight must be rerun before each actual child dispatch and again at
fan-in before reliance on a child return.

## Selected node

`N1 — build and execute the packaged-artifact network, key-attachment, and renderer-security proof; on passing evidence close DEL-09-06's open D-APP-97 R4-P49 scope and DEL-09-04 REQ-009 / R4-P49 packaged-security residual.`

The node may add or modify only the proof/packaging scripts, automated tests,
and CI workflow integration needed to make the proof executable and
repeatable. It does not authorize an unrelated runtime/security feature node.
A product defect discovered outside packaging/proof/test glue is registered
upward and stops this node rather than becoming a second node.

## Declared reads

- Root and project agent instructions, WORKING_ITEMS and TASK contracts, the
  live software skill registry, `software-bounded-implementation` and
  `software-code-review` method packs, the software workflow profile/config,
  and APP-HOLD surfaces.
- D-APP-97 C1, the accepted decomposition entry, and both selected
  deliverables' `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`, `MEMORY.md`,
  `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and current
  assessments/evidence.
- Relevant product and proof surfaces: `.github/workflows/desktop-release-template.yml`, `frontend/package.json`, packaging configuration, `frontend/scripts/**`, `frontend/electron/**`, `frontend/src/lib/**`, and related tests.
- Git status, accepted-basis diff, and read-only repository identity/history.

## Proposed sealed implementer scope

- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-IMPLEMENT-01`
- Agent: `TASK + software-bounded-implementation` v1
- Objective: implement and execute N1 as one coherent proof node, preserving
  all D-APP-97 and F-APP-2 fences.
- ScopePath: the DEL-09-06 folder; DeliverableIDs: `DEL-09-06`, `DEL-09-04`.
- ApplyEdits: `true`.
- Proposed product/proof write targets:
  - `.github/workflows/desktop-release-template.yml` only if CI proof
    integration is necessary;
  - `projects/chirality-app-dev/frontend/scripts/**` only for bounded
    security-proof, packaging-proof, aggregation, or verification behavior;
  - `projects/chirality-app-dev/frontend/src/__tests__/**` for focused
    automated proof/policy regressions;
  - `projects/chirality-app-dev/frontend/package.json` only if an explicit,
    non-release proof command alias is necessary; `package-lock.json` is not
    writable;
  - new run-specific proof evidence below the selected DEL-09-06 and
    DEL-09-04 folders, plus each selected folder's `_STATUS.md`, `MEMORY.md`,
    and `_run_records/**`;
  - run-local implementer return/status/check evidence explicitly named in
    the final launch brief.
- The implementer owns all N1 product, automated-test, proof-evidence, and
  deliverable-state writes. It may narrow the exact path list after
  reconnaissance but may not widen these categories.
- Allowed execution surfaces: repository reads/search/edits; Git read-only
  diff/status/show; the brief-authorized software-workflow helpers; the
  focused and registered checks named below; exact host-capability commands
  requested through escalation when packaging, Electron, process inspection,
  or keychain access requires it.
- Required outputs: exact changed-path list and behavioral rationale; stable
  parseable proof evidence tied to the freshly built unsigned artifact and
  source revision; normalized check results; host commands/results; write
  containment; calibrated DEL state updates only after proof passes; TASK run
  record; residual risks/blockers/reruns; implementer return/status.
- Acceptance:
  1. A freshly built unsigned macOS artifact is identity-bound and the proof
     exercises packaged bytes rather than a repository-dev substitute.
  2. Packaged network evidence is fail-closed and shows no non-allowlisted
     outbound TCP, the required blocked renderer diagnostic/probe signal, and
     separate provider and renderer enforcement without provider expansion.
  3. Key handling evidence covers accepted precedence/storage and proves no
     real or fixture key leakage into logs, events, summaries, tracked files,
     or retained artifacts; renderer policy metadata cannot leak credential,
     query, or userinfo material.
  4. Attachment evidence covers server-side path/type/symlink/readability and
     byte-budget validation, partial-failure continuation, total-failure
     `ATTACHMENT_FAILURE`, and failed-send retry preservation.
  5. The secret scan, focused tests, full Vitest, applicable frontend and
     Electron typecheck, build, network policy, instruction-root integrity,
     unsigned pack/dist, and packaged proof all pass on their declared
     surfaces with stable retained evidence.
  6. DEL-09-06's exact D-APP-97 R4-P49 Remaining item and DEL-09-04's exact
     REQ-009 / R4-P49 packaged-security residual are removed only when the
     accepted evidence proves them; both lifecycle states and Checking
     Approval SHAs remain unchanged.
- Escalation: any dependency/lockfile/pin, product runtime security behavior
  outside proof/packaging glue, provider/network expansion, real credential
  need, signing/notarization/distribution/publication, release/lifecycle act,
  owner-machine deployment, RunAtLoad work, foreign-loop/root-governance
  change, missing required host proof, or additional node returns to
  WORKING_ITEMS/Agent 0 without widening N1.

## Proposed fresh reviewer scope

- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-REVIEW-01`
- Agent: fresh `TASK + software-code-review` v1
- ApplyEdits: `false`; AllowedWriteTargets: `[]`. The manager persists the
  native return/status so the reviewer remains filesystem read-only.
- Inputs: the sealed implementer brief/return, accepted basis, complete
  manager-frozen file/hash manifest for 100% of the product-source and proof
  diff, verification evidence, host commands/results, and the two unchanged
  SOW contracts plus their proposed state deltas.
- Objective: independently review every frozen changed path for correctness,
  regressions, security, evidence integrity, write containment, acceptance
  coverage, claim calibration, and preservation of all fences.
- Required return: `PASS | PASS_WITH_FINDINGS | FAIL`; exact 100% hash and
  semantic coverage; findings with locations/impact/remediation; evidence-gap
  audit against every implementer acceptance item; residual risks; explicit
  confirmation of no writes/delegation. Publish requires `PASS` with zero
  actionable findings.
- Any actionable finding returns to a bounded serialized remediation attempt
  followed by a newly fresh 100% review.

## Check placement

- In-session: focused script/workflow/security tests; full frontend Vitest;
  frontend and Electron typecheck as applicable; registered frontend build;
  secret scan; static/script validation; APP-HOLD integrity; instruction-root
  integrity; software change-scope validation; diff/whitespace hygiene.
- Host-capability, run by the executing agent after exact-command escalation:
  `npm run desktop:dist` (or the narrower accepted unsigned pack command if it
  fully produces the required subject) and the exact packaged Electron,
  keychain-backed, process/network-capture proof command exposed by N1. A
  sandbox denial is not a pass or a park condition; park only if the
  escalation request itself is declined.
- CI: only registered CI checks and any D-APP-97-authorized unsigned artifact
  proof integration added by N1. CI is additional/external proof and does not
  replace a required host-capability surface unless an owning instrument
  explicitly permits that substitution.

## Parked exclusions

Signing, notarization, distribution/publication, release claims, provider
expansion, lifecycle transition, Checking Approval SHA change, owner-machine
daemon deployment, login-time `RunAtLoad`, decisions/registers, dependency or
lockfile changes, root governance/agents/skills/tools, foreign-loop writes,
and any engineering target discovered after selection are parked outside this
activation.

## Proceed gate

Agent 0 approval is required before the implementer brief is materialized and
dispatched. The graph in `WORK_GRAPH.md` is frozen; approval may authorize
dispatch without changing the graph. Any scope, acceptance, risk, or authority
change requires a versioned amendment and renewed approval.
