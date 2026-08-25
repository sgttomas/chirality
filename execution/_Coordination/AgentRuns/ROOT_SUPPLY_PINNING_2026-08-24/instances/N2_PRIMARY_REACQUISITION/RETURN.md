# Return — N2 Primary Reacquisition and Inventory

- **Status:** `PASS`
- **Verdict:** `PASS_UNDER_R13_AMENDED_SIGNATURE_GATE`
- **Primary archive:** `71843308` bytes; SHA-256
  `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032`;
  exact official `rust-v0.149.0` match.
- **Primary binary:** arm64 Mach-O; `179721344` bytes; SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`;
  exact R13 match.
- **Signature:** exact R13-admitted class—Team `2DC432GLL2`, hardened
  runtime, strict modified-signature failure, invalid-entitlements warning,
  and `spctl` exit `1`. No additional signature disagreement.
- **License:** exact-tag Apache-2.0 text, `10926` bytes, SHA-256
  `d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc`.
- **Notice:** exact-tag notice, `242` bytes, SHA-256
  `9d71575ecfd9a843fc1677b0efb08053c6ba9fd686a0de1a6f5382fd3c220915`.
  The primary archive contains neither file; future redistribution must add
  and carry the applicable license/notice obligations.
- **Execution:** none; N2 never ran vendor code.
- **Quarantine:**
  `/private/tmp/chirality-root-supply-r14-primary.lTtHP2`; external,
  untracked, and retained intact for N2b/N3.
- **Evidence:** candidate `02_SUPPLY_INVENTORY_PRIMARY/` and instance
  `COMMAND_RECORD.md`.
- **N2b gate:** `RELEASED` for only the two exact R13 equivalence assets.

## Durable output hashes

| Output | SHA-256 |
| --- | --- |
| `02_SUPPLY_INVENTORY_PRIMARY/LICENSE_AND_REDISTRIBUTION.md` | `2ae42de7c8ea0dd387e38d029ebb7d622d91c99e6e5908730baae5bbc6ba67a2` |
| `02_SUPPLY_INVENTORY_PRIMARY/PRIMARY_SUPPLY_INVENTORY.md` | `86a0daa9c513e5bb8178f013a3e0a2f3f3e198d59499a777d43a9ea449bd1756` |
| `02_SUPPLY_INVENTORY_PRIMARY/PRIMARY_SUPPLY_MANIFEST.json` | `284068b5f1c5946641105fd2794ceea50bc989e0b52ce15211b35887f2ecc8bb` |
| `02_SUPPLY_INVENTORY_PRIMARY/SIGNATURE_INSPECTION.txt` | `dc7f00255ac91ebbcf0546a110152e2ce15f4dc8261bb3e713aa381c660fea9d` |
| `instances/N2_PRIMARY_REACQUISITION/COMMAND_RECORD.md` | `bde0f7a9d59c6619c6f67033fa22be8ce815ca0bdc1ceff1c4764371d326d8ad` |
| `instances/N2_PRIMARY_REACQUISITION/STATUS.json` | `2dd5e66527e2f601a466fbdcb520c346eb698d5900878dab98bbabf65716a770` |

No G2 acceptance, pin amendment, installation, cutover, implementation,
publication, or reliance claim is made. The invalid vendor signature remains
the named R13-B G5 open finding.
