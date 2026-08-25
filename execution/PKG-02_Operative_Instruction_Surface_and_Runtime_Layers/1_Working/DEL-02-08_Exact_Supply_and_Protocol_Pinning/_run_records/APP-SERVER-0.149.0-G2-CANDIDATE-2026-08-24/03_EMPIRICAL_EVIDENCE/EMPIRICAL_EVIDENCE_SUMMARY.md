# App Server 0.149.0 R14 Empirical Evidence

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**Node result:** `PASS_WITH_DOCUMENTED_GAPS_AND_ADMITTED_DENIED_EGRESS`

The digest-exact arm64 App Server executed under the R14 containment envelope
and identified itself as `codex-app-server 0.149.0`. Every vendor invocation
was preceded by an executable-identity check, sandbox-profile identity check,
and a network-denial preflight that returned `Operation not permitted`.

The evidence establishes:

- effective user, untrusted-project, and session-flag configuration layers;
- `configRequirements/read = null` on the unmanaged disposable host;
- Appendix-B.1 delegation controls and precedence, including
  `features.multi_agent_v2`;
- a complete 118-entry feature inventory over two pages, including stage,
  enabled state, and default-enabled state;
- `features.plugins` as the exact 0.149.0 switch that governs startup curated
  and featured plugin work: its runtime default is `true`; a session override
  reads back `false` and suppresses every observed plugin startup attempt;
- three sandbox-denied plugin destinations with their triggering operations;
- no completed connection, credential prompt, login/device flow, `auth.json`,
  external write, or approval grant.

The package entrypoints do not expose the current documentation's schema/type
generation commands. The dedicated app-server rejects both direct commands,
and the only relevant ancillary executable, `codex-code-mode-host`, exposes
only `--listen`. Generated JSON schema, generated TypeScript types, and a
schema-derived exhaustive method list are therefore
`UNAVAILABLE_UNDER_BOUNDS`. The candidate must carry those gaps to G2; this
run did not loosen containment or obtain another executable.

This packet is evidence only. It makes no G2 acceptance, pin amendment,
implementation, cutover, release, publication, or reliance claim.
