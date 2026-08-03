# A2-PARITY-VERIFIER-01 Terminal Return

Verdict: `ACCEPT_FAN_IN`

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

Posture: fresh read-only verification; no repair, product execution, package or
test rerun, or unauthorized write.

## Nine check dispositions

1. **Evidence index — PASS.** 39 data rows; 39/39 SHA-256 matches; zero
   missing and zero mismatches. `EVIDENCE_INDEX.csv` SHA-256:
   `f6fb49d322ce4c6d94b0b68de20efc5dcfb8efe69d7a1df02352e77ebbca2c73`.
2. **Source/package identity — PASS.** Source 380/380; package 446/446;
   14/14 symlink paths and targets match. Executable/app.asar/Info.plist hashes
   match the manifest; the executable is thin arm64. Signing is linker/adhoc,
   `TeamIdentifier=not set`, with no release-signing claim.
3. **Four packaged observations — PASS.** DOM, full AX trees, and visually
   inspected 2560x1580 PNGs correlate Workbench live 53-deliverable contract
   state; Pipeline DECOMP/PREP/TASK/AUDIT intent; selection held at `null`
   during the live primary turn and enabled after completion; and read-only
   replay of session `e2c32024-fa62-48d5-b27a-d8637080d2c3` with 2 events,
   1 transcript item, 0 malformed records, and terminal event
   `a26a661d-721e-491d-ab9f-66b2aa3b2dd0 / turn.completed`.
4. **Attribution calibration — PASS.** Exact admitted identity is persona
   `WORKING_ITEMS`, role `agent1`; recursive runtime-evidence inspection finds
   no parent/child attribution field, and none is inferred.
5. **Validation account — PASS.** Hash-bound records confirm focused 58/58,
   typecheck, build, the sole successful `desktop:pack`, full Vitest 142 files
   passed / 1 skipped and 1,111 passed / 4 skipped, blocking Section 9 16/16,
   packaged premerge 8/8 plus report-only 16/16, receipt, corpus, practitioner,
   self-check, pytest 349, dependency lint, manifest checks, and secret scan.
   Final summary hashes are release quality
   `6718f0f5e3214f4344e1691d12d78255ad2e1f22b686f06553ba8017617b2a29`,
   Section 8
   `264d5ecab7f9fd9bc9832814765876c94204f8fe2653dad32d9006bb4a63acb9`,
   and Section 9
   `d44d6e0e357a4dc324b7a3b299359747bc259a580c4f8c73ecdb499c79fa4f4d`.
   The first wrapper's AF_UNIX `EINVAL` and exact shorter-`TMPDIR` retry are
   disclosed, not erased.
6. **Cleanup/projection containment — PASS.** Both exact temporary roots and
   run PIDs 54016/54094 are absent; no CDP/App listener remains. Owner daemon
   PID 2499 remains and owner plist mtime is `1784951879`.
   `runtime/node_modules` is restored as the original real directory, inode
   `22189023`; file aggregate
   `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`,
   empty-symlink aggregate
   `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
   both backup paths absent, and Root runtime diff/status empty.
7. **D-APP-89/D-APP-88 posture — PASS.** Zero ordinary compatibility-facade
   consumers, exactly 13 rollback probes, facade retained. The D-APP-88
   distinct helper remains absent/blocked and is a non-blocking mandatory
   future parity-rerun trigger.
8. **Historical relations — PASS.** Exactly six
   `HISTORICAL_RELATION_UNKNOWN`; authoritative CSV SHA-256
   `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`;
   zero diff.
9. **No unauthorized D-APP-86 effect — PASS.** HEAD remains
   `97678a841ef58345c73d3470ed8de57c9b1405d2`; tracked status matches the
   frozen pre-run baseline, frontend source is 380/380, Root runtime diff is
   empty, and `git diff --check` passes. No product/config/test/document,
   foreign-loop, Git, receipt, Task Management, decision, deliverable
   pointer/status, authority, decomposition, SCOPE_CHANGE, signing,
   notarization, release, publication, or distribution write is attributable
   to D-APP-86.

## Limitations and rerun

Required cleanup removed transient Attempt-01 and first-wrapper raw logs; their
dispositions remain in indexed, hash-verified records, while final validation
summaries/logs remain and match. The secret scan reports 3,697 files scanned,
zero blocked findings, and no provider-secret inputs; explicitly skipped
binary/extension classes were separately bounded by manifest, parsing, and
visual inspection. Native token/context occupancy is unavailable and not
inferred. A later accepted D-APP-88 distinct-helper implementation requires a
fresh parity rerun.

All sealed checks pass. Manager fan-in and any lifecycle, Task Management,
receipt, Git, signing, release, publication, or distribution act remain
outside this Agent-2 authority.
