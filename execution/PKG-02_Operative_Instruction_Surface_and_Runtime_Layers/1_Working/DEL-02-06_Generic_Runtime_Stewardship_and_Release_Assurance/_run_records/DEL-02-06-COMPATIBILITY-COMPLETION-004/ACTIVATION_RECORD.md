# Activation record — DEL-02-06 compatibility completion 004

- Manager: `WORKING_ITEMS` Agent 1
- Parent run: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`
- Manager instance: `N1-WORKING-ITEMS-DEL0206`
- Package: `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`
- Selected deliverable: `DEL-02-06` only
- Context envelope: `M`
- Repository basis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Accepted Scope of Work SHA-256:
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
- Accepted semantic snapshot SHA-256:
  `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`
- Owner authority: E1 ruling recorded in
  `execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/DEL02_PREPARATION_AUTHORIZATION_HANDOFF.md`
- Owner-supplied epoch and candidate identity: `1` / `root-runtime-1`
- Posture: `MIXED`

## Objective and completion boundary

Reproduce the accepted six-member semantic basis without altering it; prepare
one exact compatibility-completion candidate that applies epoch `1` and
contains every binding field required by the accepted compatibility member;
preserve honest `HELD_UNAVAILABLE` states; validate identity, member hashes,
completeness, determinism, collision, reserved-value, authority, and write
containment; obtain a fresh read-only refutation; and return the exact bytes
and SHA-256 for a later accountable-human acceptance decision.

Preparation and validation do not accept the candidate. Runtime or client
implementation, contract repinning, lifecycle change, release, publication,
reliance, foreign-loop writes, register disposition, Git commit, push, PR, or
merge are excluded.

## Declared reads

- Root `AGENTS.md` and `agents/AGENT_WORKING_ITEMS.md`.
- Complete DEL-02-06 Scope of Work, status, context, references, dependencies,
  semantic lens, memory, and existing run records.
- The 2026-08-21 authorization handoff and its cited accepted snapshot.
- Deterministic local validation tools and tracked-tree identity evidence.

## Declared writes

- This immutable run root.
- DEL-02-06 `_STATUS.md`, only to record this owner-authorized activation and
  dispose REM-001 without changing `INITIALIZED`.
- The supervising instance directory, only for durable `STATUS.md` and
  `RETURN.md`.

No anticipated write locus is treated as authority.

## Dependency and profile state

- `_DEPENDENCIES.md`: no declared upstream or downstream edge.
- Root-local `software-workflow.json`: absent at activation.
- No implementation or registered software check is authorized or invoked.
- Child form: bounded ephemeral Agent 2 generalists; Agent 2 delegation is
  prohibited.

## Return gate

The manager may return the prepared bytes only after deterministic validation
and one fresh refuter return. Any required binding that lacks accepted bytes
or evidence remains a named blocker; it is never invented. The next owner is
the accountable human deciding whether to accept or return the exact prepared
candidate bytes.
