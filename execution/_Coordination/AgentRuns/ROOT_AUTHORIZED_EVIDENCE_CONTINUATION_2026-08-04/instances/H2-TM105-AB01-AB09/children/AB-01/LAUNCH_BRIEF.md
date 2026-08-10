# Agent-2 sealed brief — TM105 AB-01 threat evidence

ChildID: `H2-TM105-AB01-AB09/AB-01`

Parent: `H2-TM105-AB01-AB09` (`HELPS_HUMANS`, Agent 1)

Construction: bounded ephemeral Agent 2 generalist. The work is novel evidence
reasoning; no live TASK skill supplies this exact threat-model method. This
child must not delegate.

## Objective

Execute only acquisition brief AB-01 under the standing TM105-A
preparation-only posture. Return a repo-evidence-grounded asset/principal/
trust-boundary inventory and a threat matrix covering confused deputy, replay,
stale grants, policy mismatch, credential leakage, child widening,
native-tool bypass, and evidence tamper. Distinguish current mechanical
controls, control gaps/unmitigated risk, and evidence that would falsify each
control claim. Every unsupported owner, vendor, platform, deployment, data,
or topology fact is `UNKNOWN`.

## Authority and boundaries

- Evidence only; no semantic selection or contract-candidate drafting.
- Do not infer deployment topology, trusted principals, grant issuer/policy
  authority, trust anchors, regulated data, vendor guarantees, or product
  acceptability.
- Do not select a backend, rights grammar, trust boundary, severity policy,
  control, or lifecycle posture. A severity entry may be `UNKNOWN`; any
  qualitative provisional severity must be explicitly labeled analyst
  triage, non-authoritative, and tied to observed current code behavior.
- Do not authorize or perform implementation, lifecycle, release, reliance,
  Git, PR, notice, register, receipt, client, or foreign-loop acts.
- Treat current code/tests as implementation evidence, not generic TM105
  semantic authority. Treat the Piping response as consumer-local evidence.

## Exact read scope

Resolve `REPO_ROOT` using `git rev-parse --show-toplevel`. Read only this brief
and the following evidence sources; do not discover or read other files:

| SHA-256 | Repo-relative path |
|---|---|
| `d76fab70ef8ff7a6b5f4b5d669fb6367fa7707b664256433420b8b210c61ebdb` | `runtime/packages/contracts/src/engine.ts` |
| `bcb87844dce118a3f7743b3e2e0ecc0c376627d2dbaf1dee483a281c6f2b767b` | `runtime/packages/contracts/src/harness/tool-descriptor.ts` |
| `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | `runtime/packages/contracts/src/harness/event-schema.ts` |
| `53c140a7ffa490e749faac8131ed8bf24b0f18d1392ac5931258a7b3f7d40427` | `runtime/packages/contracts/src/harness/engine-conformance.ts` |
| `28f8bade3372a6b0f1797a0c9623f0ad68f54f4ef2a6dee6638aeaeef20a29fa` | `runtime/packages/core/src/auth-registry.ts` |
| `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` | `runtime/packages/core/src/agent1-run-coordinator.ts` |
| `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` | `runtime/packages/core/src/turn-coordinator.ts` |
| `42dbdd15f73e60839fdfd41b980a871a9a49a4ba62d0bb33df23933568167dff` | `runtime/tests/agent1-run.test.ts` |
| `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` | `runtime/tests/turn-hardening.test.ts` |
| `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7` | `projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md` |

The parent already resolved the applicable governance and signed authority.
For this child, the following sealed constraints are controlling: K-PROV-1
(cite exact path and line/section), K-INVENT-1 (unknowns remain unknown),
K-CONFLICT-1 (surface conflicts), K-CLAIM-1 (do not overstate warrant),
K-GHOST-1 (no undeclared reads), and K-WRITE-1/2 (exact write containment).

## Allowed tools and write scope

Read-only shell operations (`git rev-parse`, `sed`, `rg`, `shasum`, `wc`) are
allowed only against the exact paths above. Use `apply_patch` to create only:

- `children/AB-01/RETURN.md`
- `children/AB-01/STATUS.json`

No other write is permitted. Do not use network tools. Do not run product
tests or mutate the checkout.

## Required return

`RETURN.md` must include:

1. input hash verification and any drift;
2. asset, principal, trust-boundary, and attacker-capability inventories;
3. a matrix with one or more rows for every required threat class, including
   evidence reference, observed exposure, present mechanical control,
   remaining/unmitigated risk, severity posture, and falsification evidence;
4. explicit conflicts and non-coverage;
5. owner/vendor/platform facts still `UNKNOWN`;
6. separately owned next evidence actions, not semantic recommendations; and
7. a statement that all semantic/implementation/lifecycle/release/reliance/
   byte-gate holds remain intact.

`STATUS.json` must be valid JSON and state child ID, terminal status, input
drift status, output path, unresolved facts, and no-authority-effect flags.

Do not claim completeness beyond the declared evidence set.
