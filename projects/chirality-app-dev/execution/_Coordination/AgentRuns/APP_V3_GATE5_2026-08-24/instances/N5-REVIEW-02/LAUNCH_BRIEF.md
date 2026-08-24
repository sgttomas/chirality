# Sealed Brief — Fresh Independent Gate-5 Repair-Cycle-1 Review

- Parent: `APP_V3_GATE5_2026-08-24` / HELP_HUMAN.
- Role: `REVIEW` Agent 1.
- Review type: `INDEPENDENT_VERIFICATION` of the complete current
  SCA-APP-008 Gate-5 candidate after N4/N5 repair cycle 1.
- Basis: `cc196023a5532fe58955655c1144cd09ee88343a`.
- Historical input: `N5-REVIEW-01` is evidence for the pre-normalization bytes
  only and is not accepted as review of the current candidate.
- Read scope: repository-wide as needed to verify governing instruments,
  basis blobs, current applied truth, protected identities, authority-corpus
  outputs, dependency evidence, audit evidence, and write-set containment.
- Write scope: only `LAUNCH_BRIEF.md`, `REVIEW.md`, `RETURN.md`, and
  `STATUS.json` in this directory.
- Independence: the reviewer did not author N0 through N5 or repair cycle 1
  and does not edit reviewed bytes.
- Required result: `PASS` only with zero open blocker, major, or minor
  findings; otherwise return an exact repair list.
- Prohibited: reviewed-content repair, authority mutation, pointer movement,
  notice routing, staging, commit, push, PR, merge, or any write outside this
  directory.

## Required checks

1. Read `AGENTS.md`, `agents/AGENT_REVIEW.md`, the full Gate-5 steer, the full
   approved Gate-4 plan, the owner resume authorization, N4 repair lineage,
   N5 repair fan-in, and REVIEW-01 as historical evidence only.
2. Re-run every REVIEW-01 criterion against current bytes: N0 correction; N1
   blob truth, reconstruction, and collision census; rollback/resume; N2/N3
   exact application; contract/register parity and SCC posture; corpus v19;
   four dependency refreshes; named closure audit; pointer, notice, handoff,
   protected identities, and complete write-set containment.
3. Independently prove the six named audit CSVs are CRLF-to-LF-only repairs
   with equal parsed arrays and exact pre-to-post lineage.
4. Verify current `MANIFEST.sha256` is
   `7c30c9e2244beca0a9d8182e1908ce188cba48ea87b919b5da16f3a83423077d`,
   all 16 entries validate, the old manifest reconstructs exactly, and audit
   metrics and verdict are unchanged.
5. Verify every current downstream pin was regenerated; every remaining old
   manifest occurrence is historical or explicit lineage; and REVIEW-01 is
   properly superseded for current-state use.
6. Re-run candidate whitespace, `git diff --check`, agent instructions,
   entrypoints, Task Management, receipt precheck, authority-corpus status and
   audit, dependency schemas, audit package checks, candidate JSON/CSV parsing,
   protected identities, zero instruction-surface diff, and live G4 validation.
