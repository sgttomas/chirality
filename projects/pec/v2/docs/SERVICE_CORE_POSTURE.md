# PEC v2 service-core posture

This note records the posture enforced by
`v2/tools/check_service_core_posture.py`. It describes a continuing PEC build
gate; it is not a completion claim, release act, or source of governed truth.

## Operative definitions

The **service core** is exactly the production Python surface rooted at
`v2/src/pec_v2/core`. A **runtime dependency** is an import reachable from a
production Python module in that surface. Python standard-library modules,
PEC-local modules rooted at `v2/src`, and workspace-internal runtime-contract
packages explicitly enumerated in `v2/config/service_core_posture.json` are
not third-party runtime dependencies. The initial explicit workspace-contract
set is empty; there is no wildcard or implicit admission. Build, test, and
development imports outside the operative core are not runtime dependencies.

## Enforced rules

- `PEC-SVC-001`: the service core has zero third-party runtime dependencies.
  The only permitted exception class is an explicitly enumerated
  workspace-internal runtime-contract package.
- `PEC-SVC-002`: the service core initiates and configures no external network
  egress.

The checker evaluates dependency and locality assertions on every registered
run. It fails closed on a violation, missing or unreadable input, unclassifiable
import, tooling error, or missing workflow registration. Every verdict names
the exact SHA-256 digests of the evaluated core tree, configuration bytes, and
workflow bytes, so a passing result is not reusable for a later state.

## Reading and acting on a failure

A finding identifies its source location and, for a dependency finding, the
dependency and importer. Under the owner-selected D-PEC-77 G-A policy, a
failed, missing, or unevaluated assertion blocks a **PEC release candidate**.
That force is PEC-only: the mechanism does not veto Git, release another loop,
or bind any governed act outside PEC.

The checker only reads repository files. It makes no network call, opens no
socket or service, edits no source or manifest, and holds no authoritative
state. PEC can be absent without blocking any governed act. The gate therefore
constrains PEC's own build without making a governed act depend on PEC-held
state or availability.

## Open transport question

`OI-009` / `SOW-083` remains open: the API transport may ultimately be Unix
socket only or may additionally permit a loopback listener. Unix-domain and
loopback-only patterns receive the same local classification under either
reading. That classification does not authorize loopback, resolve the open
question, or pre-empt its later owner ruling.

This note confers no cross-loop, Git, lifecycle, acceptance, release, or
professional-reliance authority, and it does not assert that DEL-01-05 or its
continuing obligations are complete.
