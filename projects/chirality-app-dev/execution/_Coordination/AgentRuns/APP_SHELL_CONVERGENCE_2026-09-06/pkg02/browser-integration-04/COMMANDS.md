# Execution

Server cwd frontend: `CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next dev --hostname 127.0.0.1 --port 3187`. Exact host escalation after earlier sandbox listen EPERM. Next15.5.21 ready919ms, compiled1340 modules780ms. Captured tree/file/deliverables requests200. Session49599 stopped Ctrl-C exit0. Node24.18.0 and Chromium148.0.7778.96; exact Playwright/executable paths in scripts.

Repo cwd: `node <this-directory>/keyboard.mjs`, `node <this-directory>/matrix.mjs`, `node <this-directory>/geometry-supplement.mjs`; each host-escalated after prior sandbox Chromium SIGABRT/EPERM and each exited0. Exact scripts, fixtures, stdout/stderr and results preserved. Harness routes are synthetic, file/tree requests use owned temporary fixture, external requests blocked. No real provider/account access.

Final host port check returned61 ECONNREFUSED; all25 source hashes match.
