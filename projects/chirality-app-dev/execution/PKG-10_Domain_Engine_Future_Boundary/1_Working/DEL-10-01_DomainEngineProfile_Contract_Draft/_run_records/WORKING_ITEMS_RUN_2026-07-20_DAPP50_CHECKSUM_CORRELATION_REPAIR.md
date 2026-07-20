# WORKING_ITEMS Run — D-APP-50 Checksum-Correlation Repair Correction

**Date:** 2026-07-20

**Package:** PKG-10 — Domain Engine Future Boundary

**Deliverable:** DEL-10-01 — DomainEngineProfile Contract Draft

**Authority:** D-APP-50 Option A and riders; W6 release in control update v12

**Repair commit:** `55a066fdff6877d8aa2a49ce08a545ac98872848`

## Purpose and preserved history

This record corrects the reachable private pull-contract pin after fresh independent
V2 evaluation blocked the W4 correction. It supplements rather than rewrites the W2
and W4 records: Receipts 83 and 84 and both earlier DEL-10-01 D-APP-50 run records
remain immutable evidence of the bases evaluated by V1 and V2.

The V2 evaluation package
`execution/_Evaluation/DAPP50_HEADLESS_LIVE_REPAIR_BACKCHECK_FCF152B_2026-07-20/`
returned `BLOCK` with finding `V2-F-001`. The adapter accepted an exit-zero result
whose declared result envelope had no matching checksum reference. This was a
deterministic nested transport/result correlation defect, not an exhaustive
solver-semantic finding. V1 F-002 remained cured and `frontend/dist` remained absent.

## W5 bounded repair evidence

W5 repaired exactly two paths:

1. `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` — SHA-256
   `29b3093e8835002274c859195c31e46a2bf9db597226fee759c347270b5d5df1`.
2. `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` — SHA-256
   `67e962ddbf721b340f1340633c2f66d121b2b65d169a087a5a163d62238973b4`.

The adapter now requires at least one complete checksum whose payload reference type
is exactly `result_envelope` and whose reference id matches the declared result-envelope
reference id. The focused suite passed 51 tests, including real configured-process
refusals for unrelated checksums, a mismatched reference id, and a matching id with
the wrong reference type. Prior structural, token, boundary, exit-correlation, and
transport checks remain in force. W5 reported no blockers, unknowns, conflicts, or
waivers and performed no Git action.

## G2 reachable repair

G2 created commit `55a066fdff6877d8aa2a49ce08a545ac98872848` with single parent
`fcf152bdae1e1764b11dfabf3f87d50c5680213d`. The commit contains exactly the two
W5 paths above at the recorded SHA-256 values. The G2 terminal RETURN, HANDOFF, and
STATUS hashes are respectively
`1be55b497981176ba64c4ee007facbb8b02b2c5fe86f0fbf5c9aebfcc232e95e`,
`853873432917c30f276a96646ae82f0ad38a779ced135756afaec6e0030001e3`, and
`84d27d72cc297992cb47ef962ff51b0f1dc00b97a439b5c46085c05054eb20b3`.

## Corrected D-APP-48 pin

W6 changes only `source.commitSha` in the D-APP-48 private intra-repo pull contract,
advancing it from G1 to the reachable G2 repair commit. Registry version, package
identity, constants, export list, order, targets, hashes, validation commands, and
every boundary flag remain byte-for-byte unchanged. The two repaired paths are
runtime/test files rather than package exports, so the existing export hashes remain
current at G2.

## Validation and boundaries

W6 gates strict duplicate-key JSON, deterministic pull-contract validation, recorded
dependency lint, the focused 51-test suite, receipt validation before and after the
append, authority corpus v9, repository self-check, validation and practitioner-harness
pytest baselines, exact topology/hash/diff/no-index/cached/staged/whitespace/write
containment, and continued absence of `frontend/dist`.

D-APP-50 remains a read-side `open_pipe_stress` headless-preview exposure. No apply or
proposal transport, protected-path write, piping/tier-0/pec change, provider/network
expansion, packaging, release, publication, distribution, lifecycle transition, waiver,
or professional/certification/sealing/authentication/code-compliance/solver-truth claim
is created. DEL-10-01 remains `IN_PROGRESS`; its complete Remaining section and
Checking Approval SHA are unchanged.

The sole next gate is fresh independent V3 EVALUATION of G2 plus this correction.
Final publication remains held until V3 accepts.
