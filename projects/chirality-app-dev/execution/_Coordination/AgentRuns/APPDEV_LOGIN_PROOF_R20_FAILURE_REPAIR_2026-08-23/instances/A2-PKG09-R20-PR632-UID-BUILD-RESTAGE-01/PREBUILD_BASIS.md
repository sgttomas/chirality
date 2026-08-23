# Prebuild basis freeze

Observed before either authorized one-shot invocation:

- Branch: `codex/app-login-proof-r20-repair`.
- HEAD/source/build revision: `2ee96958daf997b7a156f020739bde43ca78ebf9`.
- Parent: `4a48aeaede2d050631006f8ff23fb11736752bef`.
- Frontend tree: `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- `git status --short --untracked-files=all projects/chirality-app-dev/frontend`: empty.
- `git diff --stat HEAD -- projects/chirality-app-dev/frontend`: empty.
- Git index: empty.
- Frozen dist canonical directory: `/Users/ryan/Library/Caches/chirality/electron-dist`; physical `pwd -P` is identical; non-symlink directory; mode `drwxr-xr-x`.
- Frozen dist inventory: exactly one entry, regular non-symlink `electron-v43.2.0-darwin-arm64.zip`; mode `-rw-r--r--`; size `122090802`; SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
- `package.json` SHA-256: `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`.
- `package-lock.json` SHA-256: `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`.
- Candidate fixture-test SHA-256: `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7` (retained Phase-F accepted value; not rerun here).
- Proof guard script SHA-256: `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.
- Supply wrapper SHA-256: `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db`.
- Supply verifier SHA-256: `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`.
- Network posture: ordinary workspace sandbox with restricted external network; supply/build escalation and download are forbidden. Invocation counts are supply `0`, pack `0` at this freeze.

The precondition is `PASS`. The worktree is clean for tracked files, the exact frontend is fully clean, and the only existing untracked paths are the four App-only v13 predecessor records named by the manager. Neither one-shot has started.
