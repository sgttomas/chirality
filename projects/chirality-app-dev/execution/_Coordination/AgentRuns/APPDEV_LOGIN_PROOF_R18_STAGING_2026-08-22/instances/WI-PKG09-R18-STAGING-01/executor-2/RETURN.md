# Executor-2 return — A2-PKG09-R18-WP02-EXECUTE-02

## Result

`FAILED — SOLE SHASUMS REQUEST RETURNED HTTP 302; FAIL-CLOSED BEFORE IMPLEMENTATION`

- Parent: `WI-PKG09-R18-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r18-staging`
- accepted request-time basis: `HEAD == origin/main ==
  166efa82748133e90674be62304b81f8a0a8c1b4`
- proof status: not run; DEL-09-04 remains `IN_PROGRESS` and unproved
- derivative status: terminal request evidence only; no supply freeze, package,
  R18, status amendment, or proof

## Request gate

The fresh executor evidence directory was initialized before the request. The
sole network request used `/usr/bin/curl` against exactly:

```text
/usr/bin/curl --proto '=https' --tlsv1.2 --max-redirs 0 --fail-with-body --silent --show-error --connect-timeout 20 --max-time 60 --dump-header <executor-2>/shasums256.response-headers.txt --output <executor-2>/SHASUMS256.txt --write-out 'http_code=%{http_code}\nurl_effective=%{url_effective}\nnum_redirects=%{num_redirects}\nsize_download=%{size_download}\n' https://github.com/electron/electron/releases/download/v43.2.0/SHASUMS256.txt
```

Curl exited `0` and reported `http_code=302`, the exact requested URL as
`url_effective`, `num_redirects=0`, and `size_download=0`. The response body is
zero bytes. The redirect was not followed. Its host was
`release-assets.githubusercontent.com`, which is outside the one-URL/one-host
authority. Therefore the request did not provide the required plausible
SHASUMS text or the required verbatim arm64 line, and the brief requires this
node to stop.

One earlier shell invocation failed locally before curl could start because zsh
expanded an unquoted `=https` token; it produced `https not found`, made zero
requests, and created no response evidence. The corrected invocation above made
the first and only network request. Network request count is exactly `1`; no
redirect or second request occurred.

The complete raw response headers were observed transiently. Because the
Location header contained a time-limited signed query/JWT, repository evidence
retains only a claim-calibrated sanitized header record with HTTP status,
content length, origin server, and redirect host. The signed query is not
retained or reproduced here.

## Terminal disposition

Per the sealed redirect gate, execution stopped before:

- owner-staged zip inspection or hashing;
- nested `@electron/get` source inspection or citation;
- source, package-manifest, lockfile, test, R18, or `_STATUS.md` edits;
- verifier, syntax, typecheck, focused, full-frontend, APP-HOLD, practitioner,
  self-check, package consistency, instruction-root, whitespace, or candidate
  validation;
- any `npm run desktop:pack` attempt.

This fresh executor made `1` network request and `0` package builds. The prior
executor's cache-miss attempt and evidence remain unchanged. No review candidate
exists. A rerun would require new owner authority because the only permitted
request has been consumed and the specified GitHub URL redirects to another
host.

During terminal evidence closeout, the shared local remote-tracking reference
advanced: `HEAD` remains the accepted basis
`166efa82748133e90674be62304b81f8a0a8c1b4`, while `origin/main` now resolves to
`abf3c1bf5996cd9333ad706df14e62df32fbbf0f`. This executor did not fetch or
sync and does not infer who advanced the shared reference. Per the standing
direction, no non-rewriting sync occurred; any sync requires owner
authorization. The index and tracked worktree remain empty. The only porcelain
entries are the inherited untracked R18 run root, including the four new
`executor-2/` files listed below.

## Fences and handoff

No artifact download, second host/request, source implementation, dependency or
provider expansion, proof-package adoption, R19 procedure, GUI, prepare,
capture, logout/login, bootstrap, kickstart, operator/default job/plist/launcher
query or action, signing, notarization, deployment, distribution,
release-readiness/proof claim, Receipt 189, staging, commit, push, PR, merge, or
delegation occurred. DEL-09-04 remains `IN_PROGRESS` and unproved. The terminal
request evidence is derivative and authorizes nothing.

Frozen executor-2 evidence paths are:

1. `executor-2/RETURN.md`
2. `executor-2/SHASUMS256.txt` (zero-byte response body)
3. `executor-2/shasums256.response-headers.txt` (sanitized)
4. `executor-2/request-metadata.txt`
