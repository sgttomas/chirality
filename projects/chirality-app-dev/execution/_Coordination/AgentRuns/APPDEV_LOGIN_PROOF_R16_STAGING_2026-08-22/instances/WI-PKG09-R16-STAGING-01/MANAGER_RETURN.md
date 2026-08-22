# WORKING_ITEMS manager return — DEL-09-04 R16 staging

- RunID: `APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22`
- InstanceID: `WI-PKG09-R16-STAGING-01`
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r16-staging`
- Exact basis / HEAD / origin/main:
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Manager verdict: `VALIDATED_PASS`
- Deliverable state: `IN_PROGRESS` and unproved

## Outcome

The unsigned local arm64 app was rebuilt from the exact merged detector repair
revision using the tracked R13 command `npm run desktop:pack`. The first
attempt stopped only on the pinned Electron 43.2.0 cache miss plus sandbox DNS;
the complete failure log was preserved. One manager-authorized retry of the
same tracked command with retrieval permission limited to that pinned artifact
exited zero. The tracked command's embedded packaged-dependency and
instruction-root gates passed.

A new R16 was authored entirely from current exact-merge evidence. It discloses
the earlier approximately 12:50 prior-authorized rebuild/material as
unadopted and superseded without importing any identity from it. The concrete
owner procedure now remains valid after a later documentation-only commit or
merge because it binds the built frontend tree using an empty
build-revision-to-current-HEAD frontend diff rather than requiring live HEAD
equality. It fail-closes exact proof root/plist/service uniqueness and stages
complete Step 0, prepare, PREPARED check, owner logout/login, capture,
PASS/revision, three-file preservation/hash, and verbatim owner-handoff blocks.

No GUI launch, prepare, capture, logout/login, bootstrap, kickstart, default
operator query/mutation, signing, notarization, deployment, distribution,
release, publication, staging, commit, push, or merge occurred.

## Exact package and evidence identities

- `PROOF_APP`:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- `PROOF_REVISION`: `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- bundle identifier / short version / bundle version / minimum macOS:
  `com.chirality.app` / `2.0.0` / `2.0.0` / `15.0.0`
- main executable: readable/executable thin arm64 Mach-O
- main executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- signature posture: Electron linker-only ad-hoc identity, no Team ID or
  Developer ID; app resources unsealed; no signing/notarization claim
- packaged CLI:
  `Contents/Resources/runtime-cli/chirality-cli.mjs`, present/readable,
  SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`
- successful complete package log SHA-256:
  `67f9c2de21de732f819e59cad4f4b94429cd654c227fc27653ed676d9937ce62`
- instruction-root summary SHA-256:
  `89ba0e597190205fd50e1216e9efeb9f6ea9dd53e920a27f31251ad8cfb5b468`
- instruction-root manifest SHA-256:
  `dfea68cf9b550848d5573a02c73b6647700e0543b6376bb61831c3d38d1c75d1`

The optionless live preflight returned PASS in `READ_ONLY_PREFLIGHT` mode with
no mutation, root creation, or service/job inspection. The proposed root,
exact proof plist, and exact proof job remained absent. The default operator
job, plist, and launcher were not queried or touched.

## Staged concrete values

```text
PROOF_ROOT=/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20
PUBLIC_EVIDENCE=/Users/ryan/Desktop/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20-public-evidence
```

These are documentation-only values. The proof root and plist are absent and
the exact proof label is not loaded. Actual prepare, owner logout/login,
capture, handoff, proof acceptance, and any operator deployment remain owner
acts.

## Review and checks

Fresh Agent 2 review passed all 16 items with no findings. It independently
re-ran package/CLI/signature/instruction-root identity, live preflight and
exact proof-identity absence, every staged shell block and procedure boundary,
all hashes, status/lifecycle, App containment, empty index, whitespace and
`git diff --check`. It also created an independent distinct later docs-only
synthetic HEAD and proved the staged frontend source gate remains passing with
an empty frontend diff and no live ref/index/preflight mutation.

Final checks:

- exact frontend diff: empty;
- scoped frontend porcelain: empty;
- Git index: empty;
- App-only containment: PASS;
- `git diff --check -- projects/chirality-app-dev`: PASS;
- APP-HOLD register-match scan: PASS;
- practitioner self-check: exit 0 at the existing calibrated baseline;
- practitioner pytest: 350 passed;
- proposed proof root/plist: absent;
- authorized temp recovery root: absent after reviewed closeout.

The first manager APP-HOLD invocation used an incorrect duplicated project
prefix and exited before running the scanner. The exact repo-root invocation
was then run and returned PASS; no product or evidence byte changed.

Reviewed identities:

- R16 SHA-256:
  `348397ce3f7a217492017f187c7068b7b41cd9ea0e279f8b4bf86c1daaf9108e`
- DEL status SHA-256:
  `4f9e04a3d229b9d64c83a038ba980518709684b3ed36fbb5e1d96172653b21a6`
- executor return SHA-256:
  `f24635a2392e6c5bc716a35dbf87615dbfaaa2a52e48c845b60d21558df07e88`
- fresh review SHA-256:
  `2f027dc8fcf25663f625d2d89a67b715b258ffd14b883689886c8e9bf08e312f`

## Exact repository changes

1. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
2. `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/` — owner transcription, plan/graph,
   activation, sealed briefs/amendments, complete attempt logs, executor return,
   fresh review, runtime telemetry/summary, and this manager return.

No path outside `projects/chirality-app-dev/` changed and nothing is staged.

## Authorized temp-root closeout

Only after fresh review PASS, the manager revalidated
`/private/tmp/chirality-app-login-proof-r16-superseded-20260822` as the exact
literal target, a real non-symlink directory owned by the current user, whose
resolved path exactly matched the authorization. That directory alone was
removed and its absence confirmed. It is not recoverable from that location.

## Derivative status and handoff

R16, package outputs, integrity/preflight evidence, logs, reviews and this
return are derivative evidence tied to the exact accepted source snapshot;
they do not replace source truth or establish login-session proof, lifecycle
acceptance, release readiness, signing, notarization, deployment,
distribution, publication, issuance or reliance.

No blockers remain for Git integration of this bounded R16 staging tranche.
