# DEL-07-05: reverse-pass notes (R2, PKG-07)

`DEL-07-05_reverse.csv` answers every row of the seven named capability files, in the given order: BUILD, ELECTRON, HARNESS, ROUTES, RTCORE, SETTINGS and WORKSPACE (311 rows).

## Responses

| Response | Rows | Capabilities |
|---|---:|---|
| CLAIMED_BY | 6 | ROUTES-033, SETTINGS-021, SETTINGS-022, SETTINGS-023, WORKSPACE-023, WORKSPACE-024 |
| PARTIAL | 4 | HARNESS-050, HARNESS-051, WORKSPACE-019, WORKSPACE-025 |
| NOT_MINE | 301 | All other rows |

The 301 NOT_MINE rows include every BUILD, ELECTRON and RTCORE row. The Runtime has no dependency-register surface, and RTCORE-033 (application-owned dynamic tools) registers no dependency tool at the frozen basis.

## Errata

There is no errata file. The reverse pass found no forward row to correct, and no coverage gap: every dependency-register capability maps to an existing claim key.

## Where the capability files agree or disagree with the ledger or the pack

### Route reach agrees with the ledger

ROUTES-033, WORKSPACE-023/024 and SETTINGS-022 say the route is served (REACH=LIVE, ENABLED) but has no rendered caller. The ledger's CLM-012.13 note says the same. ROUTES-043 and WORKSPACE-025 carry STATE=DISABLED, confirming that the Pipeline/Workbench callers are never rendered.

Both the ledger and these capability files disagree with the pack. `REACHABILITY.csv` marks `deliverable-api.ts` LIVE through `chat/page>loop-shell`, but that chain is never rendered.

### MCP rows agree with the ledger

HARNESS-050 and HARNESS-051 (REACH=LEGACY_ONLY, STATE=DISABLED) match the ledger's `REACH=LEGACY_ONLY` tagging and the R4-Q1 citation on CLM-012.14.

The ledger adds one piece of evidence the capability files do not state: the live Runtime fingerprint shows `mcpServers: []` (`runtime-service.ts:580`).

### SETTINGS-021 overstates reader validation

SETTINGS-021 describes the register reader as doing "row validation into a typed register snapshot". At the frozen basis, `register-reader.ts:24-122` only normalizes values and emits warnings. All validation happens at write time (`register-writer.ts:97-305`).

The ledger's CLM-012.3 (PARTIALLY_IMPLEMENTED) rests on exactly this gap. The capability text should read "normalization and warnings".

### WORKSPACE-019 omits the leaf-symlink guard

WORKSPACE-019 describes containment as a realpath check. It does not mention the separate leaf-symlink guard on dependency writes (`deliverable-contracts.ts:143-171`), which WORKSPACE-024 does cover.

Neither row mentions that the dependency write path has no instruction-root check. The ledger records that gap on CLM-012.15.

### Rows owned elsewhere

These rows touch dependency data but belong to other deliverables:

- WORKSPACE-013: document-kit scan.
- WORKSPACE-017: reference-hash warnings.
- WORKSPACE-026, 032, 034: retired UI presentation.
- HARNESS-045, 047: legacy containment policy and hooks.

## Seal

The claims SHA-256 is unchanged: `10e14a3eb3133ca8f6e6ea8fb8f05406d9e3b59a9c9beec1b9b56f872d5fd9c4`.
