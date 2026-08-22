# Executor return — A2-PKG09-R16-EXECUTE-01

## Result

`PASS — EXACT-MERGE UNSIGNED BUILD AND R16/STATUS STAGING COMPLETE; FRESH REVIEW REQUIRED`

- Parent: `WI-PKG09-R16-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r16-staging`
- exact `HEAD` / `origin/main`:
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- index: empty
- proof status: not run; DEL-09-04 remains `IN_PROGRESS` and unproved
- blockers: none

## Execution and evidence

The pre-build fail-closed gate passed: exact branch/revisions, clean index and
tracked tree, empty frontend porcelain, absent proposed root/plist, and absent
exact proof job. Only manager-created untracked files under this new run root
were present.

The first exact `npm run desktop:pack` attempt exited `1` on sandbox DNS during
the pinned Electron `43.2.0` arm64 cache miss. The executor stopped, reported
the boundary, and adopted locked amendment 01. The one authorized retry ran
the exact same tracked command from the exact frontend cwd with network
permission limited by purpose to that pinned artifact retrieval. It exited
`0`. No dependency, manifest, lockfile, source, or provider changed.

Primary evidence:

| Evidence | SHA-256 |
|---|---|
| `executor/desktop-pack.log` (failed attempt) | `827459042c5115f7b0e1ac14d9a25d9550bc48ddf1b1cf5442adafc4d1975ee5` |
| `executor-attempt-2/desktop-pack.log` | `67f9c2de21de732f819e59cad4f4b94429cd654c227fc27653ed676d9937ce62` |
| `executor-attempt-2/package-identity.log` | `038429e3922bf116335c58867306d91bed941fa6e84da6a57a928636a4e61d18` |
| `executor-attempt-2/codesign-executable.log` | `ed95764d6ca7b0c17d7ca066fe76f5f20a900d69cc11784428eae20407eb6dfa` |
| `executor-attempt-2/integrity-evidence.log` | `708d914e9d96b6d2f3a5e20aa5cfe7427da1e83ea1184d0a0338b7b1f93f01f9` |
| `executor-attempt-2/post-build-git.log` | `2e530b21023c537d221ec4427ec13615f473f735f420ea844ac4197b1c24cc55` |
| `executor-attempt-2/preflight.log` | `61337ccf4dc63ff98578f37dce3bcfcb812881d97e15ec5823104fb87855b5c0` |
| `executor-attempt-2/preflight-boundaries-before.log` | `30de2e3ec990035ab1934c782f59c0fb83bc084537cb62784b6d6a93d6b5747f` |
| `executor-attempt-2/preflight-boundaries-after.log` | `6b9908b811c5e8db749784dfc7f27100f160a79a0cce6ed96f3d9eca168f004b` |
| `executor-attempt-2/post-commit-portability.log` | `f2866bcb9f8c12aa1ba8dcf728aeeda87a64ff8db3917e0625d3f3b9a28e3c28` |
| `executor-attempt-2/post-commit-portability-setup-failure.txt` | `089f4b855a9eff9bb01fca4a7eff1a70fc19500f8aea613bbc9d4676c7d09751` |
| `executor-attempt-2/amendment-02-exact-absence-gate.log` | `014b8e2d588ba4275525c5e298283ecbc6b1ffa12a680904a2617bdbacc3bc56` |

The successful tracked command passed its embedded packaged dependency
boundary and instruction-root integrity gates. The current summary is `pass`,
binds exact Git SHA `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`,
and checked `43` files. Summary SHA-256:
`89ba0e597190205fd50e1216e9efeb9f6ea9dd53e920a27f31251ad8cfb5b468`;
manifest SHA-256:
`dfea68cf9b550848d5573a02c73b6647700e0543b6376bb61831c3d38d1c75d1`.

## Package identity

- app:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- identifier/version/build/minimum macOS:
  `com.chirality.app` / `2.0.0` / `2.0.0` / `15.0.0`
- executable: readable/executable thin arm64 Mach-O
- executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- signature display: only ad-hoc/linker-signed; no Team ID or Developer ID;
  Electron Builder skipped application signing
- CLI: present/readable; SHA-256
  `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`

The strict read-only signature verification exits `1` because the
linker-signed executable has no sealed resources. This exact calibrated result
is recorded; it is not upgraded into a sealed signature claim.

## Preflight and absence

The committed optionless `preflight` exited `0` with `PASS`,
`READ_ONLY_PREFLIGHT`, all identity checks true, no mutation, no proof-root
creation, and no service/job inspection. The proposed root remained absent
before and after, and the exact proof plist/job remained absent. No default
operator job, plist, or launcher was queried or touched.

## Applied changes

1. New R16:
   `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`
   - SHA-256:
     `348397ce3f7a217492017f187c7068b7b41cd9ea0e279f8b4bf86c1daaf9108e`
2. Minimal status amendment:
   `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
   - SHA-256:
     `4f9e04a3d229b9d64c83a038ba980518709684b3ed36fbb5e1d96172653b21a6`
3. Complete executor evidence under this instance's `executor/` and
   `executor-attempt-2/` directories.

R16 was written only from fresh exact-merge evidence. It contains the required
prior approximately `12:50` supersession disclosure without adopting any
earlier byte or identity. It stages concrete, independently copy-pasteable
Step 0, prepare, prepared-check, owner-act, capture, PASS/revision,
preservation/hash, and owner-handoff documentation. All extracted shell blocks
pass `/bin/zsh -n`, and no required value is a placeholder.

Pre-review amendment 02 removed the non-portable live
`HEAD == PROOF_REVISION` assertion. Step 0 now retains the repository-toplevel
check, treats an empty build-revision-to-current-HEAD frontend diff as the
authoritative source gate, requires the exact proof plist to be absent, and
requires unambiguous exact-label not-found classification from `launchctl`
exit `113` plus its exact two-line output. A temporary scratch Git copy created
distinct synthetic later docs-only commit
`22e689882f0e99d78e24cbd1fa98911077259cf3`; its only change was the synthetic
App documentation path, while the authoritative frontend diff was empty and
the source gate exited `0`. That portability check did not run preflight or any
host mutation and did not change the live ref, index, status, or package.

## QA and containment

- `git diff --check -- projects/chirality-app-dev`: PASS
- extracted R16 shell-block syntax: PASS
- exact frontend commit-to-HEAD diff: empty
- exact frontend porcelain: empty
- index: empty
- tracked source/manifest/lockfile/dependency changes: none
- synthetic later docs-only `HEAD` portability gate: PASS
- all dirty/untracked paths: inside `projects/chirality-app-dev/`
- allowed product/deliverable writes: exactly R16 and `_STATUS.md`
- proposed proof root: absent at final check
- prohibited actions: none

## Derivative status and rerun

R16, the ignored package, integrity artifacts, preflight output, and executor
logs are derivative evidence tied to exact source snapshot
`06f60e42e35ea5c39abf9e33c4d3e877d77c4497`; they do not replace source
truth. No proof, release, signing, notarization, deployment, distribution,
publication, lifecycle, issuance, or reliance claim is made.

Fresh evidence-only review is required before Git integration. Rebuild and
restage if the frontend tree or executable hash changes. Stop and select fresh
proof values if the proposed root, exact plist, or exact label ceases to be
unique and absent. Actual prepare/logout/login/capture and proof acceptance
remain owner acts.
