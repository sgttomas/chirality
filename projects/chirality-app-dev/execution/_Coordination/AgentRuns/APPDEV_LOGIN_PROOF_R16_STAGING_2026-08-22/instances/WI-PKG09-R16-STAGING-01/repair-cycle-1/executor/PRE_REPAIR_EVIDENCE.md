# Pre-repair byte evidence

- Basis HEAD: `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Index: empty
- Subject: exact original 35-path R16 tranche

## Six surplus terminal LF findings

Each listed file ended in byte sequence `0a 0a`; the authorized transition is
deletion of exactly the final `0a`, leaving one terminal LF.

| Run-root-relative path | Old bytes | Old SHA-256 |
|---|---:|---|
| `CHAT_TRANSCRIPTION.md` | 3089 | `e5ce0dc4792f99ff243add85a74b28bcbf6a912f84e349091c3746f04a16c4a1` |
| `ORCHESTRATION_PLAN.md` | 3332 | `e4999b0f78d3269891c1a55574907fb539b16ae60341700eedd1f9e53cc48649` |
| `WORK_GRAPH.json` | 1226 | `cbc6f8afea46e5bf90c471611e54f1f2ecc1647f8fff7d20012ba3a895a6242c` |
| `instances/WI-PKG09-R16-STAGING-01/ACTIVATION_AND_WORK_GRAPH.md` | 623 | `8a4bbb69dbf03fec9b28ca062e75db14a8b144743bee4475afdad543a7ff3108` |
| `instances/WI-PKG09-R16-STAGING-01/briefs/A2-PKG09-R16-EXECUTE-01.md` | 8513 | `2cb9104e99eec59745c2a71a947526e4d733e829a011717ed6d39bf0140010a9` |
| `instances/WI-PKG09-R16-STAGING-01/briefs/AMENDMENT_02_POST_COMMIT_STEP0_PORTABILITY.md` | 1781 | `7456f776f7e803ee92f53946507458a3d532962bf2b2a544424a9d481905439e` |

## Six log-line trailing-whitespace findings

For each of lines 16, 17, and 18 in both logs, the pre-repair line ended in
`29 20 0d 0a` (`)`, space, carriage return, LF). The authorized transition is
exactly `29 0a`, preserving the visible text and line boundary while deleting
the trailing space and carriage return.

| Run-root-relative path | Old bytes | Old SHA-256 |
|---|---:|---|
| `instances/WI-PKG09-R16-STAGING-01/executor/desktop-pack.log` | 5201 | `900a08787bdeaa946a85997f12824dcc73af0ad5cb18febad483cbcf6da8bf16` |
| `instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/desktop-pack.log` | 15962 | `e1f3bc133fb1a993611acf7952fcabd89bb5bdab09ae5e58519c5b1b01b262e9` |

Historical raw identity indexes retain their then-current values. Current
identity claims are refreshed after the direct byte repair.
