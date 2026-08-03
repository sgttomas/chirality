# R2 package evidence manifest

The generated app bundles are ignored derivatives and are not governed product truth. The following frozen extracts bind the package claims without retaining the full generated bundles.

| Evidence | SHA-256 | Claim |
|---|---|---|
| `package/PACKAGED_HASHES.txt` | `2c89220302479c1b6111864681660a09a023dd139c69f6eeccbb1975b9ba6104` | GUI, embedded-helper, and standalone-helper main/asar hashes |
| `package/SYMLINK_CENSUS.txt` | `5dc2df56a27afc8c3178a9a70ae3adc9e7a445bdbae3bc923fb04b9f82553c57` | 14 relative links and zero absolute links |
| `package/CHILD_TOPOLOGY.txt` | `7a54f80acc951edd1d6d5baecf0efc5527988a4f31a0086e196493ff42d947e0` | builder-generated helper child topology |
| `package/TOP_LEVEL_HELPER_CENSUS.txt` | `30a62b53c8d82f6e9c3a529e9aca450737495194280a4d05bf9b1241428d0df6` | exactly one top-level embedded helper |
| `package/WHOLE_TREE_COMPARISON.md` | see file hash in the corrected return | deterministic 812-entry content/mode/link comparison across standalone and embedded derivatives |
| `package/plists/gui.Info.plist` | `207434bba99d2323afa2790b5f3eb4609db04072094a2c6f7bc91a69d13d2696` | GUI identity |
| `package/plists/helper.Info.plist` | `06e7963346b43841a0e5be8bc6d56e025d946cc9ac77233e9b0fbc75c743f070` | runtime-helper identity and `LSUIElement` |
| `package/plists/Chirality Runtime Service Helper.Info.plist` | `4b871122a7cc8f4c4b20f46b03515f429209537fc9c5aa5aa794c16e6cbf1475` | generic child identity |
| `package/plists/Chirality Runtime Service Helper (GPU).Info.plist` | `5d637258aa656f7fc355c7482a67e9cc4971cf0e00f0c4f05405c6245a32e569` | GPU child identity |
| `package/plists/Chirality Runtime Service Helper (Plugin).Info.plist` | `82c90741ba5acb012d8f8a4029c3debbe428d5a440d72c8c45341286d5cce51f` | Plugin child identity |
| `package/plists/Chirality Runtime Service Helper (Renderer).Info.plist` | `2c271d670238327ec784709aca54a15b46e4fff6ed1b88c07b4f907565316245` | Renderer child identity |

Sanitized runtime logs are `raw/desktop-daemon.log` (`3be7915b764dee035ec2a33d57c14fdac66c92373d14c22f623b9672a49f73b5`) and `raw/desktop-main.log` (`3c9ca281da3ac124dd0eb2ac5e894e21f68de71de68d40e6380ae4ec01faa44a`). No secret markers or token contents are present.
