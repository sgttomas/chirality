# RV113: REDACTION_01 to the SR-PY review's addendum 01 (before its first commit)

TASK (Type 2), RV113, for ROOT (HELP_HUMAN, Agent 0), the return path. 2026-10-08 UTC.

## What changed, and why

- **The problem.** `addendum_01/harness/sanitize_py.py`, my record sanitizer, spelled the machine's names in split pieces, in its two screen lists (`BAD` and `LOWER_BAD`).
- **The rule.** The owner's direction (2026-10-08) is that the machine's names never reach the public repository, in any form. RR "RV117 passes #1111; …", ruling 4, requires a record that carries a host name to be redacted before its first commit. This addendum had not been committed yet, so I redacted it before its first commit, as the coordinator asked.
- **The change.** The script now carries no machine name and no fragment of one.
  - It reads the names at run time: from `hostname`, `scutil --get LocalHostName` and `scutil --get ComputerName`, and from the private names file outside the repository (`WT/tools/t3_host_names.private.txt`).
  - It screens each name case-insensitively: whole and by each distinctive label, in split forms, and a network name's own domain as written.
  - A hit prints the file and a label, never the name.
  - The strict path forms and the junit host-attribute rule are unchanged.
- **Nothing else in the record changed.** `ADDENDUM_01.md` is unchanged. Every other file of `addendum_01/` is byte-identical to its first publication. Only that one line of `SHA256SUMS.addendum_01` changed.

| File | Old sha256 | New sha256 |
|---|---|---|
| `addendum_01/harness/sanitize_py.py` | `7dff5ffc190d8da8d73d14e44150d4983ace2873f5e55a82f5c3ee6fab5fbe78` | `544a4587dd71c438d2c959f2c91fe1c3d90e7f3a2af85dc442eba71962d92d51` |
| `SHA256SUMS.addendum_01` (183 entries, all OK) | `048bda6ace76a11a9242cd81c8744822354fedee168abc9cf7aa156181f217c0` | `c65a445e8296b81bd9a3656d99964b1cd76b5da2a30b187a6b897bde34216bd4` |
| `ADDENDUM_01.md` | `a61bbe1b5c81ffc88c988e4fcc04d4702dcc8873d8b06a2d151fc2a8dfd757e3` | unchanged |

## The behaviour on its inputs is unchanged (`redaction_01/equivalence.txt`)

All runs used VENV's Python. They are compared by `redaction_01/compare_trees.py`: plain files byte for byte, and `.gz` files by their decompressed bytes. The gzip header holds the time of writing, in the old script as in the new.

1. **The same raw inputs.** I re-assembled the addendum's evidence, unsanitized, from scratch. The old and new scripts each ran on their own copy of it, and each returned rc 0. **Their outputs are identical on all 183 files.**
2. **Rerun on what it sanitized.** The new script ran on a copy of the folder as now published, and returned rc 0. **The outputs are identical on all 183 files:** the 76 plain files byte-identical, and the 107 `.gz` files with identical decompressed bytes.
3. **Rerun on the folder as first published.** The new script flags exactly one file, the old `sanitize_py.py` itself, which is the reason for this redaction. Every other file passes, unchanged.
4. **Self-test.** I wrote each name to a scratch file by redirection, never printing it, and deleted the files afterwards. The new script flags every form the old one flagged.

## Screens

Both of ROOT's tools ran from my scratch, on a temporary index of my own (`GIT_INDEX_FILE`), never NUM's. That index staged this folder's files for this addendum and my two other new addenda:
- `t3_host_screen.py <NUM> --staged`;
- `validate_private_terms.py --staged --from-host --terms-file WT/tools/t3_host_names.private.txt`, run from NUM.

The results are in my return to ROOT. This file is screened as part of that run.

## Records

`REDACTION_01.md`, and `redaction_01/` (`compare_trees.py`, `equivalence.txt`), covered by `SHA256SUMS.redaction_01`.
