# Packaged security precedence closure — 2026-08-20

Verdict: **PASS** for the selected D-APP-97 packaged-security residual.

The fresh unsigned arm64 app and DMG were built from source revision
`6710ee6354debc201f6a454e2802897026cd4b38` plus the four accepted N1/N2
product identities recorded in `summary.json`. The packaged subject identity
is `1623b2971bcef5fc6a2ae80ce0baa747a6746e28a2b821cd1e6bf125574b4ce2`.

Focused and full tests, typecheck, build, practitioner harness, root
self-check, APP-HOLD, packaged dependency boundary, instruction-root
integrity, secret scan, and the host packaged-security proof passed. The
packaged main preserves UI safeStorage precedence, then
`ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`, and carries only the
non-secret `ui | env | none` source vocabulary. The live packaged proof
exercised encrypted safeStorage store/status/remove, provider isolation,
blocked renderer diagnostics/probes, five descendant TCP snapshots with zero
non-allowlisted outbound, confirmed GUI/daemon code-0 shutdown and stream
closure, and cleanup with zero retained credential or metadata leaks.

Bulk output remains review-only at
`/tmp/chirality-precedence-closure.pXvs6Z`. Per D-APP-99, the repository keeps
only this compact account and `summary.json`; the app, DMG, raw logs, TCP
captures, and full scan/check transcripts are not committed.

This closes only the DEL-09-06 D-APP-97 packaged-security Remaining item and
the coordinated DEL-09-04 REQ-009 / R4-P49 packaged-network Remaining item.
It does not change lifecycle, Checking Approval SHAs, dependencies,
RunAtLoad, owner-machine deployment, signing, notarization, distribution,
publication, or release readiness.
