# App authority corpus v21 candidate

Status: prepared and mechanically reconciled; owning-loop acceptance pending.

## Basis and membership rationale

The prior current corpus `v20` named two Root role files that no longer exist:
`AGENT_SOFTWARE_DECOMP.md` and `AGENT_DOMAIN_ENGINE.md`. The Root v3 role
registry has exactly four active roles and does not register either legacy
identifier. The Runtime context contract supplies the active role instruction
separately for each run, so adding every active role instruction to every App
deliverable's substantive source corpus would conflate runtime context with the
deliverable reference set.

Root's compatibility ledger maps `SOFTWARE_DECOMP` to `WORKING_ITEMS` plus the
`software-decomp` workflow and maps `DOMAIN_ENGINE` to `WORKING_ITEMS` plus the
`domain-engine` workflow. The two retired corpus members represented those
methods. Corpus `v21` therefore replaces them with the complete canonical
workflow closures:

- `workflows/software-decomp/WORKFLOW.md`
- `workflows/software-decomp/resources/contract.md`
- `workflows/software-decomp/resources/method.md`
- `workflows/domain-engine/WORKFLOW.md`
- `workflows/domain-engine/resources/contract.md`
- `workflows/domain-engine/resources/method.md`

The resource members are required because both entrypoints delegate substantive
inputs, output contracts, and stage methods to those files. Entry-point-only
pinning would not detect changes to the operative method basis.

Source identities inspected for this decision:

| Source | SHA-256 |
|---|---|
| `agents/registry.json` | `767fdfe25f3722b8b0428cdd4146182d54c67e0f601e11e9c3321ffc5f868cf4` |
| `docs/AGENT_WORKFLOW_RUNTIME.md` | `1889a89c0e21575738671b43be93c3df2e24937b2ded0566d158fa1ae1cd445d` |
| `workflows/legacy-agents.json` | `c632821831194002e9c976a69f3b49227aff448e18a4c803527f90c1ef23ea42` |
| `workflows/software-decomp/WORKFLOW.md` | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` |
| `workflows/software-decomp/resources/contract.md` | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` |
| `workflows/software-decomp/resources/method.md` | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` |
| `workflows/domain-engine/WORKFLOW.md` | `922b6dadbc8a8f71899954a6f7e47b45df753fb81a6ca644218a9cf642b0e94e` |
| `workflows/domain-engine/resources/contract.md` | `414cccf9805318c6a450d17077cc1091a47e82ac7be5e2ac48596a6789ac6998` |
| `workflows/domain-engine/resources/method.md` | `e3bbb3e344c7c5eb69d5288b190287595b739333b09825541f58305e20926caf` |

## Candidate effects

- `AUTHORITY_CORPUS.json` keeps versions `v1` through `v20` unchanged, appends
  `v21`, and moves `current_version` to `v21` as a candidate pointer.
- The 12-member `v21` corpus pins each workflow entrypoint and both resources
  it names, so changes anywhere in the selected workflow basis create drift.
- The reconciler uses canonical repository-relative workflow paths, recognizes
  the two retired role-file aliases only for migration, writes the successor
  path and role description, updates `refs` on future version bumps, and covers
  both current table-form and bullet-form reference records.
- The final candidate differs from the base across 168 reference rows in 52
  current deliverable `_REFERENCES.md` files: 53 table-form alias rows
  migrated; seven bullet-form rows in DEL-09-07 refreshed, including the
  remaining alias; and 108 workflow-resource rows added. No lifecycle field,
  product source, historical snapshot, or prior
  corpus version was changed.
- The `v21.binding_commit` value is the recorded preparation basis
  `c16812685831a1cae3d44bf478d08b033c605c3a`, following the existing tool's
  pre-commit capture behavior. It is not the future candidate commit or an
  acceptance identity.

## Validation

- Structural comparison of base `.versions` with candidate
  `.versions[0:20]`: byte-equal after canonical JSON serialization.
- First table-form `apply`: 53 rows across 51 files reconciled. The strengthened
  audit then exposed seven stale bullet-form rows in DEL-09-07; the follow-up
  apply reconciled all seven. Full-closure audit then exposed 108 missing
  resource rows across 52 files; the closure apply added all 108.
- Malformed/incomplete current snapshot checks now return a clear nonzero
  `INVALID CURRENT CORPUS` result instead of allowing a missing resource hash
  to reach a traceback.
- Second `apply`: 0 rows across 0 files changed.
- `audit`: all deliverable reference rows reconciled to corpus `v21`.
- `status`: all 12 `v21` members `MATCH`; no drift.
- `git diff --check` over the corpus, reconciler, README, and affected
  `_REFERENCES.md` files: pass.
- Exact postimage hashes for all 52 affected `_REFERENCES.md` files are in
  `CORPUS_V21_REFERENCE_MANIFEST.sha256`; `shasum -a 256 -c` passes for every
  entry.

## Acceptance and pointer action

This file records candidate preparation only. After the complete App/Root/
Runtime source tree is frozen, the App integration owner must rerun `status`
and `audit`, include these files in the frozen review and candidate commit, and
present that exact commit for owning-loop human acceptance. Human acceptance
must bind the exact candidate SHA. Until then, `current_version: v21` is a
candidate worktree pointer and does not supersede the accepted `v20` authority
state. No package, native adapter, supplier, publication, release, lifecycle,
or reliance state follows from this candidate.
