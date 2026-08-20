# WORKING_ITEMS manager validation

- Package/deliverable: `PKG-09 / DEL-09-04` only.
- Accepted basis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2` on `codex/app-packaged-sdk-proof-20260820`.
- Authority: D-APP-97 C1; APP-HOLD dispatch/review/fan-in checks `ALLOW/PASS`, zero held, register match.
- Product result: the unsigned Desktop workflow invokes the unchanged scripted no-live-provider packaged SDK verifier against staged and read-only mounted app Resources; distinct summaries are fail-closed and retained/uploaded.
- Focused regression: `PASS`, 1 file / 5 tests.
- Workflow syntax: YAML parse `PASS`; all 6 `run:` blocks Bash syntax `PASS`.
- Normalized registered checks: `PASS` — frontend/Electron typecheck; full Vitest 148 files passed / 1 skipped, 1,144 tests passed / 4 skipped; repo self-check exit 0; APP-HOLD integrity `PASS`; practitioner pytest 350 passed.
- Governance/static: G4 corpus/schema `PASS` for 35 manifests; app receipt validator `PASS` and ledger unchanged; D-APP-38 authority corpus `MATCH`; `git diff --check` `PASS`.
- Build decision: no separate local build. Workflow/test/control bytes changed, not application/build source; the named macOS PR workflow owns the actual `desktop:dist`, staged app, read-only DMG, and upload proof. This proof remains required and is not inferred.
- Fresh review: `PASS`, all 13 frozen hashes matched, tracked-diff hash matched, 100% coverage, zero actionable findings, zero reviewer writes.
- Containment: exact sealed write targets only. The packaged verifier, dependencies/locks/pins, runtime/product source, provider/network policy, credentials, foreign loops, shared receipt/completion log, lifecycle, and Checking Approval SHA are unchanged.
- Existing self-check findings are unchanged cross-repository baseline findings outside this node; self-check exits 0 and no finding is caused or modified by this tranche.
- Candidate-range G4: schema/corpus preflight passes; the authoritative candidate-range command remains required after CHANGE creates the commit.

Closure verdict: `IMPLEMENTED_AND_REVIEWED_PRE_CI / EXTERNAL_PROOF_REQUIRED`.
