# R4.4.6 attempt-2 intake and D-APP-94 fresh-verifier return

Verdict: `BLOCK`

Role performed: genuinely fresh, read-only ephemeral Agent 2 adversarial
verification. No repair, runtime/process inspection, signal, package,
helper/GUI, keychain, credential, product, Git, Task Management, or
foreign-loop action was performed. This return is the sole write.

## Material blockers

1. **The frozen source-attribution erratum is contradicted by the immutable
   returned bytes.** The required proposition was that the
   `2026-08-08T05:57:26.027Z` / `Unknown project: chirality-app-dev` line is in
   `gui.stdout.txt`, **not** `gui.stderr.txt`. Independent literal searches
   found one matching record in each file:

   - `returned_r4_4_6/gui.stdout.txt:5`:
     `[chirality-desktop] 2026-08-08T05:57:26.027Z [info] runtime.connectivity.state {"state":"disconnected","failedAttempts":1,"lastError":"Unknown project: chirality-app-dev","changedAt":"2026-08-08T05:57:26.027Z"}`;
   - `returned_r4_4_6/gui.stderr.txt:1`:
     `[chirality-desktop] 2026-08-08T05:57:26.027Z [warn] runtime.connectivity.bind_failed {"attempt":1,"reason":"Unknown project: chirality-app-dev"}`.

   Therefore the completed form's attribution of the attempt-1
   `runtime.connectivity.bind` record to `gui.stderr.txt` is supported, not an
   erratum. The contrary statements in
   `R4_4_6_ATTEMPT2_INTAKE_VALIDATION.md`,
   `R4_4_6_ATTEMPT2_DISPOSITIONS_AND_CAUSAL_MATRIX.md`, and the D-APP-94 packet
   cannot pass the required frozen-byte check. This does not give the line
   fresh-C1118 status or causal credit: C1118 remains `NOT_RUN`.

2. **The frozen completed form carries the wrong R4.4.6 runbook identity.**
   `returned_r4_4_6/completed-evidence-return.md:18` records runbook SHA-256
   `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`,
   which is the earlier R4.4.5 identity. The R4.4.6 packet freeze binds
   `prepared/OWNER_OPERATED_RUNBOOK.md` at
   `9fda14d73d3eca1a0b055ea727853ecec11e824d8cc17fd57161a4ab9f2193d8`,
   and direct hashing reproduces the latter. The completed form itself is
   frozen and reproduces its adjacent sidecar at
   `033002556ca64c1dbe531ccbd5f3c425494f22cbdf8f7941cb583b9943cb5e98`;
   the mismatch is thus a retained substantive form error, not mutable drift.

Either blocker is independently sufficient for `BLOCK`.

## Required-check evidence

1. **Frozen identities:** all candidate files and every identity bound by both
   freezes reproduced on initial read and on the final stability pass; the
   exact values are listed below.

2. **Immutable return inventory:** direct enumeration found exactly 40 regular
   files, comprising 20 primaries and 20 adjacent sidecars. Each sidecar digest
   reproduced its primary. The independently sorted
   `name|byte_count|sha256\n` aggregate was
   `97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110`.
   The primary results were:

   | Primary | Bytes | SHA-256 | Sidecar check |
   |---|---:|---|---|
   | `c1103.sha256.txt` | 182 | `df35907b158b459d0ad7ca2a1ba4d1fa6592955e35bcecc7ce7ff8522898a95f` | PASS |
   | `c1104.electron-builder.runtime-helper.json` | 1890 | `1cb9e4c7325166f69139eeba3a0bdfcfa1d4f871e03acf4af1809aa88fa02a36` | PASS |
   | `c1104.package.json` | 6436 | `b53a867e8aa7d8874cf7ce2417691a05d449babaa9bf0b905c550deb13b3ac6d` | PASS |
   | `c1105.exit.txt` | 26 | `bf55d4479fcfbc254fb89bbe20a0baf8552d51302ed14ba2d55f77f667d4fd07` | PASS |
   | `c1105.output.txt` | 1454 | `df37a51cfe329286431bf2998ec592d4e81f6cd435c85364fc490017c6f404d8` | PASS |
   | `c1106.exit.txt` | 26 | `bf55d4479fcfbc254fb89bbe20a0baf8552d51302ed14ba2d55f77f667d4fd07` | PASS |
   | `c1106.output.txt` | 136 | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` | PASS |
   | `c1107.exit.txt` | 26 | `bf55d4479fcfbc254fb89bbe20a0baf8552d51302ed14ba2d55f77f667d4fd07` | PASS |
   | `c1107.output.txt` | 3348 | `521b31eb568d570681b97da845cd8212baf0f3b8eadcacda9401d80f2cffbb14` | PASS |
   | `c1108.exit.txt` | 26 | `bf55d4479fcfbc254fb89bbe20a0baf8552d51302ed14ba2d55f77f667d4fd07` | PASS |
   | `c1108.output.txt` | 26517 | `7f8ac07017371b5098363a0bb50486fc592db5aea843e220d16394bc02d8d5a9` | PASS |
   | `completed-evidence-return.md` | 17426 | `033002556ca64c1dbe531ccbd5f3c425494f22cbdf8f7941cb583b9943cb5e98` | PASS |
   | `control-transcript-precleanup.txt` | 69106 | `982ae86e49a5f5ebe611dca0c6f789f34c785fbcc39ef2a2d237d9c72b60988e` | PASS |
   | `control-transcript.txt` | 80266 | `ff78e462c81563c97ada775c590412ca9cc27e4ea474e68aea353873c323690a` | PASS |
   | `gui.pid` | 6 | `26cd5a9e8a2e471a62bc10a8b00aead662c1fe56d79924f97096ebbf9d6add7b` | PASS |
   | `gui.stderr.txt` | 58432 | `8ce751515e90911ebf5d41f0e4679945b430d2d422b2671aa643e7a8c8c2190c` | PASS |
   | `gui.stdout.txt` | 1424 | `292fdb6fbd28291e24a985968d19852e84aaf79d24eb4b7d6796a2311a5bb4d7` | PASS |
   | `helper.pid` | 6 | `46f22259ed1cce7e25437b21d3a92c18d965797326be737369fffd0e1bcf25d8` | PASS |
   | `helper.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | PASS |
   | `helper.stdout.txt` | 470 | `6ca345fd80dea79b91b31829fa5fc287fc268860b2154317c77e1050aa48fc3e` | PASS |

3. **CONTROL ranges:** direct byte parsing of the 80,266-byte transcript found
   exactly 22 ordered output markers and reproduced these zero-based,
   end-exclusive ranges/exits:
   `01 [0,264) 0; 02 [264,1137) 0; 03 [1137,1867) 0; 04 [1867,5182) 0; 05 [5182,11707) 0; 06 [11707,14030) 0; 07 [14030,14853) 0; 08 [14853,16289) 0; 09 [16289,23028) 0; 10 [23028,50335) 0; 11 [50335,64537) 0; 12 [64537,65530) 0; 13 [65530,65973) 0; 14 [65973,66675) 1; 15 [66675,67664) 0; 23 [67664,68635) 0; 25 [68635,73872) 0; 26 [73872,74721) 0; 27 [74721,75397) 1; 28 [75397,77785) 0; 29 [77785,79738) 0; 30 [79738,80156) 0`.
   Bytes `[80156,80266)` are only the rendered shell prompt/newline. Thus
   C1146.30 is the last CONTROL input, with no later input; steps 14 and 27 are
   the only exit-1 markers.

4. **Step-14 route:** `prepared/OWNER_OPERATED_RUNBOOK.md:80-81` says missing
   or unexpected C1116 paths stop before GUI launch. Transcript bytes
   `[65973,66675)` show both named paths returning `No such file or directory`
   and step 14 exit 1; bytes `[66675,67664)` then show C1117 GUI launch and
   step 15. The intake correctly classifies step 14 `FAIL`, step 15
   `DEVIATION`, and the execution as not route-conformant.

5. **Form/contact:** the form and sidecar reproduce, so the form is frozen as
   returned. C1118 is `NOT_RUN`, and the contact records remain supporting
   only, never a fresh-C1118 substitute or causal credit. The frozen erratum
   nevertheless fails for the exact reason in blocker 1. The form also carries
   the runbook-identity error in blocker 2.

6. **C1105-C1108:** each output is present and sidecar-reproducing; each exit
   file is exactly 26 bytes/two newline-terminated records,
   `command_exit=0` and `tee_exit=0`. C1108 records helper packaging at
   `dist-runtime-helper/mac-arm64`, GUI packaging at `dist/mac-arm64`, and the
   same run-root archive
   `/private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip`
   for both. Its `desktop:verify-dependencies` JSON is `status: PASS`, with
   `localPackageEntries: 0`, an empty forbidden list, all required packages,
   and no failures. This supports package/launch identity only; C1119 and the
   signal path were not run.

7. **Returned launch/cleanup/rollback evidence:** transcript and PID primaries
   agree on helper PID 92988 and GUI PID 93012, both direct children of CONTROL
   shell 90439, with their exact helper/GUI executables. Applicable cleanup
   order was GUI identity check -> GUI `TERM` -> observed GUI job completion ->
   helper identity check -> helper `KILL` -> zero-row GUI check. Step 27 exit 1
   is the final zero-row `ps`, so no GUI KILL was applicable. The eight C1140
   rollback hashes reproduce current safe read-only filesystem hashes:
   `850f7b00...335b`, `16ad6688...d1f`, `5006bef6...026a`,
   `1f14df17...ba53`, `5c8fce2a...1a56`, `a6759be0...558`,
   `1918ae7d...91e9`, `f8b6d8c2...36be6`. C1141 has zero output bytes between
   its input and the step-29 record. The fixed temp root, all five candidate
   additions, and returned build/dependency derivatives are absent in safe
   read-only filesystem checks. `lldb-transcript.txt` is absent; steps 16-22
   and 24 have no CONTROL marker; C196/C197 were unused.

8. **Terminal calibration:** the derivative terminal verdict is
   `STOP_INCOMPLETE — ENVIRONMENT DEPENDENCY AT C1118`. All eight D-APP-88
   signal-path causal cells are `UNKNOWN`; package/runtime identity is only
   `SUPPORTED AT LAUNCH`. No D-APP-88 acceptance, DEL-09-04 closure,
   TM-APP-036 firing, product/remedy, release, or reliance conclusion follows.

9. **D-APP-94 packet:** apart from the contradicted source-attribution premise,
   it neutrally presents A/B/C, makes Option A conditional on static isolation
   and ordinary fail-closed behavior, gives exact preparation-only tokens,
   states authority/evidence/risk/affected-surface/later-gate boundaries, and
   decides nothing. It grants no source implementation, keychain, credential,
   execution, product, release, or reliance authority.

10. **Register/future gates:** exactly one register row begins
    `| D-APP-94 |`, and its state is `AWAITING_RULING`. The packet requires
    every option to obtain fresh C1118 and separately repair/fresh-verify the
    step-14 observation/gate before any future attempt.

11. **Current-source plausibility:** read-only review of
    `electron/api-key-storage.ts`, `runtime-host.ts`, `main.ts`, and
    `src/__tests__/electron/api-key-storage.test.ts` found real safeStorage
    read/write/decrypt call paths, runtime-host credential consumers, startup
    surfaces, explicit unavailable-storage fail-closed behavior, and focused
    tests. A narrowly guarded diagnostic-only design, an isolated keychain, or
    a normal-session environment are plausible *planning* choices. No existing
    bypass is proved; the packet correctly makes Option A conditional.

## Final stability hashes

Initial and final candidate/bound-identity values were identical:

| Object | Final SHA-256 |
|---|---|
| `R4_4_6_ATTEMPT2_INTAKE_FREEZE.md` | `b5a5245f958a04889753a14db58d59e89defff7af37fb29a22aa7fed96830537` |
| `DAPP94_DECISION_PACKET_FREEZE.md` | `8107d832a01959a49e0993f7d3748171d4b40741fca943ada84aa67002dd6f4e` |
| `D-APP-94_PACKET_MISSING_KEYCHAIN_ENVIRONMENT_2026-08-08.md` | `ce30c8fe04ee64263a3399c89753d84a167781092bc62bd7fa043fd6345709a6` |
| `_DECISIONS/_REGISTER.md` | `5698122ebd7cdb8312b138d71c7c8439c3b2cf760f85fd9439825b8104f215ca` |
| `R4_4_6_ATTEMPT2_RETURNED_MANIFEST.md` | `6415697209d4c4bc6befdfed49b5eb4e3287b3142af831f259f935a8e20a8009` |
| `R4_4_6_ATTEMPT2_CONTROL_RANGE_INDEX.md` | `a7f5d9d00aa1fbe954e0604494acdbdaa0312984fd553d8c8aef153e600b8f54` |
| `R4_4_6_ATTEMPT2_DISPOSITIONS_AND_CAUSAL_MATRIX.md` | `b3f872918bd4876b75f2428af47153f16609d10621897fa98f831e77d956140d` |
| `R4_4_6_ATTEMPT2_INTAKE_VALIDATION.md` | `fc7b94b702f8840bdcb84c146577ce0d058cf6a9826f7a92b109781d56aac9ce` |
| `MANAGER_FREEZE_R4_4_6.md` | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| `A2_DAPP93_R4_4_6_SUCCESSOR_FRESH_VERIFIER_RETURN.md` | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` |
| `MANAGER_FREEZE_R4_4_6_CLEANUP_OBSERVATION_ADDENDUM.md` | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |
| `A2_DAPP93_R4_4_6_CLEANUP_OBSERVATION_ADDENDUM_FRESH_VERIFIER_RETURN.md` | `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f` |
| sorted all-40 returned-object aggregate | `97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110` |

The frozen intake and D-APP-94 decision packet do not pass the sole fresh
verifier gate.
