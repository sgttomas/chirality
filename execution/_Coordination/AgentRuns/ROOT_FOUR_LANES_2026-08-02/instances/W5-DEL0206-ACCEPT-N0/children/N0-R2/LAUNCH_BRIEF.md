# N0-R2 sealed child launch — fresh basis and accepted-input proof

Form: `EPHEMERAL AGENT 2 GENERALIST`

RequestedBy: `WORKING_ITEMS/W5`
ParentRunID: `ROOT_FOUR_LANES_2026-08-02`, plan version `11`
ParentInstanceID: `W5-DEL0206-ACCEPT-N0`
ChildInstanceID: `N0-R2-W5`
PackageID: `PKG-02`
DeliverableID: `DEL-02-06`

## Governing method

Read and follow in full:

- `packet_blueprint/N0_RERUN_BRIEF.md`, SHA-256
  `d9519594a6fe1a9eb115725bef4d16ac73e1d459853b7c98577da4061e99be36`;
- `packet_blueprint/N0_RERUN_CHECKLIST.md`, SHA-256
  `fb326c03008c3bbfc58efa9a98d4cf22e58c60b80d36bcdc8462624ebff14af7`.

Resolve both paths under RunID
`DEL-02-06-RUNTIME-SPEC-001`. This launch updates parent/node/current-evidence
identities only; it does not change the brief's objective, checks, or holds.

## Frozen evidence

| Evidence | Exact SHA-256 |
|---|---|
| Owner acceptance ruling | `7ddbef0480700483cb07efe771b64e3f413b489288a02bde987a6a85b9ba70f7` |
| Candidate presentation | `2ecd01dcfe95ca9417592875624dff1990cc4ddf6622a2d1126e24e97a2d4a42` |
| W4 return | `25cd4cd934d0141612c15719db1aa562ba4615657ca5eb2a4787fcfe61aeeac0` |
| Candidate/live manifest | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` |
| External acceptance record | `ee035e91d561935d36c6238a50304752d2fd4e67d24e5c2203c550ff8d40760c` |
| Accepted Scope of Work | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` |
| PRD | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| Live decomposition | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| Fresh AUDIT_DECOMP return | `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1` |
| Gate-1 confirmation record | `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f` |

## Objective and tools

Independently execute every N0-R2 checklist item and return exactly one
`RELEASE_N1_N2_N3 | HOLD` verdict. Treat packet acceptance as planning-input
acceptance only.

Use non-shell Node file reads, SHA-256, JSON/CSV parsing, and direct-process
execution of the exact Python packet/acceptance/Scope-of-Work validators.
`apply_patch` is allowed only for the two return files below. Do not use Bash,
network, runtime tests, implementation commands, or delegation.

## Write boundary

AllowedWriteTargets only:

1. `basis/N0_R2_RETURN.md`
2. `basis/BASIS_REPORT_R2.json`

Both resolve under the DEL-02-06 RunID root. No other write is permitted.

Stop after those terminal returns. Agent 2 does not release or dispatch any
dependent node.
