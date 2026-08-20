# Sealed Agent 2 Launch Brief — fresh blocked-return verifier

- RequestedBy: `WI-PKG02-DAPP86-RERUN-01`
- RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
- ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01`
- ChildInstanceID: `A2-PKG02-PARITY-VERIFIER-01`
- AgentType: fresh ephemeral generalist Agent 2; no delegation; evidence-only; no repair.
- PackageID / DeliverableID: `PKG-02` / `DEL-02-02`.
- Objective: independently validate whether the executor's `BLOCKED / PARTIAL` return is truthful, internally consistent, hash-complete, contained, and sufficient for manager fan-in as a failed instrument.
- AcceptedBasis: frozen control-plane files and executor return under this run root; clean start commit `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`; D-APP-86 packet/ruling; D-APP-88/D-APP-93 closure records; prior 2026-08-03 parity evidence.
- Dependencies: executor terminal return exists; no UI execution or product repair is permitted.
- DeclaredReads: repository-wide; all current run files; relevant accepted decision/status/history/product/package configuration; read-only process/socket/path inspection needed for cleanup verification.
- AllowedTools: read-only deterministic shell/hash/json/csv/source inspection only. Do not start the packaged app, daemon, build, server, or test suite. Do not use Computer Use. Do not write outside the verifier instance target.
- AllowedWriteTargets: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/instances/A2-PKG02-PARITY-VERIFIER-01/**` only.
- ExpectedOutput: `RETURN.md` with a clear `ACCEPT_BLOCKED_FAN_IN` or `REJECT_FAN_IN` verdict and exact findings.
- AcceptanceCriteria: all six named outputs and executor return exist; indexed artifacts exist and hashes match; claims do not overstate UI/replay/validation; unexpected owner-state write is evidenced without inferred before-state; run-owned cleanup is independently supported; product/runtime/tracked paths outside allowed evidence are unchanged; helper/package identity claims are calibrated against the current executable package and the prior package; any discrepancy in parent tasking, network approval provenance, or distinct-helper assertion is explicitly surfaced; verifier performs no repair.
- Escalation: any missing/mismatched evidence, continuing process/socket/temp root, further owner-state risk, unauthorized tracked change, or false closure claim.
