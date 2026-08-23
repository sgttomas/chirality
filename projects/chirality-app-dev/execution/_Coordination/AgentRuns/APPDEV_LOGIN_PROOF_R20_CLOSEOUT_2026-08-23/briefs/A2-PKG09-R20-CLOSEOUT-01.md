# Sealed brief — R20 public proof snapshot and DEL-09-04 closeout

- RequestedBy: WORKING_ITEMS / HELP_HUMAN owner-directed run.
- RunID: `APPDEV_LOGIN_PROOF_R20_CLOSEOUT_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-CLOSEOUT-01`.
- ChildInstanceID: `A2-PKG09-R20-CLOSEOUT-01`.
- Role: non-delegating ephemeral Agent 2; delegated-harness-native role is instruction-asserted.
- Basis: exact clean `75c4e2ba401a6f5ad0c2f38846c39db6ab157405`; frontend tree must remain `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.

## Objective

Record the owner-executed R20 PASS without acceptance/release overclaim: snapshot exactly three public JSON files, author a successor R21 record preserving R20 history, update DEL status minimally, and record WP-00/G0.25 outcome as evidence only for a later human gate ruling.

## Exact source and destination

- Source directory: `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence`.
- Source names, and no others: `prepared.json`, `summary.json`, `evidence-package.json`.
- Expected hashes respectively: `5961b2060b554dc12989947a45335422f48f9e953d5af60c2ece88f7fdcf0a88`, `38a603c470a51209b463a4657448794f8500cb32bfd5f83c2e6c611fb0aa06b1`, `aa84cdf66753d229dc9b2d27d147bc892107f054266d62f1f4bdf261280a6405`.
- Destination: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Evidence/R20_Owner_Login_Proof_PASS_2026-08-23/`, directory mode `0700`, files mode `0600`.

Inspect only the exact source directory metadata and the three exact files. Require source directory real/non-symlink/mode `0700`; require each source regular/non-symlink/mode `0600`; do not enumerate or read any other Desktop path. Verify hashes before copy. Copy mechanically with no transformation, set destination modes, verify `cmp` and hashes after copy, and parse only the copied public JSON thereafter.

## Required semantic checks and records

1. Verify the copied JSON supports source revision `2ee96958daf997b7a156f020739bde43ca78ebf9`, PASS status, prepared-manifest/summary cross-hashes, all launch-agent/login-session/process assertions true, full cleanup true with no refusal and `passOnlyFailureLogCleanup` removed, and defaultProtection true. Bind package executable identity `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` only where public/committed evidence supports it.
2. Author `_run_records/R21_R20_OWNER_LOGIN_SESSION_PROOF_PASS_CLOSEOUT_2026-08-23.md`, quoting the complete owner direction and handoff verbatim from the run CHAT transcription. Distinguish owner report, HELP_HUMAN host verification, and independent public-file observations. State R20 `EXECUTED AND PASSED`, proof obligation satisfied by owner-executed evidence, but no acceptance or release-readiness claim.
3. Update `_STATUS.md` minimally: the packaged-LaunchAgent login-session proof obligation is satisfied; any frontend mutation invalidates the staged procedure and requires a new staged revision plus fresh owner proof for a future claim; DEL remains `IN_PROGRESS` for separately gated signing/notarization/DMG/release lanes. Remove/replace the obsolete unproved Remaining item without closing those lanes.
4. Read the committed WP-00/G0.25 gate contract and record the evidence outcome in R21 or a run-local assessment. The decision/ruling remains human-only; do not mark a human gate ruled.
5. Write only the destination snapshot, R21, `_STATUS.md`, and `instances/A2-PKG09-R20-CLOSEOUT-01/**`. Do not touch Task Management, receipts, frontend, package, procedure, Git, operator state, or any other deliverable.

## Absolute fences

Never read, stat, list, traverse, or otherwise query `/private/tmp/ch-r18-91499728-51dd`. Never query or touch `com.chirality.runtime`. No proof command, GUI, launchctl query beyond no query at all, signing, notarization, deployment, distribution, publication, release claim, network, stage, commit, push, PR, or merge.

## Return

Freeze activation, source/destination metadata and hash evidence, semantic-check evidence, exact changed paths/hashes, and RETURN. Run JSON parsing, `git diff --check`, App containment/index, frontend identity, and narrow candidate whitespace for your instance/shared files. Stop on any failed gate.
