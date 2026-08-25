# License and Redistribution Inventory

State: `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Exact-tag identities

| Field | Value |
| --- | --- |
| Official tag | `openai/codex` `rust-v0.149.0` |
| License URL | <https://raw.githubusercontent.com/openai/codex/rust-v0.149.0/LICENSE> |
| License size | `10926` bytes |
| License SHA-256 | `d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc` |
| License Git blob | `4606e72e042564097e8780d66c1d4dcb611869bd` |
| License identity | Apache License, Version 2.0, January 2004 |
| Notice URL | <https://raw.githubusercontent.com/openai/codex/rust-v0.149.0/NOTICE> |
| Notice size | `242` bytes |
| Notice SHA-256 | `9d71575ecfd9a843fc1677b0efb08053c6ba9fd686a0de1a6f5382fd3c220915` |
| Notice Git blob | `2805899d56d0332d175cfc613c67d45d6f006db7` |
| Primary archive license member | none |
| Primary archive notice member | none |

The exact-tag notice identifies OpenAI Codex, Copyright 2025 OpenAI, and the
included Ratatui-derived code and MIT attribution.

## Redistribution obligations inventoried from the exact text

Apache-2.0 Section 4 permits source or object distribution, modified or
unmodified, provided the distributor:

1. gives every recipient a copy of the license;
2. makes modified files carry prominent notices that they were changed;
3. retains applicable copyright, patent, trademark, and attribution notices
   in the Source form of distributed derivative works; and
4. when the Work includes a `NOTICE` file, carries the applicable attribution
   notices in a distributed `NOTICE`, accompanying source/documentation, or an
   appropriate generated display.

Additional exact-text consequences recorded for later packaging:

- added notices must not purport to modify the license;
- additional terms for modifications or a derivative work as a whole may be
  supplied only while use, reproduction, and distribution remain compliant;
- the license does not grant trademark permission except reasonable use in
  describing origin and reproducing `NOTICE` content;
- the Work is supplied on an `AS IS` basis without warranties or conditions;
  and
- anyone offering extra warranty, support, indemnity, or liability does so on
  their own behalf and responsibility and must protect contributors as the
  license states.

## Packaging consequence

The primary `.tar.gz` contains only the executable and is not a self-contained
redistribution package. A future redistribution package must include the exact
license copy and evaluate/carry every applicable notice attribution. This is a
recorded packaging obligation. Because the exact terms and exact notice are
identified and pinned, the N2 evidence gate is
`PASS_TERMS_IDENTIFIED_PACKAGING_OBLIGATION_RECORDED`; no unresolved license
identity remains. This is not permission in this tranche to redistribute,
publish, cut over, or rely on the artifact.
