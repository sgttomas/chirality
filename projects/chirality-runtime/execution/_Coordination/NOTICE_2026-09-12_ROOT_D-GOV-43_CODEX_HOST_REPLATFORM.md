# Root notice: D-GOV-43 Codex host re-platform applied to the Runtime loop

Root D-GOV-43 (ruled 2026-09-11) with its topology A2 supplement (recorded
2026-09-12) re-platforms the Chirality App onto stock OpenAI Codex App Server.
Publication SHA `d2878462be59a43b4afc175a8cce85abca9cf696`; ruling
`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`;
supplement `D-GOV-43_supplement_topology_A2.md`. This notice records the
application of that ruling to this loop under item 11's bounded coordinated
authority. It is not an adoption request and does not reopen the decision.

Topology A2: the App starts, owns and stops a simplified Runtime service as a
child process; the service speaks its existing Unix-socket API with client
tokens private to the application and owns the stock, lockfile-pinned
`codex app-server` child. The Runtime stays independent of Electron and Next;
the App is the only production consumer; Piping and local models are deferred.

Family dispositions applied here (proposal `IMPACT.md`, purpose test):
family 1 (private supplier admission and certification) and family 2
(fixed-policy control of Codex) retire; family 3 (credential and home
separation) adapts into the App's effective Codex home with private
`auth.json` and shared configuration; family 4 (ordinary software integrity)
retains; family 5 (process hygiene) retires as gates; family 6 (human
accountability) retains. Nothing is re-created under another name.

Applied on branch `claude/chirality-codex-replatform-3999f1`: `README.md`
rewritten; `docs/CODEX_MVP_INTEGRATION.md` superseded; the D-GOV-43 reading of
`docs/PRD.md` recorded in the hold-closure packet (`docs/PRD.md` itself is
Root-pinned and unchanged) and `docs/PRD_AUTHORITY.md` revised with two hashes
re-issued once; DEL-02-07 through DEL-02-12 retired in place (lifecycle state
unchanged) and DEL-02-06 revised by packet notes; SCA-004 closes the nine
`HELD_UNAVAILABLE` bindings; supersession entries in `HANDOFF_STATE.md`,
`MIGRATION_APPLICATION.md` and `MIGRATION_ACCEPTANCE_2026-09-06.md`;
`tools/codex-supplier/`, `tools/native-admission/` and
`tools/provision-hosted-release-anchor-v2.mjs` deleted (last commit
`e83cb1f47`). `AgentRuns/RUNTIME_*` records are unchanged history.

Retained modules: `RuntimeService`, session store, turn coordinator,
`DelegatedRuntime`, `CodexSupervisor`, `CodexLogin`, the socket API, client,
CLI and the PEC integration opportunity (compatibility unverified, not an MVP
prerequisite). Source changes under `packages/` and `tests/` are made by the
implementing session and reviewed independently before the consolidated
build. Release, publishing and the owner's native trial remain separate human
decisions.
