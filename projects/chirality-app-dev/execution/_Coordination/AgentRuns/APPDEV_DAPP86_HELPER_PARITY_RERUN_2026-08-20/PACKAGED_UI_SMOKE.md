# Packaged UI smoke — blocked result

Verdict: `NOT OBSERVED — BLOCKED BEFORE UI ACTION`

The current packaged GUI reached its connected startup state, but startup
unexpectedly wrote `/Users/ryan/.local/bin/chirality`. The sealed brief requires
an immediate stop for owner-machine risk. Therefore no `node_repl + @oai/sky`
action was taken and no Workbench, Pipeline, guarded-selection, or
post-completion-selection claim is made.

The exact startup/stop evidence is in
`instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/runtime/desktop-main.log`
(SHA-256 `4b0b310ec20ed294a2e986dab76fe1cdd65fb620ed357cf57ca93b515b37d702`).

Surface dispositions:

| Surface | Result | Reason |
|---|---|---|
| Workbench opens/returns | BLOCKED | Stop occurred before UI action. |
| Pipeline opens/returns | BLOCKED | Stop occurred before UI action. |
| In-flight navigator guard | BLOCKED | Stop occurred before UI action. |
| Post-completion recorded-session selection | BLOCKED | Stop occurred before UI action. |
