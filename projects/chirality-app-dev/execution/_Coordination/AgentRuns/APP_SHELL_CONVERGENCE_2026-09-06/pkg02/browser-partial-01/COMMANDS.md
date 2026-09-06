# Actual commands and outcome
Cwd repository unless specified. Node v24.18.0; Next15.5.21; Playwright cached module path and Chromium executable are recorded verbatim in evaluator.mjs. No live account/runtime calls; harness routes intercepted. Only projectRoot fixture path seeded; no secrets printed.

Server cwd frontend: `CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next dev --hostname 127.0.0.1 --port 3187`. Sandbox returned listen EPERM (process exit0 despite failed startup); exact escalated command succeeded, session87400, ready999ms. Next compiled root1379modules1143ms, tree/file real endpoints returned200. Stopped via Ctrl-C exit0.

`node <this-directory>/evaluator.mjs`: sandbox launch SIGABRT/EPERM preserved sandbox-launch-failure.json. Exact escalated evaluator exited1 due heading selector ambiguity: hidden h2 and visible h1 both named Shell redesign checkpoint. evaluator.stdout.log/stderr.log preserved. No product failure inferred from evaluator error. failure.png is the actual document1440light screenshot.

`node <this-directory>/diagnostic.mjs`: exact escalated diagnostic exited0; observations and screenshots1440/960/900light preserved. Read-only reviewer requested stopped checkpoint for source repair; no further matrix attempted.
