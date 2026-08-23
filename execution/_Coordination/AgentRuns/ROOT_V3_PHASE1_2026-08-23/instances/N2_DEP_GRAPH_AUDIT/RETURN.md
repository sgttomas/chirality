# N2 graph and dependency-closure terminal return

Verdict: `PASS_WITH_COVERAGE_WARNINGS`

Role entry was instruction-asserted. This bounded Agent 2 did not delegate.

## Graph result

- Exact node set: `PASS` — 59 nodes = 53 applied register deliverables + 6 packages.
- Structural edges: 53 package-membership edges, all non-gating.
- Declared sequencing dependency edges: 0; none inferred.
- SCCs: 59 singleton; non-trivial SCCs: 0; cycle edges: 0.
- Cycle disposition: no move required; no human-gated cut/merge was made.
- `WORK_GRAPH.json` SHA-256: `e36cac85ef02237db7e249a57f1b88f2cd06290db4c1d607de65b78d038cc52e`.
- `DAG.md` SHA-256: `d699b95f750fcc485e79f03ec616fbba7db35f8437e3506bc42b3ad1055c5281`.
- `SCC_Report.md` SHA-256: `f8e3f0e9f46bbd2855d8117a736a7cfd6d5b66d380572babe39fde4815e5e43e`.
- Complete graph artifact manifest SHA-256: `675357b85e806631014531de2df0fc6c02e026fc6c8bf82b4e6131d0ef416955`.

## Audit result

- Verdict: `WARNING` with zero failures and zero blockers.
- Live coverage: 53/53 deliverables and 6/6 packages resolve.
- New INIT state: 7/7 `OPEN` with explicitly initialized-empty dependencies;
  expected, not a defect.
- Pre-existing state: 46/46 remain dependency extraction `NOT_RUN_YET` with no
  declared edge.
- Closure: 0 execution edges, 0 orphan dependency targets, 53 singleton
  deliverable SCCs, 0 cycles, 0 hubs, 0 bidirectional pairs.
- Prior comparison: 0 unresolved closure violations among pre-existing folders;
  prior Gate-1 audit also had 0 blockers and 0 warnings.
- Coverage warnings: 0/53 extracted `Dependencies.csv` schemas and 0/53
  extracted `ANCHOR/IMPLEMENTS_NODE` rows. These await the separately gated
  SOW/dependency-extraction act.
- `closure_summary.json` SHA-256: `6dc2838ef5f354c00b7c31750212524a92aa67b0a5c26c7e07345749d3567660`.
- `Dependency_Closure_Report.md` SHA-256: `e47f42f3e4daba0ac1982b8e839b56d246c13d1462f713521a2ef2a5bec3f890`.
- Audit `RETURN.md` SHA-256: `d4a3c659c3f8a3384c9fa752b2672e822ac4b8da10f9d6f55fcec26f21e1a070`.
- Complete audit artifact manifest SHA-256: `d14bf4812cfdfa8d633eeeeff42349eb9ef49546b56b2ef7b542bdd1e1536234`.

Every created evidence-file identity is recorded in the two
`ARTIFACT_HASHES.csv` manifests at those exact manifest identities.

## Reproducibility and checks

- `derive_graph.py`: two consecutive reruns reproduced every graph artifact
  byte-for-byte.
- Repository `tools/coordination/analyze_dep_closure.py`: invoked with the
  human-authorized output override; its raw outputs are preserved under
  `Generic_Tool_Raw/` and correctly show that the generic tool finds zero Root
  `Dependencies.csv` inputs.
- `analyze_closure.py`: two consecutive reruns reproduced every audit artifact
  byte-for-byte and supplies the Root register + `_DEPENDENCIES.md` binding the
  generic tool lacks.
- Evidence-whitespace V2: `normalize_generic_raw()` converts every raw generic
  CSV to LF and ensures terminal LF on all six CSVs plus the raw JSON. Two
  consecutive reruns reproduced the normalized identities byte-for-byte.
- JSON parse: `PASS` for `WORK_GRAPH.json` and `closure_summary.json`.
- `git diff --check`: `PASS`.
- `validate_candidate_whitespace.py --base-ref origin/main`: `PASS`.
- Protected surfaces: no live decomposition, pointer, deliverable metadata,
  Task Management, prior graph/audit, tool, runtime, project, or docs write.
- Output-location override: no `_Evaluation/DepClosure` or pointer write.

## Derivative status and blockers

Both evidence packages cite accepted SCA-004 revision 1.3, all seven applied
decomposition identities, N1 commit `dab470e2f0c7345f10c34bcce9e489eb68bf0541`,
N1 return SHA-256 `71a4d6b9089f4b7a01581ba7ce8787915dba9e10aaed7fdc92e1c8a77ad28e50`,
and fresh-review SHA-256 `9f567edcd6687b936838ad4b80204a4766b2635b6920cf524e034cf72bb569d2`.
They are derivative evidence, never decomposition authority, and must be
re-derived after accepted SOWs and dependency extraction.

Blockers for this N2 tranche: none. Remaining gated work is accepted SOWs,
dependency extraction, and the required graph/audit rerun. Any future SCC cut
or merge remains owner-gated.

## Repair V2 — evidence-whitespace normalization

Fresh review cycle 1 found one formatting-only defect. Amendment V2 normalized
the seven generic-tool raw preimages and cascaded only dependent evidence/hash
citations. Graph bytes, audit verdict/metrics, and protected surfaces remain
unchanged.

| File | Before SHA-256 | After SHA-256 |
|---|---|---|
| `Generic_Tool_Raw/bidirectional_pairs.csv` | `e0fcf0084fce3ec4ebb162e6d9e7430e6bde0eeb759307d8b6716301cf950c59` | `96763837f083b613c05053bee7e700c98f7abff516e73ecc31d7ba6589143243` |
| `Generic_Tool_Raw/closure_summary.json` | `01fde24a5a86e9e335e31e4f9fb48997594140100a00e65597014f71a0ab10b7` | `183b06cd6b9a27e3b80702d8aa5acd706cfe6425522b65b1b2b1380c110c6d38` |
| `Generic_Tool_Raw/coverage.csv` | `71b044faf99f4ff079153d5497519885b30fd4a3bce20abd408d1609eae69500` | `1704c0539a74cf9f1674c6e76e0cf3400f5b67b2972791b3562ad2c128b1cce7` |
| `Generic_Tool_Raw/hubs.csv` | `461b09cff46fadec5ae392e5feae820b87bd608ec22935ff7eb4e33c5fb9b5c0` | `2a8f48c7ddbe9ae0266d826695bd86419362cb584f503b09d373e0128c49b955` |
| `Generic_Tool_Raw/id_normalization.csv` | `1e1dc4b14515b25fd32c69e7b965d4e9ba4f5489ce3ea5d46fad2e9c938dd2f3` | `24820fc7cf0c53df91c2616321418bd6684c723bc71109267ef98a25ca94fd9c` |
| `Generic_Tool_Raw/orphans.csv` | `2f5dc27ce8e121fe54a0fbab33c2de421476e1adc67f8da7a11104e82b3410fa` | `1867026637b5d4943e54be975737a01e475c78e149cf23789c816c3e19e6770c` |
| `Generic_Tool_Raw/scc_summary.csv` | `1cd736c87b44cb483cf3cd64a2376a19821a7f50fe6b6dbaadb842ba21b20e7d` | `2951a8e40268d483dba0101bd83e04c53ccf3236818353af6b3039c68d896578` |
| `analyze_closure.py` | `54b22783ec0d2956e09bc54cd2e0e5666e7acd03987aab5c6a94ee8b43aee6c2` | `7cb890efeb17b52bbe60de6fc532b1024b0db2d5456598d968c313c0cf798228` |
| Audit `Decision_Log.md` | `ef4755750d3c8aec123f6d620ff1bee2c0953540d3417fc18784e983db379232` | `e53702b2b8a734041272d189902435f5f7c46bd0df12bd6373f65202cdf3f0c4` |
| Audit `closure_summary.json` | `a7f09f3f2690312a40630f35bf78b675cdadd63535ca46cabea5b97d4a90ee71` | `6dc2838ef5f354c00b7c31750212524a92aa67b0a5c26c7e07345749d3567660` |
| Audit `RETURN.md` | `b78e6987910915adccf386f5cd99f85eb778c9ec04d8e877b2a42275156e8313` | `d4a3c659c3f8a3384c9fa752b2672e822ac4b8da10f9d6f55fcec26f21e1a070` |
| Audit `ARTIFACT_HASHES.csv` | `21990f80e3b365deed3a03bb3128b5352bb1bd22836ac57b342ac8d7aaa8b42e` | `d14bf4812cfdfa8d633eeeeff42349eb9ef49546b56b2ef7b542bdd1e1536234` |
