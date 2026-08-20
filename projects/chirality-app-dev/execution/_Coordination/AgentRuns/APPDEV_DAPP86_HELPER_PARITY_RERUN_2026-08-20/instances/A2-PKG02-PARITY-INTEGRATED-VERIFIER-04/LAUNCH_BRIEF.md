# Sealed launch brief — A2-PKG02-PARITY-INTEGRATED-VERIFIER-04

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01-AMEND03`
InstanceID: `A2-PKG02-PARITY-INTEGRATED-VERIFIER-04`
Role: fresh evidence-only Agent 2 generalist verifier
Source HEAD: `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`
Source tree: `fe8ece104dd281e3219bd95fa8b121437d524520`
Branch: `codex/app-dapp86-helper-parity-rerun-20260820`

## Objective

Independently verify the exact frozen run-root bytes after Agent 0's versioned
V4 containment disposition. Preserve V3 as rejected provenance. Determine
whether the repaired records are internally consistent, exactly hashed,
truthfully calibrated as `BLOCKED / PARTIAL`, and contained under the amended
attribution rule. Do not repair anything.

## Governing containment disposition

Read `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md` completely. Agent 0
has ruled that the Receipt 183 diff in
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` is parent-owned lawful
fan-in state, is not attributable to this package manager or its children, and
is excluded from the package write-containment judgment. You may observe its
existence but must make no judgment on its semantics. Require every write
attributable to `WI-PKG02-DAPP86-RERUN-01` and its children to be inside this
run root.

## Frozen artifacts and exact SHA-256

- Manager `RETURN.md`: `3c68a8d060e13e4e7c9d085e172ff6bcb95b1e4eb3255073bc8d028a13a9270b`
- `CLOSEOUT_AMENDMENT_01.md`: `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7`
- `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md`: `6ada335fab940c9c9265a37fa2d042fba94beff8a8f0a66df1a28c9d12e812a8`
- `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md`: `27f7fb008ffee1d2f7561ee53be39734b262e29cf37d5eb51c16da1195a8df51`
- `EVIDENCE_INDEX.csv`: `9cc9a80452c5b684d453adf23986f937eebbe582a2a67023fa27fc74f199fbf1`
- `STATUS.md`: `127f5b9b0c02842571c3f22d5a3b7432c507def9af421c7622387599b919e3af`
- `HANDOFF_STATE.md`: `da113537fa4999ef15a864ee4d1777ab9646c6b75c2363d576929deb8b5c772c`
- `REGISTERED_CHECKS.json`: `a99a5b6d9b83fecc43f35707f120c668271c018174886193ac876e2e7b1259b0`
- `RUNTIME_SUMMARY.json`: `738d5889e9ba81f1cda64779e23a1afcdb2e7ebdd3195febd3a2548847ab851c`
- E1 `RETURN.md`: `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9`
- E1 `STATUS.json`: `b175bf31f92883f52e11fe6cdae32fa01b6a8e559cdcdd2e905bf85b2ef9256e`
- V1 `RETURN.md`: `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21`
- V1 `STATUS.json`: `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1`
- V2 `RETURN.md`: `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e`
- V2 `STATUS.json`: `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832`
- V3 `LAUNCH_BRIEF.md`: `a85c2459a9761dabffe348776b56fb0724ff4799c9a39952d8e0950e938b0bd8`
- V3 `RETURN.md`: `2ca7810a2a48667ae1f63b4350f300918334edfbc183fb1acb11e5e128bdce87`
- V3 `STATUS.json`: `38bf6fd267d7f5d3be229e8db73e3dad5fa4bb87aa000a0c5deac66396d3ecfe`

## Required checks

1. Recompute every frozen hash above exactly.
2. Parse all run-root JSON. Confirm E1/V1/V2/V3 statuses use
   `chirality-agent-instance-status/v1`, are terminal, and bind the exact
   immutable child-return hashes and outcomes.
3. Parse `EVIDENCE_INDEX.csv` as six columns and exactly 22 current data rows;
   resolve every `Artifact` under the run root and recompute every indexed
   hash.
4. Confirm `REGISTERED_CHECKS.json` uses
   `chirality-software-check-evidence/v1`, binds the frozen branch/HEAD/tree,
   and records packaged UI as `BLOCKED` and premerge, release-quality, and
   secret-scan as `NOT_RUN`, never PASS. Confirm `waivers` is empty.
5. Confirm manager `RETURN.md` binds `RUNTIME_SUMMARY.json` by exact path,
   exact hash, and PASS only for telemetry-ledger completeness; confirm it
   explicitly says waivers are none.
6. Recompute the runtime ledger summary: 15 events, five sessions, five
   STARTs, five FINISHes, zero unmatched. Confirm claim calibration remains
   `BLOCKED / PARTIAL`: no parity closure, no established distinct-helper
   trigger, no authorized rerun, launcher untouched after the recorded write,
   and package-retry authorization/successful-command provenance UNKNOWN.
7. Recompute all retained raw-execution evidence hashes used by V2/V3 and
   independently revalidate the source and packaged-app manifests. Confirm
   prior child returns and raw evidence remain byte-preserved.
8. Verify the current launcher at `/Users/ryan/.local/bin/chirality` remains at
   SHA-256 `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`
   and do not alter it.
9. Apply the amended containment rule: all package-manager/child-attributable
   writes must be within this run root. Explicitly exclude the parent-owned
   Receipt 183 diff from attribution and make no judgment on its semantics.
   Report any other outside-run-root attributable effect as a blocker.
10. Confirm V3 remains preserved with its exact rejected verdict and explain
    that V4 does not rewrite or erase that provenance.
11. Run only read-only validation. No repair, test rerun, build, app, daemon,
    UI, network, receipt, product, deliverable, launcher, or Git mutation.

## Permissions

Repository-wide read is allowed. The only allowed verifier write is:

`instances/A2-PKG02-PARITY-INTEGRATED-VERIFIER-04/RETURN.md`

Do not create `STATUS.json`; the manager will create it after your return.
Do not modify this brief, any earlier artifact, Receipt 183, or any path outside
the V4 return target.

## Return contract

Write a concise evidence-backed return with verdict
`ACCEPT_REPAIRED_FAN_IN_V4` only if every required check passes. Otherwise use
`REJECT_REPAIRED_FAN_IN_V4`, identify exact blockers, and stop. Include exact
checked hashes, index/manifests/raw-evidence counts, status/registered-check/
runtime/claim results, containment conclusion under Amendment 03, launcher
identity, and an explicit no-repair/no-semantic-receipt-judgment statement.
