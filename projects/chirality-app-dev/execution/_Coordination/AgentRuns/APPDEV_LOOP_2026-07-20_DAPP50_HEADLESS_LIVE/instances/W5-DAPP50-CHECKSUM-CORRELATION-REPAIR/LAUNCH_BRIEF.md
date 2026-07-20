# W5-DAPP50-CHECKSUM-CORRELATION-REPAIR — WORKING_ITEMS Brief

- **Role:** WORKING_ITEMS
- **Package:** `PKG-10_Domain_Engine_Future_Boundary`
- **Selected deliverable:** `DEL-10-01_DomainEngineProfile_Contract_Draft`
- **Required branch/HEAD:**
  `codex/app-dev-dapp50-headless-live-20260720` /
  `fcf152bdae1e1764b11dfabf3f87d50c5680213d`
- **Posture:** serialized two-file repair; delegation prohibited
- **Objective:** cure only V2-F-001 and return commit-ready bytes.

Read full `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, update v9, V2's complete
evaluation and terminal records, W3/G1 repair evidence, the two live target
files, frozen `schemas/headless_runner.schema.yaml`, final Rust
`core/runner/headless/src/lib.rs` checksum validation, and TP-RUNNER-015 exit-0
witness. Reproduce basis/topology, V2 hashes/finding, current two target hashes,
empty index, contained dirty state, and `frontend/dist` absence. Return `BLOCK`
before writes on mismatch.

## Exact write authority

Edit only:

1. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`;
2. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`;
3. this instance's terminal `RETURN.md`, `HANDOFF.md`, and `STATUS.json`.

Require `runner_result.checksums` to contain at least one complete checksum with
`payload_ref.ref_type === "result_envelope"` and `payload_ref.ref_id` exactly
equal to `runner_result.result_envelope_ref.envelope_ref.ref_id`, matching the
final Rust `has_result_envelope_checksum` condition. Preserve every existing
structural, token, boundary, exit-correlation, and transport check. Do not add
solver-semantic validation or broaden the transport contract.

Correct the positive fixture to contain a matching result-envelope checksum.
Add adversarial cases proving failure when: only unrelated checksums exist;
the `ref_id` mismatches; and the `ref_type` is not `result_envelope` despite a
matching id. Preserve positive acceptance with additional unrelated complete
checksums. Tests must exercise the real configured-process transport and
assert sanitized fail-closed behavior.

## Required validation

- focused repaired runner suite;
- generated catalog test;
- full frontend suite, typecheck, production build, and managed premerge;
- D-APP-48 validator and dependency lint (the current contract still pins G1
  and must remain unchanged in W5);
- receipt validator, authority corpus v9, repository self-check, validation
  pytest, practitioner-harness pytest;
- exact tracked/untracked/ignored/cached/staged/no-index/whitespace/write-scope
  containment; `frontend/dist` absent; stop only an owned server.

Do not edit status/run records/receipts/contracts/decisions/prior controls or
evaluations, other source, piping/tier-0/PEC, ignored/build outputs beyond
ordinary required build/test refresh, or any unrelated path. Do not package,
clean, stage, commit, push, PR, merge, repin, change lifecycle, expand
authority, waive a gate, or make release/professional/solver-truth claims.

Return `REPAIRED_AWAITING_G2_COMMIT | BLOCK` with exact before/after target
hashes, test counts, containment, blockers/unknowns/conflicts/waivers, and G2
as the only next gate on success.
