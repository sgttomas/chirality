# Sealed Agent 2 brief — v2 command-authority ledger author

RequestedBy: WORKING_ITEMS
RunID: `APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_V2_2026-08-09`
ParentInstanceID: `WI-PKG09-DAPP93-A3-V2-03`
ChildInstanceID: `A2-DAPP93-A3-V2-LEDGER-01`
PackageID: `PKG-09`
DeliverableID: `DEL-09-04`

## Objective

Author one exact new v2 `COMMAND_AUTHORITY_LEDGER.md` for a future owner-operated D-APP-93 attempt 3. This is new authorship, not recovery or continuity with the unrecoverable `8577...` ledger. Assign one new, unique, individually `OWNER_APPROVAL_REQUIRED` ID to every executable command and every operator input. Do not use inherited `C196`, `C197`, `C1067-C1157`, or any lost-A3 IDs.

## Accepted basis and declared reads

Read `ACTIVATION.md`, `WORK_GRAPH.md`, the accepted terminal D-APP-93/D-APP-94 lane handoff, ruled/verified D-APP-94 Final Posture Option A adoption records, accepted R8 recipe evidence, and intact R4.4.6 packet objects only as explicitly non-authoritative drafting aids. Read the sibling supporting artifacts after they appear only to ensure exact command/object alignment. Do not read or reconstruct a damaged prior draft as authority.

## Required ledger semantics

- Exact fixed root `/private/tmp/chirality-dapp93-owner-operated-attempt3-v2-20260809`; exact isolated HOME beneath it; exact returned destination under this run root at `returned_attempt3_v2`.
- Absence-first, fail-closed gates for fixed root and returned destination.
- D-APP-94 recipe exactly: `umask 077`; `HOME/Library/Keychains/login.keychain-db`; `security create-keychain -p ''`; no explicit `unlock-keychain`; no explicit default-keychain write; no explicit list-keychains/search-list write; synthesized default/search readback; prompt result must be `NONE` only; owner-state/backstop evidence; evidence commit before cleanup.
- All Electron/helper launches and user-data are under isolated HOME/user-data.
- A newly named fresh per-attempt C1118-equivalent evidence/action gate that blocks trace/signal until authenticated contact evidence is returned, hash-bound, and later validated. It is not authorized or satisfied here.
- Mandatory first-signal gate unchanged in substance.
- Copy/static-only LLDB script revalidation; the historical script may be source material but future copy/use requires a new v2 command ID and owner approval.
- Literal exhaustive runbook alignment; blank raw/derived evidence sidecars; complete failure routing; `PASS_COMPLETE` versus `STOP_INCOMPLETE`; commit-before-cleanup.
- Every operator keystroke/input including debugger attach/control inputs gets its own unique approval-required ID. No ranges may hide executable input.

## Allowed tools and writes

Allowed: static reads, text authoring, `rg`, `sed`, `awk`, `sha256sum`, parse/receipt/corpus checks. Do not execute any ledger command.
AllowedWriteTargets: `candidate/COMMAND_AUTHORITY_LEDGER.md` and `returns/A2_LEDGER_AUTHOR_RETURN.md` only.

## Expected return and acceptance

Return exact path, bytes, SHA-256, full first/last ID and count, proof of uniqueness, proof every executable/operator input is individually `OWNER_APPROVAL_REQUIRED`, fixed-root/return-destination counts, old-ID absence, lost-ledger non-continuity, and exact blocker or PASS. Stop after one complete authoring attempt/checkpoint.

## Exclusions

No delegation. No operational command; Security/Keychain/Electron/package/trace/debugger/LLDB/runtime/network/credential/fresh-contact act; token/index write or approval; product/frontend/source, decision/register/ruling, deliverable/status/memory, Task Management, Git, receipt, foreign-loop write; acceptance/reliance/release/lifecycle claim.
