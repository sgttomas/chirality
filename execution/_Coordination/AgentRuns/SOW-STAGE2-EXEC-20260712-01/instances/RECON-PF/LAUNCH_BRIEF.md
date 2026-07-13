# RECON-PF Sealed Launch Brief — v1

Role: `RECONCILIATION` Agent 1 manager, read-only subject verifier
Node: `P-F` — ten-pilot cross-package fan-in

Objective: independently reconcile the terminal App PKG-07 and Piping PKG-13
pilot preparation packages against P3, current main, exact Stage-1 blobs, and
the accepted Stage-2 pilot gate. Produce a preintegration snapshot candidate;
do not repair or integrate any deliverable.

Accepted basis: D-GOV-16; Stage-2 P-F contract; P3_MANIFEST B1/G3 PASS;
synchronized main `0d260eb024d8b8dada0df477b70ac880a6906ffa`;
`PILOT-VALIDATION-001`; Stage-1 commits
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26` and
`31c35ea9798c29cd0af16b7089186f3942dcfcb1`; WORKING-P-A PASS and
WORKING-P-P PASS. H1/H2 remain unapproved; all ten members are IN_PROGRESS.

Read scope: Git refs/tree read-only; P0/P2/P3 accepted snapshots; both package
manager instances and all child/candidate evidence; ten exact current
deliverable folders; Stage-1 commits/evidence; active SOW tools and applicable
project validation profiles. Do not read or modify `.claude-worktrees/`.

Write only:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/P4_PILOTS/preintegration/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-PF/{RETURN.md,STATUS.json}`.

Temporary read-only simulations may use `/tmp` and must be removed or reported.
No candidate/package evidence, project, source, control, `_STATUS.md`, lifecycle,
canon, caller, tool, Git, PR, receipt, release, H1/H2, ISSUED, integration, or
retirement write is authorized. No delegation is required.

Mandatory independent fan-in:

1. Verify synchronized refs, terminal manager/child contracts, exact expected
   population 6 App + 4 Piping, and complete child provenance. Classify the
   abandoned App DEL-07-01 attempt as unaccepted substrate failure and require
   the fresh R1 terminal PASS; do not count both.
2. Recompute from current project truth and P3 all 40 legacy source hashes,
   ten status hashes, IN_PROGRESS lifecycle states, pilot identities, and
   absence of live SOW. Require exact equality.
3. Extract/recompute all ten candidate hashes from the named Stage-1 commits
   and compare byte-for-byte with the candidate packages. No regeneration or
   marker insertion is allowed.
4. Independently validate current legacy-only states as `LEGACY_FOUR_DOC` and
   exact target-only candidates as `SOW_V1`, applying
   `PILOT-VALIDATION-001`. Verify every child validation result, map target,
   parity row/source-line disposition, checklist binding/order, repeated HTML
   stability/safety, source/status identity, and three-part verdict.
5. Require aggregate closure of exactly 325 mappings and 3,466 source lines,
   all preserved, with zero unresolved target, parity issue, semantic addition,
   lifecycle/control delta, blocker, missing member, or waiver.
6. Reconcile package replacement manifests into one exact 50-row manifest:
   ten `ADD ScopeOfWork.md` plus 40 legacy deletes, 50 unique project paths,
   grouped as ten disjoint five-path atomic replacements. Reconcile rollback as
   the exact hash/operation inverse. Verify no status/control path appears.
7. In isolated temporary copies, apply each five-path post-state and validate
   exactly `SOW_V1` with no legacy/dual/invalid state; verify rollback restores
   exact P3 bytes and `LEGACY_FOUR_DOC`.
8. Verify App/Piping manager project checks and rerun proportionate independent
   format/consumer/containment checks. Require current source/caller basis and
   live project trees unchanged.
9. Validate evidence portability, JSON/CSV/TSV schemas, hashes, unique paths,
   write containment, and `git diff --check` on declared outputs.

Required P4 preintegration outputs: `BASIS.md`, `PACKAGE_FANIN.md`,
`MEMBER_MATRIX.tsv`, `REPLACEMENT_MANIFEST.tsv`, `ROLLBACK_MANIFEST.tsv`,
`CHECKS.md`, `FINDINGS.csv`, `MANIFEST.tsv`, and `HANDOFF_STATE.md`, plus
terminal instance `RETURN.md` and `STATUS.json`. Mark the snapshot
`CANDIDATE — AWAITING HELP_HUMAN P-F FAN-IN`; RECON PASS recommends but does
not itself accept P4 or release P-G.

Return `PASS`, `BLOCKED`, or `DECISION_REQUIRED` with exact counts, hashes,
verdict classes, calibrated findings, blockers/unknowns/waivers, rerun rules,
and next owner HELP_HUMAN. Any discrepancy blocks P-G.
