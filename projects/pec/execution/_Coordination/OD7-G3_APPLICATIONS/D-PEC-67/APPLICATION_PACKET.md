# D-PEC-67 OD7-G3 — Single-Carrier Composite Application

**Status:** EXACT APPLICATION CANDIDATE — NO LIVE APPLY
**Owner composite gate:** OPEN
**Current basis:** `a6b10683219c22f45f31e3dffa4fb164b4582051`
**Provisional carrier:** `D-PEC-67`

## Required section approvals

All seven section gates in `../SECTION_INDEX.csv` must be separately approved
by exact identity. The carrier does not merge their authority. If any section
is rejected or amended, this composite must be regenerated.

## Exact live write surfaces if later approved

- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-67_od7_g3_boundary_dispositions.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `projects/pec/docs/PRD.md`
- `projects/pec/AGENTS.md`
- `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`
- `projects/pec/execution/_Scripts/pec_reliance_hold.py`
- `projects/pec/execution/_Scripts/tests/test_pec_reliance_hold.py`
- `projects/pec/execution/_Scripts/README.md`
- `tools/REGISTRY.md`
- `execution/_Coordination/NOTICE_2026-07-27_D-PEC-67_OD7-G3_BOUNDARY_DISPOSITIONS.md`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-07-27_D-PEC-67_OD7-G3_INTERFACE_CLARIFICATIONS.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md` (one additive receipt, exact number and verbatim owner
  ruling resolved at application-time rescan)
- `projects/pec/execution/_Coordination/OD7-G3_APPLICATIONS/D-PEC-67/` (the accepted application packet, section approvals, owner
  ruling, validation, and handoff)

No decomposition, ScopeOfWork, runtime, implementation, profile, lifecycle,
release, dependency, estimate, schedule, or other notice surface is implicit.

## Load-bearing candidate identities

- `DECISION_RECORD_CANDIDATE.md` — SHA-256 `268d0c06ab125070d2b57ea2b38c0acef6601ab17a879b403b06d4aae8ff40a0` (pre-ruling D-PEC-67 record)
- `candidate_live/REGISTER.md` — SHA-256 `49a13898b1ad28077c2de419a8bd827c25b6e9435382ac9164b8ffb8c4ed2f6a` (single-row register postimage)
- `candidate_live/PRD.md` — SHA-256 `b4f30890fd62e7474080429d85aa8cad232b5aff392c8a4fe0d2a2901c6df7d2` (integrated K03-A plus K11-A PRD postimage)
- `candidate_live/AGENTS.md` — SHA-256 `20ce48df9ca4a73f838defd0f2bf85aecf97db1a11f523f5ee2f7bc74f1c4390` (PEC overlay hold preflight postimage)
- `candidate_live/ACTIVE_RELIANCE_HOLDS.csv` — SHA-256 `d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a` (authoritative L-A1 hold register)
- `candidate_live/pec_reliance_hold.py` — SHA-256 `53f9f6e4dbdeaa16d9f6cba140d0c15bf373b936d7af48437c4a98ae833470c1` (deterministic hold preflight)
- `candidate_live/tests/test_pec_reliance_hold.py` — SHA-256 `6238d4a680c472354b4134dc71a7e03c4b0e200430780ccb07a98373625f5cad` (deterministic hold regression tests)
- `candidate_live/SCRIPTS_README.md` — SHA-256 `9f9a8eb23d1d521529ab0f33326296891d2d428072eec507dbe08e3db8b354ec` (PEC execution-script contract)
- `candidate_live/TOOLS_REGISTRY.md` — SHA-256 `6a74063b945b8b91c8b5174dc1703d5462761f0a053284d599a37a4c6c946a6b` (root tool-registry postimage)
- `candidate_live/NOTICE_ROOT.md` — SHA-256 `7692f9ed4393fbdb32fc44278d102c96cc837474bb5a04cc461fdd4f8809e995` (non-binding Root notice)
- `candidate_live/NOTICE_APP.md` — SHA-256 `923b905f9454aa3b3aa57889b8f6b55f3fb877abdbdbe33ab8ef42a288e2c3d8` (non-binding App notice)

## Dependencies

1. `D-PEC-67` and the application archive path remain absent after the
   execution-time register and candidate-reservation scan.
2. Every section gate is separately approved by exact identity.
3. The live PEC register, PRD, AGENTS overlay, and receipt file reproduce
   their manifest preimages.
4. The two new PRD rows are adopted by this act, but C3/C15 propagation waits
   for later PEC SCOPE_CHANGE.
5. L-A1 becomes authoritative in this act; L-A2 remains unapplied.

## Application rule

The owner ruling is copied verbatim into the durable decision/application
record. That transcription and the next receipt number are the only
application-time substitutions permitted. Any other byte change returns as a
new exact candidate.

## Rollback

Before Git closeout, restore existing surfaces to the exact preimages and
remove only new enumerated surfaces. After Git publication, use a separately
approved revert or supersession; never rewrite the ruled record.
