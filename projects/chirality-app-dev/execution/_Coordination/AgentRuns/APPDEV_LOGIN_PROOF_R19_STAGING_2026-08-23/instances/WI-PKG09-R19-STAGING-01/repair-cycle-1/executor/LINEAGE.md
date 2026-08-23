# R19 repair-cycle-1 lineage

## Frozen preimage

- Original log path:
  `instances/WI-PKG09-R19-STAGING-01/executor/desktop-pack.full.log`
- Required preimage bytes: `6737`
- Required preimage SHA-256:
  `a15031aa4ae1dc640075409858eb0c8e7602858fa0f49c5115b0ac244162bec6`
- Deterministic `gzip -n` preimage:
  `repair-cycle-1/executor/preimages/desktop-pack.full.log.gz`
- Gzip bytes / SHA-256: `2127` /
  `b9ba318019fbd8bb6565c6c463df6cddd823ab04a16e0f10e25bd5e86c287c52`
- Decompressed bytes/hash match the required preimage exactly.

## Original transcript source

- Retained original R19 execution event ID:
  `exec-df1a0a3b-c9af-4dc0-b3fa-b3836070813a`
- Event timestamp: `2026-08-23T06:21:41.991Z`
- Original tool stdout bytes: `15638`
- Exact matching raw field count in that event: `1`
- Recovered field bytes: `9588` including its terminal LF
- Recovered field SHA-256:
  `0f1611f07c7a52900d89bd60f8702986555435a632305542e73b400f29e155b3`
- Field begins with exact Electron Builder prefix
  `  • duplicate dependency references  dependencies=[` and ends with the
  original dependency array plus one LF.

The field was read from the retained actual R19 output event. It was not
regenerated, approximated, inferred from another build, or produced by a pack
rerun.

## Exact replacement proof

- Suppression-marker offset in preimage: `4693`
- Marker bytes: `227`
- Prefix bytes / SHA-256: `4693` /
  `87e9bf6a4a5030db4064423b61452c527702c0db40268566ffaf016e3927dea4`
- Suffix bytes / SHA-256: `1817` /
  `88b7ba67b0b63a7224c90c42c5d6ba4567b60bd0c397ada84bd4578cb82f612a`
- Restored log bytes: `16098`
- Restored log SHA-256:
  `2c0229474bad89dce1ced7e1303a2cd5b5bff0d0df3624dd5cd850baf1cb2db8`
- Prefix identity: exact
- Suffix identity: exact
- Suppression-marker count after repair: `0`
- Exact recovered-field count after repair: `1`

Only the preimage marker bytes were replaced by the exact original field.
