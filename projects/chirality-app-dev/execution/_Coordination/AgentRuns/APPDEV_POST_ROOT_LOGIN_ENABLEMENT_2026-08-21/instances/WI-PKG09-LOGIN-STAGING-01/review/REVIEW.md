# A2-PKG09-LOGIN-REVIEW-01 — Node 3 review

- Reviewer: fresh ephemeral generalist Agent 2
  `A2-PKG09-LOGIN-REVIEW-01`
- Scope: 100% of Node 3 persistent diff and current generated build evidence
- Verdict: `FAIL — ONE ACTIONABLE FINDING`
- Repair performed: none (evidence-only review)

## Review matrix

| # | Result | Evidence |
| ---: | --- | --- |
| 1 | PASS | `executor-attempt-2/desktop-pack.log` records exact `npm run desktop:pack`, cwd `projects/chirality-app-dev/frontend`, and exit `0`. The current app exists at `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`; metadata independently resolves to `com.chirality.app`, version `2.0.0`, minimum macOS `15.0.0`, and thin `arm64`. |
| 2 | PASS | Executor return, generated integrity summary, R13, and current `HEAD` all identify exact commit `1b375af4f1219ecfc00fc2755854aa7fd4220901`. The commit exists and is 40 hexadecimal characters. |
| 3 | PASS | Independent `git diff --quiet 1b375af4f1219ecfc00fc2755854aa7fd4220901..HEAD -- projects/chirality-app-dev/frontend` returned `0`; scoped staged, unstaged, porcelain, and untracked checks were also empty. |
| 4 | PASS | The current summary SHA-256 is `1028e49effe50da36cef27e7d2e05a5fcf1dc0369bc418f3c05e683c4d61cd82`; it records `status: pass`, `gitSha` equal to the build commit, and `checkedFileCount: 43`. Source and bundled `agents/AGENT_HELP_HUMAN.md` independently hash to `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`, are 10,073 bytes, and compare byte-identical. R13 accurately preserves `sourceCompleteness.status: needs_remediation` for absent candidate `examples` while the required comparison row remains `satisfied`. |
| 5 | PASS | `PROOF_APP` exists; `PROOF_REVISION` matches the package summary and `HEAD`; `/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa` is absent. The concrete label has the required `com.chirality.ci.runatload.login.owner.` prefix, its canonical plist is absent, and `launchctl print gui/501/<label>` returned not-found (`113`). |
| 6 | **FAIL** | R13 keeps prepare, logout/login, and capture separate and does not claim execution, but its two advertised copy-paste blocks omit R12's required repository-root execution context. See finding `F-01`. |
| 7 | PASS | No proof root or proof plist exists and the proof label is unloaded. The operator job remains loaded separately as `com.chirality.runtime`; the operator plist and launcher still hash to `2ebc556673d7dc1232a9e230a88a75355dec6916ad6c432f707a525b29a6c7bc` and `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`. Executor evidence and persistent state consistently record no GUI launch, prepare/capture, bootstrap/kickstart, logout/login, operator mutation, artifact-proof label, signing, notarization, distribution, provider expansion, release, or issuance act. |
| 8 | PASS | R13 records the first future authorized GUI-launch launcher rewrite as an accepted expected operator-facing effect, explicitly not a park condition and not performed or authorized by this staging record. |
| 9 | PASS | DEL-09-04 remains `IN_PROGRESS`. `_STATUS.md` and R13 retain prepare, logout/login, capture, proof acceptance, deployment, and release boundaries as owner acts or open work, and R13 requires rebuild after a frontend change plus new values if uniqueness/absence changes. |
| 10 | PASS | Node 3 persistent writes are limited to DEL-09-04 `_STATUS.md`, R13, and the unique WI-PKG09 instance. Generated frontend outputs are ignored by the applicable Git rules. The index is empty, `origin/main..HEAD` has no commit, and no shared receipt/completion surface was written by Node 3. |
| 11 | PASS | Tracked diff-check, trailing-whitespace scan, fence balance, referenced paths, summary/manifest hashes, app metadata, executable SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, and evidence directories all resolve. The functional copy-paste issue is isolated as `F-01`. |
| 12 | PASS | R13 transparently classifies the record/build outputs as derivative evidence, records the initial `ENOTFOUND github.com` cache-miss attempt and fresh bounded retry, keeps the retry evidence distinct, states no current agent blocker, and preserves owner-act blockers and rebuild/reselection triggers. |

## Actionable finding

### F-01 — Owner blocks are not self-contained at their required working directory

R12 requires the procedure to run **from the repository root**
(`R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`, lines 53–61). R13 calls
both phases copy-paste blocks, but the prepare command at lines 118–125 and the
post-login capture command at lines 136–140 invoke the repository-relative
path `projects/chirality-app-dev/frontend/scripts/...` without setting or
stating the repository-root cwd. A block pasted from the default post-login
shell directory will fail before the proof harness runs; the capture block is
especially exposed because it executes after a separate logout/login phase.

Action: make each phase independently executable from its stated context by
adding an explicit concrete repository-root `cd`/cwd instruction to both
phases, or by using the concrete absolute script path in both blocks. Preserve
the two-phase separation and all current owner/proof fences.

## Final verdict

`FAIL — ONE ACTIONABLE FINDING`. All build identity, integrity, containment,
state, and claim-boundary checks pass. Repair `F-01`, then perform the required
fresh review; do not treat this review as authorization to run either owner
phase.
