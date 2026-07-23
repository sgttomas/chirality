# G3 Return — Desktop, CLI, and Integration Fan-In

Status: `COMPLETED`

Chirality Desktop is a daemon client. The same packaged Electron executable can
run headlessly as the per-user runtime daemon, preserving Electron safeStorage.
The Desktop settings surface reports daemon, credentials, and model residency;
legacy `/api/harness/*` routes are thin compatibility proxies.

Tracked project manifests were added for app-dev and PEC. The public exporter
includes generic runtime contracts, core, daemon, client, CLI, and safe engine
adapters while excluding credentials, machine state, and PEC-private adapters.

The bundled CLI executed through Electron's embedded Node runtime without a
global Node dependency.
