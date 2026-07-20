# Application Content Audit Return

## Verdict

`PASS`

The current application bytes reproduce D-APP-70 Option A without selecting
the unresolved preload physical lead or changing source, lifecycle, Approval,
ScopeOfWork, or dependency truth.

## Basis and methods

- Basis: `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`.
- Compared current bytes independently against
  `CQF1_SCOPE.csv`, D-APP-70's packet and ruling, the accepted V1 return/status,
  and every entry in the 14-file `ACTIVATED_57652BA1/` hash binding in
  `POST_MAIN_BASIS_v1.json`.
- Parsed `APPLIED_MAPPING.csv` and `REMAINING_DISPOSITION.csv` with Python's
  CSV parser; recomputed SHA-256 from file bytes; compared ordered path lists,
  uniqueness, group populations, authorities, treatments, and source hashes.
- Compared all five current `_STATUS.md` files to `git show HEAD:<path>` and
  inspected the exact Git diffs. Recomputed each before/after status hash and
  each local-record hash.
- Recomputed all 22 source hashes, five `ScopeOfWork.md` hashes, five
  `_DEPENDENCIES.md` hashes, five `Dependencies.csv` hashes, all 14 accepted
  upstream derivative hashes, and the accepted V1 return/status hashes.
- Inspected each local record and every applied row against the ruling's
  owner/treatment and retained-boundary text. No W1 assertion was used as
  substantive proof.

## Exact coverage

| Check | Result |
|---|---|
| Scope rows / applied rows / unique applied paths | `22 / 22 / 22` |
| Existing paths / exact current source hashes | `22 / 22` |
| Exact original scope and proposal order | `22 / 22` |
| Ordered path-list SHA-256 | `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36` |
| Groups | `9` |
| Group populations | `5+4+6+1+1+1+1+1+2=22` |
| Physical/primary / shared-only | `21 / 1` |
| Changed statuses / local R5 records | `5 / 5` |
| Closed CQ-F1 containers / retained CQ-F1 residuals | `4 / 1` |
| Source / SOW / dependency surfaces hash-reproduced | `22 / 5 / 10` |
| Accepted upstream derivative files hash-reproduced | `14 / 14` |

## Row and group verdict

`PASS` — `APPLIED_MAPPING.csv` has the exact 22 unique paths in
`CQF1_SCOPE.csv` order and carries the exact source hashes bound by
`POST_MAIN_BASIS_v1.json`. Every row names the applicable
`D-APP-70 Option A recommendation <group>` and the exact D-APP-70 ruling path.

The nine ruled groups reproduce the ruling without substitution:

1. Five shell/presentation paths: DEL-02-01 physical/primary treatment with
   the ruled host, consumer, persona, shared-style, and selector boundaries.
2. Four working-root document paths: DEL-02-03 primary with DEL-02-01 host,
   DEL-03-03 route dependency, DEL-09-04 verification-consumer, attachment
   UI/security, and non-substitution boundaries.
3. Six replay/projection paths: DEL-05-04 primary with DEL-05-01, DEL-05-02,
   DEL-05-05, DEL-02-01, DEL-06-01/PKG-06, and DEL-08-05 interests retained.
4. One route path: DEL-07-03 physical route-contract owner, retaining
   DEL-07-01 containment and DEL-02-03 consumption.
5. One catalog path: DEL-06-02 mechanism only, without absorbing generated
   capability semantics.
6. One preload path: shared-boundary-only treatment with no physical owner.
7. One proof fixture: DEL-09-06 primary, retaining the DEL-04-01 evidence edge
   and development/test-only boundary.
8. One contract lint: DEL-03-01 semantic lint owner, retaining DEL-09-05 as
   release-quality consumer.
9. Two PEC evidence paths: DEL-10-04 primary, retaining DEL-10-03, F-APP-3,
   and the no-apply/no-hard-fence boundary.

The current D-APP-70 packet and ruling hashes are respectively
`94b01c68e0611c6f2b0a13f6e1087830876d62aab4bfcda2c386aceb721f4b16`
and `1428294b9af34a97b19b7284860a5fdefc7fdb6157cce8c9516f4b54b064638a`,
exactly matching the bound basis. The accepted V1 return/status hashes also
reproduce exactly as
`28fd98d46a160016d6fd875ea0281c07ee85971054b4e7de45fbe9af83b62936`
and `9f71e6d7604439f69d94c78cea66bbe0f1feb2924b06adfcc37e0b25e3274460`.

## Boundary verdict

`PASS` — exactly 21 rows are
`APPLIED_PHYSICAL_OR_PRIMARY`. Only
`projects/chirality-app-dev/frontend/electron/preload.ts` is
`SHARED_BOUNDARY_APPLIED_PHYSICAL_LEAD_UNRESOLVED`; its
`PhysicalOrPrimaryOwner` cell is blank. Its retained boundary is exactly:

`DEL-02-03 selectDirectory; DEL-02-05 apiKey; DEL-09-06 safeStorage/security; physical lead remains DEL-02-03, DEL-02-05, DEL-09-06, or deferral under D-APP-71`

The row-level `RetainedBoundaries` fields and
`RETAINED_BOUNDARIES.md` preserve the ruling's consumer, security, evidence,
UI-state, shared/split, capability, and integration distinctions. No current
row converts those distinctions into SOW or dependency truth.

## Status and record verdict

`PASS` — the only `_STATUS.md` paths changed from `HEAD` under the subject
execution tree are the declared DEL-02-01, DEL-03-03, DEL-06-02, DEL-09-04,
and DEL-10-04 files. Their before/after and record hashes independently
reproduce as follows:

| Container | Before status SHA-256 | After status SHA-256 | Record SHA-256 | Rows |
|---|---|---|---|---:|
| DEL-02-01 | `095fdd18e562532a2376e6e55cad894a492926c8902999bb1c6b34fafcbdbd47` | `3679b7f14ff36d35ee82f52e493f3f05b80f7fe9e864bb63d7ab08fe00354bae` | `1410a40bc864c4de73ce4eda77543b5079504ac7df2176077635c306e6266103` | 14 |
| DEL-03-03 | `fc283765cc5b233d88438190dada7c73e64ae5f20b676a78f174b3434db56930` | `fbbebf92ea8fe58ea75e663f7ae2493865cf23b7320b524f2b5c48082a0cb7d9` | `1c92f0e4c377bd0d1dcb2ca59178a185c4257efb7948f08b79d49d1918a0f438` | 1 |
| DEL-06-02 | `1f5a488c605f7f6ff7019066960f58102b0e65d30ee2abf043b0189a1bfe8ef1` | `2a1bcc40e75614f4859922b206ce6d971c5ddf3924c23f80cc89c560de7f626b` | `b18c0dd1b6bef01e497e27b1264e60ace694f17543b6ea71513d080190129b51` | 1 |
| DEL-09-04 | `f733bf5c4cb14e760bc5e0dadc39cdedc1ffabeb536893078df5f6c3a2415382` | `e571ae16bc62800f6d14ce33630a6d7b1414fdebcccc35b6bb11c0be93c476f3` | `5628f2a3a378ce5eb46b8a9cd3d0c10bbcb046a1964b360f019e5a575f6f759c` | 4 |
| DEL-10-04 | `17c6847e0475f7baadb95f20f8db2bf8d5db57d7c817cbdfdbacd49f1b2ab518` | `9d0a185d5ba691239e2109b668ca6fc59e90fc8aea326b9a3787dcc279bd247a` | `22338f36f68722bb44e82e84498724310f910e642ab9fd018e9b58e5c97fbb4b` | 2 |

Exactly five files named
`R5_DAPP70_CQF1_MAPPING_APPLICATION_2026-07-20.md` exist. Each record binds
the exact ruling hash, applied derivative, status before/after hashes,
affected mapping row(s), current source hashes, retained boundaries, and the
no-change claims for source, SOW, dependencies, lifecycle, Approval SHA, and
MEMORY. The five record byte hashes equal both `REMAINING_DISPOSITION.csv` and
`MANIFEST.json`.

For all five statuses, the complete pre-`## Remaining` metadata block is
byte-identical to `HEAD`; therefore Current State, Last Updated,
Authorization Basis, Directive, and Checking Approval SHA did not change.

## Disposition verdict

`PASS` — DEL-02-01, DEL-03-03, DEL-06-02, and DEL-10-04 now have empty
`Remaining` sections and each removed only its prior CQ-F1 entry. DEL-09-04
removed the ruled `chirality-window.d.ts`, scripted-proof, and contract-lint
portions and retains exactly one executable CQ-F1 item prefixed
`(gated: D-APP-71)`.

That residual offers only DEL-02-03, DEL-02-05, DEL-09-06, or deferral; it
states that no path-level owner was applied and no source repair was
authorized. DEL-09-04's unrelated packaging/release Remaining line compares
byte-for-byte equal to the `HEAD` line. Thus the accounting is four exact
closures plus one truthful D-APP-71 residual, with unrelated residual truth
preserved.

## Preservation verdict

`PASS` — all 22 current source SHA-256 values equal both the applied rows and
`POST_MAIN_BASIS_v1.json`; all paths exist. All five SOW hashes and all ten
dependency-surface hashes reproduce their basis values. The 14 accepted
upstream derivative hashes reproduce `14/14`. No frontend/runtime source path
is present in the Git diff. The exact status metadata comparison proves no
lifecycle or Approval SHA change on the five written deliverables.

## Findings, repair, rerun, unknowns, and conflicts

- Findings: none.
- Blocking findings: `0`.
- Repair required: none.
- Required rerun: none on the audited bytes. Rerun this application-content
  slice if the basis, D-APP-70 authority, accepted V1, upstream derivative,
  applied derivative, any of the 22 sources, any of the five statuses or five
  records, SOW/dependency surfaces, or D-APP-71 residual changes.
- Unknowns: none within the sealed application-content scope.
- Conflicts: none.
- Waivers: none.
