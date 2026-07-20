# V3 D-APP-70 Format-Binding Backcheck Report

## Verdict

`ACCEPT`

The exact R4 repair is nonsemantic, internally closed, and contained. The
earlier CHANGE count of 14 remains a preserved unresolved historical
observation; current evidence proves exactly 13 diagnostic locations across
ten files and does not support an invented fourteenth location.

## Basis and current anchors

- Basis/HEAD: `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`
- R4 RETURN / STATUS / HANDOFF:
  `3f466b9d95a9967dc8e1eac81defb884c4d6ee6821f74dd1df7c1099d759bf84` /
  `568f71392021ed1353b4bcff5c17a29763f75b0430230a5ea2d8362ba1c6fba6` /
  `f520e4fe67dcab28561ee2c22c23204adfc2aeae9fdd1ace5c05d9b608ba12e1`
- W1 RETURN / STATUS:
  `4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38` /
  `fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655`
- V2 RETURN / STATUS:
  `8bd93871ef167c283204e135b5a88e7106de279f498a11c4138406eecd043874` /
  `d1c54e2276129cc4930dd6433b556a26ed7041147294ed92662701a85d92a5c3`
- Applied MANIFEST / HANDOFF:
  `40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e` /
  `388effec0ce63d606d2707dc59ba4a52d68efcff18553bc7043fcd2787c01c94`
- D-APP-71 packet / register / Receipt ledger:
  `711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c` /
  `3eb0a430bc98c43b4b7f2b6603d1f186ec679bc44685cb80ea1350aed96828c5` /
  `7e5b6baa046fac24bebbf3990378bd596647410b2c974eab7cd91166392eebc4`

## Exact 17-transition reconstruction

For every current file, V3 independently replaced only graph-declared new
hash tokens with their old tokens, then reversed only the declared whitespace
repair. Every reconstructed byte stream reproduced the old SHA-256 exactly.

| Surface | Old SHA-256 | Current SHA-256 | Reversed token occurrences | Whitespace class |
|---|---|---|---:|---|
| V2 RETURN | `d7a469edf8e96a15d035ea5453be53df3ba52d0f0c0945c706e7821cafdf5160` | `8bd93871ef167c283204e135b5a88e7106de279f498a11c4138406eecd043874` | 8 | one terminal LF |
| Application brief | `aef7d7b87df7ea61c71ce69171dd6e633a0c0b53178ac69e8e00a3a33ec4c0ed` | `47e12e5dcd517d12086cbea9b3594c0ca248c5d7bb46369b1cb9d21ca0bbb78d` | 0 | one terminal LF |
| Application return | `625c1dbfe05560178070863e18464946f2c2e8447332cbaab8b16d0a2630f896` | `63041440b1745061f779293c1e9f305046268366304de1d1ae3c68572e04194d` | 0 | one terminal LF |
| Governance brief | `bf066469b86ab43c1521a0ec998294a089b13b98dd47d6fa9417a833807d7ab7` | `1751f7b9da0b5f9e179760ae0b321e885213e42cee9b00ff1b190da53390883a` | 0 | one terminal LF |
| Governance return | `25ee7c56e438b34ea1e02fbffcc75937b5fa44775e12baf4700af97b00f20cd3` | `1bf0849b6e2b12604135d1493130f9156611b77a69b9ecadad1ba2f9d1e87952` | 5 | one terminal LF |
| D-APP-71 packet | `b0c5f227be6c87b11fe280a4912fc1a0d6efb3500f6488691ef3214a497e2eb6` | `711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c` | 0 | two spaces on each of lines 3–6 |
| V2 protocol | `eee60bc8e5d78809228fc771bd73cb5368d6c17b3f517609f87140a470511a8c` | `c756daae95042bbcad832593d23f0b0db88442a11dd418626b2f0aa2dee94054` | 0 | one terminal LF |
| V2 report | `46d26d9818d8a026fc8d52edb93fcf44e268ef997eb3d99eff9244a120911772` | `7bcc83e4d88434933177b8958305cbae94b1f26c769b03afbc351021b7efbd17` | 5 | one terminal LF |
| V2 findings | `451044943ffd5b56c340b6bf271592b84747285bb84272820a1b3c734e61a528` | `621f3f6665cd97a573058112de8c4848342470b1b289f24e48ff5f4511bbc97c` | 0 | one terminal LF |
| V2 handoff | `957cce6026fdbf6a3d32291bb65fad0048bc72ae25ac3436164bf320c6be3078` | `5edc7a9e042abd300033687742e749a42a5a0525e4e5a369fc6928519e4f436b` | 0 | one terminal LF |
| Applied handoff | `41540480d8011942668ae4fa9976482cb30fd2814852b5e74d9b8ec5b2e86cec` | `388effec0ce63d606d2707dc59ba4a52d68efcff18553bc7043fcd2787c01c94` | 1 | hash tokens only |
| Applied manifest | `eac0ec145d33e55c0ce5dbfe066223812a790183ae33ef7e4c33c27bd408e39c` | `40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e` | 2 | hash tokens only |
| Receipt ledger | `4b0eb0dc88c02e0c856a225fccf5f00385258cfc567e8adbc8ba0140e91740eb` | `7e5b6baa046fac24bebbf3990378bd596647410b2c974eab7cd91166392eebc4` | 2 | hash tokens only |
| W1 handoff | `19c2593e2202782d3d62e4987f5e3ea0bc9bf53fb2026a987c6f2663a09908f1` | `097b0744eeda3414e31914f682a810d2716567eb4ffb432c2ddbe2ad2974b363` | 4 | hash tokens only |
| W1 return | `5811a5a94b39596f9e8244cc4c8ac631de87438a8e940c2b9f66d9985df4cc98` | `4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38` | 6 | hash tokens only |
| W1 status | `19d56061817027452a46b97ac143b0b6d24a241d0b4e4c1c33ee334ac0cff566` | `fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655` | 3 | hash tokens only |
| V2 status | `2293506289ce27637a673680902555fb6f0139573299fe8ac79f3618eacdf22d` | `d1c54e2276129cc4930dd6433b556a26ed7041147294ed92662701a85d92a5c3` | 14 | hash tokens only |

The complete delta is 50 exact 64-hex token occurrences, nine one-byte
terminal-LF deletions, and four two-byte U+0020 deletions. Thus the repair has
13 whitespace locations and 17 whitespace bytes. No other byte changed.

## Population, stale closure, and hygiene

- Pre-v17: 42 paths; hash
  `d2365880b7639a9c6465b38468d4787c3c1b33bc416705b96913fbb174d27438`.
- Pre-v18: 48 paths; hash
  `2b735dadd409ff52ed45ef1b211fc1e59c6a32447c8ba6e58440853901b0c10f`.
- V3 launch: 52 paths; hash
  `1d2ce8386d8cba1d691f7bbbb3c7ce9a56e808ea26a7cb74029a51bd1999431c`;
  pre-write content aggregate
  `6ec2b18ba4a44fe8b33dd9a63264d2a8fec79621009eb71b01b06a8d90d48281`.
- Superseded-token scan: 61 occurrences in eight authorized historical
  controls only, including the explicit v16 section of HANDOFF_STATE; zero
  stale current-cluster occurrences.
- Individual no-index checks: 52/52 launch paths and 17/17 repaired/transitive
  paths, zero diagnostics.
- Actual worktree, cached, and non-mutating staged-equivalent patch checks:
  exit zero.

## Semantic and state neutrality

The applied package remains seven-file manifest-closed. W1 remains
`APPLICATION_COMPLETE_AWAITING_V2`; V2 remains `ACCEPT`. Mapping remains
22 exact ordered rows in nine groups `5+4+6+1+1+1+1+1+2`, with 21
physical/primary rows, one blank-owner shared-only preload row, four closures,
one narrowed residual, and five local records.

D-APP-71 remains exactly `AWAITING_RULING`, selection null, with no ruling
file and neutral DEL-02-03, DEL-02-05, DEL-09-06, and DEFER options. Receipt-80
is unique/latest, has parent Receipt-79, and reverse reconstruction proves only
its two pointer hashes changed.

Preservation recomputed: 22/22 sources, 5/5 SOWs, 10/10 dependency files,
5/5 statuses, 5/5 local records, 14/14 upstream derivative files, 4/4 R3
surfaces, and 2/2 accepted V1 surfaces. No lifecycle, Approval SHA, source,
SOW, dependency, decomposition, authority, release/publication, hard-fence, or
Git state changed.

## Controls, origin, findings, and handoff

- Strict recursive JSON and CSV schemas: PASS.
- Receipt validator: PASS.
- Authority corpus v9: eight MATCH, no drift.
- Repository self-check: exit zero at existing 3 REVIEW / 6 WARN.
- `origin/main`: `e315fb8406d44dce684cbec091f3174c261efee4`; 90-path
  advance, sorted path hash
  `f3f2a523b28a92744637b05b7b363215621733099f152c1b45c5ae3116fbec1f`;
  90/90 paths under `projects/chirality-piping/**`, zero overlap.
- Findings / blockers / unknowns / conflicts / waivers: `0 / 0 / 0 / 0 / 0`.
- Required rerun: none on current bytes; rerun V3 after any bound-byte,
  population, authority, anchor, origin-overlap, or Git-state change.

HELP_HUMAN may consider the repaired tranche eligible for a later separately
released CHANGE handoff. No downstream release or Git action occurs here.
