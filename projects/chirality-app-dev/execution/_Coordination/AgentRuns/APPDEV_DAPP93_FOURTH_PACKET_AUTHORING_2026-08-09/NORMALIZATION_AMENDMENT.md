# Closeout normalization amendment

Owner-authorized mechanical closeout adjustment: remove exactly one surplus
terminal blank line from each file below. No semantic content changed. For
each row, appending one LF byte to the post-repair file reproduces the
pre-repair SHA-256 exactly.

| Relative path | Pre-repair SHA-256 | Post-repair SHA-256 |
|---|---|---|
| `ACTIVATION.md` | `83e3780bba682fd9f61ad0ec91673f3786eb00b770409224ae113c17fd247b2f` | `e294cde5b80bedfda6d3715482c3e2cf22678e56271719f5b38b274fddbd7388` |
| `CAUSAL_ANALYSIS_FOUR_LINEAGES.md` | `108d3b8d9c1876e6b0db63fc04951cbe515c187c968a23cc941e748ea097e616` | `5d7eb4e165175dd621685733b7a89887a0d2d145aca70f804af276ccf1ce6188` |
| `HANDOFF_STATE.md` | `845c534d486ea8b37a40944469a6232708596d583098cd83d9b8688adcbc4ba9` | `75f045baf21a2e636a6b41c3f515064ffe6160e36f51d174f3056e757f72e047` |
| `MANAGER_RETURN.md` | `556950adf9cca5ecf176e322c0666854202e0bc4f07ac492ef2c88098a32e62a` | `ba77dce31a06bcb4d6bd358bada84feff55ec65acb14ad75fc02c4dd1709bcfd` |
| `RECEIPT_READY_FACTS.md` | `97f4cc07ec418d14f96147dc1edb8d34325b462b4b44a0137fedab0c48ef64e0` | `1bdc2f5790a6062d52756889c242994cae8a11ec43ded1c36a11e0772385549f` |
| `RUNTIME_SUMMARY.json` | `4da681bba88c8379d219231b6edef2dc12e913aae4892e70a7f1a335072d8d65` | `a01d355e7cc0852a954af81784e315994c40389ed63f711682a22a3689c3003c` |
| `WORK_GRAPH.md` | `4d5993c0ae4a3f5545de7747e986de205c45a57904a91a15575cea10d8499806` | `f3041ae9fe24e6cc0d606f62186abc6721d05e38c163ba4138fe926549fc00b6` |
| `allowlists/N1_COMMAND_FORMS.txt` | `bcaddc80287d3a5724fbf463dd71e2acf62f29f3055b23cd83cc3e3713b67be4` | `23a4c5559efa70766d16761f2c689083059b2b42097890a5a2ebff9116cc6f6a` |
| `allowlists/N1_READ_ALLOWLIST.txt` | `52ac804af92d0e946099e70a8e9bfd269708a50a3d067d0618ba3b11dbbf8277` | `793be5ff4d6d5b81f18552f1db5f24235caf1a9c6b9abaa3daa8abef60b9a197` |
| `briefs/N1_TAINT_CLEARANCE_BRIEF.md` | `0a53473c4a881e693dceb953211c8440ad97b270d3e97b6ae8fb7b7921c0fdf9` | `6dd4aa9a9217e7282707abd7f5d9fd26128c693087a5d3af2dd030c06c23e85f` |
| `returns/N1_TAINT_CLEARANCE_RETURN.md` | `c4ee40ab3b5d7dbc689a62355b56d85fab05bbb5b2604bd8564906d2adfca81a` | `b829b673f8b489fe82054515fc0c0ec868a66d1ea8194cf26e9b8fd3fbfc2c22` |
| `taint_clearance/STAGE_1_SALVAGE_HASHES.md` | `25ba97175e4113a3a57d589ba2b753846c9e85676d8987ed37044299d380b384` | `0cb136c024f65ba75578624fcd3cfa7f2561eb73629f8be9ba7c5e0d071e665b` |
| `taint_clearance/STAGE_2_IDENTITY_SCAN.md` | `51a22ded86c91ebe030f1fcb599dc6979c020aac8dd2ae33ad1de1156b2793c2` | `4c8510ce353e4332b66cda80adcf8e23e6ec238b20c1450dfccfa8a00084302c` |
| `validation/CLOSEOUT_CHECKS.md` | `1a87dd1f7ae8fbfb46c86ecba09d739fda09cc70b401de06a10b3dff05d3bf21` | `7608eb15a271c263db7d89bb42acad98adcf7e4c5f0cbab73668d6434872ec70` |
| `validation/FOUR_ROOT_BASELINE.md` | `fd7e681e74e996e72e9e6d5242c94f6722ed1df168b489924ee7362712352dcd` | `b60ec2f1a6cd9b1b4bbf3245ef422a22b974ddb01a5c3c4d4be6bdf04b959c83` |
| `validation/MANAGER_VALIDATION_BLOCKED.md` | `95c17d5918195000ec1fb2f13ba062bee41f4881e4100344503b3f1fb2ac119d` | `6f0fb73a781184f4885196e9c6e94d11744df01592e73ebc6680f116d059612f` |
| `validation/N1_PRE_DISPATCH_PREFLIGHT.md` | `7c1aea636b125154b10271fbf7c8ef01ed6a7ab3dd9491940cbd0bab4b560147` | `ef5ffb3ab96ab13230b4a0a6f435149c60164dac7e49f889fd56f2e7d760fa4f` |

Embedded and pre-existing hash citations inside the preserved records remain
intentionally unedited. When such a citation names a pre-repair identity, this
amendment is the authoritative normalization map to the current post-repair
identity. The substantive manager verdict remains
`BLOCK_N1_PREVALIDATED_COMMAND_FORM_NOT_EXECUTABLE`; no taint PASS, packet,
freeze, verifier, approval hash, execution authority/action, or fifth lineage
is created by this normalization.
