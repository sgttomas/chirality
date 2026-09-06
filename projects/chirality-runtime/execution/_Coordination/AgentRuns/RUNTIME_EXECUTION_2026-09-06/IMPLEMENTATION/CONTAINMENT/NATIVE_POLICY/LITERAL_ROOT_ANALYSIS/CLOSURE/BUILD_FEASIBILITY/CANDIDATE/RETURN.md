# Supplier candidate return

Bounded preparation complete. Baseline build PASS (1059.69 s); patched build PASS (717.74 s); both version/signature inspections PASS. Four selected protected-glob source tests PASS (147.73 s including compilation). Direct exact-source policy comparison PASS: baseline SIGABRT before shell startup; patched shell starts, allowed project write succeeds, sibling read/write denied and loopback connectx denied by the OS.

Patched App Server: `/private/tmp/runtime-execution-20260906/supplier-candidate/builds/patched-artifacts/codex-app-server`, SHA256 `b1ba73f40c3a40ebc161ea75dd68c24e90589e6e74e651065167636ad56876b2`.

Baseline App Server: `/private/tmp/runtime-execution-20260906/supplier-candidate/builds/baseline-artifacts/codex-app-server`, SHA256 `a3ac0445f8fab23c62a97f3c9c8e420f094b67927948c1cfa69390b6e0742f93`.

Each artifact directory retains `codex-code-mode-host`, SHA256 `1132f2d954e272fafc77d837e71ddd0918c6ce6487f961e30171413e9011eb81`, and its own MANIFEST.json. Both local builds have linker-created ad-hoc signatures, no vendor TeamIdentifier. The accepted executable was rehashed unchanged. No account, inference, signing key, accepted pin or accepted installation was used or changed.

Source commit `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0`; Rust1.95.0; verified V8 150.4.0. Both variants share explicit 139-workspace-version lock normalization; 1,218 external package records unchanged; 1,028 crate checksums verified. One behavioral difference is the recorded literal-root directory-read policy rule. Binaries, source and cache remain only in declared scratch; evidence and recipes are durable here. Retain scratch until parent explicitly closes rerun needs and directs cleanup.

## Recommendation boundary

The parent has reported a paired actual-shell result: candidate passes eight checks covering primary/native-child project writes, foreign/broker read denials and second-process resume; same-policy baseline has four shell exits134. Network posture conformance is provisional/inconclusive: parent reports the ON and ASK-ALLOW controls show the same curl failure as OFF, with no listener hits or approvals. A working positive network control is still required; the actual App Server network boundary is not established by these runs. These parent-owned results were not independently executed by this specialist; parent must attach its exact final evidence and assess remaining G-SBX limbs.

Based on the completed local differential and those reported actual results, recommend completing the remaining actual conformance and then presenting acceptance of this distinct local candidate as the actionable option. Acceptance must explicitly address artifact provenance, local ad-hoc signing, support/maintenance and the new supply pin. Do not select it through implementation. Retaining the original pin keeps affected execution unavailable; seeking an upstream fix avoids accepting this local supplier variant but requires a new released artifact, pin review and full rerun. No issue publication or source acceptance is implied.

No claim of full G-SBX, production readiness, reproducible vendor binary identity, complete dependency audit, account-backed model behavior or owner acceptance follows from this specialist package. Glob helper tests exercise lowering; they do not alone establish every TOML classification or native action path.

Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent 2, role instruction-asserted and not mechanically enforced. Agent 0 role is not mechanically enforced.
