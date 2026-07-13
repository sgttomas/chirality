# CHANGE-P-G Integration Readiness

Session: `2026-07-13_CHANGE-P-G`  
Verdict: `READY`  
Branch: `codex/sow-stage2-pilots`  
Integration branch: `main`  
Exact basis: `0d260eb024d8b8dada0df477b70ac880a6906ffa`

## Observations

- Local `main`, `origin/main`, and remote `refs/heads/main` all resolved to the
  exact basis before branch creation; divergence was `0/0`.
- No local or remote `codex/sow-stage2-pilots` branch existed and no merge,
  rebase, cherry-pick, revert, or bisect operation was active.
- The project trees contained no pre-existing change. The declared untracked
  `.claude-worktrees/` container remains external and untouched.
- P-F-R1 is accepted by HELP_HUMAN. `ACCEPTANCE.md` SHA-256 is
  `8e5d453f98e7be40256c200f15e80eb05df02f0167b037b90d1f59332ff10224`;
  `ACCEPTANCE_MANIFEST.tsv` SHA-256 is
  `84e11ec2c8268aafd3297e95f45cfc5463ca0d1f09563c8bf454172b8ba4c9b0`.
- All 15 rows in the acceptance manifest reproduce their named artifact
  hashes. All five manager/reconciliation contracts are terminal `PASS`.
- The release set is exactly ten `IN_PROGRESS` members: App `DEL-07-01`
  through `DEL-07-06`, followed by Piping `DEL-13-01` through `DEL-13-04`.
- The replacement manifest has 50 unique rows in ten disjoint five-path
  groups. Each group adds one accepted `ScopeOfWork.md` and deletes the four
  legacy production documents. The 50-row rollback manifest is the exact
  operation/hash inverse.
- Current preimages reproduce 40/40 legacy document hashes, 10/10 absent SOW
  preimages, 10/10 status hashes, ten `LEGACY_FOUR_DOC` resolver results, and
  ten `IN_PROGRESS` lifecycle values. Candidate hashes reproduce 10/10.
- No replacement path names `_STATUS.md`, a control file, or a path outside
  the ten accepted deliverable directories. Checkout and temporary path
  prefixes are absent from the accepted pilot package evidence.
- Findings, blockers, material unknowns, and waivers are zero.

## Interpretation and controlled risks

The accepted derivative package is mechanically ready for the sealed serial
integration. The principal risks are path overreach, candidate-byte drift,
status/lifecycle mutation, and commit-architecture drift. These are controlled
by staging and validating exactly one manifest group per deliverable, recording
every commit and pre/post identity, and stopping on the first mismatch.

## Approved execution

`HUMAN-STEER-001` supplies standing approval for this run's PR merge. CHANGE
will first bind the preparation evidence, then create exactly ten serial
five-path replacement commits in the accepted order, then bind the integration
evidence in a separate commit. It will not merge or cherry-pick either Stage-1
pilot branch and will not perform H1/H2, ISSUED, lifecycle, release, or legacy
retirement action.

Rollback remains a later explicit non-history-rewriting forward commit using
the accepted inverse manifest and archived source bytes. No automatic rollback
is authorized.
