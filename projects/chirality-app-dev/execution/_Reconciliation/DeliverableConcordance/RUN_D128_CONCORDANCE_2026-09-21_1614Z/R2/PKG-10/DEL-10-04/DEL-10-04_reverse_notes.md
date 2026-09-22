# DEL-10-04 — reverse-pass notes (R2, PKG-10)

The reverse pass answered 320 capability rows from seven area files, in this order: BUILD 41,
ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS, WORKSPACE.

| Response | Rows |
|---|---:|
| CLAIMED_BY | 2 |
| PARTIAL | 8 |
| NOT_MINE | 310 |

The reverse validator passed on each of the seven capability files. The errata validator also
passed. The sealed ledger's SHA-256 is unchanged
(`d8783a4b9840c4382382654dd7929cd9666fdd1f95b261dc66c738ff78428fd0`).

## Claimed and partial capabilities

| Capability | Response | Claim | Why |
|---|---|---|---|
| CAP-BUILD-038 | CLAIMED_BY | CLM-016.1 | D-APP-70 maps this PEC evidence-driver path to DEL-10-04 as primary owner. |
| CAP-BUILD-039 | CLAIMED_BY | CLM-016.1 | D-APP-70 maps this PEC evidence-driver path to DEL-10-04 as primary owner. |
| CAP-BUILD-040 | PARTIAL | CLM-016.1 | This is PEC interaction evidence, but it is not one of the two mapped paths. |
| CAP-HARNESS-053 | PARTIAL | CLM-016.1 | DEL-10-04 owns the pec registry-entry content; DEL-10-01 owns the registry mechanism. |
| CAP-HARNESS-055 | PARTIAL | CLM-016.1 | DEL-10-04 owns the PEC-fixture evidence; DEL-10-03 owns the tool surface. |
| CAP-HARNESS-054 | PARTIAL | CLM-004.6 | The OpenPipeStress runner is cited as FR-114 evidence. |
| CAP-RTCONTRACT-042 | PARTIAL | CLM-004.6 | The OpenPipeStress descriptor is cited as FR-114 evidence. |
| CAP-RTCONTRACT-043 | PARTIAL | CLM-028 | The OpenPipeStress runner text in the catalog is cited against the CLM-028 trade-off. |
| CAP-RTCONTRACT-040 | PARTIAL | CLM-010.3 | DEL-10-04 specifies validation of the profile contract; the contract itself is the D-APP-49 staged surface. |
| CAP-RTCONTRACT-041 | PARTIAL | CLM-010.11 | DEL-10-04 specifies operation-descriptor fixture coverage; the contract itself is the D-APP-49 staged surface. |

No coverage gap was found: every capability that matches DEL-10-04 scope has a forward row.

## Errata

There is one erratum, on CLM-016.1 `ImplementationEvidence` (a REACH tag only). The sealed row
tagged `pec-scratch-server.mjs` as REACH=LEGACY_ONLY. CAP-BUILD-038 shows the helper is reached
from the opt-in integration test, so its reach is TEST_ONLY.
`run-pec-bridge-rehearsal.ts` stays LEGACY_ONLY (UNREACHED).

The erratum changes no Disposition. Sealed and errata-applied census figures are therefore
identical:

| Disposition | Sealed | Errata-applied |
|---|---:|---:|
| STALE_SPECIFICATION | 30 | 30 |
| PARTIALLY_IMPLEMENTED | 9 | 9 |
| ALIGNED | 7 | 7 |
| NOT_AUDITABLE | 5 | 5 |
| REMAINING_STATE_MISMATCH | 3 | 3 |
| ACCEPTED_DIVERGENCE | 1 | 1 |
| AUTHORITY_CONFLICT | 1 | 1 |
| IMPLEMENTED_DIFFERENTLY | 1 | 1 |
| UNKNOWN | 1 | 1 |
| **Total** | **58** | **58** |

## Reach granularity, recorded without an erratum

The capability files tag the runtime-contracts modules below by their consumers. The forward
ledger followed the evidence pack's module-level `REACHABILITY.csv`, which marks them LIVE only
because they are exported through the contracts barrel:

| Module | Capability file's tag |
|---|---|
| `domain-profile.ts` | TEST_ONLY |
| `operation-proposal.ts` | TEST_ONLY |
| `tool-descriptor.ts` | LEGACY_ONLY |
| `tool-catalog.ts` | TEST_ONLY |

The forward rows (CLM-003, CLM-004.1, CLM-004.6, CLM-010.x, CLM-028) followed the rulebook's
prescribed map and already say "exported; no product caller". No disposition changes:

- Under the stricter reading, only CLM-004.1 and CLM-010.1 become "nothing domain-related is
  live". They were already PARTIALLY_IMPLEMENTED with R4-Q1.
- The CLM-028 finding concerns where the OpenPipeStress-specific text sits in the public
  contracts package, and that does not depend on reach.

I raise this for the manager: the evidence pack's reach map (per module) and the capability
files (per consumer) use different granularity.
