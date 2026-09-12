# Root notice: D-GOV-43 Codex host re-platform, PEC loop

Root ruled D-GOV-43 on 2026-09-11 (proposal revision 3 at
`3ef2ef524956498f8923323dc6cf9d672dbeb50b`) and recorded its topology
supplement on 2026-09-12; both are published on `main` at
`d2878462be59a43b4afc175a8cce85abca9cf696` (PR #767). This notice records
the application of that ruling under item 11's bounded coordinated
authority. It is a record of application, not an adoption request, and it
does not reopen approval of D-GOV-43.

What changes for the Runtime host: the selected topology is A2. The
Chirality App starts, owns and stops a simplified Runtime service as a child
process; the service speaks its existing Unix-socket API with client tokens
private to the application and no TCP listener, and it owns a stock,
lockfile-pinned `codex app-server` child. The per-user LaunchAgent daemon,
the supervisor's second socket, hosted admission and identity binding, the
exact-supply pin with drift refusal and the closed event vocabulary are
retired. The Runtime host stays independent of Electron and Next so later
Chirality applications can run it as an application-owned service; only the
Chirality App is implemented and qualified in this tranche.

What this means for PEC: `docs/PRD.md`, the v2 coordination-plane candidate
and `NOTICE_ROOT_RUNTIME_PROJECT_MIGRATION_2026-09-05.md` classify PEC as a
Runtime client. That classification stands, with the target re-expressed:
PEC remains a client of the Runtime socket API, now hosted as an
application-owned service rather than a per-user daemon. A2 preserves PEC's
integration opportunity. PEC's compatibility with the repaired service is
unverified and is not an MVP prerequisite; the App is the only production
consumer in this tranche. PEC revises its own text under its own instruments
and cadence; no PEC source, contract, lifecycle or release act follows from
this notice.

Application records: Root `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`
and `D-GOV-43_supplement_topology_A2.md`; App loop
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`.
This notice authorizes no release, publishing, Piping integration or
local-model work. Prepared by a bounded TASK executor; the owner has not
personally reviewed this text.
