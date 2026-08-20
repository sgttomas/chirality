# Frozen work graph v1

Status: `FROZEN BEFORE DISPATCH — AGENT 0 PROCEED APPROVAL REQUIRED`

Selection authority: `HUMAN+AGENT_0`. The human prescribed the node-selection
and development-pressure method; Agent 0 selected the one already-authorized
D-APP-97 C1 engineering target.

Posture: `MIXED`, fully serialized. There is exactly one engineering node.
Fresh review, remediation/re-review, package fan-in, and CHANGE are validation
or closeout stages rather than additional engineering targets.

## Nodes and stages

1. `N1 / A2-PKG09-PACKAGED-SECURITY-IMPLEMENT-01` — one bounded `TASK + software-bounded-implementation` child builds and executes the packaged-artifact network, key-attachment, and renderer-security proof, runs its checks, writes all node-owned product/test/proof/deliverable state, and returns exact evidence.
2. `R1 / A2-PKG09-PACKAGED-SECURITY-REVIEW-01` — after N1 reaches a terminal return and the manager freezes the complete diff/evidence identity, one fresh read-only `TASK + software-code-review` child reviews 100% of the frozen subject.
3. `RM*` — only if R1 or a later review has an actionable finding, a bounded serialized implementation remediation attempt owns the exact affected N1 targets and reruns affected/full gates.
4. `RR*` — a new fresh read-only 100% review follows every remediation.
5. `FAN-IN` — WORKING_ITEMS validates child returns, exact proof/check evidence, APP-HOLD reliance, containment, claim calibration, derivative disposition, deliverable effects, blockers/reruns, and the CHANGE handoff.
6. `CHANGE` — separate Agent 1 Git closeout after accepted fan-in; commits node(s) in dependency order and performs the tranche's PR closeout under the supervising run.

Edges: `N1 -> R1 -> FAN-IN -> CHANGE`; when needed,
`R1/RR* finding -> RM* -> RR* -> FAN-IN`. No stage is concurrent and no
write overlap exists.

## Ownership

- N1 owns all product/proof scripts, automated tests, CI integration,
  node-specific proof evidence, both selected deliverables' exact state/run
  evidence, and its run-local implementer return/status/check evidence.
- R1/RR* are filesystem read-only. They do not repair or rewrite the candidate.
- WORKING_ITEMS owns only graph/brief freezing and one package fan-in set of
  manager validation, return, status, and handoff records.
- Shared receipts, completion logs, registers, and other shared coordination
  roots are not written per node. Any required shared write occurs once under
  Agent 0 ownership at tranche fan-in.

## Check surfaces

- In-session: focused automated checks; full frontend Vitest; applicable
  frontend and Electron typecheck; registered build; secret scan; script and
  workflow validation; APP-HOLD integrity; instruction-root integrity;
  changed-path containment; candidate diff/whitespace hygiene.
- Host-capability: exact escalated unsigned `desktop:dist`/pack command and
  exact packaged Electron/keychain/process/network proof command after N1
  freezes its interface. These commands are executed by the active agent in
  this session; no pass is inferred from a sandbox denial.
- CI: registered CI and D-APP-97-authorized unsigned artifact proof only.
  External CI evidence cannot silently substitute for a required host proof.

N1 is selectable because each mandatory check has an available declared
surface: deterministic validation in-session, packaging/Electron/keychain
execution through host-capability escalation, and registered CI where the
final workflow exposes an external proof surface.

## Fan-in gates

1. A freshly built unsigned packaged artifact is the proof subject and is
   identity-bound to this branch/source revision.
2. Packaged network/provider and renderer controls pass fail-closed evidence
   without secret leakage or provider/network expansion.
3. Key precedence/storage/redaction and attachment validation/failure/retry
   coverage satisfy the selected DEL-09-06 AC-001 / R4-P49 scope.
4. DEL-09-04 REQ-009 is proven over the packaged artifact, not inferred from
   source/config review or the prior scripted no-live-provider SDK proof.
5. Every required focused, full, build, secret, network, instruction-root,
   unsigned package/dist, and packaged-proof check passes on its declared
   surface; exact commands and evidence are retained.
6. Fresh read-only review covers 100% of the frozen diff and returns `PASS`
   with zero actionable finding.
7. Write containment passes; lifecycle, Checking Approval SHA, F-APP-2,
   provider scope, credentials, dependency pins, owner-machine state, and
   unrelated Remaining items are unchanged.

## Failure and escalation

If N1 fails its checks, preserve its exact failed state/evidence and stop; no
dependant stage is released. If review finds a defect, serialize the bounded
remediation and fresh re-review. Any newly discovered work that is not part of
N1 is registered upward and is not added as a node. Dependency/lockfile,
runtime-security feature, provider/network, release/lifecycle, signing,
notarization, distribution, RunAtLoad, owner-machine, foreign-loop, or root
governance needs escalate to Agent 0.

Branch: `codex/app-packaged-security-proof-20260820`; accepted basis
`357a58b56726feba49507534159c3fbc4656b818`; intended PR base `main`; no PR
dependency declared.
