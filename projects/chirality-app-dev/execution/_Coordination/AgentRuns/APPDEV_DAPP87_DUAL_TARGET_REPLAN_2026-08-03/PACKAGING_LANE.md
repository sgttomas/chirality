# Packaging Lane

## Required artifact properties

Both architecture choices must be able to produce two locally distinguishable
unsigned macOS artifacts:

- standalone Chirality Desktop; and
- the first per-domain control-plane application.

Each artifact needs an explicit product name, bundle identifier, executable
identity, icon/resources, target profile, packaged Root-runtime/client
dependencies, instruction-root/resource posture, data/session compatibility
policy, and update/release-channel posture. None is selected here.

The current `frontend/package.json` has one `appId`, one `productName`, one
Electron main, and one package output. It therefore proves a single-artifact
baseline only. D-APP-88 R2 proves that a distinct Electron target can be built
and embedded, but its helper result was rolled back and blocked on graceful
stop; it neither supplies domain-product identity nor authorizes reuse.

## Configuration and resource boundary

A later selected form must ensure:

- target identity is fixed before packaging and cannot change at runtime;
- only an allowlisted target manifest/config reaches the renderer;
- domain resources are not bundled into standalone unless explicitly shared;
- standalone resources and generic product copy do not masquerade as the
  domain target;
- target-specific configuration cannot grant runtime/tool capability;
- both artifacts bind the same accepted generic runtime contract version only
  after Root authority exists;
- local data/session compatibility and migration are explicit if both
  artifacts can point at the same working root.

## Unsigned local validation matrix

| Check | Standalone | Domain target | Common proof allowed? |
|---|---:|---:|---|
| deterministic clean build | required | required | command/schema only |
| expected bundle/product/executable identity | required | required | no |
| icon/resource/config manifest | required | required | no |
| no opposite-target resources/config | required | required | no |
| dependency boundary | required | required | validator logic may be shared |
| instruction-root integrity | required | required | validator logic may be shared |
| launch/working-root smoke | required | required | no |
| runtime-client connectivity/reconnect | required | required | no |
| Woven/typed-agent/workflow/gate smoke | common + standalone | common + domain | shared common plus separate target proof |
| secret/network/redaction posture | required | required | shared checks plus target output proof |

Signing, notarization, publication, distribution, auto-update, and release
channel selection remain outside this run.

## Candidate deliverable effects

- Direct amendment candidates: `DEL-01-03`, `DEL-09-04`, and `DEL-09-05`.
- Conditional candidates: `DEL-04-05`, `DEL-05-01`, `DEL-09-01`,
  `DEL-09-02`, `DEL-09-03`, and `DEL-09-06`.
- D-APP-88 and the existing `DEL-09-04` helper residual remain separately
  blocked. A domain-artifact decision cannot close or bypass them.
