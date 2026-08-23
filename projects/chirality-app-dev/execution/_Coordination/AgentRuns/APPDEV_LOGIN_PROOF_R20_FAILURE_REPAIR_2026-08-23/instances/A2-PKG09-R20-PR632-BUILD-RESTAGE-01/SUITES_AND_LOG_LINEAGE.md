# Full-suite evidence and raw-log lineage

## Exact invocation counts and results

| Command | Environment | Count | Exit | Result |
|---|---|---:|---:|---|
| `npm test` | ordinary workspace sandbox | 1 | 1 | 22 failed / 1,260 passed / 4 skipped |
| `npm test` | permission limited to local Unix/loopback test sockets; external network forbidden | 1 | 0 | 1,282 passed / 4 skipped |

The ordinary diagnostic retained 21 established local TCP/Unix `listen EPERM` failures and one established synthetic-PID SIGKILL absence case. It remains diagnostic non-PASS. Neither class is upgraded to a product regression. The cure passed without a retry; the prior Pi/oMLX 200 ms timing case did not recur.

## Raw-log lineage

Raw logs were captured completely, then converted with deterministic `gzip -n` to keep binary evidence out of semantic candidate-whitespace checks. Decompression reproduces each exact preimage hash.

| Evidence | Raw bytes | Raw SHA-256 | `.gz` SHA-256 |
|---|---:|---|---|
| `desktop-pack.log.gz` | 15,854 | `5402cc5f5d24c1d33a6261d129f9ca3555df597babf483b9010facc1d04138e6` | `d0a8bacf1a4c198688f667005ecccb50fdfd20a3453cd3f6c6af3e593e51ed87` |
| `npm-test-sandbox.log.gz` | 10,845 | `67350a824fef5651ce7f88618986d4357e596adbd4d87ce8988159bd3caed980` | `e978046e542efee70f4c76cb86b0b3fa8b4bd76ef26e7547097ca01b0ab76ac8` |
| `npm-test-local-socket-cure.log.gz` | 486 | `21fe62023dd5b526357018d9a00ffd2da925c3eec61737fe2ba6b28d07bc62f9` | `301c54d02e95700d1171f12927072898df16551123c3730282787d76992d58a5` |

The 144-byte supply log remains plain text at SHA-256 `5af72fdf79d96a79f68b7d81b118f437d266c0b73e803ac6b8e567cba1ce20ae`. The Step-0 log remains plain text at SHA-256 `077c101ce108b221ad6df2582f14b575335c32bb23fbd664bb71b36ccb5bed81`.

## Hash preservation after both suites

Every hash frozen in `PRE_FULL_SUITE_FREEZE.md` was identical immediately after both full-suite invocations: shared pre-suite candidate files, source/package scripts, fixture test, generated main, main executable, packaged CLI, `app.asar`, instruction summary/manifest, HEAD, and frontend tree. Scoped frontend porcelain and b338-to-HEAD frontend diff remained empty; the Git index remained empty.

A coordination hold message arrived after the sole cure invocation had already started. The run was allowed to reach its terminal result to preserve the exact-once contract; it was not interrupted or retried.
