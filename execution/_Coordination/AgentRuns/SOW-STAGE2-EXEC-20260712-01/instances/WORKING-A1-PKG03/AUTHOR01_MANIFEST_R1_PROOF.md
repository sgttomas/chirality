# AUTHOR-DEL-03-01 Manifest R1 Proof

Authority: `amendments/A1-PKG03-AUTHOR01-MANIFEST-R1-001.md`.

Verdict: `PASS`.

| Property | Preimage | Postimage |
|---|---:|---:|
| Bytes | 4,328 | 6,295 |
| Lines | 30 | 30 |
| Data rows | 29 | 29 |
| Unique paths | 29 | 29 |
| SHA-256 | `1b0c5d862dee09eae4298d22908f5a89dde4d0db11852342049eaebf127bab95` | `5b25453a2f63fb4cc582687c878d6a54e71245bf2edbf455fd461536fe2a1b0a` |
| Path-column SHA-256 | `da67a7a35963c5e3780abf2501dc82700a026b29cf8ed03b03a6581ca7b5286f` | `da67a7a35963c5e3780abf2501dc82700a026b29cf8ed03b03a6581ca7b5286f` |

Exactly 58 empty cells became computed values: one SHA-256 and one byte count
for each existing artifact. All 29 postimage hashes and byte counts reproduce
independently. Blanking only those 58 computed cells in the postimage
reconstructs exactly 4,328 bytes at the recorded malformed preimage hash,
proving the header, path strings, set, and order are byte-identical.

Generator defect: the original zsh loop used the special `path` variable.
Corrected method: a bounded in-place Perl regeneration read each first-column
artifact in binary mode and filled only columns two and three.

Direct malformed-preimage bindings: `NONE` inside the package instance; the
only prior hash occurrence is the authorizing amendment. No binding refresh
was required.
