# Exact Packaging Equivalence Inventory

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**Verdict:** `PASS_EQUIVALENT_2_OF_2`

**Basis:** `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`

## Asset identities

| Official `openai/codex@rust-v0.149.0` asset | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | `71843308` | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` | primary retained bytes independently reverified |
| `codex-app-server-aarch64-apple-darwin.zst` | `50359498` | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` | downloaded and exact |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | `93775517` | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` | downloaded and exact |

The two R13 alternate assets were downloaded only from their canonical
release URLs into the external equivalence quarantine. Size and SHA-256 were
required before extraction. The primary archive and extracted primary were
independently reverified in the retained N2 quarantine.

## Payload equivalence

| Packaging | Contained payload | Bytes | SHA-256 | Architecture | `cmp` versus primary |
| --- | --- | ---: | --- | --- | ---: |
| primary tar | `codex-app-server-aarch64-apple-darwin` | `179721344` | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` | Mach-O arm64 | reference |
| zstd | decompressed `codex-app-server-aarch64-apple-darwin` | `179721344` | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` | Mach-O arm64 | exit `0` |
| package tar | `bin/codex-app-server` | `179721344` | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` | Mach-O arm64 | exit `0` |

The two alternate payloads also compare equal to each other (`cmp` exit
`0`). This proves the required 2/2 alternate-packaging equivalence against
the independently reverified N2 primary.

## Signature disposition

Both alternate app-server copies report Team Identifier `2DC432GLL2`, the
hardened-runtime flag, strict verification exit `1` with `invalid signature
(code or signature have been modified)`, an invalid-entitlements warning,
and `spctl` exit `1`. Those facts match exactly the R13-admitted documented
defect class. No additional app-server identity or signature disagreement
was observed. The invalid published signature remains the R13-B G5 open
finding; this pass is not a reliance claim.

## Quarantine and execution

- Primary quarantine: `/private/tmp/chirality-root-supply-r14-primary.lTtHP2`
- Equivalence quarantine: `/private/tmp/chirality-root-supply-r14-equivalence.BmK7x0`
- Downloaded or extracted vendor-code execution in N2b: `NONE`
- Quarantines are outside the repository and retained for bounded N3.

No G2 acceptance, pin amendment, installation, cutover, implementation,
publication, or reliance claim is made.
