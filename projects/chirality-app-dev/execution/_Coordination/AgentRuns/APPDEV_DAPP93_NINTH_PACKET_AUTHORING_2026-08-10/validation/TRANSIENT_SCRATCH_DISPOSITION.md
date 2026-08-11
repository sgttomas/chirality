# Transient probe-scratch disposition

Status: `RECORDED THEN REMOVED — NOT AN AUTHOR OUTPUT OR PACKET BYTE`

N1's exact F09 probe used the frozen run-local `scratch/probe-home` and
`scratch/probe-tmp`. Neutral `xcrun lldb --version` created 16 Python bytecode
cache files totaling 170,658 bytes plus one 1,441-byte `xcrun_db`. These were
contained probe side effects, not one of the 17 declared child outputs, and
were never read as authority or included in the candidate packet.

Before deterministic cleanup, the manager recorded the following identities:

| Relative leaf | SHA-256 |
|---|---|
| `_bootlocale.cpython-39.pyc` | `33dc113df75d53b388b877a180c1cafdf772ebf74a96863459106f0f9e49d6ce` |
| `_collections_abc.cpython-39.pyc` | `1fff8ec711cbd0e9d7c25bef92ff8308138330bebfa770fcadfd0e4b6b88caf9` |
| `_sitebuiltins.cpython-39.pyc` | `958f7dc78cf99170e1286845249a1548e50977283556035d9e8ed0be9c698c4f` |
| `abc.cpython-39.pyc` | `7599449f4670a13cf4bd8eed0fdb0dc2cfbb1035771e94d99ecfbef86b6e6d9e` |
| `codecs.cpython-39.pyc` | `92db5e32b733347cdfd42ed8d4a5629caf107a6190d76d88ded25c159d38086b` |
| `encodings/__init__.cpython-39.pyc` | `56602a1713880802114141dc4ff731a99a078b42ea65751dc7d27c1527a686f5` |
| `encodings/aliases.cpython-39.pyc` | `07951d683c18547516b703d33b36507bf5cb2fead8a161463cfb54c20b7bec5d` |
| `encodings/cp437.cpython-39.pyc` | `204dda1afa7a91e5c31fb1ec8435c122a60767573b74faa79e4fd0e916a5b98e` |
| `encodings/latin_1.cpython-39.pyc` | `a2f4c72f8029b576c0ad6db027fbe4355a563062787bf41dba24117688659e28` |
| `encodings/utf_8.cpython-39.pyc` | `ad7ed56037cdf85a4460d06f81ce1674cc42ec4eba6f272a12148da7c8fa1fd1` |
| `genericpath.cpython-39.pyc` | `f3cb7470259d4332464307aaad6f30965802669dbc9d5902b93657489473b9c3` |
| `io.cpython-39.pyc` | `8a4ab6c419a7f5de4528dcfa29212e88bbd99c76fecce604d4b5b6740aac77ef` |
| `os.cpython-39.pyc` | `e4a38564fa7667697b1c8e7f5753e4233ba274ad1ffecfb339e01815af1939ee` |
| `posixpath.cpython-39.pyc` | `bc8ecdd0fcd404df182bbb44c50e6726e93f5e2a1d95db875dd7e59617fa4647` |
| `site.cpython-39.pyc` | `72fdf0aa3462fd69c696bba38ea65722576d51141772a00af418961084a83aba` |
| `stat.cpython-39.pyc` | `1ca5729378c465f3e426d5320a96f6cac37c8c0307f221f6077800f9e7881ffe` |
| `probe-tmp/xcrun_db` | `31c8720d2d0f5bf0fd22d15bcf369000c3abc83c8d3f066b0f4047d9dd4636e1` |

The manager then removed exactly the two generated directories
`scratch/probe-home/` and `scratch/probe-tmp/`. No declared N1 output, packet
byte, source byte, historical root, or non-run-root path was altered.
