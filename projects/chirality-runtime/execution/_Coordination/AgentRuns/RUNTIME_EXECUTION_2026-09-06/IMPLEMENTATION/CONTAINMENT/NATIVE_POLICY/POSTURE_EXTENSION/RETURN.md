# Network posture and profile-shadow plumbing

Parent authorized this extension. Added commandNetworkPosture off/on, default off. The stable semantic digest includes posture and boolean network value. Both highest-precedence legacy network flag and named native profile network setting reflect the explicit posture. Selection is plumbing, not user consent; caller must authenticate and bind actual owner consent before execution. Compiler tests for both postures perform no network/provider operation.

Returned expectedPermissions is the exact selected profile object: filesystem path map and network.enabled. Per-key CLI overrides can merge with project configuration; they are not asserted to replace the complete table. The actor must compare actual effective selected permissions exactly, rejecting extra keys/grants/presets, before each turn. No full-table replacement behavior is claimed without exact-loader evidence. The parent/actor consumer received this obligation explicitly.

launchArguments now supplies the exact app-server subcommand. No vendor execution occurred. Unsupported glob rules remain rejected; literal-path compiler coverage is not claimed to complete the accepted full protected-rule corpus. includePlatformDefaults:false remains intended semantics requiring actual native read-policy proof, not an enforcement fact inferred from the digest.

Native compiler test passed, including stable off digest and distinct on digest, matching config and expected policy network values. Original seals remain unchanged as historical records.
