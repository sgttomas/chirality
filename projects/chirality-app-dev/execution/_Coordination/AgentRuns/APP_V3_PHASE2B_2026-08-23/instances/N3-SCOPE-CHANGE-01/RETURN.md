# N3-SCOPE-CHANGE-01 — Return

**Status:** `COMPLETE`
**Verdict:** `PASS`
**Authority effect:** `NONE`
**ReadyForNextPhase:** `NO`

## Outputs

| Artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| `Phase2b/RESOLVED_APP_CONTRACT_RECONSTRUCTION.md` | `920a5f4091270d42048ab44161726ca87687624d97351d5a02840bf17617e2dd` | `4142` |
| `Phase2b/CONTRACT_INVARIANT_COVERAGE_REGISTER_REGENERATED_CANDIDATE.csv` | `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0` | `98230` |
| `Phase2b/COMPANION_REGISTER_REBUILD_TRANSACTION.md` | `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d` | `6606` |
| `instances/N3-SCOPE-CHANGE-01/VALIDATION_EVIDENCE.md` | `c060f0e86595f6c3ce8af7ce086b80af2d86d59b6a92ca70a09e368b0dd930f1` | `2706` |

## Exact reconstruction identities

| Identity | Value |
| --- | --- |
| Phase-2 control full contract | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` (`34317` bytes) |
| Final Phase-2b full contract | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` (`34877` bytes) |
| Regenerated C-01 LF row | `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` |
| Resolved C-06 LF row | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |

N3 independently replayed Gate-3 C-01 through C-11 against the live App
contract. Old C-01 plus the resolved C-06 first reproduced the Phase-2
identity exactly. Substituting only N1's regenerated C-01 then reproduced
N1's preliminary Phase-2b identity exactly. C-06 remained byte-identical and
the candidate stayed at 214 lines, so all source-anchor line positions remain
stable.

## Companion-register result

- CSV shape: 18 columns, 83 data rows;
- census: 83 unique IDs across 50 families, preserving the accountable live
  delta of exactly +2/+2 for K-CONSENT-1 and K-UNTYPED-1;
- all 83 `ContractSourceSHA256` cells bind `842bf170…`;
- all 83 decomposition pins retain candidate `932b890e…`;
- all 83 source anchors resolve to the same invariant ID in the reconstructed
  contract;
- contract/register ID parity is exact;
- DEL-03-04 remains in both repaired K-EVENT-3 carrier cells; and
- 82 non-K-CONTROL-1 rows differ from Phase 2 only at the global contract pin.

K-CONTROL-1 changes only six declared fields. Its calibrated row proves:

| Field / property | Exact result |
| --- | --- |
| `SemanticOwnerProduct` | `ROOT` |
| `OwnerAuthorityBasis` | `ROOT_RULED_CONTINUING_STEWARDSHIP` |
| `ProvenanceStatus` | `EXTERNAL_ROOT_AUTHORITY` |
| Ratified Root row | `docs/CONTRACT.md` line 162, SHA-256 `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83` |
| `CoverageStatus` | `MAPPED_WITH_OPEN_ISSUE` |
| `OpenIssueIDs` | `RUNTIME-OPEN-005;DEL-02-07;WP-03` |
| Live claim | exactly one control socket; live single-socket checks only |
| Design-gated claim | supervisor socket and two-listener inventory activate with DEL-02-07/WP-03 implementation |

No live second-socket, two-listener implementation, or implementation
coverage is claimed.

## Validation and containment

The raw CSV candidate was written first. Candidate whitespace passed against
`ef92fab10f40aa95da484701982d83fa1abca874` before any N3 transaction,
return, or status pinned its identity. A second candidate-whitespace run after
the transaction records also passed. CSV parse/census, source-anchor,
contract/register mapping, protected-surface, containment, and
`git diff --check` checks passed.

Protected identities remain:

- live App contract `6d3a082c…`;
- live companion register `84d6fe00…`;
- `_LATEST.md` `a0298fdc…`;
- Task Management register `eb37fba1…`; and
- frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.

## N4 handoff

N4 may consume:

- N1 `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`;
- N2 `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463`;
- resolved C-06 row `92c9d359…`;
- N3 reconstruction evidence `920a5f4091270d42048ab44161726ca87687624d97351d5a02840bf17617e2dd`;
- raw register candidate `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`;
  and
- register transaction `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d`.

N4 must independently replay the full contract, parse the CSV, validate all
83 anchors and mappings, compare the K-CONTROL-1 row with the ratified Root
row and A6-A posture, and confirm there is no live second-socket or
implementation-coverage claim. The package remains
`AWAITING_OWNER_APPROVAL`; N4 review cannot approve or apply it.

No live target, old candidate, shared handoff, receipt, pointer, register,
frontend, docs, Root-loop path, commit, push, or merge was written.
