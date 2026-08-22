# Orchestration plan — Root DEL-02-06 preparation, CHANGE amendment, and housekeeping

RunID: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`

Version: `1`

SelectionAuthority: `HUMAN`

Posture: `MIXED`

## Accepted basis

- Repository/working root: `/Users/ryan/.codex/worktrees/0b6e/chirality`.
- Branch: `codex/root-del0206-change-housekeeping-20260821`.
- Branch base: `origin/main@1b375af4f1219ecfc00fc2755854aa7fd4220901`.
- Required ancestor: `adf805e0d9ac55787e8ac815c3018467babb7f50` (`git cat-file -t`: `commit`; ancestor predicate: PASS).
- Root Receipt 111 and `DEL02_PREPARATION_AUTHORIZATION_HANDOFF.md` are present on the base.
- DEL-02-06 accepted semantic snapshot: SHA-256 `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`.
- Owner-supplied compatibility epoch/candidate: `1` / `root-runtime-1`.
- Root Step-0 guards G0–G4: PASS before dispatch; branch divergence from `origin/main`: `0/0`; clean before branch creation.

## Graph

| Node | Manager | Objective | Dependencies | Write ownership | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|
| N1 | WORKING_ITEMS | Prepare and refute the exact DEL-02-06 compatibility-completion candidate within the five-step grant; record activation/REM-001 without lifecycle promotion | none | DEL-02-06 package path plus N1 instance records | exact prepared bytes path and SHA-256; six-member reproduction; validation/refutation; blockers; package handoff | fresh review PASS, or repaired-and-rereviewed within two cycles; no accepted historical member modified |
| N2 | HELPS_HUMANS | Implement TM-ROOT-124 instruction amendment, G4 manifest with resolvable 40-char base, and three routed coordination notices | none | `agents/AGENT_CHANGE.md`, one new Root G4 manifest, App/Piping/domain-engine coordination notices, N2 instance records | instruction tranche and validation/review evidence; no register write | fresh review PASS, or repaired-and-rereviewed within two cycles; base resolves as commit |
| N3 | TASK_MANAGEMENT | Run mandatory federation; close TM-ROOT-116 and, after N2 lands, TM-ROOT-124; add two owner-directed attention rows; assess only fired DEL-02-06 deferral triggers | N1 and N2 landed in dependency order | Root Task Management register home, Root receipt/handoff/control records only | validated register/archive delta, federation result, trigger assessment and owner slate | complete federation; owner-directed rows exact; no foreign register write; no docs/validator implementation |

N1 and N2 are concurrent and write-disjoint. N3 is serialized after the N1
and N2 commits because its closure evidence and trigger assessment consume
their landed bytes. HELP_HUMAN is the integration owner for the Root receipt,
run handoff, Git closeout, PR creation, and owner decision slate.

## Human gates and exclusions

- Prepared compatibility bytes remain candidate/derivative state until a
  separate accountable owner acceptance.
- No implementation, lifecycle promotion, release, publication, reliance,
  foreign-loop content/register write, artifact-proof label, or merge.
- No selection of the nine other OPEN rows, `TM-ROOT-120`, or any DEFERRED row
  whose exact trigger is not fired by N1.
- If `origin/main` advances, no sync occurs without a new owner authorization.
- Node failure is isolated. Up to two enumerated-finding repair/re-review
  cycles are allowed; persistent failure is recorded and passing independent
  work may still land.
