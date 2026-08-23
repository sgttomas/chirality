# R21 — R20 owner login-session proof PASS closeout

- Date: `2026-08-23`
- R20 proof revision: `2ee96958daf997b7a156f020739bde43ca78ebf9`
- R20 frontend tree: `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`
- Package executable SHA-256: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- R20 disposition: **EXECUTED AND PASSED**
- DEL disposition: the packaged-LaunchAgent actual-login-session proof obligation is satisfied by owner-executed evidence; DEL-09-04 remains `IN_PROGRESS` on separately gated signing, notarization, DMG, and release lanes.

## Claim boundary and attribution

This successor preserves R20's staging and repair history while recording the later owner-executed result. Three claim classes remain distinct:

1. **Owner report:** the owner states that Step 0 passed, preparation reached non-claiming `PREPARED`, one ordinary logout/login occurred, capture exited zero, the exact-revision check passed, and the public handoff printed.
2. **HELP_HUMAN host verification:** the run transcription reports independent host checks of the public-file hashes/cross-hashes and proof summary, plus exact proof-service/plist/process cleanup observations. Those host observations are attributed to HELP_HUMAN; this Agent 2 did not repeat them.
3. **This Agent 2's independent public-file observations:** only the exact public directory metadata and three named public JSON files were inspected. Their pre-copy types, modes, hashes, byte-identical DEL copies, copied JSON schemas, cross-hashes, and public semantics passed the sealed gates below. No private proof root or operator service was queried.

R20 is therefore recorded as `EXECUTED AND PASSED`, and its packaged-LaunchAgent login-session proof obligation is satisfied by the owner-executed evidence. This is an evidence and deliverable-status statement, not proof acceptance, release acceptance, release readiness, lifecycle issuance, signing, notarization, distribution, publication, deployment, or professional/reliance approval.

Any frontend mutation invalidates the staged R20 procedure for a future claim. A future proof claim after such a mutation requires a newly staged exact revision/package identity and a fresh owner-executed proof.

## Immutable public evidence snapshot

Source directory reported by the owner and inspected under the sealed public-only boundary:

`/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence`

DEL snapshot:

`Evidence/R20_Owner_Login_Proof_PASS_2026-08-23/`

The source and destination directories are real, non-symlink directories at mode `0700`, UID `501`, GID `20`. Each source and copied destination file is a real, non-symlink regular file at mode `0600`, UID `501`, GID `20`. Each pair passed byte-for-byte `cmp` after the copy.

| File | Bytes | Source inode | DEL inode | SHA-256 |
|---|---:|---:|---:|---|
| `prepared.json` | 1,248 | 51,867,393 | 51,911,010 | `5961b2060b554dc12989947a45335422f48f9e953d5af60c2ece88f7fdcf0a88` |
| `summary.json` | 2,018 | 51,867,394 | 51,911,011 | `38a603c470a51209b463a4657448794f8500cb32bfd5f83c2e6c611fb0aa06b1` |
| `evidence-package.json` | 398 | 51,867,395 | 51,911,012 | `aa84cdf66753d229dc9b2d27d147bc892107f054266d62f1f4bdf261280a6405` |

Only those three public files were copied. JSON parsing after the copy established:

- `prepared.json` is `chirality-packaged-launchagent-login-proof-session/v1`, status `PREPARED`, exact source revision `2ee96958daf997b7a156f020739bde43ca78ebf9`, exact executable hash `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, `preparedJobAbsent=true`, `bootstrapInvoked=false`, `kickstartInvoked=false`, `proofClaimed=false`, and recorded-only default protection.
- `summary.json` is `chirality-packaged-launchagent-login-proof/v1`, status `PASS`, at the same exact source revision and executable hash. All launch-agent assertions are true: prepared job absence, RunAtLoad, login-discovered job, loaded-program identity, loaded-arguments availability, and loaded-arguments match; bootstrap/kickstart are false. The login-session identity transition, PID observation, and executable identity match are true.
- Cleanup is complete: process/job/plist absent and runtime data removed are all true; job-mutation/destructive-cleanup refusals are false; failure-log copy/private-only flags are false; `passOnlyFailureLogCleanup` is `REMOVED`.
- All summary default-protection assertions are true: plist unchanged, loaded state unchanged, and mutation targets excluded. The proof boundary records the owner logout/login requirement, no harness logout/login, and no proof claim during preparation.
- `evidence-package.json` is `chirality-packaged-launchagent-login-proof-evidence/v1`, status `PASS`, at the exact source revision. Its prepared-manifest and summary cross-hashes exactly equal the copied files above, and its manifest names exactly `prepared.json` and `summary.json`.

The package executable identity is bound because both copied `prepared.json` and `summary.json` directly record the same hash. No private or uncommitted evidence is used for that identity.

## WP-00 / G0.25 evidence-only assessment

The committed plan `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`) defines WP-00 §9 to exit only with owner-executed evidence or an explicit deferral/invalidated-state record. Its §10.1 G0.25 pass-evidence branch is: the DEL-09-04 staged owner procedure is completed and snapshotted, or explicitly deferred with invalidation/re-stage consequence; the hard stop is treating staged evidence as current after frontend mutation; the decision owner is the human owner plus App loop. Root `execution/_Coordination/LOOP_RECEIPTS.md` Receipt 114 C2 records the owner's agreement to execute the sequence first.

The copied exact-revision public snapshot supplies evidence matching the plan's owner-executed/completed-and-snapshotted branch, and this record states the invalidation/re-stage rule. That is evidence for the owner's later gate ruling only. This record does **not** declare G0.25 human-ruled, passed, or accepted. WP-00's separately named daemon-deployment act is not established by these three public files and is not claimed here.

## Complete owner direction and handoff — verbatim

The following block is transcribed byte-for-byte from run-root `CHAT_TRANSCRIPTION.md` (SHA-256 `9d9237f6671e24c8eb3f72a5cf71b21221aa4aeb09b16f5efae60f581200dba9`):

> OWNER DIRECTION — DEL-09-04 R20 login-session proof PASSED; record and close the proof obligation.
>
> I executed the staged R20 procedure on 2026-08-23: Step 0 PASS, Step 1/1b PREPARED (proofClaimed false, sourceRevision 2ee96958daf997b7a156f020739bde43ca78ebf9), one ordinary logout/login, capture exit 0, PASS and exact-revision check PASS, three public files preserved, handoff printed. The verbatim handoff:
>
> CHIRALITY LOGIN PROOF OWNER HANDOFF
> PROOF_REVISION=2ee96958daf997b7a156f020739bde43ca78ebf9
> PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933
> PUBLIC_EVIDENCE=/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence
> STATUS=PASS
> 5961b2060b554dc12989947a45335422f48f9e953d5af60c2ece88f7fdcf0a88  prepared.json
> 38a603c470a51209b463a4657448794f8500cb32bfd5f83c2e6c611fb0aa06b1  summary.json
> aa84cdf66753d229dc9b2d27d147bc892107f054266d62f1f4bdf261280a6405  evidence-package.json
> OWNER_MESSAGE=R20 login-session proof returned for owner review; no acceptance or release claim is implied.
>
> HELP_HUMAN independently verified on the host: the three public-file hashes match on disk (0600 in a 0700 directory); evidence-package.json's preparedManifestSha256 and summarySha256 equal the on-disk hashes; summary.json shows status PASS with every launchAgent/loginSession/process assertion true, cleanup fully complete (processAbsent, jobAbsent, plistAbsent, runtimeDataRemoved all true, nothing refused, passOnlyFailureLogCleanup REMOVED), and defaultProtection all true; the proof service exits 113, the plist is absent, and no proof daemon process remains. Do not read the private session root.
>
> In one bounded tranche on a new branch from current main:
>
> 1. Record R20 as EXECUTED AND PASSED in a new run-record section or successor record per your convention, quoting this direction and the handoff verbatim, with the three public-evidence hashes as the immutable proof identity bound to PROOF_REVISION 2ee96958daf997b7a156f020739bde43ca78ebf9 and package executable 79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874. Copy the three public files (and only those three) from the Desktop public-evidence directory into the DEL-09-04 evidence tree as the immutable snapshot, verifying the three hashes byte-for-byte before and after the copy.
> 2. Update DEL-09-04 _STATUS.md: the packaged-LaunchAgent login-session proof obligation is satisfied by owner-executed evidence; state the re-stage rule (any frontend mutation invalidates the staged procedure and requires a new staged revision and a fresh owner proof for any future claim); DEL-09-04's remaining scope (signing, notarization, DMG, release lanes) stays IN_PROGRESS and separately gated — no release-readiness claim.
> 3. Record the WP-00/G0.25 gate outcome as evidence for the owner's later gate ruling — the gate decision itself remains a human act.
> 4. Close or update the relevant Task Management rows for the proof-failure repair chain per your register conventions (candidates already recorded: parser fixtures, umask/uid portability, KeepAlive crash-loop hazard routing to G-HELPER).
> 5. Receipt 192 with this CHAT_TRANSCRIPTION; full pre-push gate set including whitespace (gzip/normalize any captured logs); push; one PR; do not merge. If main advances, request sync authorization and record it.
>    Not authorized: any signing, notarization, deployment, distribution, publication, release-readiness, or acceptance claim; any frontend, packaging, daemon, or staged-procedure change; touching com.chirality.runtime; reading /private/tmp/ch-r18-91499728-51dd.

## Handoff state

- Accepted upstream basis: committed revision `75c4e2ba401a6f5ad0c2f38846c39db6ab157405`, R20 staged record SHA-256 `f3cd377d980606fd71af259d4d24f4cbc52601418a009b8b4d6aa382ba6b5341`, and the exact owner direction/public evidence identities above.
- Derivative status: this R21 and the DEL snapshot are derivative closeout evidence; they do not replace the copied public JSON or the owner act.
- Closure verdict: R20 `EXECUTED AND PASSED`; packaged-LaunchAgent login-session proof obligation satisfied by owner-executed evidence; DEL-09-04 remains `IN_PROGRESS` for unrelated separately gated lanes.
- Rerun requirement: any frontend mutation requires a new staged revision/package and fresh owner proof before any future claim.
- Remaining blocker: signing, notarization, DMG, release, and any acceptance/publication act remain separately human-gated. G0.25 remains for human/App-loop ruling.
