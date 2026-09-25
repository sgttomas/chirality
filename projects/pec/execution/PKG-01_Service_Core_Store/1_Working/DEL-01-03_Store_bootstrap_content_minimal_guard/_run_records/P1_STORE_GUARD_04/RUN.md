# RUN — P1_STORE_GUARD_04 (D-PEC-91 A-53 COUNT-domain slice)

Role: WORKING_ITEMS (Type 1), instruction-asserted, owning PKG-01 / DEL-01-03
only. Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C4.
Brief: `C4_D91_COUNT_DOMAIN_SLICE.md` in HELP_HUMAN's session scratchpad
(`.../scratchpad/closeout/`), SHA-256
`51a5152699b465f35afa19099c866c6c6e2f2baa19d4bad71d27c9e5832ae497`, read from
disk and hashed by this manager. No other scratchpad file was read.
Date: 2026-09-25 (session date). Host: Claude Code Agent tool, isolated
worktree. Model steer: `claude-opus-5-5`, high reasoning (D-PEC-91 ruling,
owner question 5). The host reports the manager as `claude-opus-5-5`; the
reasoning level is instruction-asserted.

## Basis (actual origins and SHA-256 at `origin/main` `8b6553850aa8a98cb44aed02e9fe91e23b1234bd`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_RULING_2026-09-25.md` | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` (matches the ruling and the brief) |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-91 row, line 108: `RULED A-53 / EFFECTIVE ON MERGE`) | `a18b54f872f8df80691647bb982926fa1756b1d2297eb3a7ffe8caab12d85250` |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| DEL-01-03 `ScopeOfWork.md` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| `workflows/software-bounded-implementation/WORKFLOW.md` (bundled, `chirality-root:bundled:workflow:software-bounded-implementation`; author method) | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `.agents/skills/software-code-review/SKILL.md` (project skill; verifier method) | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/L2A_REVIEW_DEL-01-03.md` (context, immutable) | `b1f8731613d8645f9454bedefd25c02a41d04f24356ac3bb40587afdb82041c5` |
| `_run_records/P1_STORE_GUARD_03/RUN.md` (context, immutable) | `078914b85147417175fc8e701f80fd4799d48131e13e932d9e7bacbe38bc1b17` |

The specification is the proposal's per-repair table, R15 exact rule, R17
edits D1–D10, finite verification, administrative grant, rollback and limits,
with the ruling's A-53 substitutions and its clarifications N-2..N-5 and
"A-53 consequential wording":

- `_MAX_COUNT = 2**53 - 1`; its comment cites the JSON safe-integer range
  (RFC 8259), not SQLite INTEGER; 16 decimal digits, not 19.
- `2**53 - 1` admitted and rendered `"9007199254740991"`.
- `2**53` replaces `2**63` in `invalid_values`.
- Over-bound list `(2**53, 2**63, 10**639, 10**5000)`.
- D1, D2 and D5 use `2**53 - 1` (9,007,199,254,740,991) and `2**53`; D1's
  rationale sentence is the proposal's A-53 sentence (L169); D1's digit count
  is 16.
- D10 states the COUNT bound as `2**53 - 1` rather than "at most 63 bits".
- M2, M3 relative to the A-53 bound; M6 (widening to `10**4000`) unchanged.
- N-4: each run records whether R16's read-only block actually ran.

## Preconditions

1. Fetched `origin/main` = `8b6553850aa8a98cb44aed02e9fe91e23b1234bd`
   (PR #902 merge; `merge-base --is-ancestor` confirms it). The ruling
   file and the D-PEC-91 register row are present. PASS.
2. Fresh preimage verification: all four opened paths and the four unopened
   paths match the proposal's rollback table (see `PREIMAGE.md`). PASS.
3. Reliance-hold `dispatch-for-production` preflight: ALLOW, exit 0, for all
   four opened paths (see `PREIMAGE.md`). PASS.

Branch: `claude/pec-d91-count-domain-slice`, created from fresh `origin/main`
`8b6553850` with `--no-track` (the host permitted the new local branch).
Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7; SQLite 3.50.4; `id -u` 501. Commit identity: no
`user.email` is configured (exit 1); commits use the auto-derived identity
`Ryan Tufts <ryan@Ryans-MacBook-Air.local>`, as the base's recent non-merge
commits do (`c906efbc5`, `3dedb4c52`, `ca85173ad`).

## Work graph

| Node | Owner | Act | Depends |
|---|---|---|---|
| N1 | WORKING_ITEMS | Preconditions, branch, run root, `PREIMAGE.md` | — |
| N2 | TASK author (`pec-task`, opus) | F-1 before-reproduction on preimage (run-root scratch, limits default/640/0); R15–R17 with A-53 on the four paths under software-bounded-implementation; after-reproduction; mutation runners under `probes/`; `AUTHOR_RETURN_0N.md` | N1 |
| N3 | WORKING_ITEMS | Five registered checks and verbose storage run under `checks/`; M1–M7 and D-PEC-89 M1–M9 reruns under `checks/` | N2 |
| N4 | TASK verifier (`pec-reviewer`, opus, read-only) | software-code-review; substantive admissibility; independent F-1 reproduction on preimage and candidate; boundary cases; R16 block; R17 text; verdict saved by the manager as `VERIFIER_VERDICT_0N.md` | N3 |
| N2'/N4' | author / verifier | Correction cycles while a blocking finding remains | N4 |
| N5 | WORKING_ITEMS | `rely-for-production` preflight, containment, whitespace, ASCII | N4 PASS |
| N6 | WORKING_ITEMS | One `MEMORY.md` entry | N5 |
| N7 | WORKING_ITEMS | Commit, push, PR (no merge) | N6 |

## Progress log

- N1 complete.
