# Work graph v1 — API-key environment-precedence repair

Status: `FROZEN`

Selection authority: `HUMAN+AGENT_0`
Pattern: `MIXED`
Branch: `codex/app-api-key-precedence-20260820`
Basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`

```text
N1 PKG-04 / DEL-04-05
  implementation + focused/full registered checks + fresh read-only review
  |
  v accepted terminal handoff
N2 PKG-02 / DEL-02-05
  dependent contract verification/state calibration + registered checks/review
  |
  v accepted terminal handoff
N3 PKG-09 / DEL-09-06 -> DEL-09-04
  fresh unsigned dist + packaged security proof + state calibration
  |
  v
fresh integrated 100% read-only review
  |
  v PASS with zero actionable findings
run fan-in + APP-HOLD reliance + CHANGE handoff
```

## Node contract table

| Node | Package instance | Depends on | Write owner | Check surface | Terminal return |
|---|---|---|---|---|---|
| N1 | `WI-PKG04-API-KEY-PRECEDENCE-01` | none | Electron key-store source, focused test, PKG-04 evidence/state | in-session focused/full Vitest, typecheck, build, harness/self-check, APP-HOLD; fresh read-only review | fixed runtime semantics, exact checks/evidence, calibrated DEL-04-05 state, blockers/reruns |
| N2 | `WI-PKG02-API-KEY-PRECEDENCE-01` | accepted N1 | PKG-02 evidence/state only | in-session focused UI/status evidence, registered frontend gates, harness/self-check, APP-HOLD, record/diff checks; review as required | verified R03 consumer behavior, calibrated DEL-02-05 state, blockers/reruns |
| N3 | `WI-PKG09-API-KEY-PRECEDENCE-01` | accepted N2 | PKG-09 compact proof/evidence/state and final integration records | in-session focused/full gates, secret/network/instruction checks; host unsigned dist + packaged Electron/keychain/network proof; fresh integrated review | identity-bound packaged PASS or exact blocker, calibrated DEL-09-06/DEL-09-04 state, CHANGE handoff |

## Graph invariants

- One WORKING_ITEMS instance owns exactly one package.
- The graph is serialized because all nodes share the frontend gate surface.
- Only the named write owner changes a shared or semantic surface.
- A predecessor releases its dependant only after terminal validation and
  APP-HOLD reliance.
- Remediation and fresh re-review remain inside the originating node; they do
  not create an additional engineering node.
- Product acceptance, lifecycle, release, signing, distribution, RunAtLoad,
  and owner-machine deployment are not inferred from proof or state writes.
