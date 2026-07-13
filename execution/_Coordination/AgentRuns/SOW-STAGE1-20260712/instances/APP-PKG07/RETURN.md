# APP-PKG07 Calibration Return

Verdict: `PASS`
Commit: `9f219099eddc1e17aee643bcef040706de8f8f01`
Candidate: DEL-07-03, SHA-256
`6fa7732954b95314176d81045edeb9492405785cf4568acf210968f903cc9ab0`.

All 31 mappings are `PRESERVED` and cover 339/339 source lines. Parity,
candidate validation, independent Agent-2 verification, protected-input
hashes, lifecycle neutrality, root self-check, skill/agent validation, and
scope containment pass. The four source files and `_STATUS.md` are
byte-identical; lifecycle remains `IN_PROGRESS`. Schema, project-content, and
native-substrate outcomes are PASS. No conflict, blocker, waiver, or rerun.
Evidence is under DEL-07-03 `_run_records/SOW_CALIBRATION_2026-07-12/` on the
named commit. Evidence is derivative and the legacy kit remains authoritative.

## Frozen-schema wave

Verdict: `PASS`; commit
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; worktree clean.

All six candidates validate as `PILOT_DUAL`. Their 191 mappings preserve
2,173/2,173 source lines; six independent returns pass and reproduce maps and
parity byte-for-byte. DEL-07-03 used the required frozen-source reconversion;
the other five used one first conversion each. Fresh conversion and verifier
reruns are zero. All statuses remain byte-identical and `IN_PROGRESS`;
pre-wave tracked package bytes and historical calibration evidence are
unchanged. Repeated HTML, typecheck, production build, Vitest (703 passed,
4 skipped), scope/practitioner pytest (274 passed), self-check, and exact
50-path containment pass. Receipt 51 and the project handoff are on the named
commit. Final classifications: schema/content/preservation PASS; serialized
conversion `SUBSTRATE_FALLBACK`, followed by native verifier PASS. The initial
missing `node_modules` condition was resolved with `npm ci` and was not a
conversion/test rerun. No blocker, conflict, waiver, or rerun requirement.
