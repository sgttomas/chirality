# Repair lineage — PR #632 record-only whitespace repair

## Frozen basis

- HEAD: `85caafd4882a2ffff204ed87334171608ce462be`.
- Frontend tree: `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- Controlling diagnostic: exactly 12 flagged paths.

## Markdown preimage

`instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md` was 16,439 bytes with SHA-256 `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`. Lines 23–25 each ended in exactly one U+0020 byte followed by LF. The authorized mutation removes only those three U+0020 bytes.

## Raw-log preimages

| Raw path under `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/` | Bytes | Preimage SHA-256 |
| --- | ---: | --- |
| `desktop-pack.full.log` | 15,852 | `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2` |
| `app_hold.log` | 40,411 | `385349664ef768432fe29b77187ffedfd01a02c1ea4c6a9682b71fed9c7ada14` |
| `corpus.log` | 671 | `c7a8e08208ccd784d3d548e4b19cd9e4458927b081490d2261ece8383d971dd4` |
| `focused.log` | 265 | `86763a2fc84d86f34ff2aadd64d6eed010f7a1a15f3e0b378f368965622eed27` |
| `npm-test.local-socket-cure.log` | 487 | `ec482e01748d566159a0886fa84f455a10200c06ef0cc0c890177bf9bea1cf8b` |
| `npm-test.sandboxed.log` | 9,888 | `b0e940374fc41342b2ca00bf9cee98187320c6559ca1b06321e427ecfc72eda2` |
| `package_verify.log` | 991 | `e3c37d4378ff23fae6cb6f2c0abc77126a9c3f2d3c6fbe067888a4f0c6811034` |
| `pytest.log` | 422 | `e37aea43f5848789f77a4943204636989b97f3bc292ff832d9fee520d4580c73` |
| `receipt.log` | 165 | `4a31bf4f8309774e5a867718d8c267a06eb51477331b57abe1267abb839e969c` |
| `self_check.log` | 21,501 | `ad40c223a005f0cc4a58348b0a74c876b3d5126e391f6df165e59178f38d991f` |
| `typecheck.log` | 137 | `6be4cb0a247e09985e6ce57668de3c06547f0a4e2400e257eae36da4584208a2` |

Each raw file is replaced by same-name `.gz` using deterministic `gzip -n -9`. Each compressed member must decompress to the exact byte count and SHA-256 above before the raw deletion is accepted. Gzip byte counts and SHA-256 identities are recorded after mutation.

## Verified postimages

`instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md` is 16,436 bytes with SHA-256 `253819ca75533f6c0f46f9844ea1641f16e694a51ed3e4fffd9bb80b9f0afb55`. Its Git diff contains only the three line replacements caused by removing exactly one terminal U+0020 from each of lines 23–25; all other bytes are unchanged.

| Gzip path replacing the raw name | Gzip bytes | Gzip SHA-256 | Recovered bytes / SHA-256 |
| --- | ---: | --- | --- |
| `desktop-pack.full.log.gz` | 3,205 | `fd7e8acb7e7305f95f26acbfcd1e753aee426470cbbcf8ee4feefc4193b16d9f` | 15,852 / `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2` |
| `app_hold.log.gz` | 2,559 | `6c584837c0b717d1abe7000afbb3cb78fe44f4a61d1f157a0d5555851aff6736` | 40,411 / `385349664ef768432fe29b77187ffedfd01a02c1ea4c6a9682b71fed9c7ada14` |
| `corpus.log.gz` | 295 | `0cdc8e9440312aafd4d4acb425a5735a0b55b8e41446b22449542a15174fa4e2` | 671 / `c7a8e08208ccd784d3d548e4b19cd9e4458927b081490d2261ece8383d971dd4` |
| `focused.log.gz` | 213 | `72417f76a8b54260b0a7712126f5f97ebed3f98375fe1dc8f26ca187f033c740` | 265 / `86763a2fc84d86f34ff2aadd64d6eed010f7a1a15f3e0b378f368965622eed27` |
| `npm-test.local-socket-cure.log.gz` | 357 | `e80951a26ec9a9dd585cb10ebb78489b4f5af5d5eb898daa556728b1979f7dd6` | 487 / `ec482e01748d566159a0886fa84f455a10200c06ef0cc0c890177bf9bea1cf8b` |
| `npm-test.sandboxed.log.gz` | 1,915 | `13f4045727837e961bca36e4d103f5e4c06a1c077fd03d622bcb957abe50087d` | 9,888 / `b0e940374fc41342b2ca00bf9cee98187320c6559ca1b06321e427ecfc72eda2` |
| `package_verify.log.gz` | 438 | `2f4805ee7244eef447236686846abbdc722981467fd5c6961a396546d4284130` | 991 / `e3c37d4378ff23fae6cb6f2c0abc77126a9c3f2d3c6fbe067888a4f0c6811034` |
| `pytest.log.gz` | 78 | `9da9f969aac25188a54c2aa4615ddc3d760358cb355e121ce6b88683309905f2` | 422 / `e37aea43f5848789f77a4943204636989b97f3bc292ff832d9fee520d4580c73` |
| `receipt.log.gz` | 159 | `d5ff2bcc0730027a9a8d35efd85c1ab885ccbdc2ba5576b68e4a16cbaa03cb80` | 165 / `4a31bf4f8309774e5a867718d8c267a06eb51477331b57abe1267abb839e969c` |
| `self_check.log.gz` | 3,214 | `3bb314b0d6286700ba121ab60b603af69a481b26af9646569d5ff55173fb0829` | 21,501 / `ad40c223a005f0cc4a58348b0a74c876b3d5126e391f6df165e59178f38d991f` |
| `typecheck.log.gz` | 115 | `f9661075529f176c6eb5fdde1be19620195c7a18af02f96962a98c1f2b9f4774` | 137 / `6be4cb0a247e09985e6ce57668de3c06547f0a4e2400e257eae36da4584208a2` |

For every row, the raw source path is absent, the `.gz` path is a regular file, `gzip -t` exits `0`, and `gzip -cd` reproduces the frozen byte count and SHA-256. The compressed names are deterministic: `gzip -n` stores neither the raw filename nor timestamp.
