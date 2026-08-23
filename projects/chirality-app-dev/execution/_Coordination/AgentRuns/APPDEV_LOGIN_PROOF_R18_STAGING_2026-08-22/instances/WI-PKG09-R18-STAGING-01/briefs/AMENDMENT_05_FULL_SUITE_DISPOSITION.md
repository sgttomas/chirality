# Amendment 05 — full-suite disposition

Disposition: `RECORD / CURE`

Owner classifies the retained 21 sandbox socket-bind failures as
`ENVIRONMENT_SANDBOX_SOCKET_DENIAL`, not a tranche defect, and authorizes one
exact `npm test` rerun with local loopback/Unix-socket permission. No source
change, network request/tool, package rerun, or other full-suite rerun is
authorized. The retained sandbox result remains not PASS.

R18/status will record the diagnostic, cure evidence, identical before/after
source state, and future PR pre-merge `full_test` + typecheck confirmation as
not yet observed. A TM candidate for deterministic sandbox handling is
harvested only; no implementation or register disposition occurs.
