# D-APP-93 owner-trace repository normalization amendment

Status: `COMPLETE — RAW SOURCE IDENTITIES PRESERVED; REPOSITORY COPIES NORMALIZED`

## Superseding direction and scope

The owner superseded the earlier immutable-whitespace exception posture with
`Fix the files. Do it the right way.` The two named repository evidence copies
were therefore normalized canonically. The external source files were not
edited. No fact, packet, product, runtime, source, lifecycle, closure,
acceptance, remedy, or disposition act was performed.

`records/IMPORTED_IDENTITIES.sha256` is retained byte-exact at SHA-256
`3bae2915dd21a0701ea4159dc5e60f4d26fd70d0e4cf12e74e78bb897b778888` as
the source-ingest identity manifest. Its `evidence/**` labels name the import
targets at the instant of exact ingest; for the two normalized files it is not
a manifest of the current repository-copy bytes. Current repository-copy
identities are governed by `records/NORMALIZED_REPOSITORY_IDENTITIES.sha256`.

## Canonical byte transform

For each named raw source, the transform was applied in this exact order:

1. replace every `CR LF` byte pair with one `LF`;
2. replace every remaining lone `CR` byte with one `LF`;
3. remove every maximal run of `SP` or `HT` immediately before `LF` or EOF;
4. preserve every other byte in order.

| Repository path | Raw source SHA-256 | Raw bytes | CRLF pairs | Remaining lone CR after step 1 | Trailing SP/HT runs removed | Trailing bytes removed | Normalized SHA-256 | Normalized bytes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| `evidence/EVIDENCE_CAPTURE.md` | `fe0f89eea64a294e1c050e6bc46cd6d2934fe185f98d149fe54cfd6a8191d707` | 14,459 | 0 | 0 | 1 | 1 SP, 0 HT | `314ee96db7d73552a1e41d1b88e6d5d32fcd8aa7ed9c19411c3e2e56844e6ef1` | 14,458 |
| `evidence/LLDB_TRANSCRIPT.txt` | `43763e06b4d3536f48713cfc5b5d4a69b496d3fd4057212b5da3694262740536` | 971,359 | 552 | 8 | 17 | 277 SP, 0 HT | `358228ac79541b829f2c61f3bcd3e89983f150ea020a2e692c02d8e27623f522` | 970,530 |

The evidence-capture trailing run was the single SP at source line 107. The
transcript's 17 trailing runs contained 277 SP bytes total. Two of the eight
remaining CR bytes in the transcript were the first byte of a `CR CR LF`
sequence; the ordered transform correctly produces two LF bytes for each such
sequence.

## Reproducibility and identity verification

The two external raw sources were re-read after normalization and retained
their raw SHA-256 identities and byte counts shown above. A separate
reproduction pass loaded each external raw byte stream, applied the four
ordered rules in memory, and compared the result byte-for-byte to its
repository copy: 2/2 exact. The normalized copies contain zero `CR` bytes and
zero trailing `SP`/`HT` runs before `LF` or EOF. The normalized repository
identity manifest replays 11/11 `OK` from the run root.

The pre-normalization fresh-verifier return at SHA-256
`99f2357445dcb1d87dd3761d279e1753cdbf6bdc4fc9d4d8fd866b4944eeb5f0`
is preserved as evidence of the exact-ingest semantic review. Its statements
that the two landed copies matched the ingest manifest describe the
pre-normalization state. The manager performed the deterministic reproduction,
semantic-preservation, inventory, and candidate-whitespace rechecks recorded in
`validation/CLOSEOUT_CHECKS.md` after this authorized normalization.
