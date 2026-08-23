# Sealed brief — A2-PKG09-R18-WS-REPAIR-01

## Identity and objective

- RequestedBy / Parent: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-WS-REPAIR-01`
- Fresh ephemeral generalist Agent 2; no delegation
- Objective: repair exactly five whitespace-only evidence defects while
  proving byte lineage and preserving substantive output.

## Exact targets and frozen pre-state

Paths are relative to the run root:

| Path | Bytes | Pre SHA-256 | Finding |
|---|---:|---|---|
| `instances/WI-PKG09-R18-STAGING-01/executor-3/REQUEST_STATE.md` | 743 | `3902379feebe7c13ec67bbe642e42e0e6a9bb37939b82a854f1076a021d235aa` | blank EOF |
| `instances/WI-PKG09-R18-STAGING-01/executor-3/shasums256.response-headers.sanitized.txt` | 5234 | `8fcdc127011282e75e8d0a3bbd118ab733f723c3f6a4c04cad5e4f017375668f` | CR/trailing whitespace on 43 lines plus blank EOF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/focused-tests.log` | 261 | `580ad49f26036c10c70fb6b13fea8e4e8fb0d7244112d0c70885834cdc55338b` | blank EOF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/full-vitest.log` | 9888 | `7e0907732af579802a927d09028b301cc167b1ec83fc490e7d1fc61bd1220dab` | blank EOF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/typecheck.log` | 136 | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` | blank EOF |

Fail closed before repair if any count/hash differs.

## Allowed writes and method

Write only the exact five targets plus unique
`repair-cycle-1/executor/` evidence/return. Before modification, preserve each
exact preimage as deterministic `gzip -n` evidence under
`repair-cycle-1/executor/preimages/`; record compressed hashes. Do not preserve
defective plaintext duplicates.

For each target, remove only:

- carriage returns used as line-ending/trailing CR;
- trailing spaces/tabs at line ends;
- surplus blank lines at EOF.

End with exactly one final LF. Do not change any other byte, line order, text,
or interior blank line. A deterministic normalization of each decompressed
preimage must equal the repaired target byte-for-byte. Record pre/post bytes,
hashes, CR count, horizontal-trailing-byte count, surplus EOF byte count, and
exact delta classification.

## Validation and return

Run `git diff --no-index --check /dev/null <file>` for each repaired target and
every new repair evidence text file; run candidate-wide new-file/staged-
equivalent whitespace checks, `git diff --check`, App-only containment, JSON
parse for all run JSON, exact seven semantic frozen hashes, original review
hash `3dd9e7377c8ceb5c8237aee6837431d872b86335605b2c87cfc800a3d46e21bc`,
and empty index. No test/build/network/package/proof/receipt/Git action.

Return `REPAIR_PASS` only on exact equivalence and all gates. Include lineage,
hashes, delta counts, changed paths, and fresh-review requirement.
