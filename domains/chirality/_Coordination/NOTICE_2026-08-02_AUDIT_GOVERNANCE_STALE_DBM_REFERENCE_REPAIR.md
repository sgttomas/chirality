# Routed Change Notice — AUDIT_GOVERNANCE stale DBM §5.1 reference repair

Routed by: Root loop, 2026-08-02, under the `AGENTS.md` agent-index
change-notice rule.

This notice is coordination, never authority. The domain loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence. Corpus-drift status remains the deterministic
detection path; this notice exists so detection does not depend on it alone.

## What changed

`agents/AGENT_AUDIT_GOVERNANCE.md` was repaired to remove references to a
`DBM_Agent_Instruction_Architecture.md` §5.1 agent table that no longer
exists (the live agent index moved to `AGENTS.md`; the current DBM carries
no agent table). Specifically:

- Pass 1b no longer counts agents from a DBM §5.1 table.
- Pass 5b is redefined from "AGENTS.md vs. DBM §5.1" to "Competing agent
  index detection": `AGENTS.md` is the sole live index, and any agent
  enumeration presented as an inventory in another governance document is
  reported as an issue.
- Pass 5c compares agent headers against `AGENTS.md` only.
- The summary, report template, and rationale sections were aligned with
  the above. No write scope, tool access, output contract, or pass
  numbering changed.

Instruction SHA-256:
`58c4f9e5dc4e1c3ae16f2e0bb70940e4400dcc3e07259f911f8e3b9af680a628`
(superseding
`e65f27ea2b116bc6e9c8b520d340d0b70d0e35b99b2f0231287d38c4a09276e6`).

## What did not change

All other `agents/` files, `AGENTS.md`, the DBM itself, and all K-*
invariants are untouched. No lifecycle, reliance, release, or
professional-judgment act is performed by this notice or the repair.

## Follow-on for this loop

This domain's source catalog lists `AGENT_AUDIT_GOVERNANCE.md` in its
accepted corpus; repin or record corpus currency for the new SHA when this
loop next reconciles. Accepted decomposition truth against the prior
snapshot remains valid as-of its citation.
