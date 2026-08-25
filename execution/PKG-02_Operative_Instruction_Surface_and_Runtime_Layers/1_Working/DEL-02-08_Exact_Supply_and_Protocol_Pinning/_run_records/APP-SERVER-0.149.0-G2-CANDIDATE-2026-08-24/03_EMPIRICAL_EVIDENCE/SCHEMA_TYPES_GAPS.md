# Schema and Type Generation Gaps

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

| Evidence | Result |
| --- | --- |
| dedicated app-server help | no `generate-json-schema` or `generate-ts` command |
| direct `generate-json-schema --out <disposable>` probe | exit `2`, `unexpected argument 'generate-json-schema'` |
| direct `generate-ts --out <disposable>` probe | exit `2`, `unexpected argument 'generate-ts'` |
| package `codex-code-mode-host --help` | only `--listen`; no schema/type command |
| package `rg` / `zsh` | not executed; generic search/shell members cannot emit App Server protocol artifacts |
| generated output directories | absent after the negative probes |

Disposition: generated JSON schema, generated TypeScript types, and a
schema-derived exhaustive stable/experimental method inventory are
`UNAVAILABLE_UNDER_BOUNDS`. Current official App Server documentation
describes `codex app-server generate-json-schema` and `generate-ts`, but none
of the three pinned assets contains that wrapper executable. R14-B permits
only executables inside those assets; obtaining or executing another binary
would violate the bound. The candidate returns the gap to the owner at G2.
