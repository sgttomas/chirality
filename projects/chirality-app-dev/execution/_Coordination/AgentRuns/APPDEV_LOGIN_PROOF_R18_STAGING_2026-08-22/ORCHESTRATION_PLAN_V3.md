# DEL-09-04 R18 Tranche A continuation — orchestration plan v3

Status: `FROZEN — NETWORK NODE ONLY; SYNC ACKNOWLEDGMENT HOLD`

This plan preserves v1 cache-miss and v2 redirect-stop evidence. It supersedes
only the network boundary: one fresh executor may follow the known 302 once to
`release-assets.githubusercontent.com`. No implementation node is released.

## Immediate graph

1. `A2-PKG09-R18-NETWORK-03`: exactly one new curl invocation/request chain,
   exact GitHub start URL, HTTPS only, maximum one redirect, chain limited to
   GitHub then release-assets, text response only, no artifact.
2. `WI-PKG09-R18-STAGING-01`: validate network evidence and pause.
3. Future sync/implementation/review nodes remain held until supervising
   HELP_HUMAN supplies the exact sync acknowledgment.

The network executor writes only `executor-3/` evidence. It may not implement,
test, build, write R18/status/receipt, or review.

## Network acceptance

- Exactly one new curl invocation and one redirect, with response chain only
  `github.com -> release-assets.githubusercontent.com`.
- Final 2xx, plausible plain-text body near 7.6 KB, complete body retained once.
- Full body SHA-256 recorded and exactly one arm64 filename line whose hash is
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
- Headers sanitized so signed redirect query values are not retained; status,
  hosts, request/redirect count, final status, effective host, and byte size
  remain evidenced.
- No artifact request/download or other host.

## Hold

Even on PASS, stop before source/tests/build/R18/status/review/receipt. The
authorized non-rewriting sync target is
`b143444bd497eae1b1b638670a33e6df756d9084`, but execution waits for the exact
sync acknowledgment requested by HELP_HUMAN. No silent sync.
