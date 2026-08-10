# Sealed brief — D-APP-93 R4 pre-repair mechanical audit

RequestedBy: `WORKING_ITEMS`

RunID: `APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06`

ParentInstanceID: `WI-DAPP93-R4-PACKET-REPAIR-01`

ChildInstanceID: `A2-DAPP93-R4-MECHANICAL-AUDIT-01`

Agent form: fresh ephemeral Agent 2 generalist; read-only mechanical auditor;
must not delegate.

## One objective

Audit the unchanged R3 D-APP-93 owner-operated prepared packet exhaustively for
exactly two defect classes authorized by the owner:

1. a runbook branch invokes a command where that command's stated
   preconditions cannot hold on that branch; or
2. a declared required evidence byte/object has no enumerated capture command
   or no enumerated return/inclusion action.

Do not repair any prepared byte. Produce exhaustive matrices and bounded repair
recommendations using sequential new command IDs after C1145.

## Accepted immutable basis

- `MANAGER_FREEZE_R3.md` SHA-256
  `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963`;
- R3 verifier return SHA-256
  `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006`;
- R4 authority adoption SHA-256
  `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e`;
- work-graph amendment v1.5 SHA-256
  `e2bbe7d5b38ea14f24e068e25b22226d104ee285dcd3505ed0590575626381d5`.

The child must reproduce these four identities and all fourteen identities
bound by `MANAGER_FREEZE_R3.md` at entry and again immediately before return.
Any mismatch is a blocking return; do not continue semantic audit after an
entry mismatch.

## Declared reads

Read only:

- repository root `AGENTS.md`;
- `agents/AGENT_WORKING_ITEMS.md` only as parent-role context;
- this sealed brief;
- `R4_PACKET_REPAIR_AUTHORITY_ADOPTION.md`;
- `WORK_GRAPH_AMENDMENT_V1_5.md`;
- `MANAGER_FREEZE_R3.md` and every object it binds;
- `reviews/A2_DAPP93_OPTION_A_R3_VERIFIER_ONLY_RETURN.md`;
- all files under this run root's `prepared/` directory when needed to trace
  commands, branches, evidence requirements, hashes, ranges, tokens, and
  cross-references;
- prior immutable run-local control/review records only when required to test
  a cited precondition or accepted identity.

## Allowed tools

Static filesystem reads and deterministic text/hash analysis only, including
`rg`, `sed`, `awk`, `find`, `sort`, `comm`, `diff`, `shasum`, and read-only
shell composition. `apply_patch` may be used only to create the one terminal
return named below.

## Sole allowed write target

`instances/A2-DAPP93-R4-MECHANICAL-AUDIT-01/TERMINAL_RETURN.md`

No other file or byte may be created, modified, deleted, renamed, staged, or
committed.

## Required return

The terminal return must include:

1. entry and final hash-reproduction tables for all required identities;
2. an exhaustive branch/command/precondition matrix covering every runbook
   branch, every command invoked by that branch, the command's stated
   preconditions, whether each can hold at that point, and evidence/citation;
3. an exhaustive required-evidence matrix mapping every declared required
   byte/object to its literal capture command, immutable/hash-binding action,
   return/inclusion action, and exact consumer/validator; use `NONE` explicitly
   for absent links;
4. findings limited strictly to the two authorized defect classes, with exact
   citations, consequences, and minimal bounded repair recommendations;
5. a proposed single sequential command-ID allocation beginning at C1146 for
   every new operation required, with no gaps or reuse;
6. explicit confirmation of the three known defects: step disposition must
   cover step 31; the step-5 early-failure route must become a fail-closed
   pre-C196/pre-C197 evidence-preservation and cleanup path invoking neither
   C1144 nor C1130; complete C1105-C1108 outputs require hash-bound capture and
   return actions;
7. a final verdict of `AUDIT_COMPLETE_REPAIR_REQUIRED` or
   `AUDIT_BLOCKED_BASIS_DRIFT`.

Exhaustive means no sampled branches, commands, evidence rows, or inferred
ellipsis. Recommendations may name prepared/control files within owner scope,
but the child must not edit them.

## Exclusions

No runtime, debugger, LLDB, package/build, helper or GUI, signal, credential,
network, product, release, reliance, Git, Task Management, foreign-loop, or
other action. Do not execute any C-numbered command. Do not inspect live
processes, caches, credentials, evidence targets, or runtime state. Do not
repair, validate by execution, approve, present, or use any future execution
token. C196/C197 remain exact, valid, and unused; C1067 onward remain
unapproved.

## Escalation

Return blocked only for basis drift, unreadable declared source, inability to
produce exhaustive matrices, or pressure to cross the exclusions. Do not ask
the child to choose scope or authority.
