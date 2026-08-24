# N3 Return — Gate-5 Contract and Companion-Register Atomic Application

**Node:** `N3-SCOPE-CHANGE-01`
**Role:** `SCOPE_CHANGE` Agent 1
**Basis / HEAD:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `PASS — CONTRACT ATOMIC GROUP APPLIED EXACTLY`
**Authority effect:** `LIVE_APP_CONTRACT_AND_COMPANION_REGISTER_APPLICATION_ONLY`

## Authorized atomic group

N3 wrote exactly these two authoritative App surfaces as one atomic group:

| Package role | Target | Pre-image SHA-256 / bytes | Applied SHA-256 / bytes |
| --- | --- | --- | --- |
| Authoritative product contract | `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` / 27308 | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` / 34877 |
| Authoritative companion register | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` / 88985 | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` / 98230 |

Both private N1 candidates were independently re-hashed immediately before
application and matched the required identities and byte counts. The register
candidate was also byte-identical to the independently reviewed N0 candidate
at `Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv`.

The first single-group `apply_patch` encoding attempt was rejected before any
write because the patch interface did not accept numbered unified-diff hunk
headers. N3 immediately re-hashed both live targets and confirmed both exact
pre-images remained unchanged. A second single-group `apply_patch` call using
neutral hunk headers applied both complete-file diffs together. No rollback
was required and no partial authoritative state existed.

## Independent pre-write gates

- C-01 through C-07 live pre-images each occurred exactly once.
- C-08's live basis anchor occurred once; after C-04 it occurred zero times;
  the approved post-C-04 application anchor occurred once.
- C-09, C-10, and C-11 insertion anchors each occurred exactly once.
- The approved LF-terminated C-01 row was
  `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616`.
- The approved LF-terminated C-06 row was
  `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`.
- Independent reconstruction from the exact C-01 through C-11 transaction
  anchors was byte-identical to the private N1 contract candidate and produced
  `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`
  at 34877 bytes.
- The live-pre-image collision census for both `K-CONSENT-1` and
  `K-UNTYPED-1` was `0 / 0` exact-row/literal occurrences in the App
  contract, `0 / 0` ID/literal occurrences in the App register, and `0 / 0`
  exact-row/literal occurrences in the ratified Root contract.

## Post-application checks

- Every C-01 through C-07 old pre-image occurs zero times; each approved
  post-image occurs exactly once.
- The C-08 basis pre-image occurs zero times and each C-08 through C-11
  inserted post-image occurs exactly once.
- The contract contains 83 unique invariant IDs.
- The corrected register contains 83 unique invariant IDs across 50 families,
  and its ID set equals the contract invariant-ID set exactly.
- All 83 `SourceAnchor` values resolve to the named invariant row at the exact
  live contract line.
- All 83 `ContractSourceSHA256` values equal the applied contract identity
  `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`.
- All 83 `AppDecompositionBasis` values cite the true decomposition candidate
  identity `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`;
  no incorrect Phase-2 anchor remains.
- `K-CONTROL-1` remains `SemanticOwnerProduct=ROOT`,
  `ProvenanceStatus=EXTERNAL_ROOT_AUTHORITY`, and
  `CoverageStatus=MAPPED_WITH_OPEN_ISSUE`, with open issues
  `RUNTIME-OPEN-005;DEL-02-07;WP-03`. Its enforcement text keeps the
  supervisor-socket and two-listener checks design-gated until DEL-02-07
  implementation. No stale implementation-coverage claim was introduced.
- `git diff --check` passed for both N3 authoritative targets.

## SCC ordering consumption

N3 consumed the owner-accepted A2-B orderings without lifting any downstream
gate:

| SCC | Accepted move | Non-gating edge retained | Downstream gate retained |
| --- | --- | --- | --- |
| `SCC-DELEGATION-EVIDENCE` | `DECOMPOSE` | `E-020` | WP-03/WP-05 fixtures and later implementation authority |
| `SCC-ACCOUNT-MIGRATION-UX` | `DECOMPOSE` | `E-018` | accepted Root/App account-consent contract |
| `SCC-RUNBOOK-VALIDATION` | `INVERT` | `E-032` | G6a exact-candidate ruling and WP-09/WP-11 separation |

No SCC was cut, merged, or silently linearized. Application confers no
carrier activation, implementation, lifecycle, release, publication,
readiness, or reliance authority.

## Containment and sibling-work acknowledgement

N3 touched only its two live authoritative targets and this N3 evidence root.
During N3, sibling N2 independently changed
`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; N3
observed it at the required post-image `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`
but did not edit, restore, stage, or otherwise treat that change as N3 work.

The live `_LATEST.md` remained
`a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`,
the Task Management register remained
`eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`,
and the frontend tree remained
`74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.

## Handoff

N3 is `PASS`. N4 may validate the combined N2/N3 applied state, run the
registered dependency extraction for the four amended carriers, and dispatch
`AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION`. A later failure of
the contract group must restore the contract and companion register together
from N1's exact recovery blobs.
