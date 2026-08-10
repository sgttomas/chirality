# D-APP-93 — Simpler diagnostic architecture for the D-APP-92 causal proof

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-06 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Predecessor:** D-APP-92 Option A ruling SHA-256
`391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78`.

## 1. Decision requested

Which simpler execution architecture, if any, should govern preparation of a
new exact diagnostic packet for the still-open D-APP-92 causal trace and
replay objective:

- **Option A:** owner-operated interactive execution;
- **Option B:** single-session automation with no two-session supervisor; or
- **Option C:** defer unchanged.

This packet selects nothing. An A or B ruling would establish an architecture
baseline and authorize preparation of a later hash-bound execution packet
only. It would not authorize reconstruction, packaging, launch, LLDB, attach,
signal, replay, or any other command.

## 2. Why a new decision is required

D-APP-92 selected bounded native tracing plus sealed replay as the diagnostic
objective. Its later Attempt-8 designs tried to coordinate runtime control and
LLDB through an automated two-session supervisor. Fresh verification rejected
v1.20 and v1.21 on independently material target-binding, terminality,
deadline/callback, stdin-completion, and action-enumeration defects. The next
authoring cycle then stopped before successor bytes.

Those failures are evidence that the two-session supervisor design accumulated
a large and difficult-to-prove automation surface. They do **not** prove that
either candidate below is safe, do not establish a cause, and do not authorize
execution. A newly selected architecture still requires an exact prepared
packet, appropriate command authority, returned evidence, and fresh
adversarial verification.

## 3. Exact evidence basis

All cited run artifacts are derivative diagnostic evidence, not product,
decomposition, or acceptance truth.

| Evidence | SHA-256 | Calibrated contribution |
|---|---|---|
| D-APP-92 packet | `644c80ecff11577c9ab0f4f4fae4fa9b1f609cdaa2d801f118ffe052bfad77c6` | selected diagnostic objective and original limits |
| D-APP-92 ruling | `391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78` | diagnostic-only authority; first-signal gate unchanged |
| Attempt-5 `HANDOFF_STATE_R4.md` | `57ddd38db05a27f164d18163f014cbb97a02bd4356ee493ebb1d4d717c38bb3c` | narrow offline package method/identity/topology and rollback posture |
| Attempt-5 fresh verifier | `72576140d1d83688832c34998d4f912e3e43563cf70131699a51d125622e32f9` | accepts only offline construction, recorded package identity/topology, cleanup, and preparation release |
| Attempt-7 fresh verifier | `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f` | accepts timing/order mock direct-child PID/sentinel handshake for packet preparation only |
| current LLDB script | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` | current exact trace-script bytes; reuse requires fresh revalidation and freeze |
| C196/C197 owner adoption | `555c8e3078aaf29935cd48770a7e324850761b43fbf81499ad40ed95faddf535` | exact, preserved, valid, and unused command authority |
| C196/C197 fresh verifier R2 | `3ea8ac736a5a41da29ac12c37a2414bca3bf2fb698ac6bf84cbfdc48f216c1e3` | verifies exact approval fence only, not execution fitness |
| Attempt-8 `HANDOFF_STATE_R11.md` | `fca5663391800c57f2f97f760fdbd4ede79257d734f3abd130ffdc656206d43a` | v1.21 remains rejected; successor cycle stopped before bytes |
| v1.20 fresh verifier | `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655` | rejected two-session supervisor target/terminal/deadline/stdin graph |
| v1.21 fresh verifier | `8a765c15ac195661ec8e82da874fec5ef8981f083c135f6e02378673b82fe423` | rejected remaining byte-binding, callback-bound, completion, and enumeration defects |

The LLDB script path is
`execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt`.

## 4. Evidence that survives, and what does not

Four evidence classes must not be conflated with live execution state or
authority.

### 4.1 Attempt-5 package evidence

What survives is accepted offline package-construction method, the
contemporaneously recorded package identity/topology, and rollback/cleanup
evidence. The package and build trees were removed. Any later execution must
freshly reconstruct the candidate, freshly bind every required source,
dependency, package, identity, and topology hash, and prove cleanup again.

The raw C216 stdout/stderr byte stream is unavailable. No option may claim the
old package itself survives, reconstruct the missing raw stream, or use the
Attempt-5 result as runtime, attach, signal, replay, or first-signal credit.

### 4.2 Attempt-7 handshake evidence

What survives is a successful timing/order mock proof involving a direct-child
`/bin/sleep`, PID/sentinel acknowledgement, natural exit, terminal-session-
before-cleanup ordering, and cleanup. It proves no Electron/helper/GUI runtime,
PID-reuse safety, attach safety, signal delivery, LLDB behavior, replay timing,
or causal seam.

### 4.3 LLDB script

The current script bytes and SHA above survive as candidate diagnostic
material. Before any later use, the selected architecture's preparing manager
must freshly inspect the exact bytes, validate breakpoint/backtrace behavior
against the selected package and available symbols, freeze the script hash,
and bind that hash into the exact packet and runbook. Current presence and hash
are not execution authority or proof that every breakpoint will resolve.

### 4.4 Preserved C196/C197 approval

The approval remains valid, exact, unused, and limited to:

1. `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s <the exact frozen script>`;
2. one sealed direct-child helper PID only;
3. enumerated breakpoint/backtrace capture;
4. a 150-second absolute attach-to-detach maximum; and
5. in the same existing LLDB PTY, exact interrupt byte `\u0003`, then exact
   debugger bytes `process detach\nquit\n`.

It grants no PID search, alternate target, other debugger, process authority,
new signal path, generic stdin forwarding, watchdog, privilege, entitlement,
security/signing/admin change, memory/environment inspection, or credential
access. A later design may claim this authority only if its execution preserves
those exact semantics.

## 5. Option A — Owner-operated interactive execution

### 5.1 Architecture

After an Option A ruling, the loop prepares—but does not execute—a later exact
packet containing:

1. a fresh reconstruction recipe and hash-bound package manifest derived from
   the accepted Attempt-5 method;
2. a freshly revalidated and hash-frozen LLDB script;
3. a literal, numbered, step-by-step runbook with exact commands, expected
   evidence, stop conditions, cleanup, and deviation recording; and
4. a bounded evidence-return schema and ingestion/verification brief.

The owner then personally operates the later approved runbook in the owner's
own interactive macOS GUI session. The owner personally performs the launch,
selects the exact sealed direct-child PID supplied by the runbook's bound
launch evidence, invokes attach, causes the exact first signal at the ruled
step, observes the bounded trace/replay window, and performs detach/quit. No
agent, supervisor, forwarding program, watchdog, or second terminal session
translates those interactive acts.

After the owner returns the evidence, the App loop:

1. ingests only the declared evidence set;
2. independently validates hashes, ordering, target binding, trace timing,
   cleanup, redaction, and runbook deviations;
3. authors a supported-versus-unknown causal matrix; and
4. dispatches a genuinely fresh read-only adversarial verifier before making
   any causal, remedy, acceptance, or next-step claim.

### 5.2 Sequencing and gates

The phases are distinct and cannot imply one another:

1. **Architecture ruling:** chooses Option A and permits preparation only.
2. **Preparation:** produces the package recipe/manifest, script freeze,
   literal runbook, evidence schema, rollback, and exact command request.
3. **Preparation verification:** a fresh adversarial verifier must accept the
   packet before it is presented for any still-required command authority.
4. **Command gate:** every operation not already covered by exact C196/C197
   receives explicit owner approval. Package reconstruction, launch,
   registration, GUI interaction, signal, evidence handling, cleanup, and
   rollback are not inherited from C196/C197.
5. **Owner execution:** the owner executes only the exact approved literal
   runbook and records every step outcome or deviation.
6. **Evidence ingestion and validation:** execution does not equal acceptance.
7. **Causal matrix and fresh verification:** no supported cause or next step
   exists before both are complete.

### 5.3 Survival disposition

| Prior evidence | Option A disposition |
|---|---|
| Attempt 5 | **Consumes as historical construction method/identity/topology evidence only.** Fresh reconstruction and hash binding are mandatory; no package survives; raw C216 remains unavailable. |
| Attempt 7 | **Historical control evidence only.** It may inform runbook ordering and cleanup, but owner-operated interaction does not consume the two-session mock as runtime or safety proof. |
| LLDB script | **Candidate bytes may be reused only after fresh revalidation and freeze.** |
| C196/C197 | **May be consumed exactly** because the owner controls the same LLDB PTY and personally supplies the exact interrupt/detach/quit bytes, but only if the later packet preserves the exact direct-child PID, script, enumerated capture, and 150-second semantics. Any change requires new authority. |

### 5.4 Evidence return contract

The later runbook must require the owner to return, without credential values:

- exact source, dependency, archive, reconstructed-package, public identity,
  topology, LLDB-script, and runbook hashes;
- literal numbered-step outcomes, timestamps, start/stop times, and every
  deviation or skipped step;
- the sealed launch record establishing the numeric helper PID as the exact
  direct child, with the narrowly approved identity fields fixed by the later
  packet;
- raw LLDB stdout/stderr or the exact interactive transcript, including
  breakpoint resolution, trace events, bounded backtraces, errors, interrupt,
  detach, quit, and terminal state;
- the exact first-signal step and bounded poll/teardown/Root-stop/socket/owner
  observations required by D-APP-88;
- cleanup and rollback results, post-cleanup hashes, derivative absence, and
  retained-evidence manifest; and
- an explicit limitations/redaction record stating any missing bytes,
  unresolved symbols, timing uncertainty, operator deviation, or credential
  omission.

Evidence containing a token, keychain value, API key, secret, memory dump, or
environment dump is rejected from ingestion and returned for credential-safe
redaction under a separately governed process; it is not silently normalized.

### 5.5 Risks and failure modes

- Human timing and transcription error can reduce reproducibility.
- A wrong or stale PID, unexpected helper exit, unresolved breakpoint, attach
  prompt, elapsed 150-second bound, unexpected LLDB state, or runbook deviation
  is a stop; it is not repaired interactively outside the literal runbook.
- Manual operation may yield incomplete raw evidence or uncertain timing.
- The owner must retain evidence on a diagnostic failure when safe to do so,
  then perform only the approved cleanup/rollback steps.
- The simpler control plane reduces programmatic translation risk but transfers
  substantial execution and evidence-capture burden to the owner.

## 6. Option B — Single-session automation without a two-session supervisor

### 6.1 Architecture

After an Option B ruling, the loop prepares—but does not execute—a new exact
single-session design. One bounded controlling session owns the reconstruction
handoff, launch handles, exact direct-child PID record, LLDB child/session,
replay clock, evidence capture, cleanup, and rollback. There is no second
terminal session, sentinel-to-supervisor handoff, or two-session coordinator.

The later packet must enumerate every external command and every
script-internal operation that can launch, attach, write debugger input,
translate an interrupt, signal a process, enforce a time limit, retain
evidence, clean up, or roll back. It must contain explicit terminal/error
branches, exact target-identity revalidation immediately before attachment or
signal, bounded output/callback behavior, and a mechanically provable maximum.

### 6.2 Sequencing and gates

1. **Architecture ruling:** chooses Option B and permits preparation only.
2. **Preparation:** authors the complete single-session state machine, exact
   commands/internal actions, fresh package binding, script freeze, evidence
   schema, failure branches, cleanup, and rollback.
3. **Static and semantic verification:** a genuinely fresh adversarial
   verifier checks exact enumeration, byte stability, direct-child target
   safety, bounded timing/output, terminality, credentials, cleanup, and
   authority before any token is presented.
4. **Command gate:** all automated runtime and debugger behavior receives exact
   owner approval. No automation operation is inferred from architecture
   selection or historical C196/C197.
5. **Execution and evidence return:** only the sealed single session runs.
6. **Loop ingestion/validation, causal matrix, and a second fresh adversarial
   verification:** required before any causal or next-step claim.

### 6.3 Survival disposition

| Prior evidence | Option B disposition |
|---|---|
| Attempt 5 | **Consumes as historical construction method/identity/topology evidence only.** Fresh reconstruction and hash binding are mandatory; no package survives; raw C216 remains unavailable. |
| Attempt 7 | **May inform sequencing design only.** The mock proves timing/order of a direct-child PID/sentinel handshake, not single-session Electron, attach, signal, or replay safety. Because this option removes the two-session protocol, the proof remains historical control evidence rather than an execution prerequisite. |
| LLDB script | **Candidate bytes may be reused only after fresh revalidation and freeze.** |
| C196/C197 | **Context only unless exact semantics are literally preserved.** Any programmatic interrupt translation or forwarding, new stdin operation, watchdog, process signal, supervisor/controller behavior, changed target provenance, or changed session semantics is wholly new authority. The packet must not claim approval inheritance. |

### 6.4 Evidence return contract

The later execution must return the same package, script, target, trace,
first-signal, poll, cleanup, rollback, redaction, and limitation evidence
classes required by Option A, plus:

- a hash-bound single-session controller/state-machine object;
- machine event records for each enumerated external and internal operation;
- exact debugger stdin/stdout/stderr byte hashes and completion status;
- program-enforced output/chunk/duration bounds;
- watchdog/deadline arming and firing evidence, if such mechanisms are newly
  proposed and approved;
- terminal-versus-error evidence for every owned child; and
- a complete branch disposition showing which actions ran, did not run, or
  failed closed.

The loop independently validates that evidence, authors the causal matrix,
and dispatches a genuinely fresh verifier. Automation success alone is not
evidence acceptance.

### 6.5 Risks and failure modes

- One session reduces cross-session handoff and sentinel complexity but still
  combines timing, target identity, debugger I/O, child terminality, cleanup,
  and rollback in one state machine.
- An event-loop stall, unbounded callback/output, PID reuse, stdin-completion
  ambiguity, process-error/close confusion, or watchdog race can invalidate the
  claimed bound or target fence.
- Fail-closed behavior may intentionally retain temporary state and require a
  later separately approved cleanup action; the packet must state this before
  execution.
- The v1.20/v1.21 failures are mandatory design warnings, not reusable proof
  and not evidence that the single-session form is safe.

## 7. Option C — Defer unchanged

Authorize no replacement execution architecture and no packet preparation.
D-APP-92's diagnostic objective remains unconsumed, D-APP-88 remains open,
DEL-09-04 remains `IN_PROGRESS`, and TM-APP-036 remains unfired. The current
rolled-back product baseline remains operative.

| Prior evidence | Option C disposition |
|---|---|
| Attempt 5 | Retained as historical narrow offline package-method/identity/topology/cleanup evidence only; not consumed. |
| Attempt 7 | Retained as historical mock timing/order evidence only; not consumed. |
| LLDB script | Retained as historical candidate bytes; not revalidated, frozen for execution, or consumed. |
| C196/C197 | Preserved valid and unused; not invoked or consumed. |

A defer ruling should name the exact future trigger, if any. Elapsed time is
not acceptance or closure.

## 8. Comparative decision surface

| Dimension | Option A — owner-operated | Option B — single-session automation | Option C — defer |
|---|---|---|---|
| Control architecture | Owner personally operates one GUI/LLDB session from a literal runbook | One fully enumerated automated session; no second session or two-session supervisor | None |
| Automation complexity | Lower; preparation and evidence ingestion remain governed | Material, but narrower than rejected two-session design | None |
| Owner burden | Highest during execution and evidence capture | Lower during execution; owner still rules exact packet | No execution burden |
| Authority surface | Existing C196/C197 may remain exact; all other operations separately gated | Most runtime/debugger/I/O/watchdog behavior likely wholly new authority | No new authority |
| Timing safety | Human-operated 150-second discipline; deviations are explicit stops | Must be mechanically bounded across callbacks, output, branches, and child terminality | Not exercised |
| Evidence durability | Depends on literal runbook and complete owner-returned transcript | Machine capture can be stronger if the exact state machine is proven | Existing evidence only |
| Principal risk | Operator timing/transcription and incomplete returned evidence | Hidden executable branches, target races, I/O/terminality/deadline defects | Causal question remains open |
| Attempt-5 evidence | Method/history only; fresh reconstruction required | Method/history only; fresh reconstruction required | Historical only |
| Attempt-7 proof | Historical ordering guidance only | Historical sequencing guidance only; no runtime credit | Historical only |
| LLDB script | Freshly revalidate/freeze before use | Freshly revalidate/freeze before use | Not consumed |
| C196/C197 | Consumable only under exact owner-operated semantics | Context only unless exact semantics are literally preserved; new automation gets new authority | Preserved unused |

## 9. Validation implications after a ruling

### If A is selected

The preparing manager must return a complete literal runbook packet, not a
summary. A fresh verifier must check every hash, step, command, stop, target
binding, timing bound, evidence field, credential exclusion, cleanup, and
authority distinction before presentation. After owner execution, the loop
must distinguish operator attestation, raw machine evidence, derived findings,
unknowns, and unsupported claims in its validation and causal matrix.

### If B is selected

The preparing manager must freeze the complete external and internal action
graph. Static syntax or command-count checks are insufficient. Fresh semantic
verification must prove exact executable/action congruence, bounded callbacks
and output, live direct-child identity, debugger I/O completion, true child
terminality, exhaustive branches, retained-evidence behavior, and rollback.

### For either execution option

- Any missing raw byte stream remains missing and receives no reconstructed
  identity.
- An unresolved breakpoint is `UNKNOWN`, not evidence that a seam was not
  entered.
- A trace event can support only the seam it actually observes.
- The mandatory D-APP-88 first-signal conjunction remains unchanged.
- A fresh verifier PASS accepts only its stated claim level. It does not select
  a remedy, accept D-APP-88, close DEL-09-04, or fire TM-APP-036.

## 10. Later affected surfaces

If A or B is selected and its later preparation is separately executed, the
affected durable surfaces are limited to:

- a new App AgentRuns preparation/evidence root;
- an exact execution/runbook or automation command packet;
- fresh package/source/script/evidence/rollback manifests;
- later validation, causal-matrix, verifier, manager-return, handoff, and loop
  receipt records; and
- a later owner command-approval/adoption record where required.

Temporary reconstruction, package, HOME/userData, helper/GUI, debugger, and
evidence-capture paths must be individually named by that later packet. This
proposal creates none of them. No existing D-APP-92 evidence is rewritten.

## 11. No-effect boundary

This proposal and its register row create no runtime, debugger, LLDB, attach,
package/reconstruction, helper, GUI, signal, replay, network, credential,
memory/environment dump, process census, privilege, entitlement, security,
signing, admin, product/source/config/test change, remedy, D-APP-88 acceptance,
DEL-09-04 closure, TM-APP-036 firing, PRD/decomposition/SCOPE_CHANGE, generic
Root/Piping/PEC semantic, lifecycle, release, distribution, reliance, receipt,
Git, Task Management, foreign-loop, or professional-acceptance authority or
effect.

An A or B ruling authorizes preparation of the later exact packet only. The
owner-operated or automated execution remains separately command-gated. No
runbook, package recipe, script revision, automation program, command graph,
or runtime artifact is authored by this decision surface.

## 12. Owner return tokens

- `APPROVE D-APP-93 OPTION A — OWNER-OPERATED INTERACTIVE EXECUTION ARCHITECTURE — PREPARE THE HASH-BOUND PACKAGE, FRESHLY REVALIDATED LLDB SCRIPT, LITERAL RUNBOOK, AND EVIDENCE-RETURN PACKET ONLY — NO RUNTIME, DEBUGGER, PACKAGE, SIGNAL, CREDENTIAL, PRODUCT, RELEASE, RELIANCE, OR GIT ACTION`
- `APPROVE D-APP-93 OPTION B — SINGLE-SESSION AUTOMATION WITHOUT A TWO-SESSION SUPERVISOR — PREPARE THE FULLY ENUMERATED HASH-BOUND AUTOMATION AND EVIDENCE-RETURN PACKET ONLY — NO RUNTIME, DEBUGGER, PACKAGE, SIGNAL, CREDENTIAL, PRODUCT, RELEASE, RELIANCE, OR GIT ACTION`
- `DEFER D-APP-93 OPTION C — NO DIAGNOSTIC EXECUTION ARCHITECTURE SELECTED — TRIGGER: <exact trigger>`
