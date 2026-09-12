# Root notice: D-GOV-43 Codex host re-platform applied to the App loop

Root ruled D-GOV-43 on 2026-09-11 (proposal revision 3 at
`3ef2ef524956498f8923323dc6cf9d672dbeb50b`) and recorded its topology
supplement on 2026-09-12; both are published on `main` at
`d2878462be59a43b4afc175a8cce85abca9cf696` (PR #767). This notice records
the application of that ruling to the App loop under item 11's bounded
coordinated authority. It is a record of application, not an adoption
request, and it does not reopen approval of D-GOV-43.

The selected topology is A2. The App starts, owns and stops a simplified
Runtime service child; the service speaks its existing Unix-socket API with
client tokens private to the application and no TCP listener, and owns the
stock, lockfile-pinned `codex app-server` child. The socket API, client,
harness port and Next routes are retained and repaired: loopback HTTP and
SSE through the in-process Next server remain the renderer channel, the SSE
keepalive, timeout and disconnect defects are repaired, and a renderer
disconnect no longer interrupts a turn. Retired from the App path are the
LaunchAgent and installer (DEL-09-07 and APP-HOLD-1), hosted admission and
identity binding, restart admission, the native admission addon, the
host-account XPC channel, supplier containment evidence, packaged-basis
hashing, the Stage 9 to 13 packaging spine, the per-chat model and effort
freeze and the closed event vocabulary. Codex remains the sole engine.

Applied App surfaces: `_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`
supersedes in the stated parts D-APP-125 item 3, D-APP-126, D-APP-122,
D-APP-100, D-APP-88 and D-APP-107; SCA-APP-008 is revised before any
acceptance (`_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/REVISION_2026-09-12_D-GOV-43_A2.md`);
PKG-09 DEL-09-03 to DEL-09-07, PKG-03 DEL-03-01 to DEL-03-04, PKG-05
DEL-05-02 and PKG-02 DEL-02-05 carry revised Remaining items; the hold
register row for DEL-09-07 is retired; earlier notices carry supersession
headers. The new short packaging procedure and native checklist are in
`AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`. Executed trial records,
packaging stage records and daemon-era chats are preserved unchanged; the
new procedures supersede their applicability.

Not yet revised in this tranche, flagged for the owning loop: the
"Shared Runtime Boundary" and D-APP-107 preflight paragraphs of
`projects/chirality-app-dev/AGENTS.md`, `docs/harness/reliance_boundary_register.md`,
`docs/RELEASE_QUALITY_GATES.md`, the corpus-hashed App documents and
`frontend/docs/harness/*`, all named in IMPACT.md for clause-level revision.

This notice authorizes no release, publishing, trial acceptance, change to
the Codex sole-engine rule, local-model work or reliance on the retired
daemon path. Prepared by a bounded TASK executor; the owner has not
personally reviewed this text.
