# DEL-08-01 — reverse-pass notes

The forward ledger is sealed. Its SHA-256 is still
`5b2dea32140bc410f597e870965612127c3fa92df150881a44cbf10b78c1ff58`.

## Inputs

- **Capability areas:** BUILD, ELECTRON, HARNESS, RTCONTRACT and RTCORE.
- **Rows answered:** all 239, in `DEL-08-01_reverse.csv`. The rows come from the manager's
  `REVERSE_INPUT_capabilities.csv`.

## Responses

| Response | Count | Rows |
|---|---:|---|
| CLAIMED_BY | 2 | CAP-BUILD-007 → CLM-009.3; CAP-HARNESS-041 → CLM-005 |
| PARTIAL | 8 | CAP-BUILD-006, CAP-HARNESS-026, CAP-HARNESS-045, CAP-HARNESS-047, CAP-HARNESS-058, CAP-RTCORE-016, CAP-RTCORE-035, CAP-RTCORE-042 |
| NOT_MINE | 229 | All other rows |

The PARTIAL rows are behaviors that DEL-08-01's test suite verifies but other deliverables
implement:

- DEL-07-01: working-root admission and instruction-root policy.
- DEL-08-04: the subagent governance bridge.
- DEL-09-04: packaging and staging.
- Runtime / PKG-06: the method catalog and native role configuration.

## Errata

There are 2 errata rows, both in the `ImplementationEvidence` field. Neither changes a
Disposition.

- **CLM-009.7:** adds a live surface the forward pass missed.
  - Runtime `runtime-service.ts:587-615` `listAgents` still parses the SPEC §7.1/§7.2
    `AGENT_TYPE` and `AGENT_CLASS` fields from `agents/AGENT_*.md`. It is used for legacy persona
    sessions.
  - The packaged v3 role files do not have these fields. As a result, legacy persona direct chat
    finds no Type 0 or Type 1 agents.
  - This strengthens the forward row's R4 routing.
- **CLM-009.12:** corrects a reach tag.
  - `native-role-config.ts` `loadTrustedNativeRoleConfiguration` has no product caller, so it is
    TEST_ONLY at symbol level.
  - The live Codex child-role surface is `product-native-role-config.ts:8-37`
    (`materializeProductNativeRoles`).

## Systematic reach-tag difference (no errata filed)

- **The difference:**
  - BUILD capability rows tag the instruction-root scripts `REACH=LIVE; BUILD-TIME`.
    - This covers `prepare-packaged-instruction-root.mjs` (CAP-BUILD-006) and
      `verify-instruction-root-integrity.mjs` (CAP-BUILD-007).
    - These scripts are chained in `desktop:prepare`, `desktop:pack` and `desktop:dist`.
  - The forward ledger tags the same scripts `REACH=TEST_ONLY`. That followed the pack
    `REACHABILITY.csv` limit 3: scripts are not product entry points.
- **About 14 rows are affected,** for example CLM-009.3, .4, .5, .6 and .13, and SEC-2.
- **Why no errata:**
  - The forward Dispositions already treat the packaging pipeline as the operative path for these
    obligations.
  - Changing the tags would change no Disposition, so I did not file per-row errata.
- **For the manager:** recommend adopting the BUILD area's `BUILD-TIME` note convention run-wide.
  The forward notes §5 proposed the same.

## Coverage gaps

None. No capability exposes a DEL-08-01 obligation that lacks a forward row.

- **SCA-APP-010 additions:** these are the proposal-clause checks, skill-template checks and
  organisation-layer pin checks (SEC-1, SEC-2, REM-1). No capability implements them, which is
  consistent with the forward rows.
- **CAP-BUILD-013:** the afterPack resource assertion includes instruction-root presence. I
  answered NOT_MINE because it is packaging finalization (DEL-09-04), not a conformance check.
