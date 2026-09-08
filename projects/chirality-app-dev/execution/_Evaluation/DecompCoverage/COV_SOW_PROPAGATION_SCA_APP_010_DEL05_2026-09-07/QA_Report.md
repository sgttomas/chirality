# QA report

- Base identity: `HEAD = 35249accf139f52478d029458946e50ed25ee5dc`.
- Addendum manifest: 13/13 members rehashed successfully; `MANIFEST.sha256` SHA-256 `694baaa9b7f102e855df1e428ea5b729b0d5749c15e38515706371ee49bf907f`.
- Patch: SHA-256 `d71f6a2971409e6a872b778a73d66a2355cb41b2bb125af95da26c3d67f6b98f`; forward `git apply --check --cached` PASS against the base index preimage; reverse `git apply --check --reverse` PASS against the live postimage; one path, 10 insertions and 8 deletions.
- SOW: preimage SHA-256 `83f206d623dd72130cab799e8e9216440635fb3cbe82ed8b17a6216092abf06f`; live SHA-256 `0c40921347b4478d3d200daf4a766a5652239a2c9ab4b60ad0646017c5c70c29`; 35,562 bytes.
- Validator: `tools/scope_of_work/validate_scope_of_work.py --json` returned `SOW_V1`, `valid: true`, zero issues.
- Derived checklist: two fresh derivations were byte-identical, SHA-256 `fdb055a4e64a8381c1828933f2e27cb7157963a3613b977e116b04a8df3de2eb`.
- Definitions: 28 CLM, 5 REQ, 2 AC, 2 VER, 2 OUT; all identifiers unique. Frontmatter and Markdown fence checks pass.
- Historical applied-row quotation: pre/post extracted `CLM-028` section SHA-256 `02d170d6d7a24634deeabd5d23847c3d9cbf22edf4b056eded13d2aa20c10de3`.
- App pointer: SHA-256 `7a2d955e464403267daba513ac2600e6666acb814e42ff0be09935cf8f4eee23`; it retains SCA-APP-010 as active and records only the addendum's `APPLIED_AUDIT_PENDING` state.
- Active semantic snapshot: 59/59 `MANIFEST.sha256` entries rehash successfully; live decomposition SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; companion SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; handoff SHA-256 `314268a664c425fd031be02451394b1986122aad930fedbae89cf0cba372ad30`.
- Changed-path boundary before audit output: App state contains exactly the DEL-02-05 SOW, `_ScopeChange/_LATEST.md`, and the 13 addendum members. `git diff --check -- projects/chirality-app-dev` passes.
- Runtime DEL-02-06/09 SOW, Runtime pointer/addendum, and Runtime audit coordination paths are concurrent authorized sibling state excluded from this App verdict.
- Limit: this was a bounded document/poststate audit. It did not execute or infer source, supplier, implementation, product tests, trial, lifecycle, release, publication, or concordance effects.
