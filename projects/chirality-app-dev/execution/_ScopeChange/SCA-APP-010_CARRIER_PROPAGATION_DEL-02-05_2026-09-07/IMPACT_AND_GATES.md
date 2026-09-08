# Runtime/App SOW propagation impact and gates

Status: `CANDIDATE_ONLY__UNAPPLIED`.

This append-only v2 successor closes review-v1 findings F-001 and F-002. Relative to author-v1 candidate SOW bytes, only Runtime DEL-02-06 `CLM-003` authority attribution and App DEL-02-05 `REQ-001` typed Runtime projection ownership change. Runtime DEL-02-09 is byte-identical to author-v1.

The candidate changes only the published Runtime account-authority propagation surface and the corresponding App consumer contract. Runtime DEL-02-06 changes only `CLM-003` and `REQ-010`. Runtime DEL-02-09 changes only `REQ-001` and `REQ-002`. The App DEL-02-05 postimage makes targeted changes to its controlling responsibility and acceptance text, `REQ-001`, `REQ-005`, `AC-002`, `VER-002`, and the `OUT-002` evidence expectation. All other accepted text and identifiers are preserved.

Runtime acceptance remains under Runtime SCOPE_CHANGE and the Runtime SOW owner:

1. **Gate 2 — impact acceptance:** accept the bounded two-SOW impact and the continued conservation of one Runtime SOW-104 row, seven carriers, four objectives, 66 qualified inherited requirements, nine holds plus separate R16-B, historical basis, and `root-runtime-1` epoch 1.
2. **Gate 3 — exact SOW approval:** approve the exact complete DEL-02-06 and DEL-02-09 postimages and `RUNTIME.patch` by hash.
3. **Gate 4 — application, snapshot, and audit plan:** authorize exact application to the two Runtime SOW paths, creation of a new immutable accepted snapshot, required pointer update only if the owning workflow permits it, deterministic checks, independent audit, and an explicit handoff state.

The Runtime candidate does not become accepted or effective merely because it is reviewed. Application, snapshot creation, audit, and closure require their owning acts.

App propagation is separately owned. The App owning workflow must accept the exact DEL-02-05 postimage and `APP.patch` by hash, apply it through its own authorized process, create its own immutable accepted snapshot, and record its own audit and closure status. Runtime acceptance cannot amend App scope, and App acceptance cannot amend Runtime scope.

Cross-project concordance becomes effective only after both accepted snapshots exist and the Runtime/App integration owners bind their exact identities in a conflict-free concordance record. Until then, this handoff is candidate coordination evidence only.

No source, supplier, account, credential, process, implementation, build, test, qualification, trial, lifecycle, hold, hosted-readiness, release, publication, pointer, or Git act is performed or authorized by this packet.
