# Required content — OWNER_ENVIRONMENT_PREFLIGHT.zsh

- Zsh script with `set -eu`, no network, no writes outside an owner-supplied evidence directory.
- Require exactly one evidence-directory argument and refuse `/`, `$HOME`, or an absent directory.
- Restricted `PATH=/usr/bin:/bin`.
- Verify SHA-256 of `/bin/zsh`, `/usr/bin/lldb`, `/bin/ps`, and `/usr/bin/shasum` against packet-pinned values.
- Record actual hashes and tool version/output shape in Step 0 evidence.
- Neutral LLDB probe is `/usr/bin/lldb --version`, expected exit 0 and first line beginning `lldb-`.
- Owner-only process probe is `/bin/ps -p $$ -o pid=`, expected exit 0 and numeric output. It is OWNER_PREFLIGHT because manager sandbox execution is denied while readable binary identity is pinned and process observation is necessary to identify the trace target.
- Never attach, signal, kill, launch, build, install, or mutate runtime/product/system state.
- Use descriptive fresh labels only.
