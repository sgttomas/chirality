# N1 Fresh Exact-Artifact Acquisition

- **State:** `EXACT_PRIMARY_ASSET_AND_PAYLOAD_VERIFIED`
- **Retrieval date:** 2026-08-27
- **Official channel:** `https://github.com/openai/codex/releases/tag/rust-v0.149.0`
- **Official metadata API:**
  `https://api.github.com/repos/openai/codex/releases/tags/rust-v0.149.0`
- **Metadata receipt SHA-256:**
  `edc7e7fa96701ef0b15a81588b5003882027cc93b4ff5e4eaefa8073934de8dc`
- **Metadata receipt bytes:** `342325`
- **Published tag/date readback:** `rust-v0.149.0` /
  `2026-08-20T21:04:55Z`
- **Fresh quarantine:** `/private/tmp/chirality-r16-n1.iMyfhF`

Only the minimum required accepted asset was downloaded:

| Asset | Official metadata bytes | Received bytes | Official/received SHA-256 | Result |
| --- | ---: | ---: | --- | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | `71843308` | `71843308` | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` | `PASS_EXACT` |

The archive contained one member,
`codex-app-server-aarch64-apple-darwin`. It was extracted only after the
archive gate passed. The payload is a 179,721,344-byte arm64 Mach-O with
SHA-256
`b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`,
exactly matching the R15-accepted payload identity.

The asset and extracted payload remain untracked in the fresh quarantine.
No prior artifact or quarantine was reused. No vendor binary executed before
the archive and payload identities passed. Final teardown and absence proof
are recorded at N4.
