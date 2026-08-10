# Sealed Agent 2 brief — D-APP-93 Option A packet author

RequestedBy: `WORKING_ITEMS`

RunID: `APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06`

ParentInstanceID: `WI-DAPP93-A-PREPARE-01`

ChildInstanceID: `A2-DAPP93-A-PREPARE-01`

PackageID: `PKG-09`

DeliverableID: `DEL-09-04`

## One objective

Author a complete, internally consistent, preparation-only D-APP-93 Option A
owner-operated diagnostic packet. It must be literal enough for the owner to
execute later after a fresh explicit command grant, but it authorizes and
executes nothing now.

## Governing basis to read before writing

Read root `AGENTS.md`, `agents/AGENT_TASK.md`, the selected committed App loop
workplan, and these exact live inputs:

- `execution/_Coordination/_DECISIONS/D-APP-93_PACKET_SIMPLER_DIAGNOSTIC_ARCHITECTURE_2026-08-06.md`;
- `execution/_Coordination/_DECISIONS/D-APP-93_RULING_OWNER_OPERATED_INTERACTIVE_EXECUTION_ARCHITECTURE_2026-08-06.md`;
- `execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_RULING_ADOPTION_2026-08-06/HANDOFF_STATE.md`;
- `loop/LOOP_RECEIPTS.md`, Receipt 133;
- D-APP-92 run `HANDOFF_STATE_R4.md`, `MANAGER_RETURN_R4.md`,
  `reviews/A2_ATTEMPT5_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`, adopted command
  amendment v1.13, its Attempt-5 overlay script, and relevant source/package
  manifests;
- D-APP-92 run `reviews/A2_ATTEMPT7_FRESH_ADVERSARIAL_VERIFIER_RETURN.md` and
  accepted Attempt-7 ordering evidence;
- D-APP-92 run `OWNER_COMMAND_APPROVAL_ADOPTION.md` and
  `reviews/A2_FRESH_ADVERSARIAL_VERIFIER_RETURN_R2.md`;
- D-APP-92 run `trace/lldb-signal-trace.txt`; and
- the D-APP-88 R2 candidate-source tree cited by Attempt 5.

All paths are relative to `projects/chirality-app-dev` except root instruction
files. Recompute every cited current-file SHA-256. Static reads, hashing, text
search, syntax inspection, and absence checks are allowed. Do not invoke
LLDB, a package manager, build tool, archive extractor, helper, GUI, signal,
network client, or product test.

## Allowed tools and write targets

Allowed tools: read-only shell inspection and hashing; `apply_patch` for
documents and a self-contained copy of the existing text LLDB script.

AllowedWriteTargets:

- `execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/prepared/**`;
- `execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/instances/A2-DAPP93-A-PREPARE-01/TERMINAL_RETURN.md`.

Do not write the brief, activation, work graph, manager files, reviews,
Receipt 134, the decision register, decisions, other runs, frontend, or any
foreign-loop path. Do not delegate.

## Required frozen candidate outputs

Produce all of these:

1. `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` — bind every existing
   candidate-source input and baseline/lock input by current full SHA-256;
   exact local Electron 43.2.0 archive path/hash/size; accepted local
   `electronDist` overlay script path/hash and exact pre/post hashes; expected
   package paths, identities, topology, symlink and package-hash fields;
   absence of old package/build trees and missing raw C216 stream; literal
   future reconstruction/package/identity/cleanup commands and cwd; stop on
   every mismatch. State that this is a recipe/expected manifest, not an
   existing package, and no package/build tree is created in this tranche.
2. `prepared/lldb-signal-trace.txt` — a self-contained byte-identical copy of
   the current script unless static review proves a defect. The task does not
   authorize a semantic revision; if a defect is found, stop and report it
   rather than changing command meaning.
3. `prepared/LLDB_STATIC_REVALIDATION.md` — reproduce old and copied script
   hashes, parse every command block statically, enumerate the five breakpoint
   intents and 16-frame bound, state symbol-resolution limits, bind exact C196
   and C197 semantics, and expressly state that no debugger or target was
   invoked and breakpoint resolution remains unknown until the future run.
4. `prepared/OWNER_OPERATED_RUNBOOK.md` — a literal numbered runbook. The
   owner personally operates one interactive GUI/terminal session; no agent
   automation, forwarding program, watchdog, supervisor, sentinel protocol,
   or second-session coordinator. It must cover: preflight and hashes;
   temporary reconstruction; dependency projection; static/focused checks;
   one package invocation; package binding; GUI-session helper and GUI launch;
   sealed direct-child helper PID capture/binding without name search;
   same-owner-session LLDB C196; proof that all enumerated breakpoints loaded
   and target resumed; absolute monotonic 150-second attach-to-detach deadline;
   the exact first `SIGTERM` only at the ruled step; bounded observations;
   same existing LLDB PTY exact C197 input (`ETX`, then exact bytes
   `process detach\nquit\n`); terminal proof; evidence freeze; cleanup; D-APP-89
   rollback; post-cleanup hashes and absence. Every step needs exact command,
   cwd, expected record, pass condition, stop/deviation path, and authority ID.
   Any stale/wrong PID, target exit, identity mismatch, unexpected prompt,
   unresolved mandatory breakpoint, elapsed deadline, debugger state, missing
   byte, credential-bearing output, or operator deviation stops forward
   execution. After attach begins, detach remains mandatory before the bound
   whenever safely possible. Do not claim any execution is approved merely
   because it is written here.
5. `prepared/EVIDENCE_RETURN_PACKET.md` — a fillable schema, file inventory,
   exact hashes, raw transcript requirements, UTC and monotonic timestamps,
   numeric PID/direct-child evidence, package/public identity/topology, first
   signal, bounded poll/teardown/Root-stop/socket/owner observations, terminal
   state, cleanup/rollback, retained-evidence manifest, credential exclusion,
   deviations, missing bytes, unresolved symbols, and limitations. Templates
   remain blank; never fabricate an outcome.
6. `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` — later App
   loop intake checks, credential-safe rejection/redaction posture, exact hash
   and ordering checks, deviation disposition, a supported/contradicted/
   unknown causal-matrix template, and the mandatory fresh post-execution
   adversarial verifier. Execution never equals acceptance.
7. `prepared/COMMAND_AUTHORITY_LEDGER.md` — assign new sequential IDs starting
   at `C1067` to every future operation, including every read, write, copy,
   symlink, test/build/package, launch, PID record, snapshot, LLDB-adjacent
   check, first signal, poll/sleep, evidence copy/hash, termination, deletion,
   and rollback action. Each row must give exact literal command or exact
   operator input, cwd/session, dynamic-placeholder provenance, class, current
   authority state, purpose, pass/stop condition. Preserve historical C196 and
   C197 as exact separate rows marked `OWNER_APPROVED — VALID — UNUSED` only
   if their literal semantics are unchanged. All C1067+ rows are
   `OWNER_APPROVAL_REQUIRED`; do not infer authority from Attempt 5, Attempt 7,
   D-APP-93, or C196/C197.
8. `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` — concise decision-ready
   exact token covering the complete enumerated C1067+ range and preserved
   exact C196/C197 semantics. The request must state that the current packet
   authorizes nothing and execution may begin only after the owner returns the
   exact token. No generic, implicit, or partial authority.
9. `prepared/PREPARED_PACKET_INDEX.md` — list every prepared object, purpose,
   dependency, pending manager hash placeholder, and no-effect boundary.
10. `instances/A2-DAPP93-A-PREPARE-01/TERMINAL_RETURN.md` — report coverage,
   exact paths, static checks, current hashes where computable, limitations,
   authority calibration, exclusions, and manager-freeze readiness.

## Required truth calibration

- No Attempt-5 package artifact survives. Old package/build trees are absent
  and raw C216 stdout/stderr bytes are unavailable. Attempt 5 preserves only
  accepted offline reconstruction method and contemporaneously recorded
  identity/topology/cleanup evidence. Fresh output hashes remain expected,
  not actual.
- Attempt 7 preserves only historical mock timing/order direct-child
  PID/sentinel evidence. It proves no Electron/runtime/attach/signal behavior
  and its two-session sentinel protocol is not part of Option A.
- The historical script's recorded SHA is
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`;
  reproduce it and statically revalidate it before copying/reusing it.
- C196/C197 exact approval is valid, exact, unused, and consumable only when
  literal sealed direct-child, same-PTY, exact-input, enumerated-capture, and
  absolute 150-second semantics are preserved. It supplies no PID search,
  launch, signal, package, evidence, cleanup, watchdog, forwarding, process,
  or other authority.
- D-APP-88 and DEL-09-04 remain open; TM-APP-036 remains unfired; D-APP-89 is
  the operative rolled-back baseline; no product, remedy, causal, first-signal,
  lifecycle, release, or reliance effect occurs.

## Hard exclusions

No runtime, LLDB/debugger invocation, attach, package/build invocation or
artifact, helper/GUI launch, signal, replay, network, credential access,
memory/environment dump, process inspection, product/source/config/test edit,
acceptance, release, reliance, Git action, Task Management, or foreign-loop
action. Do not execute any future command that the packet enumerates.

## Acceptance and escalation

The packet must be internally literal and exact, with no unbound authority
claim, no fabricated evidence, and no hidden operational step. Stop and report
`BLOCKED` if exact commands or identity sources cannot be made unambiguous
without executing, if the script requires semantic change, or if any output
would exceed this preparation-only authority. Otherwise return
`READY_FOR_MANAGER_FREEZE` and stop before manager hashing.
