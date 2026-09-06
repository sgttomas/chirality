# Export consumer repair — migration iteration 2

Same owner-directed migration branch, parent iteration df7d62308021e80cf3aeef758f83e8ee5069b402. Governance CI failed two export tests because the public export profile still required root runtime/. Ignored local residue masked the missing clean-checkout source with an empty runtime projection. This missed active consumer is corrected; initial sealed evidence remains unchanged.

The exporter now reads five runtime workspace root files and packages/tests from projects/chirality-runtime into the existing public runtime/ layout. Project AGENTS, manifest, PRD, loop and coordination never export. Regression assertions require actual code/package contents and reject governance scaffold paths. Tests use scratch staging; no public release is performed. G4 records the exporter/test repair; App receives the follow-on notice.

Focused tests28 PASS; independent read-only review PASS without findings. Full affected suite and Root guards/entry/status/self-check are in CHECKS.json. App registered premerge and PEC CI passed on df7d623, resolving that commit’s local binding-only limitation. New HEAD requires its own CI. Runtime/App/PEC source and review seals remain unchanged.

Accepted source, authority package, lifecycle and pointers remain untouched. Current baseline audit findings and nine holds remain. Derivative evidence only; ownership transfer and governance-only Root require exact owning acceptance. Rollback restores the coherent migration including exporter mapping; no operational state conversion. One corrective receipt/commit/push updates PR727, no self-merge.

Parent /root HELP_HUMAN, OpenAI GPT-6, exact serving model ID unavailable; Agent0 role not mechanically enforced. Native reviewer runtime_workspace_move is instruction-asserted with actual brief/return here. Next owner: Ryan Tufts for exact transfer subjects and PR merger readiness after CI.
