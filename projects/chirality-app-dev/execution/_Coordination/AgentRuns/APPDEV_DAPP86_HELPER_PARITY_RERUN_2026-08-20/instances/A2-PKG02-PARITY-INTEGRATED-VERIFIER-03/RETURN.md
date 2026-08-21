# A2-PKG02-PARITY-INTEGRATED-VERIFIER-03 return

Verdict: `REJECT_REPAIRED_FAN_IN`

Scope: fresh read-only V3 verification of the frozen integrated-review repair.
No repair, test, build, app, daemon, UI, launcher, product, deliverable, shared
surface, or Git action was performed. This return is the verifier's only
write. No `STATUS.json` was created.

## Blocking finding

`F1 — RECEIPT / CONTAINMENT CONTRACT FAILED`

Acceptance criteria 7 and 8 do not hold in the verified current state.
`git diff --name-only` reports the tracked path
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, outside this run root.
Relative to frozen HEAD `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`,
the diff adds Receipt 183 at current lines 5477–5486. That receipt explicitly
records this D-APP-86 helper-parity rerun and points to this run root.

- Current receipt-ledger SHA-256:
  `d6669149906f546993753b22d700e26d3b1e435ab36382ca257ae81bcba49767`.
- HEAD receipt-ledger SHA-256:
  `2d44c7bbc0d82b11a720352142aaaebcd0bf746370c03b9103db75c91d1d9489`.
- HEAD contains no Receipt 183; the working-tree diff adds it.
- No staged diff exists. The only tracked working-tree diff is this receipt
  ledger; the run root is otherwise untracked.

This verifier does not infer who wrote the receipt or when. The observed
current-state fact is sufficient: Receipt 183 is not untouched, a path outside
the run root changed, and the repaired records' no-receipt/shared-surface-effect
contract is therefore false. Because every acceptance criterion is mandatory,
the otherwise-valid repaired fan-in must be rejected.

## Frozen-byte verification

All eleven required frozen hashes match:

| Artifact | Checked SHA-256 | Result |
|---|---|---|
| Manager `RETURN.md` | `3c68a8d060e13e4e7c9d085e172ff6bcb95b1e4eb3255073bc8d028a13a9270b` | PASS |
| `CLOSEOUT_AMENDMENT_01.md` | `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7` | PASS |
| `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md` | `6ada335fab940c9c9265a37fa2d042fba94beff8a8f0a66df1a28c9d12e812a8` | PASS |
| `EVIDENCE_INDEX.csv` | `9cc9a80452c5b684d453adf23986f937eebbe582a2a67023fa27fc74f199fbf1` | PASS |
| `STATUS.md` | `127f5b9b0c02842571c3f22d5a3b7432c507def9af421c7622387599b919e3af` | PASS |
| `HANDOFF_STATE.md` | `da113537fa4999ef15a864ee4d1777ab9646c6b75c2363d576929deb8b5c772c` | PASS |
| `REGISTERED_CHECKS.json` | `a99a5b6d9b83fecc43f35707f120c668271c018174886193ac876e2e7b1259b0` | PASS |
| `RUNTIME_SUMMARY.json` | `738d5889e9ba81f1cda64779e23a1afcdb2e7ebdd3195febd3a2548847ab851c` | PASS |
| E1 `STATUS.json` | `b175bf31f92883f52e11fe6cdae32fa01b6a8e559cdcdd2e905bf85b2ef9256e` | PASS |
| V1 `STATUS.json` | `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1` | PASS |
| V2 `STATUS.json` | `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832` | PASS |

`EVIDENCE_INDEX.csv` parses as exactly six columns with 22 data rows. All
22 paths resolve under the run root and every indexed SHA-256 matches.

## Status, registered-check, and runtime verification

- E1, V1, and V2 use `chirality-agent-instance-status/v1`, are terminal, and
  bind exact immutable return hashes:
  - E1: `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9`,
    outcome `BLOCKED / PARTIAL`.
  - V1: `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21`,
    outcome `ACCEPT_BLOCKED_FAN_IN`.
  - V2: `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e`,
    outcome `ACCEPT_AMENDED_FAN_IN`.
- `REGISTERED_CHECKS.json` is valid JSON, uses
  `chirality-software-check-evidence/v1`, and exactly binds HEAD
  `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, tree
  `fe8ece104dd281e3219bd95fa8b121437d524520`, and branch
  `codex/app-dapp86-helper-parity-rerun-20260820`.
- Its focused-test, typecheck, build, desktop-pack, fixture, and packaged-UI
  proof hashes match respectively:
  `1aae3ff66b7afd86d99c54eef10aa12f34e726ad1ab7f48da00a039126f7db46`,
  `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f`,
  `f964c5833323869b36b68102a71e7dc717346a9ac6365cf86ef378479228becd`,
  `5675bdbb162f9463b3500f883e5524a8e511df982e4bcc626f34b20a08186513`,
  `39dcee74ea8ddfc1aa110addc3ff8e280d4aea0b8f595b4d73b7efa3ffba7cd8`,
  and
  `38ee41bc01415f21311136bd344a4d48e1ab836e9504906749168e4cbd837ed0`.
  The retained logs support 6 files/36 tests, typecheck, build, and the
  recorded DNS-failed pack attempt. Packaged UI is `BLOCKED`; premerge,
  release-quality, and secret scan are `NOT_RUN`, never PASS. `waivers` is an
  empty array.
- Manager `RETURN.md` binds `RUNTIME_SUMMARY.json` by exact path, the required
  `738d5889...851c` hash, and status `PASS` only for ledger completeness; it
  explicitly records waivers as none.
- `RUNTIME_SUMMARY.json` is valid JSON and matches the append-only runtime
  ledger: 15 events, five sessions, five STARTs, five FINISHes, and zero
  unmatched sessions. Its closeout calibration remains `BLOCKED / PARTIAL`,
  parity closure false, distinct-helper trigger false, rerun authorized false,
  launcher untouched after the recorded write, and both retry-authorization
  and successful-package-command provenance `UNKNOWN`.
- Live source exposes `CHIRALITY_SKIP_CLI_LAUNCHER=1` and describes daemon mode
  as the same bundle relaunched with `--runtime-daemon`. The frozen package has
  the ordinary Electron helper apps but no distinct daemon-specific helper
  `.app`. The runtime calibration is truthful.
- The launcher current identity still matches the recorded post-write state:
  mode `-rwx------`, size `1114`, inode `45468523`, mtime
  `2026-08-20T15:26:36-0600`, SHA-256
  `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.

## Raw-byte preservation

All 18 executor evidence files match the exact hashes recorded by V2:

| Artifact relative to E1 `evidence/` | Checked SHA-256 |
|---|---|
| `CLEANUP_CONTAINMENT.md` | `186be2bbe36e359c3c964cc6f84f18e10b0578291fcf103c5915a8c44351c0c2` |
| `baseline/CRITICAL_IDENTITIES.sha256` | `ac3016fb91da984255e39c8f9e1df06f8b29d2a7530b13e8f8692624b4ff9500` |
| `baseline/GIT_STATUS.txt` | `1880e59ffe740df9f2735004316af8b39c70bdaaf92660517b2831948384fc9e` |
| `baseline/PACKAGE_INFO_PLIST.txt` | `0d27606cefbacb6a77d7235729ad952f3a0e6fe6281d6c54ab097c1992f7ddad` |
| `baseline/PACKAGE_MANIFEST.sha256` | `f7c072834fcc48c5a1fe37a6516ff33bcb4592c6dc2978aa0bf70843aa4ae54e` |
| `baseline/PACKAGE_SYMLINKS.tsv` | `6308b00235ff20598389689fbe50417fbb184ca45d20bd7fe1c1bdc0ac41f73c` |
| `baseline/SOURCE_MANIFEST.sha256` | `941bc28a6bf58ce2ee4d18d778923baec8ad91fca194a4e1ec025eea4b780e2d` |
| `baseline/TRACKED_DIFF.sha256` | `abcfa6a9d4df344d1781bc2560b5e4cdcae08b39ed303063535e7e1e926a304a` |
| `runtime/daemon-status.json` | `34e9da2c461758f682a6770c515270a7dc6831641dcca093581a11fd5e3217cc` |
| `runtime/desktop-daemon.log` | `782a89f18b9b6a9d7add63bf02143e993cee414346aa6fbdf6651ae5a0d71947` |
| `runtime/desktop-main.log` | `4b0b310ec20ed294a2e986dab76fe1cdd65fb620ed357cf57ca93b515b37d702` |
| `runtime/fixture.json` | `39dcee74ea8ddfc1aa110addc3ff8e280d4aea0b8f595b4d73b7efa3ffba7cd8` |
| `runtime/project-register.json` | `f320aed8fb9340fe7836b86f2761d040dda7c66b1f32b2b71531ffe101bcfadc` |
| `runtime/runtime-driver.mjs` | `9cfab9bce317223266a3d4e7b094424956d652063a5bbb7be62230e832533cf8` |
| `validation/build.log` | `f964c5833323869b36b68102a71e7dc717346a9ac6365cf86ef378479228becd` |
| `validation/desktop-pack.log` | `5675bdbb162f9463b3500f883e5524a8e511df982e4bcc626f34b20a08186513` |
| `validation/focused-tests.log` | `1aae3ff66b7afd86d99c54eef10aa12f34e726ad1ab7f48da00a039126f7db46` |
| `validation/typecheck.log` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` |

The source and package manifests also independently revalidate 509/509 and
446/446 target files. E1/V1/V2 returns remain byte-preserved at the hashes
listed above.

## Disposition

Criteria 1–6 pass. Raw-evidence and child-return preservation within criterion
7 pass. The Receipt 183 and run-root-only containment requirements in criterion
7 fail, and the no-receipt/shared-surface-effect requirement in criterion 8
fails. No parity, product, deliverable, release, lifecycle, waiver, trigger,
rerun, network-authorization, launcher-restoration, or Git effect is accepted
or inferred by this verdict.
