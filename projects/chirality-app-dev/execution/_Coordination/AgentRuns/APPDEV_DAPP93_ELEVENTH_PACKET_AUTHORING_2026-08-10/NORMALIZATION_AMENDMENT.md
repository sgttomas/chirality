# Normalization amendment — eleventh-lineage blocked evidence

Status: `OWNER-AUTHORIZED MECHANICAL NORMALIZATION; NO SEMANTIC EFFECT`

The owner authorized removal of exactly one surplus terminal LF from each of
the 14 files below. For every row, the pre-repair bytes ended `0A 0A`; the
post-repair bytes equal the pre-repair bytes with only the final `0A` removed,
retain one terminal `0A`, and are exactly one byte shorter. Existing hash
citations inside preserved records were not edited. This amendment keeps both
the cited pre-repair identity and the normalized identity resolvable.

Pre-normalization `FINAL_INVENTORY.sha256` SHA-256:
`93259081631b715fa97866b5b7a4845e215443b8bb9b15ac9c8739806da5edd4`.

| Path (run-root relative) | Bytes pre → post | Pre-repair SHA-256 | Post-repair SHA-256 |
|---|---:|---|---|
| `ACTIVATION.md` | 1413 → 1412 | `41e7c20cef11a2dea3f1e634f4baa83fe33813f377cb60246bde46338b96103d` | `193d1f55a01aac195798a0cfa54dd69fe9d867b6bccb6da527c9a320068bf47e` |
| `ELEVEN_LINEAGE_CAUSAL_ANALYSIS.md` | 2997 → 2996 | `2e88f2b5322acb5833c8155042b4398114dc61877679dad6b6d4948cc0656e59` | `c26b0356ba17cd261d71bd55ba86f378fb832bcb27acc8bd346423cc8a4a70c9` |
| `HANDOFF_STATE.md` | 865 → 864 | `b6a3d711783bf014f4a2ca3b86c42b6f873dbb417fcb010fc7910e52a6b0ccfe` | `137b7245453189587144a121fef45c590dc00ada1480dabcd09699e912f94a6c` |
| `MANAGER_RETURN.md` | 1622 → 1621 | `a87105e297502c951ec61cf7eb0089e1a66cf217ce979935565f6519336edbc1` | `8b8070afd27f88d11c9b29feea1928b6f97ac97cc78b88995ca974a40877bdb5` |
| `RECEIPT_READY_FACTS.md` | 1250 → 1249 | `b959cb4e926f0d5bc1613d34d4daf408fd6350b5797269582cf48c5cdbe0d668` | `f2c1a78af4421205e3801e1de00fb6046569753eaae78791dff2e3fd615f32a1` |
| `RUNTIME_SUMMARY.json` | 753 → 752 | `11a288068471b745895d38f9e535b28d22a3b456784c343cb0ec81fc7d1bb5e7` | `99a645b612a7936a86714ab156ffe3e3fcffccfc50bedebb97af375d8582e7b6` |
| `WORK_GRAPH.md` | 3911 → 3910 | `1c920580720543f7073c290193eeb562be6d89b78ebec8dcb17e43d1b8c8648f` | `9a6b10a66bfafa1804b51e02d7dee765f6099b61094f2659c72dd006e8932507` |
| `allowlists/HISTORICAL_ROOT_FENCE.txt` | 1217 → 1216 | `9424a4b5f2148156d4c146f9ccf995c0a92ae273d339367ea83b6115aa2e086a` | `d25a2ff22ad059462905f38bd447939be064787ce470aae31840a4aef0fa756a` |
| `allowlists/N1_WRITE_TARGETS.txt` | 234 → 233 | `5f7105f7603c4f6f8e58a81e02b5c4d728a36101bb1138206c1320b439f00e0c` | `ebc81b24ee1c8b9358a49ed970a806bc7ef9762e228d28814ac7519b5a4c7be4` |
| `briefs/N1_NO_SHELL_PACKET_AUTHOR_BRIEF.md` | 6155 → 6154 | `43e6690bb6dd063a616b25aa19f160fe17d4d8ba56fa2722d7c3a6b44153efc2` | `26d6a830051794da9daccccb343466760881c51ea6b787276f729306c2701e42` |
| `manager/OBSERVE_PROGRESS.py` | 816 → 815 | `2153300601674fd642b086741e56c3aa4a445e314b3dfe901a645384fe4adde2` | `5f60c2b23c70b03d615acbe89310c36fed12d14d1c8d1488e8fb0a2cea338682` |
| `manager/VALIDATE_PACKET.py` | 3926 → 3925 | `9391f63996b0dc16364bc1f136b4395499dea1095e01f9b117117ff1725d0276` | `183b955ead4cdb50f016f0e908551f7c6d007d8c77e46afb1ee46ada8f4e8ca7` |
| `validation/CLOSEOUT_CHECKS.md` | 1476 → 1475 | `e6575b9f3d8e5215e4c62dea6ab3e2403aa1cc52bd9fd7c4e9b1be8b15adaa5b` | `f351a4d441af660d6eec019bc43f351c2dc3680907c1ea7f26c813813126a539` |
| `validation/MANAGER_VALIDATION_BLOCKED.md` | 2571 → 2570 | `d4b94c8fb54899826fe5b8b58d65177423bebf21084d01d4073c7da59357517f` | `46c520a8f45ca4cbc44850dadd78687a7cb6cd0407c7b174d2c812997123eb5b` |
