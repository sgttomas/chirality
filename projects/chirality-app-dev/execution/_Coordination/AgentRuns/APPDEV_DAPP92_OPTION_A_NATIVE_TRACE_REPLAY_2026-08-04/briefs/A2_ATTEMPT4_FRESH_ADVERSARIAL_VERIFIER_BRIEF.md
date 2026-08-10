# Fresh Agent 2 adversarial verifier brief — D-APP-92 Attempt 4

RequestedBy: `WORKING_ITEMS`
RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
ParentInstanceID: `WI-DAPP92-A-ATTEMPT4-01`
ChildInstanceID: `A2-DAPP92-A-ATTEMPT4-VERIFY-01`
PackageID: `PKG-09`
DeliverableID: `DEL-09-04`
Role: `FRESH EVIDENCE-ONLY EPHEMERAL GENERALIST`

## Objective

Adversarially verify the current Attempt-4 bytes and terminal state without
repairing or extending them. Determine whether the attempt lawfully consumed
exactly the owner-approved scope, truthfully bounds the observed C198 failure,
fully cleaned up, and is fit for terminal manager acceptance and a Receipt-123
closeout.

## Accepted basis

- exact owner token in `OWNER_ATTEMPT4_COMMAND_APPROVAL_ADOPTION.md`;
- adopted `COMMAND_REGISTER_AMENDMENT_V1_12.md` and its immutable proposed
  predecessor;
- `briefs/A2_ATTEMPT4_PACKAGE_EXECUTION_BRIEF.md`;
- Attempt-4 author outputs with pre-dispatch SHA-256 identities:
  - `evidence/attempt4/C198_STDOUT_STDERR.txt`:
    `41398a7cee7654a9fad224d6c478dcabd81890d2646917819213f45844ab65bf`;
  - `evidence/attempt4/COMMAND_OUTCOMES.md`:
    `bcaf366f4eeb30d8af1a40ec6b14e4a1c008f5ac5607becbe9630a20e66725fd`;
  - `evidence/attempt4/CLEANUP_PROOF.md`:
    `94a4e5192efe8ab3f192361e9bef8b6fabca941a2150cf5d9b6d9e1ae22329ac`;
  - `instances/A2-DAPP92-A-ATTEMPT4-EXECUTE-01/TERMINAL_RETURN.md`:
    `f4d303796f8723b35f93c1b990a25c17dae555370f982e260252e4d1e40b807e`.

## Declared reads and allowed tools

Read all cited run-local artifacts and exact governed frontend baseline files.
Use only read-only shell tools needed for hashing, text/search inspection,
path-absence checks, Git status/diff inspection, receipt validation,
candidate-whitespace validation, and App-only write-containment assessment.
Do not run build/package/runtime/frontend tests; the author already restored
and removed their dependencies. Do not access owner caches or credentials.

AllowedWriteTargets:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT4_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`

## Required adversarial checks

1. Recompute every bound author-output hash and fail on drift.
2. Confirm the adoption transcribes the exact direct owner token and releases
   only C207-C209 plus one byte-identical C198 retry, while the adopted graph
   retains existing reconstruction/identity-read/mandatory-cleanup authority.
3. Confirm C207-C209 paths/namespace/archive hash and C198 bytes are exact;
   seek evidence of more than one Attempt-4 C198 invocation, any fifth retry,
   or any invented recovery.
4. Inspect the raw C198 bytes. State the strongest supported root-cause
   boundary and reject any stronger inference. Confirm the claimed sequence
   (`packaging ... Electron 43.2.0` then `getaddrinfo ENOTFOUND github.com`) and
   that C179-C184 were correctly skipped.
5. Verify all eight current frontend hashes, absence of the five candidate
   additions, named generated/dependency paths, and fixed temporary root;
   confirm exact frontend Git status is empty.
6. Search current Attempt-4 evidence for any helper/GUI launch, PID/process,
   LLDB/debugger, signal, replay, memory/environment/credential, release,
   Git-mutation, TM, foreign-loop, successful network, or package-identity
   overclaim. Distinguish the failed DNS attempt from a successful network
   effect.
7. Run the receipt validator on the current pre-Receipt-123 ledger; run the
   full-App candidate-whitespace validator against base
   `7aada3fbadf340a07ef828cc18b350c8c01b517d`; run `git diff --check`; and
   assess write containment. Report exact command/outcome evidence.
8. Verify prior Attempt-3 artifacts named by Receipt 122 remain present and
   that Attempt-4 did not overwrite them.

## Verdict contract

Return exactly one verdict:

- `PASS_FOR_TERMINAL_CLOSEOUT` only if every required check passes and the
  evidence is fit for terminal manager acceptance; or
- `BLOCK` with precise defects and no repair.

Regardless of verdict, state that no fifth retry, cache guess, network,
runtime, debugger, signal, replay, product remedy, release, Git, TM, or
foreign-loop authority follows.
