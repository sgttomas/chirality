# PIP-PKG13 Calibration Return

Verdict: `PASS`
Commit: `64aceb781bd26b148648922a4e103aa49096c4d1`
Candidate: DEL-13-01, SHA-256
`6c76b2c785acc56ee1e67aaba64930e457b8c2ca20d4d9e8b4156cebe579c43d`.

All 26 mappings are `PRESERVED` and cover 280/280 source lines. Parity,
candidate validation, independent Agent-2 verification, protected-input
hashes, lifecycle neutrality, focused schema/dependency checks, deterministic
HTML, harness pytest (264 passed), self-check, and containment pass. The four
source files and `_STATUS.md` are byte-identical; lifecycle is `IN_PROGRESS`.
Schema and project-content outcomes PASS. The initial author TASK launch hit
the four-slot runtime cap and used D-GOV-15's sequential fallback; this is
classified `SUBSTRATE_FALLBACK`, while the later native verifier PASSed. No
content conflict, blocker, waiver, or rerun. Evidence is derivative under
DEL-13-01 `_run_records/SOW_STAGE1_CALIBRATION_2026-07-12/`.

## Frozen-schema wave

Verdict: `PASS`; commit
`31c35ea9798c29cd0af16b7089186f3942dcfcb1`; worktree clean.

All four candidates validate as `PILOT_DUAL`. Their 134 mappings preserve
1,293/1,293 source lines; four independent returns pass. DEL-13-01 used the
required frozen-source reconversion, DEL-13-02/03/04 each used one conversion,
and there were zero fresh conversion or verifier reruns. All four statuses
remain byte-identical and `IN_PROGRESS`; the ISSUED baseline and historical
evidence are untouched. Repeated HTML, focused tool/artifact/dependency checks,
harness pytest (264 passed), and self-check pass. Final classifications:
schema/content/preservation PASS; serialized conversion remains separately
`SUBSTRATE_FALLBACK`, followed by native verifier PASS. Receipt 43 and the
project handoff are on the named commit. No blocker, conflict, or waiver.
