# Sealed Agent 2 brief — proof-test typing remediation 05

- ChildInstanceID: `A2-DAPP100-IMPLEMENT-05`
- TaskSkill: `software-bounded-implementation`; ApplyEdits: `true`.
- Objective: correct only the TypeScript overload compatibility of the `canonicalize` and `makeTemp` test doubles in the short-socket proof test while preserving behavior and coverage.
- Detection evidence: `npm run validate:release-quality` nested full suite passed 1139 tests/4 skips, then typecheck failed at proof-test lines 36-37 because simple `(string) => Promise<string>` doubles did not satisfy overloaded Node `realpath` and `mkdtemp` types.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts`; this run root `REMEDIATION_RETURN_05.md`.
- AcceptanceCriteria: focused proof tests pass; frontend typecheck passes; no production/proof/runtime/dependency/Git changes.
