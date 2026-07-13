# CHANGE-A2-G Sealed Launch Brief — v1

Role: `CHANGE` Agent 1. Integrate the accepted W-A2 preintegration snapshot for
the exact 16 ordinary App members using its 80-row replacement manifest and
inverse rollback. Basis is synchronized `main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa`;
accepted snapshot is `snapshots/W_A2/preintegration/ACCEPTANCE.md` with manifest
SHA-256 `0dbf05dec12668517f3b34097d15afdb5bff3a9bfa9f73569f614883238b000d`.

Human blanket approval for PR merging is active for this goal. Follow
`AGENT_CHANGE.md` gates: reproduce the accepted snapshot, create a `codex/`
branch, integrate only the exact 16 five-path replacements while preserving
all `_STATUS.md` bytes/lifecycle, run required App checks, commit, push, open a
ready PR, monitor required CI, merge after success, synchronize main, run
postmerge checks, and write immutable integration/postmerge evidence plus
terminal return/handoff. Do not touch H1/H2, any other project path, or
`.claude-worktrees/`. Stop and report on any drift, conflict, failed required
check, or mismatch.
