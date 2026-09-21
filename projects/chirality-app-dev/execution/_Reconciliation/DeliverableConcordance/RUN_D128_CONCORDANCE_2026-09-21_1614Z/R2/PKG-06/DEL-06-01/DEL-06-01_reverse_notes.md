# DEL-06-01 — reverse-pass notes (pass 2)

The sealed ledger `DEL-06-01_claims.csv` is unchanged (SHA-256 `a9e3aa79d099502844350eaac52f6cd79e74dc1550678387b37341f2c95d0e3a`).

**Capability files answered, in this order:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WOVEN. There are 413 rows in total.

## Responses

| Response | Rows |
|---|---:|
| CLAIMED_BY | 2 |
| PARTIAL | 20 |
| NOT_MINE | 391 |

**CLAIMED_BY**

- CAP-HARNESS-043 (the legacy permission overlay module) maps to CLM-008.
- CAP-RTCONTRACT-019 (the fixed mapping from mode to Codex `PolicySelection`) maps to CLM-004.

**PARTIAL**

- **Ask mediation.** These map to CLM-009.7 or CLM-009.2:
  - HARNESS-004, -005, -044;
  - ROUTES-013;
  - RTCONTRACT-017, -018;
  - RTCORE-030, -031;
  - SETTINGS-032;
  - SHELL-037.
- **Mode presentation and plumbing.** These map to CLM-004 or CLM-009.6:
  - SHELL-025;
  - ROUTES-001;
  - SETTINGS-030.
- **Permission events.** RTCONTRACT-022 and RTCORE-025 map to CLM-009.10.
- **Tool parity.** RTCONTRACT-037 and RTCORE-039 map to CLM-009.12.
- **Declared permission classes only.** HARNESS-057 and RTCONTRACT-042 map to CLM-034.1. HARNESS-058 maps to CLM-015.1.

No BUILD, ELECTRON or WOVEN capability belongs to DEL-06-01.

## Errata (12 rows, one file)

No Disposition, CauseTag or HumanDecisionNeeded changes. The errata correct evidence and gloss only.

1. **Runtime tool filtering is not a live control on the Codex path.**
   - The sealed ledger cites `runtime-method-service.ts:507-529` (restrictRequestedTools/restrictRuntimeTools) as live filtering of application tools.
   - At the frozen basis, `DelegatedRuntime.turn` ignores the turn tool list (`delegated-runtime.ts:289`, `_runtimeTools`). CAP-RTCORE-039 records this as STATE=DISABLED for Codex.
   - Only the requested-name check (`restrictRequestedTools`, including the readOnly rule to allow read tools only) still applies.
   - Corrected fields:
     - ImplementationEvidence on CLM-009.3, -009.4, -009.5, -009.11, -009.12, CLM-025 and CLM-030;
     - Notes on CLM-009.11 and CLM-009.12.
   - Effect on dispositions:
     - CLM-009.11 stays ALIGNED. Its enforcement rests on the Codex sandbox and approval policy.
     - CLM-009.12 IMPLEMENTED_DIFFERENTLY is reinforced: there is no parity mechanism at all on the live path.
2. **`dontAsk` is not simply absent.**
   - `runtime-daemon-harness-port.ts:205-207` (LIVE) silently maps a legacy `mode: 'dontAsk'` to `permissionMode: 'readOnly'`.
   - On the live path, readOnly is Codex on-request/read-only, which prompts instead of denying. That sharpens the K-PERM-5 conflict.
   - Corrected fields: ImplementationEvidence and Notes on CLM-009.6; Notes on CLM-004.

**Not raised as errata.** CLM-003, -005, -008, -027 and -031 cite `delegated-runtime.ts:304` as the Runtime's rejection of `dontAsk`. That statement is true at the Runtime boundary, so it was left unchanged.

## Census: sealed versus errata-applied

Identical. No erratum changes ClaimType or Disposition.

| Disposition | Sealed | Errata-applied |
|---|---:|---:|
| STALE_SPECIFICATION | 19 | 19 |
| AUTHORITY_CONFLICT | 12 | 12 |
| IMPLEMENTED_DIFFERENTLY | 10 | 10 |
| NOT_AUDITABLE | 5 | 5 |
| PARTIALLY_IMPLEMENTED | 4 | 4 |
| ALIGNED | 4 | 4 |
| REMAINING_STATE_MISMATCH | 3 | 3 |
| STALE_VERIFICATION | 2 | 2 |

## Coverage gaps (for the manager)

- **None requiring a new forward row.** Each capability that touches permission scope maps to an existing key.
- **CAP-SETTINGS-030** (legacy `dontAsk` mapped to `readOnly`) is an undocumented live behaviour. It is covered only through the CLM-009.6 errata. A dedicated IMPLEMENTED_UNDOCUMENTED row may be warranted if the manager prefers.
