# Agent 2 return — Agents projection minimal presentation

Status: `SUCCESS`

Implemented the owner-directed minimal Agents projection in the exact two authorized loci. A card now presents only a recorded agent type as `Agent 0`, `Agent 1`, or `Agent 2`; a recorded persona; and a human-readable tree relationship. Roots read `Top-level`. Children name an in-view parent by recorded persona, falling back to its recorded agent type and then the short truthful phrase `Parent relationship recorded`. Detached entries read `Parent relationship unavailable`.

Unknown type and persona values are omitted without inference. Engine, provider, model, currency, runtime status, source, observation time, session identifiers, artifact and approval references, diagnostics, and unresolved raw parent identifiers are absent from rendered output. Session identifiers remain internal for React identity, hierarchy lookup, selected state, and the unchanged selection callback.

Refresh, loading, error, empty, selected, disabled-selection, roots, child nesting, and detached placement remain operational. The focused test covers all admitted type labels, recorded personas, human parent copy without raw identifiers, unknown omission, detached presentation, removed metadata, refresh/error/loading behavior, and selected/disabled selection behavior.

Validation:

- Focused Vitest: `PASS` — 1 file, 6 tests.
- Registered frontend typecheck: `PASS`.
- Exact two-path `git diff --check`: `PASS`.
- Frozen patch equality, reverse application, and two-path scope: `PASS`.

No CSS, contracts, hierarchy builder, Runtime, permissions, Git, or other product/test locus was changed. No implementation failure was suppressed. The only failed attempt was a patch-tool formatting rejection before any source mutation; it had no product effect.

Limitations: Full suite, build, premerge, Electron, browser, native UI, local server, daemon, and network checks were excluded by the sealed brief. Fresh independent review remains owned by the parent workflow before publication.
