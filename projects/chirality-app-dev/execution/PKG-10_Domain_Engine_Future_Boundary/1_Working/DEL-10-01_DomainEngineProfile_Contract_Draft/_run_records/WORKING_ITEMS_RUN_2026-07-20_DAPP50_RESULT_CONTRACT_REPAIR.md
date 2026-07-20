# WORKING_ITEMS Run — D-APP-50 Result-Contract Repair Correction

**Date:** 2026-07-20

**Package:** PKG-10 — Domain Engine Future Boundary

**Deliverable:** DEL-10-01 — DomainEngineProfile Contract Draft

**Authority:** D-APP-50 Option A and riders, W4 release in control update v7

**Repair commit:** `fcf152bdae1e1764b11dfabf3f87d50c5680213d`

## Purpose and preserved history

This record corrects the reachable private pull-contract pin after independent V1
evaluation blocked the original W2 closeout. It supplements rather than rewrites W2:
Receipt-83 and `WORKING_ITEMS_RUN_2026-07-20_DAPP50_HEADLESS_PREVIEW_LIVE.md`
remain immutable evidence of the first closeout, including the basis evaluated by V1.
W4 changes no implementation or test byte.

The V1 evaluation package
`execution/_Evaluation/DAPP50_HEADLESS_LIVE_BACKCHECK_F67D4470_2026-07-20/`
returned `BLOCK` with two findings. F-001 identified incomplete fail-closed validation
of the complete DEC-065 result contract. F-002 identified material ignored packaging
residue left by a cancelled packaging attempt. That failed evaluation remains derivative
evidence; it is not replaced by this repair record.

## W3 repair and cleanup evidence

W3 repaired only:

1. `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` — final SHA-256
   `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109`.
2. `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` — final SHA-256
   `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41`.

The repaired adapter now validates the exact app-facing DEC-065 `solve` result
contract fail-closed: exact top-level identity and allowed-key sets; complete local-process
policy; typed validation objects and diagnostics; complete runner-result members and nested
records; analysis/result/audit/checksum/privacy/provenance/professional-boundary shapes;
unknown-key rejection; and exit/result correlation. Exit zero requires a completed,
non-blocking, structurally complete result; exit one requires a blocking diagnostic; schema
defects retain the stable refusal contract. The scope remains result validation only—no
descriptor, registry, transport, profile, proposal, apply, or permission change.

W3 also removed exactly the V1-authorized `frontend/dist/**` target after validating its
identity and containment. That deleted directory was ignored generated packaging residue.
It is reproducible only by rerunning packaging and is not Git-restorable. W3 did not delete
the distinct normal-build outputs `.next` or `dist-electron`, and W4 confirms
`frontend/dist` remains absent without running a packaging command.

## G1 reachable repair

G1 created one local commit with single parent
`f67d44706f4b2b5495833f809cb0bc714d2bbc18`. Commit
`fcf152bdae1e1764b11dfabf3f87d50c5680213d` contains exactly the two repaired paths
at the SHA-256 values above. No other dirty closeout, control, evaluation, receipt, or
generated-output path entered that commit; the index was empty afterward.

## Corrected D-APP-48 pin

W4 changes only `source.commitSha` in the D-APP-48 private intra-repo pull contract,
advancing it from the original G0 implementation commit to the reachable G1 repair commit
`fcf152bdae1e1764b11dfabf3f87d50c5680213d`. Registry version
`harness-tools.v14.headless-preview-live`, package identity, constants, export list/order/
targets/hashes, validation commands, and every boundary flag remain byte-for-byte
unchanged. The two repair paths are runtime/test files rather than package exports, so the
existing export hashes remain correct at the new pin.

## Validation evidence

- Required branch, repair commit, single parent, exact two-path commit population, and both
  committed blob hashes reproduce.
- W2 project and terminal hashes, V1 findings and derivative package, W3 repair/cleanup
  evidence, and G1 terminal hashes reproduce before W4 writes.
- Strict duplicate-key JSON, deterministic pull-contract validation, recorded contract
  dependency lint, focused repaired runner tests, receipt validation, authority corpus v9,
  repository self-check, validation pytest, practitioner-harness pytest, exact diff/no-index/
  cached/staged/whitespace/write containment, and `frontend/dist` absence are W4 gates.
- No packaging command, source edit, Git action, or provider/network proof is part of W4.

## Boundaries and next gate

D-APP-50 remains a read-side `open_pipe_stress` headless-preview exposure. No apply or
proposal transport, protected-path write, piping/tier-0/pec change, provider/network
expansion, packaging, publication, distribution, lifecycle transition, waiver, or
professional/certification/sealing/authentication/code-compliance/solver-truth claim is
created. DEL-10-01 remains `IN_PROGRESS`; its full Remaining section and Checking Approval
SHA are unchanged.

The sole next gate is a fresh independent V2 EVALUATION of the repaired commit plus this
correction. Final publication remains held until V2 accepts.
