# Runtime Affected-Client Lane

## App requirements that may be planned now

Both targets must act as clients of one Root-owned generic runtime posture and
must preserve:

- stable App request/API/SSE/UI-event compatibility;
- explicit target/product-profile attribution in client requests and evidence,
  if Root later accepts such a field;
- project-root, persona/agent, mode, options, attachment, and policy inputs;
- visible connection, restart/rebind, interruption, terminal, and error states;
- canonical session/event replay compatibility without creating a second event
  store;
- App/project human approval and policy inputs without redefining generic tool
  mediation;
- target-specific presentation isolated from provider/model/runtime semantics;
- affected-client conformance evidence for standalone and domain artifacts.

These are consumer needs, not contract definitions. Any new public field,
target identity, resume rule, or compatibility version requires the owning
Root gate and later App adoption.

## Explicit blocked interfaces

| Concern | State | Current reason |
|---|---|---|
| generic runtime contract | `BLOCKED_BY_ROOT` | Root `TM-ROOT-105/107/109` and Piping consumer-response prerequisites |
| sandbox semantics | `BLOCKED_BY_ROOT` | same; requires full consumer-set contract |
| runtime/run identity | `BLOCKED_BY_ROOT` | generic identity semantics not App-owned |
| contract/version negotiation | `BLOCKED_BY_ROOT` | generic version policy not ruled |
| resume/session continuation | `BLOCKED_BY_ROOT` | generic session semantics Root-owned |
| Agent-2 Bash/arbitrary shell | `BLOCKED_BY_ROOT` | no Bash grant; H1 created none |

D-APP-89 establishes a validated App migration candidate to direct
`@chirality/runtime-contracts` imports and retains the facade as rollback. It
does not retire the facade or settle target/version identity. D-APP-88 R2 is
blocked and rolled back; the Root live-connection/server-close explanation is
an investigation hypothesis only.

## Candidate deliverable effects

The later product/SCA work should review `DEL-03-01` through `DEL-03-04`,
`DEL-04-01`, `DEL-04-02`, `DEL-04-05`, `DEL-05-01` through `DEL-05-05`,
`DEL-06-01`, `DEL-06-02`, `DEL-08-03`, and `DEL-08-04`. The likely near-term
effect is target-indexed conformance evidence and client attribution, not a
change of generic ownership. Exact direct amendments wait for the selected
architecture and Root contract response.
