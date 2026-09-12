# Stage26 / R17 packaging brief

Phase A dispatched by HELP_HUMAN after the restart-admission repair landed
(commits 15a07bdef, 5045178d4 on the integration checkout). Separate TASK
`r17_packaging`, Claude Fable 5.1 medium, no delegation, prepares and later
packages. The independent recipe reviewer is a separate instance. HELP_HUMAN
retains Section B (R16 retirement), guarded launch and all native testing.

Use only the integration checkout
`/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`
(a git worktree sharing `/Users/ryan/dev/chirality/.git`; run every command
from it). Derive one consolidated Stage26/R17 candidate from completed Stage25
(`/private/tmp/chirality-local-human-trial-20260910-25`, read-only, never
modified) the way Stage25 was derived from Stage24 (`derive-stage25.py`,
`STAGE25_FROZEN_PROCEDURE.md`, `stage25-preparation-manifest.json`,
`L_STAGE25_PACKAGING/PREPARATION.md`, `PACKAGING_REVIEW.md`, `RETURN.md`,
`FINAL_REVIEW.md`). Read those before deriving; do not rerun historical
commands blindly.

Static inputs are unchanged from Stage25: the qualified, owner-approved
root-directory supplier correction
(`/private/tmp/chirality-supplier-root-directory-fix-20260911-01/artifact/codex`),
the unchanged official code-mode host with its host-only allow-jit policy,
the qualified raw native addon, the Electron cache, `npmRebuild=false`, and the
directory-plus-two-executable account-free observer closure. No supplier
download, host/V8 build, native rebuild or new supplier source/build. Only the
frozen source commit changes: it carries the reviewed five-file App batch
(interruption status, session sidebar, composer scrolling), the Runtime
restart-admission renewal, and one test-only correction. Payload hashing at
daemon start and sign-in stays removed; sealed metadata and code-signature
checks remain. Never add `/` to recursive Runtime read roots.

New stage root: `/private/tmp/chirality-local-human-trial-20260910-26`
(create-only, mode 0700). Durable R17 paths must be absent until their steps:
`/Users/ryan/Applications/Chirality Trial 20260910 R17.app`,
`/Users/ryan/Library/Application Support/Chirality Trial 20260910 R17`,
`/Users/ryan/Applications/Launch Chirality Trial 20260910 R17.command`
(derived from the accepted R16 launcher with only its three R16 references
changed; record the expected diff and hash). The running R16 trial (R16 App,
userdata, `com.chirality.runtime` LaunchAgent naming the R16 executable,
daemon pid) is left untouched by every step you run; only the lead's Section B
retires it before the first R17 GUI launch.

Phase A (now): prepare the exact recipe, tools, procedure document, phase-a
checks and preparation manifest without build, signing, provisioning or
launch. Do not run the create-only source freeze tool and do not freeze the
input manifest until the lead supplies the released commit after the pending
independent source review; write the procedure with `<FROZEN_COMMIT>` and note
the expected value (`git rev-parse HEAD` at dispatch) as tentative. Confirm
the checkout is clean apart from this coordination directory. Phase B remains
unexecuted until recipe review and explicit lead release.

Phase B (after release): one consolidated build and the existing distinct
packaging checks, stopping on the first failed gate and preserving its
evidence. Routine correction within scope returns to the lead; never silently
retry a build or broaden scope. No duplicate broad test suites: the lead has
already run the Runtime and frontend suites for this source.

Boundaries: no protected live identity/auth/binding/Codex-home/session/event
reads, no credentials or keychain, no opening any App bundle, no Computer
Use, no network beyond what the accepted recipe already performs offline.
Filter any harness or desktop log output with `grep -v '@'` before recording
it. Preserve all prior worktrees, stages, Apps, userdata, caches and failed
evidence. No publishing.

Return for Phase A: `L_STAGE26_PACKAGING/PREPARATION.md` with the manifest
path and SHA-256, the exact static delta versus Stage25 (expected: source
commit only), the procedure path, read-only checks performed, and anything
that could not be derived. Then stop and wait for the lead.
