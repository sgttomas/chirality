# A2-PKG02-PARITY-AMEND-VERIFIER-02 return

Verdict: `ACCEPT_AMENDED_FAN_IN`

Scope of acceptance: Closeout Amendment 01 and the corrected manager-owned
records are fit for blocked/partial fan-in. This accepts no parity closure,
distinct-helper trigger, rerun authority, package-command provenance, release
readiness, or deliverable/lifecycle effect. No repair was performed.

## Findings

1. **Corrected records are mutually consistent.** `RUN_MANIFEST.md`,
   `VALIDATION.md`, `HANDOFF.md`, manager `RETURN.md`, `EVIDENCE_INDEX.csv`,
   `STATUS.md`, `HANDOFF_STATE.md`, and `CLOSEOUT_AMENDMENT_01.md` consistently
   preserve `BLOCKED / PARTIAL`, hold N2, deny parity closure, state that the
   explicitly distinct-helper trigger is not established, authorize no rerun,
   leave the launcher untouched after the recorded write, and attribute the
   write to omission of `CHIRALITY_SKIP_CLI_LAUNCHER=1` from the verification
   invocation. Live `frontend/electron/cli-launcher.ts` exposes that opt-out,
   and live `electron/main.ts` describes daemon mode as the same app bundle
   relaunched with `--runtime-daemon`. The accepted D-APP-88/D-APP-93 closure
   accepts the signal binder, bounded teardown, and regression remedy; it does
   not establish a distinct helper bundle. DEL-02-02 and DEL-08-02 retain an
   explicitly distinct-helper acceptance/landing gate.
2. **Package/network claims are calibrated.** No corrected manager-owned
   surface claims an authorized or durably evidenced retry. Those surfaces set
   network-retry authorization and the exact successful package-command
   provenance to `UNKNOWN` while retaining only package existence and byte-hash
   facts. Historical activation, plan, sealed briefs, and earlier child returns
   remain preserved as their original run record; they are not cited as proof
   of retry authorization or of a fired trigger.
3. **The current index is well formed and hash-consistent.** The CSV has one
   six-column header plus 16 six-column data rows. All 16 artifact paths exist
   under the run root and all 16 SHA-256 values match. The CSV SHA-256 is
   `c70fca60c115a18ac91ed1004ffd985defc7630e7baaf7623f1990cf91c56ff0`.
   The manager return's 12-row statement accurately reports the earlier V1
   check of the pre-amendment index; the append-only runtime amendment event
   records the corrected 16-row index.
4. **Frozen identities still independently revalidate.** The source manifest
   passes 509/509 rows and has SHA-256
   `941bc28a6bf58ce2ee4d18d778923baec8ad91fca194a4e1ec025eea4b780e2d`.
   The package manifest passes 446/446 rows and has SHA-256
   `f7c072834fcc48c5a1fe37a6516ff33bcb4592c6dc2978aa0bf70843aa4ae54e`.
5. **Earlier child returns and raw executor evidence are preserved.** The
   executor return is
   `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9`
   and the first verifier return is
   `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21`,
   exactly matching their previously recorded hashes. Every raw-artifact hash
   previously recorded in the executor return, first verifier return, index,
   manifest, or validation ledger still matches. The deterministic aggregate
   SHA-256 over the 18 sorted `SHA256  relative-path` raw-evidence lines is
   `f9e11970d46f805dc8a76ac3874b3b9659a113ccf15ba5bc5485a7b984e8a9fe`.
6. **Write containment holds.** HEAD/tree/branch remain
   `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`,
   `fe8ece104dd281e3219bd95fa8b121437d524520`, and
   `codex/app-dapp86-helper-parity-rerun-20260820`. There is no tracked or
   staged diff. Every non-ignored untracked path is under this run root; hence
   tracked product/source, deliverable status/memory/run-record, receipt,
   register, project plan, Git, and foreign-loop surfaces are unchanged. The
   untracked frozen orchestration plan and graph predate the amendment; their
   current hashes are recorded below. The owner launcher remains mode
   `-rwx------`, size `1114`, inode `45468523`, mtime
   `2026-08-20T15:26:36-0600`, and SHA-256
   `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`,
   exactly matching the recorded post-write state. This verifier did not touch
   it.
7. **Telemetry treatment is valid.** `RUNTIME_EVENTS.jsonl` is append-only and
   records this verifier's start. `RUNTIME_SUMMARY.json` summarizes the nine
   completed pre-amendment events and need not contain this active session;
   manager-owned telemetry may be summarized after this return.

## Corrected manager-record hashes

| Artifact | SHA-256 |
|---|---|
| `RUN_MANIFEST.md` | `035c473da4dbb72edf2e3f6fda92e8c94e041b8c1c842468772844c5897a16d6` |
| `VALIDATION.md` | `20c5b054232e5b5b9323b77a5c9f98690b401897a7a13632cd9421e8ca0678fc` |
| `HANDOFF.md` | `20f8283dcbe2468c624017cd6fff5108d8a58fd738eae54e79193515b0fc17ee` |
| `RETURN.md` | `f333e7170a99ccf26aeb1f00ede6075296ac26515c2040b40a27b6a69eab0ed7` |
| `EVIDENCE_INDEX.csv` | `c70fca60c115a18ac91ed1004ffd985defc7630e7baaf7623f1990cf91c56ff0` |
| `STATUS.md` | `2c4a3bf002fa73ae3d01abb1c0ffd0600ed6eb79a5c617c19dbbd27a64c4bd51` |
| `HANDOFF_STATE.md` | `52593e20138aee088c0c736e2b8df46f6baa0889c49338afd33e3169002891f3` |
| `CLOSEOUT_AMENDMENT_01.md` | `4a5f42306364ff16a18e57e8e6888a4a746487c0242b2dca1b326d6da07e5104` |

## Preserved raw-evidence hashes

Paths below are relative to
`instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/`.

| Artifact | SHA-256 |
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

## Preserved control-plane hashes

| Artifact | SHA-256 |
|---|---|
| `ACTIVATION.md` | `f0495112d0253f0481b55f55b137f042b34744b0317225ab39afa7d3a606b1a0` |
| `ORCHESTRATION_PLAN.md` | `67df4f540bea366558693f1464f9fbb3837d865c93d5a75e34591a431c5fad65` |
| `WORK_GRAPH.json` | `1a03746442a9e3ba8018af8448d104c809aefde403e807955e1c6ba6ee61a86e` |
| Executor `LAUNCH_BRIEF.md` | `ce23f5e3a40fab4ad4c5967ca70e6bb5e41aca51005df057a4c9bbe9db19f1aa` |
| Executor `RETURN.md` | `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9` |
| First verifier `LAUNCH_BRIEF.md` | `86d6528bb98b67a628d6cc3a5e033977bbfe31e1adb9380573281ca2119060ac` |
| First verifier `RETURN.md` | `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21` |

No repair, launcher mutation, product/source edit, deliverable update, plan
update, Git action, test/build/app/daemon/UI execution, or foreign-loop write
was performed.
