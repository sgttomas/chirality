# Required content — OWNER_RUNBOOK.md

- Title and immutable packet-use warning.
- State no authority until exact frozen-packet SHA approval.
- Step 0 invokes `scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh` from the packet directory, records binary hashes, expected exit codes/output shapes, and stops on mismatch.
- Operative section is owner-run LLDB causal tracing of helper SIGTERM survival only; it may reference `/usr/bin/lldb`, `/bin/ps`, LLDB commands, and the exact owner-supplied target PID at run time.
- Never build, install, overlay, sign, notarize, publish, mutate source, or alter product/runtime configuration.
- Explicit stop rules: Step 0 mismatch; target identity mismatch; attach failure; unexpected process topology; command/output variance; missing evidence; cleanup failure.
- Evidence capture points map to `EVIDENCE_CAPTURE.md` and `scripts/CAPTURE_TRACE_EVIDENCE.zsh`.
- Include cleanup/detach and hash capture; no assertion of causal conclusion in advance.
- Use descriptive fresh labels only; none may match the historical-ID pattern set.
