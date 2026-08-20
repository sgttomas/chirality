# API-key environment-precedence repair — orchestration plan v1

Status: `FROZEN BEFORE IMPLEMENTATION`

## Activation identity

- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- Parent: `HELP_HUMAN`
- Selection authority: `HUMAN+AGENT_0`. The owner expressly authorized the
  cross-package repair and thereby unlocked the recorded-limit owner gate;
  Agent 0 selected and serialized the three package nodes below.
- Branch: `codex/app-api-key-precedence-20260820`
- Accepted basis and stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`
  (PR #586 head). The tranche targets a stacked PR whose base is the PR #586
  branch unless that predecessor merges before publication.
- Pattern: `MIXED`, serialized `N1 -> N2 -> N3 -> integrated fan-in -> CHANGE`.
- Package ownership: three separate WORKING_ITEMS instances are mandatory.
  This run-level graph does not authorize any instance to manage another
  package. The present instance is assigned only N3 / PKG-09 plus run-level
  integration coordination after accepted predecessor handoffs.

## Step 0 basis

- `loop/LOOP_RECEIPTS.md` Receipt 180 records the packaged-security tranche
  and the sole accepted blocker: production order in
  `frontend/electron/api-key-storage.ts` is reversed relative to the accepted
  `DEL-02-05-R03` / `DEL-04-05-RQ-001` contract.
- Live source at the accepted basis checks `CHIRALITY_ANTHROPIC_API_KEY`
  before `ANTHROPIC_API_KEY`; accepted order is UI safeStorage first,
  `ANTHROPIC_API_KEY` second, then `CHIRALITY_ANTHROPIC_API_KEY`.
- The receipt validator passes. Authority corpus v18 reports no drift. The
  current decision register is ruled through D-APP-103; the owner's explicit
  run direction is the narrow repair authority and grants nothing beyond it.
- The accepted software method profile is `software-workflow.json` under
  `docs/SOFTWARE_WORKFLOW_PROFILE.md`. Current source/status/dependency truth
  assigns runtime semantic ownership to DEL-04-05, UI/status contract
  consumption to DEL-02-05, and packaged-proof consumption to DEL-09-06 with
  DEL-09-04 as its dependent consumer.
- RunID uniqueness was confirmed before this record was created.

## APP-HOLD dispatch preflight

From `projects/chirality-app-dev`:

```text
/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path agents/AGENT_WORKING_ITEMS.md --target DEL-04-05 --target DEL-02-05 --target DEL-09-06 --target DEL-09-04
```

Result: `ALLOW` for all four targets. Active and scanned held sets are empty;
every target is `CLEAR` / `NOT_HELD`.

- Repository HEAD: `6710ee6354debc201f6a454e2802897026cd4b38`
- Register SHA-256: `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`
- Scan fingerprint SHA-256: `8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`

Each manager reruns APP-HOLD before dispatch and before reliance.

## Selected nodes

### N1 — PKG-04 / DEL-04-05 — primary runtime semantic owner

- Instance: `WI-PKG04-API-KEY-PRECEDENCE-01`
- Objective: repair the Electron environment fallback to the accepted
  safeStorage > `ANTHROPIC_API_KEY` > `CHIRALITY_ANTHROPIC_API_KEY` order and
  replace the self-expiring expected-failure with positive regression coverage.
- Write owner: production source and focused automated test bytes, plus
  PKG-04 run evidence and truthful DEL-04-05 state calibration.
- Checks: focused API-key-storage tests, full frontend Vitest, frontend and
  Electron typecheck as applicable, build, registered harness/self-check and
  APP-HOLD, then fresh 100% read-only software review. All are in-session.
- Acceptance: both-primary-present and every other precedence case match the
  accepted contract; no provider, credential-storage, or error-semantic
  expansion; DEL-04-05 state changes only where evidence proves RQ-001.

### N2 — PKG-02 / DEL-02-05 — dependent UI/status contract consumer

- Instance: `WI-PKG02-API-KEY-PRECEDENCE-01`
- Dependency: accepted terminal N1 handoff.
- Objective: verify the fixed runtime/status behavior against DEL-02-05-R03,
  repair only stale or incomplete PKG-02 evidence/state, and close only what
  the accepted contract and checks prove.
- Write owner: PKG-02 evidence, run records, memory, and status only. Product
  source and the N1-owned test are read-only.
- Checks: focused API-key status/UI regression evidence, affected/full
  registered frontend gates, harness/self-check, APP-HOLD, record/schema and
  diff hygiene; fresh read-only review if any executable or substantive
  acceptance evidence is added. In-session.

### N3 — PKG-09 / DEL-09-06 with DEL-09-04 dependent consumer

- Instance: `WI-PKG09-API-KEY-PRECEDENCE-01`
- Dependency: accepted terminal N2 handoff.
- Objective: rebuild the unsigned desktop artifact from the repaired bytes,
  rerun the packaged security proof, update compact identity-bound evidence,
  and remove only the DEL-09-06 and DEL-09-04 packaged-security residuals
  proven by the passing result.
- Write owner: PKG-09 proof/evidence scripts only if the fixed product identity
  requires bounded compatibility glue, compact proof evidence, PKG-09 run
  records/memory/status, and run-level integration return after predecessor
  handoffs. N1 product/test bytes and PKG-02 state are read-only.
- Checks: focused and full frontend tests, applicable typecheck/build, secret
  scan, network policy, instruction-root integrity, unsigned `desktop:dist`,
  packaged Electron/keychain/network proof, APP-HOLD, containment and diff
  hygiene, followed by fresh integrated 100% read-only review.
- Surfaces: deterministic checks in-session; unsigned packaging and exact
  Electron/keychain/process proof on the host-capability surface after exact
  escalation. CI may supplement only registered checks.

## Serialization and failure behavior

The three nodes share the frontend gate surface, so they are not eligible for
parallel execution even though their package-state writes are disjoint. A
failed node holds only its declared dependants. Passed predecessor work may be
returned for CHANGE as a partial landing; no manager silently widens another
package or converts a discovered target into a new node.

## Parked exclusions

Login-time `RunAtLoad`, owner-machine daemon deployment, signing,
notarization, distribution/publication, release or lifecycle claims, provider
expansion, dependency or lockfile changes, root/foreign-loop governance,
decision-register edits, and any newly discovered engineering target are
parked. The accepted F-APP-2 and APP-HOLD fences remain unchanged.

## Closeout

After all accepted node returns and fresh review, N3 integration coordination
performs candidate-wide containment, parse, whitespace, APP-HOLD reliance,
and state-consistency validation. Git commit/push/stacked-PR work is routed
only to CHANGE. Receipt and shared completion-log writes remain post-review
Agent 0/CHANGE work and are not authorized by this record.
