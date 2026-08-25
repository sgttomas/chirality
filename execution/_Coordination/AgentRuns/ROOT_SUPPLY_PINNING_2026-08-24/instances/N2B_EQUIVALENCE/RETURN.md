# Return — N2b Exact Packaging Equivalence and Ancillary Hash Freeze

- **Status:** `PASS`
- **Verdict:** `PASS_EQUIVALENT_2_OF_2`
- **Zstd asset:** `50359498` bytes; SHA-256
  `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677`.
- **Package asset:** `93775517` bytes; SHA-256
  `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2`.
- **Contained app servers:** both alternate arm64 Mach-O payloads are
  `179721344` bytes, SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`,
  and byte-identical to the independently reverified N2 primary (`cmp` exit
  `0` for zstd and package; alternate-to-alternate exit `0`).
- **Signature:** both alternate app-server copies match only the exact
  R13-admitted defect class. No additional identity or signature disagreement
  was observed.
- **Package inventory:** five files, four Mach-O executable members; the
  three ancillary executable identities are frozen in
  `EXECUTABLE_HASH_FREEZE.json` for R14-B.
- **Execution:** none; no downloaded or extracted member was invoked.
- **Quarantines retained:** primary
  `/private/tmp/chirality-root-supply-r14-primary.lTtHP2`; equivalence
  `/private/tmp/chirality-root-supply-r14-equivalence.BmK7x0`.
- **N3 gate:** `RELEASED`, subject to per-run executable-hash and sandbox-deny
  preflight checks.

## Durable output hashes

| Output | SHA-256 |
| --- | --- |
| `02B_EQUIVALENCE/EQUIVALENCE_INVENTORY.md` | `11ee3b41fd9dda8f4a33a7c6a77a6bb86c14e24f16781795b743110f336b4005` |
| `02B_EQUIVALENCE/EQUIVALENCE_RESULTS.json` | `283e92d066028537157bdd5ac179fe505c10460647164048f358f664317111eb` |
| `02B_EQUIVALENCE/EXECUTABLE_HASH_FREEZE.json` | `ef40fa3be9a15e521bc9b30ba3b82c41f2ebe71d9f8ca6cf45a0cfa5308da5ec` |
| `02B_EQUIVALENCE/PACKAGE_ANCILLARY_INVENTORY.md` | `3f896705cb922966c974d57f25a0f496c8c1e95921ec4c86c78f6bbfe5e30ba2` |
| `02B_EQUIVALENCE/SIGNATURE_INSPECTION_ALTERNATES.txt` | `b5d7101ea7f259d47d3c4a587218b042ab66720826d5669c98666693f06f59ac` |
| `instances/N2B_EQUIVALENCE/COMMAND_RECORD.md` | `bc18c5994de24b15f5b1bdfc6091fcf9a3ec9e53ea14932f665485a70d99d1f6` |

## Deterministic evidence correction

The prior `.zst` archive row in `EQUIVALENCE_INVENTORY.md` carried a malformed
65-hex-character splice sharing material with the archive and payload
identities; it matched neither identity. It is corrected to the official,
already-recorded 64-character archive SHA-256
`c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677`.
This record-only correction used no download, vendor execution, or network
probe and did not change the underlying equivalence result.

No G2 acceptance, pin amendment, installation, cutover, implementation,
publication, or reliance claim is made. The invalid vendor signature remains
the named R13-B G5 open finding.
