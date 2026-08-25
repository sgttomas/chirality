# Primary Supply Inventory — App Server 0.149.0 — macOS arm64

Candidate state: `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

N2 verdict: `PASS_UNDER_R13_AMENDED_SIGNATURE_GATE`

Observed: 2026-08-25T04:06:47Z (2026-08-24 America/Edmonton)

## Authority and dependency

- Basis commit: `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
- N1 return SHA-256:
  `3b37a25b50254ecedce1871e59515ce53c8de7e42f24cc9dca97e71853cfae20`
- Original supply steer SHA-256:
  `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`
- R12 SHA-256:
  `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`
- First resume steer SHA-256:
  `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`
- R13 SHA-256:
  `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960`
- Second resume steer SHA-256:
  `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164`
- R14 SHA-256:
  `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9`

## Exact acquisition

The N1-selected primary archive was downloaded once from the exact official
release URL:

`https://github.com/openai/codex/releases/download/rust-v0.149.0/codex-app-server-aarch64-apple-darwin.tar.gz`

It was written to the unique external quarantine
`/private/tmp/chirality-root-supply-r14-primary.lTtHP2/`. The quarantine is
outside the repository and the received bytes are absent from `git ls-files`.

| Field | Published identity | Observed identity | Result |
| --- | --- | --- | --- |
| Repository/release | `openai/codex` / `rust-v0.149.0` | canonical GitHub release URL | MATCH |
| Asset | `codex-app-server-aarch64-apple-darwin.tar.gz` | exact named asset only | MATCH |
| Size | `71843308` bytes | `71843308` bytes | MATCH |
| SHA-256 | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` | same | MATCH |

No alternate release, binary version, mirror, or equivalence asset was
downloaded by N2. Exact-tag `LICENSE` and `NOTICE` texts were retrieved only
to discharge the license and redistribution inventory; they are not
substitute artifacts.

## Archive and platform inventory

`tar -tzvf` passed. The archive contains exactly one member:

```text
-rwxr-xr-x  0 runner staff 179721344 Aug 20 14:45 codex-app-server-aarch64-apple-darwin
```

The member was extracted and inspected without execution:

| Field | Observed value |
| --- | --- |
| Size | `179721344` bytes |
| SHA-256 | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` |
| Format | Mach-O 64-bit executable |
| Architecture | `arm64` |
| Mach-O type | `EXECUTE` |
| Build platform | macOS (`LC_BUILD_VERSION` platform `1`) |
| Minimum OS | `11.0` |
| SDK | `15.5` |

These identities match the R13 primary requirement exactly.

## Signature inventory under R13

Static inspection found an embedded signature with:

- identifier `codex-app-server`;
- Team Identifier `2DC432GLL2`;
- hardened-runtime flag `0x10000(runtime)`;
- SHA-256 CDHash `58661040e933585cbea4128ad6314b7ca0bf54da`;
- full SHA-256 CDHash
  `58661040e933585cbea4128ad6314b7ca0bf54dab3a58d666e0ac9c12b592f21`;
- signature size `9048` bytes; and
- `LC_CODE_SIGNATURE` offset `178311296`, size `1410048`.

The verification result matches every element of the defect class R13 admits:

```text
TeamIdentifier=2DC432GLL2
invalid signature (code or signature have been modified)
In architecture: arm64
codesign_strict_exit=1
warning: binary contains an invalid entitlements blob. The OS will ignore these entitlements.
spctl_exit=1
```

Gatekeeper's text was `internal error in Code Signing subsystem`. Upstream
issue <https://github.com/openai/codex/issues/37725> is the defect reference
named by R13. The exact 0.149.0 measurement above—not the issue alone—grounds
this artifact's result.

No other signature, identity, version, architecture, or license disagreement
was observed. Under R13-A this exact signature class is inventory, not a stop.
It remains the named R13-B G5 open finding and is not made valid by this
candidate.

## License and redistribution

The primary release archive contains neither a license nor a notice member.
N2 therefore verified the exact official tag's `LICENSE` and `NOTICE` files:

| File | Size | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `LICENSE` | `10926` | `d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc` | `4606e72e042564097e8780d66c1d4dcb611869bd` |
| `NOTICE` | `242` | `9d71575ecfd9a843fc1677b0efb08053c6ba9fd686a0de1a6f5382fd3c220915` | `2805899d56d0332d175cfc613c67d45d6f006db7` |

The license is Apache License 2.0. A future redistribution package must add a
copy of the license and carry the applicable Section 4 attribution/notice
obligations, including the exact-tag notice. The primary archive is therefore
not itself a self-contained redistribution package. N2's redistribution gate
is `PASS_TERMS_IDENTIFIED_PACKAGING_OBLIGATION_RECORDED`: the exact terms and
notice are available and pinned, while their omission from the binary-only
archive remains visible for G2 and later packaging. This tranche performs and
authorizes no redistribution.

## Boundary and handoff

- The vendor binary was never executed or installed by N2.
- No live `CODEX_HOME`, PATH, launchd, daemon, pin, manifest, or runtime
  configuration was touched.
- The quarantine remains intact and untracked for N2b and, only after N2b
  passes, N3.
- N2b is released for only the two exact R13 equivalence assets.
- No G2 acceptance, pin amendment, cutover, implementation, publication, or
  reliance claim is made.
