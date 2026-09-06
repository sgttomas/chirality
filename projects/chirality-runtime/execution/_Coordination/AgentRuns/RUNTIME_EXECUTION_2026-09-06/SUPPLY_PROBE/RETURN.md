# Exact supply offline diagnostic

OpenAI GPT-6 ephemeral Agent 2; serving model ID unavailable; role not mechanically enforced, instruction-asserted. No delegation. Diagnostic evidence only, not release conformance or a hold disposition.

## Result

Exact accepted original App Server 0.149.0 executed successfully. The official OpenAI release tar.gz and extracted original match both accepted digests and sizes in IDENTITY.json; post-execution original remains SHA-256 `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`. No signing transform was performed. Only this packaging was downloaded; zstd tooling is absent, so the smallest usable installed-decompressor packaging was selected. Source URL is `https://github.com/openai/codex/releases/download/rust-v0.149.0/codex-app-server-aarch64-apple-darwin.tar.gz`; licensing remains the accepted manifest Apache-2.0 plus notice inventory; no redistribution occurs.

Observed exact-pin methods: initialize, initialized notification, config/read, configRequirements/read, experimentalFeature/list. All four requested IDs responded under interactive stdio. Version reports 0.149.0. Configuration readback confirms plugins=false, approval_policy=never, workspace network=false, web_search=disabled, analytics/feedback=false. Config requirements are null. No model/account request, login, turn, thread creation, registry or host service modification occurred. Feature response is one page, not a complete feature/method inventory. Schema/types remain unavailable on accepted evidence; no guessed exhaustive API claim.

## Containment and observations

Used an empty disposable HOME/CODEX_HOME, minimal environment (no inherited credentials), disposable working directory and macOS sandbox denying all network, all user-home reads, Keychain mach lookup and writes outside the disposable supply tree. Preflight records denied user-home access and denied out-of-tree write; loopback connection failed. No completed external connection is possible under network* deny; no packet-level attempted-egress enumeration was performed.

The default outer sandbox rejected sandbox_apply, before artifact execution. An initial preflight predicate incorrectly admitted that install error; the version launch also failed before artifact execution. Predicate corrected to reject sandbox_apply and require all three probe outputs, then an approved tool escalation installed the same restrictive inner profile successfully. The preflight and final diagnostic code are preserved. Initial nested-context codesign returned invalid signature; clean minimal-environment codesign subsequently returned 0 on the unchanged exact bytes. This context difference does not dispose the accepted R13 G5 vendor-signature finding. Initial observations are recorded here from tool output; final machine records are preserved.

The initial piped protocol trial closed stdin too soon: only initialize responded. Interactive sequential trial preserved in interactive.json waits for each reply and completes all admitted read-only requests. Production transport must correlate replies while keeping stdin open; newline JSON protocol has no outer jsonrpc member in these observed messages.

## Handoff

No owner intervention is required to reproduce these bounded offline methods. This does not prove account policy, real model execution, App client conformance, runtime supervisor integration, installation/signing, activation or release. Parent can use the exact raw protocol responses to test its adapter but must not label these evidence limbs complete. R13 explicitly says stop if macOS refuses execution; no ad hoc copy was needed. Teardown removes downloaded archive, executable and disposable HOME/work/tmp; evidence only is committed.
