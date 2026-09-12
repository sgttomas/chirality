# TASK: one replacement package after merge

Separate Type 2 packaging instance, gpt-6-astra, medium. No delegation.
Read Root/App AGENTS, TASK, this run's HANDOFF_20260912.md, current
BUILD_EVIDENCE_20260912.md, and the adjacent
APP_V3_CODEX_HOST_REPLATFORM_20260912 PACKAGING_PROCEDURE.md and build evidence.
Work from `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`
for source/records. Initial assignment is preparation only. Parent supplies the
reviewed and merged source commit before setup, build, or packaging may start.

Prepare to reuse the successful sequential flow from
`/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence/run-build.py`.
Use new detached build checkout `/Users/ryan/.claude/chirality-build-ui-recovery-20260912`,
output with suffix `-out`, and evidence with suffix `-evidence`. Never overwrite
either earlier build/output/evidence. Sources cannot be under /private/tmp.
Do not delete the earlier A2 build or any trial state.

After parent's explicit commit dispatch, create the detached checkout, npm ci
in Runtime and frontend, stage instructions, build Runtime and frontend, and run
desktop:dist once. Signing uses the recorded owner-supplied identity SHA1
`C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF` through
CHIRALITY_SIGNING_IDENTITY_SHA1. No security command, credential discovery,
notarization, stapling, native App launch, or publishing. Remove inherited Apple
notarization/import credential variables from child environment without printing
values. The existing pack entry uses --publish never. Stop and report any failed
step; do not silently retry setup/build or patch product source.

Record each command's exit and filtered log (omit every line containing @),
actual source commit, App/DMG sizes and digest, bundle identity, codesign strict
verification and hardened-runtime identities/entitlements, stock Codex pin,
dependency boundary and instruction integrity. spctl before notarization may
reject as Unnotarized Developer ID; record it as pending owner notarization,
not Gatekeeper success. Use actual packaged App/DMG paths for version identity.
Do not rerun unaffected source tests. Write a concise new build-evidence record
and return the exact artifact and limits. Parent integrates the record and owns
the owner handoff; no Git writes except the authorized detached worktree setup.

Never inspect live identity/auth/token/binding/keychain/Codex-home/session/event
files, R17 state, or intro-rehearsal. Guarded-launcher restriction remains; this
assignment does not launch a candidate App. Build-time Codex --version is the
existing pin check, not a model turn. Publishing and owner acceptance remain
separate.
