# Option A decision gates

Status: `G0 COMPLETE; G1 THROUGH G6 HELD`

## Gate map

| Gate | Question | Required inputs | Decision owner | Allowed result | Present state |
|---|---|---|---|---|---|
| `G0 — Option selection` | Continue V1 as the preferred evidence candidate? | E1 report and owner ruling | Human owner | Select evidence hold, restore, or reject | **COMPLETE:** Option A selected; no approval/supersession. |
| `G1 — Validation-target identity` | Which exact Chirality implementation family and identity schema will the evidence campaign test? | `OPTION_A_IDENTITY_BASIS.json`; PIA-U10 options/schema | Human Root owner | Select one target for validation, amend options, or continue hold | **HELD:** same-descriptor Root/App implementations unresolved. |
| `G2 — App work acceptance` | Will the App loop authorize the repair and proof work under its own instruments? | Accepted draft handoff; G1 target; exact App brief | Human/App owner | Accept, amend, decline, or defer each work unit | **HELD:** Root draft creates no App authority. |
| `G3 — Evidence fan-in readiness` | Do all mandatory technical bundles satisfy their exact schemas and acceptance rules? | PIA-U21/U22/U23/U24/U30 returns; PIA-U25 classified release-only | EVALUATION validates; human accepts any waiver | Ready, not ready, or explicit waiver request | **HELD:** package/live/identity evidence missing. |
| `G4 — Root Pi version/identity decision` | Does Root accept Pi `0.82.0` with the exact identity, reject it, or continue the hold? | New EVALUATION fan-in; exact candidate hashes; conflicts/unknowns | Human Root owner | Accept exact candidate, reject, or continue hold | **HELD:** no Root approval exists. |
| `G5 — App successor` | If Root accepts, does App prospectively supersede its `0.80.10` / `43.1.1` facts and adopt the affected client? | Root decision/notice; App impact assessment; App evidence | Human/App owner | Accept, amend, decline, or defer App successor/SCOPE_CHANGE | **HELD:** D-APP-72 remains operative. |
| `G6 — Task Management disposition` | Do the later decision record and validation evidence satisfy TM-ROOT-106 closure? | Root decision; validation evidence; any App response required by final disposition | Human through Root TASK_MANAGEMENT | Owner-ruled disposition and later archive | **OUTSIDE RUN.** |

## G1 identity choices to present

PIA-U10 must present, at minimum, these non-inferred choices:

1. **Root-wrapper canonical.** Root's `createPiOmlxEngineAdapter` becomes the
   sole public implementation family; App supplies a governed
   `PiTurnRuntimePort`/provider composition. Required source migration and
   affected-client work are separately gated.
2. **App-host implementation explicitly registered.** Root accepts a generic
   identity schema under which App's `PiAgentEngineAdapter` is a named
   affected-client implementation family. Root's reference wrapper is not the
   executed family. Registry/fingerprint/evidence must carry this distinction.
3. **Converged Root concrete adapter.** Move or recreate the concrete session
   implementation under the Root engine package, then make App consume it.
   This is broader than an identity record and requires SCOPE_CHANGE plus
   implementation authority.
4. **Continue hold.** Gather only non-implementation evidence or revise the
   identity proposal; no candidate is selected for final validation.

E2 does not choose among these. A G1 selection chooses what to validate, not
whether Pi `0.82.0` is approved.

## G3 mandatory versus release-only evidence

Mandatory before G4:

- canonical implementation identity and collision-proof evidence;
- exact-lock install, dependency closure/integrity, and lifecycle evidence;
- source regression/conformance on the final candidate;
- repaired packaged-proof entrypoint;
- exact macOS package/native/WASM/direct-load/production-route evidence;
- repeated live `0.82.0` proof required by the current reliance register; and
- explicit treatment of the Electron prerequisite conflict in the decision
  packet, even though App alone may supersede its authority fact.

Release-only after version acceptance unless the owner expressly folds it into
G4:

- complete 140-artifact/package-actual third-party notice provenance;
- signing, notarization, publication, distribution, lifecycle, and reliance
  acts.

Not part of G4:

- Pi-native Read/Write/Edit/Bash, OS sandbox implementation, H1, or R1 durable
  resume. Those remain separate D-APP-84/Root work and cannot be smuggled into
  a version decision.

## Decision packet contract for G4

The final Root decision surface must cite:

1. exact owner question and non-inferred options;
2. accepted authority snapshots and SHA-256 values;
3. candidate identity JSON and every implementation/package/lock hash;
4. validated return inventory and immutable bundle hashes;
5. criterion-by-criterion verdict from `OPTION_A_ACCEPTANCE_MATRIX.csv` or its
   successor;
6. explicit conflicts, unknowns, waivers, and release-only residuals;
7. selected result: accept exact candidate, reject, or continue hold;
8. prospective effect and no-effect boundaries;
9. rollback identity and rerun triggers; and
10. separately owned App and Task Management follow-ons.

No agent drafts the owner's act as though already selected.
