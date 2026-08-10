# Stage 2 — authority semantics

Status: `COMPLETE`

Run: `APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09`

## Controlling posture

The two operative rulings combine as follows:

1. The selected execution architecture is owner-operated and interactive.
   The owner, not an agent or controller, would personally perform launch,
   exact direct-child PID selection, debugger attach and input, the first
   signal, bounded observation, and debugger detach/quit.
2. The isolated sealed-HOME login-keychain recipe is a planning baseline
   supported by bounded feasibility evidence. It is not runtime, Security,
   Keychain, Electron, credential, package, trace, product, or reliance
   authority.
3. This lineage is preparation only. No row in the reconstructed ledger is
   executable until the complete packet is byte-frozen, freshly verified,
   and the owner approves that exact freeze hash.
4. Approval of one row never grants another row, an alternate spelling, a
   retry, an omitted branch, an inferred recovery action, or a deviation.

## Authority classes for the fresh ledger

| Authority class | Meaning | Later execution requirement |
|---|---|---|
| `PREPARATION_ONLY_STATIC` | A command is written into the packet or used by a future verifier as exact planned text, but this lineage does not run it. | Exact command must be present in the frozen packet and covered by the owner's exact-hash approval before invocation. |
| `OWNER_OPERATED_NEW` | A shell command or operator action not covered by any preserved exact fence: reconstruction, package, launch, signal, evidence, cleanup, or rollback. | Fresh owner approval of the exact frozen packet is mandatory. Owner executes literally and records outcome/deviation. |
| `OWNER_OPERATED_PRESERVED_FENCE` | The debugger attach/input sequence may rely on the accepted unused two-operation debugger fence only when its target provenance, script bytes, capture scope, timing, PTY, interrupt, detach, and quit semantics remain literal. | The fresh packet must demonstrate exact semantic preservation and still receive owner approval by freeze hash. Any semantic change is `OWNER_OPERATED_NEW`. |
| `OWNER_ATTESTATION` | A non-command interactive observation or confirmation that cannot honestly be reduced to machine output, such as prompt state or GUI-visible posture. | The frozen runbook must state the exact observation, allowed response, evidence field, and stop rule. |
| `INGESTION_ONLY` | A future post-execution evidence-copy, hash, inventory, or validation operation; it makes no causal or acceptance claim by itself. | Separately authorized only after owner-returned evidence exists; no credential-bearing input may be ingested. |
| `PROHIBITED` | An operation outside the selected posture or evidence boundary. | It must not appear as an executable step. Its occurrence is a stop/deviation requiring return to the manager/owner. |

Every executable ledger row uses one of the first five classes and says
`YES — exact frozen-packet hash approval` in `required_owner_approval`.
`PROHIBITED` appears only in negative rules and checks, never as an executable
ledger row.

## Preserved debugger-fence semantics

The preserved fence can be classified as preserved only if all of these facts
remain true at execution time:

- exactly one sealed numeric PID, obtained as the direct child of the bound
  helper launch, is the target;
- the debugger is invoked through the system developer-tool launcher in batch
  mode against that exact PID and the exact freshly frozen script;
- capture is limited to the enumerated breakpoints and bounded backtraces;
- attach-to-detach elapsed time cannot exceed 150 seconds;
- the owner supplies the exact interrupt byte and subsequent detach and quit
  inputs in the same existing debugger PTY;
- there is no PID search, alternate target, retry, supervisor, input-forwarder,
  watchdog, privilege/entitlement change, memory inspection, environment
  inspection, or credential access.

A fresh static revalidation of the candidate script is required before
freeze. An unresolved breakpoint remains an `UNKNOWN` at execution; it is not
proof that the seam was not entered.

## Planning-baseline semantics for isolated sealed HOME

The accepted recipe supports only this planned structure:

- create a new absent fixed diagnostic root and a dedicated HOME beneath it;
- create a disposable login keychain in that HOME with the public empty
  passphrase used by the accepted feasibility recipe;
- do **not** issue a separate explicit unlock operation;
- bind isolated-HOME default and search-list readbacks to the single expected
  disposable keychain path before Electron launch;
- run only the hash-bound package under the isolated HOME and separately bound
  user-data path;
- treat any uncancelled prompt, search/default mismatch, unavailable
  encryption, credential request, owner-state drift, or unexpected keychain
  condition as a stop;
- retain diagnostic evidence on failure when the approved stop path requires
  it; delete only the explicitly disposable roots after the runbook's
  terminal and evidence-retention gates pass.

The planning baseline does not establish a universal keychain rule, does not
authorize the unsupported password-store bypass, and does not allow product
or package bytes to be patched to avoid safe storage.

## Command-by-command authority rules

1. Each shell command, debugger invocation, debugger input, signal-producing
   action, GUI launch action, evidence-producing action, and cleanup action is
   a separate ledger row with one exact literal representation.
2. Preconditions must bind the immediately required hash, absence, identity,
   direct-child, temporal, or prior-row success facts. A narrative phase gate
   is not a substitute for row-level preconditions.
3. `success_gate` states exact observable evidence. Silence is not success
   unless the exact command's contract defines an empty result and byte count.
4. `failure_route` is always fail-closed: stop operational progression,
   record the actual outcome/deviation, retain governed evidence, and perform
   only cleanup/rollback rows whose own preconditions are satisfied.
5. Cleanup is not ambient authority. Each removal, restoration, terminality
   check, and absence proof is separately enumerated and hash-bound.
6. Retries, alternate commands, new paths, new PIDs, changed debugger input,
   and manual recovery are prohibited unless they are independently present
   and approved in the frozen ledger.
7. A failed cleanup that leaves a live process or uncertain terminal state
   blocks destructive root deletion. The state is retained and returned for a
   new ruling.

## Evidence and epistemic semantics

- Machine bytes, owner attestations, and derived findings remain distinct.
- Exact stdout/stderr or transcript bytes are required where the runbook
  claims byte evidence; a conversational summary cannot replace missing raw
  bytes.
- Hashes bind only the bytes actually hashed. Historical package identity and
  topology are reconstruction targets, not current package bytes.
- A trace event supports only the seam it observes. Execution success does not
  establish a cause, remedy, product acceptance, lifecycle closure, release,
  or reliance.
- Missing output, unresolved symbols, timing uncertainty, skipped steps,
  operator deviation, redaction, and credential omission are explicit
  limitations, never silently normalized.
- Returned material containing a token, secret, keychain value, API key,
  memory dump, or environment dump is rejected from ordinary ingestion and
  routed to a separately governed credential-safe process.

## Mandatory stops and prohibited expansions

Stop before the next operational row on any of the following:

- source, dependency, archive, package, identity, topology, script, or runbook
  hash mismatch;
- missing local dependency or an attempted network fetch;
- package, helper, GUI, keychain, HOME, user-data, PID, or evidence path outside
  the exact frozen values;
- inability to prove the helper PID is the current sealed direct child;
- helper exit, PID mismatch/reuse concern, attach prompt, privilege or
  entitlement request, unresolved required debugger setup, timeout, or
  unexpected debugger state;
- any prompt other than the runbook's explicitly permitted cancel-only case;
- credential request or exposure, owner keychain/default/search-list drift,
  or unexpected Security/Keychain output;
- a first-signal, bounded-observation, stop, cleanup, rollback, terminality, or
  evidence-retention result that does not meet its exact gate;
- any operator deviation or need for an unenumerated command.

Explicitly prohibited expansions include network use, alternate package
sources, owner-keychain use, credential access, process census/PID search,
memory or environment dump, signing/notarization/distribution, persistent
security/entitlement changes, product-byte mutation, generic runtime repair,
release, reliance, Git mutation, Task Management, foreign-loop action, and
execution by an agent.

Authority-semantics result: `PASS — PREPARATION AND EXECUTION GATES SEPARATED; ALL FUTURE OPERATIONS REQUIRE EXACT FREEZE-HASH OWNER APPROVAL`.
