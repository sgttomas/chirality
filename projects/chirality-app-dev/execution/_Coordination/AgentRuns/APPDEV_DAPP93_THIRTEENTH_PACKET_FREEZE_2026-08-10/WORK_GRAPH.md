# Frozen work graph

Version: `v1 — FROZEN BEFORE SUBSTANTIVE RUN ACT`

Selection authority: owner direction, 2026-08-10. Posture: `TERMINAL_FAN_OUT_IN` with no author node and at most one fresh verifier node after freeze.

| Node | Actor | Depends on | Output | Gate |
|---|---|---|---|---|
| M0 | WORKING_ITEMS manager | frozen invocation inventory | citation verification, byte-exact salvage, independent re-verification, assembly result | any mismatch/editorial need BLOCK |
| M1 | WORKING_ITEMS manager | accepted M0 | freeze manifest and aggregate | exact all-byte enumeration |
| N2 | fresh Agent 2 verifier | accepted freeze | written PASS/BLOCK | read-only; no repair |
| M2 | WORKING_ITEMS manager | N2 PASS/BLOCK | approval-gate presentation or blocked closeout | never execute packet |

Pacing: M0 expected 10 minutes; M1 5 minutes; N2 10 minutes; M2 5 minutes. Checkpoints judge durable file/byte growth, not silence. Native token/context telemetry is unavailable and is stated per event.

Escalation: any mismatch, forbidden read, unfrozen manager invocation, candidate editorial need, freeze mismatch, or verifier BLOCK stops the lineage. No fourteenth lineage.
