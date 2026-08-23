# Repair lineage — implementation evidence hygiene cycle 1

Initial candidate-whitespace exit `1` named exactly one surplus terminal blank-line LF in each of the four records below. No source finding was reported.

| Record | Preimage bytes | Preimage SHA-256 | Postimage bytes | Postimage SHA-256 | Post tail | `SHA256(post + LF)` |
| --- | ---: | --- | ---: | --- | --- | --- |
| `ACTIVATION.md` | `1119` | `c0060da4fb916aafc890d34c37f961a35ee0a17849288bd179350dfcfaf5c52e` | `1118` | `ae1f607d942b6a66600b45d59af399c9dceff7253e3624648acf16f697ebf7f1` | `2e0a` | `c0060da4fb916aafc890d34c37f961a35ee0a17849288bd179350dfcfaf5c52e` |
| `CHECKS_AND_LINEAGE.md` | `3608` | `18d5d95b822b853bf4c860c2a390d4dab299bba78310fe4c7e0c71c2c264f5df` | `3607` | `74b125a4cdcd3b47a1556ae9d79f1afa1113a34c16d52adff75792b4796afe0c` | `2e0a` | `18d5d95b822b853bf4c860c2a390d4dab299bba78310fe4c7e0c71c2c264f5df` |
| `IMPLEMENTATION_MODE_INVENTORY.md` | `1658` | `9f5a804ea6abe93c989c99ec60a326a82b4a586ed59bcfa71d255a4086147b59` | `1657` | `53d0f32a134721eda9ae545d9ff0bc0a2dae656fdb5b4421daa85d8a899c1bfc` | `2e0a` | `9f5a804ea6abe93c989c99ec60a326a82b4a586ed59bcfa71d255a4086147b59` |
| `RETURN.md` | `1987` | `505e6e0ab4e19c3b626fe0f20aa16216b91312ab94ed6b3867c220538af392b9` | `1986` | `412ce3bd36e04909dc9c465fc2285d2e613248310cb45722b24031578442520d` | `2e0a` | `505e6e0ab4e19c3b626fe0f20aa16216b91312ab94ed6b3867c220538af392b9` |

For every row, the postimage is exactly one byte shorter, ends in one LF but not two, and appending one LF reconstructs the preimage hash. No other byte or file was changed by the repair.
