# V3 D-APP-70 Format-Binding Backcheck Return

## Verdict

`ACCEPT`

The R4 format-and-binding repair passes fresh independent evaluation. This
permits only HELP_HUMAN consideration of a later separately released CHANGE
handoff. It does not authorize repair, D-APP-71 selection, downstream release,
or Git action.

## Exact reconstruction and discrepancy

V3 independently reconstructed all 17 preimages from current bytes. The exact
old-to-current transitions are:

```text
d7a469edf8e96a15d035ea5453be53df3ba52d0f0c0945c706e7821cafdf5160 -> 8bd93871ef167c283204e135b5a88e7106de279f498a11c4138406eecd043874
aef7d7b87df7ea61c71ce69171dd6e633a0c0b53178ac69e8e00a3a33ec4c0ed -> 47e12e5dcd517d12086cbea9b3594c0ca248c5d7bb46369b1cb9d21ca0bbb78d
625c1dbfe05560178070863e18464946f2c2e8447332cbaab8b16d0a2630f896 -> 63041440b1745061f779293c1e9f305046268366304de1d1ae3c68572e04194d
bf066469b86ab43c1521a0ec998294a089b13b98dd47d6fa9417a833807d7ab7 -> 1751f7b9da0b5f9e179760ae0b321e885213e42cee9b00ff1b190da53390883a
25ee7c56e438b34ea1e02fbffcc75937b5fa44775e12baf4700af97b00f20cd3 -> 1bf0849b6e2b12604135d1493130f9156611b77a69b9ecadad1ba2f9d1e87952
b0c5f227be6c87b11fe280a4912fc1a0d6efb3500f6488691ef3214a497e2eb6 -> 711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c
eee60bc8e5d78809228fc771bd73cb5368d6c17b3f517609f87140a470511a8c -> c756daae95042bbcad832593d23f0b0db88442a11dd418626b2f0aa2dee94054
46d26d9818d8a026fc8d52edb93fcf44e268ef997eb3d99eff9244a120911772 -> 7bcc83e4d88434933177b8958305cbae94b1f26c769b03afbc351021b7efbd17
451044943ffd5b56c340b6bf271592b84747285bb84272820a1b3c734e61a528 -> 621f3f6665cd97a573058112de8c4848342470b1b289f24e48ff5f4511bbc97c
957cce6026fdbf6a3d32291bb65fad0048bc72ae25ac3436164bf320c6be3078 -> 5edc7a9e042abd300033687742e749a42a5a0525e4e5a369fc6928519e4f436b
41540480d8011942668ae4fa9976482cb30fd2814852b5e74d9b8ec5b2e86cec -> 388effec0ce63d606d2707dc59ba4a52d68efcff18553bc7043fcd2787c01c94
eac0ec145d33e55c0ce5dbfe066223812a790183ae33ef7e4c33c27bd408e39c -> 40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e
4b0eb0dc88c02e0c856a225fccf5f00385258cfc567e8adbc8ba0140e91740eb -> 7e5b6baa046fac24bebbf3990378bd596647410b2c974eab7cd91166392eebc4
19c2593e2202782d3d62e4987f5e3ea0bc9bf53fb2026a987c6f2663a09908f1 -> 097b0744eeda3414e31914f682a810d2716567eb4ffb432c2ddbe2ad2974b363
5811a5a94b39596f9e8244cc4c8ac631de87438a8e940c2b9f66d9985df4cc98 -> 4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38
19d56061817027452a46b97ac143b0b6d24a241d0b4e4c1c33ee334ac0cff566 -> fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655
2293506289ce27637a673680902555fb6f0139573299fe8ac79f3618eacdf22d -> d1c54e2276129cc4930dd6433b556a26ed7041147294ed92662701a85d92a5c3
```

The byte delta is exactly 50 authorized hash-token occurrences, nine one-byte
terminal-LF deletions, and four two-byte trailing-U+0020 deletions on D-APP-71
packet lines 3–6. That is 13 diagnostic locations across ten files and 17
whitespace bytes. No other byte, prose, field, option, order, count, verdict,
or state differs. The prior CHANGE count of 14 is preserved unresolved; no
fourteenth location or eleventh file is inferred.

## Anchors, populations, and neutrality

- Current W1 RETURN/STATUS:
  `4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38` /
  `fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655`.
- Current V2 RETURN/STATUS:
  `8bd93871ef167c283204e135b5a88e7106de279f498a11c4138406eecd043874` /
  `d1c54e2276129cc4930dd6433b556a26ed7041147294ed92662701a85d92a5c3`.
- Applied MANIFEST/HANDOFF:
  `40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e` /
  `388effec0ce63d606d2707dc59ba4a52d68efcff18553bc7043fcd2787c01c94`.
- D-APP-71 packet/register/Receipt ledger:
  `711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c` /
  `3eb0a430bc98c43b4b7f2b6603d1f186ec679bc44685cb80ea1350aed96828c5` /
  `7e5b6baa046fac24bebbf3990378bd596647410b2c974eab7cd91166392eebc4`.
- Populations: 42 pre-v17, six v17/R4 controls, 48 pre-v18, four v18 new
  controls, 52 at launch. Exact sorted hashes respectively
  `d2365880b7639a9c6465b38468d4787c3c1b33bc416705b96913fbb174d27438`,
  `2b735dadd409ff52ed45ef1b211fc1e59c6a32447c8ba6e58440853901b0c10f`,
  and `1d2ce8386d8cba1d691f7bbbb3c7ce9a56e808ea26a7cb74029a51bd1999431c`.

W1 remains `APPLICATION_COMPLETE_AWAITING_V2`; V2 remains `ACCEPT`;
D-APP-71 remains `AWAITING_RULING`, selection null, with the same four neutral
options and no ruling file. Receipt-80 remains unique/latest with parent 79;
only its two pointer hashes changed. Mapping remains 22 ordered rows, nine
groups, 21+1 treatments, four closures plus one residual, and five records.

Preservation passes for 22 sources, five SOWs, ten dependencies, five statuses,
five records, 14 upstream files, four R3 surfaces, and two accepted-V1
surfaces. No semantic, lifecycle, Approval SHA, source, SOW, dependency,
decomposition, authority, release/publication, hard-fence, or Git change
occurred.

## Hygiene, controls, containment, and findings

- Superseded hashes: 61 occurrences in eight authorized historical controls,
  including HANDOFF_STATE's v16 section; zero current-cluster stale references.
- Individual no-index checks: launch 52/52 and repair set 17/17, zero
  diagnostics; V3 outputs also checked individually at closure.
- Actual worktree/cached and staged-equivalent patch checks: PASS.
- Strict recursive bound/new JSON and CSV schemas: PASS.
- Receipt validator, authority corpus v9 (8/8 MATCH), and self-check (existing
  3 REVIEW / 6 WARN): PASS.
- Origin `e315fb8406d44dce684cbec091f3174c261efee4`: 90/90 piping-only paths,
  sorted path hash
  `f3f2a523b28a92744637b05b7b363215621733099f152c1b45c5ae3116fbec1f`.
- Findings / blockers / unknowns / conflicts / waivers: `0 / 0 / 0 / 0 / 0`.
- Required rerun: none on current bytes; rerun after any bound-byte,
  population, authority, anchor, origin-overlap, or Git-state change.
- Final writes: authorized V3 evaluation root and instance only.

## Output hashes

| Output | SHA-256 |
|---|---|
| Evaluation protocol | `7ff4d5433bc20fd5b280832ba36830c11a1ec79a990ecaa65d8a564c4e42ecda` |
| Evaluation report | `03d99cafe3df387b4bc86ff67b4b30521c56dd0b5199ff05a19c7f02ead86856` |
| Findings register | `621f3f6665cd97a573058112de8c4848342470b1b289f24e48ff5f4511bbc97c` |
| Handoff | `0534f473632006e2fc4332ac5864444e769c45cb91b85f0546971da7e2a206ad` |

Terminal STATUS records this return's hash. Self-hashes are omitted because
they are structurally self-referential.
