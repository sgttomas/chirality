# Sealed Agent 2 Launch Brief — Closeout Amendment 01 verifier

- RequestedBy: `WI-PKG02-DAPP86-RERUN-01`
- RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
- ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01-AMEND01`
- ChildInstanceID: `A2-PKG02-PARITY-AMEND-VERIFIER-02`
- AgentType: fresh ephemeral generalist Agent 2; no delegation; evidence-only; no repair.
- PackageID / DeliverableID: `PKG-02` / `DEL-02-02`.
- Objective: independently verify Closeout Amendment 01 after the records corrections, including exact claim calibration, hash/index consistency, raw-evidence preservation, and write containment.
- AcceptedBasis: Agent 0 disposition accepting truthful `BLOCKED / PARTIAL` facts, holding N2, directing no rerun, classifying the launcher write as an invocation opt-out omission, and determining the explicitly distinct-helper trigger is not established.
- DeclaredReads: repository-wide read; all files under this run root; live `frontend/electron/cli-launcher.ts`; accepted D-APP-88/D-APP-93 closure; DEL-02-02 and DEL-08-02 status text; Git state.
- AllowedTools: read-only deterministic shell/hash/CSV/JSON/source inspection. Do not start app, daemon, build, tests, or UI. Do not write product or launcher state.
- AllowedWriteTargets: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/instances/A2-PKG02-PARITY-AMEND-VERIFIER-02/**` only.
- ExpectedOutput: `RETURN.md` with `ACCEPT_AMENDED_FAN_IN` or `REJECT_AMENDED_FAN_IN`, exact hashes, findings, and no repair.
- AcceptanceCriteria:
  1. `RUN_MANIFEST.md`, `VALIDATION.md`, `HANDOFF.md`, `RETURN.md`, `EVIDENCE_INDEX.csv`, `STATUS.md`, `HANDOFF_STATE.md`, and `CLOSEOUT_AMENDMENT_01.md` consistently state `BLOCKED / PARTIAL`, no parity closure, N2 held, no trigger established, no rerun authorized, launcher untouched, and verification opt-out omission.
  2. Every claim that a network/package retry was authorized or durably evidenced is removed from corrected manager-owned surfaces; authorization and successful-command provenance are `UNKNOWN` while package existence/hash facts remain.
  3. The CSV parses as exactly six columns per row; every indexed artifact exists and all hashes match.
  4. Earlier executor raw evidence and child returns remain byte-preserved; record the current hashes and compare where earlier recorded hashes exist.
  5. No product/source, deliverable status/memory/run-record, receipt, register, plan, launcher, Git, or foreign-loop path changed; only this run root is non-ignored untracked state.
  6. Runtime telemetry remains append-only and can be summarized after verifier return; do not require the pre-verifier summary to contain this active session.
- Escalation: any unsupported approval claim, false trigger/parity closure, hash mismatch, malformed index, raw-evidence mutation, or write-containment breach.
