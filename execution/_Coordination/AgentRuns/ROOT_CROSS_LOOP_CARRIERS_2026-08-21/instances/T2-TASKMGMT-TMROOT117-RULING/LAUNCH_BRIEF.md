# T2 TASK_MANAGEMENT Launch Brief — TM-ROOT-117 Option-R closure

- **RunID:** `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- **Parent:** `HELP_HUMAN`
- **Role:** `TASK_MANAGEMENT` (Agent 1)
- **Invoking loop:** Root
- **Mode:** owner-ruled resolution closeout / row maintenance

## Owner act

The owner ruled:

```text
TM-ROOT-117 — APPROVE OPTION R (RE-SCOPE). CLOSE TM-ROOT-117
RESOLVED_BY_DECISION. ROUTE A RECIPROCAL NOTICE DIRECTING APP TO REPLACE
TM-APP-032'S TRIGGER WITH THE EXACT TEXT IN THE T1 RETURN; NO SUCCESSOR
IDENTITY IS ACCEPTED BY THIS RULING.
```

The full continuation direction is transcribed at
`execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/OWNER_DIRECTION_TRANSCRIPT_PR602_REPAIR_AND_RULINGS_2026-08-21.md`,
SHA-256
`2d89d0aa1410e9bec74af54a1a8cb8b151cf60009c2214a3c682f925ba8ddb3e`.

The parent has already routed the reciprocal App notice at
`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM117_TRIGGER_RESCOPE_AND_DEL0206_PREPARATION_AUTHORIZATION.md`,
SHA-256
`fd587b676a55c42feecd2c0e9dbcb96d67a1f2bcff3d5ab66d6fdb78826fdaf0`.
It contains the exact T1 replacement trigger and grants no App authority.

## Required work

1. Run the mandatory read-only federation preflight over all canonical
   registers and record coverage/counts.
2. Create
   `execution/_Coordination/_TaskManagement/CLOSEOUT_2026-08-21_TM-ROOT-117.md`
   as SHA-bound closure evidence. Bind the owner ruling, exact App notice,
   absence of any accepted D-APP-48 successor, and no-effect boundary.
3. Move only `TM-ROOT-117` from Root `REGISTER.csv` to
   `REGISTER_CLOSED.csv`, preserving the 25-column schema and source fields;
   set `Status=CLOSED`, `Disposition=RESOLVED_BY_DECISION`, closure evidence
   path/hash/quote, `LastReviewed=2026-08-21`, and `Closed=2026-08-21`.
4. Append exactly one Root loop receipt, Receipt 111, covering this entire
   continuation. It must bind:
   - the exact continuation transcript and hash;
   - the four-file basis-SHA repair, H2 return SHA-256
     `6bf3c4f83ca2f13909a33342a64dfae14c67bae570a31eb0746faba825736cc6`,
     corrected basis `e3e18d27740018efd12e73193c02395a9eca93c2`,
     and nonexistent rejected SHA;
   - TM-ROOT-117 Option-R closure and the routed App notice;
   - the separate DEL-02-06 owner ruling recorded at
     `AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/DEL02_PREPARATION_AUTHORIZATION_HANDOFF.md`,
     SHA-256
     `a9b34030a8cece37eb20442241402d3553a383b598acc88f3de6e62280d0e562`;
   - epoch `1`, candidate `root-runtime-1`, the separate-tranche activation
     boundary, and the future exact-byte human acceptance gate;
   - PR #602 review/merge remaining owner acts, no artifact-proof label, and
     no rebase, force push, branch deletion, implementation, lifecycle,
     release, publication, reliance, or foreign-register effect.
5. Validate Root live/archive registers after the move and rerun mandatory
   federation. Write `RETURN.md` and `STATUS.json` in this instance directory.

## Write scope

- `execution/_Coordination/_TaskManagement/CLOSEOUT_2026-08-21_TM-ROOT-117.md`
- `execution/_Coordination/_TaskManagement/REGISTER.csv`
- `execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv`
- `execution/_Coordination/LOOP_RECEIPTS.md`
- this instance's `RETURN.md` and `STATUS.json`

Do not write foreign registers/notices, Root or run handoff state, DEL-02-06,
the basis-repair targets, product/runtime files, or Git.

## Expected post-state

- Root register: 21 live rows (`OPEN=11`, `DEFERRED=10`).
- Root archive: 104 closed rows.
- `TM-ROOT-117` appears exactly once, in the archive.
- Receipt 111 is unique and terminal.
