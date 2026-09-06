# Actual commands and execution

Server cwd frontend: `CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next dev --hostname 127.0.0.1 --port 3187`. Exact host escalation used after previous identical sandbox listen EPERM. Next15.5.21 ready1036ms, compiled1354 modules1022ms, all captured root/tree/deliverables requests200. Session67441 stopped Ctrl-C exit0. Node24.18.0, Chromium148.0.7778.96; evaluator records exact Playwright and executable paths.

Repo cwd commands `node <this-directory>/first-capture.mjs`, `dev-menu.mjs`, `dev-menu2.mjs`, `dev-preferences.mjs`, `matrix.mjs`, `matrix2.mjs` used exact host escalation after earlier Chromium sandbox SIGABRT/EPERM. First four exited0. First development menu capture preceded transition; second waited500ms and then observed menu. Preferences inspection waited300ms after click. Matrix exited1 for evaluator container-width assertion; matrix2 exited1 for actual Settings pointer interception. Available command stdout/stderr persisted; menu probes produced no stdout/stderr in tool output.

All product API traffic isolated to loopback with harness route fixtures; no account/provider calls. No source writes. Temporary fixture source bytes preserved. Final host socket verification returned61 ECONNREFUSED.
