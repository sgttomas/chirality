# W5 D-APP-50 Checksum-Correlation Repair Return

## Terminal result

`REPAIRED_AWAITING_G2_COMMIT`

V2-F-001 is repaired within the exact two-path scope. There are no blockers,
unknowns, conflicts, or waivers. G2 commit-only publication is the sole next
gate; repin/correction, fresh evaluation, and final publication remain held.

## Basis and provenance

- Branch: `codex/app-dev-dapp50-headless-live-20260720`
- Required and reproduced HEAD:
  `fcf152bdae1e1764b11dfabf3f87d50c5680213d`
- Role: WORKING_ITEMS, sole serialized integration owner; no delegation
- Update v10 and Amendment v2 confirmed that the interrupted first W5 manager
  authored the unvalidated two-file candidate and ran no completed test.
- This manager independently inspected and validated the candidate and made no
  further source edit.
- Git action: none; index remained empty.

## Repair

The adapter now requires `runner_result.checksums` to contain at least one
complete checksum whose `payload_ref.ref_type` is exactly `result_envelope` and
whose `payload_ref.ref_id` exactly equals
`runner_result.result_envelope_ref.envelope_ref.ref_id`. This matches the final
Rust `has_result_envelope_checksum` predicate without adding solver-semantic
validation or broadening the transport contract.

The positive configured-process fixture contains the matching checksum plus an
unrelated complete request checksum. Real configured-process adversarial cases
assert sanitized `HEADLESS_RUNNER_RESULT_SCHEMA_MISMATCH` refusal when only
unrelated checksums exist, the result-envelope reference id mismatches, or a
matching id has the wrong reference type. Every prior structural, token,
boundary, exit-correlation, and transport check is preserved.

| Path | G1 SHA-256 | W5 SHA-256 |
|---|---|---|
| `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` | `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109` | `29b3093e8835002274c859195c31e46a2bf9db597226fee759c347270b5d5df1` |
| `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` | `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41` | `67e962ddbf721b340f1340633c2f66d121b2b65d169a087a5a163d62238973b4` |

## Validation

- Focused configured runner suite: PASS, 51/51.
- Generated tool-catalog suite: PASS, 2/2.
- Full frontend suite: PASS, 779 passed / 4 skipped across 98 passed and one
  skipped test file.
- Frontend typecheck: PASS.
- Production Next/Electron build, without packaging: PASS.
- Managed premerge: PASS, Section 8 8/8 and Section 9 16/16 report-only; the
  W5-owned Next server was stopped.
- D-APP-48 pull-contract validator and harness dependency lint: PASS. The
  contract remained at SHA-256
  `e01120ad843578813a558a2f9bffbf6a7504dc8d294eff983f27482dc201caa6`
  and still pins G1.
- App-dev receipt validator: PASS; ledger remained at SHA-256
  `819be78ee30629d5ef1b54814d6d4f849cd5816e675b8fc79899bb97cb12e2e8`.
- Authority corpus v9: PASS, 8/8 match and no drift.
- Repository self-check: exit 0 at the existing 3 REVIEW / 6 WARN baseline.
- `tools/validation` pytest: PASS, 123/123.
- `tools/practitioner_harness` pytest: PASS, 311/311.
- Final branch/HEAD, exact target hashes, empty index, tracked/cached
  whitespace, frontend-source write fence, ignored-output distinction, and
  process checks: PASS. `frontend/dist` remains absent; ordinary ignored
  `.next`, `dist-electron`, and harness artifacts remain distinct.

## Containment and boundaries

W5's subject writes are exactly the adapter and focused test, plus this
instance's three terminal records. Existing W2/W4 closeout dirt, both prior run
records, the run control/evaluation packages, and ignored build outputs were
not adopted as W5 writes. No contract, receipt, status, decision, prior control
or evaluation, other source, piping/tier-0/PEC surface, packaging output,
lifecycle state, or release surface was edited by W5.

No packaging, cleanup, staging, commit, push, PR, merge, repin, lifecycle
transition, waiver, or professional/solver-truth claim occurred. The only next
gate requested is G2 CHANGE commit-only publication of the exact two repaired
tracked files.
