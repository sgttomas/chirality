# Execution

Server cwd frontend: `CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next dev --hostname 127.0.0.1 --port 3187`. Host escalation after earlier sandbox listen EPERM. Next15.5.21 ready883ms; root compiled1340 modules695ms. Actual tree/file/validate/deliverables returned200. Server37919 stopped Ctrl-C exit0.

Repo cwd: `node <this-directory>/evaluator.mjs`, host escalation after prior Chromium sandbox SIGABRT/EPERM, exit0. Node24.18.0 and Chromium148.0.7778.96, exact paths in evaluator. Scripts, fixture, stdout/stderr, requests/response statuses and observations preserved. All harness requests intercepted and external requests blocked; actual local endpoints use owned temporary fixtures.

Final host port check returned61 ECONNREFUSED; all25 source hashes unchanged.
