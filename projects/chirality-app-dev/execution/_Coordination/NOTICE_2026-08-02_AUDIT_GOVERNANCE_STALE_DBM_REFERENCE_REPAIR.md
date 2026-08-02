# Routed Change Notice — AUDIT_GOVERNANCE stale DBM §5.1 reference repair

Routed by: Root loop, 2026-08-02, under the `AGENTS.md` agent-index
change-notice rule.

This notice is coordination, never authority. The App loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence.

## What changed

`agents/AGENT_AUDIT_GOVERNANCE.md` was repaired to remove references to a
`DBM_Agent_Instruction_Architecture.md` §5.1 agent table that no longer
exists: Pass 1b no longer counts agents from the DBM, Pass 5b is redefined
as competing-agent-index detection with `AGENTS.md` as the sole live index,
and Pass 5c compares agent headers against `AGENTS.md` only. No write
scope, tool access, output contract, or pass numbering changed.

Instruction SHA-256:
`58c4f9e5dc4e1c3ae16f2e0bb70940e4400dcc3e07259f911f8e3b9af680a628`
(superseding
`e65f27ea2b116bc6e9c8b520d340d0b70d0e35b99b2f0231287d38c4a09276e6`).

## What did not change

All other `agents/` files, `AGENTS.md`, and the DBM itself are untouched.
No lifecycle, reliance, release, or professional-judgment act is performed
by this notice or the repair.

## Follow-on for this loop

This loop bundles `agents/` wholesale into the app package; the
instruction-root integrity check recomputes hashes from source at build
time, so no repin is required. Any local mirror or citation that quotes the
old Pass 5b title ("AGENTS.md vs. DBM §5.1") should be reconciled when next
touched.
