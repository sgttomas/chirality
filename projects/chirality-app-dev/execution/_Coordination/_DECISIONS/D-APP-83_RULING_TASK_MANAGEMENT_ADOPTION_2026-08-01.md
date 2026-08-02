# D-APP-83 — App Task Management Adoption

Status: `RULED (Option A)`

DecisionID: `D-APP-83`

Date: 2026-08-01

Owner: Ryan Tufts

Owning loop: Chirality App Dev

Subject: `execution/_Coordination/TM_ADOPTION_PACKET_2026-07-31.md`

## Question

Whether this loop adopts the Chirality Task Management standard and mints its
own schema-1.0 Action Item register, and, if adopted, whether Task Management
is invoked on demand / on an owner-scheduled routine (Option A) or bound to
every loop entry and close (Option B).

## Owner ruling

The owner returned in session:

> D-APP-83 ruling: Option A.

## Ruled effect

Option A is adopted exactly as presented in the subject packet:

1. This loop adopts a per-loop Task Management Action Item register at
   `execution/_Coordination/_TaskManagement/REGISTER.csv`, using schema 1.0,
   its canonical 25-column order, and `TM-APP-<seq>` identifiers.
2. `TASK_MANAGEMENT` is invoked on demand or on an owner-scheduled routine.
   There is no loop-entry or loop-close binding, and `loop/LOOP_INIT.md`
   remains unchanged.
3. The register is a session-residue disposition ledger only. It is not a
   work-discovery queue, resolution surface, approval, scope, priority,
   lifecycle authority, or gate. K-TM-1..6 apply in full.
4. The 24 root rows named by the owner's 2026-08-01 steer are linked into this
   loop's register, in the directed order, as `TM-APP-001` through
   `TM-APP-024`: `TM-ROOT-035`, `TM-ROOT-036`, `TM-ROOT-047`,
   `TM-ROOT-055`–`TM-ROOT-061`, `TM-ROOT-063`–`TM-ROOT-067`,
   `TM-ROOT-069`–`TM-ROOT-075`, `TM-ROOT-101`, and `TM-ROOT-103`.
   The root rows are not moved or edited; the App rows cite them and preserve
   their disposition state under Task Management PRD §6.2.
5. Per the owner's specific direction, the `TM-ROOT-035`-linked App row
   records that the root loop declined runtime identity (`DEL-02-06 OUT-002`)
   as out of root scope and that this loop carries it.
6. `TM-ROOT-103` is migrated only. This ruling does not initiate or implement
   the Pi/oMLX Agent 2 capability-expansion proposal; the owner intends its
   decision packet to be the headline of the next session.
7. An ordinary coordination notice is routed to the root loop with the
   D-APP-83 and linked-row evidence so root `TASK_MANAGEMENT` can disposition
   `TM-ROOT-098`. This ruling does not authorize an App actor to edit the root
   register.

## Explicit non-effects

This ruling does not amend `loop/LOOP_INIT.md`, create any duty for another
loop, authorize cross-loop register writes, select or execute the App parity
instrument, initiate the Pi/oMLX expansion packet, change App scope or
decomposition, advance lifecycle state, or disturb the six historical
`UNKNOWN` relations preserved by D-APP-81 clause 6.

The owner ruling is the semantic act. The files and checks implementing it
are evidence of application, not a substitute for that act.
