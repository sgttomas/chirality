# SCA-APP-006 Gate 3 Basis Update

**State:** `CURRENT_BASIS_VERIFIED`

**Prior Gate-2 basis:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`

**Current accepted main:** `c487b7dd57a378e2f74417118e78e7f61a161629`

**Date:** 2026-07-27

## Currency result

Accepted main advanced through the OD7-G1 program-record closeout. The new
commit changes governance and coordination records, including the D-APP-75
effective-state closeout, but does not change the App decomposition, App PRD,
App CONTRACT, or prior App SCOPE_CHANGE pointer used by SCA-APP-006.

| Relevant input | Blob at `4214915d9` | Blob at `c487b7dd5` | Result |
|---|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `7e2c2c3c8a9b0ca9498db4102ad688240d91ef0b` | `7e2c2c3c8a9b0ca9498db4102ad688240d91ef0b` | `BYTE_IDENTICAL` |
| `docs/PRD.md` | `048e1ed174f71669a770d0b41b58e108efef55` | `048e1ed174f71669a770d0b41b58e108efef55` | `BYTE_IDENTICAL` |
| `docs/CONTRACT.md` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` | `BYTE_IDENTICAL` |
| prior tracked App `_ScopeChange/_LATEST.md` | `73505247ce7ec90602176e0003cf854154855166` | `73505247ce7ec90602176e0003cf854154855166` | `BYTE_IDENTICAL` |

The Gate-2 impact assessment remains current. Gate-3 candidate generation is
therefore based on accepted main `c487b7dd57a378e2f74417118e78e7f61a161629`
without reopening Gate 2.

## Non-drift limits

This finding does not absorb the OD7 coordination changes into SCA-APP-006,
does not modify D-APP-75, does not release APP-HOLD-1, and does not authorize
contract repair or repinning. It establishes only that the Gate-3 source bytes
and accepted action envelope did not drift.
