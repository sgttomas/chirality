# RECON-B1 Sealed Launch Brief — v1

Role: `RECONCILIATION` Agent 1 manager, read-only subject verifier

Objective: independently verify the ORCHESTRATOR-B1 `P3_MANIFEST` candidate
against synchronized post-C2 main, P0_BASIS, P2_CONSUMERS, and the accepted B1
gate. Determine whether conversion may be released; do not repair the subject.

Accepted basis: D-GOV-16; accepted Stage-2 plan B1/G3 contract; main
`9349594530dc19e55baf9c2ef0b7eb4716f48a17`; P0_BASIS; P2_CONSUMERS C2G
postmerge PASS; ORCHESTRATOR-B1 terminal PASS; H1/H2 unapproved.

Read scope: Git refs/tree/history; `basis/**`; `snapshots/P0_BASIS/**`;
`snapshots/P2_CONSUMERS/**`; `snapshots/P3_MANIFEST/**`;
`instances/ORCHESTRATOR-B1/**`; exact two-project deliverable populations;
current root/App caller surfaces and accepted manifests; deterministic
validators needed to reproduce claims. Do not read or modify
`.claude-worktrees/`.

Write scope:

- `execution/_Reconciliation/DeliverableConcordance/SOW-STAGE2-EXEC-20260712-01-B1/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-B1/{RETURN.md,STATUS.json}`.

No P3 candidate, project, source, control, `_STATUS.md`, lifecycle, canon,
caller, tool, Git, PR, receipt, release, H1/H2, conversion, or retirement write
is authorized. No delegation is required.

Mandatory independent checks:

1. Verify synchronized refs and exact accepted main basis.
2. Reproduce the 154-member census independently from tracked paths; check
   five legacy/control files per member, zero SOW, 153 IN_PROGRESS plus the
   exact sole ISSUED member, ten pilots/144 remaining, and the accepted path
   digest.
3. Recompute all four source hashes, status hash, lifecycle, pilot, and issued
   fields and compare independently to P0 and P3. Require 154/154 row equality,
   zero field delta, and P3 manifest byte equality to P0.
4. Verify all P3 `MANIFEST.tsv` hashes without relying on the manager's
   reported result. Check P2 bindings and accepted caller overlay hashes.
5. Independently inspect the active SOW/legacy transition caller search and
   the 64-root/9-App disposition closure. Classify any drift, unknown, or
   superseded hash explicitly; require zero newly active/unclassified caller.
6. Independently prove the C2-to-current-main changed-path range contains no
   governed deliverable-population path and that membership/source/status/
   lifecycle truth is unchanged.
7. Validate P3 schema/row counts, candidate/handoff status, ORCHESTRATOR return
   contract, evidence portability, and write containment.
8. Separate schema/content, preservation/containment, and execution-substrate
   verdicts. Any missing evidence, failed mandatory check, material unknown,
   lifecycle/membership/caller delta, or source/status drift blocks G3.

Required outputs: `RUN_BASIS.md`, `MANIFEST_REPRODUCTION.md`,
`CALLER_CLOSURE_AUDIT.md`, `CONTAINMENT_AUDIT.md`, `FINDINGS.csv`, and
`HANDOFF.md` in the reconciliation package, plus terminal instance
`RETURN.md` and `STATUS.json`. Run structure checks and `git diff --check` over
declared outputs.

Return contract: `PASS`, `BLOCKED`, or `DECISION_REQUIRED`; exact reproduced
counts/digests/hashes; calibrated findings with provenance; blockers,
unknowns, waivers, rerun conditions; and next owner `HELP_HUMAN B1 fan-in`.
PASS recommends but does not itself release conversion or accept P3.
