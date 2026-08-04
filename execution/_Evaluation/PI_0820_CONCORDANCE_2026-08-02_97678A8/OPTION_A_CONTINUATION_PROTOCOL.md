# Option A continuation protocol — Pi 0.82.0 evidence hold

Continuation node: `E2`
Parent evaluation: `PI_0820_CONCORDANCE_2026-08-02_97678A8`
Owner selection: `SELECT PI OPTION A under evidence hold; do not approve or supersede yet.`
Posture: `EVIDENCE-COLLECTION DESIGN / NO APPROVAL / NO SUPERSESSION`

## Frozen authority and evidence basis

The continuation is authorized by
`execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/OWNER_RULING_2026-08-02_CONTINUATION.md`
at SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`.
The plan-v4 surfaces read for sequencing are `ORCHESTRATION_PLAN.md` and the
terminal fan-in status graph `WORK_GRAPH.json`, observed respectively at SHA-256
`5d84ae468c6bb64607052c6b100674a237d1cd146b25d8b84838728dc4855737`
and `a7bd5a1fb61e8f387b6921952f6fc9aba88379cf9633a334fde27185e2a720d2`.

The accepted evaluation basis remains repository snapshot
`97678a841ef58345c73d3470ed8de57c9b1405d2`. The continuation checkout is
`4337990334c3e339a02c54de811d9f238246d524`; a scoped Git comparison proves
that every Pi candidate path enumerated in `OPTION_A_IDENTITY_BASIS.json` is
byte-identical to the accepted evaluation snapshot. Branch movement is not
candidate identity; the recorded file hashes are.

The prior immutable derivative outputs remain unchanged:

- `EVALUATION_PROTOCOL.md` — SHA-256
  `ebb7d19f7cf8aa3ca33c5e32c7bffe34fab1707ba7c9f50c9f0efef7f86cf824`;
- `EVALUATION_REPORT.md` — SHA-256
  `e5253fbb40dfa1159981d87073d415e6156adb338f51316be0a97ac1c7f620c1`;
- `FINDINGS.csv` — SHA-256
  `10c9e70b1db6e456d287c46e02578087958c89da763e829919823ddc3d0917d0`;
- `HANDOFF.md` — SHA-256
  `c241ece1f7fc59a57814b442fa5f7dd7523e65ca9f7924dd64a6691b5e9d22f0`.

No current authority changes:

- D-APP-72/SCA-APP-002 Pi `0.80.10` remains operative App authority.
- Root D-GOV-20 remains version-neutral.
- D-APP-84 V1 remains a prospective, Root-conditioned App target.
- Pi `0.82.0` bytes remain a preferred evidence candidate only.

## Evaluation questions

1. What exact Chirality implementation family is the Root candidate asked to
   accept: Root's `createPiOmlxEngineAdapter`, App's executable
   `PiAgentEngineAdapter`, or a governed convergence of the two?
2. Which fields make that implementation distinguishable from another adapter
   that advertises the same `pi` / `omlx` / package / version descriptor?
3. Does the App remain the executable dependency owner, or must the Pi package
   resolution move behind the Root engine package?
4. Which exact Electron/Node/builder/client composition forms part of the
   compatibility identity, and how is the `43.1.1` versus `43.2.0` authority
   conflict handled?
5. What evidence proves clean install, lifecycle behavior, complete dependency
   closure, source conformance, packaged native/WASM loadability, production
   route behavior, and live oMLX behavior for one exact candidate?
6. Which evidence is required for a Root version/identity decision, which is
   separately required for App adoption, and which remains release-only?

## Accepted toolbelt

This E2 planning pass uses only deterministic read-only inspection and the
already validated E1 returns. It dispatches no implementation or proof work.
Future work units in `OPTION_A_WORK_UNITS.csv` are bounded proposals: each
requires its owning loop/instrument to accept a sealed brief and its allowed
write targets before execution.

## Immutable evidence contract

Every future executed work unit must create a unique, run-ID-bearing evidence
directory. A mutable `latest` pointer may aid navigation but is never evidence.
At minimum each return bundle contains:

1. `BASIS.json` — source commit, dirty-state declaration, authority references,
   candidate identity, tool/runtime versions, and SHA-256 of every governed
   input;
2. `COMMANDS.jsonl` — ordered command, working directory, redacted environment,
   start/end timestamps, exit status, and produced-artifact references;
3. `RESULTS.json` — schema-versioned assertions with explicit PASS/FAIL/UNKNOWN;
4. `ARTIFACT_MANIFEST.csv` — relative path, byte size, SHA-256, provenance,
   derivative status, and evidence role;
5. `RETURN.md` — evidence-linked findings, limitations, blockers, and reruns;
6. `STATUS.json` — terminal status and exact acceptance-criteria verdict; and
7. a package-specific manifest named in the work-unit row.

Evidence is valid only when all hashes reproduce, every command is attributable
to the exact candidate, secrets/raw credentials are absent, and the bundle is
preserved without later in-place mutation. A rerun creates a new run ID.

## Sequencing

1. **E2 freeze — complete in this package.** Preserve authority, observed
   descriptor/implementation facts, questions, work units, and holds.
2. **Root candidate-identity gate.** HELPS_HUMANS / DEL-02-06 prepares the
   exact implementation-identity candidates. The human selects one identity
   for validation only. This is not Pi approval.
3. **App acceptance of its draft handoff.** The App loop chooses whether and
   how to authorize the client-owned repair/proof units. No Root file grants
   that authority.
4. **Candidate repair and proof.** After exact Root/App candidate hashes are
   frozen, execute clean-install/supply, package/native/WASM, source regression,
   live proof, and notice units in dependency order.
5. **Root identity conformance.** Prove that runtime registration, fingerprints,
   session evidence, packaging, and client composition bind the selected
   implementation family and cannot collide with the alternative.
6. **Independent EVALUATION fan-in.** Validate all returns and produce a new
   immutable candidate assessment. Do not modify the E1 package.
7. **Human Root decision gate.** Accept `0.82.0` and one exact identity, reject
   it, or continue the evidence hold. Passing evidence does not choose.
8. **App successor gate, only after Root acceptance.** App may consider a
   D-APP-72 successor and App SCOPE_CHANGE under its own authority.
9. **Task Management later.** Register disposition/archival is outside this
   continuation.

## Explicit holds

- `HOLD-PI-AUTHORITY`: no Root or App `0.82.0` approval exists.
- `HOLD-APP-SUPERSESSION`: D-APP-72/SCA-APP-002 `0.80.10` remains operative.
- `HOLD-IDENTITY`: no canonical Chirality adapter implementation family is
  selected for validation or acceptance.
- `HOLD-FOREIGN-WRITE`: no App or other project surface may be written here.
- `HOLD-SOURCE`: no dependency, lockfile, adapter, runtime, package, workflow,
  notice, decision, decomposition, or authority source write is authorized.
- `HOLD-NATIVE-PRIMITIVES`: native Read/Write/Edit/Bash and OS sandbox work from
  D-APP-84 P1/X1/H1 is separate held scope; native/WASM in this package means
  existing packaged dependency assets only.
- `HOLD-RESUME`: `durableResume: false` remains; R1 is not activated.
- `HOLD-LIFECYCLE-RELEASE`: no lifecycle, release, distribution, signing,
  notarization, publication, or reliance claim.
- `HOLD-TM`: no Task Management closure or archive action.
- `HOLD-GIT`: E2 performs no commit, push, PR, merge, rebase, or force action.

## Stop condition

E2 stops when the Root evidence-hold package and draft-only App handoff are
complete, hash-bound, validated, and returned to HELP_HUMAN. Execution of any
future work unit requires new authority from its owning instrument.
