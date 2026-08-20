# Work graph v2 — API-key environment-precedence repair

Status: `FROZEN BEFORE AMENDMENT PRODUCT WRITES`

Selection authority: `HUMAN+AGENT_0`
Amendment disposition: `AMEND+RELAY — no new node`
Pattern: `MIXED`
Branch: `codex/app-api-key-precedence-20260820`
Basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`

```text
N1 PKG-04 / DEL-04-05
  accepted env-order repair
  + amendment: non-secret store-owned source discriminator
  + focused/full checks + fresh read-only review
  |
  v accepted terminal amended handoff
N2 PKG-02 / DEL-02-05
  IPC consumes source discriminator; no environment re-inference
  + focused/full checks + fresh read-only review
  |
  v accepted terminal amended handoff
N3 PKG-09 / DEL-09-06 -> DEL-09-04 (unchanged)
  fresh unsigned dist + packaged security proof + state calibration
  |
  v
fresh integrated 100% read-only review
  |
  v PASS with zero actionable findings
run fan-in + APP-HOLD reliance + CHANGE handoff
```

## Revised node contract table

| Node | Package instance | Depends on | Product write owner | Required checks | Terminal return |
|---|---|---|---|---|---|
| N1 | `WI-PKG04-API-KEY-PRECEDENCE-01` | none | `api-key-storage.ts` and focused storage test | focused/full Vitest, typecheck, build, harness/self-check, APP-HOLD, secret/scope/whitespace; fresh read-only review | fixed order plus accurate non-secret source fact, exact evidence/state, blockers/reruns |
| N2 | `WI-PKG02-API-KEY-PRECEDENCE-01` | accepted amended N1 | `api-key-ipc.ts` and focused IPC test | focused storage/IPC contract tests, full Vitest, typecheck, build, harness/self-check, APP-HOLD, secret/scope/whitespace; fresh read-only review | correct UI/env/none IPC classification, exact evidence/state, blockers/reruns |
| N3 | `WI-PKG09-API-KEY-PRECEDENCE-01` | accepted amended N2 | unchanged PKG-09 compact proof/evidence/state boundary | v1 focused/full/secret/network/instruction/unsigned-dist/packaged-host/APP-HOLD gates; fresh integrated review | identity-bound packaged PASS or exact blocker, calibrated DEL-09-06/DEL-09-04 state, CHANGE handoff |

## Preserved invariants

- One WORKING_ITEMS instance owns exactly one package.
- N1 owns the store fact; N2 owns the IPC classification; N3 consumes the
  integrated behavior in the packaged artifact.
- Status responses reveal only a source token, never credential material.
- Existing provider identities, error/unavailable semantics, fixed
  environment order, release fences, lifecycle, dependencies, and lockfile
  remain unchanged.
- Only an accepted terminal return releases the next node.
