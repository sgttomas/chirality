# Agent 2 brief — D-APP-93 R4.4.6 successor fresh verifier

Status: `SEALED — READ-ONLY ADVERSARIAL VERIFICATION`

## Purpose

Independently audit the immutable R4.4.6 D-APP-93 overlay and successor
return-namespace freeze. Return exactly one evidence-first `PASS` or `BLOCK`.
Do not repair, execute, reinterpret authority, or create another agent.

## Accepted basis

- predecessor R4.4.5 freeze:
  `ddfbf431772526df6f884474c0dad84d57ce7c7aacede73ec72c4ed5751670c4`;
- predecessor fresh-verifier PASS:
  `fffd3c4f56162e3624dfca5ad012c4af4af209dbd349271a82bd344c9d7268bb`;
- failed-attempt derivative intake freeze:
  `012ce18778b90798624a3491657e80d5238c7e04d984c6994c46364c0bcd0d91`,
  verdict `STOP_INCOMPLETE`;
- owner namespace-rebind adoption:
  `4a824367f52148bdfe9fc0d9034abd0cd545bda7cf842e3aef42f11f78a56c9d`;
- candidate successor freeze:
  `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89`.

Run directory:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06`.

## Mandatory checks

1. Reproduce the candidate freeze and every identity it binds before any
   substantive review and again immediately before the return.
2. Reproduce the accepted `returned/` snapshot as exactly 28 files, all 14
   primary/sidecar pairs, and aggregate identity
   `ea52c8ee03ba3e5cd0ce04013885aae35d3ac283026f5ca4a42626e95a81d618`.
   Confirm no accepted returned or intake byte changed.
3. Prove `returned_r4_4_6/` and
   `/private/tmp/chirality-dapp93-owner-operated-20260807` are absent.
4. Enumerate every live successor returned-path literal. Require exactly 89
   full-path occurrences targeting only `returned_r4_4_6/`, zero exact live
   predecessor `returned/` paths, coherent absence/copy/export/form/sidecar
   ordering, and no reference that would overwrite accepted evidence.
5. Audit every operational fixed-root/archive/config literal. Require the
   D-APP-93 fixed root everywhere, zero D-APP-92 temporary-root literals, and
   explicit classification of preserved D-APP-92 C196/LLDB-script provenance
   as intentional and byte-exact rather than stale.
6. Recompute the D-APP-93 overlay SHA-256 and independently derive its two
   post-overlay configuration hashes from the frozen pre-overlay candidates
   without touching the frontend. Require the overlay method delta to be only
   the current fixed-root value plus mechanically updated embedded hashes.
7. Prove C1102 changes only its script operand relative to the accepted
   predecessor; prove C196/C197, SHA-720AD198 script, every non-return-path
   command byte, the ordinary C1145→C1144→C1130 order, pre-C196 paths,
   terminal cut, raw-packet semantics, and failure routes remain exact.
8. Re-run the absolute executable/host-path audit and verify every live
   prepared index/token/manifest/runbook/evidence/ingestion/inventory/matrix
   cross-reference is coherent with the successor namespace and overlay.
9. Confirm the future token is withheld/unapproved, frontend is clean, fixed
   roots are absent, whitespace/diff checks pass, and all writes are confined
   to the App run directory.
10. Treat any missing identity, stale/ambiguous path, hidden overwrite,
    unbound command delta, unsatisfied route precondition, token inconsistency,
    or freeze drift as material `BLOCK`.

## Authority boundary

Read-only verification plus the sole return write below. No repair, runtime,
debugger, package, helper/GUI, signal, credential, product, release, reliance,
Git, Task Management, foreign-loop, network, or other action is authorized.

## Sole write target

`reviews/A2_DAPP93_R4_4_6_SUCCESSOR_FRESH_VERIFIER_RETURN.md`

The return must state the exact verdict, evidence for every mandatory check,
initial and final candidate-freeze/hash stability, limitations, sole-write
attestation, and its own SHA-256. Stop immediately after that write.
