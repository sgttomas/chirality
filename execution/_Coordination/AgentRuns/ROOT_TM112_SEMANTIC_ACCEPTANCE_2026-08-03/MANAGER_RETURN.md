# HELPS_HUMANS manager return — TM112 semantic acceptance

RunID: `ROOT_TM112_SEMANTIC_ACCEPTANCE_2026-08-03`
Verdict: `ACCEPTANCE RECORDED / IMPLEMENTATION BRIEF SEALED / NOT STARTED`

The accountable human accepted `ROOT-TM112-SEMANTICS-01 G2 C1 F1` and exact
N-STOP-1..7 semantics, authorizing the previously bounded implementation/test
tranche. `ACCEPTANCE_RECORD.md` binds the signed transcript block and the
pre/post whitespace clause bytes. `IMPLEMENTATION_BRIEF.md` freezes the future
write scope and complete regression matrix. `BASIS_MANIFEST.sha256` binds the
immutable carrier.

Formatting-only carrier normalization changed the sealed implementation-brief
hash from
`b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218` to
`617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`.
Only trailing spaces/Markdown hard breaks and a surplus terminal blank line were
removed; accepted semantics and prose content are unchanged.

The branch prerequisite is present at pushed commit
`2b6d53027ea10374dd515a4a5a203f8ed4cf2f04`. Clause hash changed from
`2428824746c5a6928c2894619d67bbc817717bed536f5ee64b11cdafda0db62e` to
`fd3ba31a8c53719e165b131d872868a53760adab4dc7ae92015fbd6641a11ead`
only because two Markdown hard-break pairs were removed; normalized bytes are
identical and the clause EOF is unchanged.

Authorized future product files are only `docs/SPEC.md` §14.1,
`runtime/packages/daemon/src/runtime-daemon.ts`, and bounded
`runtime/tests/daemon.test.ts` cases. No source, test, canonical contract,
register, receipt, App, lifecycle, or Git change occurred in this acceptance
run. App notice routing remains conditional on human acceptance of the repair,
and no App-specific or process/SIGTERM causal claim is accepted.
