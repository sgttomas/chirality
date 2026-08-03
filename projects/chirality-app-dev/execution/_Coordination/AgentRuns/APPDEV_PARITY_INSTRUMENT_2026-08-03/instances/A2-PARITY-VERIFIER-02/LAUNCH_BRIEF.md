# Sealed Brief — A2-PARITY-VERIFIER-02

RequestedBy: `WI-PKG09-DAPP86-A`

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

ParentInstanceID: `WI-PKG09-DAPP86-A`

ChildInstanceID: `A2-PARITY-VERIFIER-02`

AgentType: fresh ephemeral Agent 2 generalist

Objective: perform a fresh, concise, read-only verification of the frozen
D-APP-86 Option A executor evidence and persist a durable terminal return.
This supersedes verifier 01 only because verifier 01 completed its assertions
but stalled twice before writing a return; verifier 01's messages are
non-acceptance provenance and must not be used as evidence for this verdict.

## Required reads

Read `AGENTS.md`, `agents/AGENT_TASK.md`, verifier 01's sealed
`LAUNCH_BRIEF.md`, the run-root activation/work graph/amendments, all six
run-root outputs, `EVIDENCE_INDEX.csv`, executor brief/return/TASK record and
indexed evidence, and the cited D-APP-86/88/89 packets, rulings, returns, and
handoffs. Do not rely on verifier 01's messages or unstated operator memory.

## Scope and prohibitions

Read-only repository inspection and deterministic hashing/parsing are allowed.
Do not launch, package, test, repair, mutate product state, delegate, access
secrets, or write anywhere except:

- `instances/A2-PARITY-VERIFIER-02/RETURN.md`
- run-root `A2_VERIFIER_RETURN.md`

## Exact assertions

Independently establish:

1. all 39 evidence-index rows exist and their SHA-256 values match;
2. source 380/380, package 446/446, 14 symlinks, executable/app.asar/plist
   hashes, arm64 and adhoc/unsigned identity match the frozen basis;
3. DOM/AX/PNG evidence proves Workbench, Pipeline, in-flight selection guard,
   post-completion selection, and exact read-only replay of the named session,
   2 events, 1 transcript item, and named terminal event;
4. replay identity is only `WORKING_ITEMS` / `agent1`, with no parent/child
   attribution present or inferred;
5. the complete validation ledger passes and truthfully retains the initial
   AF_UNIX path-length failure plus exact shorter-`TMPDIR` successful retry;
6. both temp roots and child residue are absent, owner daemon assets are
   untouched, and both dependency projections are restored exactly with no
   backup or Root diff attributable to the projection;
7. D-APP-89 remains zero ordinary consumers / 13 rollback probes / facade
   retained; D-APP-88 helper remains absent and a mandatory future parity
   rerun trigger;
8. exactly six D-APP-81 historical relations remain UNKNOWN at the recorded
   hash with no diff; and
9. D-APP-86 caused no product/config/test/document, foreign-loop, Git,
   receipt, Task Management, decision, pointer/status, authority,
   decomposition, SCOPE_CHANGE, lifecycle, signing/notarization/release,
   publication, or distribution write.

## Short return schema — mandatory

Write no more than 1,200 words. Use:

1. `Verdict: ACCEPT_FAN_IN | REJECT_FAN_IN`
2. one nine-row table: assertion, PASS/FAIL, exact evidence
3. `Limitations and rerun` (identity calibration and D-APP-88 trigger)
4. `Containment` (writes made and no-repair statement)
5. exact SHA-256 of the instance return, excluding any self-hash claim

The run-root copy must have identical substantive findings; a title/path note
may differ. Hash both, report both to the parent, and finish immediately.
Reject on any failed assertion; never repair.
