# Sealed brief — N1 accepted-source and command-surface reconstruction

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_DAPP93_FRESH_PACKET_AUTHORING_2026-08-09`
- ParentInstanceID: `WI-PKG09-DAPP93-FRESH-01`
- ChildInstanceID: `A2-DAPP93-FRESH-SOURCE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- Objective: independently reconstruct the accepted pre-attempt-3 authority and
  evidence basis and the complete command/operator surface needed by a wholly
  fresh packet, without authoring packet commands.
- ScopePath: the run root plus declared accepted source paths discovered from
  D-APP-92/93/94 and their accepted handoffs.
- AcceptedBasis: `ACTIVATION.md`, `WORK_GRAPH.md`, current live D-APP-92/93/94
  register rows and exact packet/ruling records, DEL-09-04 `ScopeOfWork.md`,
  `_STATUS.md`, dependencies and accepted evidence explicitly cited by those
  authorities.
- Dependencies: none.

## Exclusions

Do not read, open, inspect, semantically diff, quote, copy, or rely on either
blocked attempt-3 root's `prepared/**`, `candidate/**`, `briefs/**`, `returns/**`,
author working bytes, or lost/deleted ledger material. Only the terminal
handoff/manager-validation/runtime-summary files named in `ACTIVATION.md` and
Receipt 146 may be read for exclusion and recorded digest constraints.
Mechanical whole-root path/size/SHA-256 inventory is allowed only to prove
non-mutation; do not surface excluded content.

## Declared reads and tools

- Read-only repository inspection, `rg`, `find`, `sha256sum`/`shasum -a 256`,
  `stat`, strict JSON parsing, and Git read-only object/status commands.
- No network, GUI, runtime, package, build, script execution from accepted
  packet sources, debugger/LLDB, Security/Keychain, Electron, signal/trace,
  credential, C1118, product, release, receipt, register, Task Management,
  Git mutation, or foreign-loop action.

## Allowed write targets

- `source_reconstruction/**`
- `returns/N1_SOURCE_RECONSTRUCTION_RETURN.md`

## Expected outputs

1. `source_reconstruction/ACCEPTED_SOURCE_LEDGER.tsv` with repo-relative path,
   size, SHA-256, acceptance status, authority role, and citation route.
2. `source_reconstruction/COMMAND_SURFACE_REQUIREMENTS.md` enumerating every
   required command class and every operator-input class separately, source-
   cited, without assigning command IDs or executable bytes.
3. `source_reconstruction/HISTORICAL_COMMAND_ID_EXCLUSIONS.txt` containing all
   historical command identities that the completed packet must not contain;
   derive these only from accepted pre-attempt-3 sources and the allowed
   terminal blocked records, never excluded drafts.
4. `source_reconstruction/OLD_ROOT_INVENTORY_BEFORE.tsv` and
   `source_reconstruction/OLD_ROOT_PRESERVATION_BEFORE.md`, using a sorted
   `root-relative-path<TAB>bytes<TAB>sha256` inventory and SHA-256 of exact TSV
   bytes for each old root.
5. `returns/N1_SOURCE_RECONSTRUCTION_RETURN.md` with PASS/BLOCK, counts, hashes,
   unresolved contradictions, and explicit confirmation that excluded bytes
   were not content inputs.

## Acceptance criteria and escalation

Every accepted source is independently hash-verified and its acceptance route
is explicit. Command/operator requirements are complete enough for a ledger
author to enumerate individually. Any missing authority, ambiguity, need for an
excluded source, hash mismatch, or inability to prove old-root inventory is an
immediate `BLOCK`; write the terminal return and stop. Do not delegate.
