# R18 whitespace repair cycle 1 — byte lineage

Status: `NORMALIZATION_EQUIVALENCE_PASS`

Each defective preimage was frozen before modification with deterministic
`gzip -n`. Decompressing each archive reproduces its frozen byte count and
SHA-256. Applying only CR line-ending/trailing-CR deletion, line-end space/tab
deletion, surplus EOF-LF deletion, and exactly one final LF reproduces the
repaired target byte-for-byte.

| Target relative to run root | Pre bytes | Pre SHA-256 | Gzip bytes | Gzip SHA-256 | Post bytes | Post SHA-256 | CR bytes | Trailing space/tab bytes | Surplus EOF LF bytes | Delta |
|---|---:|---|---:|---|---:|---|---:|---:|---:|---|
| `instances/WI-PKG09-R18-STAGING-01/executor-3/REQUEST_STATE.md` | 743 | `3902379feebe7c13ec67bbe642e42e0e6a9bb37939b82a854f1076a021d235aa` | 510 | `fb2763dc195fad6b7ee8ed156c4f4468136a6b34154ba0c340ec94bd7da5ca75` | 742 | `c54c2465a2d9dfa765d756a97a0b8c35306441eceae011bdc46e7f736aace778` | 0 | 0 | 1 | deletion-only: one surplus EOF LF |
| `instances/WI-PKG09-R18-STAGING-01/executor-3/shasums256.response-headers.sanitized.txt` | 5234 | `8fcdc127011282e75e8d0a3bbd118ab733f723c3f6a4c04cad5e4f017375668f` | 1724 | `da3a6151d2c2a31e76394aa086bc93be7da297dba1381416fe604f43e3cd39dc` | 5188 | `f0754892c2fa8df1a9c59f14679f3abe1ea7e068999bcc230fc136a2ade6c6a1` | 43 | 2 | 1 | deletion-only: 43 CR, two trailing horizontal, one surplus EOF LF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/focused-tests.log` | 261 | `580ad49f26036c10c70fb6b13fea8e4e8fb0d7244112d0c70885834cdc55338b` | 209 | `4dc547762885d087bb0042dd49e1cadfe337e79aa67e6236af69e9b9d78d531f` | 260 | `d7d1868010e9b1785f594bed19b7f6e93be7f446c6c7198cfece92c74aa9edb6` | 0 | 0 | 1 | deletion-only: one surplus EOF LF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/full-vitest.log` | 9888 | `7e0907732af579802a927d09028b301cc167b1ec83fc490e7d1fc61bd1220dab` | 1917 | `ede5caba8e7ab7065af2493cb72ab69f7e1405220d481e0469ae6b60f0b12c8c` | 9887 | `8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19` | 0 | 0 | 1 | deletion-only: one surplus EOF LF |
| `instances/WI-PKG09-R18-STAGING-01/review-1/typecheck.log` | 136 | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` | 115 | `2bee31acfe5afe23d0b26c161ef1cc6ed88b8bf68ecb590b29ec4fa48b90e61d` | 135 | `b1a67869986e76e171a01d5f562874d6b55653c9b53cea7c552d8949510a8483` | 0 | 0 | 1 | deletion-only: one surplus EOF LF |

No line order, text, or interior blank line changed. All five repaired targets
end with exactly one LF.
