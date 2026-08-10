# D-APP-94 Option C R5 isolated-HOME feasibility-probe packet

Status: `FROZEN R5 CANDIDATE — OWNER APPROVAL AND ONE FRESH VERIFIER PASS REQUIRED`

Purpose: retest the narrow bare-Electron 43.2.0 safeStorage feasibility question
using the host/session HOME-resolution behavior discovered by R4, without
reusing or altering any R4 namespace or making ordinary owner-domain writes.

## Accepted discovery and predecessor disposition

- R4 discovery intake:
  `R4_PRECONDITION_DISCOVERY_INTAKE.md`, SHA-256
  `962aa7135fcda412169e9477e5c57da517bd2dcf383084d2d7f24691646a5bf7`;
- R4/predecessor disposition:
  `PREDECESSOR_NAMESPACE_DISPOSITION_R5.md`, SHA-256
  `2f4b3e4f666443c1e5f9c370279fc8e6ae2ba538476296ed611acfc8ea134d1e`;
- frozen R4 chain remains anchored by driver
  `1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538`,
  freeze `47d39a4512816adddae5def9f79453c9b7c724f08dcc4f406815314c85f646ef`,
  and fresh-verifier PASS
  `09937b21d205702b33bbdadf7c426a591a202aeb6f299684895cd5ac56dcd829`.

On this exact host/session, accepted bytes show owner HOME default/search both
equal the one-element login keychain baseline, while isolated HOME default
exited 1 with exact no-default stderr and isolated HOME search exited 0 empty.
This calibrates R5 only; it is not a universal macOS semantics claim.

## New namespaces and driver

- R5 root:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809`;
- R5 HOME:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809/home`;
- R5 keychain:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809/home/Library/Keychains/dapp94-option-c-r5.keychain-db`;
- R5 userData:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809/user`;
- sibling return:
  `execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned_r5/`;
- R5 driver:
  `prepared/run-dapp94-option-c-probe-r5.zsh`, SHA-256
  `5f7cf2830679a0fb07ff26f6b7642d4d133347512af337cdcabffdc2b8a23d4a`.

Both R5 namespaces must be absent. The retained R4 root and current `returned/`
remain untouched and are not absence gates.

## Domain separation

Every R5 isolated-domain default/search observation, create, unlock,
default/search bind, and delete command is an explicit
`/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$PROBE_HOME" /usr/bin/security ...`
invocation. The driver first reproduces the accepted isolated-HOME no-default/
empty-search tuple before creation, then binds and observes only the R5
keychain within that HOME.

Plain owner-domain `security` calls are limited to:

1. pre-probe raw default/search observations and byte comparisons;
2. one signal-safe post-probe/failure raw default/search drift check;
3. the backstop set/verify sequence only after both observations succeed and
   at least one byte comparison is exactly mismatch status 1.

Observation or comparison error is not proven drift and authorizes no owner
write. Matching owner state records `NOT_NEEDED`; ordinary failure and signal
routes then retain R5 state without writing owner domain. The backstop is
single-owner, signal-excluded, non-reentrant, and terminally blocks retry. Any
backstop use makes the attempt non-passing and retains all R5 state.

## Probe, prompt, and material classification

The driver preserves the hash-bound public Electron 43.2.0 archive, executable
member, activation-policy-prohibited probe source, public constant, and one
encrypt/decrypt round trip. It launches no Chirality product byte and creates
no GUI window. Literal `-p ''` is public zero-length mechanics; any generated
safeStorage item is disposable cryptographic probe state, never owner/provider
credential material.

If any system prompt appears, the owner approves nothing, enters nothing, and
selects Cancel only. After control returns the only script input is `NONE` or
`SHOWN_CANCELLED`. Cancellation routes to owner drift check and retained R5
state. If cancellation does not return control, the owner performs no signal,
retry, inspection, or fallback action and reports held state.

## Success and failure order

Success requires probe checks, owner-domain after-check exact MATCH, and
`BACKSTOP_STATE=NOT_NEEDED`. The driver then copies/hashes all raw evidence to
`returned_r5/`; rechecks the same state variables; deletes only the isolated
keychain through the exact isolated HOME; proves absence; removes only the R5
root; and hashes cleanup evidence.

Every failure retains R5 state. No owner-domain write occurs absent proven
drift. No product, package, trace, C1114/C1117, C196/C197, debugger, credential,
network, reliance, Git, Task Management, foreign-loop, or other authority is
included.
