# Analysis Checks

- Analyzer unit tests: `3 passed`.
- Source population: 10 packages / 3 waves / 47 members.
- Package status schema variants: normalized without dropping members,
  mappings, source lines, replacement rows, rollback rows, or project writes.
- Event catalog: 43 unique rows; every evidence path exists; every exact text
  needle resolves; normalized output records evidence SHA-256 and line.
- Project checks: 67 invocations; heterogeneous `results`/`checks` and
  `id`/`check` schemas normalized; 60 timed and seven explicitly untimed.
- Git windows: all three basis, evidence-binding, and merge commits resolved;
  no negative interval.
- RECON: 47/47 apply and rollback simulations reproduced from terminal status.
- Output idempotence: PASS; an immediate rerun reproduced every output hash.
- Snapshot manifest: 3/3 path/hash/byte bindings reproduce; manifest SHA-256
  `2c811150735678b0c5e570c0f23f8ff502ec9d3bb57b4ef4d233c56357f7e890`.
- Python AST parse and scoped `git diff --check`: PASS.
- Scope: no source-run, project, plan, candidate, lifecycle, H1/H2, or
  integration write.
