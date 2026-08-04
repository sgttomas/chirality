# PROJECT_SETUP — SCA-004 Metadata Alignment Manifest

**Status:** EXECUTED / VALIDATED
**Owning instrument:** PROJECT_SETUP
**Execution date:** 2026-08-03
**Branch:** `codex/pec-sca004-metadata-alignment-20260803`
**Branch basis:** `88e7590d3664d4f1daf91bed2a8899bda0748b92`

This package is derivative coordination evidence. It cites accepted upstream
truth and does not replace decomposition or SCA authority.

## Accepted basis

| Surface | SHA-256 |
|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.4 | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| `execution/_Decomposition/Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` |
| `execution/_Decomposition/ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` |
| `execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md` | `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c` |
| `COV_SCA004_POSTCHANGE_2026-08-03_1442/Decomp_Coverage_IssueLog.csv` | `8be2c2b512b83a1cd8b2c2f24630261fa0a14c219a7abdca6b76c0659d4de4b1` |

## Exact live-effect manifest

The governed live-effect set contains exactly 128 paths. Its canonical grouped,
newline-terminated path-list SHA-256 is
`1d0ce82cee00d1e66b447eff6e32062eb4038fa0564eef95a6c580f1736b074e`.
The canonical grouped order is: (1) the 63 `_CONTEXT.md` paths sorted,
excluding DEL-01-06, (2) the 64 `_REFERENCES.md` paths sorted, and (3) the
DEL-01-06 `Dependencies.csv` path last.

The exact population is resolved from the 64 actual deliverable directories
matching `projects/pec/execution/PKG-*/1_Working/DEL-*`:

1. 63 `_CONTEXT.md` paths, sorted and excluding only
   `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md`; and
2. all 64 `_REFERENCES.md` paths, sorted; and
3. `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Dependencies.csv` last.

The canonical exhaustive deliverable population is frozen in SCA-004
`Propagation_Plan.md` B1/B2. Execution proved the resolved set was exactly the
128 changed live paths with no missing or unexpected member.

## Exact transformations

- The 63 context files received only the revision-1.4/SCA-004 provenance-tail
  append. Semantic fields remained byte-equivalent to `Deliverables.csv`.
- Every reference packet's accepted-basis first bullet changed from revision
  1.3/SCA-003 to revision 1.4/SCA-004.
- DEL-01-06's reference-ledger bullet changed from `covers SOW-094` to
  `covers SOW-077;SOW-094`.
- DEL-01-06 `Dependencies.csv` gained one CRLF-terminated row,
  `DEP-01-06-003`: `ANCHOR / TRACES_TO_REQUIREMENT / SOW-077`. It is declared,
  satisfied trace metadata and not an execution edge.

## Aggregate byte guards

Component aggregate hashes concatenate members in sorted path order within each
population. The all-128 aggregate concatenates the three populations in the
canonical grouped order above: 63 contexts, then 64 references, then the
DEL-01-06 dependency register.

| Population | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|
| 63 `_CONTEXT.md` files | `81fef8f223d47088c9a15a4fce3e339923db659b2518f645039b555801672e9a` | `16dbfae64fd4ab58e7dc952c5688fec70161ca4a51395580220b3667c93c1df8` |
| 64 `_REFERENCES.md` files | `cfcebf2745e5462d22ffd7618a2643e334ffdfbce33dcafbd0d8d57b0e422839` | `98af4a4d43932c559d183d130d5523c1b5457273f3153d74f7d91f8a90ce53d7` |
| DEL-01-06 `Dependencies.csv` | `4b668218dbd9f3b5ff7ed50643cc14c969dfff3088bcd29f221537a32e4277f1` | `c733411f9d1aa300eaacd84406fc2de83a1c04d4ebd4426994c92bec90019c46` |
| All 128 live targets | `de81ba7959b0c896ba500dd89941205f1e3a9ebfbc98d0cf4d5d01d786b9e338` | `db59a07593386f52e259b413c448baf68356643d95d165b75f2ce9e015e4294a` |

No `_LATEST` pointer was created or updated.
