# ORCHESTRATOR-B1 Sealed Launch Brief — v1

Role: `ORCHESTRATOR` Agent 1 manager

Objective: reproduce the two-project deliverable census and active-caller
closure on synchronized post-C2 main, compare it row-for-row with P0_BASIS,
and prepare the derivative `P3_MANIFEST` candidate that gates all conversion.

Accepted basis:

- D-GOV-16 ruling `7584718aa32b112e415331736d1a8e68c12ac176`;
- accepted Stage-2 plan and node B1 contract;
- P0_BASIS census/caller manifests and handoff;
- P2_CONSUMERS C2F-R2 PASS and C2G postmerge handoff;
- synchronized local/origin/remote main
  `9349594530dc19e55baf9c2ef0b7eb4716f48a17`;
- H1 and H2 remain unapproved.

Read scope: Git refs and tracked tree; the accepted B0 basis and P0 snapshot;
P2_CONSUMERS including exact hashes and postmerge handoff; the two project
`1_Working/DEL-*` populations; active caller surfaces/manifests; applicable
deterministic validators. Do not read or modify `.claude-worktrees/`.

Write scope:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/P3_MANIFEST/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-B1/{RETURN.md,STATUS.json}`.

No project, deliverable, source, control, `_STATUS.md`, lifecycle, canon,
caller, tool, Git, PR, receipt, release, H1/H2, conversion, or retirement write
is authorized. No delegation is required. Use read, bounded shell diagnostics,
and deterministic validators only.

Required checks and outputs:

1. Prove local main, origin/main, and remote main equal the accepted C2G final
   tip with divergence `0/0`; tracked worktree must be clean apart from the
   declared run outputs and untouched `.claude-worktrees/`.
2. Reproduce the complete tracked census from the two exact project roots.
   Require 154 members, all five legacy production/control files present per
   member, zero `ScopeOfWork.md`, 153 `IN_PROGRESS`, and exactly Piping
   `DEL-01-01` as the sole `ISSUED` member.
3. Emit `EXECUTION_MANIFEST.tsv` using the P0 schema, C-sorted by path, with
   fresh SHA-256 hashes for the four legacy sources and `_STATUS.md`, lifecycle,
   pilot, and issued columns.
4. Compare every manifest row and field with
   `basis/CENSUS_MANIFEST.tsv`. Emit a machine-readable row/field comparison;
   any membership, source, status, lifecycle, pilot, or issued delta blocks.
5. Recompute the exact path digest and ten-pilot/144-remaining partition from
   the accepted basis; require exact equality.
6. Verify all P2_CONSUMERS manifest hashes and the current hashes/dispositions
   of all 64 root and 9 App caller rows. Search for newly active/unclassified
   SOW/legacy transition callers using the accepted B0/P2 search basis; any
   caller-classification drift blocks.
7. Prove consumer activation and the C2G evidence commits changed no path
   under either project deliverable population and no source, control,
   `_STATUS.md`, lifecycle, or membership truth.
8. Write `BASIS.md`, `EXECUTION_MANIFEST.tsv`, `ROW_COMPARISON.tsv`,
   `CALLER_CLOSURE.md`, `CHECKS.md`, `MANIFEST.tsv`, and `HANDOFF_STATE.md` in
   `P3_MANIFEST`. Mark the package `CANDIDATE — AWAITING RECON-B1`; it becomes
   accepted only after independent parent fan-in.
9. Run JSON/TSV structure checks as applicable and `git diff --check` on the
   declared outputs.

Return contract: `PASS`, `BLOCKED`, or `DECISION_REQUIRED`; exact ref, census,
lifecycle, partition, row-comparison, digest, caller, containment, and check
results; artifact hashes; blockers/unknowns/waivers; rerun conditions; next
lawful owner `RECON-B1` on PASS. Terminal `STATUS.json` is mandatory.
