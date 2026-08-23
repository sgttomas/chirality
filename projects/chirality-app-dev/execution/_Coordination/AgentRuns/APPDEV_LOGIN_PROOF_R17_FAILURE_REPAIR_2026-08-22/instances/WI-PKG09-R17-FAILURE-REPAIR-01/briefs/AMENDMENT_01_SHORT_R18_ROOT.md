# Amendment 01 — short future R18 root

- Disposition: `AMEND`, pre-freeze and non-consequential to product code.
- Superseded proposal:
  `/private/tmp/chirality-r18-91499728-51dd-4b2d-8aff-0eb77648135a`
  with a 97-byte future socket path.
- Controlling proposal: `/private/tmp/ch-r18-91499728-51dd`
- Read-only check: the exact controlling path is absent and not a symlink.
- Exact lengths: root 33 UTF-8 bytes; full
  `${root}/runtime-data/runtime/control.sock` 67 UTF-8 bytes; safety margin 36
  bytes below the 103-byte macOS maximum.

The executor must replace the superseded proposal in R17, status, current
evidence, and its return; refresh affected hashes; and perform no product-code
or other semantic change for this amendment. The fresh reviewer must assess
uniqueness, absence/non-symlink state, exact byte count, practical short-root
intent, and the 36-byte margin. The root remains proposal-only: do not create,
stage as R18, prepare, capture, or otherwise query it beyond read-only
absence/non-symlink checks.
