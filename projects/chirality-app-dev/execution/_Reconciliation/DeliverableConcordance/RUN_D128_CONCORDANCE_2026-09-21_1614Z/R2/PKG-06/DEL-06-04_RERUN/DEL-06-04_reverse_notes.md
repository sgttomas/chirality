# DEL-06-04 reverse-pass notes (rerun, pass 2)

## Responses

- **Capability files answered** (409 rows, in this order): BUILD, ELECTRON, HARNESS, ROUTES,
  RTCONTRACT, RTCORE, SETTINGS, SHELL, WORKSPACE.
- **CLAIMED_BY: 3**
  - HARNESS-045, the path policy, is claimed by CLM-009.2.
  - HARNESS-047, the write hooks, is claimed by CLM-009.1. This covers the write family only.
  - SETTINGS-026, the atomic write, is claimed by CLM-009.11.
- **PARTIAL: 10**
  - HARNESS-043 → CLM-009.7
  - HARNESS-051 → CLM-009.10
  - HARNESS-056 → CLM-032.1
  - HARNESS-048 → CLM-009.13
  - HARNESS-031 → CLM-009.8
  - RTCONTRACT-019 → CLM-009.9
  - RTCORE-028 → CLM-009.2
  - RTCORE-030 → CLM-009.12
  - SHELL-025 → CLM-009.9
  - ELECTRON-026 → CLM-009.14
- **NOT_MINE: 396**

## Errata and coverage gaps

- **Errata:** none. No forward row was contradicted by the capability evidence, so there is no
  errata file.
- **Sealed and errata-applied census:** identical (see `DEL-06-04_notes.md` §1).
- **Coverage gaps:** none that DEL-06-04 should own.
  - WORKSPACE-022 and WORKSPACE-024 are the App status and dependency write routes. They are the
    live substitute noted in CLM-004.4 and CLM-009.10. They are owned by the workspace and
    lifecycle deliverables, not by this deliverable.

## Observations

- **Instruction-root protection has no live owner.**
  - HARNESS-025 and HARNESS-026 handle instruction-root and working-root resolution. RTCORE-043
    records a write-root policy. All three are left NOT_MINE: they belong to DEL-07-01 and the role
    and policy owners.
  - None of these capabilities enforces the instruction-root write block on the live path. This
    supports the AUTHORITY_CONFLICT on CLM-009.3.
- **The HARNESS surface file agrees with the forward reachability tags.**
  - It tags HARNESS-043/045/047/051 as `LEGACY_ONLY; STATE=DISABLED`.
  - This matches the forward ledger's LEGACY_ONLY tags and the R4-Q1 routing.

## Seal

The claims SHA-256 is unchanged:
`839f78e13c4c41de25a706deb2fe52c813b609dbeb8227f32f84ab9ebfaa250a`.
