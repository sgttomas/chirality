# Build review checkpoint

Reviewed pinned release workflow, Rust toolchain declaration, Cargo target configuration, V8 setup action and resolver, local code-mode-protocol/skills build scripts, and fetched V8/native SQLite/AWS-LC build paths. Code-mode protocol uses vendored protoc; V8 uses the exact predownloaded archive and binding override. No user-account or signing-key requirement was found in these reviewed build paths. This is bounded build preparation review, not a complete dependency security audit.

Cargo locked fetching checks immutable dependency identities; an independent archive checksum pass verified1028 downloaded crates. All1218 external lock records remain unchanged;139 workspace-local version fields needed normalization from0.0.0 to0.149.0 because the release tag updated Cargo.toml but not Cargo.lock. Initial failed locked attempts are retained. Baseline and patched source share that explicit normalization.

Baseline currently builds offline under a write-containment profile allowing only supplier scratch and /dev/null, maximum4Cargo jobs, with CARGO_HOME/RUSTUP_HOME/target/tmp/clang/XDG caches isolated. Existing HOME is preserved and provider credential environment is absent. No unsupported interpretation of this build profile as the production native action profile is made.
