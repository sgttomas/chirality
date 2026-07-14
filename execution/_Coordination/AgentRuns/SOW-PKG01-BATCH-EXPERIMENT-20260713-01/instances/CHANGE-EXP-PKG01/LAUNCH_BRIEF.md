# CHANGE-EXP-PKG01 Sealed Launch Brief

Role: `CHANGE` Agent 1.
RunID: `SOW-PKG01-BATCH-EXPERIMENT-20260713-01`.

Perform routine Git closeout for the completed standalone experiment evidence.
Expected entry: `main@ef461cfdb3a4b135dc670b04f646eca3eac47712`, synchronized
with `origin/main` and remote main.

Stage exactly the experiment run root:

`execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01/**`

including this CHANGE instance's launch, terminal STATUS, and RETURN. Stage no
other path. Specifically, do not stage, inspect, modify, stash, reset, clean,
or otherwise act on `.claude-worktrees/**` or the four unrelated dirty domain-
audit paths.

Validate JSON, diff hygiene, exact staged containment, and these hashes/counts:

- package snapshot manifest:
  `68ef7561011b2ba8a3abf69e3dc00ab0a4f4cf69b18beb982c1e1a1bd31bb72c`
  with 133 rehashing entries;
- manager manifest:
  `bbc5bddc118e2138a92fd0b465b19ad0803afea38339aefbbb9bcbfb9d56347a`
  with 29 entries;
- author/verifier manifests: 265/317 entries and exact prior identities;
- reconciliation snapshot:
  `8d5e220b1620c5d3ef62856aefaf6dcd6be4059e276561d77848bd521730dc57`
  with nine entries;
- RECON instance manifest:
  `67d494e6a109ae35d66d583e06755af15c97a1aa227f9ab014c124d81b44dd13`
  with four entries;
- 3 members, 2 Agent-2 sessions, 88 mappings, 727 source lines, exact 15-row
  replacement/inverse, 3 simulations, and five retained efficiency findings.

Confirm the staged diff changes no active Stage-2 workplan/current run,
project path, lifecycle, H1/H2, integration, instruction, or skill file. If
ready, commit with message `Record PKG-01 batch conversion experiment` and push
`main` to its existing upstream. Do not create a branch or PR. Return exact
commit/push/divergence evidence, checks, remaining external dirty paths,
blockers, and handoff.
