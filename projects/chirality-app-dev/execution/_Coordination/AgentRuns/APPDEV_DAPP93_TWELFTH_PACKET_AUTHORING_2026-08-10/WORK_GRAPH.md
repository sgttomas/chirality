# Frozen work graph v1

Selection authority: owner direction, 2026-08-10. Posture: `TERMINAL_FAN_OUT_IN` with one author followed by one fresh verifier.

| Node | Actor | Depends on | Writes | Terminal gate |
|---|---|---|---|---|
| M0 | WORKING_ITEMS | activation | manager/control, specs, stubs, preflight evidence | citations exact; every manager form pinned/probed; end-to-end filled-fixture fan-in PASS |
| N1 | ephemeral Agent 2 | accepted M0 | six packet stubs, self-census, terminal return only | all sentinel lines replaced exactly; SPEC files unchanged; census equals disk; content checks PASS |
| M1 | WORKING_ITEMS | accepted N1 | probe ledger, manager validation, freeze records | authored forms probed by tier; five components complete; zero rejected historical IDs; packet frozen |
| N2 | fresh ephemeral Agent 2 | accepted frozen M1 | verifier return only | read-only PASS over frozen packet, both probe tiers, census, citations, and zero historical IDs |
| M2 | WORKING_ITEMS | verifier PASS | manager return, handoff, runtime summary, inventory | stop at exact hash approval gate |

Edges: `M0 -> N1 -> M1 -> N2 -> M2`. No concurrent writes. N2 is held unless M1 accepts and freezes the packet. No repair is permitted after freeze.

Escalation: any citation mismatch, unpinned manager form, failed probe, SPEC mutation, unfilled sentinel, census mismatch, historical-identity hit in a filled stub, failed authored-form probe, verifier non-PASS, or scope breach blocks the lineage. A block produces preserved evidence and a twelve-lineage causal analysis; no thirteenth lineage starts.

Pacing: M0 expected 15 minutes; N1 stage expectations are runbook 8 minutes, scripts 8 minutes, evidence/citation 6 minutes, approval/census/return 6 minutes, total 28 minutes. Checkpoints no earlier than 10 minutes and then every 10 minutes. Liveness is filled-stub count plus bytes, never silence. Interrupt only after a full interval with zero durable growth, recording file count/bytes; native context occupancy is unavailable and must be stated per event.

Manager symmetry: every manager command used for activation, pre-dispatch, supervision, fan-in, validation, freeze, and closeout must appear in `allowlists/MANAGER_COMMAND_ALLOWLIST.md` or be recorded as parent-provided activation intake before graph freeze. All command operands must stay within `allowlists/MANAGER_READ_ALLOWLIST.txt` and the run root, except the exact authorized citation operands. Closeout performs a self-audit.
