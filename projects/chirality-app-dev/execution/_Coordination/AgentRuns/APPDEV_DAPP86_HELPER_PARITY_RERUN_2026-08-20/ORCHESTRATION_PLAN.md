# Orchestration Plan v1 — D-APP-86 post-helper parity rerun

Status: `FROZEN — EXECUTION AUTHORIZED`

- RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
- Selection authority: App `HELP_HUMAN`, applying the owner's standing development-pressure direction and the live DEL-02-02 mandatory rerun trigger.
- Accepted basis: clean branch `codex/app-dapp86-helper-parity-rerun-20260820` at `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`; D-APP-86 Option A; accepted D-APP-88/D-APP-93 closure and PR #552 remedy.
- Posture: `MIXED`.
- Single shared evidence owner: `WI-PKG02-DAPP86-RERUN-01`.
- Derivative status: this run package is evidence/control-plane material only and cannot replace product, decomposition, decision, lifecycle, or owner truth.

## Parent graph

1. `N1` — PKG-02 / DEL-02-02 integrated executing-case evidence. Build one frozen unsigned package basis, bind the distinct helper identity, and execute the D-APP-86 Workbench, Pipeline, in-flight selection guard, post-completion recorded-session selection, and real-daemon replay observations. Checks run on the local macOS host in-session and on the packaged app host-capability surface.
2. `N2` — PKG-08 dependent deliverable disposition. It is released only after Agent 0 accepts N1 evidence. Its own package manager owns any PKG-08 writes and checks. Edge: `N1 -> N2`.

No third node is manufactured. Shared receipt/register/completion-log writes remain reserved to Agent 0 fan-in.

## N1 internal graph

1. `E1` — one bounded Agent 2 executor owns isolated build/runtime execution and writes only its instance evidence plus the six shared evidence outputs under this run root. It may write bounded evidence plumbing under `frontend/**` only if the authorized instrument itself cannot execute; it must stop on a product/runtime defect.
2. `V1` — one fresh evidence-only Agent 2 verifier starts after E1 returns. It is read-only over product and evidence and must not repair E1 outputs.
3. `M1` — WORKING_ITEMS validates fan-in, writes telemetry summary and manager return, and updates DEL-02-02 `_run_records`, `_STATUS.md`, and `MEMORY.md` only if the proof is accepted.

Edges: `E1 -> V1 -> M1 -> N2`. Overlapping writes are serialized.

## Gates and human decision points

- Stop and escalate on any need for product/runtime repair, provider credential/network expansion, signing/notarization/distribution, owner-machine LaunchAgent deployment, security/permission prompt, shared-surface write, or partial/failed instrument.
- A normal packager download of an already-declared dependency requires parent-routed approval before retry.
- No human decision is currently required to start N1. Any failed observation parks only its dependants and returns exact evidence.

## Checks

- Focused Workbench/Pipeline/navigator/replay tests.
- `npm run typecheck`, `npm run build`, `npm run desktop:pack`.
- Reachable isolated packaged `npm run harness:validate:premerge`.
- `npm run validate:release-quality` with no silent provider-backed skip.
- `npm run proof:secret-scan`.
- App corpus/receipt checks, repo-wide self-check and practitioner-harness pytest at manager fan-in.
- Source/package/helper identity, evidence hashes, secret hygiene, process/socket/temp-root cleanup, and allowed-write containment.
