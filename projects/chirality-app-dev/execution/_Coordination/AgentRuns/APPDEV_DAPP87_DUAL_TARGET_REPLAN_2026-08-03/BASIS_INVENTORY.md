# Basis Inventory and Frozen Planning Facts

## Adopted facts

- Two targets are required: standalone Chirality Desktop and a per-domain
  control plane.
- Domain applications are the primary delivery vehicle for agents; domain-first
  sequencing is required.
- Woven Dialogue is the accepted primary collaboration surface. Work/Agents is
  an evidence-conditioned projection, replay is read-only, and existing route,
  query, alias, matrix, accessibility, and compatibility obligations persist.
- Root owns generic runtime semantics and operational state. App owns client
  integration, UI/packaging participation, project policy/human gates, and
  affected-client conformance evidence.
- Accepted decomposition topology remains 10 packages / 51 deliverables / 78
  SOW rows / 10 objectives. Planning may propose amendments but not create
  topology.

## Current topology observations

- `frontend/` is one npm workspace with one Next application, one Electron
  main entry, one `appId` (`com.chirality.app`), and one product name
  (`Chirality`). It already uses internal workspaces/packages but does not have
  two product-shell packages or two packaging manifests.
- Shared surfaces are physically composed under `src/components/`, especially
  `woven-dialogue/`, `shell/`, `workbench/`, and `pipeline/`; existing routes
  `/`, `/chat`, `/workbench`, and `/pipeline` share the application.
- Domain support is a closed, code-defined profile registry for
  `open_pipe_stress` and `pec`; it is not a product skin/configuration system.
- D-APP-89 migrated ordinary App consumers to Root runtime-contract imports,
  while preserving the deprecated facade as rollback. That migration is a
  validated candidate awaiting ordinary Git fan-in and is not generic-contract
  selection.
- D-APP-88 R2 proved a separate Electron helper target can be packaged, but
  its post-GUI first-signal graceful-stop evidence failed. All product bytes
  were rolled back. It cannot be treated as accepted target packaging.

## Existing deliverable families implicated for later amendment analysis

- Product/UI: `DEL-01-03`, `DEL-02-01` through `DEL-02-05`, `DEL-05-04`,
  `DEL-08-02`, `DEL-08-03`, `DEL-08-05`.
- Runtime affected-client: `DEL-03-01` through `DEL-03-04`, `DEL-04-01`,
  `DEL-04-02`, `DEL-04-05`, `DEL-05-01` through `DEL-05-05`, `DEL-06-01`,
  `DEL-06-02`, `DEL-08-03`, `DEL-08-04`.
- Packaging/validation: `DEL-09-01` through `DEL-09-06`.
- Domain boundary: `DEL-10-01` through `DEL-10-05`, with current-release
  domain operation execution still fenced absent later authority.

This is an impact inventory, not an amendment. The final work-order lane must
separate direct candidate amendments from cross-reference or no-change rows.

## Current Remaining anchors

- `DEL-02-01`, `DEL-02-02`, and `DEL-08-02` still owe packaged Desktop smoke
  evidence for Woven/Workbench/Pipeline/guarded selection surfaces.
- `DEL-05-04` still owes real-daemon transcript rendering and same-session
  Desktop/CLI replay evidence.
- `DEL-03-01` retains the post-landing facade retirement gate.
- `DEL-09-04` retains packaging/release, helper identity, premerge, deployment,
  instruction-root, and login-time residuals; D-APP-88 remains blocked.
- `DEL-09-05` and `DEL-09-06` retain release-preparation evidence residuals.
- `DEL-10-01` retains a governed-next-capability gate and PEC client work.

## Root-blocked lanes

The current Root response leaves `TM-ROOT-105`, `TM-ROOT-107`, and
`TM-ROOT-109` open/deferred behind the Piping response and Root instruments.
Generic runtime, sandbox, identity, version, resume, and Bash are therefore
`BLOCKED_BY_ROOT`. The 2026-08-03 D-APP-88 notice adds a graceful-stop
investigation request but does not prove a Root cause or alter these gates.

## Evidence-class discipline

PRD, decomposition, ruled SCA handoffs, and rulings are accepted inputs.
Source and Remaining files are live state. D-APP-88/89 run artifacts and this
entire re-plan are derivative evidence. Coordination notices are not authority.
