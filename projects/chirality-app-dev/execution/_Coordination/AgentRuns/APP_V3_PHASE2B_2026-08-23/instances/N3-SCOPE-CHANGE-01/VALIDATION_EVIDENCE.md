# N3 Validation Evidence — Phase-2b Resolved Contract and Companion Register

**Basis:** `ef92fab10f40aa95da484701982d83fa1abca874`
**Raw register candidate:** `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`
**Resolved contract candidate:** `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`

## Required ordering

1. Mechanically wrote the raw full-file CSV candidate.
2. Ran candidate whitespace against the exact basis: PASS.
3. Computed the raw candidate SHA-256 and byte count.
4. Authored the hash-pinning reconstruction and transaction records.

No hash-pinning N3 artifact existed before step 2.

## Reconstruction checks

| Check | Result |
| --- | --- |
| Phase-2 control replay | `PASS` — `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`, `34317` bytes |
| Phase-2b final replay | `PASS` — `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`, `34877` bytes |
| C-01 final LF row | `PASS` — `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` |
| C-06 final LF row | `PASS` — `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |
| Contract lines | `PASS` — 214, unchanged from Phase 2 |

## Register checks

| Check | Result |
| --- | --- |
| CSV shape | `PASS` — 18 columns, 83 data rows |
| Unique IDs / families | `PASS` — `83 / 50` |
| Exact live delta | `PASS` — `81 / 48` to `83 / 50`, only K-CONSENT-1 and K-UNTYPED-1 added |
| Contract pins | `PASS` — all 83 equal `842bf170…` |
| Decomposition pins | `PASS` — all 83 equal `932b890e…` |
| Source anchors | `PASS` — 83/83 resolve to the matching invariant in the reconstructed contract |
| Contract/register ID parity | `PASS` — exact 83-ID set equality |
| Phase-2 row delta | `PASS` — 82 rows change only `ContractSourceSHA256`; K-CONTROL-1 changes only six declared fields |
| DEL-03-04 repair | `PASS` — retained in both K-EVENT-3 carrier cells |
| K-CONTROL-1 status | `PASS` — `MAPPED_WITH_OPEN_ISSUE` |
| K-CONTROL-1 open issues | `PASS` — `RUNTIME-OPEN-005;DEL-02-07;WP-03` |
| K-CONTROL-1 provenance | `PASS` — `EXTERNAL_ROOT_AUTHORITY` |
| Duplicate IDs | `PASS` — none |

## Protected-surface checks

- live App contract remains `6d3a082c…`;
- live companion register remains `84d6fe00…`;
- `_ScopeChange/_LATEST.md` remains `a0298fdc…`;
- App Task Management register remains `eb37fba1…`;
- frontend tree remains `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`; and
- N1 and N2 candidate identities remain `cf889103…` and `c6b6d314…`.

The candidates make no application, implementation-coverage, lifecycle,
pointer, notice-routing, release, publication, or foreign-loop claim.
