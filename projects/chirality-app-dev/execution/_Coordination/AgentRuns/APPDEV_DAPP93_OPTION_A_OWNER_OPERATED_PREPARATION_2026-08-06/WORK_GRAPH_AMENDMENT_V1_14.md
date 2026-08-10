# Work graph amendment v1.14 — D-APP-93 host-path class repair

Status: `ACTIVE — SINGLE INTEGRATION OWNER — VERIFIER HELD`

Authority: `R4_4_4_HOST_PATH_REPAIR_AUTHORITY_ADOPTION.md`.

1. Reproduce the R4.4.4 freeze/PASS/token/adoption/handoff/Receipt-142 basis
   and record the fail-closed step-1 stop.
2. Replace exactly 34 `/bin/printf` command references with
   `/usr/bin/printf`: four in C1105-C1108 operation cells and thirty in
   C1146.01-C1146.30 subinputs. Change no other command byte.
3. Update only mechanically affected ledger, inventory, future owner token,
   prepared index, backcheck, freeze, and necessary same-run control records.
4. Audit every absolute executable path in every operation cell/subinput
   against the current host, distinguishing executable positions from
   placeholders, arguments, data sources, and destinations. Require zero
   missing executables.
5. Prove exact 34-substitution equivalence, preserve C196/C197 and all packet
   invariants, then freeze and stop for HELP_HUMAN acceptance.
6. Only after acceptance, dispatch exactly one new genuinely fresh read-only
   verifier. Never repair or dispatch a second verifier after its verdict.

No packet command, runtime, debugger, package, helper/GUI, signal, credential,
product, Git mutation, Task Management, foreign-loop, or other action is part
of this graph.
