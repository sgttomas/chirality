# API-key environment-precedence repair — orchestration plan v2

Status: `FROZEN BEFORE AMENDMENT PRODUCT WRITES`

This plan supersedes v1 for dispatch and fan-in. The activation identity,
branch, accepted basis, three separate package managers, exclusions, release
fences, and N3 objective in `ORCHESTRATION_PLAN.md` remain unchanged.

## Amendment authority and finding

- Disposition: `AMEND+RELAY`; no new engineering node.
- Authority: the owner's accepted cross-package API-key precedence repair and
  Agent 0's in-run disposition of the dependent DEL-02-05-R03 finding.
- N2 verified that the existing IPC status heuristic cannot distinguish a
  configured safeStorage/UI credential from an environment fallback. When an
  environment key exists concurrently with a safeStorage key, it labels the
  resolved UI credential as `env`, contradicting the accepted UI > env > none
  status contract.
- The finding belongs to the selected cross-package repair: PKG-04 owns the
  credential-store status fact and PKG-02 owns the renderer-facing IPC
  classification. It does not authorize a fourth node, provider expansion,
  credential disclosure, or unrelated status redesign.

## APP-HOLD dispatch preflight

Rerun from `projects/chirality-app-dev` before amendment writes:

```text
/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path agents/AGENT_WORKING_ITEMS.md --target DEL-04-05 --target DEL-02-05 --target DEL-09-06 --target DEL-09-04
```

Result: `ALLOW` for all four targets. Every target is `CLEAR` / `NOT_HELD`;
active and scanned held sets are empty.

- Repository HEAD: `6710ee6354debc201f6a454e2802897026cd4b38`
- Register SHA-256: `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`
- Scan fingerprint SHA-256: `8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`

Each amended manager reruns APP-HOLD before child dispatch and reliance.

## Revised serialized graph

### N1 / PKG-04 amendment — store-owned source fact

- Manager: `WI-PKG04-API-KEY-PRECEDENCE-01`.
- Preserve the already reviewed environment order in
  `frontend/electron/api-key-storage.ts`.
- Amend `SafeStorageCredentialStore.status` to return a non-secret credential
  source discriminator sufficient to distinguish stored/UI, environment, and
  unconfigured resolution. No credential value may cross the status API.
- Add focused storage tests covering stored/UI precedence over simultaneous
  environment values, canonical environment, compatibility environment, oMLX
  environment, and unconfigured status.
- Write ownership: `frontend/electron/api-key-storage.ts`, its focused test,
  PKG-04 evidence/state, and PKG-04 run-local records only.
- Checks: focused storage tests; full frontend Vitest; frontend/Electron
  typecheck; build; registered harness/self-check and APP-HOLD; secret scan,
  scope/whitespace checks; fresh 100% read-only review. In-session.
- Acceptance: discriminator is accurate, non-secret, provider-isolated, and
  preserves the fixed environment precedence and all existing get/set/remove
  behavior.

### N2 / PKG-02 amendment — IPC consumer

- Manager: `WI-PKG02-API-KEY-PRECEDENCE-01`.
- Dependency: accepted terminal handoff from amended N1.
- Amend `frontend/electron/api-key-ipc.ts` and its focused test so IPC status
  consumes the store-owned discriminator rather than re-inferring source from
  the Electron process environment.
- Preserve the public renderer result vocabulary `ui | env | none`, daemon
  unavailable behavior, non-secret response, provider isolation, and existing
  store/remove contracts.
- Write ownership: `frontend/electron/api-key-ipc.ts`, its focused test,
  PKG-02 evidence/state, and PKG-02 run-local records only. N1 product/test and
  PKG-04 state are read-only.
- Checks: focused IPC and storage contract tests; full frontend Vitest;
  frontend/Electron typecheck; build; registered harness/self-check and
  APP-HOLD; secret scan, scope/whitespace checks; fresh 100% read-only review.
  In-session.
- Acceptance: simultaneous UI and environment credentials report `ui`;
  environment-only reports `env`; no credential reports `none`; unreachable
  daemon remains structured/unavailable; no renderer credential exposure.

### N3 / PKG-09 — unchanged downstream proof consumer

N3 remains held until amended N1 and N2 each return accepted terminal
handoffs. Its unsigned dist, packaged security proof, compact evidence,
DEL-09-06 / DEL-09-04 state calibration, checks, host surface, fresh integrated
review, and exclusions remain exactly as frozen in v1.

## Serialization and closeout

Execution order is `N1 amendment -> fresh N1 review -> N2 amendment -> fresh
N2 review -> N3 -> fresh integrated review -> fan-in -> CHANGE`. The shared
frontend gate surface prohibits parallel execution. Remediation/re-review is a
proof-loop attempt inside the owning node, not a new node. Receipt, completion
log, commit, push, and stacked PR publication remain outside manager authority
until post-review CHANGE closeout.
