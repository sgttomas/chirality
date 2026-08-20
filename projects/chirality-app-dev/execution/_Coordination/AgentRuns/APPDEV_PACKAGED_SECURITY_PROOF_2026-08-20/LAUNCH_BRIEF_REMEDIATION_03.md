# Remediation 03 brief — missing CI tranche manifest

- Parent/run: `WI-PKG09-PACKAGED-SECURITY-01` /
  `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`.
- Graph position: adjacent CI proof-loop remediation after node commit
  `605a0b7bc85e054d32221083e1f15a57b2d85dee`; not a new engineering node.
- Objective: add exactly
  `docs/governance_harness/tranche_manifests/APP-DEL0906-PACKAGED-SECURITY-CI-20260820.yaml`
  following the existing APP-DEL0904/DEL0905 schema.
- Required manifest truth: basis
  `357a58b56726feba49507534159c3fbc4656b818`; instruction paths are the changed
  workflow and the new manifest; authorization is D-APP-97 C1 ruled by Ryan
  Tufts on 2026-08-17; integration ownership is HELP_HUMAN / current PKG-09
  WORKING_ITEMS / CHANGE; merge gate `human-gated-pr`; `self_merge: false`;
  M6 `none-required` because the workflow is App-specific and changes no
  agents, skills, root-governance prose, or shared consumer contract. The
  manifest records authority and grants none.
- Write authorization: the one new manifest only. No product, workflow,
  evidence, deliverable, lifecycle, Remaining, memory, approval SHA, receipt,
  completion log, register, agent, skill, or other governance write.
- Checks: YAML parse; manifest schema; full G4 candidate-range validation from
  base `357a58b...` through worktree candidate; exact-path diff/containment;
  report hashes. No host product proof rerun.
- APP-HOLD dispatch: `ALLOW` for DEL-09-06 and DEL-09-04.
