# Standalone versus embedded helper whole-tree comparison

Status: `PASS_WITH_ADVISORY`

The still-available ignored derivatives were compared after product rollback:

- standalone: `frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app`
- embedded: `frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app`

For each root, all descendants were sorted by POSIX relative path and serialized as tab-separated tuples:

- directory: `relative-path`, `D`, four-digit POSIX mode;
- regular file: `relative-path`, `F`, four-digit POSIX mode, byte size, SHA-256;
- symbolic link: `relative-path`, `L`, four-digit POSIX mode, exact link target.

A terminal newline was added to the canonical serialization before hashing.

| Measure | Standalone | Embedded |
|---|---:|---:|
| Total descendants | 812 | 812 |
| Regular files | 446 | 446 |
| Directories | 352 | 352 |
| Symbolic links | 14 | 14 |
| Canonical serialization SHA-256 | `3009a81765d3fd923b6b37d7578367027432b4b1c341bb0170bc247722ef75b3` | `3009a81765d3fd923b6b37d7578367027432b4b1c341bb0170bc247722ef75b3` |
| Exact tuple equality | PASS | PASS |

This binds file content, modes, sizes, relative paths, and link targets for the two package trees. It does not bind extended attributes, directory timestamps, or code-signing state beyond the bytes present in regular files.

Advisory: these are ignored generated derivatives made from the frozen R2 candidate. The live product source was rolled back, so the derivatives are source-misaligned with the current worktree and are not authoritative product state, acceptance evidence, or a commit candidate.
