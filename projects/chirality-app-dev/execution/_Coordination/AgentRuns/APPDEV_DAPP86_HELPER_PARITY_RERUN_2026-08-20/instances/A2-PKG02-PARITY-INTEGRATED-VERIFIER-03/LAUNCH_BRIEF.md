# Sealed Agent 2 Launch Brief — integrated-review V3

- RequestedBy: `WI-PKG02-DAPP86-RERUN-01`
- RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
- ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01-AMEND02`
- ChildInstanceID: `A2-PKG02-PARITY-INTEGRATED-VERIFIER-03`
- AgentType: fresh ephemeral generalist Agent 2; no delegation; read-only verification; no repair.
- PackageID / DeliverableID: `PKG-02` / `DEL-02-02`.
- Objective: verify the frozen integrated-review contract repair byte-for-byte and semantically, then return `ACCEPT_REPAIRED_FAN_IN` or `REJECT_REPAIRED_FAN_IN`.
- AcceptedBasis: Agent 0's records-only remediation direction. No rerun, product/source/deliverable/launcher/Git/shared-surface effect is authorized.
- DeclaredReads: repository-wide read; all current run-root files; live project instructions and status/decision sources needed to calibrate claims.
- AllowedTools: read-only deterministic shell/hash/CSV/JSON/source inspection. Do not start app, daemon, UI, build, or tests. Do not repair.
- AllowedWriteTargets: only `instances/A2-PKG02-PARITY-INTEGRATED-VERIFIER-03/RETURN.md`. Do not create or edit `STATUS.json`; the manager writes that sole post-verification mutation after your terminal return.

## Frozen bytes to verify

| Artifact | Required SHA-256 |
|---|---|
| `RETURN.md` | `3c68a8d060e13e4e7c9d085e172ff6bcb95b1e4eb3255073bc8d028a13a9270b` |
| `CLOSEOUT_AMENDMENT_01.md` | `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7` |
| `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md` | `6ada335fab940c9c9265a37fa2d042fba94beff8a8f0a66df1a28c9d12e812a8` |
| `EVIDENCE_INDEX.csv` | `9cc9a80452c5b684d453adf23986f937eebbe582a2a67023fa27fc74f199fbf1` |
| `STATUS.md` | `127f5b9b0c02842571c3f22d5a3b7432c507def9af421c7622387599b919e3af` |
| `HANDOFF_STATE.md` | `da113537fa4999ef15a864ee4d1777ab9646c6b75c2363d576929deb8b5c772c` |
| `REGISTERED_CHECKS.json` | `a99a5b6d9b83fecc43f35707f120c668271c018174886193ac876e2e7b1259b0` |
| `RUNTIME_SUMMARY.json` | `738d5889e9ba81f1cda64779e23a1afcdb2e7ebdd3195febd3a2548847ab851c` |
| E1 `STATUS.json` | `b175bf31f92883f52e11fe6cdae32fa01b6a8e559cdcdd2e905bf85b2ef9256e` |
| V1 `STATUS.json` | `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1` |
| V2 `STATUS.json` | `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832` |

## Acceptance criteria

1. Every required hash above matches the current file.
2. `EVIDENCE_INDEX.csv` parses as exactly six columns and all 22 indexed paths/hashes match.
3. E1/V1/V2 status records use `chirality-agent-instance-status/v1`, bind the exact immutable return hashes, and preserve outcomes `BLOCKED / PARTIAL`, `ACCEPT_BLOCKED_FAN_IN`, and `ACCEPT_AMENDED_FAN_IN`.
4. `REGISTERED_CHECKS.json` uses `chirality-software-check-evidence/v1`, binds exact HEAD `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, and truthfully records focused tests/typecheck/build while packaged UI is `BLOCKED` and premerge/release-quality/secret-scan are `NOT_RUN`, never PASS. Waivers must be an empty array.
5. Manager `RETURN.md` binds `RUNTIME_SUMMARY.json` by exact path/hash/status and explicitly states waivers none.
6. Runtime summary is valid JSON, status PASS only for 15-event/5-session ledger completeness, and its closeout calibration remains `BLOCKED / PARTIAL`, no parity closure, no trigger, no rerun, launcher untouched, and retry/package-command provenance `UNKNOWN`.
7. Raw executor evidence and E1/V1/V2 returns remain byte-preserved. No path outside this run root changed; Receipt 183 is untouched.
8. No parity, product, deliverable, release, lifecycle, waiver, trigger, rerun, network-authorization, launcher-restoration, or Git effect is inferred.

Return exact checked hashes and any finding. Perform no repair. After writing `RETURN.md`, stop.
