# Attempt-4 candidate-whitespace repair backcheck

Status: `PASS — FOUR FINDINGS REPAIRED MECHANICALLY`

The first fresh Attempt-4 verifier returned `BLOCK` only because the mandatory
candidate-whitespace validator found four current-byte defects. Verifier
SHA-256:
`9cd2ab474889c863b50a107aacada44bf41e3b18b4293b0f44db34e66a704769`.

## Exact repairs

| Path | Finding | Pre SHA-256 | Post SHA-256 | Repair |
|---|---|---|---|---|
| `OWNER_ATTEMPT4_COMMAND_APPROVAL_ADOPTION.md` | one blank line at EOF | `ee33d3e65691d5bef46f9548141cec9a22ed1bbc5c32fed75bbba7f8fc28851f` | `b134c081b77375878828bdb490316059f264014172b1544cabecc8fc555267e5` | removed exactly one terminal LF |
| `evidence/attempt4/C198_STDOUT_STDERR.txt` | three line-terminal spaces | `41398a7cee7654a9fad224d6c478dcabd81890d2646917819213f45844ab65bf` | `cd3ca1dd91a181a3900fb9b136c3f4871949916488c3bbb1ce76d780591e2c54` | removed only `[ \t]+$` on the three reported lines |

The exact original 5,634 C198 bytes were losslessly preserved before repair in
deterministic-gzip container
`evidence/attempt4/C198_STDOUT_STDERR_RAW.txt.gz`, container SHA-256
`e736c7081b1a39634feb28a02286b3c1950e5bd80bbf8cbbd825f7f8fb1271db`.
Decompression reproduces the exact pre-repair SHA-256
`41398a7cee7654a9fad224d6c478dcabd81890d2646917819213f45844ab65bf`.

Semantic-normalized equality was proved without materializing another file:
decompressing the raw capture, applying only `s/[ \t]+$//`, and hashing
produced
`cd3ca1dd91a181a3900fb9b136c3f4871949916488c3bbb1ce76d780591e2c54`,
exactly the repaired readable-copy hash. No non-whitespace byte changed.

`evidence/attempt4/COMMAND_OUTCOMES.md` was refreshed only to bind both the raw
and readable forms; its pre/post SHA-256 identities are
`bcaf366f4eeb30d8af1a40ec6b14e4a1c008f5ac5607becbe9630a20e66725fd`
and
`e1205486ca300d894b022b9afe8c6deabb697475f3ccb0c84ad91db45ec36013`.
The attempt outcome, command count, failure boundary, cleanup claims, and all
exclusions are unchanged.
