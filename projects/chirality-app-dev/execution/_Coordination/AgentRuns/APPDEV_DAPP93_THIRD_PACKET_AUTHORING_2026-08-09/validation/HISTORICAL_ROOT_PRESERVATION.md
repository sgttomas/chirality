# Historical blocked-root preservation — baseline

Baseline: `da40d7dc4192c9aa2f49e9438729179aae281b61`

The following roots are excluded from all authoring reads and writes. Their
Git tree identities and SHA-256 digests of byte-sorted `git ls-tree -r
--full-tree HEAD -- <root>` output are the preservation controls.

| Root | Git tree | Files | Blob bytes | Inventory SHA-256 |
|---|---|---:|---:|---|
| `APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09` | `256c7c43f419afed9ba5120cfc489f09a13c9b3b` | 34 | 119383 | `9a15948e7587545c3e079edf1c92f764ff8743d4f326bcf80e1e4feef2365b8c` |
| `APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_V2_2026-08-09` | `801c94300f44fd816a5fc059f0afbdab6f78eab4` | 20 | 89845 | `fb69594e1d43a93adcf4ade0b9dce2c2166b38f4a1cba2dfea421629ca6cad17` |
| `APPDEV_DAPP93_FRESH_PACKET_AUTHORING_2026-08-09` | `1298c1c8f34de361cf7f0e882c7723e0cc68dbb7` | 10 | 26099 | `ab688f21e0594f239097906441ce6bef097c60a55e77e10bcb13d888189252b2` |

Before child dispatch, `git diff --quiet HEAD -- <root>` returned zero for all
three roots.

Only these terminal blocked records may be consulted by the manager for
preservation and, only if this lineage blocks, the required three-failure
causal comparison. They are not authoring sources and are excluded from every
child read scope:

- attempt-3: `SUCCESSOR_HANDOFF_STATE.md`,
  `SUCCESSOR_MANAGER_VALIDATION_BLOCKED.md`;
- attempt-3 V2: `HANDOFF_STATE.md`, `MANAGER_VALIDATION_BLOCKED.md`,
  `RUNTIME_SUMMARY.json`;
- fresh lineage: `HANDOFF_STATE.md`, `MANAGER_VALIDATION_BLOCKED.md`,
  `MANAGER_RETURN.md`, `RUNTIME_SUMMARY.json`,
  `validation/OLD_ROOT_PRESERVATION.md`.

No other byte in these roots is an allowed read for this activation.

## Terminal preservation recheck

After N1 stopped, all three committed tree identities, file counts, blob-byte
totals, and inventory SHA-256 values reproduced exactly. `git diff --quiet
HEAD -- <root>` again returned zero for each root. N1 made no write to any
historical root.

N1 nevertheless reported a read-scope violation: one broad Stage 3 `rg -l`
content search had ineffective exclusion globs and searched files in all three
roots. No matching content was displayed, cited, copied, or used. The roots
are byte-preserved, but the sealed absolute read exclusion was violated; the
lineage is therefore blocked and no downstream node was released.

This absolute read exclusion was imposed by HELP_HUMAN/WORKING_ITEMS as a
stricter operational fence. The owner direction prohibited resume, copy, and
repair of prior drafts but did not explicitly prohibit every read. The search
therefore violates the sealed child brief; it does not establish that the
owner's stated non-reuse requirement was violated.
