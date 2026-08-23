# Sealed Child Brief — D-GOV-35 ruled record and proposal-packet disposition

InstanceID: `DGOV35_RECORD_PACKET`
Parent: `N1_DGOV35_M2_APPLICATION` (`HELPS_HUMANS`)
AgentType: `2 — ephemeral bounded generalist`
Delegation: `PROHIBITED — do not spawn or delegate`
Basis: `b143444bd497eae1b1b638670a33e6df756d9084`
WorkingRoot: repository root

## Objective

Implement only the ruled D-GOV-35 decision-record subpackage from N1 of the
Phase-0b steer: mint the decision record, add its one register row, and mark
the proposal packet ruled while preserving all packet bytes not expressly
authorized to change.

## Required reads

Read completely before editing:

- `AGENTS.md` (Agent-2 non-delegation and evidence rules);
- `agents/AGENT_TASK.md` (Agent-2 bounded execution contract; no skill is
  loaded for this heterogeneous one-off task);
- `plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md`;
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`;
- all four files in
  `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/`;
- `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md`;
- `docs/governance_harness/_DECISIONS/_REGISTER.md`; and
- parent brief
  `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0B_2026-08-22/instances/N1_DGOV35_M2_APPLICATION/LAUNCH_BRIEF.md`.

## Authorized writes — exact whitelist

1. `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` (new)
2. `docs/governance_harness/_DECISIONS/_REGISTER.md` (one D-GOV-35 row only)
3. `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/README.md`
4. `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/D-GOV-35.proposed.md`
5. This child folder's `RETURN.md` and `STATUS.json`

No other write is authorized. Do not commit, push, merge, edit `AGENTS.md`,
edit the manifest, or edit any other run folder.

## Content contract

- Follow the D-GOV-34 record convention exactly where applicable.
- Decision header must state:
  `Status: RULED — APPLICATION TRANCHE PREPARED; PUBLICATION PENDING`,
  Date `2026-08-22`, this Phase-0b run as FramedBy, AcceptedBasis
  `main@abf3c1bf5996cd9333ad706df14e62df32fbbf0f`, Supersedes D-GOV-14
  item 7's exclusivity sentence only, and CandidateSHA / PublicationSHA /
  EffectiveSHA `TBD`.
- `HumanRuling` must faithfully carry R1-A: `[click] "Approve as proposed"`
  plus its complete recorded form. Include the eight ruled items copied from
  the proposal without semantic alteration. Record that the three named
  concordance sentences are disposed by this same N1 application tranche.
- Add exactly one D-GOV-35 row in the register's existing row form.
- Append the exact status line
  `RULED 2026-08-22 — see \`_DECISIONS/D-GOV-35_delegated_harness_native_class.md\``
  to `README.md` and `D-GOV-35.proposed.md`, pointing unambiguously at the
  decision record. Preserve the remaining packet bytes. In `README.md`,
  update only the SHA table entries for the two changed packet files, using
  the existing normalized self-hash convention for the README row.

## Acceptance checks

- `git diff --check` passes for the five content paths.
- Register diff is one row only.
- Proposal diff is append-only status line; README diff is append-only status
  line plus the two required SHA-table changes.
- Decision record includes all eight numbered ruled items and complete R1-A
  recorded form.
- Return exact changed-path SHA-256 values and a concise diff summary in
  `RETURN.md`; end with terminal `STATUS.json` using status `COMPLETE` or
  `BLOCKED` and name any blocker without widening scope.
