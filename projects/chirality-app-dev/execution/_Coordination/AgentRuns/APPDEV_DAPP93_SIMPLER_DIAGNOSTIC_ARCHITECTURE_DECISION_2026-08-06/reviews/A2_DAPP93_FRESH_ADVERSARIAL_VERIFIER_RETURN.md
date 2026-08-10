# A2 D-APP-93 fresh adversarial verifier return

## Verdict

`PASS_FOR_OWNER_DECISION_PRESENTATION`

The frozen D-APP-93 packet and decision-register row are stable, neutral,
evidence-calibrated, and safe for owner decision presentation at the proposal
claim level. This verdict is structural and semantic verification only. It is
not an owner ruling and authorizes no preparation, runtime, debugger, package,
signal, network, credential, product, release, reliance, receipt, or Git
action.

## Initial frozen-object identities

| Frozen object | Required SHA-256 | Initial SHA-256 | Result |
|---|---|---|---|
| D-APP-93 packet | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | PASS |
| Decision register | `f89ae7cf34b8efe5f7b50d139f71c892d72ac5517ffd93335a43ba9a1e576cd8` | `f89ae7cf34b8efe5f7b50d139f71c892d72ac5517ffd93335a43ba9a1e576cd8` | PASS |

## Mandatory semantic checks

1. **Register integrity — PASS.** The register contains 93 contiguous,
   unique decision rows, D-APP-01 through D-APP-93, so D-APP-93 was the next
   free ID when added. Exactly one row begins with `D-APP-93`. It is
   `AWAITING_RULING`, names the exact frozen packet path, has ruling record
   `-`, and expressly limits any ruling to later packet preparation with no
   execution or acceptance effect.
2. **Neutrality — PASS.** The packet is explicitly `PROPOSAL —
   AWAITING_RULING — NO OPTION SELECTED`, says that it selects nothing, and
   makes no recommendation. Options A, B, and C are presented as genuine
   alternatives. Conditional selection language and the owner return tokens
   grant preparation only and hide no execution authority or recommendation.
3. **Required candidates — PASS.** Option A is a later hash-bound package,
   freshly revalidated/frozen LLDB script, and literal numbered runbook that
   the owner personally operates for launch, direct-child PID selection,
   attach, first signal, and detach/quit in the owner's GUI session. Returned
   evidence is later ingested and validated before causal-matrix authorship
   and fresh adversarial verification. Option B is a single controlling
   session with no second terminal, sentinel-to-supervisor handoff, or
   two-session supervisor. Option C defers unchanged.
4. **Attempt-5 calibration — PASS.** The packet limits survival to offline
   construction method, contemporaneously recorded identity/topology, and
   rollback/cleanup evidence. It states that package/build trees were removed,
   raw C216 bytes remain unavailable, fresh reconstruction and hash binding
   are mandatory for later execution, and no runtime, attach, signal, replay,
   or first-signal credit exists. Each option's disposition preserves that
   limit.
5. **Attempt-7 calibration — PASS.** Only mock timing/order, direct-child
   `/bin/sleep`, PID/sentinel acknowledgement, natural exit, terminal-before-
   cleanup ordering, and cleanup survive. The packet grants no Electron,
   runtime, PID-reuse, attach, signal, LLDB, target-safety, replay, or causal
   credit. The A/B/C tables clearly distinguish historical-control/design
   guidance from consumption.
6. **LLDB-script calibration — PASS.** The current script SHA-256 is exactly
   `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
   Reuse is conditional on fresh byte inspection, selected-package/symbol
   revalidation, freeze, and later packet/runbook hash binding. Current
   presence grants neither authority nor breakpoint fitness.
7. **C196/C197 calibration — PASS.** The packet preserves the approval as
   exact, valid, and unused and limits it to the frozen script, one sealed
   direct-child PID, enumerated capture, a 150-second attach-to-detach bound,
   and exact same-PTY ETX followed by `process detach\nquit\n`. Option A can
   consume only literally preserved owner-operated semantics. Option B treats
   the approval as context unless those semantics are literal and identifies
   translation, forwarding, stdin, watchdog, process-signal, and controller
   behavior as wholly new authority.
8. **Mechanics and gates — PASS.** A and B separately state architecture
   ruling, preparation, fresh packet verification, owner command gate,
   execution/evidence return, loop ingestion/validation, causal-matrix
   authorship, and fresh post-execution verification. Neither architecture
   ruling implies a later gate.
9. **Evidence contract — PASS.** Option A requires exact package/source/
   dependency/archive/identity/topology/script/runbook hashes, timestamps,
   numbered outcomes and deviations, live direct-child PID binding, LLDB
   transcript and terminal state, first-signal and bounded poll evidence,
   cleanup/rollback and retained-evidence records, credential-safe redaction,
   and explicit limitations. B inherits those classes and adds a hash-bound
   state machine, enumerated machine/action events, exact debugger I/O hashes
   and completion, enforced bounds, deadline/watchdog evidence, child
   terminality, and complete branch disposition.
10. **Risks and validation — PASS.** A identifies human timing,
    transcription, stale/wrong PID, helper exit, breakpoint, attach-state,
    deadline, deviation, and incomplete-evidence risks. B identifies event-
    loop, callback/output, PID, stdin, terminal/error, state-machine, and
    watchdog races. v1.20/v1.21 are treated as mandatory complexity warnings,
    never safety proof.
11. **Affected surfaces and no-effect fence — PASS.** The packet identifies
    only prospective later durable surfaces and says this proposal creates no
    recipe, runbook, script revision, controller, automation, command graph,
    package, or runtime artifact. Its no-effect boundary covers runtime,
    debugger, attach, package, signal, replay, network, credential, product,
    acceptance, release, reliance, receipt, Git, Task Management, and foreign-
    loop effects.
12. **Evidence citations — PASS.** Every cited file exists and every exact
    SHA-256 reproduces. The calibrated contributions match the cited sources;
    no missing, mismatched, or materially overclaimed source was found.
13. **Text hygiene and consistency — PASS.** Neither frozen object contains
    trailing whitespace or a terminal blank line. Markdown table pipe counts
    are consistent within every table. The packet contains no current-option
    selection, hidden recommendation, or contradiction with the register.

## Evidence SHA-256 reproduction

| Packet evidence row | Reproduced SHA-256 | Result |
|---|---|---|
| D-APP-92 packet | `644c80ecff11577c9ab0f4f4fae4fa9b1f609cdaa2d801f118ffe052bfad77c6` | PASS |
| D-APP-92 ruling | `391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78` | PASS |
| Attempt-5 `HANDOFF_STATE_R4.md` | `57ddd38db05a27f164d18163f014cbb97a02bd4356ee493ebb1d4d717c38bb3c` | PASS |
| Attempt-5 fresh verifier | `72576140d1d83688832c34998d4f912e3e43563cf70131699a51d125622e32f9` | PASS |
| Attempt-7 fresh verifier | `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f` | PASS |
| Current LLDB script | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` | PASS |
| C196/C197 owner adoption | `555c8e3078aaf29935cd48770a7e324850761b43fbf81499ad40ed95faddf535` | PASS |
| C196/C197 fresh verifier R2 | `3ea8ac736a5a41da29ac12c37a2414bca3bf2fb698ac6bf84cbfdc48f216c1e3` | PASS |
| Attempt-8 `HANDOFF_STATE_R11.md` | `fca5663391800c57f2f97f760fdbd4ede79257d734f3abd130ffdc656206d43a` | PASS |
| v1.20 fresh verifier | `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655` | PASS |
| v1.21 fresh verifier | `8a765c15ac195661ec8e82da874fec5ef8981f083c135f6e02378673b82fe423` | PASS |

## Final frozen-object identities

| Frozen object | Initial SHA-256 | Final SHA-256 | Result |
|---|---|---|---|
| D-APP-93 packet | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e` | PASS — no drift |
| Decision register | `f89ae7cf34b8efe5f7b50d139f71c892d72ac5517ffd93335a43ba9a1e576cd8` | `f89ae7cf34b8efe5f7b50d139f71c892d72ac5517ffd93335a43ba9a1e576cd8` | PASS — no drift |

Final verdict: `PASS_FOR_OWNER_DECISION_PRESENTATION`.
