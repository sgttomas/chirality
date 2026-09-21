# V-DEL-04-04: verifier notes

These notes cover the evidence-only verifier shard for `DEL-04-04`, graded under the PKG-04
`GRADING_KEY.md` and `CONVENTIONS.md`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 1 | 0 | 2 |
| n | 12 | 12 | 0 | 0 |
| b | 2 | 2 | 0 | 0 |
| c | 2 | 2 | 0 | 0 |
| e | 3 | 3 | 0 | 0 |
| **Total** | **22** | **20** | **0** | **2** |

No Disposition was refuted. Both CONTESTED verdicts concern `CauseTag`, and in both rows the
Disposition holds.

## (ii) Systematic patterns

1. **CauseTag choice on the live-path composition rows is inconsistent.**
   - Most rows where the Runtime composition replaced the legacy PersonaComposer carry:
     - `CODEX_SOLE_ENGINE`, or `RUNTIME_EXTRACTION` with the other as `CAUSE2`;
     - DirectionEvidence `GOV:D-GOV-43; CTX:HANDOFF.md:215-218`.
     - Examples: CLM-005, CLM-010.4, CLM-010.6.
   - CLM-010.7 is the same kind of gap (a legacy preface item that is absent on the live path),
     yet it takes `UNRECORDED_JUDGMENT` with `NONE_FOUND`.
   - CLM-010.11 takes `CODEX_SOLE_ENGINE` with `NONE_FOUND`. The live rejection of unknown keys
     is general Runtime request validation (`runtime-daemon.ts:916-918`) as well as the Codex
     envelope check.
   - Both rows are defensible either way under GRADING_KEY 6, so both are CONTESTED.
2. **Residuals that tell the reader to drop the PRD warning overlook the worker's own REGISTER-1.**
   - Affected rows: the CLM-004 RemainingWork ("drop PRD warning") and the CLM-020 RemainingWork
     ("remove PRD snapshot confirmation").
   - REFERENCE_HASHES shows that PRD `Match=NO` at `00115c719`, so the PRD caution is in fact
     live again.
   - This does not change either Disposition, because both rows are STALE_SPECIFICATION on other
     grounds.
   - RemainingWork is not a keyed field, so I noted this without refuting either row. The
     manager may want to align the residuals with REGISTER-1.
3. **The shared evidence string lists `project:AGENTS` as a supplied entry.** On the live path
   `nativeProjectDiscovery: true` skips that entry.
   - Affected rows: CLM-009, CLM-016, CLM-018, CLM-023 and SEC-1.
   - The worker's reverse notes already disclose this, and the dispositions are unaffected.
   - The three errata (CLM-010.3, CLM-010.6 and CLM-010.8) are all correct.

## (iii) Capability-file accuracy

- **CAP-HARNESS-025:** the tags `REACH=LIVE` and `STATE=ENABLED` hold. `resolveInstructionRootPath`
  is imported by the live routes `working-root/{file,workflow,workflow-drafts}`, and
  `assertInstructionRootReadable` is imported only by `persona-manager.ts` and
  `agent-instruction.ts`, as the capability notes say.
- **CAP-RTCORE-038:** the tags `REACH=LIVE` and `STATE=ENABLED` hold. `nativeProjectDiscovery: true`
  is at `app-owned-composition.ts:226`. That line blames outside the four post-release commits.
- **No inaccuracies found.**

## (iv) Effort

- I read about 20 frozen-tree files, using line ranges only. They included the DEL-04-04 SoW,
  `_STATUS.md` and Dependencies, and the DEL-07-01 and DEL-07-03 `_STATUS.md` files.
- On the code side I read `runtime-method-service.ts`, `delegated-engine-adapter.ts`,
  `delegated-runtime.ts`, `codex-supervisor.ts`, `app-owned-composition.ts`,
  `persona-resolution.ts` and `persona-manager.ts`.
- On the governance side I read SPEC 13 and TYPES 3.4.
- I ran read-only `git blame -L` on TYPES 3.4, `codex-supervisor.ts:104-112`,
  `codex-supervisor.ts:181` and `app-owned-composition.ts:226`.
- The context budget was adequate.
