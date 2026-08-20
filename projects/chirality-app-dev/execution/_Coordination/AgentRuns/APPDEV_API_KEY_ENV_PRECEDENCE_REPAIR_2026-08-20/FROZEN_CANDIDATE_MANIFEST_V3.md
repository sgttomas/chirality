# Frozen integrated candidate manifest v3

- Frozen after Review 02 terminal return; no agent was writing candidate bytes
- Branch: `codex/app-api-key-precedence-20260820`
- Basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`
- Candidate paths: `98`
- Product/test paths: `4`
- Evidence/state/control paths: `94`
- Aggregate SHA-256: `7ea308cf90bac02a7c439c71d0f01d2024ecee2a90c1fc16cfd1f4fd95bc1959`
- Raw N3 host proof: `/tmp/chirality-precedence-closure.pXvs6Z`

## Exact reconstruction

Before this v3 manifest and Review 03 controls were created, the complete
candidate was the sorted union of modified and untracked paths:

```text
{ git diff --name-only --diff-filter=ACMRTUXB; git ls-files --others --exclude-standard; } | sort -u
```

The aggregate is the SHA-256 of the newline-delimited `/usr/bin/shasum -a 256`
per-file output in that exact 98-path order. Review 03 excludes only this v3
manifest and its own launch/status/return controls, then must reconstruct
exactly 98 paths and the aggregate above. Manifests v1/v2 and Reviews 01/02
plus remediation controls remain included and must be inspected.

## Accepted backchecks

- Review 02 independently passed F1-F3, product/security, raw packaged proof,
  compact evidence, APP-HOLD, state/Remaining calibration, lifecycle,
  dependency, and release-fence checks.
- Review 02's sole finding was the v2 manifest aggregate; no candidate product,
  evidence, or state remediation was requested.
- Product/test, compact proof, raw artifact, and normalized harness identities
  remain unchanged.

Review 03 must review all 98 paths and return PASS with zero actionable
findings before fan-in.
