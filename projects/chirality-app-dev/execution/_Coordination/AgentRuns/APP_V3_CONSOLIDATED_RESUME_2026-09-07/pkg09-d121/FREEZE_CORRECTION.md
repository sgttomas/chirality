# Post-freeze terminal-manifest correction

Status: `MANIFEST_V3_SUPERSEDED_BY_V4`.

After terminal V3 SHA-256 `80c553fc3e813145562008b739faeaa0501fd0a30246e9a62817b3f9b1c90e03` was communicated, the manager found that five packet members incorrectly made carrier commit/publication a prerequisite for the D121 source increment. The authoritative `pdf-application/OBSERVABILITY_ADDENDUM.md` and `pkg02-next/D121_GATE_CLARIFICATION.md` state that observable applied carrier bytes, checks and run record on the run branch suffice and that D121 requires no separate carrier merge between predecessor and source increment.

The manager corrected the affected wording. Exact pre-correction → current SHA-256 identities are:

- `MANAGER_RETURN_FINAL.md`: `ba5dabf05e1be86f3055110b76f0b1ef9639a58821d1f6e1180129d0b85acdec` → `44bba64505de14f86f09da562f33b6a78bc4390125f337a1a522e8664860756d`;
- `PACKAGED_PROOF_BRIEF.md`: `1642fc376adf71ce073136f6a420e746f1ad432609fbce4dd683ab5906dedde4` → `65777f473e3e9d36010d413af33e31ac00bd04401b900ad15bab54c4189145c9`;
- `PAIRED_SOURCE_FREEZE_REQUIREMENTS.md`: `75eb0bcba7489a480434b39182c7ec11505dbe154cbbd535bd0b90725e8612d5` → `f98e20933e1cb40875da7b9f1c17205977080c9df04fbf795700601a6fbfc06f`;
- `TERMINAL_HANDOFF.md`: `dd85d929db81c4b8adb3306f9e692eece96a0e870906e66a6c1fa92cd1ef63a9` → `60f5ec18bb6bc663533abef3f8e6bb61de5e329322552d9ca30abf564582edf2`;
- `WORK_GRAPH_v3.json`: `05e08023de9f1f410f15338ba6795858760553cf1490ba11ed29e3d94d2832cd` → `358560f0de2d70d433b574232de9490cf8e06c5768d1ea2d6a446a49b22d15f6`;
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`: `885e78c41215bfa62fe9996814b2c224a073afdeca6ff30c698f524b790eb4a7` → `fc19446a2181c8e2145b0834ef54135f684ef9070e9f0dc44cbf2161a7ec363e`;
- DEL-09-06 `_run_records/D121_CARRIER_APPLICATION_2026-09-07.md`: `29c5a82487cc2c19c22a8fe39f4077c2c99e02e9ed26ba9e20e5f7bd19d88176` → `74e3fd1e66001662568c81fc6fd1ed7ae13b2b01805f24f69033ba0ff977e175`;
- `MANIFEST_v3.json`: `80c553fc3e813145562008b739faeaa0501fd0a30246e9a62817b3f9b1c90e03` → `99bdd55d8035bc86d00f3f20ebfa0d8caac52551421ca8545320618174434ad8`.

The current V3 file verifies its listed 26 members but was regenerated after its earlier identity was communicated and is therefore superseded as the terminal publication manifest. Carrier bytes were unchanged. `MANIFEST_v4.json` is the sole current terminal manifest and binds the current packet, this correction record and preserved V1/V2/V3 history.

## Mechanical EOF normalization successor

CHANGE staged the then-current 38-path selection and its real index whitespace check found one extra final blank line in 14 added evidence files. Before normalization, their exact bytes were copied to the excluded read-only derivative snapshot `../pkg09-d121-eof-preservation/`; its manifest SHA-256 is `9dd7737e9152a8ef5b4c9eaaf6bb94067c91b57ecf9fde3212025a47a5f7ab06`. The snapshot preserves the original identities and is not selected for publication.

Each publishable file below changed only by removal of one final LF:

- `CARRIER_APPLICATION_v2.md`: `ff0a4c8c9e62d4196df0c9947dfc1fdbb270faf97a2b5e68d60d9101f86d03be` → `91f83e72a4d1aaf35f199ea863cfd39c1bf638d020174119862a056db978a879`;
- `CHECKS_v2.md`: `ab73cf6223bf9bdc67b2e3044f493b029cdc13306d6e9ee8cc55a924017e68fd` → `3627c531c486935543c1bedd70fc78f7ee95265aec8f24acd2259413772559c8`;
- `MANAGER_RETURN.md`: `0d4b4df090b7dd5f468ec3839d0b2bdfe6cd7ac1cffa989c7b1186dc1732ff14` → `fca5cc7f88f9d8ad67fe9e0caaf0faadef7fb83d711537c8f3abcd4ad8d70cfb`;
- `MANAGER_RETURN_v2.md`: `df92aa8ceb8d8b6694d5cd2348953ba492ff83dfbd6a8e521ff582467eae1cf5` → `934805a2653c3a71d15ad6b2127e3bbec1e8b54ac47e99bc221c9cbd1aa88cd8`;
- `MANIFEST.json`: `7ed9ccf398e3df978422e02079962316380b37feaa0a58c8e860263a68d9d9bc` → `aa1885518b17738423ec9d8bda800700614d4a4aaa252e562e1b0b088c9df90f`;
- `MANIFEST_v2.json`: `1a69b5fc02750cda474e1b4e15e64b0e6371272674a1c5918e26f6ab07caf19b` → `ed44388c466c22857703480dbc477e990cf996ae6bc073e90639d7d06674ceb7`;
- `PREFLIGHT_AND_IDENTITIES.json`: `773853aab965070204e6ee98428e281fe74818d13d84a75294cfc4df35ed16be` → `57cbe8e6dcdc0b4322be8be63c2d9b214aa27adee3cef9437b2675250d48caf5`;
- `PREFLIGHT_AND_IDENTITIES_v2.json`: `08ede4514628d0e7fc359db6eb73a66a4a2ad280cd4213cb3d5457c2cc819919` → `a74bd255d4a61b1f5eae7157db0532dc28f5f02ddd7479cde0f0dabe5272ed43`;
- `REGISTERED_CHECKS.json`: `92b68776bc7a496900f385225bb08d47481da3ae77485586c6f455668eb05f52` → `6bc67578fc70b5cfdd92efae552f6a956c46f872ebb44976583815a71dafd2a1`;
- `V1_FAILURE_NOTICE.md`: `698b4600b21abc64e704f84990680ff7b1d083aa13e4bd3e402ff89b10d2090c` → `4d0dbfeba20a6cab761e18f96a3415cc8bbd27e7dd3f047c038149ad7420c077`;
- `WORK_GRAPH.json`: `1a0b6452c50f78e5876155ba90bcf4dabaf3484d93f7ee67eb3d8e28f28721f0` → `31e47fca6e533c3b47c0ee56af9f199c117854e3fcd971428a12368b0dd6ee78`;
- `WORK_GRAPH_v2.json`: `9ab583e26654d1ec6fd4d4d495312e435f9434addcf5fb894793bd4ee3030641` → `48c2bb7f412f4657d8e9e878a036ef7b88308f8256e9d3a27bfdeae1d584ef41`;
- `application-v2/APPLICATION.json`: `48b189fddd6b7d250409852793baf228d40a88beb273b592ac6677e5d2755203` → `0220be9f5572081dd62afbe542fdb65652c17a9ad2abdee5e16717a2fa1a94cf`;
- `review-v1/SEALED_BRIEF.md`: `0fb1da03c251c8a6bb48ddaba7a0ca9bd2e6715dc0850c0935478f89fb08c6ac` → `5d0c8653487fd14e95baeb9326b0c9e7593c8f53803d7d34d82d429e13cff608`;

The nested `review-v1/MANIFEST.json` sealed-brief reference was refreshed to the normalized `SEALED_BRIEF.md` hash. V1/V2/V3/V4 artifacts remain selected as historical evidence; `MANIFEST_v5.json` is the sole current terminal binding after normalization. Carrier and Receipt-261 bytes were not changed in this mechanical cycle.
