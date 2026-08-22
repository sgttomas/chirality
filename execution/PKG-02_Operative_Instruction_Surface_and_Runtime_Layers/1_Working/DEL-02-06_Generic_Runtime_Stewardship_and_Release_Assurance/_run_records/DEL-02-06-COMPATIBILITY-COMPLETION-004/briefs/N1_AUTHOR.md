# Sealed brief — N1 author compatibility completion

RequestedBy: `N1-WORKING-ITEMS-DEL0206`
RunID: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`
ParentInstanceID: `N1-WORKING-ITEMS-DEL0206`
ChildInstanceID: `N1-AUTHOR-COMPATIBILITY-COMPLETION`
PackageID: `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`
DeliverableID: `DEL-02-06`

Objective: prepare one canonical JSON compatibility-completion candidate that
applies owner-supplied epoch `1` / identity `root-runtime-1` to the exact
accepted six-member semantic basis and contains every binding field required
by the accepted compatibility member, using explicit honest held/unavailable
states wherever a later gate has not supplied accepted evidence.

AcceptedBasis: repository
`1b375af4f1219ecfc00fc2755854aa7fd4220901`; accepted Scope of Work
`dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`;
accepted semantic snapshot
`3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`;
accepted six-member package manifest
`6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`.

Dependencies: manager acceptance of N0 basis reproduction.

DeclaredReads: DEL-02-06 `ScopeOfWork.md`, `_STATUS.md`, `_DEPENDENCIES.md`,
all existing run records, the activation record and work graph in this run,
the 2026-08-21 authorization handoff, and tracked-tree collision evidence.

AllowedTools: read, search, SHA-256 and JSON parsing/serialization checks, and
file writing. No network. No software implementation or product check.

AllowedWriteTargets:

- `author/RETURN.md`
- `candidate/COMPATIBILITY_COMPLETION_CANDIDATE.json`

ExpectedOutputs: exact canonical candidate bytes and SHA-256 plus an author
return mapping each of the accepted compatibility member's eight binding
groups to a populated value or a named `HELD_UNAVAILABLE` blocker.

AcceptanceCriteria:

1. epoch is canonical positive decimal `1` and identity is exactly
   `root-runtime-1`;
2. all six accepted member paths and SHA-256 values plus the exact sorted
   six-member package-manifest identity are present;
3. source and release identities; every accepted affected-client basis and
   exact operation; conformance/migration evidence; Root regression evidence;
   census, Tier-0, PEC, notice and findings; cutover/rollback/replay/
   indeterminate disposition; and semantic/implementation/cutover/release
   acts each appear exactly once as structured groups;
4. unavailable later-gate values are `HELD_UNAVAILABLE` with null identity,
   exact reason, owner, gate, and blocking posture; none is guessed;
5. historical accepted members are unchanged; and
6. candidate status is preparation-only and expressly unaccepted.

EXCLUSIONS: acceptance, historical-member edits, implementation, lifecycle,
release, publication, reliance, foreign-loop writes, register disposition,
Git, PR, or merge. This Agent 2 must not delegate.

Escalation: return any missing required group, ambiguous accepted basis,
collision, reserved value, or need for invented data to the parent without
repairing outside the declared targets.
