# N4 Repair Cycle 1 — CRLF-to-LF Evidence Lineage

**Scope:** exactly six record-only CSVs in the immutable named closure-audit
package and its `MANIFEST.sha256`.

## CSV lineage

| Evidence file | Pre SHA-256 / bytes / CR | Post SHA-256 / bytes / CR | Parsed rows / data rows | Semantic comparison |
| --- | --- | --- | ---: | --- |
| `Evidence/bidirectional_pairs.csv` | `93fea38e2e8f109b4213960c3f1429988f16646ca385d6668597441f026d7dd8` / 34 / 2 | `fc8d468c5226c825760791d6e4811226fa1fe6b260e456131f80dcaba2ea55f5` / 32 / 0 | 2 / 1 | parsed rows exactly equal |
| `Evidence/coverage.csv` | `29cbd96607697e0fe019c9ba5e98c448e8f9eee02a25fec67ff8520d62bd47a9` / 1074 / 52 | `f760cd1060663149f844862f15cdcfc9210066f1b945e34456fc84f490f96658` / 1022 / 0 | 52 / 51 | parsed rows exactly equal |
| `Evidence/hubs.csv` | `461b09cff46fadec5ae392e5feae820b87bd608ec22935ff7eb4e33c5fb9b5c0` / 46 / 1 | `2a8f48c7ddbe9ae0266d826695bd86419362cb584f503b09d373e0128c49b955` / 45 / 0 | 1 / 0 | parsed rows exactly equal |
| `Evidence/id_normalization.csv` | `1e1dc4b14515b25fd32c69e7b965d4e9ba4f5489ce3ea5d46fad2e9c938dd2f3` / 32 / 1 | `24820fc7cf0c53df91c2616321418bd6684c723bc71109267ef98a25ca94fd9c` / 31 / 0 | 1 / 0 | parsed rows exactly equal |
| `Evidence/orphans.csv` | `b6c339528acf05ac83267821a1b37134ebd19c4ef8c79408ba2ab3ffdf076e95` / 70 / 6 | `e407f0945467ce4600d08bba0dca9b45504728dcbf5a105e3fdb794784f53679` / 64 / 0 | 6 / 5 | parsed rows exactly equal |
| `Evidence/scc_summary.csv` | `bdb6da3782a576c602072c9b40574b5f2c2112619b5ab02973ff8a381dcb8226` / 120 / 2 | `348508f92d0033220fd7cfbc8770f47df35af8218ff0f1bd7aa246016d3dc8e3` / 118 / 0 | 2 / 1 | parsed rows exactly equal |

For every file, the post-image equals the pre-image with only each `CRLF`
sequence changed to `LF`. No other byte was removed, inserted, reordered, or
changed. CSV parsing before and after produced exactly equal row/cell arrays.

## Mandatory ordering evidence

Immediately after the six normalizations, and before regenerating any pinning
artifact, this command returned exit 0:

```text
python3 tools/validation/validate_candidate_whitespace.py --base-ref cc196023a5532fe58955655c1144cd09ee88343a
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

## Manifest lineage

`MANIFEST.sha256` changed only its six entries for the repaired CSVs:

- pre: `1b50536809996025f6476e08c475b242a2113932c9a8b2dbdbd9156d93ca7012`,
  1421 bytes, 16 entries;
- post: `7c30c9e2244beca0a9d8182e1908ce188cba48ea87b919b5da16f3a83423077d`,
  1421 bytes, 16 entries.

All 16 post-manifest entries were independently rehashed against their named
regular files and matched. The other ten manifest rows and their content bytes
are unchanged.

## Audit consistency

The repair does not change audit semantics, counts, or verdict:

- `Dependency_Closure_Report.md` remains
  `540d50daaceaa5d09bcae41128c4f5b6eb2486649fdf41378b091e00fdbd4f7f`;
- `Dependency_Closure_IssueLog.csv` remains
  `b3fe661e45c1a4536956fb3a19f8381232fe1d840f1549e0b9ca0f8046a5f95d`;
- `Evidence/closure_summary.json` remains
  `88e07de9d40a9fa659c10301c1eef28bf48d0cd2ace8b5dcc120d2c38e72d662`;
- verdict remains `WARNINGS`, non-blocking;
- 51/51 registers remain schema-valid, 564/564 evidence rows remain populated,
  112/112 ACTIVE endpoints remain resolved, with one nine-node SCC, five
  isolates, and one bidirectional pair.

No other audit/content byte was changed.
