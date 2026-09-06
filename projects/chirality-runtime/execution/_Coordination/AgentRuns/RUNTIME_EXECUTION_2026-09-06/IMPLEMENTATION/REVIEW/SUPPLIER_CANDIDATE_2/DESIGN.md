# Candidate2 design for independent review

Recommend the minimal initialization correction, not a new private requirements loader. The exact source already compiles the trusted named proxy and registers execution-scoped request attribution. Session initialization incorrectly gates both callback creation and proxy approval enablement on the presence of managed requirements, even when the effective named proxy is present. PROPOSED_NETWORK.patch changes only those two decisions in core/src/session/session.rs; retain candidate1 literal-root rule and shared139workspace-version lock normalization unchanged.

1. Create the existing weak-session callback whenever config.permissions.network exists (previously additionally required requirements_toml.network).
2. Pass callback presence as enable_network_approval_flow on the initial proxy start. A second gate exists at config/network_proxy_spec.rs135-155; changing callback creation alone would not work.

No new environment variable, CLI/public/model input, file path, requirements merge or source-of-authority layer is introduced. The existing host-owned sealed named profile and trusted actor policy readback remain the input authority. No managed flag stored in SessionServices is falsified. Existing requirements loading, MDM/cloud/system precedence, profile constraint merging and refresh rules remain untouched.

## Preserved enforcement, exact-source grounds

- network_proxy_spec.rs107-116 derives hard_deny_allowlist_misses from requirements.managed_allowed_domains_only;145 still refuses any decider when this is true. All managed constraints are still applied/validated at110-123. Tests237ff cover this behavior.
- network-proxy/src/network_policy.rs346-380 invokes a decider only for NotAllowed. Explicit denied domain and all other blocked reasons bypass callbacks and remain baseline denials. Add a unit test with an always-Allow decider proving explicit Denied never invokes it.
- tools/network_approval.rs623ff requires request attribution; missing/ambiguous owner and absent active turn reject.709-726 validates the actual permission profile and approval policy; Never rejects.793-832 rejects failed/aborted approval. Existing pending-owner/drop/disconnect tests preserve cancellation and fail-closed outcomes.
- Review authority remains session.request_approval, not this callback. No reviewer default or routing change is proposed; Runtime must continue highest-precedence user reviewer plus exact effective readback. Managed reviewer constraints retain their existing authority.
- Disabled/external profiles remain rejected by permission_profile_allows_network_approval_flow; unrestricted/default operation is not newly approved automatically. The changed case is a configured restricted named proxy without managed requirements, whose allowlist miss can now request existing governed approval. No client or no successful answer means no Allow decision.

## Refresh limitation

Existing live profile refresh preserves an existing proxy callback. If a proxy is removed and later recreated, source session/mod.rs1145 passes no callback and the old managed-requirements flag; that path stays fail-closed and may lack prompts. The Runtime policy is immutable within a worker and this candidate does not claim arbitrary live profile switching support. Independent reviewer should assess whether this limitation needs a separate bounded correction before reliance; it is not an authority bypass.

## Alternatives

A private additive requirements file would require a new trusted path channel, canonical/protected input validation, merge/precedence semantics and release plumbing. It is unnecessary to initialize the already-present attributed callback and risks authority confusion. Exposing the debug managed-config hook is rejected because it substitutes requirements; enabling debug assertions or domain preallow is outside the task. No file-loader alternative is selected.

## Checks before relying on candidate

Review the exact diff and constraint paths independently before applying. Build candidate2 frozen/offline with4jobs using pinned Rust/V8/dependencies; preserve separate candidate1/baseline bytes. Run source network_proxy_spec tests (requirements allow/deny/hard-deny), network_approval tests (Never, restricted profiles, ambiguity, cancellation, disconnect and pending owner), and network-proxy explicit-deny/not-allowed tests. Tests are source-level, not actual user UI proof. Parent then runs actual private/public primary/native ask allow/deny/cancel, missing/stale callbacks, reviewer readback, OFF/ON controls and candidate1 differential, under existing endpoint bounds. Candidate2 source/supply acceptance remains an owner act after concrete results.
