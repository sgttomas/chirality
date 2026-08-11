# Frozen work graph — D-APP-93 tenth lineage

Version: `L10-GRAPH-v1`

Posture: `TERMINAL_FAN_OUT_IN`, serialized. Selection authority: owner
direction of 2026-08-10.

| Node | Role | Dependency | Exact durable contract | Gate |
|---|---|---|---|---|
| M0 | WORKING_ITEMS | baseline | manager command contract/log, citations, controls, exactly 18 N1 stubs | identities, allowlists, stub 18/18, tool/intake/tier probes PASS |
| N1 | fresh Agent 2 author | accepted M0 | fill only the exact 18 stubs | stage census, fresh 80-row packet, two-tier ledger, command mirror, terminal disk census |
| M1 | WORKING_ITEMS fan-in/freeze | accepted N1 | validation, command-log audit, immutable freeze | 18/18 FILLED, reprobes, zero IDs, complete packet freeze |
| N2 | genuinely fresh read-only Agent 2 verifier | immutable M1 freeze | verifier return stub only | independent PASS covering both tiers and census |
| M2 | WORKING_ITEMS close | accepted N2 | return, handoff, inventory, approval request | STOP at frozen-hash owner gate |

No remediation/replacement author or eleventh lineage exists. A stub unfilled
at the first checkpoint after its stage blocks. N2 is never released before
freeze.

N1 stages: 10, 10, 12, 22, 20, 10, 10, and 10 minutes; total 104 minutes.
First checkpoint no earlier than minute 10, then every 12 minutes. Every
checkpoint records exact FILLED/UNFILLED counts, remaining paths, file count,
and bytes. Growth is progress; quietness alone is not failure.
