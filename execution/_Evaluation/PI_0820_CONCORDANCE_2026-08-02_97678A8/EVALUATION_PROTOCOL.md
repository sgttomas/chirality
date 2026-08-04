# Evaluation protocol — Pi 0.82.0 concordance and supply-chain validation

Run ID: `PI_0820_CONCORDANCE_2026-08-02_97678A8`
Parent run: `ROOT_FOUR_LANES_2026-08-02`, node `E1`
Manager: `EVALUATION`
Execution root: repository `execution/`
Repository snapshot: `97678a841ef58345c73d3470ed8de57c9b1405d2`
Posture: read-only evaluation; outputs are derivative evidence, never approval

## Accepted basis

- Owner harvest ruling: `execution/_Coordination/_TaskManagement/RULING_2026-08-02_ROOT_HARVEST_SLATE.md`, SHA-256 `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`, item 3 / `TM-ROOT-106`.
- D-APP-84 REV2 Root route: `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`, SHA-256 `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- App governing decision currently naming Pi `0.80.10`: `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-72_RULING_2026-07-21.md`, SHA-256 `c7dcbb5aaa0f82481fb76825c7099c4e355c4ada80232c51f3a3cf6ba2076577`.
- D-APP-84 REV2 packet and ruling, respectively SHA-256 `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9` and `f439c79e358ffaa1e30f897cd1be901195aa1b4b2a184e2c0465a8ee87461c58`.
- Root and App source, package, lockfile, notice, lifecycle, packaging, regression, and conformance surfaces at the frozen repository snapshot.

## Questions and decision criteria

1. Do all declared Pi dependencies close exactly and with verifiable lockfile integrity at `0.82.0`?
2. Do install scripts, native modules, and WASM assets conform to the recorded lifecycle and distribution policy?
3. Are notices complete, adapter identity unambiguous, and package/runtime behavior supported by regression and conformance evidence?
4. What exact authority conflict exists between D-APP-72 / App `0.80.10` and executable Root/App `0.82.0`, and what supersession path is required?
5. Which decision-ready option best preserves the evidence while refusing to treat present bytes as approval?

The evaluation may recommend but may not make the Pi-version, lifecycle, reliance, release, or supersession decision. No score is requested and no scoring rubric is selected.

## Scope and exclusions

In scope: exact Pi dependency closure/integrity; lifecycle scripts; native and WASM policy; notices; adapter identity; Root/App packaging, regression, and conformance evidence; authority and supersession chain.

Excluded: source repair, dependency or lockfile edits, App authority writes, SCOPE_CHANGE writes, decision records, register changes, Git mutations, release or reliance acts.

## Accepted toolbelt and dispatch order

- Deterministic read-only commands: `git`, `rg`, `find`, `shasum`, Node/npm inspection and existing read-only verification/test scripts where they do not mutate governed state.
- `EVALUATION_DEPENDENCY_AUDIT` for exact dependency/integrity/supply-chain closure.
- `EVALUATION_STRUCTURE_AUDIT` for lifecycle/native/WASM/notices/packaging/regression evidence.
- `AUDIT_GOVERNANCE` for authority, adapter identity, conflicts, and supersession path.

The owner explicitly permitted bounded read-only Agent 2 checks. These three scopes are independent evidence lenses over the same frozen snapshot and may fan out concurrently. Each return is preserved under `returns/`; synthesis is prohibited until schema, scope, evidence, and write containment are validated.

## Outputs and decision points

- `EVALUATION_REPORT.md`, `FINDINGS.csv`, and `HANDOFF.md` in this directory.
- Child launch briefs and preserved returns under `returns/<DispatchID>/`.
- E1 instance `RETURN.md` and `STATUS.md`.
- Human decision: retain D-APP-72 `0.80.10`, explicitly supersede it in favor of `0.82.0`, or reject/remediate `0.82.0`; present bytes cannot decide this.
- Later owners: `SCOPE_CHANGE` for governed decomposition/authority propagation, App client owner for dependency/adapter/package changes, and `CHANGE` only after an accepted decision and validated implementation tranche.

## Closure conditions

Evaluation closeout requires evidence-linked findings, exact conflicts and unknowns, validation commands/results, decision options and recommendation, named owners, blockers, and rerun requirements. It does not close `TM-ROOT-106` and does not approve Pi `0.82.0`.
