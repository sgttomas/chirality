# W6 D-APP-50 Checksum-Repin Correction Handoff

- **Verdict:** `BLOCK`
- **Basis:** G2 `55a066fdff6877d8aa2a49ce08a545ac98872848`
- **Candidate hashes:** D-APP-48
  `ad10f6e5808754c4acf2e9114f189c892dbec2231a3059d3717e9689e7807040`;
  DEL-10-01 status
  `3b5c7a7e1ebe2c15fcd59e3a9a92c9b16ab6371a553dfa0492ddee2f791bd020`;
  checksum repair record
  `fbdbc50ad0d8e324799f702e5a821a19a5227b54f804ddc5cfbd23da98a11823`;
  Receipt-85 ledger
  `c8a7ab466fc694b6743310a8a5cd6f75c4280c49fb67baac1c6717da442bb0e8`.
- **Captured gates:** strict JSON, pull contract, dependency lint, focused
  51/51, receipt validation, corpus v9, self-check, validation pytest 123/123,
  topology/hash/diff/containment, empty index, and dist absence pass.
- **Blocker:** practitioner-harness pytest terminal exit code and summary were
  not retained. Two W6-owned duplicate attempts exited; no process remains and
  no `311/311` claim is made.
- **Candidate posture:** unstaged and unaccepted pending a clean validation
  retry; Receipt-83/84 prefix remains byte-identical.
- **Unknowns/conflicts/waivers:** one terminal-result unknown / none / none.
- **V3/final publication:** held.

Route only to a fresh serialized W6 validation retry with exactly one
practitioner-harness run whose terminal exit code and summary are retained.
Do not rewrite prior receipts or run records. Release V3 only after a coherent
W6 `ACCEPT`.

