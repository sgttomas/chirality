# Orchestration Plan — Root v3 Phase 0c

PlanVersion: `1`
RunID: `ROOT_V3_PHASE0C_2026-08-23`
SelectionAuthority: `HUMAN`
Posture: `MIXED`
SupervisingRole: `HELP_HUMAN`
AcceptedBasis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`
OwnerSteerSHA256: `ef2ffa62949b870671ccd00d2384429a0b1c97bb9d52259034448c6662cd0eca`
R2RecordSHA256: `63b174f00860cd31dbdde1f734a9e1ca08c44f7cd2ed51f7716612f3847a6bce`

## Objective and authority

Execute exactly the two owner-selected Phase-0c nodes: draft, without applying,
the SCA-004 Gate-3 exact amendment candidate and Gate-4 propagation plan; then
backfill the D-GOV-34 and D-GOV-35 Git-act SHA slots from recorded evidence.
The basis gate and idle-workplan Step 0 passed before this plan was written.

## Work graph

| Node | Lane | Content ownership | Dependency | Expected return | Fan-in gate |
|---|---|---|---|---|---|
| N1 | SCOPE_CHANGE | `execution/_ScopeChange/SCA-004_2026-08-22_1749/**` only | verified basis and R2-A | deterministic Gate-3 candidate, exact diff, Gate-4 plan, validation, decision/handoff state | zero-failure validator; protected bytes unchanged; fresh independent review PASS |
| N2 | HELPS_HUMANS | exact D-GOV-34/35 records, their register rows if required, and one new live manifest | verified basis and recorded Git evidence | evidence-bounded SHA/status backfill and schema-valid manifest | slot-only record diffs; CI-form G4 and instruction validators PASS; fresh independent review PASS |

N1 and N2 may author concurrently because their content write sets are
disjoint. Each instance owns only its own control-plane subfolder. Git commits
are serialized by CHANGE in the owner-prescribed order N1 then N2. Receipt 116,
run-level final validation and handoff, push, and PR creation occur only after
both reviewed commits fan in.

## Human gates and stops

Gate 3 and Gate 4 are drafting only and return separately to the owner against
published exact bytes. No Gate 5, live decomposition or companion-register
write, `_LATEST.md` write, `_STATUS.md` write, new deliverable folder, Task
Management change, runtime/project/tool/export write, sync/rebase, or merge is
authorized. If `origin/main` advances, stop and request owner sync authority.
Publication is one human-gated PR; self-merge is false.

## Closure contract

Accept only complete Agent-2 returns and fresh zero-actionable-finding reviews.
Preserve failures and repair cycles. Final closeout appends Receipt 116 with
both verbatim CHAT_TRANSCRIPTION blocks, records every hash, commit, check and
open gate, updates the Root handoff, pushes normally, opens one PR, and stops
without merge.
