# QA Report

## Deterministic Tooling

- Native schema validation: 51/51 pass.
- Native closure analysis: complete; see `Evidence/closure_summary.json`.
- App-local strict validation: 5/51 pass, 46 fail, 503 errors. Failures are strict `DependencyID` format hygiene, not graph-edge evidence changes.

## Coverage

- Dependency files: 51
- Total dependency rows: 554
- Anchor rows: 244
- Execution rows: 310
- IMPLEMENTS_NODE anchors present: 51
- Evidence populated: 554/554

## Graph Health

- Active deliverable graph nodes: 46
- Active deliverable graph edges: 114
- SCC count: 2
- SCC sizes: [18, 2]
- Orphans: 5
- Bidirectional pairs: 13
- Hubs: 0

## Limitations

The native closure tool uses a header/version schema check and is compatible with dependency-extract governance. The app-local strict linter enforces an additional `DependencyID` pattern and currently fails many files. This snapshot reports that discrepancy but does not normalize IDs.
