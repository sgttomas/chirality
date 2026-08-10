# A2 brief — D-APP-93 simpler diagnostic architecture decision packet

- Parent: `HELPS_HUMANS` Agent 1 under App `HELP_HUMAN`
- Construction form: fresh ephemeral Agent 2 generalist
- Objective: author a decision-only D-APP-93 proposal and one register row
- Working root: `projects/chirality-app-dev`
- Decision ID: `D-APP-93` (next free live-register ID at dispatch)
- Date: `2026-08-06`

## Read-only context

Read the applicable root `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`, committed
App loop plan, Receipt 131, live decision register, D-APP-92 packet and ruling,
Attempt-5 handoff/verifier/evidence, Attempt-7 verifier/evidence, current LLDB
script, C196/C197 approval/adoption and verifier, `HANDOFF_STATE_R11.md`, and
the v1.20/v1.21 rejected verifier returns.

The current owner direction is authoritative for this authoring tranche:

> RE-SCOPE D-APP-92: prepare a decision surface for a simpler diagnostic architecture. Candidate architectures must include (a) owner-operated interactive execution — agent-prepared hash-bound package, LLDB script, and a literal step-by-step runbook; the owner personally executes launch, attach, signal, and detach in their own GUI session; the loop ingests and validates the returned evidence, authors the causal matrix, and dispatches fresh adversarial verification — and (b) single-session automation with no two-session supervisor. State per candidate what survives from accepted evidence: the Attempt-5 package, the Attempt-7 handshake proof, the LLDB script, and the preserved C196/C197 approval. Prepare the surface; decide nothing; no runtime, debugger, package, or Git action.

## Write scope

Write only:

1. `execution/_Coordination/_DECISIONS/D-APP-93_PACKET_SIMPLER_DIAGNOSTIC_ARCHITECTURE_2026-08-06.md`;
2. exactly one appended `D-APP-93` row in
   `execution/_Coordination/_DECISIONS/_REGISTER.md`, state
   `AWAITING_RULING`; and
3. `execution/_Coordination/AgentRuns/APPDEV_DAPP93_SIMPLER_DIAGNOSTIC_ARCHITECTURE_DECISION_2026-08-06/instances/A2-DAPP93-PACKET-AUTHOR-01/TERMINAL_RETURN.md`.

Do not write the runbook, package recipe, LLDB script, command packet, ruling,
receipt, validation, manager freeze, verifier brief/return, manager return, or
handoff. Stop before manager hashes.

## Required packet content

The packet is `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`. Present no
selection and no recommendation. Include:

- Option A: owner-operated interactive execution exactly as directed. A later
  agent-prepared, hash-bound package + freshly revalidated/frozen LLDB script +
  literal step-by-step runbook; owner personally performs launch, attach,
  signal, and detach in the owner's own GUI session; the loop later ingests and
  validates returned evidence, authors a supported-versus-unknown causal
  matrix, and dispatches a genuinely fresh adversarial verifier.
- Option B: single-session automation with no two-session supervisor. Define
  the high-level mechanics and owner-gated later design/command packet, but do
  not author implementation or commands now.
- Option C: defer unchanged, leaving D-APP-88/DEL-09-04 open and TM-APP-036
  unfired.

For each candidate state precisely what survives from these four evidence
classes and whether the candidate consumes it:

1. Attempt 5 survives only as accepted offline package-construction identity,
   topology, method, rollback, and cleanup evidence. The package/build tree was
   removed and must be freshly reconstructed and hash-bound before any later
   execution. Raw C216 bytes are unavailable. Do not call the package itself
   surviving.
2. Attempt 7 survives only as accepted timing/order mock direct-child
   PID/sentinel handshake evidence. It proves no real runtime, attach, signal,
   target safety, or replay behavior. State whether each option consumes it or
   keeps it only as historical control evidence.
3. The current LLDB script at
   `execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt`
   currently hashes to
   `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
   It may be reused only after fresh revalidation and freeze for the selected
   execution; current bytes/hash are evidence, not execution authority.
4. C196/C197 approval is preserved, valid, exact, and unused. For Option A it
   may be consumed only if the owner-operated execution preserves the exact
   LLDB PTY, one sealed direct-child helper PID, enumerated breakpoint/
   backtrace, 150-second attach-to-detach, exact ETX plus
   `process detach\nquit\n`, and exclusion semantics. Any changed PID
   provenance, target, script semantics, session mechanics, or commands needs
   new authority. For Option B it is context only unless the automation
   literally preserves those exact semantics; any programmatic translation,
   forwarding, new stdin operation, watchdog, process signal, or supervisor
   behavior is wholly new authority. Do not imply approval inheritance.

For A and B include:

- high-level mechanics and explicit separation between later preparation,
  owner command approval, execution, evidence return, loop ingestion/
  validation, causal-matrix authorship, and fresh adversarial verification;
- evidence return contract, including exact hashes/manifests, timestamps,
  PID/direct-child binding, LLDB transcript, owner-recorded literal runbook
  step outcomes/deviations, first-signal and bounded-poll evidence,
  cleanup/rollback evidence, credential redaction, and limitations;
- failure modes and stop/retain-evidence behavior;
- validation implications and claim calibration;
- affected files/surfaces only if later selected and separately authorized.

Include a comparative table covering complexity, human burden, authority
surface, timing safety, evidence durability, automation risk, and the four
survival classes. Explain that prior v1.20/v1.21 failures are evidence about
the two-session supervisor's automation complexity, not proof that a simpler
single-session design is safe.

Include exact owner return tokens for A/B/C that rule only the architecture
baseline and authorize preparation of a later exact execution/runbook packet,
not any operation. The token wording must not authorize runtime, debugger,
package, signal, credential, product, release, reliance, or Git action.

Include an explicit no-effect boundary: this packet/register row creates no
runtime, debugger, attach, package/reconstruction, helper, GUI, signal, replay,
network, credential, memory/environment dump, process census, privilege,
entitlement/security/signing/admin, product/source/config/test, remedy,
D-APP-88 acceptance, DEL-09-04 closure, TM-APP-036 firing, PRD/decomposition/
SCOPE_CHANGE, generic Root/Piping/PEC semantics, lifecycle, release, reliance,
receipt, Git, Task Management, or foreign-loop effect. The later owner-run
execution remains separately command-gated.

## Acceptance checks

- D-APP-93 is next-free and appears once in the register.
- One register row only, `AWAITING_RULING`, packet pointer exact, ruling `-`.
- Packet is decision-ready, neutral, and contains no selected/recommended
  option.
- Every evidence citation exists and any stated SHA matches current bytes.
- Preservation matrix is calibrated exactly as above.
- No runbook/package/script/commands are authored; no executable operation.
- All changes stay App-only and within the three write targets.
- `git diff --check` passes for authored text.
- Terminal return lists touched paths and confirms the author stopped before
  manager hashing and performed no runtime/debugger/package/Git operation.
