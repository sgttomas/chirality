# N1 return — accepted-turn recovery inventory

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N1`
- Runtime identity: `/root/w1_del0206/n1_w6`
- Parent runtime identity: `/root/w1_del0206`
- Form: fresh bounded ephemeral Agent 2 generalist
- Verdict: `ACCEPT_FOR_N4`
- Date: `2026-08-03`

## Input validation

| Input | SHA-256 | Result |
|---|---|---|
| `briefs/N1.md` | `719b0094793bf657ac4755b9d94db3df56f042723210520fd30c9a55ad698116` | Matches sealed wrapper |
| W6 child `LAUNCH_BRIEF.md` | `d85f34226d9cbed10a207dafd0465fdc8b16b082914417633dd57e7d3f33c4ce` | Read in full |
| `ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | Accepted read item 4 resolved |
| `READ_SCOPE_AMENDMENT_1.md` | `01320cbe83e72fbcf7861bb30651654904764d27f3200b56ff4e118764331206` | Eleven added read-only paths resolved |
| `basis/N0_R2_RETURN.md` | `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522` | Matches accepted dependency |
| `basis/BASIS_REPORT_R2.json` | `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8` | Parsed; verdict `RELEASE_N1_N2_N3`, 26/26 PASS, zero findings |

## Output

| Output | SHA-256 | Result |
|---|---|---|
| `inventory/N1_INVENTORY.md` | `f4b6039095fa0b7f98d83969fdab29c351d59ee31e43cdb5eb23cd5fa242dcc0` | Complete current-state matrix, contradiction list, gaps, source coverage, and proposal-only affected paths |

## Findings

1. `N1-F01` — The declared daemon startup path begins listening without a
   session/event scan for durable `turn.accepted` entries lacking every one of
   `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted`.
2. `N1-F02` — Ordinary and governed Agent 1 admission use memory-only active
   reservations and do not inspect durable accepted-without-terminal residue.
3. `N1-F03` — Current persistence has exact-event-ID suppression but no
   turn-level idempotent reconciliation or crash-residue terminal producer.
4. `N1-F04` — Local residency drain accounting is memory-only and is not
   reconstructed from durable session history after restart.
5. `N1-F05` — Client and CLI transport failures cannot distinguish a request
   that never reached acceptance from one durably accepted with unknown
   completion; neither surface silently retries or replays.
6. `N1-F06` — Replay is descriptive and does not reconcile event truth with
   session or governed-run summary state.
7. `N1-F07` — The general runtime event vocabulary omits `turn.cancelled`, the
   harness vocabulary includes it, and session summary status collapses it to
   `failed`; all four terminal event types must remain explicit in later work.
8. `N1-F08` — Existing declared tests prove same-process lock, failure,
   disconnect/interruption, and model drain behavior, but not crash/restart
   reconciliation, durable drain reconstruction, or repeated-reconciliation
   idempotency.

No evidence of an existing accepted-turn reconciliation mechanism was found in
the declared read set. The result does not select a repair, adopt a contract,
or infer any client obligation from source proximity.

## Source coverage

- Accepted Scope-of-Work read item 4: `4/4` files read in full and hash-recorded.
- `READ_SCOPE_AMENDMENT_1.md`: `11/11` files read in full and hash-recorded.
- Accepted N0 return/report: `2/2` read; JSON parsed.
- Exact per-file hashes and citations are recorded in `N1_INVENTORY.md`.
- Additional read request: none.

## Tool-use statement

- Used non-shell Node file reads, SHA-256 hashing, text inspection, and JSON
  parsing through the Node REPL tool.
- Used `apply_patch` only to create the two exact authorized outputs.
- Bash/shell: not used.
- Network: not used.
- Executable software checks or implementation commands: not used.
- Delegation: not used.
- Git: not used.

## Write-containment statement

Allowed and actual writes are identical:

1. `inventory/N1_INVENTORY.md`
2. `inventory/N1_RETURN.md`

No runtime, client, project, profile, contract, decomposition, PRD, lifecycle,
release, reliance, Task Management, Git, or foreign-loop write was performed.

## Hard stops and next owner

No semantic selection, implementation, N4 dispatch, lifecycle/release/reliance
act, SCA/decomposition/PRD act, or client classification was performed. The
verdict is a recommendation to WORKING_ITEMS only. WORKING_ITEMS must validate
and accept this return before any N4 fan-in or dependent graph transition.
