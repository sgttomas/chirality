# Orchestration Plan — Root v3 Phase 0

- Run ID: `ROOT_V3_PHASE0_2026-08-22`
- Plan version: `3`
- Selection authority: `HUMAN`
- Descriptive posture: `MIXED`
- Supervising role: `HELP_HUMAN`
- Working root: repository root
- Branch: `codex/root-v3-phase0-2026-08-22`
- Exact branch basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Owner steer: `plans/steers/chirality_app_v3_phase0_steer_root_2026-08-22.md`, SHA-256 `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3`
- Owner G0 record: `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`

## Aligned objective and authority

Create only the governed Root Phase-0 basis authorized by the owner steer:
the D-GOV-35 proposal packet, DEL-02-03 M2 preparation, and SCA-004 Gate-1
assessment with its objective-relative release-pathway graph. No hold,
lifecycle, pointer, pin, implementation, release, publication, or merge gate
is lifted. The G0 record amends the non-governing Revision 3.1 input where it
says `AMENDS PLAN`.

The steer passed its complete pre-write basis gate. Root Step-0 guards G0–G4
also passed before this run package was created.

## Nodes and ownership

| Node | Runtime role/form | Content write ownership | Dependencies | Expected return | Fan-in gate |
|---|---|---|---|---|---|
| N1 | `HELPS_HUMANS` Agent 1 manager | `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/` | none | complete proposal packet, patch SHA, check evidence, blocker state | fresh semantic review; patch applies without changing `AGENTS.md` |
| N2 | bounded ephemeral-generalist Agent 2 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/` | N1 accepted by HELP_HUMAN | complete preparation package referencing N1 patch SHA, validator evidence, blocked handoff | manifest validates; SOW and status bytes unchanged |
| N3 | `SCOPE_CHANGE` Agent 1 manager, with nested `AUDIT_DEP_CLOSURE` Agent 2 | `execution/_ScopeChange/SCA-004_2026-08-22_1749/` and `execution/_Coordination/NOTICE_2026-08-22_ROOT_SCA-004_V3_RELEASE_PATHWAY_DAG.md` | none; nested audit depends on draft graph | Gate-1 assessment, graph, audit return, four-state handoff, routed notice | graph resolves and parses; audit return has verdict; `_LATEST.md` unchanged |

Every node may also write its immutable control-plane records below its own
`instances/<NODE>/` folder. Content write sets are otherwise disjoint and may
not widen. N1 precedes N2. N3 may run concurrently with N1/N2 but cannot close
until its nested audit has returned.

## Human decision points and holds

- D-GOV-35 remains `PROPOSED — AWAITING OWNER RULING`.
- SCA-004 remains `AWAITING_OWNER_ACCEPTANCE`; Gate 2 and all later gates are
  closed.
- The instruction application tranche remains blocked on the D-GOV-35 ruling.
- All ten DEL-02-06 `HELD_UNAVAILABLE` bindings remain held.
- The G1 pin blockers remain TM-ROOT-106 and TM-ROOT-122; no pin amendment is
  authorized here.
- Sync/rebase, artifact download, implementation, foreign-loop writes,
  lifecycle change, merge, and every not-selectable surface remain prohibited.

## Failure and supervision

Unlimited bounded repair and fresh re-review apply. A node that cannot meet
its contract records blockers in its return/handoff without narrowing or
widening silently. HELP_HUMAN accepts only validated returns, commits accepted
node content in N1 → N2 → N3 order, performs byte-level fan-in checks, and
then routes Git publication through CHANGE semantics without merge.

## Version 2 amendment

N1 fresh review exposed an incompatible pair of mechanical requirements: Git
does not accept a conventional zero-context unified hunk through the literal
default `git apply --check`, while the owner requires both. This does not
change proposed `AGENTS.md` semantics or any write/authority gate. For N1
acceptance, the literal executable check controls; the patch must use the
minimum unchanged anchors Git requires, all within the named section, carry
zero context outside it, and minimize changed lines rather than replacing the
whole section. The exact rationale and repair contract are frozen at
`amendments/N1/2.md`.

## Version 3 amendment

N3 fresh review found that the Gate-1 assessment omitted SCOPE_CHANGE's
mandatory SOFTWARE pre-change `AUDIT_DECOMP` baseline and used an invalid
aggregate `AuditState` value. N3 must dispatch a fresh bounded read-only
`AUDIT_DECOMP` under the same owner-narrowed SCA-folder evidence override,
integrate its coverage summary without opening Gate 2, and use the fixed
four-state enum. The repair contract is frozen at `amendments/N3/2.md`.
