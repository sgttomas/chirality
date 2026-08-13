# WORKING_ITEMS activation — runtime daemon held-connection stop

- RunID: `APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- Objective: make the runtime helper's graceful stop robust under a held partial HTTP request and prove bounded teardown through an actual `SIGTERM` process path.
- Accepted basis: owner direction in the supervising HELP_HUMAN session; current `origin/main` at `f84f7b03b49ce1397b556c8e03ccc5b11c955802`; existing Root `TM-ROOT-112` force-close implementation is prior art to evaluate, not presumed deficient.
- Profile: `projects/chirality-app-dev/software-workflow.json`. It has no `runtime/**` check mapping; the owner direction expressly requires the exact local runtime focused test, full test, and typecheck commands used by this activation.
- Write boundary: `runtime/**` plus this run root. DEL-09-04 closeout surfaces remain manager-owned and are written only after accepted fan-in.
- Exclusions: packet/evidence roots, foreign loops, decision register, loop receipt, Git operations, product/runtime state outside harmless local tests, and any D-APP-93 or D-APP-88 disposition/acceptance/lifecycle act.
