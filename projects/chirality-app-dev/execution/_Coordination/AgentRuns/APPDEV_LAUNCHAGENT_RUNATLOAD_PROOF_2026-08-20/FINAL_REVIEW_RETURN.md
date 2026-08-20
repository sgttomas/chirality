# Final Integrated Review Return

- Verdict: `FAIL`; the product proof is safe and the retained CI evidence is
  valid for its bootstrap-triggered claim, but the fan-in overstates closure of
  the authoritative login-time residual.
- Reviewed basis: `origin/main@7584de0a8d53d69a135c22fe39a78cb4a30b6cb2`
  through `dcd10fa83bdff2ba89733bfd96176b6831591173`, plus every current
  uncommitted fan-in path named by the brief.
- Scope audit: `PASS`; deterministic committed-range and dirty-tree scope
  validation found no changed path outside the declared tranche/fan-in roots.
- Evidence-coverage audit: `PASS`; affected-check selection requires
  frontend test/typecheck, practitioner pytest, self-check, and APP-HOLD. The
  supplied local/CI evidence covers those checks and additionally covers build,
  G4, receipt validation, and the macOS proof surface.
- Product/workflow/G4 audit: `PASS`; no actionable code-safety finding. PR
  #590's `opened/synchronize/reopened/labeled` event set and `artifact-proof`
  job condition are byte-preserved. The proof uses the packaged CLI, a unique
  non-default label, the real disposable account LaunchAgents directory,
  bootstrap without kickstart, exact job/process identity checks, bounded
  fail-closed cleanup, and retained PASS/FAIL evidence. The G4 manifest names
  the two instruction surfaces and preserves all release/lifecycle fences.

## Actionable findings

1. **HIGH — The fan-in removes the login-time Remaining item without executing
   a login-time load.** The accepted residual explicitly says that bootstrap
   proved `RunAtLoad` but did not prove login (`R6_DAEMON_SERVICE_2026-07-25.md`
   lines 144-146). The retained summary again says `bootstrapOnly: true`, and
   the new script calls `launchctl bootstrap` directly; placing the plist in
   `~/Library/LaunchAgents` does not exercise login-session discovery/loading.
   Nevertheless `_STATUS.md` lines 26-27 removes the login-time item,
   `MEMORY.md` lines 3-10 says the gap is closed and only the owner-machine act
   remains, R11 lines 23-28 declares the same state effect, and the completion
   log, Receipt 182, and Agent-0 handoff repeat that closure. Impact: the live
   work-discovery surface loses an authorized, unproved acceptance item and the
   handoff reports a stronger result than the external proof supports.
   Remediation: retain a narrowed Remaining item stating that real-directory,
   bootstrap-triggered `RunAtLoad` now passes but actual login-session
   discovery/auto-start remains unproved; calibrate MEMORY, R11, the completion
   log, Receipt 182, and HANDOFF_STATE to record this as material partial
   engineering progress rather than closure. Alternatively, supply a real
   fresh-login proof before removing the item.

2. **MEDIUM — Receipt 182 claims the required integrated review before it has
   passed.** `LOOP_RECEIPTS.md` line 5457 cites `final fresh review 04`, but
   review 04 covered the pre-CI product candidate, not the current fan-in
   closeout files; this integrated review is the first review of those files
   and currently fails on finding 1. Impact: the receipt's Checks record is not
   true for the integrated candidate and does not evidence the owner-required
   integrated-diff review. Remediation: after correcting finding 1, rerun a
   fresh integrated review over the complete candidate and cite its PASS return
   in Receipt 182 (rather than relying on product review 04 alone).

## Residual risk

- A real logout/login or equivalent login-session recreation remains an
  external host-capability proof. The current CI run materially strengthens
  evidence for install path, packaged identity, `RunAtLoad` response to
  bootstrap, cleanup, and default-target protection, but does not cross that
  final boundary.
- No release, signing, notarization, distribution, lifecycle, reliance, owner
  machine, dependency, or lockfile authority is created by this review.

## TASK return

- `RUN_STATUS:` `FAILED`
- `ControlSurface:` `FILE`
- `TaskProfile:` `NONE`
- `TaskSkill:` `software-code-review`
- `ScopePath:` `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- `ResolvedSkillPath:` `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`
- `ResolvedSkillVersion:` `1`
- `ResolvedTaskProfileRequirement:` `NONE`
- `CompanionFiles:` `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`
- `AllowedTools:` `python3 tools/software_workflow/select_affected_checks.py:*`; `python3 tools/software_workflow/validate_change_scope.py:*`; `python3 tools/software_workflow/compare_structured.py:*`; `python3 tools/software_workflow/verify_generated_manifest.py:*`
- `ToolsUsed:` `python3 tools/software_workflow/validate_change_scope.py`; `python3 tools/software_workflow/select_affected_checks.py`
- `ToolPolicyCompliance:` `PASS`
- `WriteAuthorization:` `EXPLICIT_BRIEF_TEXT` — this return only
- `RuntimeOverrides:` none
- `Outputs:` this review return
- `MISSING:` actual login-session proof
- `NEEDS_HUMAN_RULING:` none; claim calibration can proceed under existing instruments
- `DEPENDENCY_NOTES:` none
- `AppliedChanges:` created only `FINAL_REVIEW_RETURN.md`
