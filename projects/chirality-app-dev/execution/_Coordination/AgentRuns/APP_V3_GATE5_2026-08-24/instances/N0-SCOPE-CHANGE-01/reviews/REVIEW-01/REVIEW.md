# Independent N0 corrected companion-register review

## Verdict

`PASS` — the corrected companion-register candidate is the exact A8-A
post-image, the transformation is confined to the authorized 83
`AppDecompositionBasis` cells, the historical inputs remain immutable, and no
live or forbidden surface was changed. There are no actionable findings.

## Review identity and boundary

- Run: `APP_V3_GATE5_2026-08-24`
- Subject node: `N0-SCOPE-CHANGE-01`
- Review type: `INDEPENDENT_VERIFICATION`
- Reviewer role: fresh `REVIEW` Agent 1
- Basis branch: `codex/app-v3-gate5-2026-08-24`
- Basis commit and `HEAD`: `cc196023a5532fe58955655c1144cd09ee88343a`
- `origin/main`: `cc196023a5532fe58955655c1144cd09ee88343a`
- Review writes: this new `reviews/REVIEW-01/` directory only
- Subject modification: none

Both `cc196023a5532fe58955655c1144cd09ee88343a` and required ancestor
`c2864d63b0effd3e3685a8724d82a72f9fa8f4e1` were independently confirmed as
ancestors of `origin/main`.

## Governing inputs read in full

| Input | Independently computed SHA-256 | Result |
| --- | --- | --- |
| `plans/steers/chirality_app_v3_gate5_steer_app_2026-08-23.md` | `1dfe6492f97d76d7cb57d44f4ba6f37c5011fc56c918149230800883326cf299` | `PASS` |
| `plans/steers/chirality_app_v3_app_ruling_record_a8_2026-08-23.md` | `d4018737aa9ae33e5b26f2afd3fbb2ffc1e9c8d3fe0a2494cf64c951224b6c8f` | `PASS` |
| `Gate3/GATE3_AMENDMENT_PACKAGE.md` | `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df` | `PASS` |
| `Gate4/GATE4_PROPAGATION_PLAN.md` | `47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6` | `PASS` |

Root `AGENTS.md` and `agents/AGENT_REVIEW.md` were also read in full before
review action. The sealed N0 brief narrows the generic REVIEW write contract to
the three records in this directory.

## Independent candidate verification

The source was the tracked Phase-2b candidate
`Phase2b/CONTRACT_INVARIANT_COVERAGE_REGISTER_REGENERATED_CANDIDATE.csv`; the
reviewed output was
`Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv`.

| Check | Source pre-image | Corrected candidate | Result |
| --- | --- | --- | --- |
| SHA-256 | `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0` | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | `PASS` |
| Bytes | `98230` | `98230` | `PASS` |
| Data rows | `83` | `83` | `PASS` |
| Distinct `InvariantFamily` values | `50` | `50` | `PASS` |
| Incorrect identity in `AppDecompositionBasis` | `83` | `0` | `PASS` |
| True identity in `AppDecompositionBasis` | `0` | `83` | `PASS` |
| Rows retaining `candidate-sha256=` | `83` | `83` | `PASS` |

CSV parsing and cell-by-cell comparison independently established:

- identical 18-column headers and identical row order;
- exactly 83 changed cells across exactly 83 rows;
- `AppDecompositionBasis` is the sole changed column;
- each changed cell is the exact substitution of
  `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`
  with
  `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`;
- a raw-byte replacement of all 83 incorrect identities in the source produces
  the candidate byte-for-byte; and
- the corrected column has one distinct value, preserving the exact
  `...#candidate-sha256=` label and carrying the approved true identity.

An independent run of
`validate_candidate_whitespace.py --base-ref cc196023a5532fe58955655c1144cd09ee88343a`
returned `PASS` with zero skipped untracked binary/symlink paths.

## Producer evidence review

The producer evidence is internally consistent with the independent results:

| Artifact | SHA-256 | Assessment |
| --- | --- | --- |
| `N0_REGISTER_CORRECTION.md` | `609bb6fe0d63eddfa9d7256f0bd5f294fffbab5238617d1b054e217b79adcc95` | `PASS` |
| producer `STATUS.json` | `aa7ac365d7d58aa34d18d6b56eb9212edfc0c47ab85d61e14a330c6d12db0e4f` | `PASS`; valid JSON |

The evidence records the required pre-to-post lineage, cause, one-column
scope, retained label, historical immutability, and non-authoritative N0
boundary without upgrading candidate state.

## Historical immutability and write-boundary proof

The four historical Phase-2/Phase-2b files have no tracked diff from `HEAD` and
retain their recorded identities:

| Historical artifact | SHA-256 | Result |
| --- | --- | --- |
| Phase-2 register candidate | `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079` | `UNCHANGED` |
| Phase-2 transaction | `ace737e599d8f7ec5bdefa47192e30a83f4c12112a032ffe0e0df834dda7ca84` | `UNCHANGED` |
| Phase-2b register candidate | `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0` | `UNCHANGED` |
| Phase-2b transaction | `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d` | `UNCHANGED` |

Before review writes, Git reported no tracked worktree changes. All untracked
paths were confined to the authorized Gate-5 run/control root or the new
Phase-5 candidate. The protected live surfaces independently retained:

| Surface | SHA-256 or tree OID | Result |
| --- | --- | --- |
| live decomposition | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `UNCHANGED` |
| live App contract | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `UNCHANGED` |
| live companion register | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `UNCHANGED` |
| `_ScopeChange/_LATEST.md` | `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` | `UNCHANGED` |
| App Task Management register | `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6` | `UNCHANGED` |
| frontend tree | `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb` | `UNCHANGED` |

The live targets' Git blob OIDs also match the steer exactly:
`48ae8edf982f3ce92e7a686993f3832501e42576`,
`d72b1184b978f8bfa8d84ff2124d0f2871ac2c84`,
`ab2e13344d1ce071d2c1167320b7c875c373eaaf`, and
`c6ce8b2a92c67506887d95c88790a445dbc5668d`, respectively.

## Findings and handoff

- Actionable findings: `0`
- Advisory findings: `0`
- Repair required: `NO`
- Candidate accepted for N1 consumption: `YES`
- N1 may proceed only under its own preconditions and remains prohibited from
  treating this review as authority to write live truth.
