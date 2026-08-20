# WI-PKG09-RUNATLOAD-01 — Intra-package Work Graph v1 (frozen)

- Frozen: `2026-08-20`
- Selection authority: HELP_HUMAN launch brief plus D-APP-97 C1 and live
  DEL-09-04 Remaining.
- Posture: `MIXED` — one write-capable implementation child followed by a fresh
  read-only reviewer over 100% of the frozen diff.
- Package/deliverable: `PKG-09` / `DEL-09-04` only.

## Nodes

1. `A2-PKG09-RUNATLOAD-IMPLEMENT-01` — `TASK + software-bounded-implementation`
   - Objective: add a reusable, fail-closed packaged LaunchAgent `RunAtLoad`
     proof script, focused tests, and the smallest CI integration needed to run
     it under the disposable macOS runner account's actual
     `~/Library/LaunchAgents`.
   - Reads: launch brief/basis, current unsigned Desktop workflow, frontend
     package/packaging/daemon sources and tests, shared runtime LaunchAgent/CLI
     sources, validation docs.
   - Writes: `projects/chirality-app-dev/frontend/scripts/**`,
     `projects/chirality-app-dev/frontend/src/__tests__/scripts/**`,
     `projects/chirality-app-dev/frontend/package.json` only if a reusable
     registered script is required, `.github/workflows/desktop-release-template.yml`,
     and its own run-root records. Dependencies and lockfiles are excluded.
   - Expected return: changed paths, behavior, focused/registered checks,
     proof contract, containment, residual CI/host rerun, blockers.
   - Gate: focused tests and typecheck pass; script fails closed on non-macOS,
     default label/path, non-packaged identity, missing automatic launch, and
     incomplete process/job/plist cleanup.

2. `A2-PKG09-RUNATLOAD-REVIEW-01` — fresh `TASK + software-code-review`
   - Dependency: accepted implementation return from node 1.
   - Reads: 100% frozen implementation diff and all relevant basis/source/tests.
   - Writes: none; runtime-owned launch/status/return records only.
   - Expected return: `PASS` or actionable findings with file/line evidence.
   - Gate: `PASS` with no actionable finding; otherwise return to a fresh
     bounded remediation attempt and re-review.

## Edges and ownership

- Edge: `IMPLEMENT-01 -> REVIEW-01`.
- Concurrency: none; review depends on the frozen implementation diff.
- Integration owner: WORKING_ITEMS accepts/rejects child returns and owns
  package fan-in. Agent 0 owns shared state disposition; CHANGE owns Git.
- Failure isolation: implementation failure holds review and returns the node;
  review failure holds package acceptance while preserving validated product
  work for bounded remediation.
- Escalation points: any default-label/path contact, owner-account state,
  destructive cleanup outside the unique proof identity, proof weakening,
  unregistered full check, release/public contract expansion, or fenced scope.

## Check surfaces

- In-session: focused Vitest, registered frontend test/typecheck/build as
  selected by the profile, workflow static contract tests, APP-HOLD integrity,
  practitioner harness self-check, scope validation, and diff checks.
- CI/host capability: macOS packaging plus real launchd bootstrap in the
  disposable runner account's actual `~/Library/LaunchAgents`; this proof is
  owed until the PR exists and its Desktop workflow completes.
- Proof invariant: bootstrap with `RunAtLoad` must launch automatically; the
  proof must not issue `launchctl kickstart`.
