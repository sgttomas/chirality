# SCA-004 run summary

Applied 2026-09-12 by a bounded TASK executor on branch
`claude/chirality-codex-replatform-3999f1` under D-GOV-43 item 11. Nine
`HELD_UNAVAILABLE` bindings closed; DEL-02-07 through DEL-02-12 RETIRED;
DEL-02-06 revised in this packet (its `ScopeOfWork.md` bytes are unchanged, see below); `GATE_READINESS.md`, `docs/PRD_AUTHORITY.md`, `HANDOFF_STATE.md` and `MIGRATION_ACCEPTANCE_2026-09-06.md` superseded by appended entries. Registers,
SOURCE_SCOPE_REQUIREMENTS and the DECOMP document are unchanged as the frozen
Gate3 basis. Historical `AgentRuns/RUNTIME_*` records are unchanged.

Preimage SHA-256:
- `execution/_Decomposition/HOLD_SUCCESSOR_MAP.csv` `635fa7f9a05f0a1d17dc47e4db12e142433b11cdc7894708935d0515659ab882`
- `execution/_Decomposition/GATE_READINESS.md` `426b29a947cbb7a35dc1b98fd4a7fb777cdf7983a9cb87bd3abd0355768383ca`

Postimage SHA-256 (also re-issued once in `docs/PRD_AUTHORITY.md`):
- `execution/_Decomposition/HOLD_SUCCESSOR_MAP.csv` `0bcae8529209aa0de46dfbecbc181048b02d4f0a1511db120feade202abc8c8f`
- `execution/_Decomposition/GATE_READINESS.md` `11ef70c412ffc0ee3541983c6cc0fce293c856a8fa4e7562fdde271d966bafa5`

Unchanged by design (Root-pinned records): `docs/PRD.md` (its D-GOV-43 reading is
`PRD_REVISION.md` in this packet), `execution/_ScopeChange/_LATEST.md`
(pinned by the Root successor adoption of 2026-09-07; SCA-003 remains the last
accepted Runtime scope change, and this packet is a ruling application, not a
new accepted scope change), `execution/_Coordination/MIGRATION_APPLICATION.md`
and `DEL-02-06/ScopeOfWork.md` (both pinned by the Root effective governance
state of 2026-09-06). The DEL-02-06 revision notes are recorded in
`Impact_Assessment.md` of this packet and in the DEL-02-06 `_STATUS.md` history;
the pinned bytes are read with D-GOV-43 (ruling item 11: historical records are
not rewritten).


Handoff state: DecompositionTruthState=`APPLIED_UNDER_D-GOV-43_ITEM_11`;
DerivativePackageState=`SCA003_SNAPSHOT_CURRENT_READ_WITH_D-GOV-43`;
DownstreamRerunState=`NONE_REQUIRED`; ReadyForNextPhase=`TRUE` for the
functional spike. Closure is the reviewed and merged pull request. No
release, publishing, activation, Piping or local-model act.
