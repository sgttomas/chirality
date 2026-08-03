# Validation Lane

No implementation is validated by this planning package. This matrix is the
required evidence contract for a later ruled tranche.

| Layer | Common evidence | Standalone evidence | Domain-target evidence |
|---|---|---|---|
| Source/boundary | target manifest/schema; import/dependency allowlists; no generic-runtime ownership inversion; secret scan | no domain-only imports/resources or gates | only ruled domain adapters/resources; no solver/professional act |
| Unit/logic | shared Woven, projection, route, runtime-client, permission and mapping tests | standalone default/config tests | typed-agent/info/workflow/gate mapping tests |
| Component/render | D-APP-36 controls/states/disabled-active/focus semantics | standalone copy/navigation/resources | domain copy, typed agents, structured views, workflow and decision gates |
| Browser/visual | shared high-risk layout/viewport/overlap/interaction cases | standalone wide/narrow and compatibility routes | domain wide/narrow, data density, gates, empty/stale/conflict states |
| Accessibility | keyboard, focus order, reduced motion, names/status/errors, contrast | standalone target audit | domain target audit |
| Build | clean typecheck/test/build; target-boundary validator | deterministic standalone build | deterministic domain build |
| Package | shared dependency/instruction-root/security validators | exact standalone identity/resources; launch smoke | exact domain identity/resources; launch smoke; no opposite-target content |
| Runtime client | same accepted Root contract; API/SSE/UIEvent compatibility; terminal/reconnect/replay | standalone connect/turn/interrupt/resume evidence | domain connect/typed-agent/workflow/gate evidence |
| Sessions/data | migration and canonical-session compatibility | standalone data-path behavior | coexistence/isolation with standalone explicitly proved |
| Release quality | registered checks and common evidence schema | target-specific artifact row | target-specific artifact row |

Rules:

- common evidence may prove identical shared bytes/behavior only when the
  target build graph demonstrates that identity;
- one target's screenshot, package, launch, runtime, or acceptance evidence
  cannot prove the other target;
- blocked generic-runtime interfaces remain failed/not-run, never silently
  waived;
- D-APP-88 blocked graceful-stop evidence cannot be promoted to PASS;
- D-APP-89 direct-import migration may be a source baseline only after its Git
  gate lands and a fresh zero-consumer census passes;
- all generated evidence is derivative and cites the accepted source snapshot.
