# VERIFY-B1 Independence-Scope Incident

Timestamp: `2026-07-15T01:17:44Z`

Disposition: `TERMINAL BLOCKED`

The verifier brief permits reading the author child folder only through the
parent-owned `B1_AUTHOR_ACCEPTANCE.md`. During initial path discovery, the
following exact read-only command was invoked:

```sh
find execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P3/PIP-PKG12 -maxdepth 3 -type f | sort; sed -n '1,80p' execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P3/PIP-PKG12/CANDIDATE_MANIFEST.tsv 2>/dev/null || true; sed -n '1,60p' execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P3-PKG12/children/AUTHOR-B1/CANDIDATE_MANIFEST.tsv 2>/dev/null || true; rg -n '^DEL-12-' execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P3/preflight/P3_MANIFEST.tsv
```

The first candidate-local manifest path did not exist. The second `sed`
operand read and emitted the author-owned `CANDIDATE_MANIFEST.tsv` header and
15 entries. That information consisted of candidate paths, SHA-256 values,
and byte counts, but the read itself violated the sealed independence boundary.

No semantic verification had begun. The instance stopped semantic work after
the incident was identified and notified the parent. No candidate, author, or
live-project file was written or repaired. Because knowledge obtained outside
the permitted independent basis cannot be removed from this running instance,
`PASS_UNCHANGED` is unavailable regardless of subsequent deterministic checks.

Rerun requirement: discard this verifier result for acceptance and dispatch a
new fresh evidence-only verifier instance with a new owned evidence folder.
The rerun must read only the candidates, exact live sources, accepted W-P3
rows, normative method/tool sources, parent package records, and
`B1_AUTHOR_ACCEPTANCE.md`; it must not enumerate or read any other path beneath
`children/AUTHOR-B1/`.
