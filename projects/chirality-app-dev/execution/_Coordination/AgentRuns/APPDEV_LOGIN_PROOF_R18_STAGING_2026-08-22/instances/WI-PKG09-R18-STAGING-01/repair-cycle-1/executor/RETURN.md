# A2-PKG09-R18-WS-REPAIR-01 return

Status: `REPAIR_PASS`

The five authorized evidence files were mechanically normalized from exact,
pre-verified frozen bytes. Deterministic compressed preimages and the complete
pre/post hash, size, and deletion-count lineage are in `preimages/`,
`PREIMAGE_SHASUMS256.txt`, and `LINEAGE.md`. Normalizing each decompressed
preimage deterministically equals its repaired target byte-for-byte.

Executor-owned writes were exactly:

- the five targets named in the sealed brief;
- `repair-cycle-1/executor/LINEAGE.md`;
- `repair-cycle-1/executor/PREIMAGE_SHASUMS256.txt`;
- `repair-cycle-1/executor/CHECKS.md`;
- `repair-cycle-1/executor/RETURN.md`;
- five `.gz` files under `repair-cycle-1/executor/preimages/` corresponding
  one-for-one with the five repaired targets.

All required whitespace, staged-equivalent new-file, diff, containment, JSON,
semantic-hash, immutable-review-hash, equivalence, and empty-index gates pass.
No test, build, package, network, proof, receipt, stage, commit, push, PR, or
merge action occurred. The original full-suite result remains historical and
was not rerun or upgraded. A genuinely fresh evidence-only lineage/whitespace
review remains required before manager fan-in.
