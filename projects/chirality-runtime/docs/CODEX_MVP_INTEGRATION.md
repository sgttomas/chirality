# Codex MVP integration (superseded)

Status: SUPERSEDED 2026-09-12 under D-GOV-43 (ruled 2026-09-11) and its
topology A2 supplement (recorded 2026-09-12).

This document described the daemon-era Codex integration: the authenticated
supervisor socket owning the transport, the staged and verified supplier
executable, the `workspaceWrite`-only permission profile, the native-plan REST
routes and the `nativeAddonPath` admission binding. That design is retired.
The Runtime is now an application-owned service that hosts the stock,
lockfile-pinned `codex app-server` child inside one process; policy is the
user's choice from Codex's own options; the full notification and
server-request stream is carried through.

The current host design is recorded in Root `docs/SPEC.md` section 14 and in
`projects/chirality-app-dev/docs/SPEC.md`. The ruling and supplement are
`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` and
`D-GOV-43_supplement_topology_A2.md`; the family dispositions are in the
proposal packet's `IMPACT.md`.

The original text of this document is retained in git history at commit
`e83cb1f47` and is not repeated here.
