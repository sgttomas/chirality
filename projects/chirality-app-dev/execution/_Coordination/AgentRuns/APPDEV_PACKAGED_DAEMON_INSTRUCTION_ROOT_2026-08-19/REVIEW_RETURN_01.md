# Fresh code review return 01

- ChildInstanceID: `A2-DAPP100-REVIEW-01`
- TaskSkill: `software-code-review` v1
- Verdict: `FAIL`
- Scope: 100% of all five frozen product/test/proof files and complete base/new-file diffs; listed hashes matched before and after review.
- Read-only compliance: `PASS`; no file edited and no host proof run.

## Actionable findings

1. `P1` — proof commands wait indefinitely and cleanup can leave Electron children alive after SIGTERM timeout. Add command deadlines, track every child, escalate to SIGKILL, and confirm exit before cleanup.
2. `P1` — artifact freshness is not bound to the exact tested app; `--app` can select stale unrelated bytes and `--skip-pack` relies only on directory mtime. Bind proof to the exact pack output and a run marker or captured hashes.
3. `P1` — a failed rerun can leave an earlier canonical `latest/summary.json` PASS. Write pending evidence before execution and FAIL evidence for every error, atomically replacing the canonical summary.
4. `P2` — log restart offset uses `Buffer.byteLength()` but slices JavaScript strings. Use string length consistently or process buffers.

No separate defect was found in registry authorization/drift handling, Electron bundling, or production source wiring. Full deterministic and host checks remain unproven.
