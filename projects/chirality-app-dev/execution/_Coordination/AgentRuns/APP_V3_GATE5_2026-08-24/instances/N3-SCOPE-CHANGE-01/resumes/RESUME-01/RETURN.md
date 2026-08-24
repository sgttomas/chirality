# N3 Resume-01 Return — Contract and Companion-Register Reapplication

**Date:** `2026-08-24`
**Node:** `N3-SCOPE-CHANGE-01 / RESUME-01`
**Role:** `SCOPE_CHANGE` Agent 1
**Basis / HEAD:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `PASS — AUTHORIZED RESUMED ATOMIC APPLICATION EXACT`
**Authority effect:** `LIVE_APP_CONTRACT_AND_COMPANION_REGISTER_REAPPLICATION_ONLY`

## Resume and rollback lineage

HELP_HUMAN conveyed the owner's authorization to resume Gate-5 after the
coordinating run had restored the N3 contract group to its exact pre-images.
At resume entry, `origin/main` remained the exact basis
`cc196023a5532fe58955655c1144cd09ee88343a`, the live App contract was
`6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`,
and the live companion register was
`84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`.

The original N3 `RETURN.md` and `STATUS.json` remain byte-identical as
historical evidence of the first application. This resume record does not
erase or reinterpret the intervening rollback; it proves the separately
authorized reapplication from the restored exact pre-images.

## Repeated fail-closed preflight

- The private N1 contract candidate remained
  `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`
  at 34877 bytes.
- The private N1 corrected-register candidate remained
  `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`
  at 98230 bytes and byte-identical to the independently reviewed N0
  `Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv`.
- C-01 through C-07 pre-images each occurred exactly once in the restored
  contract. The approved C-01 and C-06 LF rows remained respectively
  `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616`
  and `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`.
- C-08's basis anchor occurred once before C-04, zero times after C-04, and
  its application anchor occurred once. C-09 through C-11 anchors each
  occurred once.
- Reconstruction from C-01 through C-11 reproduced the complete private N1
  contract candidate byte-for-byte.
- The restored-live collision census for `K-CONSENT-1` and `K-UNTYPED-1`
  remained zero in the App contract, App companion register, and ratified
  Root contract, including both exact-row/ID and literal occurrence checks.

## Resumed atomic application

N3 reapplied both complete-file diffs in one `apply_patch` group:

| Target | Restored pre-image | Exact resumed post-image | Bytes |
| --- | --- | --- | ---: |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | 34877 |
| `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | 98230 |

## Repeated post-application validation

- All C-01 through C-07 old pre-images occur zero times and all approved
  post-images occur once. The C-08 basis pre-image occurs zero times and
  every C-08 through C-11 insertion occurs once.
- The live contract has 83 unique invariant IDs. The live register has the
  same 83 unique IDs across 50 families.
- All 83 register source anchors resolve to the exact named invariant at the
  exact live contract line.
- Every register `ContractSourceSHA256` equals the applied contract identity.
- Every register `AppDecompositionBasis` cites the true decomposition
  post-image identity
  `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
- `K-CONTROL-1` remains Root-owned,
  `ProvenanceStatus=EXTERNAL_ROOT_AUTHORITY`, and
  `CoverageStatus=MAPPED_WITH_OPEN_ISSUE`, with
  `RUNTIME-OPEN-005;DEL-02-07;WP-03`. Supervisor-socket and
  two-listener-inventory checks remain design-gated until DEL-02-07
  implementation; no stale implementation-coverage claim was introduced.
- The SCC consumption remains exactly
  `DECOMPOSE / DECOMPOSE / INVERT`; `E-020`, `E-018`, and `E-032` remain
  non-gating; WP-03/WP-05, the accepted Root/App account-consent contract,
  G6a, and WP-09/WP-11 separation all remain in force.
- `_LATEST.md`, the App Task Management register, and the frontend tree
  remained respectively `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`,
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`,
  and `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- `git diff --check` passed for the two resumed N3 authoritative targets.

## Containment

This resumed act touched only the App contract, the App companion register,
and this additions-only resume evidence. Sibling N2's decomposition write was
visible during the post-check but was not edited, restored, staged, or claimed
by N3. N3 performed no commit or staging operation.

## Handoff

`RESUME-01` is `PASS`. The coordinating run may proceed from the exact resumed
N2/N3 applied state to post-application validation, registered dependency
extraction, and the fresh named dependency-closure audit. Any later rollback
of this contract group must restore the contract and companion register
together.
