# D83/D84 execution continuation activation

This coordination-only continuation records the owner act supplied on
2026-09-07, the exact D84 L selection, durable session authority, the current
HELP_HUMAN work graph, and the handoff to CHANGE. It performs no D83 carrier,
D84 lifecycle, source, test, acceptance, release, or D85 act.

Repository root was resolved as
`/Users/ryan/.codex/worktrees/b347/chirality`; `WORKING_ROOT` is
`projects/pec`. Authoring branch is
`codex/pec-d83-d84-activation-20260907` at
`121ba425e13adf196b8a1b775d54f7cb0a5a94fe`; observed `origin/main` is
`c5192790f98ec024e7c2728cb1d4df3ae2b2a2dd`. PR #753 is reported open and
ready with prior CI PASS; CHANGE must verify current PR/head/check state before
the authorized merge.

The selection basis is the exact owner direction in `SESSION_AUTHORITY.md`.
The D84 L source is the existing immutable route candidate at
`../D84_CHECKING_ROUTE_PREP_2026-09-07/`; its status postimage SHA-256 is
`7d3eeb9888f10f6e938c7a0c08ff22ee1907df89812064ee76a95e0fdaeae60c`
and its bound preimage SHA-256 is
`e2579018c8012d711d9a6d81395a098991d5e6c601ea13f7486b8a331c9fc80e`.
The exact owner ruling is recorded in
`../_DECISIONS/D-PEC-84_L_RULING_2026-09-07.md` and only the D84 register row
is changed.

Authorized writes in this bounded recorder node are this new directory, the
new D84 L ruling, the D84 register row, and one append-only Receipt 173.
Existing D83/D84 activation, route, report, proposal, review, acceptance, and
other snapshot bytes remain immutable. Product, status, source, test,
lifecycle, dependency, SOW, Task Management, D85, Root, and sister-project
writes are excluded.

Execution sequencing after publication is strict: CHANGE publishes and merges
the ruling records; later managers observe them on fetched `origin/main`; D83
ordinary application and the D84 administrative reversal may then proceed in
their disjoint exact scopes. Scanner production waits for the reversal to be
recorded and independently verified. D84 repair uses WORKING_ITEMS authoring,
a fresh independent verifier, and RECONCILIATION changed-claim backcheck.
