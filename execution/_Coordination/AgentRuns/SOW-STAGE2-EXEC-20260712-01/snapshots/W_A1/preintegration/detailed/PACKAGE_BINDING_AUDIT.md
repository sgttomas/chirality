# W-A1 Package Binding Audit — Pre-Repair State

Status: `BLOCKED — PKG01 GENERATED-EVIDENCE PORTABILITY CONTRADICTION`

Audit posture: independent, read-only reproduction by the bounded
`RECON-A1-F/package_fanin_audit` generalist. Inputs were not modified. Paths
in this evidence are repo/run-relative. Accepted machine-specific strings in
exact copied source/control or marker-bound source text remain
`PRESERVED_SOURCE_LITERAL`; they were not normalized.

## Frozen basis

- Run: `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01`
- Accepted preflight: `snapshots/W_A1/preflight/**`
- Reconciliation activation:
  `amendments/A1-RECONCILIATION-ACTIVATION-001.md`
- Package inputs: `instances/WORKING-A1-PKG00..03/**`
- Candidate inputs: `candidates/W_A1/APP-PKG00..03/**`
- Migration authority:
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`
- Exact accepted row basis:
  `main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb`
- Dispatch basis:
  `main@34b87ec77010035eeaa76f0fa65981ec57e78933`

This audit records the package state immediately before the owning-manager
PKG01 R2 repair requested in response to the blocker below. Any R2 mutation
makes the affected PKG01 bindings stale and requires a fresh reproduction.

## Exact package reproduction

| Package | Manifest bindings | Members | Terminal child return/status pairs | Mappings | Source lines | Replacement / rollback | Binding result |
|---|---:|---:|---:|---:|---:|---:|---|
| APP-PKG-00 | 23/23 | 2 | 4/4 | 56 | 526 | 10 / 10 | PASS |
| APP-PKG-01 | 37/37 | 4 | 8/8 | 145 | 1,539 | 20 / 20 | PASS, portability contradiction below |
| APP-PKG-02 | 64/64 | 5 | 10/10 | 146 | 1,441 | 25 / 25 | PASS |
| APP-PKG-03 | 62/62 | 4 | 8/8 | 109 | 1,311 | 20 / 20 | PASS |
| **A1** | **186/186** | **15** | **30/30** | **456** | **4,817** | **75 / 75** | **BLOCKED at portability gate** |

All 186 nonblank package-manifest rows are unique, use repo-relative paths,
resolve to existing files, and reproduce their recorded SHA-256. The exact
row-by-row reproduction is in `PACKAGE_BINDINGS.tsv`.

Each package `STATUS.json` is terminal `PASS`; each package `RETURN.md`
states PASS. All 30 child records in the four `CHILD_INDEX.tsv` files have a
manifest-bound `RETURN.md` and `STATUS.json`; each status is terminal
`PASS`, and each return records `RUN_STATUS: SUCCESS` and/or a PASS
verdict. The 15 candidate hashes reproduce both `MEMBER_RESULTS.tsv` and the
candidate rows in the package manifests.

The four `MEMBER_RESULTS.tsv` surfaces independently sum to 456 mappings and
4,817 source lines. Every member has exactly one replacement ADD for
`ScopeOfWork.md` and four replacement DELETE rows for the legacy production
documents. All 60 live legacy preimage hashes and all 15 candidate postimage
hashes reproduce. The 75 rollback rows are the exact action inverse of the 75
replacement rows with identical deliverable, path, and hash. Neither manifest
class contains status, context, dependency, reference, lifecycle, or other
control paths.

As supplemental evidence-chain validation, all 717 rows in the 22 child
evidence manifests present under PKG01–PKG03 resolve to the recorded artifact
identity (including logical `candidate/ScopeOfWork.md` labels resolved to the
same child-workspace candidate bytes). PKG00 binds its child returns/statuses
directly and has no child `MANIFEST.tsv`.

## Named substrate, repair, and reconciliation proofs

### APP-PKG-00

- The rejected `APP-PKG-00` converter token event is preserved in
  `COORDINATION_NOTICE-001.md`; it records failure before output and the
  accepted canonical `PKG-00` rerun.
- `PROJECT_CHECKS.json` preserves the initial no-API premerge failure with
  zero accepted tests. The separate
  `PROJECT_CHECKS_PREMERGE_R1.json` is manifest-bound and PASS after the
  local stub-provider rerun.
- These are classified substrate events, not waivers and not part of the
  accepted semantic candidate basis.

### APP-PKG-01

- AUTHOR-DEL-01-02 run-record repair reproduces exactly: postimage 4,221 bytes
  at
  `7f37750893fe84b6b0d423693a9232cd5446df63de9a250420cd9c8f047058f2`;
  reversing exactly three `~/` substitutions yields the 4,329-byte preimage
  `2a1ddb8f2125540a646ad3bacc66f82eeb321534ea1e38fc75edfb816ce808e9`.
- The package check-normalization rows also reproduce their stated
  postimages and reverse hashes:
  `PROJECT_CHECKS.json`
  `756aa875a1279526dc192b4e338f049167a7de1134f18a6478450269931972a3`
  reverses to
  `cfb3aa44c4996d7aa900e26a404035f156d23600fa5825056197f45763f3b7c5`;
  `PROJECT_CHECKS_PREMERGE.json`
  `9ca4aac07fa13ace3794e1fe1a136a210a751519007991bc026839cd3b8a6638`
  reverses to
  `248a98c6d9a05c2f8499e63fba70eabf522df56db9cf46b78b7c599cd8e4bea5`.
- Exact copied source/control and marker-bound source literals remain
  classified by `PRESERVED_SOURCE_LITERAL_INVENTORY.md`.

The residual generated `workspace_root` fields described under **Blocker**
are not source literals and invalidate the package's zero-generated-prefix
claim despite the otherwise exact reverse proofs.

### APP-PKG-02

- The two-file check normalization reproduces exactly: 27 checkout-root and
  four temp-root substitutions; postimages
  `2d675db6288ec86ffdf8b70b8802b896fe88a333a1fab42792762795ab1f45e0`
  and
  `6f833bceb68fc1fb2a9fde25799f94defc97e941f6ee5e00300a8210d9dc7363`
  reverse to the amendment-bound preimages
  `6389ce4b75b949c51dedacef934d136cb09fc49d5281e5c6fe1c36d2fb273045`
  and
  `28d7194ad2d12497e96c03a4df78f56904f00da97e82f21f0e42a3c8b8a710cf`.
  Both JSON postimages parse, remain PASS, and have zero machine-specific
  generated prefixes.
- `PRESERVED_SOURCE_LITERAL_INVENTORY.md` classifies 34 occurrences in 24
  exact copied source/control files.
- Both DEL-02-03 verifier Attempt 0 records reproduce and agree: the workspace
  was absent, the verifier failed before execution/writes, and unchanged R1
  is the accepted manifest-bound terminal PASS.

### APP-PKG-03

- AUTHOR-DEL-03-01 manifest regeneration reproduces 29/29 artifacts. The
  6,295-byte postimage hash is
  `5b25453a2f63fb4cc582687c878d6a54e71245bf2edbf455fd461536fe2a1b0a`;
  blanking only its 58 generated digest/byte cells reconstructs the exact
  4,328-byte malformed preimage
  `1b0c5d862dee09eae4298d22908f5a89dde4d0db11852342049eaebf127bab95`.
- AUTHOR-DEL-03-02's accepted terminal run record reproduces as 4,705 bytes,
  93 lines,
  `cfbf9d1fcc0369d800766974d883ebfda3f11498816c7a8b1244b71237f80d16`,
  with zero checkout, machine-temp, or local-file-URI prefix. The retained
  PENDING/intermediate chain is explicitly historical; the child and package
  bind the terminal SUCCESS identity.
- The generated project-check postimage
  `81c07351c8ec4ecf7a3fdb2cab46d9a91e26e357f227744254844d21dc6c9846`
  reverses to
  `0c102a01989435831a5db8c585592da679c7027c39c1baeb71cd519eb4a99d8d`.
  Planned premerge normalization postimage
  `83714cb1d6e9a3dd84ef53827909ed776f7a20760973e25008457eb0c8cf260a`
  reverses to scratch preimage
  `be4026f9656830a235746045b83f870bf10aaff0e427edcaa087cd5cd325ee76`.
- `PRESERVED_SOURCE_LITERAL_INVENTORY.md` classifies exactly 13 copied
  source/control occurrences. Generated evidence postimages scan clean.

## Blocker

Two manifest-bound PKG01 generated JSON check records each retain one
unclassified machine-specific checkout path:

- `instances/WORKING-A1-PKG01/PROJECT_CHECKS.json`, line 84, current SHA-256
  `756aa875a1279526dc192b4e338f049167a7de1134f18a6478450269931972a3`;
- `instances/WORKING-A1-PKG01/PROJECT_CHECKS_PREMERGE.json`, line 23, current
  SHA-256
  `9ca4aac07fa13ace3794e1fe1a136a210a751519007991bc026839cd3b8a6638`.

In each file, `workspace_root` equals the machine checkout root rather than a
portable `${REPO_ROOT}` anchor. The exact defective bytes remain bound by the
two current file hashes above; this generated audit does not repeat the local
checkout prefix.

These occurrences are neither copied source/control bytes nor marker-bound
source text. They contradict PKG01 `CHECKS.md` and
`PRESERVED_SOURCE_LITERAL_INVENTORY.md`, both of which claim generated
checks/metadata contain zero checkout-root prefixes. The reconciliation
activation states that any unclassified generated prefix or contradictory
claim blocks fan-in. Therefore the package file bindings are byte-exact, but
W-A1 package fan-in is not acceptable at this pre-repair state.

## Exact rerun requirement

The owning PKG01 manager must complete the separately authorized R2
repair/revalidation, preserving the pre-repair evidence above. Reconciliation
must then freshly reproduce:

1. both repaired JSON postimages, their exact substitution counts and reverse
   preimage proofs;
2. JSON parse, PASS status, exit codes, and substantive equality;
3. zero generated checkout/temp/file-URI prefixes;
4. every directly changed package binding, including the regenerated PKG01
   package manifest and any amended checks, return, status, handoff, or repair
   proof surfaces; and
5. all unaffected package/member/candidate/replacement/rollback identities.

Blockers other than this PKG01 portability contradiction: none found.
