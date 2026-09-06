# Runtime relocation verification — completed candidate

Parent: /root HELP_HUMAN. Child: /root/runtime_workspace_move, ephemeral Agent 2, OpenAI GPT-6; exact serving model ID unavailable. Role and non-delegation are instruction-asserted, not mechanically enforced. No children or Git mutations. Basis and scope are the sealed RUNTIME_BRIEF.md and SOURCE_RELOCATION.json.

All 79 relocated tracked files remain byte-identical to the source map, including package identities, lockfile, source, tests and README. No runtime source/config/test changes were necessary. Relative TypeScript references, CLI test aliases and process-signal fixture discovery are internal to the workspace; no repository-depth fix was needed. Source conservation is recorded in RUNTIME_CHECKS/source-conservation.json.

`npm ci` in projects/chirality-runtime exited 0 (61 packages installed; npm warned about unapproved esbuild/fsevents install scripts). `npm run typecheck --prefix projects/chirality-runtime` and `npm run build --prefix projects/chirality-runtime` each exited 0. Destination dependencies and generated builds were made available to the parent for consumer validation.

The first `npm test --prefix projects/chirality-runtime` run exited 1: 61 passed, 18 failed because sandboxed local socket listeners returned EPERM. The same command with approved sandbox escalation exited 0: all 79 tests across nine files passed, including real temporary Unix socket transport, daemon shutdown and local governed-child fixtures. This is local fixture execution, not a live provider API or operational user-state migration. Exact commands, exits and raw test/build logs are under RUNTIME_CHECKS/.

Changed paths owned by this child: this return and RUNTIME_CHECKS/{checks.json,source-conservation.json,typecheck.log,build.log,test-sandbox.log,test.log}. Generated ignored node_modules/dist outputs are not publication artifacts. No runtime tracked path changed after the parent's relocation.

Closure: runtime workspace relocation verification PASS as a migration candidate. Parent must integrate App/PEC consumers, CI and exact authority packages; no runtime feature/release acceptance, source/destination authority acceptance, operational credential/state transfer or future PR merge is claimed.
