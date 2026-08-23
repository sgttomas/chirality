# CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING

Date: 2026-08-23
Owner: Ryan Tufts
Run: `APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23`

The following is the owner's direction transcribed verbatim from the launch
message. It is evidence of direction and does not itself prove any execution,
package, login-session, lifecycle, or release claim.

```text
PR #623 was merged.

OWNER DIRECTION — DEL-09-04 offline exact-merge rebuild and R19 staged procedure.
Tranche A is merged; main is d6861ae8251e2a81078577d4496e949735ff199d (frontend
tree 9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4). Non-rewriting sync this
worktree to that commit and confirm porcelain is empty. Then, in one bounded
tranche:

1. Run npm run electron:supply-chain; it must print the verified directory.
   Rebuild the unsigned arm64 app with npm run desktop:pack from exact
   d6861ae8251e2a81078577d4496e949735ff199d with NO network. electron-builder
   must log "using custom electronDist directory"; the log must contain no
   download indicator. Overwrite — do not adopt — the Tranche A evidence build.
2. Verify the package as R16 did (bundle id, version, min macOS, arm64, ad-hoc
   signature, main-executable and runtime-cli SHA-256, instruction-root
   integrity at the exact commit); confirm the R17 runtime-host socket-path
   guard is in the packaged runtime.
3. Empirical pre-check before staging (new requirement): start the packaged
   daemon once in a disposable form with CHIRALITY_USER_DATA set to exactly
   /private/tmp/ch-r18-91499728-51dd/runtime-data, confirm it binds
   runtime/control.sock and reaches a healthy state, stop it, remove that
   runtime-data, and record the evidence. No LaunchAgent, plist, bootstrap,
   or kickstart is involved in this check; the proof root must be absent again
   before staging.
4. Stage R19 without executing: PROOF_REVISION = d6861ae8251e2a81078577d4496e949735ff199d,
   exact PROOF_APP, session root exactly /private/tmp/ch-r18-91499728-51dd
   (67-byte socket path), a unique short label not loaded; Step 0 = every R16
   gate plus the printed socket byte count plus the read-only preflight; then
   the R16 block structure through the hash-printing handoff; note each block
   uses set -euo pipefail in a fresh Terminal tab.
5. Update _STATUS.md, write Receipt 190, fresh review, one PR, stop. Do not
   merge. No prepare, capture, logout/login, bootstrap, kickstart, signing,
   notarization, deployment, or release-readiness claim. The proof remains my
   act.
   Full-suite disposition: as for Tranche A — sandboxed diagnostic recorded, one
   exact cure run with local test-socket permission, reviewer accepts retained
   evidence; the PR pre-merge harness is the independent confirmation.
```

This run stops before Receipt 190 and Git/PR work. Those are separately owned
closeout steps after a frozen content commit.
