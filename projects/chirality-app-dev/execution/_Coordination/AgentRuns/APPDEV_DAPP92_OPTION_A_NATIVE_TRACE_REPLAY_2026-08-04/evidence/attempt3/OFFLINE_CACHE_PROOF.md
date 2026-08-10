# Attempt-3 offline-cache proof

Status: `TERMINAL ATTEMPT-3 EVIDENCE`

## Exact failure

Corrected C198 was invoked byte-identically three times during Attempt 3. Each
invocation reached Electron `43.2.0` Darwin-arm64 packaging and stopped before
package construction on the same bytes frozen in `C198_FAILURE_BYTES.txt`:
`getaddrinfo ENOTFOUND github.com`. No network escalation or successful network
effect occurred.

## Local archive identity

The already-local public archive is:

```text
/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip
```

SHA-256:
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
C202/C203 copied it into the isolated `electron` cache namespace and reproduced
that hash, but electron-builder does not use that namespace for this call.

## v1.11 namespace error

Amendment v1.11 used
`eee4c0a11146d71f2a23f97ebe56f88f3317ed947626839ecfe7a163d32c09b8`
under the isolated `electron-builder` cache. After the terminal failure, the
package's own `@electron/get` `Cache.getCacheDirectory()` method was invoked on
the exact artifact URL and independently returned:

```text
9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621
```

It returns the same directory for the release's `SHASUMS256.txt`. Therefore
`eee4…` was not the package's cache-key output; `9c4e…` is the exact proven
namespace and also matches the existing local archive directory.

## Effects and cleanup

- C175: PASS, actual four test files / 30 tests.
- C176: PASS.
- C177: PASS.
- C198: FAIL before package construction on all three Attempt-3 invocations.
- C179-C184: NOT RUN.
- helper/GUI launch: NONE.
- numeric helper/GUI PID: NONE.
- C196/C197: NOT RUN; owner approval remains unused.
- first SIGTERM, polls, replay, credentials, release, Git: NONE.
- C185-C195: PASS; all eight baseline/lockfile hashes reproduced and frontend
  Git status was empty.
- C199-C200: PASS; fixed runtime root removed and proved absent.

No package identity, topology, runtime fitness, or causal result is inferred.
