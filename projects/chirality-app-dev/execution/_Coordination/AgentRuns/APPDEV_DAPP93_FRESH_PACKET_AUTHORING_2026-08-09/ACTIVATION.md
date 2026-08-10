# Activation — D-APP-93 fresh packet authoring lineage

Status: `ACTIVE — PREPARATION ONLY`

## Identity and authority

- RunID: `APPDEV_DAPP93_FRESH_PACKET_AUTHORING_2026-08-09`
- InstanceID: `WI-PKG09-DAPP93-FRESH-01`
- Parent: `HELP_HUMAN`
- PackageID: `PKG-09`
- Package path: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/`
- Selected deliverable: `DEL-09-04`
- Representation state: `SOW_V1`
- Objective: prepare and validate one wholly fresh D-APP-93 command packet lineage, freeze its exact bytes, obtain one fresh verifier verdict, and stop at the exact-owner-hash-approval gate.
- Selection authority: owner direction by Ryan Tufts, 2026-08-09, beginning `D-APP-93 ruling: START A NEW AUTHORING LINEAGE.`
- Entry Git state: clean branch `codex/app-dapp93-fresh-authoring-lineage-20260809` at `2109e4bd78c0ba240dd7cb80394c0d116bb89216`.
- Standing-plan loader: committed `HEAD` selected `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md` as the unique bytewise-last `WORKPLAN_*.md` blob, mode `100644`.

This run is derivative preparation evidence only. It is not product truth,
decomposition truth, execution authority, acceptance, reliance, release, or a
lifecycle act.

## Accepted-basis boundary

The reconstruction node must independently discover, read, and SHA-256 verify
only these accepted pre-attempt-3 classes:

1. D-APP-92 proposal and ruling;
2. D-APP-93 proposal and ruling;
3. D-APP-94 feasibility-probe proposal/ruling and Final Posture proposal/ruling;
4. accepted R8 feasibility result and terminal handoff;
5. accepted terminal D-APP-93/D-APP-94 lane handoff;
6. current live DEL-09-04 and PKG-09 basis;
7. earlier accepted immutable packet/script/runbook sources explicitly cited by those authorities.

Attempt-3 roots are excluded as content input. A child may read only their
terminal handoff, manager-validation, runtime-summary, and Receipt-146 pointers
needed to bind exclusion and preservation constraints. It may mechanically hash
and inventory the roots without semantically inspecting excluded bytes.

## Hard exclusions

- Never resume from, repair, copy, semantically diff, or use as source any old
  attempt-3 `prepared/**`, `candidate/**`, `briefs/**`, `returns/**`, author
  working bytes, or deleted/lost ledger material.
- Never execute a packet command or script, LLDB/debugger, Electron/helper/
  package, Security/Keychain, signal/trace, credential, runtime, GUI, C1118,
  network, product, release, reliance, Git mutation, Task Management, receipt,
  register, decision, lifecycle, or foreign-loop operation.
- Do not write outside this run root.
- Do not create an approval claim. Every command and operator input remains
  `OWNER_APPROVAL_REQUIRED` and do-not-execute.

## Writable boundary and software profile

- Sole writable boundary:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FRESH_PACKET_AUTHORING_2026-08-09/**`
- Project-local profile: `projects/chirality-app-dev/software-workflow.json`
- Runtime/product checks in that profile are not authorized for this packet-
  authoring run. Static governance checks may be run by the manager after
  freeze; no child may infer authority from the profile.

## Completion contract

Success requires `PREPARED_VERIFIED_AWAITING_EXACT_OWNER_HASH_APPROVAL`, a
deterministic sorted path/size/SHA-256 manifest over all candidate packet bytes
plus terminal author return, SHA-256 of the manifest bytes as frozen packet
identity, fresh verifier `PASS`, post-verifier manifest recomputation proving
zero frozen-byte change, old-root preservation evidence, and terminal
`HANDOFF_STATE.md`. Anything else closes `BLOCKED` with preserved evidence,
manager validation, and exact rerun blocker.
