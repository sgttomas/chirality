# PKG-09 activation — DEL-09-04 packaged SDK proof

- RunID: `APPDEV_PACKAGED_SDK_PROOF_2026-08-20`
- Parent: `HELP_HUMAN`
- Manager: `WORKING_ITEMS`
- ManagerInstanceID: `WI-PKG09-DEL0904-PACKAGED-SDK-01`
- PackageID: `PKG-09`
- SelectedDeliverable: `DEL-09-04`
- AcceptedBasis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`
- Branch: `codex/app-packaged-sdk-proof-20260820`
- Authority: D-APP-97 C1; APP-HOLD dispatch preflight `ALLOW` on this basis.
- Objective: add and prove the existing packaged Agent SDK runtime verifier against both the staged packaged app and the read-only mounted unsigned DMG app in the Desktop Unsigned Artifact Verification workflow, preserving scripted no-live-provider operation and stable parseable JSON evidence uploaded with the unsigned CI artifact.
- Posture: `TERMINAL_FAN_OUT_IN`, serialized implementation then independent review.
- Model attribution: OpenAI Codex agents; exact builds are not exposed by the runtime.
- External proof surface: the macOS staged-app and mounted-DMG executions are `REQUIRED / PR-CI-OWED`; they are not inferred from local static checks.

## Fences

No signing, notarization, publication/distribution, release-readiness claim, provider/network expansion, credential access, lifecycle transition, Checking Approval SHA change, owner-machine LaunchAgent deployment, dependency repin, lockfile change, foreign-loop write, commit, push, PR, or merge.
