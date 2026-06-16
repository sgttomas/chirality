# Local Indexes (derived)

Generated source catalog + retrieval snapshots for the `chirality-app-dev`
domain pack. **Derived and rebuildable** — not authoritative source truth and
ignored by git except for this README and the `.gitkeep` placeholder.

Built at Phase 2.5 (after Gate 2) by:

```sh
python3 ../../tools/source_catalog/build_source_database.py \
  --domain-root domains/chirality-app-dev \
  --repo-root projects/chirality-app-dev \
  --source-manifest domains/chirality-app-dev/_Sources/Source_Manifest.csv
```

Not yet built at Gate 1.
