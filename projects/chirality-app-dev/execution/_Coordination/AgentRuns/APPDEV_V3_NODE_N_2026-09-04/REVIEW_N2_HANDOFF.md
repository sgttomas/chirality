# Sealed review handoff — Node N / N2

Status: implementation freeze ready. This is a reviewer brief, not a review launch, verdict, or report.

## Subject

- Basis: `307addfc259b046aeb2ed07d47086cd5686c35b8`.
- Head: the committed freeze returned by N1.
- Scope: 100% of `git diff 307addfc259b046aeb2ed07d47086cd5686c35b8..<freeze-head>`.
- Item: only `DEL-09-06-V3-04`.
- Reviewer posture: fresh detached read-only worktree at the freeze SHA; no writes to product/test/evidence or this implementer worktree.

## Required review questions

1. Does each packaged request get a cryptographically strong fresh nonce, and is one byte-identical CSP presented to Next before render and attached to the response?
2. Is the CSP request header the only nonce source for Next, the root layout, and response enforcement, with no stale packaged fallback path?
3. Does packaged `script-src` exclude `'unsafe-inline'` and `'unsafe-eval'` while preserving other directives and the exact development posture?
4. Do `/`, `/chat`, `/pipeline`, and `/workbench` render dynamically under matching nonces, with consecutive/global uniqueness and zero unexpected/own-resource CSP violations?
5. Does the packaged proof fail closed for unsafe-inline, missing/duplicate route evidence, duplicate nonces, widened directives, and own-resource violations?
6. Are proof-only four-window behavior, normal one-window behavior, contract pins, A1 statement, evidence/manifests, scope/fences, and no-post-proof product mutation coherent?

## Mandatory reviewer reruns

- `npm run typecheck`.
- Focused Vitest over renderer-window-policy, packaged-security-proof, and contract-pins tests.
- Full `npx vitest run` with host permissions for loopback/Unix sockets.
- `npm run build`; confirm all four operator routes dynamic.
- `git diff --check` and exact change-scope validation.
- Verify the run and proof manifests with `shasum -a 256 -c`.
- Receipts validator (read-only), corpus status, APP-HOLD dispatch/integrity, SOW validation, F-APP-2 scan.
- Review the real packaged proof summary/log and the final Node H lifecycle machine lines/cleanup. A fresh package/proof rerun is encouraged if host-capable.

Verdict is PASS only with zero BLOCKER and zero MAJOR findings. Any product/test/CSS remediation requires a new implementer commit and a fresh reviewer. Do not edit this branch.
