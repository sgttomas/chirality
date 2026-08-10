# Stage 6 — ledger alignment and completeness check

Status: `BLOCK — EXCLUDED_ROOT_SEARCH_SCOPE_VIOLATION`

Run: `APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09`

Ledger:
`source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv`, 42,705 bytes,
SHA-256 `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.

## Mechanical structure

| Check | Result |
|---|---|
| Stage fan-in | `PASS` — Stage 3 rows followed by Stage 4 rows are byte-field-equal to all Stage 5 rows |
| Row count | `PASS` — 80 command rows |
| Schema | `PASS` — exactly 13 required columns on every row |
| Namespace | `PASS` — contiguous `L3-CMD-001` through `L3-CMD-080` |
| Identity uniqueness | `PASS` — 80 distinct IDs; no gap, duplicate, alias, or external command identity |
| Required fields | `PASS` — no empty field on any row |
| Owner approval | `PASS` — every row states `YES — exact frozen-packet hash approval` |
| Failure routes | `PASS` — every row has a fail-closed route |
| Cleanup/rollback | `PASS` — every row has an explicit cleanup, rollback, retention, or no-effect disposition |
| Actors | `PASS` — only `owner-terminal`, `owner-gui`, and `owner-debugger-input` |
| Authority classes | `PASS` — only `OWNER_OPERATED_NEW`, `OWNER_OPERATED_PRESERVED_FENCE`, and `OWNER_ATTESTATION` |

## Exact historical-identity rejection

The manager-defined case-sensitive pattern set was applied to the final
ledger:

```text
C[0-9]{3,}
A3-OP-[0-9]{3}
R[0-9]+-C[0-9]{3,}
ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+
```

Exact result: `0 matches`; search exit `1`; stdout `0 bytes`.

The same pattern set returned `0 matches` independently for each of Stage 1,
Stage 2, Stage 3, Stage 4, and Stage 5. The three excluded blocked-root
basenames also returned `0 matches` in the final ledger. No excluded-root
content or blocked draft is cited by any row. That output-alignment fact does
not cure the run-scope violation recorded below.

## Coverage alignment

| Required coverage | Ledger alignment | Result |
|---|---|---|
| Preflight and path binding | exact shell/session paths, absent fixed roots, host capture | `PASS` |
| Fresh source reconstruction | eight-file rollback plus twelve-file retained candidate projection and exact hashes | `PASS` |
| Dependency projection | offline lockfile install, unchanged lock hash, complete dependency-tree capture | `PASS` |
| Local offline package construction | approved local archive hash/copy, exactly two temporary archive bindings, build and package with no-network gate | `PASS` |
| Identity and topology | five package-object hashes, helper public plist, relative framework symlinks | `PASS` |
| Sealed-HOME/keychain preparation | disposable HOME, login keychain creation, no explicit unlock, exact default/search readbacks | `PASS` |
| Helper and GUI launch | exact helper and GUI executables, same isolated HOME/userData posture, raw streams and recorded PIDs | `PASS` |
| Direct-child PID binding | persistent owner-shell PID, exact helper PID/PPID equality, no PID search or substitute | `PASS` |
| Debugger attach and input | exact system launcher, frozen script, same PTY, interrupt, detach, quit, 150-second fence | `PASS` |
| First signal | owner GUI sends exactly one graceful Quit to the traced bound PID; replay sends one exact TERM to its bound PID | `PASS` |
| Bounded observations | 15-second socket readiness, trace elapsed bound, exact child waits, socket absence, raw stdout/stderr and debugger transcript | `PASS` |
| Evidence returns | deterministic source manifest, external copy, independent returned-byte manifest | `PASS` |
| Stop/deviation retention | universal stop row, no retry/alternate PID/force signal, uncertain state retained | `PASS` |
| Cleanup and rollback | owner-state comparisons, isolated-keychain deletion/absence, exact source restoration, candidate/derivative removal, baseline and clean-status proof, fixed-root absence | `PASS` |
| Ingestion preparation | credential-safe evidence filter, two deterministic manifests, immutable external return root | `PASS` |
| Terminal status | exact no-causal/no-acceptance completion line | `PASS` |

## Authority and safety alignment

- The ledger contains no execution token. It is command text for a future
  frozen packet only.
- No row permits an agent, supervisor, second terminal, input forwarder,
  watchdog, retry, PID search, alternate target, force signal, or interactive
  repair.
- The preserved debugger fence is used only where direct-child provenance,
  frozen script bytes, capture scope, same-PTY inputs, and the 150-second
  maximum remain literal. Any variance routes to the stop row.
- The isolated keychain recipe contains no explicit unlock and no unsupported
  password-store bypass. Owner keychain state is read and compared only; the
  ledger includes no owner-keychain backstop write.
- No command performs a network fetch, credential lookup, memory/environment
  dump, signing/notarization, distribution, product acceptance, release,
  reliance, Task Management, or foreign-loop action.
- Exact destructive paths are fixed and narrow. Removal is held until live
  child terminality, evidence copy, owner-state, isolated-keychain, and
  rollback preconditions pass.

The prohibited-string scan over the final ledger returned zero hits for
explicit keychain unlock, the rejected password-store route, force-kill forms,
network clients, signing/notarization, generic-password lookup, process
environment capture, and environment-dump redirection.

## Exclusion-compliance incident

During Stage 3 discovery, a read-only `rg -l` command searched broadly under
`projects/chirality-app-dev` for retained candidate byte markers. Three
intended exclusion globs did not match the paths as written. The command's
returned path list included files inside all three absolute-exclusion blocked
roots. A content search necessarily read those files even though no excluded
content was displayed, cited, copied, or used in the ledger.

This violates the sealed brief's absolute read exclusion. The mechanical
ledger checks and zero-identity result remain useful preserved evidence, but
they cannot support N1 acceptance. There is no authorized child retry or
replacement in this lineage. N2 must remain held and the manager must close
the lineage blocked under the owner's prescribed discipline.

## N2 disposition

`HELD — DO NOT DISPATCH`. The following is retained only as a future rerun
contract and grants no downstream release:

1. freshly inspect and semantically revalidate the exact debugger script;
2. bind the packet's source, dependency, archive, expected package identity,
   topology, script, runbook, evidence-contract, and ledger hashes;
3. write no historical command identity or excluded-root basename;
4. expose the compound shell inputs as literal numbered steps without hiding
   any operation or branch;
5. freeze the exact Activity Monitor Quit action and exact debugger input
   bytes as owner actions, not automated translations; and
6. preserve the invariant that every execution step remains unauthorized
   until the owner approves the final frozen packet by its exact hash.

No packet byte, package, runtime, debugger, Security/Keychain operation,
helper/GUI action, signal, cleanup, or Git action was executed by N1.

Final N1 ledger verdict:
`BLOCK — MECHANICALLY COMPLETE ZERO-IDENTITY LEDGER PRESERVED, BUT N1 INVALIDATED BY ABSOLUTE-EXCLUSION SEARCH-SCOPE VIOLATION; N2 HELD`.
